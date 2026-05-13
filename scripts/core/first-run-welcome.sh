#!/usr/bin/env bash
# SessionStart hook for the first-run state (no .atlas-repo yet).
#
# Stays fast (<100ms) so the JSON systemMessage renders reliably in the
# TUI. A slow setup.sh inside the hook produces a 30s window where Claude
# Code doesn't render SessionStart messages — that's why setup is now
# explicit and user-driven instead of automatic.
#
# Emits in both:
#   - systemMessage              → user-visible
#   - hookSpecificOutput.additionalContext → Claude's context, including
#     a first-run flag so Claude proactively orients the user if the
#     systemMessage doesn't render.
set -uo pipefail

WELCOME="Welcome to Sky Governance Companion!

This Claude Code workspace helps you analyze and track Sky ecosystem
governance — the Sky Atlas (governing doc, formerly MakerDAO), on-chain
spell lifecycle, forum discussions, delegate vote rationales — over time.

▸ Complete one-time setup (clones the Sky Atlas, ~30s):

  1. Exit this session (type /exit or press Ctrl+C twice)
  2. Run from your shell:  bash scripts/core/setup.sh
  3. Restart Claude in this directory

After setup, every \`claude\` start auto-syncs the Atlas. Run /refresh
in-session to fetch governance data and see the briefing.

Skills available after setup:
  /refresh            Update caches, auto-process merged PRs, show briefing
  /atlas-navigate     Search and read Atlas documents
  /atlas-analyze      Explain what a specific Atlas PR changes
  /atlas-track        Process merged PRs into per-entity history
  /governance-data    On-chain delegation, votes, spell lifecycle
  /forum-search       Search cached Sky Forum discussions
  /ad-track           Process delegate vote rationales

Optional: add MESSARI_API_KEY to .env for market data; every other
feature works without it."

CONTEXT="$WELCOME

[first-run-flag] First-time setup has not been completed in this clone
(.atlas-repo is missing). If the user's first message is empty, a
greeting, or asks how to start, proactively orient them with the
welcome above.

CRITICAL: do NOT attempt to run \`bash scripts/core/setup.sh\` yourself
via the Bash tool — the sandbox denies writes to .atlas-repo. The \`!\`
prefix is also sandboxed and won't work. The user must exit this
Claude session, run setup.sh from their shell, then restart Claude.
Most skills will error until setup completes."

if command -v jq >/dev/null 2>&1; then
    jq -nc --arg msg "$WELCOME" --arg ctx "$CONTEXT" '{
        systemMessage: $msg,
        hookSpecificOutput: {
            hookEventName: "SessionStart",
            additionalContext: $ctx
        }
    }'
else
    # Fallback: plain stdout reaches Claude's context but won't render
    # to the user. Better than nothing.
    printf '%s\n' "$WELCOME"
fi

exit 0
