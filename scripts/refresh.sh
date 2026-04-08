#!/usr/bin/env bash
# Pull latest Atlas main branch, rebuild the index, and check for unprocessed PRs.
# NOTE: This script is run by the SessionStart hook. It must always exit 0
# so the hook doesn't report a failure — the PR check is advisory, not critical.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
REPO_DIR="$PROJECT_DIR/.atlas-repo"
LOG_FILE="$PROJECT_DIR/history/_log.md"

if [ ! -d "$REPO_DIR/.git" ]; then
    echo "Error: Atlas repo not found. Run scripts/setup.sh first."
    exit 1
fi

# Clear ephemeral working files from previous session
rm -f "$PROJECT_DIR"/tmp/pr-*.diff "$PROJECT_DIR"/tmp/pr-*-body.md 2>/dev/null

echo "Fetching latest Atlas..."
cd "$REPO_DIR"
git fetch origin main --depth 1 || { echo "ERROR: Failed to fetch from GitHub."; exit 0; }
git reset --hard origin/main || { echo "ERROR: Failed to reset to origin/main."; exit 0; }

# Verify local matches remote
LOCAL_HEAD=$(git rev-parse HEAD)
REMOTE_HEAD=$(git ls-remote origin main 2>/dev/null | cut -f1)
LATEST_COMMIT=$(git log --oneline -1)
cd "$PROJECT_DIR"

if [ "$LOCAL_HEAD" = "$REMOTE_HEAD" ]; then
    echo "Atlas synced with GitHub: $LATEST_COMMIT"
else
    echo "WARNING: Local ($LOCAL_HEAD) does not match remote ($REMOTE_HEAD)."
    echo "The local Atlas may be out of date. Try running this script again."
fi

echo "Rebuilding index..."
python3 "$SCRIPT_DIR/build-index.py"

# --- Check for unprocessed merged PRs ---
echo ""
echo "Checking for unprocessed PRs..."

# Determine the last processed merge date from _log.md to scope the GitHub query.
# Log format: | #217 | Title | 2026-04-02 | entities |
LAST_MERGED_DATE=$(grep -E '^\| #[0-9]+ ' "$LOG_FILE" 2>/dev/null \
    | sed -E 's/.*\| ([0-9]{4}-[0-9]{2}-[0-9]{2}) \|.*/\1/' \
    | sort -r | head -1)

if [ -n "$LAST_MERGED_DATE" ]; then
    echo "Last processed PR was merged on $LAST_MERGED_DATE. Checking for newer PRs..."
    MERGED_PRS=$(gh pr list --repo sky-ecosystem/next-gen-atlas --state merged \
        --search "merged:>=$LAST_MERGED_DATE" --limit 30 \
        --json number,title,mergedAt \
        --jq '.[] | "\(.number)\t\(.mergedAt[:10])\t\(.title)"' 2>/dev/null) || {
        echo "Warning: Could not fetch PR list from GitHub. Skipping unprocessed PR check."
        exit 0
    }
else
    echo "No previously processed PRs found. Fetching last 30 merged PRs..."
    MERGED_PRS=$(gh pr list --repo sky-ecosystem/next-gen-atlas --state merged --limit 30 \
        --json number,title,mergedAt \
        --jq '.[] | "\(.number)\t\(.mergedAt[:10])\t\(.title)"' 2>/dev/null) || {
        echo "Warning: Could not fetch PR list from GitHub. Skipping unprocessed PR check."
        exit 0
    }
fi

# Find which ones we haven't processed
UNPROCESSED=""
UNPROCESSED_COUNT=0

while IFS=$'\t' read -r pr_num merged_date title; do
    [ -z "$pr_num" ] && continue
    # Check if this PR is already in our log
    if ! grep -q "| #$pr_num " "$LOG_FILE" 2>/dev/null; then
        UNPROCESSED+="  #$pr_num ($merged_date) — $title"$'\n'
        UNPROCESSED_COUNT=$((UNPROCESSED_COUNT + 1))
    fi
done <<< "$MERGED_PRS"

if [ "$UNPROCESSED_COUNT" -eq 0 ]; then
    echo "All recent merged PRs have been processed."
else
    echo ""
    echo "=== $UNPROCESSED_COUNT UNPROCESSED MERGED PR(s) ==="
    echo "The following PRs have been merged but not yet recorded in history/:"
    echo ""
    echo "$UNPROCESSED"
    echo "Run: bash scripts/process-pr.sh <number(s)> to process them."
    echo "Then review and fill in the Context sections in the affected changelogs."
fi

# --- Refresh forum cache (background, non-blocking) ---
if [ -f "$SCRIPT_DIR/fetch-forum.sh" ]; then
    bash "$SCRIPT_DIR/fetch-forum.sh" --quiet 2>/dev/null &
fi

exit 0
