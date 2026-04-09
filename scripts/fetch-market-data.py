#!/usr/bin/env python3
"""Fetch historical market data for SKY, USDS, and sUSDS from the Messari API.

One-time backfill + incremental updates. Stores daily price and supply data
in data/voting/market/ as JSON files.

Requires MESSARI_API_KEY in .env or environment.
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

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "data" / "voting" / "market"
ENV_FILE = PROJECT_DIR / ".env"

API_BASE = "https://api.messari.io/metrics/v2"
FETCH_TIMEOUT = 30
REQUEST_DELAY = 1.0
MAX_RETRIES = 3
RETRY_BACKOFF = 5

# Sky ecosystem assets
ASSETS = {
    "sky": {
        "id": "6b4833f7-4671-4074-9de6-93d6c40bd739",
        "name": "SKY",
        "datasets": ["price", "marketcap"],
    },
    "usds": {
        "id": "5b9504b4-fc14-4ec5-af2b-4ba1bd496cfe",
        "name": "USDS",
        "datasets": ["marketcap"],
    },
    "susds": {
        "id": "9126cdbb-1903-4e99-bc7f-2aa0df86476a",
        "name": "sUSDS",
        "datasets": ["marketcap"],
    },
    "spk": {
        "id": "b09a349b-f941-4fff-8820-32398dd88839",
        "name": "SPK",
        "datasets": ["price", "marketcap"],
    },
}

LAUNCH_DATE = "2024-09-18T00:00:00Z"


def load_api_key() -> str:
    """Load Messari API key from .env or environment."""
    key = os.environ.get("MESSARI_API_KEY")
    if key:
        return key

    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if line.startswith("MESSARI_API_KEY="):
                return line.split("=", 1)[1].strip().strip("\"'")

    print("Error: MESSARI_API_KEY not found in .env or environment.", file=sys.stderr)
    sys.exit(1)


def api_get(path: str, api_key: str) -> dict:
    """Make a GET request to the Messari API with retry."""
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
            body = e.read().decode("utf-8", errors="replace")[:500]
            print(f"  HTTP {e.code}: {body}", file=sys.stderr)
            raise
        except urllib.error.URLError as e:
            if attempt < MAX_RETRIES:
                time.sleep(backoff)
                backoff *= 2
                continue
            raise


def fetch_timeseries(asset_id: str, dataset: str, api_key: str,
                     start: str, end: str, granularity: str = "1d") -> dict:
    """Fetch timeseries data for an asset."""
    path = f"/assets/{asset_id}/metrics/{dataset}/time-series/{granularity}"
    path += f"?start={start}&end={end}"
    return api_get(path, api_key)


def save_dataset(slug: str, dataset: str, data: dict) -> Path:
    """Save a dataset to disk."""
    outfile = OUTPUT_DIR / f"{slug}-{dataset}.json"
    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return outfile


def main():
    parser = argparse.ArgumentParser(description="Fetch market data from Messari API")
    parser.add_argument("--quiet", action="store_true", help="Suppress output")
    parser.add_argument("--asset", type=str, help="Fetch only this asset (sky, usds, susds)")
    parser.add_argument("--dataset", type=str, help="Fetch only this dataset (price, supply, marketcap)")
    parser.add_argument("--start", type=str, default=LAUNCH_DATE, help="Start date (ISO 8601)")
    parser.add_argument("--end", type=str, help="End date (ISO 8601, default: now)")
    parser.add_argument("--granularity", type=str, default="1w",
                        choices=["5m", "1h", "1d", "1w"], help="Time granularity (default: 1w)")
    args = parser.parse_args()

    api_key = load_api_key()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    end = args.end or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    start = args.start

    targets = ASSETS
    if args.asset:
        if args.asset not in ASSETS:
            print(f"Error: Unknown asset '{args.asset}'. Choose from: {', '.join(ASSETS.keys())}", file=sys.stderr)
            sys.exit(1)
        targets = {args.asset: ASSETS[args.asset]}

    for slug, asset_info in targets.items():
        asset_id = asset_info["id"]
        datasets = asset_info["datasets"]
        if args.dataset:
            datasets = [args.dataset]

        if not args.quiet:
            print(f"\n{asset_info['name']} ({slug}):")

        for dataset in datasets:
            try:
                data = fetch_timeseries(asset_id, dataset, api_key, start, end, args.granularity)
            except (urllib.error.URLError, OSError) as e:
                if not args.quiet:
                    print(f"  {dataset}: FAILED — {e}")
                continue

            # The API may nest data under "data" key or return it directly
            inner = data.get("data", data)

            # Extract point schema and points
            point_schema = inner.get("point_schema", inner.get("schema", data.get("point_schema", [])))
            # Points may be in data.points (v2) or data.series[0].points
            points = inner.get("points", [])
            if not points:
                series = inner.get("series", [])
                if series:
                    points = series[0].get("points", [])

            result = {
                "asset": slug,
                "asset_id": asset_id,
                "asset_name": asset_info["name"],
                "dataset": dataset,
                "granularity": args.granularity,
                "start": start,
                "end": end,
                "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "point_count": len(points),
                "point_schema": point_schema,
                "points": points,
            }

            outfile = save_dataset(slug, dataset, result)
            if not args.quiet:
                print(f"  {dataset}: {len(points)} data points → {outfile.relative_to(PROJECT_DIR)}")

            time.sleep(REQUEST_DELAY)


if __name__ == "__main__":
    main()
