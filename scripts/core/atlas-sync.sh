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

emit_and_exit() {
    if [ -n "$MESSAGE" ]; then
        if command -v jq >/dev/null 2>&1; then
            jq -nc --arg msg "$MESSAGE" '{
                systemMessage: $msg,
                hookSpecificOutput: {
                    hookEventName: "SessionStart",
                    additionalContext: $msg
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

if [ -f "$SCRIPT_DIR/build-address-map.py" ]; then
    python3 "$SCRIPT_DIR/build-address-map.py" >/dev/null 2>&1 || true
fi

MESSAGE="Atlas synced: $LATEST_SHA ($LATEST_MSG)
Run /refresh to update governance/market/forum data and see what's changed."
emit_and_exit
