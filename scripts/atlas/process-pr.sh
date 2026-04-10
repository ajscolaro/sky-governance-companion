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

    # Build a lookup of deleted docs from diff removed lines (for docs not in current index)
    declare -A DIFF_DOC_INFO
    while IFS= read -r line; do
        if [[ "$line" =~ ^-.*UUID:\ ([a-f0-9-]{36}) ]]; then
            local_uuid="${BASH_REMATCH[1]}"
            # Extract doc number, name, type from the removed line
            if [[ "$line" =~ ^-[#]+\ (A\.[^ ]+|NR-[0-9]+)\ -\ (.+)\ \[([^\]]+)\] ]]; then
                DIFF_DOC_INFO[$local_uuid]="${BASH_REMATCH[1]}	${BASH_REMATCH[2]}	${BASH_REMATCH[3]}"
            fi
        fi
    done <<< "$DIFF"

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

        ENTITY_CHANGES[$entity]+="- **${change_type}** \`$number\` - $name [$doc_type]
"
    }

    for uuid in $NEW_UUIDS; do [ -n "$uuid" ] && add_change "$uuid" "Added"; done
    for uuid in $DELETED_UUIDS; do [ -n "$uuid" ] && add_change "$uuid" "Deleted"; done
    for uuid in $MODIFIED_UUIDS; do [ -n "$uuid" ] && add_change "$uuid" "Modified"; done

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
