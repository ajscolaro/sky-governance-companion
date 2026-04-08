# Security

This project processes untrusted content from public GitHub PRs (titles, bodies, diffs, document text). Multiple layers of defense are in place.

## Native sandbox (active by default)

Configured in `.claude/settings.json`. Every Claude Code session in this repo is automatically sandboxed via macOS Seatbelt — no setup required.

### What the sandbox enforces (OS-level, applies to all Bash subprocesses)

**Filesystem:**
- Writes restricted to the project directory only
- `.atlas-repo/` is deny-write
- `~/.ssh`, `~/.gnupg`, `~/.aws` are deny-read

**Network:**
- Only `github.com`, `api.github.com`, and `forum.skyeco.com` are reachable
- `enableWeakerNetworkIsolation` is on so `gh` CLI can verify TLS certificates via macOS trust service

**Command restrictions:**
- `eval`, `exec`, pipe-to-shell (`curl | bash`, etc.) are denied via permission rules
- `allowUnsandboxedCommands: false` — prevents the `dangerouslyDisableSandbox` escape hatch

### What the sandbox does NOT enforce

The sandbox only wraps Bash commands and their subprocesses. Claude's Read, Write, and Edit tools are governed by the permission system and hooks, not the OS sandbox. This means:

- A prompt injection could convince Claude to use Write/Edit to modify files that Bash can't touch
- The sandbox filesystem rules don't apply to Claude's file tools

### PreToolUse hook (protects against self-modification)

To close this gap, a PreToolUse hook (`scripts/check-write-path.sh`) intercepts all Write/Edit calls:

| Path | Behavior |
|---|---|
| `.atlas-repo/` | **Hard block** — never writable by the agent |
| `.claude/`, `CLAUDE.md`, `scripts/` | **Requires human approval** — prompt injection can't silently modify config, instructions, or scripts |
| Everything else | Allowed normally |

This is the primary defense against the prompt injection → self-modification attack chain.

## Docker Sandboxes (future, stronger isolation)

[Docker Sandboxes](https://www.docker.com/blog/docker-sandboxes-run-agents-in-yolo-mode-safely) (`sbx`) provide microVM-based isolation purpose-built for AI agents. They work natively with Claude Code and may become the recommended way to run sessions that process untrusted PRs once evaluated.

Install: `brew install docker/tap/sbx`

## Sanitization

`process-pr.sh` sanitizes PR titles and document names before writing to `history/` changelogs:
- Strips HTML comments, XML tags, ChatML markers
- Removes `[SYSTEM]`, `[INST]` prompt injection markers
- Strips control characters

**Limitation:** PR bodies and diffs are saved raw to `tmp/` for analysis. The sandbox prevents these from causing shell-level damage, but agents should still treat `tmp/` content as untrusted data.

## Threat model summary

| Attack | Mitigation |
|---|---|
| Shell injection via crafted document names | OS sandbox restricts filesystem/network for all subprocesses |
| Prompt injection → self-modification | PreToolUse hook requires human approval for config/script writes |
| Exfiltration via network | Sandbox allowlist limits outbound to GitHub only |
| Credential theft | `~/.ssh`, `~/.gnupg`, `~/.aws` are deny-read |
| Agent bypasses sandbox | `allowUnsandboxedCommands: false` blocks the escape hatch |
| Write to Atlas mirror | Hard-blocked by hook (exit 2) + sandbox denyWrite |
