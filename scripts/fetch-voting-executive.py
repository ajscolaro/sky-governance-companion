#!/usr/bin/env python3
"""Fetch executive proposal, hat, and supporter data from the Sky Voting Portal API.

Calls /api/executive, /api/executive/hat, and /api/executive/supporters to build
a snapshot of the current governance state: which spell is the hat, who supports it,
and which ADs are on stale spells.

Daily snapshots are committed to snapshots/executive/ for time-series tracking.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data" / "voting" / "executive"
CACHE_SNAPSHOT_DIR = DATA_DIR / "snapshots"
COMMITTED_DIR = PROJECT_DIR / "snapshots" / "executive"
ADDRESS_MAP_FILE = PROJECT_DIR / "data" / "voting" / "address-map.json"

API_BASE = "https://vote.sky.money/api"
FETCH_TIMEOUT = 20
USER_AGENT = "SkyAtlasExplorer/1.0 (governance research tool)"
MAX_RETRIES = 3
RETRY_BACKOFF = 5

MAX_STR_LEN = 300


def sanitize_str(text: str, max_len: int = MAX_STR_LEN) -> str:
    text = re.sub(r"[\x00-\x08\x0b-\x0c\x0e-\x1f]", "", text)
    text = text.strip()
    if len(text) > max_len:
        text = text[:max_len] + "..."
    return text


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


def main():
    parser = argparse.ArgumentParser(description="Fetch executive data from vote.sky.money")
    parser.add_argument("--quiet", action="store_true", help="Suppress output")
    parser.add_argument("--force", action="store_true", help="Overwrite existing snapshot for today")
    args = parser.parse_args()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    committed_file = COMMITTED_DIR / f"{today}.json"

    if committed_file.exists() and not args.force:
        if not args.quiet:
            print(f"Executive snapshot for {today} already exists. Use --force to overwrite.")
        return

    address_map = load_address_map()
    by_address = address_map["by_address"]
    by_slug = address_map["by_slug"]
    all_slugs = set(by_slug.keys())

    if not args.quiet:
        print("Fetching executive data from vote.sky.money...")

    # Fetch hat
    try:
        hat_data = api_get("/executive/hat")
    except (urllib.error.URLError, OSError) as e:
        print(f"Error: Could not fetch hat: {e}", file=sys.stderr)
        sys.exit(1)

    # Fetch supporters
    try:
        supporters_raw = api_get("/executive/supporters")
    except (urllib.error.URLError, OSError) as e:
        print(f"Error: Could not fetch supporters: {e}", file=sys.stderr)
        sys.exit(1)

    # Fetch proposals
    try:
        proposals_raw = api_get("/executive")
    except (urllib.error.URLError, OSError) as e:
        print(f"Error: Could not fetch executive proposals: {e}", file=sys.stderr)
        sys.exit(1)

    # Build proposal lookup
    proposals = {}
    for p in proposals_raw:
        addr = (p.get("address") or "").lower()
        proposals[addr] = {
            "title": sanitize_str(p.get("title") or ""),
            "date": p.get("date"),
            "active": p.get("active", False),
            "spell_data": p.get("spellData", {}),
        }

    hat_address = (hat_data.get("hatAddress") or hat_data.get("address") or "").lower()
    hat_sky = hat_data.get("skyOnHat") or hat_data.get("skySupport") or "0"

    # Process supporters: map addresses to ADs, track which spell each AD supports
    ad_support = {}  # slug -> {spell_address, sky_amount, is_hat, spell_title}
    ads_on_hat = set()

    if isinstance(supporters_raw, dict):
        for spell_addr, supporter_list in supporters_raw.items():
            spell_addr_lower = spell_addr.lower()
            spell_info = proposals.get(spell_addr_lower, {})
            is_hat = spell_addr_lower == hat_address

            if isinstance(supporter_list, list):
                for supporter in supporter_list:
                    s_addr = (supporter.get("address") or "").lower()
                    slug = by_address.get(s_addr)
                    if slug:
                        ad_support[slug] = {
                            "spell_address": spell_addr,
                            "sky_amount": supporter.get("deposits") or "0",
                            "percent": supporter.get("percent") or 0,
                            "is_hat": is_hat,
                            "spell_title": spell_info.get("title", "Unknown"),
                        }
                        if is_hat:
                            ads_on_hat.add(slug)

    # Find ADs not supporting any spell
    ads_without_support = sorted(all_slugs - set(ad_support.keys()))

    snapshot = {
        "date": today,
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "hat": {
            "address": hat_data.get("hatAddress") or hat_data.get("address", ""),
            "sky_support": hat_sky,
            "title": proposals.get(hat_address, {}).get("title", "Unknown"),
        },
        "proposals": [
            {
                "address": p.get("address", ""),
                "title": sanitize_str(p.get("title") or ""),
                "date": p.get("date"),
                "active": p.get("active", False),
                "has_been_cast": (p.get("spellData") or {}).get("hasBeenCast", False),
            }
            for p in proposals_raw[:10]  # last 10 proposals
        ],
        "ad_support": ad_support,
        "ads_on_hat": sorted(ads_on_hat),
        "ads_stale_hat": sorted(set(ad_support.keys()) - ads_on_hat),
        "ads_no_support": ads_without_support,
    }

    # Write cache
    for directory in [CACHE_SNAPSHOT_DIR, COMMITTED_DIR]:
        directory.mkdir(parents=True, exist_ok=True)
        outfile = directory / f"{today}.json"
        with open(outfile, "w", encoding="utf-8") as f:
            json.dump(snapshot, f, indent=2)

    # Also write current-state cache files
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_DIR / "hat.json", "w", encoding="utf-8") as f:
        json.dump(hat_data, f, indent=2)
    with open(DATA_DIR / "supporters.json", "w", encoding="utf-8") as f:
        json.dump(supporters_raw, f, indent=2)
    with open(DATA_DIR / "proposals.json", "w", encoding="utf-8") as f:
        json.dump(proposals_raw, f, indent=2)

    if not args.quiet:
        print(f"Hat: {snapshot['hat']['title'][:80]}")
        print(f"  SKY on hat: {hat_sky}")
        print(f"  ADs on hat: {', '.join(sorted(ads_on_hat)) or 'none'}")
        if snapshot["ads_stale_hat"]:
            print(f"  ADs on stale spell: {', '.join(snapshot['ads_stale_hat'])}")
        if ads_without_support:
            print(f"  ADs not supporting any spell: {', '.join(ads_without_support)}")


if __name__ == "__main__":
    main()
