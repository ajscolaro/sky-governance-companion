#!/usr/bin/env python3
"""Session briefing: prioritized digest of what changed since last session.

Reads cached data from disk (no API calls) to produce a startup summary:
  Tier 1 — What changed: merged PRs, spell lifecycle, poll results, market moves
  Tier 2 — What's ahead: active polls, pending spells, upcoming forum proposals
  Tier 3 — First-run orientation for new users (--first-run flag)

Designed to run synchronously in refresh.sh after background fetches are kicked
off — it reads data from the *previous* session's cache, same as the old
governance-advisory.py it replaces.
"""

from __future__ import annotations

import json
import os
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
LAST_SESSION_FILE = PROJECT_DIR / ".last-session"
LIFECYCLE_FILE = PROJECT_DIR / "data" / "voting" / "executive" / "lifecycle.json"
VOTE_MATRIX_FILE = PROJECT_DIR / "data" / "voting" / "polls" / "vote-matrix.json"
MARKET_DB_FILE = PROJECT_DIR / "data" / "market.db"
FORUM_INDEX_FILE = PROJECT_DIR / "data" / "forum" / "index.json"
LOG_FILE = PROJECT_DIR / "history" / "_log.md"

# Thresholds
MARKET_MOVE_THRESHOLD = 3.0  # percent change to report
RECENT_DAYS_FALLBACK = 7  # if no .last-session file
MAX_RECENT_POLLS = 3
MAX_FORUM_POSTS = 3

# ANSI colors (disabled if not a TTY)
USE_COLOR = hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


def c(code: str, text: str) -> str:
    if not USE_COLOR:
        return text
    return f"\033[{code}m{text}\033[0m"


def bold(text: str) -> str:
    return c("1", text)


def dim(text: str) -> str:
    return c("2", text)


def cyan(text: str) -> str:
    return c("36", text)


def green(text: str) -> str:
    return c("32", text)


def yellow(text: str) -> str:
    return c("33", text)


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_json(path: Path) -> dict | list | None:
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def get_last_session() -> datetime:
    """Read .last-session timestamp, fall back to N days ago."""
    if LAST_SESSION_FILE.exists():
        try:
            ts = LAST_SESSION_FILE.read_text().strip()
            return datetime.fromisoformat(ts)
        except ValueError:
            pass
    return datetime.now(timezone.utc) - timedelta(days=RECENT_DAYS_FALLBACK)


def save_session_timestamp() -> None:
    """Write current time to .last-session."""
    LAST_SESSION_FILE.write_text(
        datetime.now(timezone.utc).isoformat(timespec="seconds") + "\n"
    )


def short_title(title: str, max_len: int = 72) -> str:
    if len(title) <= max_len:
        return title
    return title[: max_len - 3].rsplit(",", 1)[0] + "..."


# ---------------------------------------------------------------------------
# Tier 1: What changed
# ---------------------------------------------------------------------------

def get_merged_prs_since(since: datetime) -> list[dict]:
    """Parse _log.md for PRs merged after `since`."""
    if not LOG_FILE.exists():
        return []
    since_str = since.strftime("%Y-%m-%d")
    results = []
    for line in LOG_FILE.read_text().splitlines():
        if not line.startswith("| #"):
            continue
        parts = [p.strip() for p in line.split("|")]
        # parts: ['', '#NNN', 'Title', 'YYYY-MM-DD', 'sections', 'status', '']
        if len(parts) < 6:
            continue
        try:
            pr_num = int(parts[1].lstrip("#"))
            title = parts[2]
            merged = parts[3]
            status = parts[5]
        except (ValueError, IndexError):
            continue
        if merged >= since_str:
            results.append({
                "pr": pr_num, "title": title, "merged": merged, "status": status,
            })
    results.sort(key=lambda x: x["merged"], reverse=True)
    return results


def get_lifecycle_events_since(lifecycle: dict | None, since: datetime) -> list[tuple]:
    """Return (date, event_type, spell_title) tuples since `since`."""
    if not lifecycle:
        return []
    since_str = since.strftime("%Y-%m-%dT%H:%M:%S")
    events = []
    for _addr, spell in lifecycle.get("spells", {}).items():
        for event in spell.get("events", []):
            at = event.get("at", "")
            if at >= since_str:
                events.append((
                    at[:10],
                    event["type"],
                    short_title(spell.get("title", ""), 60),
                ))
    events.sort(reverse=True)
    return events


def get_ended_polls_since(matrix: dict | None, since: datetime) -> list[dict]:
    """Polls that ended since last session."""
    if not matrix:
        return []
    since_str = since.strftime("%Y-%m-%d")
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    results = []
    for pid, poll in matrix.get("polls", {}).items():
        end = poll.get("end_date", "")
        if since_str <= end < today_str:
            results.append({
                "id": pid,
                "title": poll.get("title", ""),
                "end_date": end,
                "result": poll.get("result", ""),
                "poll_type": poll.get("poll_type", ""),
                "atlas_pr": poll.get("atlas_pr"),
                "non_voters": poll.get("ad_non_voters", []),
            })
    results.sort(key=lambda x: x["end_date"], reverse=True)
    return results


