# Local Data Catalog & Repo Map

Master index of everything local. **Always check here first before reaching for GitHub, the web, or other external sources** — the whole point of this project is to streamline navigation through the curated layer.

## Top-level layout

| Path | What | Committed |
|------|------|-----------|
| `.atlas-repo/` | Shallow clone of `sky-ecosystem/next-gen-atlas` (auto-refreshed by SessionStart hook; **deny-write**) | No |
| `.claude/` | Skills, slash commands, settings, hooks | Yes |
| `.venv/` | Python virtualenv — use for any Python execution | No |
| `CLAUDE.md` | Project instructions for Claude (always loaded) | Yes |
| `README.md` / `LICENSE` | Repo-level docs | Yes |
| `data/` | All cached/derived data — gitignored, reproducible | No |
| `delegates/` | Curated AD profiles + per-AD vote rationale logs | **Yes** |
| `docs/` | Reference docs (this catalog, governance reference, security) | Yes |
| `history/` | Curated per-entity Atlas changelog — institutional memory | **Yes** |
| `intel-drafts/` | Drafts produced by `/messari-atlas-edit-drafter` | Yes (dir only; outputs are session artifacts) |
| `plans/` | Committed plan docs from past project work | Yes |
| `scripts/` | All tooling, organized by domain | Yes |
| `tmp/` | Ephemeral working files (PR bodies, diffs, pipeline artifacts) | No |

## `.atlas-repo/` — the Atlas mirror

Shallow clone (depth 20) of `sky-ecosystem/next-gen-atlas`. **`main` is canonical.** Refreshed by the SessionStart hook only; never written to by Claude (sandbox + PreToolUse hook both block it). For Atlas content, prefer `/atlas-navigate` and `data/index.json` over reading raw files here — the index is faster and the skill carries the right conventions.

## `data/` — cached & derived (gitignored)

| Path | Source | Refresh trigger | Producer |
|------|--------|-----------------|----------|
| `data/index.json` | Parsed Atlas (`.atlas-repo/`) | SessionStart hook + `/refresh` | `scripts/core/build-index.py` |
| `data/voting/address-map.json` | Delegate profiles | SessionStart hook + `/refresh` | `scripts/core/build-address-map.py` |
| `data/forum/` | Forum RSS (`forum.skyeco.com`) | `/refresh` | `scripts/forum/fetch-forum.py` |
| `data/forum/registry.json` | Atlas A.2.7.1.1.1.1 (Authorized Forum Accounts) | `/refresh` | `scripts/forum/build-account-registry.py` |
| `data/forum/posts/` | Per-topic JSON (opening post only, sanitized, 8KB body cap) | `/refresh` | `scripts/forum/fetch-forum.py` |
| `data/delegates/` | Per-AD Discourse thread RSS (sanitized) | `/refresh` | `scripts/delegates/fetch-delegates.py` |
| `data/voting/delegates/` | vote.sky.money API (delegate metadata) | `/refresh` | `scripts/voting/fetch-voting-delegates.py` |
| `data/voting/delegates/delegators/` | Per-delegate delegator lists | `/refresh` | (same) |
| `data/voting/delegates/snapshots/` | Point-in-time delegation snapshots | `/refresh` | (same) |
| `data/voting/delegation-history/` | Per-delegate delegation events | On-demand | `scripts/voting/fetch-delegation-history.py` |
| `data/voting/polls/vote-matrix.json` | Polls + per-AD votes | `/refresh` | `scripts/voting/fetch-voting-polls.py` |
| `data/voting/polls/tallies/` | Per-poll tally JSON | `/refresh` | (same) |
| `data/voting/executive/lifecycle.json` | Spell lifecycle (curated output) | `/refresh` | `scripts/voting/fetch-executive-proposals.py` |
| `data/voting/executive/index.json` | Spell index from vote.sky.money | `/refresh` | `scripts/voting/fetch-voting-executive.py` |
| `data/voting/executive/proposals.json` | Combined proposal metadata | `/refresh` | (same) |
| `data/voting/executive/hat.json` | Current hat address | `/refresh` | (same) |
| `data/voting/executive/supporters.json` | Per-spell support state | `/refresh` | (same) |
| `data/voting/executive/snapshots/` | Historical hat/supporter snapshots | `/refresh` | (same) |
| `data/voting/executive/proposals/` | Transient cache for proposal bodies (parsed then deleted) | `/refresh` | `scripts/voting/fetch-executive-proposals.py` |
| `data/voting/market/` | Price/mcap JSON for SKY, SPK, USDS, sUSDS, BTC, ETH (8 files) | `/refresh` | `scripts/voting/fetch-voting-*.py` (used for vote-impact analysis) |
| `data/market.db` | SQLite — daily price/mcap from Messari API *(optional, needs `MESSARI_API_KEY`)* | `/refresh` | `scripts/market/fetch-market.py` |
| `data/github/open-prs.json` | Open (non-draft) PRs from next-gen-atlas | `/refresh` | `scripts/github/fetch-open-prs.sh` |

