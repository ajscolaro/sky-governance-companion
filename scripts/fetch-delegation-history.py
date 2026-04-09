#!/usr/bin/env python3
"""Fetch historical delegation events for all tracked ADs.

Calls GET /api/delegates/delegation-history/{address} for each AD to get
timestamped lock/unlock events. This data lets us reconstruct delegation
power at any historical point, eliminating the need to wait for daily
snapshots to accumulate.

Note: The API appears to cap at 1000 events per delegate. For high-traffic
delegates like Cloaky, this may not cover the full history.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data" / "voting" / "delegation-history"
ADDRESS_MAP_FILE = PROJECT_DIR / "data" / "voting" / "address-map.json"

API_BASE = "https://vote.sky.money/api"
FETCH_TIMEOUT = 20
USER_AGENT = "SkyAtlasExplorer/1.0 (governance research tool)"
REQUEST_DELAY = 1.5  # higher delay — one request per AD, 13 total
MAX_RETRIES = 3
RETRY_BACKOFF = 5


def api_get(path: str) -> dict | list:
    url = f"{API_BASE}{path}"
    backoff = RETRY_BACKOFF
    for attempt in range(MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < MAX_RETRIES:
                time.sleep(backoff)
                backoff *= 2
                continue
            raise


def load_address_map() -> dict:
    if not ADDRESS_MAP_FILE.exists():
        print("Error: Address map not found. Run build-address-map.py first.", file=sys.stderr)
        sys.exit(1)
    with open(ADDRESS_MAP_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def sanitize_str(text: str, max_len: int = 200) -> str:
    text = re.sub(r"[\x00-\x08\x0b-\x0c\x0e-\x1f]", "", text)
    return text.strip()[:max_len]


def fetch_history(address: str, slug: str, quiet: bool = False) -> list[dict]:
    """Fetch delegation event history for a single delegate."""
    try:
        events = api_get(f"/delegates/delegation-history/{address}")
    except (urllib.error.URLError, OSError) as e:
        if not quiet:
            print(f"  Warning: Could not fetch history for {slug}: {e}", file=sys.stderr)
        return []

    if not isinstance(events, list):
        events = events.get("events", events.get("history", []))

    return events


def summarize_history(events: list[dict]) -> dict:
    """Compute summary stats from delegation events."""
    if not events:
        return {"event_count": 0}

    timestamps = [e.get("blockTimestamp", "") for e in events if e.get("blockTimestamp")]
    dates = sorted([t[:10] for t in timestamps if t])

    # Aggregate by caller to find largest delegators
    by_caller: dict[str, float] = {}
    for e in events:
        caller = e.get("immediateCaller", "unknown")
        total = float(e.get("callerLockTotal", 0))
        by_caller[caller] = max(by_caller.get(caller, 0), total)

    top_callers = sorted(by_caller.items(), key=lambda x: x[1], reverse=True)[:5]

    # Count locks vs unlocks
    locks = sum(1 for e in events if float(e.get("lockAmount", 0)) > 0)
    unlocks = sum(1 for e in events if float(e.get("lockAmount", 0)) < 0)

    return {
        "event_count": len(events),
        "date_range": {"earliest": dates[0] if dates else None, "latest": dates[-1] if dates else None},
        "locks": locks,
        "unlocks": unlocks,
        "unique_callers": len(by_caller),
        "top_delegators": [{"address": addr, "peak_amount": str(amt)} for addr, amt in top_callers],
    }


def main():
    parser = argparse.ArgumentParser(description="Fetch delegation event history for all ADs")
    parser.add_argument("--quiet", action="store_true", help="Suppress output")
    parser.add_argument("--delegate", type=str, help="Fetch only this delegate (by slug)")
    args = parser.parse_args()

    address_map = load_address_map()
    by_slug = address_map["by_slug"]

    targets = list(by_slug.items())
    if args.delegate:
        targets = [(s, i) for s, i in targets if s == args.delegate]
        if not targets:
            print(f"Error: Delegate '{args.delegate}' not found.", file=sys.stderr)
            sys.exit(1)

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not args.quiet:
        print(f"Fetching delegation history for {len(targets)} delegate(s)...")

    for slug, info in targets:
        addr = info["delegation_contract"]
        events = fetch_history(addr, slug, quiet=args.quiet)

        if events:
            summary = summarize_history(events)

            output = {
                "slug": slug,
                "delegation_contract": addr,
                "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "summary": summary,
                "events": events,
            }

            outfile = DATA_DIR / f"{slug}.json"
            with open(outfile, "w", encoding="utf-8") as f:
                json.dump(output, f, indent=2)

            if not args.quiet:
                dr = summary.get("date_range", {})
                print(f"  {slug}: {summary['event_count']} events "
                      f"({dr.get('earliest', '?')} to {dr.get('latest', '?')}), "
                      f"{summary['locks']} locks, {summary['unlocks']} unlocks, "
                      f"{summary['unique_callers']} unique callers")
        else:
            if not args.quiet:
                print(f"  {slug}: no events")

        time.sleep(REQUEST_DELAY)

    if not args.quiet:
        print("Done.")


if __name__ == "__main__":
    main()
