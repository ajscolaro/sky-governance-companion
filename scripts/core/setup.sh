#!/usr/bin/env bash
# First-time setup: clone the Atlas repo, build the index, create
# history dirs.
#
# Run this once after cloning sky-governance-companion. Either from your
# shell directly, or from inside an existing Claude session via:
#   ! bash scripts/core/setup.sh
#
# This is no longer invoked by the SessionStart hook — the hook does a
# fast welcome instead (scripts/core/first-run-welcome.sh) so the message
# renders reliably. Running setup explicitly means you also see clone
# progress and any errors directly.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
REPO_DIR="$PROJECT_DIR/.atlas-repo"
ATLAS_REPO="https://github.com/sky-ecosystem/next-gen-atlas.git"

if [ ! -d "$REPO_DIR/.git" ]; then
    echo "Cloning Sky Atlas (shallow, ~30s)..."
    git clone --depth 1 "$ATLAS_REPO" "$REPO_DIR"
else
    echo "Atlas repo already cloned at $REPO_DIR"
fi

echo "Building Atlas index..."
python3 "$SCRIPT_DIR/build-index.py"

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

echo ""
echo "Setup complete."
echo ""
echo "Next steps:"
echo "  - If you ran this from your shell: restart Claude in this directory."
echo "  - If you ran this via \`!\` inside Claude: run /refresh to fetch governance data and see the briefing."
