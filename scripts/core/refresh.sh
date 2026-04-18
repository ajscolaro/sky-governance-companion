#!/usr/bin/env bash
# Refresh all cached data sources in parallel, auto-process unprocessed merged
# Atlas PRs, then emit the session briefing.
#
# Invoked by the /refresh skill (not the SessionStart hook). Atlas itself is
# synced by the SessionStart hook via scripts/core/atlas-sync.sh — this script
# does not re-sync the Atlas git repo or rebuild the index. If the user needs
# fresh Atlas commits mid-session, they should restart Claude to re-trigger
# the hook.
#
# Execution order:
#   1. Parallel: all data fetches + unprocessed-PR discovery
#   2. Wait for fetches
#   3. Auto-process unprocessed merged PRs (writes skeletons to history/)
#   4. Session briefing
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
LOG_FILE="$PROJECT_DIR/history/_log.md"
VOTING_DIR="$PROJECT_DIR/scripts/voting"
FORUM_DIR="$PROJECT_DIR/scripts/forum"
DELEGATES_DIR="$PROJECT_DIR/scripts/delegates"
MARKET_DIR="$PROJECT_DIR/scripts/market"
GITHUB_DIR="$PROJECT_DIR/scripts/github"
ATLAS_DIR="$PROJECT_DIR/scripts/atlas"

if [ ! -f "$PROJECT_DIR/data/index.json" ]; then
    echo "Error: Atlas index not found. Run scripts/core/setup.sh first (or restart Claude to trigger the SessionStart hook)."
    exit 1
fi

# Clear ephemeral working files from previous session
rm -f "$PROJECT_DIR"/tmp/pr-*.diff "$PROJECT_DIR"/tmp/pr-*-body.md 2>/dev/null

# === Phase 1: Refresh all data sources in parallel ===
echo "Refreshing data sources..."

if [ -f "$VOTING_DIR/fetch-voting-polls.sh" ]; then
    bash "$VOTING_DIR/fetch-voting-polls.sh" --quiet 2>/dev/null &
fi
if [ -f "$VOTING_DIR/fetch-voting-executive.sh" ]; then
    bash "$VOTING_DIR/fetch-voting-executive.sh" --quiet 2>/dev/null &
fi
if [ -f "$VOTING_DIR/fetch-executive-proposals.sh" ]; then
    bash "$VOTING_DIR/fetch-executive-proposals.sh" --quiet 2>/dev/null &
fi
if [ -f "$VOTING_DIR/fetch-voting-delegates.sh" ]; then
    bash "$VOTING_DIR/fetch-voting-delegates.sh" --quiet 2>/dev/null &
fi
if [ -f "$FORUM_DIR/fetch-forum.sh" ]; then
    bash "$FORUM_DIR/fetch-forum.sh" --quiet 2>/dev/null &
fi
if [ -f "$DELEGATES_DIR/fetch-delegates.sh" ]; then
    bash "$DELEGATES_DIR/fetch-delegates.sh" --quiet 2>/dev/null &
fi
if [ -f "$MARKET_DIR/fetch-market.py" ]; then
    python3 "$MARKET_DIR/fetch-market.py" --quiet 2>/dev/null &
fi
if [ -f "$GITHUB_DIR/fetch-open-prs.sh" ]; then
    bash "$GITHUB_DIR/fetch-open-prs.sh" --quiet 2>/dev/null &
fi

# Discover unprocessed merged PRs (write numbers to file for Phase 3)
UNPROCESSED_FILE=$(mktemp "${TMPDIR:-/tmp}/unprocessed-prs.XXXXXX")
(
    LAST_MERGED_DATE=$(grep -E '^\| #[0-9]+ ' "$LOG_FILE" 2>/dev/null \
        | sed -E 's/.*\| ([0-9]{4}-[0-9]{2}-[0-9]{2}) \|.*/\1/' \
        | sort -r | head -1)

    GH_API="https://api.github.com/repos/sky-ecosystem/next-gen-atlas"

    if [ -n "$LAST_MERGED_DATE" ]; then
        MERGED_PRS=$(curl -sf "$GH_API/pulls?state=closed&sort=updated&direction=desc&per_page=30" \
            | jq -r --arg since "$LAST_MERGED_DATE" \
                '.[] | select(.merged_at != null and .merged_at >= $since) | .number' 2>/dev/null) || exit 0
    else
        MERGED_PRS=$(curl -sf "$GH_API/pulls?state=closed&sort=updated&direction=desc&per_page=30" \
            | jq -r '.[] | select(.merged_at != null) | .number' 2>/dev/null) || exit 0
    fi

    while IFS= read -r pr_num; do
        [ -z "$pr_num" ] && continue
        if ! grep -q "| #$pr_num " "$LOG_FILE" 2>/dev/null; then
            echo "$pr_num" >> "$UNPROCESSED_FILE"
        fi
    done <<< "$MERGED_PRS"
) &

# === Phase 2: Wait for everything to finish ===
wait

# === Phase 3: Auto-process unprocessed merged PRs ===
# Writes skeleton entries to history/<entity>/changelog.md and updates _log.md.
# Claude should follow up with /atlas-track + /atlas-analyze to rewrite
# skeletons into Material/Housekeeping sections (see CLAUDE.md).
if [ -s "$UNPROCESSED_FILE" ]; then
    PR_NUMS=$(tr '\n' ' ' < "$UNPROCESSED_FILE")
    echo ""
    echo "Auto-processing merged PRs: $PR_NUMS"
    bash "$ATLAS_DIR/process-pr.sh" $PR_NUMS || true
fi
rm -f "$UNPROCESSED_FILE"

# === Phase 3b: Surface any skeleton PRs awaiting finalization ===
# Catches both just-auto-processed PRs and any lingering skeletons from prior
# sessions where Claude didn't follow through with /atlas-track. Capped at the
# most recently added 5 (by _log.md position); any larger backlog is legacy
# debt the user should batch-clean manually rather than auto-finalize.
ALL_SKELETON_LINES=$(grep -E '^\| #[0-9]+ .* \| skeleton \|' "$LOG_FILE" 2>/dev/null || true)
if [ -n "$ALL_SKELETON_LINES" ]; then
    TOTAL_SKELETONS=$(printf '%s\n' "$ALL_SKELETON_LINES" | grep -c '^| #')
    RECENT_SKELETONS=$(printf '%s\n' "$ALL_SKELETON_LINES" | tail -5 \
        | sed -E 's/^\| #([0-9]+) .*/\1/' | tr '\n' ' ' | sed 's/ $//')
    echo ""
    if [ "$TOTAL_SKELETONS" -le 5 ]; then
        echo "Skeleton PRs awaiting finalization: $RECENT_SKELETONS"
    else
        echo "Skeleton PRs awaiting finalization (5 most recent of $TOTAL_SKELETONS): $RECENT_SKELETONS"
    fi
fi

# === Phase 4: Session briefing ===
echo ""
if [ -f "$SCRIPT_DIR/session-briefing.py" ]; then
    python3 "$SCRIPT_DIR/session-briefing.py" 2>/dev/null || true
fi

exit 0
