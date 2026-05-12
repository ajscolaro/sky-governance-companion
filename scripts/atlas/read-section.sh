#!/usr/bin/env bash
# Read a document (or subtree) from the atomized Atlas by number or UUID.
# Usage: read-section.sh <document-number-or-uuid> [--subtree] [--depth N]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
INDEX="$PROJECT_DIR/data/index.json"

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

if [[ "$QUERY" =~ ^[a-f0-9-]{36}$ ]]; then
    DOC=$(jq -r --arg uuid "$QUERY" '.[] | select(.uuid == $uuid)' "$INDEX")
else
    DOC=$(jq -r --arg num "$QUERY" '.[] | select(.number == $num)' "$INDEX")
fi

if [ -z "$DOC" ] || [ "$DOC" = "null" ]; then
    echo "Document not found: $QUERY" >&2
    exit 1
fi

DOC_NUMBER=$(echo "$DOC" | jq -r '.number')
DOC_DEPTH=$(echo "$DOC" | jq -r '.depth')
DOC_PATH=$(echo "$DOC" | jq -r '.path')

if [ "$SUBTREE" = false ]; then
    cat "$PROJECT_DIR/$DOC_PATH"
    exit 0
fi

TARGET_MAX_DEPTH=$((DOC_DEPTH + MAX_DEPTH))

cat "$PROJECT_DIR/$DOC_PATH"

jq -r --arg prefix "${DOC_NUMBER}." \
      --argjson max_depth "$TARGET_MAX_DEPTH" \
      '[.[] | select(.number | startswith($prefix)) | select(.depth <= $max_depth)] |
       sort_by(.number) | .[].path' "$INDEX" | while IFS= read -r rel_path; do
    printf '\n'
    cat "$PROJECT_DIR/$rel_path"
done