### Key data schemas

**`data/voting/polls/vote-matrix.json`** — keyed by poll ID. Each poll has:
- `title`, `start_date`, `end_date`, `result`
- `poll_type`: `atlas-edit` (Flow 1 — text change, PR merges same day) | `parameter-change` (Flow 2 — authorizes spell) | `other`
- `atlas_pr` (integer) — links Flow 1 polls to their Atlas PR
- `ad_votes` (per-AD option/weight/chain), `ad_non_voters`
- `discussion_link`, `summary`, `poll_url`

**`data/voting/executive/lifecycle.json`** — `spells` dict keyed by address. Each spell has:
- `title`, `date`, `key`, `proposal_url`
- `events` (proposed/hat/cast/expired with timestamps)
- `actions` — high-level descriptions only; specific parameter values (amounts, rates) are deliberately excluded — fetch full text via `proposal_url`
- `governance_polls`, `atlas_prs`

**`data/market.db`** — SQLite schema:
- `daily(date, asset, close, mcap)`
- `stablecoin_snapshot(date, asset, supply)`
- No `daily_prices` table, no `volume` column. **Never write raw SQL** — use `MarketDB` class (`from market import MarketDB`), the CLI (`scripts/market/market-lookup.py`), or invoke `/messari-market-data`.

**`data/forum/registry.json`** — Authorized Forum Accounts (Atlas `A.2.7.1.1.1.1.4.0.6.1`):
- `entities` — forward map
- `by_handle` — case-insensitive reverse map (`entity`/`role`/`type`/`display_handle`)
- `transitive_refs` — expansions for "(and their authorized representatives)"

## `delegates/` — curated AD profiles (committed)

