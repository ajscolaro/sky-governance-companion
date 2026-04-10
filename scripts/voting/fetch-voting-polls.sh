#!/usr/bin/env bash
# Fetch poll tallies and build vote matrix from vote.sky.money API.
# Wrapper around fetch-voting-polls.py — always exits 0 (advisory, not critical).
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"

# Ensure output directories exist
mkdir -p "$PROJECT_DIR/data/voting/polls/tallies"

# Activate venv if available
if [ -f "$PROJECT_DIR/.venv/bin/activate" ]; then
    # shellcheck disable=SC1091
    source "$PROJECT_DIR/.venv/bin/activate"
fi

python3 "$SCRIPT_DIR/fetch-voting-polls.py" "$@" || true

exit 0
