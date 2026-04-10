#!/usr/bin/env python3
"""Print a governance status advisory at session startup.

Reads cached data from disk (no API calls) to surface:
- Current hat and AD alignment
- Pending spells (proposed but not yet hat/cast)
- Active and recently ended governance polls
- New lifecycle events since last session

Two governance flows create Atlas PRs:
  1. Text edits: Poll -> PR merged (same day). Polls give 3-4 days advance notice.
  2. Spell recordings: Spell cast -> PR merged (4-11 days later). Lifecycle events
     give advance notice. Active polls give even earlier signal.

Designed to run synchronously in refresh.sh after background fetches
have been kicked off — it reads data from the *previous* session's cache.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
LIFECYCLE_FILE = PROJECT_DIR / "snapshots" / "executive" / "lifecycle.json"
SNAPSHOT_DIR = PROJECT_DIR / "snapshots" / "executive"
VOTE_MATRIX_FILE = PROJECT_DIR / "data" / "voting" / "polls" / "vote-matrix.json"

# How many days back to show recently ended polls
RECENT_POLL_DAYS = 7


def load_json(path: Path) -> dict | list | None:
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def short_title(title: str, max_len: int = 80) -> str:
    """Truncate a spell/poll title sensibly."""
    if len(title) <= max_len:
        return title
    return title[:max_len - 3].rsplit(",", 1)[0] + "..."


def format_sky(raw: str | int | float) -> str:
    """Format a raw SKY amount (wei-ish or float) into human-readable."""
    try:
        val = float(raw)
    except (ValueError, TypeError):
        return "?"
    if val > 1e15:
        val = val / 1e18  # wei to tokens
    if val >= 1e9:
        return f"{val / 1e9:.1f}B"
    if val >= 1e6:
        return f"{val / 1e6:.0f}M"
    if val >= 1e3:
        return f"{val / 1e3:.0f}K"
    return f"{val:.0f}"


def find_latest_snapshot() -> dict | None:
    """Find the most recent daily executive snapshot."""
    if not SNAPSHOT_DIR.exists():
        return None
    snapshots = sorted(SNAPSHOT_DIR.glob("????-??-??.json"), reverse=True)
    for s in snapshots:
        data = load_json(s)
        if data and "hat" in data:
            return data
    return None


def print_executive_status(snapshot: dict, lifecycle: dict) -> None:
    """Print hat status, AD alignment, and pending spells."""
    hat = snapshot.get("hat", {})
    hat_title = short_title(hat.get("title", "Unknown"))
    hat_sky = format_sky(hat.get("sky_support", "0"))

    ads_on_hat = snapshot.get("ads_on_hat", [])
    ads_stale = snapshot.get("ads_stale_hat", [])
    ads_none = snapshot.get("ads_no_support", [])
    total_ads = len(ads_on_hat) + len(ads_stale) + len(ads_none)

    print(f"  Hat: {hat_title}")
    print(f"    {hat_sky} SKY | {len(ads_on_hat)}/{total_ads} ADs aligned")

    if ads_stale:
        print(f"    Stale: {', '.join(ads_stale)}")
    if ads_none:
        print(f"    No support: {', '.join(ads_none)}")

    # Pending spells: proposed but not yet cast, and recent enough to matter.
    # Cross-reference with snapshot proposals (which have live "active" status)
    # to avoid showing old spells that were cast before lifecycle tracking began.
    active_addrs = set()
    for p in snapshot.get("proposals", []):
        if p.get("active") and not p.get("has_been_cast"):
            active_addrs.add(p.get("address", "").lower())

    # Also consider recent spells from lifecycle (last 60 days)
    cutoff_date = (datetime.now(timezone.utc) - timedelta(days=60)).strftime("%Y-%m-%d")

    pending = []
    spells = lifecycle.get("spells", {}) if lifecycle else {}
    for addr, spell in spells.items():
        event_types = {e["type"] for e in spell.get("events", [])}
        if "cast" in event_types or "expired" in event_types:
            continue
        if "proposed" not in event_types:
            continue

        # Only show if: active in API snapshot, OR recent enough
        spell_date = spell.get("date", "")
        is_active_api = addr.lower() in active_addrs
        is_recent = spell_date >= cutoff_date if spell_date else False

        if not is_active_api and not is_recent:
            continue

        is_hat = "hat" in event_types
        pending.append((spell_date, spell.get("title", ""), is_hat, addr))

    pending.sort(reverse=True)  # newest first
    if pending:
        for date, title, is_hat, addr in pending:
            status = "hat, not yet cast" if is_hat else "proposed, not yet hat"
            print(f"  Pending: {short_title(title, 65)} ({date}, {status})")


def poll_type_label(poll_type: str) -> str:
    """Short label for poll type."""
    return {"atlas-edit": "text edit", "parameter-change": "param change"}.get(poll_type, "")


def print_poll_status(matrix: dict) -> None:
    """Print active and recently ended polls with pipeline context."""
    polls = matrix.get("polls", {})
    if not polls:
        return

    today = datetime.now(timezone.utc).date()
    cutoff = today - timedelta(days=RECENT_POLL_DAYS)

    active = []
    recent = []

    for poll_id, poll in polls.items():
        end_str = poll.get("end_date", "")
        start_str = poll.get("start_date", "")
        try:
            end_date = datetime.strptime(end_str, "%Y-%m-%d").date()
        except ValueError:
            continue

        title = poll.get("title", "")
        result = poll.get("result", "")
        non_voters = poll.get("ad_non_voters", [])
        ptype = poll.get("poll_type", "")
        atlas_pr = poll.get("atlas_pr")

        if end_date >= today:
            active.append((end_str, poll_id, title, start_str, non_voters, ptype))
        elif end_date >= cutoff:
            recent.append((end_str, poll_id, title, result, non_voters, ptype, atlas_pr))

    active.sort(reverse=True)
    recent.sort(reverse=True)

    if active:
        print(f"  Active polls ({len(active)}):")
        for end, pid, title, start, non_voters, ptype in active:
            short = short_title(title, 55)
            tag = f" [{poll_type_label(ptype)}]" if ptype else ""
            voter_note = f" | not yet voted: {', '.join(non_voters)}" if non_voters else ""
            print(f"    #{pid} {short}{tag} (ends {end}{voter_note})")
    else:
        print("  No active polls")

    if recent:
        print(f"  Recently ended ({len(recent)}):")
        for end, pid, title, result, non_voters, ptype, atlas_pr in recent[:3]:
            short = short_title(title, 50)
            tag = f" [{poll_type_label(ptype)}]" if ptype else ""
            pr_ref = f" -> PR #{atlas_pr}" if atlas_pr else ""
            nv = f" | non-voters: {', '.join(non_voters)}" if non_voters else ""
            print(f"    #{pid} {short}{tag} -> {result}{pr_ref} (ended {end}{nv})")


def print_lifecycle_changes(lifecycle: dict) -> None:
    """Flag any lifecycle events from the last 24 hours."""
    if not lifecycle:
        return

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=24)
    new_events = []

    for addr, spell in lifecycle.get("spells", {}).items():
        for event in spell.get("events", []):
            try:
                at = datetime.fromisoformat(event["at"].replace("Z", "+00:00"))
                if at >= cutoff:
                    new_events.append((
                        event["at"][:10],
                        event["type"],
                        short_title(spell.get("title", ""), 55),
                    ))
            except (ValueError, KeyError):
                continue

    if new_events:
        new_events.sort(reverse=True)
        print(f"  Lifecycle events (last 24h): {len(new_events)}")
        for date, etype, title in new_events:
            print(f"    {title} -> {etype}")


def main():
    quiet = "--quiet" in sys.argv

    # Load cached data from previous session
    lifecycle = load_json(LIFECYCLE_FILE)
    snapshot = find_latest_snapshot()
    matrix = load_json(VOTE_MATRIX_FILE)

    has_data = False

    if snapshot:
        has_data = True
        print("")
        print("=== GOVERNANCE STATUS ===")
        print_executive_status(snapshot, lifecycle)

    if matrix:
        has_data = True
        if not snapshot:
            print("")
            print("=== GOVERNANCE STATUS ===")
        print_poll_status(matrix)

    if lifecycle:
        print_lifecycle_changes(lifecycle)

    if not has_data and not quiet:
        print("No cached governance data. Run /governance-data to fetch.")


if __name__ == "__main__":
    main()
