#!/usr/bin/env bash
# Sync the sky-protocol-info repo and rebuild the protocol index.
#
# Called from atlas-sync.sh on every SessionStart (best-effort, silent).
# Also called from setup.sh on first-time setup.
# Can be run standalone to refresh the protocol mirror mid-session.
#
# Note: this script cannot run via Claude's `!` prefix — the project sandbox
# denies writes to .protocol-repo. Run it from a normal shell, or let the
# SessionStart hook call it automatically.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
REPO_DIR="$PROJECT_DIR/.protocol-repo"
PROTOCOL_REPO_URL="https://github.com/sky-ecosystem/sky-protocol-info.git"

if [ ! -d "$REPO_DIR/.git" ]; then
    echo "Cloning sky-protocol-info (shallow, no submodules)..."
    git clone --depth 1 --no-recurse-submodules "$PROTOCOL_REPO_URL" "$REPO_DIR"
else
    cd "$REPO_DIR"
    git fetch origin main --depth 1 2>/dev/null
    git reset --hard origin/main >/dev/null 2>&1
    cd "$PROJECT_DIR"
fi

python3 "$PROJECT_DIR/scripts/protocol/build-index.py" >/dev/null 2>&1
