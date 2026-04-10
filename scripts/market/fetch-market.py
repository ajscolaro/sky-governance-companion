#!/usr/bin/env python3
"""Fetch daily market data from Messari API into SQLite.

Incremental by default: checks the latest date in the db and fetches
only new days. On first run, migrates any existing JSON dumps from
data/voting/market/ then fetches from the Messari API.

Requires MESSARI_API_KEY in .env or environment.

Usage:
    python3 scripts/market/fetch-market.py              # incremental
    python3 scripts/market/fetch-market.py --backfill    # full history from launch
    python3 scripts/market/fetch-market.py --quiet       # suppress output (startup)
    python3 scripts/market/fetch-market.py --migrate     # migrate JSON dumps only
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Allow importing market module from same directory
sys.path.insert(0, str(Path(__file__).resolve().parent))
from market import MarketDB, ASSETS

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
LEGACY_DIR = PROJECT_DIR / "data" / "voting" / "market"
ENV_FILE = PROJECT_DIR / ".env"

API_BASE = "https://api.messari.io/metrics/v2"
FETCH_TIMEOUT = 30
REQUEST_DELAY = 1.0
MAX_RETRIES = 3
RETRY_BACKOFF = 5

LAUNCH_DATE = "2024-09-18"

# Messari asset UUIDs
ASSET_IDS = {
    "sky":   "6b4833f7-4671-4074-9de6-93d6c40bd739",
    "usds":  "5b9504b4-fc14-4ec5-af2b-4ba1bd496cfe",
    "susds": "9126cdbb-1903-4e99-bc7f-2aa0df86476a",
    "spk":   "b09a349b-f941-4fff-8820-32398dd88839",
    "btc":   "1e31218a-e44e-4285-820c-8282ee222035",
    "eth":   "21c795f5-1bfd-40c3-858e-e9d7e820c6d0",
}


def load_api_key() -> str | None:
    key = os.environ.get("MESSARI_API_KEY")
    if key:
        return key
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if line.startswith("MESSARI_API_KEY="):
                return line.split("=", 1)[1].strip().strip("\"'")
    return None


def api_get(path: str, api_key: str) -> dict:
    url = f"{API_BASE}{path}"
    backoff = RETRY_BACKOFF
    for attempt in range(MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers={
                "x-messari-api-key": api_key,
                "Accept": "application/json",
            })
            with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < MAX_RETRIES:
                time.sleep(backoff)
                backoff *= 2
                continue
            raise
        except urllib.error.URLError:
            if attempt < MAX_RETRIES:
                time.sleep(backoff)
                backoff *= 2
                continue
            raise


def ts_to_date(ts: int | float) -> str:
    """Convert a unix timestamp to YYYY-MM-DD. Handles seconds and milliseconds."""
    if ts > 1e11:
        ts = ts / 1000
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")


def fetch_asset(slug: str, api_key: str, start: str, end: str,
                quiet: bool = False) -> list[tuple]:
    """Fetch price and/or mcap for an asset from the API.

    Returns list of (date, asset, close, mcap) tuples.
    """
    asset_id = ASSET_IDS[slug]
    info = ASSETS[slug]
    rows_by_date: dict[str, dict] = {}  # date -> {"close": x, "mcap": y}

    for dataset in ["price", "marketcap"]:
        if dataset == "price" and not info["has_price"]:
            continue
        if dataset == "marketcap" and not info["has_mcap"]:
            continue

        path = f"/assets/{asset_id}/metrics/{dataset}/time-series/1d?start={start}T00:00:00Z&end={end}T23:59:59Z"
        try:
            data = api_get(path, api_key)
        except (urllib.error.URLError, OSError) as e:
            if not quiet:
                print(f"    {dataset}: FAILED — {e}", file=sys.stderr)
            continue

        inner = data.get("data", data)
        points = inner.get("points", [])
        if not points:
            series = inner.get("series", [])
            if series:
                points = series[0].get("points", [])

        for p in points:
            date = ts_to_date(p[0])
            entry = rows_by_date.setdefault(date, {})
            if dataset == "price" and len(p) >= 5:
                entry["close"] = p[4]  # OHLCV: index 4 is close
            elif dataset == "marketcap" and len(p) >= 2:
                entry["mcap"] = p[1]

        if not quiet:
            print(f"    {dataset}: {len(points)} points")

        time.sleep(REQUEST_DELAY)

    return [
        (date, slug, vals.get("close"), vals.get("mcap"))
        for date, vals in sorted(rows_by_date.items())
    ]


def migrate_json_dumps(conn, quiet: bool = False) -> int:
    """Migrate existing JSON dump files into the database."""
    if not LEGACY_DIR.exists():
        return 0

    total = 0
    for slug, info in ASSETS.items():
        rows_by_date: dict[str, dict] = {}

        for dataset in ["price", "marketcap"]:
            path = LEGACY_DIR / f"{slug}-{dataset}.json"
            if not path.exists():
                continue
            try:
                with open(path) as f:
                    data = json.load(f)
            except (json.JSONDecodeError, OSError):
                continue

            points = data.get("points", [])
            for p in points:
                date = ts_to_date(p[0])
                entry = rows_by_date.setdefault(date, {})
                if dataset == "price" and len(p) >= 5:
                    entry["close"] = p[4]
                elif dataset == "marketcap" and len(p) >= 2:
                    entry["mcap"] = p[1]

        rows = [
            (date, slug, vals.get("close"), vals.get("mcap"))
            for date, vals in sorted(rows_by_date.items())
        ]
        if rows:
            MarketDB.upsert_rows(conn, rows)
            total += len(rows)
            if not quiet:
                print(f"  Migrated {slug}: {len(rows)} days")

    return total


def fetch_stablecoin_snapshot(api_key: str, quiet: bool = False) -> list[tuple]:
    """Fetch current stablecoin ranking from the stablecoins endpoint.

    Returns list of (date, asset_symbol, supply) tuples for today.
    """
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    rows = []
    page = 1

    while True:
        path = f"/stablecoins?page={page}&limit=25&sort=stablecoin-outstanding-supply-usd&order=desc"
        try:
            # Stablecoins endpoint is under the same base but without /assets
            url = f"https://api.messari.io/metrics/v2{path}"
            backoff = RETRY_BACKOFF
            for attempt in range(MAX_RETRIES + 1):
                try:
                    req = urllib.request.Request(url, headers={
                        "x-messari-api-key": api_key,
                        "Accept": "application/json",
                    })
                    with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
                        data = json.loads(resp.read())
                    break
                except urllib.error.HTTPError as e:
                    if e.code == 429 and attempt < MAX_RETRIES:
                        time.sleep(backoff)
                        backoff *= 2
                        continue
                    raise
        except (urllib.error.URLError, OSError) as e:
            if not quiet:
                print(f"  Stablecoins page {page}: FAILED — {e}", file=sys.stderr)
            break

        inner = data.get("data", data)
        stablecoins = inner.get("data", [])
        if not stablecoins:
            break

        for sc in stablecoins:
            symbol = sc.get("symbol", "")
            supply_data = sc.get("supply", {})
            supply = supply_data.get("outstandingSupplyUsd")
            if symbol and supply is not None:
                rows.append((today, symbol, supply))

        metadata = inner.get("metadata", {})
        total_pages = metadata.get("totalPages", 1)
        if page >= total_pages:
            break
        page += 1
        time.sleep(REQUEST_DELAY)

    if not quiet and rows:
        print(f"  Stablecoins: {len(rows)} assets ranked")

    return rows


def main():
    parser = argparse.ArgumentParser(description="Fetch market data into SQLite")
    parser.add_argument("--quiet", action="store_true", help="Suppress output")
    parser.add_argument("--backfill", action="store_true",
                        help="Fetch full history from launch date")
    parser.add_argument("--migrate", action="store_true",
                        help="Migrate existing JSON dumps only (no API fetch)")
    parser.add_argument("--asset", type=str,
                        help=f"Fetch only this asset ({', '.join(ASSETS.keys())})")
    args = parser.parse_args()

    conn = MarketDB.init_db()

    # Migrate existing JSON data if db is empty
    cur = conn.execute("SELECT COUNT(*) FROM daily")
    db_empty = cur.fetchone()[0] == 0

    if db_empty or args.migrate:
        if not args.quiet:
            print("Migrating existing JSON data...")
        migrated = migrate_json_dumps(conn, quiet=args.quiet)
        if not args.quiet:
            print(f"  Total: {migrated} rows migrated")
        if args.migrate:
            conn.close()
            return

    if args.migrate:
        conn.close()
        return

    api_key = load_api_key()
    if not api_key:
        if not args.quiet:
            print("MESSARI_API_KEY not configured. Skipping API fetch.")
        conn.close()
        return

    # Determine start date
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if args.backfill:
        start = LAUNCH_DATE
    else:
        # Incremental: start from day after latest data
        cur = conn.execute("SELECT MAX(date) FROM daily")
        row = cur.fetchone()
        if row and row[0]:
            from datetime import timedelta
            last = datetime.strptime(row[0], "%Y-%m-%d")
            start = (last + timedelta(days=1)).strftime("%Y-%m-%d")
        else:
            start = LAUNCH_DATE

    if start > today:
        if not args.quiet:
            print(f"Price data up to date ({start} > {today})")
        # Still fetch stablecoin snapshot (daily ranking)
        if not args.asset:
            sc_rows = fetch_stablecoin_snapshot(api_key, quiet=args.quiet)
            if sc_rows:
                conn.executemany(
                    "INSERT INTO stablecoin_snapshot (date, asset, supply) VALUES (?, ?, ?) "
                    "ON CONFLICT(date, asset) DO UPDATE SET supply = excluded.supply",
                    sc_rows,
                )
                conn.commit()
        conn.close()
        return

    targets = ASSETS
    if args.asset:
        if args.asset not in ASSETS:
            print(f"Error: Unknown asset '{args.asset}'. "
                  f"Choose from: {', '.join(ASSETS.keys())}", file=sys.stderr)
            sys.exit(1)
        targets = {args.asset: ASSETS[args.asset]}

    if not args.quiet:
        print(f"Fetching market data: {start} -> {today}")

    total = 0
    for slug in targets:
        if not args.quiet:
            print(f"  {ASSETS[slug]['name']}:")
        rows = fetch_asset(slug, api_key, start, today, quiet=args.quiet)
        if rows:
            MarketDB.upsert_rows(conn, rows)
            total += len(rows)

    # Fetch stablecoin rankings (daily snapshot for market share tracking)
    if not args.asset:
        sc_rows = fetch_stablecoin_snapshot(api_key, quiet=args.quiet)
        if sc_rows:
            conn.executemany(
                "INSERT INTO stablecoin_snapshot (date, asset, supply) VALUES (?, ?, ?) "
                "ON CONFLICT(date, asset) DO UPDATE SET supply = excluded.supply",
                sc_rows,
            )
            conn.commit()

    conn.close()

    if not args.quiet:
        # Report db state
        db = MarketDB()
        dr = db.date_range()
        if dr:
            print(f"\nMarket DB: {db.row_count()} rows, {dr[0]} to {dr[1]}")
        db.close()


if __name__ == "__main__":
    main()