def get_market_moves(since: datetime) -> list[tuple]:
    """Return (asset, pct_change, current_price) for significant movers."""
    if not MARKET_DB_FILE.exists():
        return []
    since_str = since.strftime("%Y-%m-%d")
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    moves = []
    try:
        conn = sqlite3.connect(str(MARKET_DB_FILE))
        for asset in ["sky", "spk", "btc", "eth"]:
            row_then = conn.execute(
                "SELECT close FROM daily WHERE asset = ? AND date >= ? "
                "AND close IS NOT NULL ORDER BY date LIMIT 1",
                (asset, since_str),
            ).fetchone()
            row_now = conn.execute(
                "SELECT close FROM daily WHERE asset = ? AND date <= ? "
                "AND close IS NOT NULL ORDER BY date DESC LIMIT 1",
                (asset, today_str),
            ).fetchone()
            if row_then and row_now and row_then[0]:
                pct = ((row_now[0] - row_then[0]) / row_then[0]) * 100
                if abs(pct) >= MARKET_MOVE_THRESHOLD:
                    moves.append((asset.upper(), pct, row_now[0]))
        # Stablecoin supply change
        for stable in ["usds"]:
            row_then = conn.execute(
                "SELECT supply FROM stablecoin_snapshot WHERE asset = ? AND date >= ? "
                "AND supply IS NOT NULL ORDER BY date LIMIT 1",
                (stable, since_str),
            ).fetchone()
            row_now = conn.execute(
                "SELECT supply FROM stablecoin_snapshot WHERE asset = ? AND date <= ? "
                "AND supply IS NOT NULL ORDER BY date DESC LIMIT 1",
                (stable, today_str),
            ).fetchone()
            if row_then and row_now and row_then[0]:
                pct = ((row_now[0] - row_then[0]) / row_then[0]) * 100
                if abs(pct) >= MARKET_MOVE_THRESHOLD:
                    moves.append((f"{stable.upper()} supply", pct, row_now[0]))
        conn.close()
    except (sqlite3.Error, OSError):
        pass
    # Sort by magnitude
    moves.sort(key=lambda x: abs(x[1]), reverse=True)
    return moves


def print_whats_changed(since: datetime, lifecycle: dict | None, matrix: dict | None) -> bool:
    """Print Tier 1 — what changed. Returns True if anything was printed."""
    merged = get_merged_prs_since(since)
    events = get_lifecycle_events_since(lifecycle, since)
    polls = get_ended_polls_since(matrix, since)
    moves = get_market_moves(since)

    anything = merged or events or polls or moves
    if not anything:
        return False

    since_label = since.strftime("%b %d")
    print(f"\n{bold('=== SINCE LAST SESSION')} {dim(f'({since_label})')} {bold('===')}")

    if merged:
        for pr in merged[:5]:
            status_tag = dim(" [tracked]") if pr["status"] == "complete" else ""
            print(f"  PR #{pr['pr']} merged {pr['merged']}: {short_title(pr['title'], 55)}{status_tag}")

    if events:
        for date, etype, title in events[:4]:
            print(f"  Spell {etype}: {title} {dim(f'({date})')}")

    if polls:
        type_labels = {"atlas-edit": "text edit", "parameter-change": "param change"}
        for p in polls[:MAX_RECENT_POLLS]:
            tag = f" [{type_labels.get(p['poll_type'], '')}]" if p["poll_type"] in type_labels else ""
            pr_ref = f" -> PR #{p['atlas_pr']}" if p.get("atlas_pr") else ""
            nv = f" | non-voters: {', '.join(p['non_voters'])}" if p["non_voters"] else ""
            print(f"  Poll #{p['id']} ended {p['end_date']}: {p['result']}{tag}{pr_ref}{nv}")

    if moves:
        parts = []
        for asset, pct, price in moves:
            direction = "+" if pct > 0 else ""
            if "supply" in asset:
                parts.append(f"{asset} {direction}{pct:.1f}% (${price / 1e9:.1f}B)")
            elif price >= 1000:
                parts.append(f"{asset} {direction}{pct:.1f}% (${price:,.0f})")
            else:
                parts.append(f"{asset} {direction}{pct:.1f}% (${price:.4f})")
        print(f"  Market: {', '.join(parts)}")

    return True


# ---------------------------------------------------------------------------
# Tier 2: What's ahead
# ---------------------------------------------------------------------------

