#!/usr/bin/env bash
# Analyze a merged PR and append structured entries to the relevant history changelogs.
# Usage: process-pr.sh <PR-number> [<PR-number> ...]
#
# For each PR:
# 1. Fetches PR metadata and diff via gh CLI
# 2. Identifies which documents were added/modified/deleted (by UUID)
# 3. Groups changes by entity subtree
# 4. Appends a skeleton entry to each affected changelog
# 5. Updates history/_log.md
#
# The skeleton includes the structural changes; interpretive context
# should be added by the agent reviewing the output.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
INDEX="$PROJECT_DIR/data/index.json"
HISTORY_DIR="$PROJECT_DIR/history"
LOG_FILE="$HISTORY_DIR/_log.md"
REPO="sky-ecosystem/next-gen-atlas"
GH_API="https://api.github.com/repos/$REPO"

if [ ! -f "$INDEX" ]; then
    echo "Error: Index not found. Run scripts/setup.sh first." >&2
    exit 1
fi

if [ $# -eq 0 ]; then
    echo "Usage: process-pr.sh <PR-number> [<PR-number> ...]" >&2
    exit 1
fi

# Sanitize external text before writing to history files.
# Strips HTML comments/tags, system-prompt-like markers, and XML-style tags
# that could be used for prompt injection when the agent reads changelogs.
sanitize() {
    local input="$1"
    # Remove HTML comments (could hide injected instructions)
    input=$(echo "$input" | sed -E 's/<!--[^>]*-->//g')
    # Remove XML-style tags (e.g., <system>, <instructions>)
    input=$(echo "$input" | sed -E 's/<[\/]?[a-zA-Z][^>]*>//g')
    # Remove common prompt injection markers
    input=$(echo "$input" | sed -E 's/\[SYSTEM\]//gI; s/\[INST\]//gI; s/\[\/INST\]//gI')
    # Remove ChatML-style markers (<|...|>)
    input=$(echo "$input" | sed -E 's/<\|[^|]*\|>//g')
    # Remove control characters (except newline and tab)
    input=$(echo "$input" | tr -d '\000-\010\013-\037')
    echo "$input"
}

# Entity routing: map document number prefixes to history directories.
# Uses a routing file so new entities can be added without editing this script.
ROUTING_FILE="$PROJECT_DIR/history/entity-routing.conf"

route_to_entity() {
    local number="$1"
    # Read routing file: each line is "prefix<TAB>directory-name"
    # Lines are checked in order; first match wins (most specific prefixes first)
    if [ -f "$ROUTING_FILE" ]; then
        while IFS=$'\t' read -r prefix dirname || [ -n "$prefix" ]; do
            [[ "$prefix" =~ ^#.*$ || -z "$prefix" ]] && continue
            if [[ "$number" == "$prefix"* ]]; then
                echo "$dirname"
                return
            fi
        done < "$ROUTING_FILE"
    fi
    echo "_other"
}

for PR_NUM in "$@"; do
    # Check if already processed
    if grep -q "| #$PR_NUM " "$LOG_FILE" 2>/dev/null; then
        echo "PR #$PR_NUM already processed, skipping."
        continue
    fi

    echo "Processing PR #$PR_NUM..."

    # Fetch PR metadata via REST API (no auth needed for public repos)
    PR_JSON=$(curl -sf "$GH_API/pulls/$PR_NUM" 2>/dev/null) || {
        echo "Error: Could not fetch PR #$PR_NUM" >&2
        continue
    }

    TITLE=$(sanitize "$(echo "$PR_JSON" | jq -r '.title')")
    MERGED_AT=$(echo "$PR_JSON" | jq -r '.merged_at // "not merged"')
    ADDITIONS=$(echo "$PR_JSON" | jq -r '.additions')
    DELETIONS=$(echo "$PR_JSON" | jq -r '.deletions')
    BODY=$(echo "$PR_JSON" | jq -r '.body // ""')

    if [ "$MERGED_AT" = "not merged" ] || [ "$MERGED_AT" = "null" ]; then
        echo "Warning: PR #$PR_NUM is not merged. Processing anyway for analysis."
    fi

    MERGED_DATE="${MERGED_AT:0:10}"

    # Save PR body to tmp/ for use during rewrite
    TMP_DIR="$PROJECT_DIR/tmp"
    mkdir -p "$TMP_DIR"
    if [ -n "$BODY" ]; then
        echo "$BODY" > "$TMP_DIR/pr-${PR_NUM}-body.md"
        echo "  → Saved PR body to tmp/pr-${PR_NUM}-body.md"
    fi

    # Fetch the diff and save to tmp/
    DIFF=$(curl -sf -H "Accept: application/vnd.github.v3.diff" "$GH_API/pulls/$PR_NUM" 2>/dev/null) || {
        echo "Error: Could not fetch diff for PR #$PR_NUM" >&2
        continue
    }
    echo "$DIFF" > "$TMP_DIR/pr-${PR_NUM}.diff"
    echo "  → Saved diff to tmp/pr-${PR_NUM}.diff"

    # Parse diff to find changed documents
    # Extract UUIDs from added (+) and removed (-) title lines
    ADDED_UUIDS=$(echo "$DIFF" | grep -E '^\+.*<!-- UUID:' | sed -E 's/.*UUID: ([a-f0-9-]{36}).*/\1/' | sort -u || true)
    REMOVED_UUIDS=$(echo "$DIFF" | grep -E '^\-.*<!-- UUID:' | sed -E 's/.*UUID: ([a-f0-9-]{36}).*/\1/' | sort -u || true)

    # Classify: new (added only), deleted (removed only), modified (both)
    NEW_UUIDS=$(comm -23 <(echo "$ADDED_UUIDS") <(echo "$REMOVED_UUIDS") 2>/dev/null || true)
    DELETED_UUIDS=$(comm -23 <(echo "$REMOVED_UUIDS") <(echo "$ADDED_UUIDS") 2>/dev/null || true)
    MODIFIED_UUIDS=$(comm -12 <(echo "$ADDED_UUIDS") <(echo "$REMOVED_UUIDS") 2>/dev/null || true)

    # Collect changes grouped by entity
    declare -A ENTITY_CHANGES

    # Build UUID → name maps from diff title lines, for both removed (-) and added (+).
    # Used to (a) recover info for deleted docs not in current index, and
    # (b) detect renames (same UUID, different name in - vs + heading).
    declare -A DIFF_DOC_INFO
    declare -A DIFF_DOC_OLD_NAME
    declare -A DIFF_DOC_NEW_NAME
    while IFS= read -r line; do
        if [[ "$line" =~ ^-[#]+\ (A\.[^ ]+|NR-[0-9]+)\ -\ (.+)\ \[([^\]]+)\].*UUID:\ ([a-f0-9-]{36}) ]]; then
            local_uuid="${BASH_REMATCH[4]}"
            DIFF_DOC_INFO[$local_uuid]="${BASH_REMATCH[1]}	${BASH_REMATCH[2]}	${BASH_REMATCH[3]}"
            DIFF_DOC_OLD_NAME[$local_uuid]="${BASH_REMATCH[2]}"
        elif [[ "$line" =~ ^\+[#]+\ (A\.[^ ]+|NR-[0-9]+)\ -\ (.+)\ \[([^\]]+)\].*UUID:\ ([a-f0-9-]{36}) ]]; then
            DIFF_DOC_NEW_NAME[${BASH_REMATCH[4]}]="${BASH_REMATCH[2]}"
        fi
    done <<< "$DIFF"

    # Detect renames: UUID present in both +/- title lines with different names.
    declare -A RENAMED_UUIDS
    for uuid in $MODIFIED_UUIDS; do
        [ -z "$uuid" ] && continue
        old_n="${DIFF_DOC_OLD_NAME[$uuid]:-}"
        new_n="${DIFF_DOC_NEW_NAME[$uuid]:-}"
        if [ -n "$old_n" ] && [ -n "$new_n" ] && [ "$old_n" != "$new_n" ]; then
            RENAMED_UUIDS[$uuid]="${old_n}|||${new_n}"
        fi
    done

    # Auto-add routing for new agent-level Core docs (A.6.1.1.X).
    # A new Prime/Launch Agent's artifact shows up as an "Added" Core doc at this
    # depth. Without an explicit routing entry it falls through to the scope-level
    # changelog — detect and scaffold the dedicated entity directory instead.
    for uuid in $NEW_UUIDS; do
        [ -z "$uuid" ] && continue
        agent_info=$(jq -r --arg uuid "$uuid" '.[] | select(.uuid == $uuid) | "\(.number)\t\(.name)\t\(.type)"' "$INDEX" 2>/dev/null)
        [ -z "$agent_info" ] && continue
        agent_number=$(echo "$agent_info" | cut -f1)
        agent_name=$(echo "$agent_info" | cut -f2)
        agent_type=$(echo "$agent_info" | cut -f3)
        if [[ "$agent_number" =~ ^A\.6\.1\.1\.[0-9]+$ ]] && [ "$agent_type" = "Core" ]; then
            if ! grep -qE "^${agent_number}\b" "$ROUTING_FILE"; then
                PROJECT_DIR="$PROJECT_DIR" ROUTING_FILE="$ROUTING_FILE" \
                AGENT_NUMBER="$agent_number" AGENT_NAME="$agent_name" \
                python3 - <<'PYEOF'
import os, re, sys
routing_file = os.environ['ROUTING_FILE']
number = os.environ['AGENT_NUMBER']
name = os.environ['AGENT_NAME']
slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-') or 'new-agent'
dirname = f'A.6--agents/{number}--{slug}'
new_line = f'{number}\t{dirname}'
with open(routing_file) as f:
    lines = [l.rstrip('\n') for l in f]
# Find the A.6.1.1.X block; collect, add new entry, sort numerically, replace
def num_key(n):
    return tuple(int(p) for p in n.split('.')[1:])
block_start = block_end = None
for i, l in enumerate(lines):
    if l.startswith('A.6.1.1.'):
        if block_start is None:
            block_start = i
        block_end = i
if block_start is None:
    # No existing block; insert before first A.6 scope line
    for i, l in enumerate(lines):
        if re.match(r'^A\.[0-9]\t', l):
            lines.insert(i, new_line)
            break
    else:
        lines.append(new_line)
else:
    block = lines[block_start:block_end+1]
    block.append(new_line)
    block.sort(key=lambda x: num_key(x.split('\t')[0]))
    lines[block_start:block_end+1] = block
with open(routing_file, 'w') as f:
    f.write('\n'.join(lines) + '\n')
# Create the directory with a stub changelog
project_dir = os.environ['PROJECT_DIR']
full_dir = os.path.join(project_dir, 'history', dirname)
os.makedirs(full_dir, exist_ok=True)
cl = os.path.join(full_dir, 'changelog.md')
if not os.path.exists(cl):
    with open(cl, 'w') as f:
        f.write(f'# {name} — Change History\n\nAtlas path: `{number}`\n\n---\n')
print(f'  → Auto-created routing: {number} → {dirname}', file=sys.stderr)
PYEOF
            fi
        fi
    done

    add_change() {
        local uuid="$1" change_type="$2"
        # Look up document in index
        local doc_info
        doc_info=$(jq -r --arg uuid "$uuid" '.[] | select(.uuid == $uuid) | "\(.number)\t\(.name)\t\(.type)"' "$INDEX" 2>/dev/null)

        if [ -z "$doc_info" ]; then
            # Try the diff-extracted info for deleted docs
            doc_info="${DIFF_DOC_INFO[$uuid]:-}"
        fi
        if [ -z "$doc_info" ]; then
            doc_info="???\tUnknown (UUID: ${uuid:0:8}...)\t?"
        fi

        local number name doc_type entity
        number=$(echo "$doc_info" | cut -f1)
        name=$(sanitize "$(echo "$doc_info" | cut -f2)")
        doc_type=$(echo "$doc_info" | cut -f3)
        entity=$(route_to_entity "$number")

        # Renamed: include old → new in the label so finalization can't miss it.
        if [ "$change_type" = "Renamed" ]; then
            local old_n new_n
            old_n=$(sanitize "${DIFF_DOC_OLD_NAME[$uuid]:-?}")
            new_n=$(sanitize "${DIFF_DOC_NEW_NAME[$uuid]:-$name}")
            ENTITY_CHANGES[$entity]+="- **Renamed** \`$number\` - \"$old_n\" → \"$new_n\" [$doc_type]
"
        else
            ENTITY_CHANGES[$entity]+="- **${change_type}** \`$number\` - $name [$doc_type]
"
        fi
    }

    for uuid in $NEW_UUIDS; do [ -n "$uuid" ] && add_change "$uuid" "Added"; done
    for uuid in $DELETED_UUIDS; do [ -n "$uuid" ] && add_change "$uuid" "Deleted"; done
    for uuid in $MODIFIED_UUIDS; do
        [ -z "$uuid" ] && continue
        if [ -n "${RENAMED_UUIDS[$uuid]:-}" ]; then
            add_change "$uuid" "Renamed"
        else
            add_change "$uuid" "Modified"
        fi
    done

    # Also count lines changed in non-title-line content (rough measure of substantive changes)
    CONTENT_ADDS=$(echo "$DIFF" | grep -c '^\+[^+]' || true)
    CONTENT_DELS=$(echo "$DIFF" | grep -c '^\-[^-]' || true)

    # Write to each affected entity's changelog
    AFFECTED_ENTITIES=""
    for entity in "${!ENTITY_CHANGES[@]}"; do
        CHANGELOG="$HISTORY_DIR/$entity/changelog.md"
        mkdir -p "$(dirname "$CHANGELOG")"

        # Create changelog if it doesn't exist
        if [ ! -f "$CHANGELOG" ]; then
            echo "# ${entity} — Change History" > "$CHANGELOG"
            echo "" >> "$CHANGELOG"
            echo "---" >> "$CHANGELOG"
        fi

        cat >> "$CHANGELOG" << ENTRY

## PR #$PR_NUM — $TITLE
**Merged:** $MERGED_DATE | **+$ADDITIONS/-$DELETIONS lines**

### Raw Changes (rewrite with /atlas-track)
${ENTITY_CHANGES[$entity]}
<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---
ENTRY

        echo "  → Updated $CHANGELOG"
        AFFECTED_ENTITIES+="$entity, "
    done

    # Clean up trailing comma
    AFFECTED_ENTITIES="${AFFECTED_ENTITIES%, }"

    # Format affected entities for log (strip prefix paths, just show names)
    LOG_ENTITIES=$(echo "$AFFECTED_ENTITIES" | sed 's/A\.[0-9.]*--//g; s/_other/other/g')

    # Append to master log (status = skeleton until rewritten via /atlas-track)
    echo "| #$PR_NUM | $TITLE | $MERGED_DATE | $LOG_ENTITIES | skeleton |" >> "$LOG_FILE"
    echo "  → Updated $LOG_FILE"

    # Clean up associative array for next PR
    unset ENTITY_CHANGES
    declare -A ENTITY_CHANGES

    echo "Done with PR #$PR_NUM."
    echo ""
done

echo "All PRs processed."
