#!/usr/bin/env bash
# First-time setup: clone Atlas repo, build index, create history dirs.
#
# Mirrors atlas-sync.sh's hook protocol: emits a single JSON response at
# exit so the welcome lands in both:
#   - systemMessage             → user-visible in the Claude Code TUI
#   - hookSpecificOutput.additionalContext → Claude's session context
# Always exits 0 so the SessionStart hook doesn't report a failure.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
REPO_DIR="$PROJECT_DIR/.atlas-repo"
ATLAS_REPO="https://github.com/sky-ecosystem/next-gen-atlas.git"

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

# Clone Atlas (shallow). Hook stdout is captured for JSON parsing, so the
# user can't see git progress anyway — clone quietly and surface only the
# final status.
#
# Shallow clone of next-gen-atlas is ~92MB / ~14k files, so the first run
# can take 20-45s on typical broadband + SSD. Print a one-liner to the
# controlling terminal so the user knows the session isn't hung. Guarded
# so it no-ops in non-TTY environments (CI, web/IDE-embedded shells).
if [ ! -d "$REPO_DIR/.git" ]; then
    if [ -w /dev/tty ]; then
        printf '[sky-governance-companion] First-time setup: cloning Sky Atlas (~30s, one-time)...\n' > /dev/tty
    fi
    if ! git clone --depth 1 --quiet "$ATLAS_REPO" "$REPO_DIR" >/dev/null 2>&1; then
        MESSAGE="First-time setup failed: could not clone the Atlas repo from GitHub.
Check your network connection and re-run \`bash scripts/core/setup.sh\` from a shell to see details."
        emit_and_exit
    fi
fi

if ! python3 "$SCRIPT_DIR/build-index.py" >/dev/null 2>&1; then
    MESSAGE="First-time setup failed: Atlas index build errored.
Re-run \`bash scripts/core/setup.sh\` from a shell to see the error."
    emit_and_exit
fi

HISTORY_DIR="$PROJECT_DIR/history"
for dir in \
    "A.0--preamble" \
    "A.1--governance" "A.2--support" "A.3--stability" \
    "A.4--protocol" "A.5--accessibility" \
    "A.6--agents" \
    "A.6--agents/A.6.1.1.1--spark" "A.6--agents/A.6.1.1.2--grove" \
    "A.6--agents/A.6.1.1.3--keel" "A.6--agents/A.6.1.1.4--skybase" \
    "A.6--agents/A.6.1.1.5--obex" "A.6--agents/A.6.1.1.6--pattern" \
    "A.6--agents/A.6.1.1.7--launch-agent-6" "A.6--agents/A.6.1.1.8--launch-agent-7" \
    "_other"; do
    mkdir -p "$HISTORY_DIR/$dir"
done

if [ -f "$SCRIPT_DIR/build-address-map.py" ]; then
    python3 "$SCRIPT_DIR/build-address-map.py" >/dev/null 2>&1 || true
fi

cd "$REPO_DIR"
LATEST_SHA=$(git rev-parse --short HEAD)
cd "$PROJECT_DIR"

MESSAGE="Welcome to Sky Governance Companion!

First-time setup complete — Atlas cloned and indexed at $LATEST_SHA.

This workspace helps you navigate the Sky Atlas (governing document of
the Sky ecosystem, formerly MakerDAO) and track governance changes over
time across forum polls, executive spells, and Active Data edits.

Skills available in any session:
  /refresh            Update caches, auto-process merged PRs, show briefing
  /atlas-navigate     Search and read Atlas documents
  /atlas-analyze      Explain what a specific Atlas PR changes
  /atlas-track        Process merged PRs into per-entity history
  /governance-data    On-chain delegation, votes, spell lifecycle
  /forum-search       Search cached Sky Forum discussions
  /ad-track           Process delegate vote rationales

Next step: run /refresh to fetch governance / forum / delegate / market
data and get a briefing of current state.

Optional: add MESSARI_API_KEY to .env for market data; every other
feature works without it."

emit_and_exit
