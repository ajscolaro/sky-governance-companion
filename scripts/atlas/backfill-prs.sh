#!/usr/bin/env bash
# ONE-TIME SCRIPT: Backfill all merged Atlas PRs into history/ skeleton entries.
#
# Fetches the full list of merged PRs from sky-ecosystem/next-gen-atlas,
# then runs process-pr.sh on each one (oldest first). Already-processed
# PRs are automatically skipped by process-pr.sh.
#
# Usage: bash scripts/backfill-prs.sh [--dry-run]
#
# This script is rate-limited to ~2 seconds per PR to avoid GitHub API throttling.
# For ~158 PRs, expect ~6 minutes total runtime.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
GH_API="https://api.github.com/repos/sky-ecosystem/next-gen-atlas"

DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=true
    echo "=== DRY RUN — will list PRs but not process them ==="
fi

echo "Fetching merged PRs from sky-ecosystem/next-gen-atlas..."

# Collect all merged PR numbers across pages (API returns 100 per page)
ALL_PRS=""
PAGE=1
while true; do
    RESPONSE=$(curl -sf "$GH_API/pulls?state=closed&sort=created&direction=asc&per_page=100&page=$PAGE" 2>/dev/null) || {
        echo "Error: Failed to fetch page $PAGE from GitHub API" >&2
        break
    }

    # Extract merged PR numbers (skip unmerged)
    PAGE_PRS=$(echo "$RESPONSE" | python3 -c "
import json, sys
prs = json.load(sys.stdin)
if not prs:
    sys.exit(0)
for p in prs:
    if p.get('merged_at'):
        print(p['number'])
" 2>/dev/null)

    if [ -z "$PAGE_PRS" ]; then
        break
    fi

    ALL_PRS+="$PAGE_PRS"$'\n'
    COUNT=$(echo "$PAGE_PRS" | wc -l | tr -d ' ')
    echo "  Page $PAGE: $COUNT merged PRs"

    # GitHub returns up to 100 per page; if we got fewer, we're done
    TOTAL_ON_PAGE=$(echo "$RESPONSE" | python3 -c "import json,sys; print(len(json.load(sys.stdin)))" 2>/dev/null)
    if [ "$TOTAL_ON_PAGE" -lt 100 ]; then
        break
    fi

    PAGE=$((PAGE + 1))
    sleep 1
done

# Deduplicate and sort numerically
ALL_PRS=$(echo "$ALL_PRS" | grep -v '^$' | sort -n -u)
TOTAL=$(echo "$ALL_PRS" | wc -l | tr -d ' ')

echo ""
echo "Found $TOTAL merged PRs total."

if $DRY_RUN; then
    echo ""
    echo "PR numbers:"
    echo "$ALL_PRS" | head -20
    echo "..."
    echo "(showing first 20 of $TOTAL)"
    exit 0
fi

echo "Processing all $TOTAL PRs (oldest first, ~2s per PR)..."
echo "Already-processed PRs will be skipped automatically."
echo ""

PROCESSED=0
SKIPPED=0
FAILED=0

for PR_NUM in $ALL_PRS; do
    # Check if already in _log.md (fast skip without calling process-pr.sh)
    if grep -q "| #$PR_NUM " "$PROJECT_DIR/history/_log.md" 2>/dev/null; then
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    echo "[$((PROCESSED + SKIPPED + FAILED + 1))/$TOTAL] Processing PR #$PR_NUM..."
    if bash "$SCRIPT_DIR/process-pr.sh" "$PR_NUM" 2>&1; then
        PROCESSED=$((PROCESSED + 1))
    else
        echo "  Warning: PR #$PR_NUM failed" >&2
        FAILED=$((FAILED + 1))
    fi

    # Rate limit to avoid GitHub API throttling
    sleep 2
done

echo ""
echo "=== Backfill complete ==="
echo "  Processed: $PROCESSED"
echo "  Skipped (already done): $SKIPPED"
echo "  Failed: $FAILED"
echo "  Total: $TOTAL"
echo ""
echo "Next step: Run /atlas-analyze on each skeleton entry to fill in Context sections."
echo "See plans/backfill-handoff.md for the handoff instructions."
