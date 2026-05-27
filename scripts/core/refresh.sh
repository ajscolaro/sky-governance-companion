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
#   3. Auto-process unprocessed merged PRs (full pipeline → fully-rendered
#      entries in history/, status=auto)
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
    echo "Error: Atlas index not found — first-time setup is incomplete."
    echo ""
    echo "  1. Exit Claude (/exit or Ctrl+C twice)"
    echo "  2. Run from your shell: bash scripts/core/setup.sh"
    echo "  3. Restart Claude, then re-run /refresh"
    echo ""
    echo "(setup.sh cannot run via the \`!\` prefix — the sandbox denies .atlas-repo writes.)"
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
if [ -f "$FORUM_DIR/build-account-registry.py" ]; then
    python3 "$FORUM_DIR/build-account-registry.py" --quiet 2>/dev/null &
fi
if [ -f "$DELEGATES_DIR/fetch-delegates.sh" ]; then
    # --rebuild-roster on every refresh so new ADs added to Atlas A.1.5.1.5.0.6.1
    # propagate into data/delegates/roster.json (and subsequent RSS fetches). Without
    # this flag, fetch-delegates.py only rebuilds when roster.json is missing.
    bash "$DELEGATES_DIR/fetch-delegates.sh" --quiet --rebuild-roster 2>/dev/null &
fi
if [ -f "$MARKET_DIR/fetch-market.py" ]; then
    python3 "$MARKET_DIR/fetch-market.py" --quiet 2>/dev/null &
fi
if [ -f "$GITHUB_DIR/fetch-open-prs.sh" ]; then
    bash "$GITHUB_DIR/fetch-open-prs.sh" --quiet 2>/dev/null &
fi

# Discover unprocessed merged PRs (write numbers to file for Phase 3).
# Gap-proof: paginate ALL closed PRs and flag every merged PR whose number is
# absent from _log.md, regardless of date. (An earlier high-water-mark design
# only considered PRs updated since the latest processed merge date, so any PR
# that slipped through a gap below that mark — content or non-content — was
# never rediscovered. That blind spot is what required the 2026-05 historical
# backfill.) Visible warnings on fetch/parse failure so silent drops stop
# (prior single-page-30 fetch silently dropped #66/#121/#167/#176).
UNPROCESSED_FILE=$(mktemp "${TMPDIR:-/tmp}/unprocessed-prs.XXXXXX")
DISCOVERY_WARN_FILE=$(mktemp "${TMPDIR:-/tmp}/pr-discovery-warn.XXXXXX")
(
    GH_API="https://api.github.com/repos/sky-ecosystem/next-gen-atlas"
    PAGE=1
    MAX_PAGES=20   # 20 * 100 = 2000 PRs; covers any plausible backlog
    ALL_MERGED=""

    while [ "$PAGE" -le "$MAX_PAGES" ]; do
        RESULT=$(curl -sf "$GH_API/pulls?state=closed&sort=updated&direction=desc&per_page=100&page=$PAGE" 2>/dev/null)
        RC=$?
        if [ $RC -ne 0 ] || [ -z "$RESULT" ]; then
            echo "WARNING: PR discovery failed at page $PAGE (curl exit=$RC); unprocessed PRs may be missed." >> "$DISCOVERY_WARN_FILE"
            break
        fi
        PAGE_COUNT=$(echo "$RESULT" | jq 'length' 2>/dev/null)
        if [ -z "$PAGE_COUNT" ]; then
            echo "WARNING: PR discovery got non-JSON response at page $PAGE; stopping." >> "$DISCOVERY_WARN_FILE"
            break
        fi
        if [ "$PAGE_COUNT" = "0" ]; then
            break
        fi
        PAGE_MERGED=$(echo "$RESULT" | jq -r '.[] | select(.merged_at != null) | "\(.number)\t\(.updated_at)"' 2>/dev/null || true)
        if [ -n "$PAGE_MERGED" ]; then
            ALL_MERGED+="$PAGE_MERGED"$'\n'
        fi
        # No early-stop on date — we must see every page to catch gaps anywhere
        # in history. Bounded by MAX_PAGES; a short page means we hit the end.
        if [ "$PAGE_COUNT" -lt 100 ]; then
            break
        fi
        PAGE=$((PAGE + 1))
    done

    if [ "$PAGE" -gt "$MAX_PAGES" ]; then
        echo "WARNING: PR discovery reached max-pages cap ($MAX_PAGES); backlog may extend further." >> "$DISCOVERY_WARN_FILE"
    fi

    # Every merged PR number found, regardless of date; the _log membership
    # check below is the sole filter, so any gap anywhere in history surfaces.
    MERGED_PRS=$(echo "$ALL_MERGED" | awk -F'\t' '$1 != "" {print $1}')

    while IFS= read -r pr_num; do
        [ -z "$pr_num" ] && continue
        if ! grep -q "| #$pr_num " "$LOG_FILE" 2>/dev/null; then
            echo "$pr_num" >> "$UNPROCESSED_FILE"
        fi
    done <<< "$MERGED_PRS"
) &

