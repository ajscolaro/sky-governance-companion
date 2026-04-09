# Snapshots

Committed time-series data from the Sky Voting Portal API (`vote.sky.money`).

This data **cannot be re-fetched** — once a point in time passes, that governance state is gone. That's why it's committed, unlike the reproducible caches in `data/`.

## Structure

```
snapshots/
├── delegation/           # Daily delegation power snapshots
│   └── YYYY-MM-DD.json   # SKY delegated per AD, delegator counts, participation
└── executive/            # Daily executive spell snapshots
    └── YYYY-MM-DD.json   # Current hat, who supports which spell, SKY amounts
```

## How snapshots are created

- **Delegation:** `scripts/fetch-voting-delegates.py` writes one snapshot per day (deduped by date)
- **Executive:** `scripts/fetch-voting-executive.py` writes one snapshot per day (deduped by date)
- Both run in the background during `scripts/refresh.sh` (session start)

## Schema

See `docs/data-catalog.md` for the full data directory index. See the fetch scripts for detailed field documentation.
