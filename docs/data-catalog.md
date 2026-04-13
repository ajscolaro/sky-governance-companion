# Data Catalog

Master index of all data directories, their sources, and refresh behavior. Read this to understand where data lives and how it gets there.

## Directories

| Directory | Source | Committed | Refresh Trigger | Script |
|-----------|--------|-----------|-----------------|--------|
| `data/index.json` | Atlas parse | No | Every session | `scripts/core/build-index.py` |
| `data/voting/address-map.json` | Delegate profiles | No | Every session | `scripts/core/build-address-map.py` |
| `data/forum/` | Forum RSS | No | Every session (bg) | `scripts/forum/fetch-forum.py` |
| `data/delegates/` | Per-AD forum RSS | No | Every session (bg) | `scripts/delegates/fetch-delegates.py` |
| `data/voting/delegates/` | vote.sky.money API | No | Every session (bg) | `scripts/voting/fetch-voting-delegates.py` |
| `data/voting/polls/` | vote.sky.money API | No | Every session (bg) | `scripts/voting/fetch-voting-polls.py` |
| `data/voting/executive/` | vote.sky.money API | No | Every session (bg) | `scripts/voting/fetch-voting-executive.py` |
| `data/voting/executive/proposals/` | sky-ecosystem/executive-votes repo | No | Every session (bg) | `scripts/voting/fetch-executive-proposals.py` |
| `data/market.db` | Messari API *(optional)* | No | Every session (bg, if API key set) | `scripts/market/fetch-market.py` |
| `data/voting/delegation-history/` | vote.sky.money API | No | On-demand | `scripts/voting/fetch-delegation-history.py` |
| `data/voting/executive/lifecycle.json` | vote.sky.money API + executive-votes repo | No | Every session | `scripts/voting/fetch-executive-proposals.py` |
| `delegates/` | Processed forum data | **Yes** | On `/ad-track` or `/governance-data enrich` | Agent-driven |
| `history/` | Processed PR data | **Yes** | On `/atlas-track` | Agent-driven |

## Key concepts

- **Gitignored (`data/`):** Reproducible caches rebuilt from external sources on each session. Safe to delete.
- **Optional (`data/market.db`):** Requires `MESSARI_API_KEY` in `.env` to populate. All other features work without it. Query via `scripts/market/market.py` (`MarketDB` class), never raw SQL.
- **Committed (`delegates/`, `history/`):** Curated institutional memory. Agent-processed, human-reviewed.

## Refresh chain

On session start, `scripts/core/refresh.sh` runs:
1. Atlas pull + index rebuild (blocking)
2. Address map rebuild (blocking)
3. Unprocessed PR check (blocking)
4. Background fetches (non-blocking): forum, delegate RSS, voting delegates, voting polls, voting executive, market data
5. Governance status advisory (blocking, reads cached data from previous session)

Background fetches always exit 0 — failures are advisory, not blocking.

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