# === Phase 2: Wait for everything to finish ===
wait

# Surface any discovery warnings to the user (not silently dropped)
if [ -s "$DISCOVERY_WARN_FILE" ]; then
    echo ""
    cat "$DISCOVERY_WARN_FILE" >&2
fi
rm -f "$DISCOVERY_WARN_FILE"

# === Phase 3: Auto-process unprocessed merged PRs ===
# Runs the full process-pr.sh pipeline (classify-diff → extract-values →
# enrich → render → verify). Output is fully-rendered Material/Housekeeping
# bullets in history/<entity>/changelog.md with status=auto in _log.md. The
# `### Context` section is left as `<!-- context: pending -->` for the in-session
# agent to fill after refresh.sh returns (see the /refresh skill).
if [ -s "$UNPROCESSED_FILE" ]; then
    PR_NUMS=$(tr '\n' ' ' < "$UNPROCESSED_FILE")
    echo ""
    echo "Auto-processing merged PRs: $PR_NUMS"
    bash "$ATLAS_DIR/process-pr.sh" $PR_NUMS || true
fi
rm -f "$UNPROCESSED_FILE"

# === Phase 3b: Surface legacy skeleton PRs (pre-pipeline) ===
# Newly-processed PRs land at status=auto. Lingering status=skeleton rows are
# from before the pipeline existed; surface them so Claude can re-process via
# `process-pr.sh --force <PR>` to upgrade them. Capped at 5 most-recent.
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

# === Phase 3c: Surface AD roster drift and unprocessed rationales ===
# Roster drift: compare Atlas-derived data/delegates/roster.json (just rebuilt above)
# against the human-curated delegates/_roster.md. New / removed ADs are surfaced so
# the session can run /ad-track sync to reconcile.
ROSTER_JSON="$PROJECT_DIR/data/delegates/roster.json"
ROSTER_MD="$PROJECT_DIR/delegates/_roster.md"
if [ -f "$ROSTER_JSON" ] && [ -f "$ROSTER_MD" ]; then
    DATA_SLUGS=$(jq -r '.[].slug' "$ROSTER_JSON" 2>/dev/null | sort)
    MD_SLUGS=$(grep -oE '^\| [^|]+ \| [a-z0-9-]+ \| topic' "$ROSTER_MD" \
        | awk -F'|' '{gsub(/^ +| +$/,"",$3); print $3}' | sort)
    if [ -n "$DATA_SLUGS" ] && [ -n "$MD_SLUGS" ]; then
        NEW_ADS=$(comm -23 <(echo "$DATA_SLUGS") <(echo "$MD_SLUGS"))
        REMOVED_ADS=$(comm -13 <(echo "$DATA_SLUGS") <(echo "$MD_SLUGS"))
        if [ -n "$NEW_ADS" ] || [ -n "$REMOVED_ADS" ]; then
            echo ""
            echo "AD roster drift vs delegates/_roster.md:"
            [ -n "$NEW_ADS" ] && echo "$NEW_ADS" | sed 's/^/  new in Atlas: /'
            [ -n "$REMOVED_ADS" ] && echo "$REMOVED_ADS" | sed 's/^/  removed from Atlas: /'
            echo "  → run /ad-track sync to reconcile"
        fi
    fi
fi

# Unprocessed rationales: cached forum posts whose source URL is not present in
# the corresponding delegates/<slug>/comms.md. Suppress output if zero.
if [ -f "$DELEGATES_DIR/find-unprocessed.py" ]; then
    PENDING_OUT=$(python3 "$DELEGATES_DIR/find-unprocessed.py" 2>/dev/null || true)
    if [ -n "$PENDING_OUT" ]; then
        echo ""
        echo "$PENDING_OUT"
        echo "  → run /ad-track to process"
    fi
fi

# === Phase 4: Session briefing ===
echo ""
if [ -f "$SCRIPT_DIR/session-briefing.py" ]; then
    python3 "$SCRIPT_DIR/session-briefing.py" 2>/dev/null || true
fi

exit 0
