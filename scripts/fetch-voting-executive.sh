#!/usr/bin/env bash
# Fetch executive proposal and hat data from vote.sky.money API.
# Wrapper around fetch-voting-executive.py — always exits 0 (advisory, not critical).
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Ensure output directories exist
mkdir -p "$PROJECT_DIR/data/voting/executive/snapshots"
mkdir -p "$PROJECT_DIR/snapshots/executive"

# Activate venv if available
if [ -f "$PROJECT_DIR/.venv/bin/activate" ]; then
    # shellcheck disable=SC1091
    source "$PROJECT_DIR/.venv/bin/activate"
fi

python3 "$SCRIPT_DIR/fetch-voting-executive.py" "$@" || true

exit 0
