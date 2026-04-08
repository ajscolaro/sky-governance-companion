#!/usr/bin/env bash
# Fetch latest Sky Forum posts via RSS into data/forum/.
# Wrapper around fetch-forum.py — always exits 0 (advisory, not critical).
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Ensure output directory exists
mkdir -p "$PROJECT_DIR/data/forum/posts"

# Activate venv if available
if [ -f "$PROJECT_DIR/.venv/bin/activate" ]; then
    # shellcheck disable=SC1091
    source "$PROJECT_DIR/.venv/bin/activate"
fi

python3 "$SCRIPT_DIR/fetch-forum.py" "$@" || true

exit 0
