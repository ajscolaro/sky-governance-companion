#!/usr/bin/env bash
# Minimal session-start sync: pull the latest Atlas and rebuild the local index.
# Data fetches and the session briefing live in the /refresh skill, which the
# user invokes when they want the full picture.
#
# Must always exit 0 so the SessionStart hook doesn't report a failure.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
REPO_DIR="$PROJECT_DIR/.atlas-repo"

if [ ! -d "$REPO_DIR/.git" ]; then
    echo "Atlas repo not found. Run scripts/core/setup.sh first."
    exit 0
fi

# Clear ephemeral working files from previous session
rm -f "$PROJECT_DIR"/tmp/pr-*.diff "$PROJECT_DIR"/tmp/pr-*-body.md 2>/dev/null

cd "$REPO_DIR"
# depth=20 covers ~1 month of merges so process-pr.sh can diff against the
# parent of recently-merged PRs without needing to deepen the clone every run.
# Older PRs trigger on-demand deepening in process-pr.sh.
git fetch origin main --depth 20 2>/dev/null || { echo "Atlas sync failed: could not fetch from GitHub."; exit 0; }
git reset --hard origin/main >/dev/null 2>&1 || { echo "Atlas sync failed: could not reset to origin/main."; exit 0; }

LATEST_SHA=$(git rev-parse --short HEAD)
LATEST_MSG=$(git log --format='%s' -1)
cd "$PROJECT_DIR"

python3 "$SCRIPT_DIR/build-index.py" >/dev/null 2>&1 || { echo "Atlas sync failed: index rebuild errored."; exit 0; }

if [ -f "$SCRIPT_DIR/build-address-map.py" ]; then
    python3 "$SCRIPT_DIR/build-address-map.py" >/dev/null 2>&1 || true
fi

# Emit the summary to both stdout (Claude's context via SessionStart hook) and
# /dev/tty (user-visible in terminal). The leading blank lines pad the tty
# write up into the scrollback so the TUI input prompt doesn't overwrite it.
{
    printf '\n\n\n'
    echo "Atlas synced: $LATEST_SHA ($LATEST_MSG)"
    echo "Run /refresh to update governance/market/forum data and see what's changed."
} | tee /dev/tty
exit 0
