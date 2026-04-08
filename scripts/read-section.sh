#!/usr/bin/env bash
# Extract content for a document from the Atlas file by number or UUID.
# Usage: read-section.sh <document-number-or-uuid> [--subtree] [--depth N]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
INDEX="$PROJECT_DIR/data/index.json"
ATLAS="$PROJECT_DIR/.atlas-repo/Sky Atlas/Sky Atlas.md"

if [ ! -f "$INDEX" ]; then
    echo "Error: Index not found. Run scripts/setup.sh or scripts/refresh.sh first." >&2
    exit 1
fi

QUERY="${1:?Usage: read-section.sh <number-or-uuid> [--subtree] [--depth N]}"
SUBTREE=false
MAX_DEPTH=999

shift
while [ $# -gt 0 ]; do
    case "$1" in
        --subtree) SUBTREE=true; shift ;;
        --depth) MAX_DEPTH="$2"; shift 2 ;;
        *) echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

# Find the document in the index
if [[ "$QUERY" =~ ^[a-f0-9-]{36}$ ]]; then
    # UUID lookup
    DOC=$(jq -r --arg uuid "$QUERY" '.[] | select(.uuid == $uuid)' "$INDEX")
else
    # Number lookup
    DOC=$(jq -r --arg num "$QUERY" '.[] | select(.number == $num)' "$INDEX")
fi

if [ -z "$DOC" ] || [ "$DOC" = "null" ]; then
    echo "Document not found: $QUERY" >&2
    exit 1
fi

LINE_START=$(echo "$DOC" | jq -r '.line_start')
LINE_END=$(echo "$DOC" | jq -r '.line_end')
DOC_NUMBER=$(echo "$DOC" | jq -r '.number')
DOC_DEPTH=$(echo "$DOC" | jq -r '.depth')

if [ "$SUBTREE" = true ]; then
    # Find the last document in the subtree (respecting --depth)
    TARGET_MAX_DEPTH=$((DOC_DEPTH + MAX_DEPTH))
    SUBTREE_END=$(jq -r --arg prefix "$DOC_NUMBER." --argjson max_depth "$TARGET_MAX_DEPTH" \
        '[.[] | select(.number | startswith($prefix)) | select(.depth <= $max_depth)] | last | .line_end // empty' "$INDEX")

    if [ -n "$SUBTREE_END" ]; then
        LINE_END="$SUBTREE_END"
    fi
fi

sed -n "${LINE_START},${LINE_END}p" "$ATLAS"
