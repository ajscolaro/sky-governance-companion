#!/usr/bin/env bash
# Fetch latest AD vote rationales via per-thread RSS feeds into data/delegates/.
# Wrapper around fetch-delegates.py — always exits 0 (advisory, not critical).
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Ensure output directory exists
mkdir -p "$PROJECT_DIR/data/delegates"

# Activate venv if available
if [ -f "$PROJECT_DIR/.venv/bin/activate" ]; then
    # shellcheck disable=SC1091
    source "$PROJECT_DIR/.venv/bin/activate"
fi

python3 "$SCRIPT_DIR/fetch-delegates.py" "$@" || true

exit 0