- `_roster.md` — canonical AD index (source of truth for who's currently aligned)
- `README.md` — directory conventions
- `<slug>/` — per-AD profile (`profile.md`, `comms.md` with processed vote rationales)
- Processed from forum/delegate data via `/ad-track` and `/governance-data enrich`

## `history/` — institutional memory (committed)

Per-entity Atlas changelogs, routed by the most specific matching prefix in `entity-routing.conf`. Entries are auto-rendered from PRs via the 5-stage pipeline (status=`auto` in `_log.md`).

- `_log.md` — master PR index (PR # → title, merge date, sections affected, status)
- `entity-routing.conf` — Atlas-prefix → history-dir mapping
- `A.{0..6}--<scope>/` — per-scope subtrees; agents live under `A.6--agents/<slug>/`
- Each leaf has a `changelog.md` sorted most-recent-first (via `scripts/core/sort-changelogs.py`)

Entry format: terse, predictable, RAG/grep-friendly. `## PR #N — Title` header, `**Merged:** date | **Type:** governance-path` metadata, then `### Material Changes` and/or `### Housekeeping`, then `### Context` (1-2 sentences). Target length 5-15 lines substantive, 3-5 trivial.

## `intel-drafts/` & `plans/` — working docs (committed)

- `intel-drafts/` — output dir for `/messari-atlas-edit-drafter` (Messari-style Atlas-Edit-poll summaries). Typically empty between drafting sessions.
- `plans/` — committed planning/spec docs from past project work (atomization migration, executive-vote monitoring design, forum-account registry, etc.). Read these for historical context on how a feature was built.

## `scripts/` — tooling

Organized by domain. **Prefer invoking the right `/skill` over running scripts directly**, but here's where things live:

| Subdir | Purpose |
|--------|---------|
| `scripts/core/` | Setup, refresh orchestrator, Atlas sync, index/address-map builders, session briefing, sort, PreToolUse write-path hook |
| `scripts/atlas/` | PR processing pipeline (`process-pr.sh` + 6 stages), search/read index, subtree compose, `search-history.py` (backing `/history-search`) |
| `scripts/forum/` | Forum RSS fetch, Authorized Forum Accounts registry build, roster cross-check |
| `scripts/delegates/` | AD vote-rationale fetch (per-AD Discourse RSS, sanitized) |
| `scripts/voting/` | vote.sky.money API ingestion (polls, delegates, executive, delegation history) |
| `scripts/market/` | Messari market-data fetch + SQLite query layer (`MarketDB`, `market-lookup.py`) |
| `scripts/github/` | GitHub API helpers (open-PRs fetch) |

## `.claude/` — agent surface

- `.claude/settings.json` — sandbox config, permissions, hooks (PreToolUse → `scripts/core/check-write-path.sh`)
- `.claude/skills/<name>/SKILL.md` — skill instructions. The eight project skills (`refresh`, `atlas-navigate`, `atlas-analyze`, `atlas-track`, `governance-data`, `forum-search`, `ad-track`, `messari-market-data`) all live here.
- `.claude/commands/` — slash-command definitions (e.g. `messari-atlas-edit-drafter.md`)

## `docs/` — reference

- `docs/data-catalog.md` — **this file** (routing index)
- `docs/governance-reference.md` — proposal types, governance roles, three flows, on-chain verification
- `docs/security.md` — sandbox model, PreToolUse hook, RSS sanitization, threat model

## Refresh chain

**SessionStart hook (automatic, fast):** `scripts/core/atlas-sync.sh` pulls the latest Atlas (or `first-run-welcome.sh` if `.atlas-repo/.git` is absent), rebuilds `data/index.json` and the address map. Nothing else.

**`/refresh` (user-invoked):** `scripts/core/refresh.sh` runs:
1. Parallel fetches: forum, delegate RSS, voting (delegates/polls/executive), market data, open PRs, unprocessed-PR discovery
2. Auto-process any unprocessed merged PRs via `scripts/atlas/process-pr.sh` (5-stage pipeline → fully-rendered entries in `history/<entity>/changelog.md`, status=`auto` in `_log.md`)
3. Session briefing (reads fresh data, prints sections with content only)

`/refresh` does **not** re-sync the Atlas git repo or rebuild the index — that's owned by the SessionStart hook. If you need fresh Atlas commits mid-session, restart Claude.

Background fetches always exit 0 — failures are advisory, not blocking.

## Auto-changelog pipeline artifacts (`tmp/`)

Each `process-pr.sh` run produces these files in `tmp/` (gitignored, cleared by the SessionStart hook):

| File | Producer | Contents |
|------|----------|----------|
| `pr-<N>.diff` | `process-pr.sh` (via `git diff sha~..sha`) | Unified diff of the PR |
| `pr-<N>-body.md` | `process-pr.sh` | Squash-merge commit body (= PR body) |
| `pr-<N>-meta.json` | `process-pr.sh` | `number`, `title`, `merged_at`, `additions`, `deletions`, `body`, `merge_sha` |
| `pr-<N>-manifest.json` | `classify-diff.py` | Per-doc add/delete/modify/rename + UUIDs + targets |
| `pr-<N>-extracted.json` | `extract-values.py` | Body-level deltas (numerics, addresses, sweeps, paired changes) |
| `pr-<N>-enriched.json` | `enrich.py` | Manifest + governance flow + poll/spell + entity routing |
| `pr-<N>-rendered.json` | `render.py` | Per-entity markdown entries (Material/Housekeeping bullets) |
| `pr-<N>-final.json` | `auto-context.py` | Same as rendered, plus filled Context paragraphs (or stripped) |

The pipeline is idempotent — re-running on the same PR with `--force` regenerates all artifacts and overwrites the changelog entry block.

## Adding a new data source

1. Create the fetch script under the appropriate `scripts/<category>/`
2. Add a background job to `scripts/core/refresh.sh`
3. Add a row to the table in this file (and a key-schema block if the shape is non-obvious)
4. If the data is committed (not gitignored), document why
