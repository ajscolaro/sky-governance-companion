#!/usr/bin/env bash
# First-time setup: clone Atlas repo, build index, create history dirs.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
REPO_DIR="$PROJECT_DIR/.atlas-repo"
ATLAS_REPO="https://github.com/sky-ecosystem/next-gen-atlas.git"

# Clone if not present
if [ ! -d "$REPO_DIR/.git" ]; then
    echo "Cloning Atlas repo (shallow)..."
    git clone --depth 1 "$ATLAS_REPO" "$REPO_DIR"
else
    echo "Atlas repo already cloned at $REPO_DIR"
fi

# Build index
echo "Building index..."
python3 "$SCRIPT_DIR/build-index.py"

# Create history dirs if missing
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

# Show first-run orientation
if [ -f "$SCRIPT_DIR/session-briefing.py" ]; then
    python3 "$SCRIPT_DIR/session-briefing.py" --first-run 2>/dev/null || true
fi

echo "Setup complete."
