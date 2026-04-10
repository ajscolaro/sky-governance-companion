# Sky Atlas Explorer

Claude Code tooling for navigating the [Sky Atlas](https://github.com/sky-ecosystem/next-gen-atlas) and tracking governance changes over time.

## What is the Sky Atlas?

The Sky Atlas is the single governing document for the Sky ecosystem (formerly MakerDAO). It's a ~3MB markdown file containing ~9,800 documents that define every rule, parameter, role, and structure in the protocol. It lives in [sky-ecosystem/next-gen-atlas](https://github.com/sky-ecosystem/next-gen-atlas) and is updated via weekly governance-approved PRs.

This project provides local tooling to search, read, and analyze that document and its changes without loading the entire file into context.

## What this does

- **Local Atlas access** — Shallow clone auto-refreshed on session start, with a parsed JSON index for fast document lookup by name, path, type, or UUID
- **Change tracking** — Process merged PRs into per-entity changelogs that accumulate institutional memory of how governance evolves
- **PR analysis** — Analyze open or merged PRs against the current Atlas and historical context
- **On-chain governance data** — Delegation snapshots, poll vote matrix, executive hat/supporter monitoring via the vote.sky.money API
- **Executive vote lifecycle** — Full proposal text fetched from `sky-ecosystem/executive-votes`, parsed into actions with authorizations, spell lifecycle tracking (proposed/hat/cast/expired), and Atlas PR cross-references. Optionally enriched with market data when available.
- **Delegate tracking** — Per-AD profiles with on-chain voting records and forum vote rationales
- **Market data** *(optional)* — Daily price and supply data for SKY, USDS, sUSDS, SPK, BTC, ETH from the Messari API. Requires `MESSARI_API_KEY`.
- **Forum search** — Cache and search Sky Forum governance discussions via RSS

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI
- Python 3.8+ with a virtual environment at `.venv/` (setup creates this automatically)
- `curl` — for GitHub REST API calls (pre-installed on macOS)
- `jq` — for JSON queries (`brew install jq` on macOS)
- `MESSARI_API_KEY` in `.env` — **optional**, enables market data (SKY/USDS/SPK prices). All other features work without it.

## Setup

Clone this repo and run your first Claude Code session in it:

```bash
git clone https://github.com/your-org/sky-atlas-explorer.git
cd sky-atlas-explorer
claude
```

On the first session, the **SessionStart hook** automatically:
1. Clones the Atlas repo (shallow) into `.atlas-repo/`
2. Builds the document index at `data/index.json`
3. Creates the `history/` directory structure

On subsequent sessions, it pulls the latest Atlas, rebuilds the index, checks for unprocessed merged PRs, and launches background refreshes for forum posts, delegate RSS feeds, voting portal data (delegation, polls, executive), executive proposal lifecycle, and market data.

No manual setup steps are required.

## Skills

Invoke these during a Claude Code session:

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

### `/governance-data` — On-chain governance data

Fetch and analyze delegation snapshots, vote alignment, executive vote lifecycle, and spell monitoring.

```
/governance-data executive        # Hat monitoring + spell lifecycle
/governance-data spell 2026-04-09 # Deep-dive into a specific spell
/governance-data snapshot         # Delegation power snapshot
/governance-data votes            # Poll vote matrix update
/governance-data status           # Data freshness report
```

### `/ad-track` — Delegate tracking

Process cached AD vote rationales from forum RSS into per-delegate profiles.

```
/ad-track
```

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
  forum/              Cached forum posts and search index
  delegates/          Cached AD vote rationales from RSS feeds
  voting/
    address-map.json  Voting address → AD slug mapping
    delegates/        Delegation API cache
    polls/            Poll tallies and vote matrix
    executive/        Executive API cache + transient proposal processing dir
    market/           Daily price and supply data (optional, requires Messari API key)
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
snapshots/            Committed time-series (irreproducible, do not delete)
  delegation/         Daily delegation power snapshots
  executive/          Daily hat/supporter snapshots + lifecycle.json
plans/                Implementation plans and handoff docs
scripts/
  core/
    setup.sh                    First-time setup
    refresh.sh                  Pull Atlas, rebuild index, launch background fetches
    build-index.py              Parse Atlas into JSON index
    build-address-map.py        Join voting addresses to AD slugs
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
    fetch-voting-delegates.py   Delegation snapshots from vote.sky.money
    fetch-voting-polls.py       Poll vote matrix from vote.sky.money
    fetch-voting-executive.py   Hat/supporter snapshots from vote.sky.money
    fetch-executive-proposals.py  Proposal lifecycle: fetch, parse, enrich, cleanup
    fetch-delegation-history.py Delegation lock/unlock event history
  market/
    fetch-market-data.py        Price/supply data from Messari API (optional)
    market-lookup.py            Look up cached market data by date
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

## License

Apache 2.0 — see [LICENSE](LICENSE).

The Sky Atlas content accessed by this tooling is maintained by the Sky ecosystem at [sky-ecosystem/next-gen-atlas](https://github.com/sky-ecosystem/next-gen-atlas), also under the Apache 2.0 license.
