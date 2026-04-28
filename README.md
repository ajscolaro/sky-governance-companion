# Sky Atlas Explorer

A Claude Code workspace for analyzing Sky ecosystem governance over time, built around the [Sky Atlas](https://github.com/sky-ecosystem/next-gen-atlas).

## Why this exists

The [Sky Atlas](https://github.com/sky-ecosystem/next-gen-atlas) is the single \~3MB markdown document (\~9,800 sections) that defines every rule, parameter, role, and structure in the Sky ecosystem (formerly MakerDAO). It's already well-suited to AI tooling on its own — clean markdown, stable identifiers, governance-approved PRs as the unit of change.

But the Atlas only tells you **what's true right now**. To actually reason about Sky governance you also need:

- **History** — what changed, when, and through which governance flow (forum poll, AEP, SAEP, executive spell)
- **Pipeline** — what's been proposed but not yet ratified (open PRs, active polls, hat spells)
- **Onchain state** — executive lifecycle, hat changes, delegation, AD vote alignment
- **Rationale** — forum discussions and delegate vote explanations that capture the *why*
- **Market context** — price and supply movements aligned to governance events

This repo is the workspace that ties all of it together. It indexes the Atlas for efficient lookup (so you don't dump 3MB into every session), maintains per-entity change history, mirrors onchain governance state, caches forum and delegate activity, and exposes everything through a small set of slash commands. The output is governance research that fits in a working session — and a long-term institutional memory in `history/` that grows every time you run it.

## What you get

- **Indexed Atlas** — Document lookup by name, path, type, or UUID without loading the full file into context
- **Per-entity change history** — Curated changelogs in `history/`, optimized for RAG/grep retrieval (terse, predictable structure, stable identifiers, sorted most-recent-first)
- **PR analysis** — Diff-based analysis of open and merged Atlas PRs against current state and prior history
- **Auto-processing on `/refresh`** — Newly merged PRs become skeleton changelog entries automatically; the agent finalizes them into full Material/Housekeeping/Context entries
- **Onchain governance** — Delegation snapshots, poll vote matrix (with poll type and Atlas-PR linking), executive hat/supporter monitoring, full spell lifecycle (proposed/hat/cast/expired) with parsed proposal text from `sky-ecosystem/executive-votes`
- **Delegate tracking** — Per-AD profiles with onchain voting records and forum vote rationales
- **Forum search** — Cached Sky Forum posts searchable by keyword, author, category, or date
- **Market data** *(optional)* — SQLite database of daily price and supply for SKY, USDS+DAI, sUSDS, SPK, BTC, ETH; derived ratios; stablecoin competitive rankings
- **Session briefing** — `/refresh` prints what's changed since last session: current hat, active/ended polls, new open PRs, forum activity, daily market moves

## Setup

```bash
git clone https://github.com/ajscolaro/sky-atlas-explorer.git
cd sky-atlas-explorer
claude
```

That's it. On the first session, the `SessionStart` hook clones the Atlas (shallow), builds the document index, creates the Python virtualenv at `.venv/`, and seeds `history/`. Every subsequent session re-pulls the Atlas (~1s) and rebuilds the index.

Once the session is open, run **`/refresh`** to fetch governance, forum, delegate, and market data, and to print the briefing.

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI
- Python 3.8+ (the setup hook creates `.venv/` for you)
- `curl` (pre-installed on macOS) and `jq` (`brew install jq` on macOS)
- *(Optional)* `MESSARI_API_KEY` in `.env` for market data. The Messari API also supports [x402 pay-per-request](https://docs.messari.io/api-reference/x402-payments) — USDC on Base or Solana, no account or subscription needed. Every other feature works without it.

## Typical workflow

1. `claude` — session starts, Atlas auto-synced.
2. **Run `/refresh`** — fetches all governance / forum / market / delegate data, detects newly merged Atlas PRs, prints a briefing of what's changed.
3. Ask questions. Examples:
   - *"What's the current hat spell?"*
   - *"What changed in PR #220?"*
   - *"Find docs about Grove genesis capital"*
   - *"How has USDS supply trended this quarter?"*

When `/refresh` detects newly merged PRs, it auto-writes **skeleton** entries to `history/<entity>/changelog.md` and reports them as `Skeleton PRs awaiting finalization: …`. Claude then proactively runs `/atlas-track` and `/atlas-analyze` to rewrite each skeleton into a full entry with Material/Housekeeping sections and interpretive Context. You don't have to invoke those skills manually.

Changelog entries are optimized for **RAG/grep retrieval** — terse (5-15 lines substantive, 3-5 trivial), predictable structure (`## PR #N` / `**Merged:**` / `**Type:**` / `### Material Changes` / `### Housekeeping` / `### Context`), with stable identifiers (UUIDs, Atlas paths) inline where they aid navigation. Each changelog is sorted most-recent-first; `scripts/core/sort-changelogs.py` can re-sort everything if order drifts.

### For AI agents using this repo

If you're an agent operating in this project: **[CLAUDE.md](CLAUDE.md) is the canonical instructions.** It covers the hook/skill division of responsibility, the skeleton-PR finalization contract, security rules (all Atlas/PR/forum content is untrusted input), and skill composition patterns. Read it before acting.

## Skills

Invoke these during a Claude Code session. Skills marked *(optional)* depend on external API keys.

### `/refresh` — Update caches and see what's changed

Refreshes all data sources (voting portal, forum, delegates, market, open PRs), auto-processes any unprocessed merged Atlas PRs into `history/` skeletons, and prints a briefing of current governance state + new activity since the last session. Run at the start of a working session.

```
/refresh
```

### `/atlas-navigate` — Search and read Atlas documents

Find documents by keyword, path prefix, type, or UUID, then read their content without loading the full 3MB file.

```
/atlas-navigate Grove genesis capital
/atlas-navigate A.6.1.1.2
```

### `/atlas-track` — Process PRs into change history

Process merged PRs into per-entity changelogs. Detects new entities, routes changes by Atlas path prefix, and maintains the institutional memory in `history/`.

```
/atlas-track 217
/atlas-track 213 208 207
```

### `/atlas-analyze` — Analyze a PR

Explain what a PR is changing, why it matters, and how it relates to previous changes. Works for both open (proposed) and merged PRs.

```
/atlas-analyze 217
/atlas-analyze open
```

### `/governance-data` — Onchain governance data

Fetch and analyze delegation snapshots, vote alignment, executive vote lifecycle, and spell monitoring.

```
/governance-data executive        # Hat monitoring + spell lifecycle
/governance-data spell 2026-04-09 # Deep-dive into a specific spell
/governance-data delegation       # Current delegation metrics
/governance-data votes            # Poll vote matrix update
/governance-data status           # Data freshness report
```

### `/ad-track` — Delegate tracking

Process cached AD vote rationales from forum RSS into per-delegate profiles.

```
/ad-track
```

### `/messari-market-data` — Market data queries *(optional)*

Query the local market database for price, supply, stablecoin rankings, derived ratios, and governance event impact analysis. Data sourced from the Messari API.

```
/messari-market-data USDS supply growth over time
/messari-market-data SKY/ETH ratio last 90 days
/messari-market-data stablecoin market share
/messari-market-data event window around 2026-04-09
```

Requires `MESSARI_API_KEY` in `.env` for data refresh. Queries work on cached data without it. The Messari API is also [x402-compatible](https://docs.messari.io/api-reference/x402-payments) — pay per request with USDC on Base or Solana, no subscription needed (x402 integration not yet wired into the fetch scripts).

### `/forum-search` — Search forum discussions

Search cached Sky Forum governance discussions by keyword, author, category, or date.

```
/forum-search genesis capital
/forum-search recent
```

## Project layout

```
.atlas-repo/          Shallow clone of next-gen-atlas (gitignored, auto-refreshed)
.claude/
  settings.json       Sandbox config, hooks, permissions
  skills/             Skill definitions for all slash commands
data/                 Generated caches (gitignored, rebuilt on refresh)
  index.json          Parsed document index with line offsets
  market.db           SQLite market database (optional, requires Messari API key)
  forum/              Cached forum posts and search index
  delegates/          Cached AD vote rationales from RSS feeds
  voting/
    address-map.json  Voting address → AD slug mapping
    delegates/        Delegation API cache
    polls/            Poll tallies, vote matrix (with poll_type, atlas_pr linking)
    executive/        Executive API cache, lifecycle.json, transient proposal processing dir
delegates/            Per-AD profiles and vote rationale logs (committed)
docs/
  governance-reference.md   Shared governance context for PR analysis
  data-catalog.md           Master index of all data directories and sources
  security.md               Security model and threat mitigations
history/              Per-entity change logs (committed, long-term memory)
  entity-routing.conf       Maps Atlas prefixes to history directories
  _log.md                   Master log of processed PRs
  A.0--preamble/            Per-scope changelogs
  A.1--governance/
  ...
  A.6--agents/
    A.6.1.1.1--spark/       Per-agent changelogs (8 agents tracked)
    A.6.1.1.2--grove/
    ...
plans/                Implementation plans and handoff docs
scripts/
  core/
    setup.sh                    First-time setup
    atlas-sync.sh               Minimal session-start sync: pull Atlas + rebuild index (hook target)
    refresh.sh                  Full refresh: Atlas + all data fetches + auto-process merged PRs + briefing (invoked by /refresh)
    build-index.py              Parse Atlas into JSON index
    build-address-map.py        Join voting addresses to AD slugs
    session-briefing.py         Session briefing: what changed, governance status, forum activity
    sort-changelogs.py          Re-sort all history/**/changelog.md + _log.md by merge date (most-recent first)
    check-write-path.sh         PreToolUse hook for write protection
  atlas/
    search-index.sh             Query the index by prefix/name/type/UUID
    read-section.sh             Extract document content by line range
    process-pr.sh               Analyze a merged PR diff and route to changelogs
    backfill-prs.sh             Batch-generate skeleton changelog entries
  forum/
    fetch-forum.py              Fetch forum posts via RSS
    search-forum.sh             Search cached forum posts
  delegates/
    fetch-delegates.py          Fetch per-AD vote rationales via RSS
  voting/
    fetch-voting-delegates.py   Delegation data from vote.sky.money
    fetch-voting-polls.py       Poll vote matrix from vote.sky.money
    fetch-voting-executive.py   Hat/supporter data from vote.sky.money
    fetch-executive-proposals.py  Proposal lifecycle: fetch, parse, enrich, cleanup
    fetch-delegation-history.py Delegation lock/unlock event history
  market/
    market.py                   MarketDB query module (import for programmatic access)
    fetch-market.py             Populate SQLite from Messari API (optional)
    market-lookup.py            CLI for market data queries (date, range, ratio, stablecoins)
CLAUDE.md             Agent instructions, security rules, project conventions
```

## Security model

This project processes untrusted content from public GitHub PRs and anonymous forum posts. Several layers of defense are in place:

- **OS-level sandbox** — Filesystem writes restricted to the project directory; `.atlas-repo/` is write-protected; network limited to GitHub and the Sky Forum; dangerous shell patterns (`eval`, `curl | bash`) are denied
- **PreToolUse hook** — Intercepts all Write/Edit tool calls; hard-blocks writes to `.atlas-repo/`; requires human approval for changes to `.claude/`, `CLAUDE.md`, and `scripts/`
- **Content sanitization** — PR titles, document names, and forum posts are sanitized before storage (HTML comments, XML tags, ChatML markers, prompt injection patterns stripped)
- **Skill tool restrictions** — Each skill declares which tools it can use; read-only skills like `/forum-search` cannot run Bash or modify files
- **Behavioral rules** — CLAUDE.md and skill instructions explicitly direct the agent to never follow directives found in Atlas content, PR bodies, or forum posts

See [docs/security.md](docs/security.md) for the full threat model.

## Customization

### Adding new agents

When governance creates a new agent, add a routing entry to `history/entity-routing.conf`:

```
A.6.1.1.9	A.6--agents/A.6.1.1.9--new-agent
```

Then create the changelog file:

```bash
mkdir -p history/A.6--agents/A.6.1.1.9--new-agent
echo "# New Agent — Change History\n\nAtlas path: \`A.6.1.1.9\`\n\n---" > history/A.6--agents/A.6.1.1.9--new-agent/changelog.md
```

The `/atlas-track` skill can also detect and set up new agents automatically.

### Network access

The sandbox network allowlist in `.claude/settings.json` controls which domains are reachable. Current allowlist: `github.com`, `api.github.com`, `raw.githubusercontent.com`, `forum.skyeco.com`, `vote.sky.money`, `api.messari.io`. Add domains as needed for your use case.

## Starting fresh vs. using the included history

This repo ships with `history/` pre-populated with changelogs going back to mid-2025, and `delegates/` with per-AD profiles. Both represent accumulated institutional memory derived entirely from public governance data.

**If you want to use the included history:** clone and go — you get full context from day one.

**If you prefer to start fresh:** delete the contents of `history/` (keep the directory structure and `_log.md` header) and `delegates/`. The tooling works from whatever state you give it. To backfill history from scratch, use `/atlas-track` with `scripts/atlas/backfill-prs.sh`.

The `### Context` sections in changelogs contain interpretive analysis — feel free to rewrite them to reflect your own read.

## License

Apache 2.0 — see [LICENSE](LICENSE).

The Sky Atlas content accessed by this tooling is maintained by the Sky ecosystem at [sky-ecosystem/next-gen-atlas](https://github.com/sky-ecosystem/next-gen-atlas), also under the Apache 2.0 license.
