#!/usr/bin/env bash
# Query the Atlas index by prefix, name, type, or UUID.
# Usage: search-index.sh [--prefix X] [--name X] [--type X] [--uuid X] [--under X] [--limit N]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
INDEX="$PROJECT_DIR/data/index.json"

if [ ! -f "$INDEX" ]; then
    echo "Error: Index not found. Run scripts/setup.sh or scripts/refresh.sh first." >&2
    exit 1
fi

PREFIX=""
NAME=""
TYPE=""
UUID=""
UNDER=""
LIMIT=50

while [ $# -gt 0 ]; do
    case "$1" in
        --prefix) PREFIX="$2"; shift 2 ;;
        --name) NAME="$2"; shift 2 ;;
        --type) TYPE="$2"; shift 2 ;;
        --uuid) UUID="$2"; shift 2 ;;
        --under) UNDER="$2"; shift 2 ;;
        --limit) LIMIT="$2"; shift 2 ;;
        *)
            # Positional arg: treat as name search if no flags given
            if [ -z "$NAME" ] && [ -z "$PREFIX" ] && [ -z "$UUID" ]; then
                NAME="$1"
            fi
            shift ;;
    esac
done

# Build jq filter
FILTER="."
if [ -n "$PREFIX" ]; then
    FILTER="$FILTER | select(.number | startswith(\"$PREFIX\"))"
fi
if [ -n "$UNDER" ]; then
    FILTER="$FILTER | select((.number | startswith(\"${UNDER}.\")) or .number == \"$UNDER\")"
fi
if [ -n "$NAME" ]; then
    FILTER="$FILTER | select(.name | test(\"$NAME\"; \"i\"))"
fi
if [ -n "$TYPE" ]; then
    FILTER="$FILTER | select(.type == \"$TYPE\")"
fi
if [ -n "$UUID" ]; then
    FILTER="$FILTER | select(.uuid | startswith(\"$UUID\"))"
fi

jq -r "[.[] | $FILTER] | .[:$LIMIT] | .[] | \"\(.number)\t\(.name)\t[\(.type)]\t\(.path)\"" "$INDEX"
