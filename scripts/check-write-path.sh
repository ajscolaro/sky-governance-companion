#!/usr/bin/env bash
# PreToolUse hook: require human approval for writes to sensitive paths.
# For all other paths, allow silently.
#
# Protected paths:
#   .claude/       — sandbox config, skills, settings
#   CLAUDE.md      — agent behavioral instructions
#   scripts/       — executed automatically by hooks
#   .atlas-repo/   — hard block (governance-approved mirror)

INPUT="${TOOL_INPUT:-}"

# Hard block: .atlas-repo/ should never be written by the agent
if echo "$INPUT" | grep -q '\.atlas-repo'; then
    echo 'BLOCK: .atlas-repo/ is a read-only mirror of the governance-approved Atlas.'
    exit 2
fi

# Require approval: config, instructions, and scripts
if echo "$INPUT" | grep -qE '\.(claude|CLAUDE\.md)|/CLAUDE\.md|/scripts/'; then
    cat <<'EOF'
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "ask",
    "permissionDecisionReason": "This file affects agent behavior or security settings. Please review."
  }
}
EOF
    exit 0
fi

# Everything else: allow
exit 0
