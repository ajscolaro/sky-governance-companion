---
name: market-data
description: >
  Query local market database for price, supply, stablecoin market share, and governance event
  impact analysis. Uses data/market.db (SQLite) populated from Messari API. Covers SKY, USDS+DAI,
  sUSDS, SPK, BTC, ETH daily data from Sep 2024 to present, plus stablecoin competitive rankings.
argument-hint: "<query in natural language, e.g. 'USDS supply growth vs competitors' or 'SKY/ETH ratio last 90 days'>"
allowed-tools: Bash, Read, Grep, Glob
---

# Market Data

You have a local SQLite database (`data/market.db`) with daily market data. **Always use the `MarketDB` class to query it — never write raw SQL, and never call Messari MCP tools for data that is already local.**

## What's in the database

| Table | Contents | Coverage |
|-------|----------|----------|
| `daily` | price (close) and market cap per asset per day | Sep 2024 → present |
| `stablecoin_snapshot` | all stablecoins ranked by supply | current day only (not historical) |

**Tracked assets in `daily`:**
- `sky` — governance token (price + mcap)
- `usds` — stablecoin supply; **includes DAI** (Messari aggregates DAI into USDS). Label as "USDS+DAI" when presenting
- `susds` — staked USDS (mcap only)
- `spk` — Spark agent token (price + mcap)
- `btc`, `eth` — benchmarks (price only)

## How to query — always use MarketDB

```python
import sys; sys.path.insert(0, "scripts/market")
from market import MarketDB
db = MarketDB()
```

### Point queries
```python
db.get_price("SKY", "2026-04-09")       # -> 0.078 (float or None)
db.get_mcap("USDS", "2026-04-09")       # -> 11500000000.0 (USDS+DAI supply)
```

### Time series
```python
# Price over time
db.get_range("sky", "2025-01-01", "2025-12-31")               # -> [(date, close), ...]

# Supply over time — this is how you answer "how did USDS supply change?"
db.get_range("usds", "2024-10-01", "2026-04-10", field="mcap") # -> [(date, supply), ...]

# sUSDS supply over time
db.get_range("susds", "2024-12-01", "2026-04-10", field="mcap")
```

### Deltas (percent change)
```python
db.get_delta("SKY", "2026-04-09", days=7)    # -> -4.0 (percent, float or None)
db.get_delta("SKY", "2026-04-09", days=-7)   # negative days = backward-looking
```

### Cross-asset snapshots
```python
db.get_context("2026-04-09")        # -> {"date": ..., "sky": 0.078, "usds_mcap": 11.5e9, "btc": 71773, ...}
db.get_event_window("2026-04-09")   # -> price behavior -3d/+7d around a governance event
```

### Derived ratios (computed on the fly from existing prices)
```python
db.get_ratio("SKY", "BTC", "2026-04-09")                           # -> 0.0000010876
db.get_ratio_range("SKY", "ETH", "2026-01-01", "2026-04-10")       # -> [(date, ratio), ...]
db.get_ratio_delta("SKY", "BTC", "2026-04-09", days=7)             # -> percent change in ratio
```

### Stablecoin competitive positioning
```python
# Current-day snapshot only (not historical — we only have one snapshot per fetch)
share = db.get_stablecoin_share("2026-04-10")
# -> {"usds_rank": 3, "usds": {"supply": 11.5e9, "share_pct": 3.89},
#     "total_supply": 295.6e9, "stablecoins": [{rank, asset, supply, share_pct}, ...]}
```

**Important:** `get_stablecoin_share()` uses the asset-level marketcap for USDS (from the `daily` table) for accuracy, not the raw stablecoin snapshot value. The label is automatically changed to "USDS+DAI".

### Formatting helpers
```python
from market import format_context, fmt_price, fmt_supply, fmt_pct
format_context(db, "2026-04-09")
# -> "SKY ~$0.0781 (down 4.0% WoW), USDS supply $11.51B, SPK ~$0.0199 ..."
```

## CLI alternative

For quick lookups without Python:
```bash
python3 scripts/market/market-lookup.py --date 2026-04-09                    # snapshot
python3 scripts/market/market-lookup.py --date 2026-04-09 --format context   # prose
python3 scripts/market/market-lookup.py --range 2025-01-01 2025-12-31        # period comparison
python3 scripts/market/market-lookup.py --window 2026-04-09                  # event window
python3 scripts/market/market-lookup.py --ratio SKY BTC                      # ratio (last 30d)
python3 scripts/market/market-lookup.py --ratio SKY ETH --range 2025-06-01 2026-04-10
python3 scripts/market/market-lookup.py --stablecoins                        # market share
python3 scripts/market/market-lookup.py --check                              # data freshness
```

## Common analysis patterns

### "How did USDS supply change over time?"
```python
data = db.get_range("usds", "2024-10-01", "2026-04-10", field="mcap")
# Compute week-over-week growth, find inflection points, etc.
```

### "Did price react to a governance event?"
```python
window = db.get_event_window("2026-04-09")  # poll end / spell cast / PR merge date
# Shows each asset's price and % change before/after the event
```

### "How is SKY performing vs BTC/ETH?"
```python
ratios = db.get_ratio_range("SKY", "BTC", "2025-01-01", "2026-04-10")
# Declining ratio = SKY underperforming BTC; rising = outperforming
```

### "Where does USDS rank vs competitors?"
```python
share = db.get_stablecoin_share("2026-04-10")
# Note: this is current-day only. For historical competitive analysis,
# use get_range("usds", ..., field="mcap") for USDS supply time series
# and note that competitor supply history is not in the local db.
```

## Cross-referencing with governance events

Market data is most useful when correlated with governance actions:
- **`history/_log.md`** — merged Atlas PR dates, for correlating supply/price with Atlas changes
- **`snapshots/executive/lifecycle.json`** — spell proposed/hat/cast dates
- **`data/voting/polls/vote-matrix.json`** — poll end dates (especially `atlas-edit` polls)

Example workflow: find USDS supply inflection points, then check `_log.md` and `lifecycle.json` for governance events within ±7 days.

### Reading vote-matrix.json safely

When reading poll data from `data/voting/polls/vote-matrix.json`, note these field types:
- `tags` — always a list of **strings** (e.g., `["high-impact", "weekly"]`), never dicts
- `poll_type` — string: `"atlas-edit"`, `"parameter-change"`, or `"other"`
- `atlas_pr` — integer PR number (only on atlas-edit polls) or absent
- `discussion_link`, `summary`, `poll_url` — strings, may be absent on older polls
- `ad_votes` — dict of `{slug: {option, option_id, sky_weight, chain, timestamp}}`
- `ad_non_voters` — list of slug strings

## Refreshing data

Data is fetched automatically on session start (`scripts/market/fetch-market.py`). To manually refresh:
```bash
python3 scripts/market/fetch-market.py              # incremental (new days only)
python3 scripts/market/fetch-market.py --backfill    # full history
python3 scripts/market/fetch-market.py --asset sky   # single asset
```

Requires `MESSARI_API_KEY` in `.env`. Without it, existing data is still queryable.

## What NOT to do

- **Don't write raw SQL** against `data/market.db` — use `MarketDB` methods
- **Don't call Messari MCP tools** (`get_timeseries`, `get_timeseries_catalog`, etc.) for data in the local db
- **Don't read the old JSON files** in `data/voting/market/` — they are legacy, the db is the source of truth
- **Don't assume `stablecoin_snapshot` has historical data** — it's current-day rankings only
