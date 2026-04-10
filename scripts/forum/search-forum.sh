#!/usr/bin/env bash
# Search cached Sky Forum posts by keyword, author, category, or date.
# Usage: search-forum.sh [KEYWORD] [--author X] [--category X] [--since YYYY-MM-DD] [--limit N]
#        search-forum.sh --id TOPIC_ID    # read full post body
#        search-forum.sh --recent [N]     # last N posts (default 10)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
INDEX="$PROJECT_DIR/data/forum/index.json"
POSTS_DIR="$PROJECT_DIR/data/forum/posts"

if [ ! -f "$INDEX" ]; then
    echo "No forum data cached. Run: bash scripts/fetch-forum.sh" >&2
    exit 1
fi

KEYWORD=""
AUTHOR=""
CATEGORY=""
SINCE=""
LIMIT=20
TOPIC_ID=""
RECENT=""

while [ $# -gt 0 ]; do
    case "$1" in
        --id) TOPIC_ID="$2"; shift 2 ;;
        --author) AUTHOR="$2"; shift 2 ;;
        --category) CATEGORY="$2"; shift 2 ;;
        --since) SINCE="$2"; shift 2 ;;
        --limit) LIMIT="$2"; shift 2 ;;
        --recent) RECENT="${2:-10}"; shift; [ "${1:-}" ] && [[ "$1" =~ ^[0-9]+$ ]] && { RECENT="$1"; shift; } || true ;;
        *)
            if [ -z "$KEYWORD" ]; then
                KEYWORD="$1"
            fi
            shift ;;
    esac
done

# --- Read a specific post ---
if [ -n "$TOPIC_ID" ]; then
    POST_FILE="$POSTS_DIR/$TOPIC_ID.json"
    if [ ! -f "$POST_FILE" ]; then
        echo "Post $TOPIC_ID not found in cache." >&2
        exit 1
    fi
    jq -r '"# \(.title)\nAuthor: \(.author)  |  Date: \(.published)  |  Category: \(.category)\nURL: \(.url)\n\n\(.body)"' "$POST_FILE"
    exit 0
fi

# --- Recent posts ---
if [ -n "$RECENT" ]; then
    jq -r ".[:$RECENT] | .[] | \"\(.topic_id)\t\(.published)\t\(.author)\t\(.title)\"" "$INDEX"
    exit 0
fi

# --- Search ---
FILTER="."
if [ -n "$KEYWORD" ]; then
    FILTER="$FILTER | select((.title | test(\"$KEYWORD\"; \"i\")) or (.excerpt | test(\"$KEYWORD\"; \"i\")))"
fi
if [ -n "$AUTHOR" ]; then
    FILTER="$FILTER | select(.author | test(\"$AUTHOR\"; \"i\"))"
fi
if [ -n "$CATEGORY" ]; then
    FILTER="$FILTER | select(.category | test(\"$CATEGORY\"; \"i\"))"
fi
if [ -n "$SINCE" ]; then
    FILTER="$FILTER | select(.published >= \"$SINCE\")"
fi

jq -r "[.[] | $FILTER] | .[:$LIMIT] | .[] | \"\(.topic_id)\t\(.published)\t\(.author)\t\(.title)\"" "$INDEX"
