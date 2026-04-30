#!/usr/bin/env bash
# Search cached Sky Forum posts by keyword, author, category, or date.
# Usage: search-forum.sh [KEYWORD] [--author X] [--category X] [--since YYYY-MM-DD] [--limit N]
#                       [--entity ENTITY] [--registered-only]
#        search-forum.sh --id TOPIC_ID    # read full post body
#        search-forum.sh --recent [N]     # last N posts (default 10)
#
# Author columns are enriched with entity attribution from the Authorized
# Forum Accounts registry (data/forum/registry.json, built from Atlas
# A.2.7.1.1.1.1.4.0.6.1). --entity filters to posts authored by an entity's
# Entity Handle or any AR (transitive); --registered-only drops unregistered
# authors. If the registry is missing, both filters error and search behaves
# as it did before with a one-line stderr notice.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
INDEX="$PROJECT_DIR/data/forum/index.json"
POSTS_DIR="$PROJECT_DIR/data/forum/posts"
REGISTRY_HELPER="$SCRIPT_DIR/registry_lookup.py"

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
ENTITY=""
REGISTERED_ONLY=""

while [ $# -gt 0 ]; do
    case "$1" in
        --id) TOPIC_ID="$2"; shift 2 ;;
        --author) AUTHOR="$2"; shift 2 ;;
        --category) CATEGORY="$2"; shift 2 ;;
        --since) SINCE="$2"; shift 2 ;;
        --limit) LIMIT="$2"; shift 2 ;;
        --entity) ENTITY="$2"; shift 2 ;;
        --registered-only) REGISTERED_ONLY=1; shift ;;
        --recent) RECENT="${2:-10}"; shift; [ "${1:-}" ] && [[ "$1" =~ ^[0-9]+$ ]] && { RECENT="$1"; shift; } || true ;;
        *)
            if [ -z "$KEYWORD" ]; then
                KEYWORD="$1"
            fi
            shift ;;
    esac
done

# Build enrichment args once. Empty array is fine under "${arr[@]}".
ENRICH_ARGS=(--enrich)
[ -n "$ENTITY" ] && ENRICH_ARGS+=(--filter-entity "$ENTITY")
[ -n "$REGISTERED_ONLY" ] && ENRICH_ARGS+=(--registered-only)

# --- Read a specific post ---
if [ -n "$TOPIC_ID" ]; then
    POST_FILE="$POSTS_DIR/$TOPIC_ID.json"
    if [ ! -f "$POST_FILE" ]; then
        echo "Post $TOPIC_ID not found in cache." >&2
        exit 1
    fi
    AUTHOR_NAME=$(jq -r '.author' "$POST_FILE")
    LABEL=""
    if [ -f "$REGISTRY_HELPER" ]; then
        LABEL=$(python3 "$REGISTRY_HELPER" --lookup "$AUTHOR_NAME" 2>/dev/null || true)
    fi
    if [ -n "$LABEL" ]; then
        AUTHOR_DISPLAY="$AUTHOR_NAME ($LABEL)"
    else
        AUTHOR_DISPLAY="$AUTHOR_NAME"
    fi
    jq -r --arg author_display "$AUTHOR_DISPLAY" \
        '"# \(.title)\nAuthor: \($author_display)  |  Date: \(.published)  |  Category: \(.category)\nURL: \(.url)\n\n\(.body)"' \
        "$POST_FILE"
    exit 0
fi

# --- Recent posts ---
if [ -n "$RECENT" ]; then
    jq -r ".[:$RECENT] | .[] | \"\(.topic_id)\t\(.published)\t\(.author)\t\(.title)\"" "$INDEX" \
        | python3 "$REGISTRY_HELPER" "${ENRICH_ARGS[@]}"
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

# --entity / --registered-only are applied post-jq via the helper, which has
# the registry loaded. Bumping --limit slightly so entity filters still return
# meaningful results when many top-LIMIT posts get filtered out is left to the
# caller — pass --limit explicitly when filtering aggressively.
jq -r "[.[] | $FILTER] | .[:$LIMIT] | .[] | \"\(.topic_id)\t\(.published)\t\(.author)\t\(.title)\"" "$INDEX" \
    | python3 "$REGISTRY_HELPER" "${ENRICH_ARGS[@]}"
