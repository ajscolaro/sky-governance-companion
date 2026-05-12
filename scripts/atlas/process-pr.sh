#!/usr/bin/env bash
# Analyze a merged PR and append structured entries to the relevant history changelogs.
# Usage: process-pr.sh [--dry-run] [--force] <PR-number> [<PR-number> ...]
#
# Pipeline (one PR at a time):
#   1. classify-diff.py   → tmp/pr-<N>-manifest.json   (per-doc add/delete/modify/rename)
#   2. extract-values.py  → tmp/pr-<N>-extracted.json  (numerics, addresses, sweeps)
#   3. enrich.py          → tmp/pr-<N>-enriched.json   (poll/spell, routing, type label)
#   4. render.py          → tmp/pr-<N>-rendered.json   (per-entity markdown entries)
#   5. auto-context.py    → tmp/pr-<N>-final.json      (Context filled by `claude -p`,
#                                                       or passthrough if ATLAS_AUTO_CONTEXT=0)
#   6. verify-entry.py    → exit non-zero if the entry doesn't account for every changed UUID
#   7. Append entry to history/<entity>/changelog.md, update history/_log.md
#
# Flags:
#   --dry-run   Run pipeline but do not modify any history/* files (prints rendered entries)
#   --force     Re-process even if PR is already in history/_log.md (overwrites prior entry)
#
# Env vars (all optional):
#   ATLAS_AUTO_CONTEXT=0          Skip the LLM Context-fill step
#   ATLAS_AUTO_CONTEXT_MODEL=...  Override model passed to `claude -p`
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
INDEX="$PROJECT_DIR/data/index.json"
HISTORY_DIR="$PROJECT_DIR/history"
LOG_FILE="$HISTORY_DIR/_log.md"
ATLAS_REPO_DIR="$PROJECT_DIR/.atlas-repo"

if [ ! -f "$INDEX" ]; then
    echo "Error: Index not found. Run scripts/setup.sh first." >&2
    exit 1
fi

DRY_RUN=0
FORCE=0
FROM_TMP=0
PR_ARGS=()
for arg in "$@"; do
    case "$arg" in
        --dry-run)  DRY_RUN=1 ;;
        --force)    FORCE=1 ;;
        --from-tmp) FROM_TMP=1 ;;  # use cached tmp/pr-<N>.diff + meta (testing)
        --) ;;
        -h|--help)
            sed -n '2,/^set -euo pipefail$/p' "$0" | sed 's/^# \{0,1\}//' >&2
            exit 0
            ;;
        *) PR_ARGS+=("$arg") ;;
    esac
done

