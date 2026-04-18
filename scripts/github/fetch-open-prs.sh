#!/usr/bin/env bash
# Cache the list of open PRs in sky-ecosystem/next-gen-atlas for the session briefing.
# Drafts are filtered out. Writes JSON array to data/github/open-prs.json.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
CACHE_DIR="$PROJECT_DIR/data/github"
CACHE_FILE="$CACHE_DIR/open-prs.json"
GH_API="https://api.github.com/repos/sky-ecosystem/next-gen-atlas"

QUIET=""
[ "${1:-}" = "--quiet" ] && QUIET=1

mkdir -p "$CACHE_DIR"

RAW=$(curl -sf "$GH_API/pulls?state=open&sort=updated&direction=desc&per_page=30" 2>/dev/null) || {
    [ -z "$QUIET" ] && echo "Warning: Could not fetch open PRs." >&2
    [ ! -f "$CACHE_FILE" ] && echo "[]" > "$CACHE_FILE"
    exit 0
}

echo "$RAW" | jq '[.[] | select(.draft == false) | {
    number: .number,
    title: .title,
    user: .user.login,
    created_at: .created_at,
    updated_at: .updated_at,
    url: .html_url
}]' > "$CACHE_FILE" 2>/dev/null || echo "[]" > "$CACHE_FILE"

[ -z "$QUIET" ] && echo "Open PRs cached to $CACHE_FILE"
