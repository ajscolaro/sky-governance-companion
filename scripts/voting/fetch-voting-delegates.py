#!/usr/bin/env python3
"""Fetch delegation data from the Sky Voting Portal API.

Calls GET /api/delegates to collect delegation metrics for all delegates,
matches them to tracked ADs via the address map, and writes to
data/voting/delegates/ (gitignored cache).

Fetches are deduped by date — only one per day unless --force is used.
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
from decimal import Decimal
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = PROJECT_DIR / "data" / "voting" / "delegates"
SNAPSHOT_CACHE_DIR = DATA_DIR / "snapshots"
DELEGATOR_DIR = DATA_DIR / "delegators"
ADDRESS_MAP_FILE = PROJECT_DIR / "data" / "voting" / "address-map.json"

API_BASE = "https://vote.sky.money/api"
FETCH_TIMEOUT = 20
USER_AGENT = "SkyAtlasExplorer/1.0 (governance research tool)"
REQUEST_DELAY = 1.0  # seconds between paginated requests
MAX_RETRIES = 3
RETRY_BACKOFF = 5  # seconds, doubles on each retry

# Sanitize string fields from API — delegate names for shadow delegates could be anything
MAX_NAME_LEN = 100


def sanitize_str(text: str, max_len: int = MAX_NAME_LEN) -> str:
    """Sanitize a string field from the API."""
    text = re.sub(r"[\x00-\x08\x0b-\x0c\x0e-\x1f]", "", text)
    text = text.strip()
    if len(text) > max_len:
        text = text[:max_len] + "..."
    return text


def api_get(path: str) -> dict | list:
    """Make a GET request to the voting portal API with retry on 429."""
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


def fetch_all_delegates() -> tuple[list[dict], dict]:
    """Fetch all delegates across all pages. Returns (delegates, stats)."""
    all_delegates = []
    stats = {}
    page = 1

    while True:
        data = api_get(f"/delegates?page={page}")

        if page == 1:
            stats = data.get("stats", {})

        delegates = data.get("delegates", [])
        all_delegates.extend(delegates)

        pagination = data.get("paginationInfo", {})
        if not pagination.get("hasNextPage", False) or not delegates:
            break

        page += 1
        time.sleep(REQUEST_DELAY)

    return all_delegates, stats


def load_address_map() -> dict:
    """Load the address-to-slug map."""
    if not ADDRESS_MAP_FILE.exists():
        print("Error: Address map not found. Run build-address-map.py first.", file=sys.stderr)
        sys.exit(1)
    with open(ADDRESS_MAP_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def fetch_delegators(address: str, slug: str, quiet: bool = False) -> list[dict]:
    """Fetch paginated delegator list for a single delegate."""
    all_delegators = []
    page = 1

    while True:
        try:
            data = api_get(f"/delegates/{address}/delegators?page={page}")
        except (urllib.error.URLError, OSError) as e:
            if not quiet:
                print(f"  Warning: Could not fetch delegators for {slug}: {e}", file=sys.stderr)
            break

        delegators = data.get("delegators", [])
        all_delegators.extend(delegators)

        pagination = data.get("paginationInfo", {})
        if not pagination.get("hasNextPage", False) or not delegators:
            break

        page += 1
        time.sleep(REQUEST_DELAY)

    return all_delegators


def main():
    parser = argparse.ArgumentParser(description="Fetch delegation snapshots from vote.sky.money")
    parser.add_argument("--quiet", action="store_true", help="Suppress output")
    parser.add_argument("--force", action="store_true", help="Overwrite existing snapshot for today")
    parser.add_argument("--delegators", action="store_true", help="Also fetch per-AD delegator lists")
    args = parser.parse_args()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    cache_file = SNAPSHOT_CACHE_DIR / f"{today}.json"

    # Dedup: skip if today's cache already exists
    if cache_file.exists() and not args.force:
        if not args.quiet:
            print(f"Delegation data for {today} already cached. Use --force to overwrite.")
        if not args.delegators:
            return
        # Fall through to delegator fetch even if cache exists

    address_map = load_address_map()
    by_address = address_map["by_address"]
    by_slug = address_map["by_slug"]

    if not args.quiet:
        print("Fetching delegates from vote.sky.money...")

    try:
        all_delegates, stats = fetch_all_delegates()
    except (urllib.error.URLError, OSError) as e:
        print(f"Error: Could not fetch delegates: {e}", file=sys.stderr)
        sys.exit(1)

    # Build aligned delegate list, matched to our slugs
    aligned = []
    rank = 0
    for d in all_delegates:
        vote_addr = (d.get("voteDelegateAddress") or "").lower()
        slug = by_address.get(vote_addr)

        if slug and slug in by_slug:
            rank += 1
            total_sky = Decimal(stats.get("totalSkyDelegated", "0") or "0")
            delegate_sky = Decimal(d.get("skyDelegated", "0") or "0")
            share = (delegate_sky / total_sky * 100).quantize(Decimal("0.1")) if total_sky else Decimal("0")

            aligned.append({
                "slug": slug,
                "name": sanitize_str(d.get("name") or slug),
                "delegation_contract": by_slug[slug]["delegation_contract"],
                "sky_delegated": d.get("skyDelegated", "0"),
                "delegation_share_pct": str(share),
                "delegator_count": d.get("delegatorCount", 0),
                "participation": sanitize_str(d.get("combinedParticipation") or "No Data", 20),
                "communication": sanitize_str(d.get("communication") or "No Data", 20),
                "last_vote_date": d.get("lastVoteDate"),
                "proposals_supported": d.get("proposalsSupported", 0),
                "rank": rank,
            })

    # Sort by delegation amount descending
    aligned.sort(key=lambda x: Decimal(x["sky_delegated"]), reverse=True)
    for i, d in enumerate(aligned, 1):
        d["rank"] = i

    snapshot = {
        "date": today,
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_sky_delegated": stats.get("totalSkyDelegated", "0"),
        "total_delegators": stats.get("totalDelegators", 0),
        "aligned_count": stats.get("aligned", 0),
        "shadow_count": stats.get("shadow", 0),
        "aligned_delegates": aligned,
    }

    # Write to cache
    SNAPSHOT_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2)

    if not args.quiet:
        print(f"Delegation data: {len(aligned)} aligned delegates, "
              f"{stats.get('totalDelegators', '?')} total delegators")

    # Optional: fetch per-AD delegator lists
    if args.delegators:
        if not args.quiet:
            print("\nFetching delegator lists...")
        DELEGATOR_DIR.mkdir(parents=True, exist_ok=True)

        for delegate in aligned:
            slug = delegate["slug"]
            addr = delegate["delegation_contract"]
            delegators = fetch_delegators(addr, slug, quiet=args.quiet)

            if delegators:
                outfile = DELEGATOR_DIR / f"{slug}.json"
                with open(outfile, "w", encoding="utf-8") as f:
                    json.dump({
                        "slug": slug,
                        "date": today,
                        "delegation_contract": addr,
                        "delegator_count": len(delegators),
                        "delegators": delegators,
                    }, f, indent=2)

                if not args.quiet:
                    print(f"  {slug}: {len(delegators)} delegators")

            time.sleep(REQUEST_DELAY)


if __name__ == "__main__":
    main()
