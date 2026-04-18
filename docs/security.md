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
- `enableWeakerNetworkIsolation` is on so network-dependent tools (curl, git) can verify TLS certificates via macOS trust service

**Command restrictions:**
- `eval`, `exec`, pipe-to-shell (`curl | bash`, etc.) are denied via permission rules
- `allowUnsandboxedCommands: false` — prevents the `dangerouslyDisableSandbox` escape hatch

### What the sandbox does NOT enforce

The sandbox only wraps Bash commands and their subprocesses. Claude's Read, Write, and Edit tools are governed by the permission system and hooks, not the OS sandbox. This means:

- A prompt injection could convince Claude to use Write/Edit to modify files that Bash can't touch
- The sandbox filesystem rules don't apply to Claude's file tools

### PreToolUse hook (protects against self-modification)

To close this gap, a PreToolUse hook (`scripts/core/check-write-path.sh`) intercepts all Write/Edit calls:

| Path | Behavior |
|---|---|
| `.atlas-repo/` | **Hard block** — never writable by the agent |
| `.claude/`, `CLAUDE.md`, `scripts/` | **Requires human approval** — prompt injection can't silently modify config, instructions, or scripts |
| Everything else | Allowed normally |

This is the primary defense against the prompt injection → self-modification attack chain.

## Docker Sandboxes (future, stronger isolation)

[Docker Sandboxes](https://www.docker.com/blog/docker-sandboxes-run-agents-in-yolo-mode-safely) (`sbx`) provide microVM-based isolation purpose-built for AI agents. They work natively with Claude Code and may become the recommended way to run sessions that process untrusted PRs once evaluated.

Install: `brew install docker/tap/sbx`

## Delegate RSS feeds

AD vote rationales are fetched from per-thread Discourse RSS feeds (`{thread_url}.rss`). These are **untrusted forum content** — the highest risk tier.

### Fetch/process separation

Raw RSS is fetched when the user invokes `/refresh` (which runs `scripts/core/refresh.sh` in background, non-blocking) and stored as sanitized JSON in `data/delegates/{slug}/`. Claude only reads this cached data when the user invokes `/ad-track` — untrusted content never enters the agent's context automatically.

### Author filtering

Only posts where `dc:creator` matches the AD's forum username are cached. The username is discovered from the thread's first post (the recognition submission) via the Discourse topic JSON API — this is the post the AD themselves authored to register. The thread URL comes from the Atlas Active Data (A.1.5.1.5.0.6.1), which is governance-approved, ensuring we're looking at the correct thread. This prevents third-party replies (which could contain injection attempts) from being stored.

### Sanitization

`fetch-delegates.py` applies the same sanitization pipeline as `fetch-forum.py`:
- HTML stripping (script/style tags, all markup)
- Injection marker removal (`[SYSTEM]`, `[INST]`, ChatML `<|...|>`, HTML comments)
- Control character removal
- Content length limits (8KB body cap)

### Threat model additions

| Attack | Mitigation |
|--------|------------|
| Injection via AD vote rationale | Sanitized at fetch time; `dc:creator` filter limits to AD's own posts; `/ad-track` skill warns agent to treat content as data |
| Malicious AD recognition submission | Same sanitization; content framed as quoted data in `comms.md`, not instructions |
| Roster manipulation via fake Atlas edit | Roster is read from merged Atlas `main` (governance-approved); open PRs cannot affect it |
| Username spoofing via thread replies | Username derived from thread creator (post #1) via Discourse API, not from arbitrary replies |

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
| Exfiltration via network | Sandbox allowlist limits outbound to GitHub and forum.skyeco.com only |
| Credential theft | `~/.ssh`, `~/.gnupg`, `~/.aws` are deny-read |
| Agent bypasses sandbox | `allowUnsandboxedCommands: false` blocks the escape hatch |
| Write to Atlas mirror | Hard-blocked by hook (exit 2) + sandbox denyWrite |