if [ ${#PR_ARGS[@]} -eq 0 ]; then
    echo "Usage: process-pr.sh [--dry-run] [--force] <PR-number> [<PR-number> ...]" >&2
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

# Locate a PR's merge commit in the local atlas-repo. next-gen-atlas
# squash-merges PRs with the title suffix " (#N)", so we grep commit subjects
# for that pattern. If the PR isn't in the shallow clone yet, deepen
# progressively (50 → 200 → 1000 → 5000 commits → unshallow).
find_pr_merge_sha() {
    local pr_num="$1"
    local sha
    sha=$(git -C "$ATLAS_REPO_DIR" log --all -E --grep="\\(#${pr_num}\\)$" --pretty=format:%H -n 1 2>/dev/null)
    [ -n "$sha" ] && { echo "$sha"; return 0; }

    for depth in 50 200 1000 5000; do
        git -C "$ATLAS_REPO_DIR" fetch origin main --depth "$depth" >/dev/null 2>&1 || break
        sha=$(git -C "$ATLAS_REPO_DIR" log --all -E --grep="\\(#${pr_num}\\)$" --pretty=format:%H -n 1 2>/dev/null)
        [ -n "$sha" ] && { echo "$sha"; return 0; }
    done

    git -C "$ATLAS_REPO_DIR" fetch --unshallow origin main >/dev/null 2>&1 || true
    sha=$(git -C "$ATLAS_REPO_DIR" log --all -E --grep="\\(#${pr_num}\\)$" --pretty=format:%H -n 1 2>/dev/null)
    [ -n "$sha" ] && { echo "$sha"; return 0; }
    return 1
}

# Ensure the merge commit's parent is present so `git diff sha~..sha` is meaningful.
# In a shallow clone (atlas-sync.sh defaults to depth=1) the parent isn't fetched,
# which would make `git show <sha>` return the entire tree as additions. Deepen
# by one if needed.
ensure_parent_available() {
    local sha="$1"
    if git -C "$ATLAS_REPO_DIR" rev-parse "$sha~" >/dev/null 2>&1; then
        return 0
    fi
    git -C "$ATLAS_REPO_DIR" fetch origin --deepen=10 >/dev/null 2>&1 || true
    git -C "$ATLAS_REPO_DIR" rev-parse "$sha~" >/dev/null 2>&1
}

for PR_NUM in "${PR_ARGS[@]}"; do
    # Check if already processed (unless --force)
    if [ "$FORCE" -eq 0 ] && grep -q "| #$PR_NUM " "$LOG_FILE" 2>/dev/null; then
        echo "PR #$PR_NUM already processed, skipping."
        continue
    fi

    echo "Processing PR #$PR_NUM..."
    TMP_DIR="$PROJECT_DIR/tmp"
    mkdir -p "$TMP_DIR"

    DIFF_FILE="$TMP_DIR/pr-${PR_NUM}.diff"
    META_FILE="$TMP_DIR/pr-${PR_NUM}-meta.json"

    if [ "$FROM_TMP" -eq 1 ]; then
        # Test path: skip git ops, expect cached diff + meta from a prior run.
        if [ ! -s "$DIFF_FILE" ] || [ ! -s "$META_FILE" ]; then
            echo "Error: --from-tmp requires both $DIFF_FILE and $META_FILE to exist" >&2
            continue
        fi
        TITLE=$(jq -r '.title' "$META_FILE")
        AUTHOR_DATE=$(jq -r '.merged_at' "$META_FILE")
        ADDITIONS=$(jq -r '.additions' "$META_FILE")
        DELETIONS=$(jq -r '.deletions' "$META_FILE")
        MERGED_DATE="${AUTHOR_DATE:0:10}"
        echo "  → Using cached diff + meta from tmp/"
    else
        # 1. Locate the PR's merge commit in the local atlas-repo
        if [ ! -d "$ATLAS_REPO_DIR/.git" ]; then
            echo "Error: .atlas-repo not found. Run scripts/core/setup.sh first." >&2
            continue
        fi
        MERGE_SHA=$(find_pr_merge_sha "$PR_NUM") || {
            echo "Error: PR #$PR_NUM not found in atlas-repo history (deepening exhausted)" >&2
            continue
        }
        echo "  → Found merge commit: ${MERGE_SHA:0:8}"

        if ! ensure_parent_available "$MERGE_SHA"; then
            echo "Error: parent of $MERGE_SHA not in shallow clone and could not deepen." >&2
            echo "       Run 'git -C .atlas-repo fetch --unshallow' from a shell with network access." >&2
            continue
        fi

        # 2. Extract metadata from the commit. next-gen-atlas squashes PRs so
        #    the commit subject is the PR title with " (#N)" appended; the body
        #    is the PR body verbatim.
        SUBJECT=$(git -C "$ATLAS_REPO_DIR" log --format=%s -n 1 "$MERGE_SHA")
        BODY=$(git -C "$ATLAS_REPO_DIR" log --format=%b -n 1 "$MERGE_SHA")
        AUTHOR_DATE=$(git -C "$ATLAS_REPO_DIR" log --format=%aI -n 1 "$MERGE_SHA")
        TITLE=$(echo "$SUBJECT" | sed -E "s/ \\(#${PR_NUM}\\)\$//")
        TITLE=$(sanitize "$TITLE")
        BODY=$(sanitize "$BODY")
        MERGED_DATE="${AUTHOR_DATE:0:10}"

        # 3. Build the unified diff and counts. Use `diff sha~..sha` rather
        #    than `show sha` so it works whether the parent is the immediate
        #    predecessor or a deepened ancestor.
        git -C "$ATLAS_REPO_DIR" diff --no-color "${MERGE_SHA}~..${MERGE_SHA}" > "$DIFF_FILE"
        SHORTSTAT=$(git -C "$ATLAS_REPO_DIR" diff --shortstat "${MERGE_SHA}~..${MERGE_SHA}")
        ADDITIONS=$(echo "$SHORTSTAT" | grep -oE '[0-9]+ insertion' | grep -oE '^[0-9]+' || echo 0)
        DELETIONS=$(echo "$SHORTSTAT" | grep -oE '[0-9]+ deletion' | grep -oE '^[0-9]+' || echo 0)
        [ -z "$ADDITIONS" ] && ADDITIONS=0
        [ -z "$DELETIONS" ] && DELETIONS=0
        echo "  → Diff: +${ADDITIONS}/-${DELETIONS} lines"

        # 4. Cache PR body + meta JSON (consumed by enrich.py)
        [ -n "$BODY" ] && echo "$BODY" > "$TMP_DIR/pr-${PR_NUM}-body.md"
        python3 - "$META_FILE" "$PR_NUM" "$TITLE" "$AUTHOR_DATE" "$ADDITIONS" "$DELETIONS" "$BODY" "$MERGE_SHA" <<'PYEOF'
import json, sys
out_path, pr, title, merged_at, adds, dels, body, sha = sys.argv[1:9]
json.dump({
    "number": int(pr), "title": title, "merged_at": merged_at,
    "additions": int(adds), "deletions": int(dels),
    "body": body, "merge_sha": sha,
}, open(out_path, "w"), indent=2)
PYEOF
    fi

    # 5. Stage 1 — classify-diff
    MANIFEST_FILE="$TMP_DIR/pr-${PR_NUM}-manifest.json"
    python3 "$SCRIPT_DIR/classify-diff.py" "$DIFF_FILE" > "$MANIFEST_FILE" || {
        echo "Error: classify-diff failed for PR #$PR_NUM" >&2
        continue
    }

    NEW_UUIDS=$(jq -r '.added[].uuid' "$MANIFEST_FILE")

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

    # 6. Stages 2-5: extract → enrich → render → context
    EXTRACTED_FILE="$TMP_DIR/pr-${PR_NUM}-extracted.json"
    ENRICHED_FILE="$TMP_DIR/pr-${PR_NUM}-enriched.json"
    RENDERED_FILE="$TMP_DIR/pr-${PR_NUM}-rendered.json"
    FINAL_FILE="$TMP_DIR/pr-${PR_NUM}-final.json"

    python3 "$SCRIPT_DIR/extract-values.py" "$DIFF_FILE" --manifest "$MANIFEST_FILE" \
        > "$EXTRACTED_FILE" || { echo "Error: extract-values failed for PR #$PR_NUM" >&2; continue; }

    python3 "$SCRIPT_DIR/enrich.py" --extracted "$EXTRACTED_FILE" --pr-meta "$META_FILE" \
        > "$ENRICHED_FILE" || { echo "Error: enrich failed for PR #$PR_NUM" >&2; continue; }

    python3 "$SCRIPT_DIR/render.py" --enriched "$ENRICHED_FILE" \
        > "$RENDERED_FILE" || { echo "Error: render failed for PR #$PR_NUM" >&2; continue; }

    # auto-context is best-effort — if the LLM call fails, fall back to passthrough
    if ! python3 "$SCRIPT_DIR/auto-context.py" --rendered "$RENDERED_FILE" > "$FINAL_FILE" 2>/dev/null; then
        echo "  → auto-context failed; using rendered output without Context paragraph"
        cp "$RENDERED_FILE" "$FINAL_FILE"
    fi

    # 7. Verify the rendered entry covers every changed UUID
    if ! python3 "$SCRIPT_DIR/verify-entry.py" --manifest "$MANIFEST_FILE" \
            --rendered "$FINAL_FILE" --enriched "$ENRICHED_FILE" >&2; then
        echo "Error: verify-entry reported missing UUIDs for PR #$PR_NUM" >&2
        continue
    fi

    # 8. Dry-run: print and stop
    if [ "$DRY_RUN" -eq 1 ]; then
        python3 - "$FINAL_FILE" <<'PYEOF'
import json, sys
r = json.load(open(sys.argv[1]))
print(f"\n[dry-run] PR #{r['pr_number']} ({r['type_label']}) — {len(r['entries'])} entit{'y' if len(r['entries'])==1 else 'ies'}\n")
for entity, text in r["entries"].items():
    print(f"=== {entity} ===")
    print(text)
    print()
PYEOF
        continue
    fi

    # 9. Write entries to changelogs (with --force, overwrite an existing
    #    matching block first so re-runs don't duplicate)
    AFFECTED=$(python3 - "$FINAL_FILE" "$HISTORY_DIR" "$PR_NUM" "$FORCE" <<'PYEOF'
import json, os, re, sys
final_path, history_dir, pr_num, force = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
r = json.load(open(final_path))
header_pat = re.compile(rf'^## PR #{re.escape(pr_num)}( |\n|$)')

affected = []
for entity, text in r["entries"].items():
    cl = os.path.join(history_dir, entity, "changelog.md")
    os.makedirs(os.path.dirname(cl), exist_ok=True)
    if not os.path.exists(cl):
        with open(cl, "w") as f:
            f.write(f"# {entity} — Change History\n\n---\n")
    existing = open(cl).read()

    # If --force, drop any prior entry block for this PR before appending
    if force:
        # Split on the standard --- separator that bounds entries
        parts = existing.split("\n---\n")
        kept = [p for p in parts if not header_pat.match(p.strip())]
        existing = "\n---\n".join(kept)
        with open(cl, "w") as f:
            f.write(existing.rstrip() + "\n")

    with open(cl, "a") as f:
        # Ensure exactly one blank line between prior content and the new entry
        if not existing.endswith("\n"):
            f.write("\n")
        f.write("\n" + text + "\n")
    affected.append(entity)

print(",".join(affected))
PYEOF
)
    if [ -z "$AFFECTED" ]; then
        echo "Warning: no entries were written for PR #$PR_NUM" >&2
        continue
    fi
    echo "  → Wrote entries to: $AFFECTED"

    # 10. Update _log.md (status=auto for fully-pipeline-generated entries)
    LOG_ENTITIES=$(echo "$AFFECTED" | tr ',' '\n' | sed 's|A\.[0-9.]*--||g; s|_other|other|g' | paste -sd ', ' -)
    if [ "$FORCE" -eq 1 ]; then
        # Drop any existing row for this PR
        grep -v "| #$PR_NUM " "$LOG_FILE" > "$LOG_FILE.tmp" && mv "$LOG_FILE.tmp" "$LOG_FILE"
    fi
    echo "| #$PR_NUM | $TITLE | $MERGED_DATE | $LOG_ENTITIES | auto |" >> "$LOG_FILE"
    echo "  → Updated $LOG_FILE"

    # 11. Re-sort all changelogs (most-recent-first)
    python3 "$PROJECT_DIR/scripts/core/sort-changelogs.py" >/dev/null 2>&1 || true

    echo "Done with PR #$PR_NUM."
    echo ""
done

echo "All PRs processed."
