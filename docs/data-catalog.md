# Data Catalog

Master index of all data directories, their sources, and refresh behavior. Read this to understand where data lives and how it gets there.

## Directories

| Directory | Source | Committed | Refresh Trigger | Script |
|-----------|--------|-----------|-----------------|--------|
| `data/index.json` | Atlas parse | No | Every session | `scripts/build-index.py` |
| `data/voting/address-map.json` | Delegate profiles | No | Every session | `scripts/build-address-map.py` |
| `data/forum/` | Forum RSS | No | Every session (bg) | `scripts/fetch-forum.py` |
| `data/delegates/` | Per-AD forum RSS | No | Every session (bg) | `scripts/fetch-delegates.py` |
| `data/voting/delegates/` | vote.sky.money API | No | Every session (bg) | `scripts/fetch-voting-delegates.py` |
| `data/voting/polls/` | vote.sky.money API | No | Every session (bg) | `scripts/fetch-voting-polls.py` |
| `data/voting/executive/` | vote.sky.money API | No | Every session (bg) | `scripts/fetch-voting-executive.py` |
| `snapshots/delegation/` | vote.sky.money API | **Yes** | Daily (deduped) | `scripts/fetch-voting-delegates.py` |
| `snapshots/executive/` | vote.sky.money API | **Yes** | Daily (deduped) | `scripts/fetch-voting-executive.py` |
| `delegates/` | Processed forum data | **Yes** | On `/ad-track` or `/governance-data enrich` | Agent-driven |
| `history/` | Processed PR data | **Yes** | On `/atlas-track` | Agent-driven |

## Key concepts

- **Gitignored (`data/`):** Reproducible caches rebuilt from external sources on each session. Safe to delete.
- **Committed (`snapshots/`):** Irreproducible time-series. Once a day passes, that governance state can't be re-fetched. Committed so it survives repo clones.
- **Committed (`delegates/`, `history/`):** Curated institutional memory. Agent-processed, human-reviewed.

## Refresh chain

On session start, `scripts/refresh.sh` runs:
1. Atlas pull + index rebuild (blocking)
2. Address map rebuild (blocking)
3. Background fetches (non-blocking): forum, delegate RSS, voting delegates, voting polls, voting executive

Background fetches always exit 0 — failures are advisory, not blocking.

## Adding a new data source

1. Create `scripts/fetch-{name}.sh` (bash wrapper) + `scripts/fetch-{name}.py` (logic)
2. Add a background job to `scripts/refresh.sh`
3. Add a row to this catalog
4. Update `CLAUDE.md` project layout
5. If time-series data is involved, add a committed `snapshots/{name}/` directory
