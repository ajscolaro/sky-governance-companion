# Data Catalog

Master index of all data directories, their sources, and refresh behavior. Read this to understand where data lives and how it gets there.

## Directories

| Directory | Source | Committed | Refresh Trigger | Script |
|-----------|--------|-----------|-----------------|--------|
| `data/index.json` | Atlas parse | No | Session start (hook) + `/refresh` | `scripts/core/build-index.py` |
| `data/voting/address-map.json` | Delegate profiles | No | Session start (hook) + `/refresh` | `scripts/core/build-address-map.py` |
| `data/forum/` | Forum RSS | No | `/refresh` | `scripts/forum/fetch-forum.py` |
| `data/forum/registry.json` | Atlas A.2.7.1.1.1.1 (Authorized Forum Accounts) | No | `/refresh` | `scripts/forum/build-account-registry.py` |
| `data/delegates/` | Per-AD forum RSS | No | `/refresh` | `scripts/delegates/fetch-delegates.py` |
| `data/voting/delegates/` | vote.sky.money API | No | `/refresh` | `scripts/voting/fetch-voting-delegates.py` |
| `data/voting/polls/` | vote.sky.money API | No | `/refresh` | `scripts/voting/fetch-voting-polls.py` |
| `data/voting/executive/` | vote.sky.money API | No | `/refresh` | `scripts/voting/fetch-voting-executive.py` |
| `data/voting/executive/proposals/` | sky-ecosystem/executive-votes repo | No | `/refresh` | `scripts/voting/fetch-executive-proposals.py` |
| `data/market.db` | Messari API *(optional)* | No | `/refresh` (if API key set) | `scripts/market/fetch-market.py` |
| `data/github/open-prs.json` | GitHub API (next-gen-atlas open PRs) | No | `/refresh` | `scripts/github/fetch-open-prs.sh` |
| `data/voting/delegation-history/` | vote.sky.money API | No | On-demand | `scripts/voting/fetch-delegation-history.py` |
| `data/voting/executive/lifecycle.json` | vote.sky.money API + executive-votes repo | No | `/refresh` | `scripts/voting/fetch-executive-proposals.py` |
| `delegates/` | Processed forum data | **Yes** | On `/ad-track` or `/governance-data enrich` | Agent-driven |
| `history/` | Processed PR data | **Yes** | Auto-rendered on `/refresh` (5-stage pipeline); status=`auto` | `scripts/atlas/process-pr.sh` |
| `tmp/` | Per-PR pipeline artifacts | No | Each `process-pr.sh` run | `scripts/atlas/process-pr.sh` |

## Key concepts

- **Gitignored (`data/`):** Reproducible caches rebuilt from external sources. Safe to delete.
- **Optional (`data/market.db`):** Requires `MESSARI_API_KEY` in `.env` to populate. All other features work without it. Query via `scripts/market/market.py` (`MarketDB` class), never raw SQL.
- **Committed (`delegates/`, `history/`):** Curated institutional memory. Agent-processed, human-reviewed. Changelog entries in `history/` are optimized for RAG/grep retrieval (terse, predictable `## PR #N` / `**Merged:**` / `**Type:**` structure with inline UUIDs and Atlas paths); sorted most-recent-first via `scripts/core/sort-changelogs.py`.

## Refresh chain

**On session start (automatic, fast):** `scripts/core/atlas-sync.sh` pulls the latest Atlas, rebuilds `data/index.json` and the address map. Nothing else.

**On `/refresh` (user-invoked):** `scripts/core/refresh.sh` runs:
1. Parallel fetches: forum, delegate RSS, voting delegates/polls/executive, market data, open PRs, unprocessed-PR discovery
2. Auto-process any unprocessed merged PRs via `scripts/atlas/process-pr.sh` (5-stage pipeline → fully-rendered entries in `history/<entity>/changelog.md`, status=`auto` in `_log.md`)
3. Session briefing (reads fresh data, prints sections with content only)

`/refresh` does **not** re-sync the Atlas git repo or rebuild the index — that's owned by the SessionStart hook. If the user needs fresh Atlas commits mid-session, restart Claude to re-trigger the hook.

Background fetches always exit 0 — failures are advisory, not blocking.

## Auto-changelog pipeline artifacts (`tmp/`)

Each `process-pr.sh` run produces these files in `tmp/` for the duration of the session (gitignored, cleared by the SessionStart hook):

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

## Poll data fields

Each poll in `data/voting/polls/vote-matrix.json` includes:
- `poll_type`: `atlas-edit` (Flow 1 — text changes, PR merges same day), `parameter-change` (Flow 2 — authorizes executive spell), or `other`
- `atlas_pr`: PR number in next-gen-atlas (atlas-edit polls only, extracted from poll content)
- `discussion_link`: Forum thread URL
- `summary`: Proposal summary text
- `poll_url`: Raw poll markdown on GitHub
- `ad_votes` / `ad_non_voters`: Per-delegate voting data

## Adding a new data source

1. Create the script in the appropriate `scripts/{category}/` subdirectory
2. Add a background job to `scripts/core/refresh.sh`
3. Add a row to this catalog
4. Update `CLAUDE.md` project layout
5. If the data is committed (not gitignored), document why
