#!/usr/bin/env bash
# Minimal session-start sync: pull the latest Atlas and rebuild the local index.
# Data fetches and the session briefing live in the /refresh skill, which the
# user invokes when they want the full picture.
#
# Emits a single JSON hook response at exit so the message lands in both:
#   - systemMessage             → user-visible in the Claude Code TUI
#   - hookSpecificOutput.additionalContext → Claude's session context
# Always exits 0 so the SessionStart hook doesn't report a failure.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
REPO_DIR="$PROJECT_DIR/.atlas-repo"

MESSAGE=""
# additionalContext for Claude; defaults to MESSAGE, but the staleness-gated
# auto-refresh below sets it to a directive the user's systemMessage need not carry.
CONTEXT=""

emit_and_exit() {
    if [ -n "$MESSAGE" ]; then
        local ctx="${CONTEXT:-$MESSAGE}"
        if command -v jq >/dev/null 2>&1; then
            jq -nc --arg msg "$MESSAGE" --arg ctx "$ctx" '{
                systemMessage: $msg,
                hookSpecificOutput: {
                    hookEventName: "SessionStart",
                    additionalContext: $ctx
                }
            }'
        else
            # Fallback: plain stdout reaches Claude's context but may not
            # render in the user's terminal.
            printf '%s\n' "$MESSAGE"
        fi
    fi
    exit 0
}

if [ ! -d "$REPO_DIR/.git" ]; then
    MESSAGE="Atlas repo not found. Run scripts/core/setup.sh first."
    emit_and_exit
fi

# Clear per-session ephemeral working files
rm -f "$PROJECT_DIR"/tmp/pr-*.diff "$PROJECT_DIR"/tmp/pr-*-body.md 2>/dev/null

# Age out pipeline intermediates older than 30 days. Atlas PRs typically
# merge well within that window, so anything older is debugging cruft from
# past pipeline runs (manifest/extracted/enriched/rendered/final/meta JSON).
find "$PROJECT_DIR/tmp" -maxdepth 1 -type f -name 'pr-*.json' -mtime +30 -delete 2>/dev/null

cd "$REPO_DIR"
# depth=20 covers ~1 month of merges so process-pr.sh can diff against the
# parent of recently-merged PRs without needing to deepen the clone every run.
# Older PRs trigger on-demand deepening in process-pr.sh.
if ! git fetch origin main --depth 20 2>/dev/null; then
    MESSAGE="Atlas sync failed: could not fetch from GitHub."
    emit_and_exit
fi
if ! git reset --hard origin/main >/dev/null 2>&1; then
    MESSAGE="Atlas sync failed: could not reset to origin/main."
    emit_and_exit
fi

LATEST_SHA=$(git rev-parse --short HEAD)
LATEST_MSG=$(git log --format='%s' -1)
cd "$PROJECT_DIR"

if ! python3 "$SCRIPT_DIR/build-index.py" >/dev/null 2>&1; then
    MESSAGE="Atlas sync failed: index rebuild errored."
    emit_and_exit
fi

# Derived from the index (uuid_refs → forward+backlinks). Best-effort: a stale
# or missing graph only disables the /atlas-navigate link-following helpers.
if [ -f "$PROJECT_DIR/scripts/atlas/build-link-graph.py" ]; then
    python3 "$PROJECT_DIR/scripts/atlas/build-link-graph.py" >/dev/null 2>&1 || true
fi

if [ -f "$SCRIPT_DIR/build-address-map.py" ]; then
    python3 "$SCRIPT_DIR/build-address-map.py" >/dev/null 2>&1 || true
fi

# Sync the protocol info repo and rebuild its index (best-effort, silent).
if [ -f "$SCRIPT_DIR/protocol-sync.sh" ]; then
    bash "$SCRIPT_DIR/protocol-sync.sh" >/dev/null 2>&1 || true
fi

# Staleness-gated auto-refresh. /refresh does slow network fetches and needs an
# agent turn for the /atlas-track Context-fill follow-up, so it can't run inside
# this hook. Instead, when the caches are stale we direct the session (via
# additionalContext) to run /refresh on its first turn; a fresh re-open stays
# instant and quiet. .last-session's mtime marks the last successful /refresh
# (session-briefing.py writes it at the end of every /refresh).
STALE_AFTER=21600  # 6h in seconds — tune here to change the auto-refresh cadence
LAST_SESSION="$PROJECT_DIR/.last-session"
NOW=$(date +%s)
if [ -f "$LAST_SESSION" ]; then
    LAST_TS=$(stat -f %m "$LAST_SESSION" 2>/dev/null || stat -c %Y "$LAST_SESSION" 2>/dev/null || echo 0)
else
    LAST_TS=0
fi
AGE=$(( NOW - LAST_TS ))
AGE_H=$(( AGE / 3600 ))
SYNC_LINE="Atlas synced: $LATEST_SHA ($LATEST_MSG)"

if [ "$LAST_TS" -eq 0 ] || [ "$AGE" -ge "$STALE_AFTER" ]; then
    if [ "$LAST_TS" -eq 0 ]; then
        AGE_DESC="not yet refreshed in this clone"
    else
        AGE_DESC="last refreshed ${AGE_H}h ago"
    fi
    MESSAGE="$SYNC_LINE
Data caches are stale ($AGE_DESC) — auto-refreshing now."
    CONTEXT="$SYNC_LINE

Workspace auto-refresh (staleness-gated, >6h): the data caches (governance, forum, delegate, market, financials, open PRs) are stale ($AGE_DESC). At the start of this session, proactively invoke the /refresh skill to update them, auto-process any newly merged Atlas PRs, and fill their changelog Context via /atlas-track. Do this before answering the user's first request unless that request is urgent or unrelated — in which case run /refresh right after. If /refresh has already run this session, do not run it again."
else
    MESSAGE="$SYNC_LINE
Data is fresh (refreshed ${AGE_H}h ago). Run /refresh anytime to update."
fi
emit_and_exit