def print_whats_ahead(lifecycle: dict | None, matrix: dict | None) -> bool:
    """Print Tier 2 — active polls and pending spells. Returns True if printed."""
    today = datetime.now(timezone.utc).date()
    today_str = today.strftime("%Y-%m-%d")
    anything = False

    # Active polls
    active_polls = []
    if matrix:
        for pid, poll in matrix.get("polls", {}).items():
            end = poll.get("end_date", "")
            if end >= today_str:
                active_polls.append({
                    "id": pid,
                    "title": poll.get("title", ""),
                    "end_date": end,
                    "poll_type": poll.get("poll_type", ""),
                    "non_voters": poll.get("ad_non_voters", []),
                })
        active_polls.sort(key=lambda x: x["end_date"])

    # Pending spells
    pending_spells = []
    if lifecycle:
        cutoff = (datetime.now(timezone.utc) - timedelta(days=60)).strftime("%Y-%m-%d")
        for _addr, spell in lifecycle.get("spells", {}).items():
            event_types = {e["type"] for e in spell.get("events", [])}
            if "cast" in event_types or "expired" in event_types:
                continue
            if "proposed" not in event_types:
                continue
            spell_date = spell.get("date", "")
            if spell_date < cutoff:
                continue
            is_hat = "hat" in event_types
            pending_spells.append((
                spell_date,
                short_title(spell.get("title", ""), 60),
                "hat, not yet cast" if is_hat else "proposed, not yet hat",
            ))
        pending_spells.sort(reverse=True)

    if not active_polls and not pending_spells:
        return False

    print(f"\n{bold('=== GOVERNANCE STATUS ===')}")

    if active_polls:
        type_labels = {"atlas-edit": "text edit", "parameter-change": "param change"}
        print(f"  Active polls ({len(active_polls)}):")
        for p in active_polls:
            tag = f" [{type_labels.get(p['poll_type'], '')}]" if p["poll_type"] in type_labels else ""
            nv = f" | not yet voted: {', '.join(p['non_voters'])}" if p["non_voters"] else ""
            print(f"    #{p['id']} {short_title(p['title'], 50)}{tag} (ends {p['end_date']}{nv})")
    else:
        print("  No active polls")

    if pending_spells:
        for date, title, status in pending_spells[:3]:
            print(f"  Pending spell: {title} {dim(f'({date}, {status})')}")

    anything = True
    return anything


# ---------------------------------------------------------------------------
# Tier 2b: Recent forum activity
# ---------------------------------------------------------------------------

def print_forum_activity(since: datetime) -> bool:
    """Print recent governance forum posts since last session."""
    index = load_json(FORUM_INDEX_FILE)
    if not index or not isinstance(index, list):
        return False
    since_str = since.strftime("%Y-%m-%d")
    recent = [p for p in index if p.get("published", "") >= since_str]
    recent.sort(key=lambda x: x.get("published", ""), reverse=True)
    if not recent:
        return False
    print(f"\n{bold('=== FORUM ACTIVITY ===')} {dim(f'({len(recent)} new)')}")
    for p in recent[:MAX_FORUM_POSTS]:
        cat = dim(f"[{p.get('category', '')}]") if p.get("category") else ""
        print(f"  {p.get('published', '')} {p.get('title', '')[:65]} {cat}")
    if len(recent) > MAX_FORUM_POSTS:
        print(dim(f"  ... and {len(recent) - MAX_FORUM_POSTS} more. Use /forum-search to browse."))
    return True


# ---------------------------------------------------------------------------
# First-run orientation
# ---------------------------------------------------------------------------

def print_first_run() -> None:
    """Print orientation for brand-new users."""
    print(f"""
{bold('=== WELCOME TO SKY ATLAS EXPLORER ===')}

This tool helps you navigate the {cyan('Sky Atlas')} — the governing document for
the Sky ecosystem (formerly MakerDAO) — and track governance changes over time.

{bold('What just happened:')}
  The Atlas repo was cloned and indexed ({cyan('~9,800 documents')} parsed).
  On future sessions, this refreshes automatically and you'll see a briefing
  of what changed since your last session.

{bold('What you can do:')}

  {cyan('/atlas-navigate')}      Search and read Atlas documents by name, path, type, or UUID
  {cyan('/atlas-analyze')}       Explain what an Atlas PR changes and why it matters
  {cyan('/atlas-track')}         Process merged PRs into per-entity change history
  {cyan('/governance-data')}     Fetch on-chain data: delegation, vote alignment, spell lifecycle
  {cyan('/messari-market-data')} Query local market data for SKY, USDS, sUSDS, SPK, BTC, ETH
  {cyan('/forum-search')}        Search cached Sky Forum governance discussions
  {cyan('/ad-track')}            Process delegate vote rationales into per-AD comms files

{bold('Key concepts:')}
  {yellow('Atlas edits')} go through polls first, then merge same-day when the poll passes.
  {yellow('Spell recordings')} happen after on-chain execution — the PR documents what already happened.
  {yellow('history/')} is the institutional memory: per-entity changelogs tracking every PR.

{bold('Try:')} "What changed in the Atlas this week?" or "Show me Spark agent documents"
""")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    first_run = "--first-run" in sys.argv

    if first_run:
        print_first_run()
        save_session_timestamp()
        return

    since = get_last_session()
    lifecycle = load_json(LIFECYCLE_FILE)
    matrix = load_json(VOTE_MATRIX_FILE)

    had_changes = print_whats_changed(since, lifecycle, matrix)
    had_ahead = print_whats_ahead(lifecycle, matrix)
    had_forum = print_forum_activity(since)

    if not had_changes and not had_ahead and not had_forum:
        since_label = since.strftime("%b %d")
        print(f"\n{dim(f'No significant changes since {since_label}.')}")

    # Save timestamp for next session
    save_session_timestamp()


if __name__ == "__main__":
    main()
