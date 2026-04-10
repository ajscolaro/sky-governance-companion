#!/usr/bin/env python3
"""Fetch poll tallies and build a vote alignment matrix.

Calls GET /api/polling/all-polls-with-tally to collect per-voter tally data
for all polls, matches voter addresses to tracked ADs via the address map,
and builds a vote matrix showing how each AD voted on each poll.

Supports --backfill (all historical polls) and incremental mode (new polls only).
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
DATA_DIR = PROJECT_DIR / "data" / "voting" / "polls"
TALLY_DIR = DATA_DIR / "tallies"
MATRIX_FILE = DATA_DIR / "vote-matrix.json"
ADDRESS_MAP_FILE = PROJECT_DIR / "data" / "voting" / "address-map.json"

API_BASE = "https://vote.sky.money/api"
FETCH_TIMEOUT = 20
USER_AGENT = "SkyAtlasExplorer/1.0 (governance research tool)"
REQUEST_DELAY = 1.0
MAX_RETRIES = 3
RETRY_BACKOFF = 5

MAX_STR_LEN = 300

# Chain ID to name mapping
CHAIN_NAMES = {
    1: "ethereum",
    42161: "arbitrum",
}


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


def load_matrix() -> dict:
    if MATRIX_FILE.exists():
        with open(MATRIX_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_updated": None, "poll_count": 0, "polls": {}, "ad_summary": {}}


def fetch_all_polls_with_tally(quiet: bool = False) -> list[dict]:
    """Fetch all polls with tally data across all pages."""
    all_polls = []
    page = 1

    while True:
        if not quiet:
            print(f"  Fetching polls page {page}...")

        data = api_get(f"/polling/all-polls-with-tally?page={page}")

        polls = data.get("polls", [])
        all_polls.extend(polls)

        pagination = data.get("paginationInfo", {})
        if not pagination.get("hasNextPage", False) or not polls:
            break

        page += 1
        time.sleep(REQUEST_DELAY)

    return all_polls


def fetch_active_poll_ids() -> list[int]:
    """Fetch IDs of currently active polls."""
    try:
        return api_get("/polling/active-poll-ids")
    except (urllib.error.URLError, OSError):
        return []


def process_poll(poll: dict, by_address: dict, all_slugs: set, ad_created: dict) -> dict:
    """Process a single poll into our matrix format."""
    poll_id = str(poll.get("pollId", ""))
    options = poll.get("options", {})
    tally = poll.get("tally", {})

    # Map option IDs to labels
    option_map = {int(k): v for k, v in options.items()}

    # Determine winning option
    winner = tally.get("winner")
    result_label = option_map.get(winner, "Unknown") if winner is not None else "Unknown"

    # Extract per-voter data from votesByAddress (primary) or results (fallback)
    ad_votes = {}
    votes_by_addr = tally.get("votesByAddress", [])

    if isinstance(votes_by_addr, list):
        for voter in votes_by_addr:
            addr = (voter.get("voter") or voter.get("address") or "").lower()
            slug = by_address.get(addr)
            if slug:
                # ballot is a list of option IDs the voter chose
                ballot = voter.get("ballot", [])
                option_id = ballot[0] if ballot else voter.get("optionId")
                option_label = option_map.get(option_id, f"Option {option_id}")
                chain_id = voter.get("chainId")
                ad_votes[slug] = {
                    "option": option_label,
                    "option_id": option_id,
                    "sky_weight": voter.get("skySupport") or voter.get("mkrSupport") or "0",
                    "chain": CHAIN_NAMES.get(chain_id, str(chain_id) if chain_id else "unknown"),
                    "timestamp": voter.get("blockTimestamp"),
                }

    # Determine non-voters — only count ADs that existed before the poll started
    poll_start = (poll.get("startDate") or "")[:10]
    eligible_slugs = {s for s in all_slugs if ad_created.get(s, "9999") <= poll_start}
    ad_non_voters = sorted(eligible_slugs - set(ad_votes.keys()))

    return {
        "title": sanitize_str(poll.get("title", "")),
        "start_date": (poll.get("startDate") or "")[:10],
        "end_date": (poll.get("endDate") or "")[:10],
        "tags": poll.get("tags", []),
        "result": result_label,
        "total_sky": tally.get("totalSkyParticipation") or tally.get("totalSkySupport") or tally.get("totalMkrParticipation") or "0",
        "ad_votes": ad_votes,
        "ad_non_voters": ad_non_voters,
    }


def compute_ad_summary(polls: dict, all_slugs: set, ad_created: dict) -> dict:
    """Compute per-AD voting summary statistics, filtered by eligibility."""
    summary = {}

    for slug in all_slugs:
        created = ad_created.get(slug, "9999")
        voted = 0
        yes_count = 0
        no_count = 0
        abstain_count = 0
        eligible = 0

        for poll_data in polls.values():
            poll_start = poll_data.get("start_date", "")
            if not poll_start or created > poll_start:
                continue  # AD didn't exist yet

            eligible += 1
            vote = poll_data.get("ad_votes", {}).get(slug)
            if vote:
                voted += 1
                option = (vote.get("option") or "").lower()
                if option == "yes":
                    yes_count += 1
                elif option == "no":
                    no_count += 1
                elif option == "abstain":
                    abstain_count += 1

        if eligible > 0:
            summary[slug] = {
                "created": created,
                "eligible_polls": eligible,
                "voted": voted,
                "participation_pct": str(round(voted / eligible * 100, 1)),
                "yes_pct": str(round(yes_count / voted * 100, 1)) if voted else "0",
                "no_pct": str(round(no_count / voted * 100, 1)) if voted else "0",
                "abstain_pct": str(round(abstain_count / voted * 100, 1)) if voted else "0",
            }

    return summary


def main():
    parser = argparse.ArgumentParser(description="Fetch poll tallies and build vote matrix")
    parser.add_argument("--quiet", action="store_true", help="Suppress output")
    parser.add_argument("--backfill", action="store_true", help="Fetch all historical polls")
    parser.add_argument("--poll", type=int, help="Fetch/update a single poll by ID")
    args = parser.parse_args()

    address_map = load_address_map()
    by_address = address_map["by_address"]
    all_slugs = set(address_map["by_slug"].keys())
    ad_created = {slug: info.get("created", "9999") for slug, info in address_map["by_slug"].items()}
    matrix = load_matrix()

    if args.poll:
        # Single poll mode
        if not args.quiet:
            print(f"Fetching poll {args.poll}...")
        try:
            poll = api_get(f"/polling/{args.poll}")
            # Also need tally — fetch via all-polls-with-tally filtered
            # or just fetch the single poll tally
            tally_data = api_get(f"/polling/tally/{args.poll}")
            poll["tally"] = tally_data
        except (urllib.error.URLError, OSError) as e:
            print(f"Error: Could not fetch poll {args.poll}: {e}", file=sys.stderr)
            sys.exit(1)

        processed = process_poll(poll, by_address, all_slugs, ad_created)
        matrix["polls"][str(args.poll)] = processed

        # Save individual tally
        TALLY_DIR.mkdir(parents=True, exist_ok=True)
        with open(TALLY_DIR / f"{args.poll}.json", "w", encoding="utf-8") as f:
            json.dump(tally_data, f, indent=2)

    elif args.backfill:
        if not args.quiet:
            print("Backfilling all polls with tally data...")

        try:
            all_polls = fetch_all_polls_with_tally(quiet=args.quiet)
        except (urllib.error.URLError, OSError) as e:
            print(f"Error: Could not fetch polls: {e}", file=sys.stderr)
            sys.exit(1)

        if not args.quiet:
            print(f"  Processing {len(all_polls)} polls...")

        TALLY_DIR.mkdir(parents=True, exist_ok=True)
        for poll in all_polls:
            poll_id = str(poll.get("pollId", ""))
            processed = process_poll(poll, by_address, all_slugs, ad_created)
            matrix["polls"][poll_id] = processed

            # Save individual tally
            tally = poll.get("tally", {})
            if tally:
                with open(TALLY_DIR / f"{poll_id}.json", "w", encoding="utf-8") as f:
                    json.dump(tally, f, indent=2)

    else:
        # Incremental mode: fetch active + recently completed polls not in matrix
        if not args.quiet:
            print("Checking for new polls...")

        existing_ids = set(matrix["polls"].keys())
        active_ids = fetch_active_poll_ids()
        new_ids = [pid for pid in active_ids if str(pid) not in existing_ids]

        # Also check recent polls-with-tally page 1 for recently completed
        try:
            data = api_get("/polling/all-polls-with-tally?page=1")
            for poll in data.get("polls", []):
                pid = poll.get("pollId")
                if pid and str(pid) not in existing_ids:
                    processed = process_poll(poll, by_address, all_slugs, ad_created)
                    matrix["polls"][str(pid)] = processed

                    tally = poll.get("tally", {})
                    if tally:
                        TALLY_DIR.mkdir(parents=True, exist_ok=True)
                        with open(TALLY_DIR / f"{pid}.json", "w", encoding="utf-8") as f:
                            json.dump(tally, f, indent=2)
        except (urllib.error.URLError, OSError) as e:
            if not args.quiet:
                print(f"  Warning: Could not fetch recent polls: {e}", file=sys.stderr)

    # Recompute summary
    matrix["ad_summary"] = compute_ad_summary(matrix["polls"], all_slugs, ad_created)
    matrix["poll_count"] = len(matrix["polls"])
    matrix["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Write matrix
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(MATRIX_FILE, "w", encoding="utf-8") as f:
        json.dump(matrix, f, indent=2)

    if not args.quiet:
        print(f"Vote matrix: {matrix['poll_count']} polls, {len(matrix['ad_summary'])} ADs tracked")
        # Show participation summary
        for slug, stats in sorted(matrix["ad_summary"].items(),
                                   key=lambda x: float(x[1].get("participation_pct", 0)),
                                   reverse=True):
            print(f"  {slug}: {stats['participation_pct']}% participation "
                  f"({stats['voted']}/{stats['eligible_polls']})")


if __name__ == "__main__":
    main()
