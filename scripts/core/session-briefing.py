#!/usr/bin/env python3
"""Session briefing: what's changed and the current governance state.

Reads cached data from disk (no API calls). Invoked by scripts/core/refresh.sh
after all parallel fetches have completed, so every data source is fresh.

Each section prints only if it has content — no empty placeholders, no entry
caps. Sections: market (daily), spells (current + pending), polls (ended since
last session + active), atlas proposals (new open PRs in last 7 days), forum
activity (new posts since last session).
"""

from __future__ import annotations

import json
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
LAST_SESSION_FILE = PROJECT_DIR / ".last-session"
LIFECYCLE_FILE = PROJECT_DIR / "data" / "voting" / "executive" / "lifecycle.json"
HAT_FILE = PROJECT_DIR / "data" / "voting" / "executive" / "hat.json"
EXECUTIVE_PROPOSALS_FILE = PROJECT_DIR / "data" / "voting" / "executive" / "proposals.json"
VOTE_MATRIX_FILE = PROJECT_DIR / "data" / "voting" / "polls" / "vote-matrix.json"
MARKET_DB_FILE = PROJECT_DIR / "data" / "market.db"
FORUM_INDEX_FILE = PROJECT_DIR / "data" / "forum" / "index.json"
OPEN_PRS_FILE = PROJECT_DIR / "data" / "github" / "open-prs.json"

# Thresholds
RECENT_DAYS_FALLBACK = 7  # if no .last-session file
PENDING_SPELL_LOOKBACK_DAYS = 60

# Market assets shown every session, grouped by display line.
# Each tuple: (db_slug, display_label, kind, line)
# kind: "price" (daily.close), "supply" (daily.mcap), "stablecoin_sum" (SUM over stablecoin_snapshot)
MARKET_ASSETS = [
    ("usds", "USDS Supply",          "supply",          1),
    (None,   "Total Stablecoin MC",  "stablecoin_sum",  1),
    ("sky",  "SKY",                  "price",           2),
    ("spk",  "SPK",                  "price",           2),
    ("btc",  "BTC",                  "price",           2),
    ("eth",  "ETH",                  "price",           2),
]

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


def yellow(text: str) -> str:
    return c("33", text)


POLL_URL = "https://vote.sky.money/polling/{}"
EXECUTIVE_URL = "https://vote.sky.money/executive/{}"


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
# Data fetchers
# ---------------------------------------------------------------------------

def _poll_has_ended(poll: dict) -> bool:
    """Check if a poll has ended using full timestamp if available."""
    end_dt = poll.get("end_datetime", "")
    if end_dt:
        try:
            end_time = datetime.fromisoformat(end_dt.replace("Z", "+00:00"))
            return datetime.now(timezone.utc) >= end_time
        except ValueError:
            pass
    # Fallback: treat end_date as ended if strictly before today
    end = poll.get("end_date", "")
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return end < today_str


def get_ended_polls_since(matrix: dict | None, since: datetime) -> list[dict]:
    """Polls that ended since last session."""
    if not matrix:
        return []
    since_str = since.strftime("%Y-%m-%d")
    results = []
    for pid, poll in matrix.get("polls", {}).items():
        end = poll.get("end_date", "")
        if since_str <= end and _poll_has_ended(poll):
            results.append({
                "id": pid,
                "title": poll.get("title", ""),
                "end_date": end,
                "result": poll.get("result", ""),
                "poll_type": poll.get("poll_type", ""),
                "atlas_pr": poll.get("atlas_pr"),
                "non_voters": poll.get("ad_non_voters", []),
                "poll_url": poll.get("poll_url", ""),
            })
    results.sort(key=lambda x: x["end_date"], reverse=True)
    return results


def _latest_two(conn: sqlite3.Connection, asset: str, field: str) -> tuple[float, float] | None:
    rows = conn.execute(
        f"SELECT {field} FROM daily WHERE asset = ? "
        f"AND {field} IS NOT NULL ORDER BY date DESC LIMIT 2",
        (asset,),
    ).fetchall()
    if len(rows) < 2 or not rows[1][0]:
        return None
    return rows[0][0], rows[1][0]


def _latest_two_stablecoin_sum(conn: sqlite3.Connection) -> tuple[float, float] | None:
    rows = conn.execute(
        "SELECT date, SUM(supply) FROM stablecoin_snapshot "
        "GROUP BY date ORDER BY date DESC LIMIT 2"
    ).fetchall()
    if len(rows) < 2 or not rows[1][1]:
        return None
    return rows[0][1], rows[1][1]


def get_market_moves() -> list[tuple] | None:
    """Return (label, pct_change, current_value, abs_delta, kind, line) tuples.

    Daily change for each asset in MARKET_ASSETS, always shown in fixed order.
    Returns None if market.db doesn't exist (no API key configured).
    """
    if not MARKET_DB_FILE.exists():
        return None
    moves = []
    try:
        conn = sqlite3.connect(str(MARKET_DB_FILE))
        for asset, label, kind, line in MARKET_ASSETS:
            if kind == "stablecoin_sum":
                pair = _latest_two_stablecoin_sum(conn)
            elif kind == "supply":
                pair = _latest_two(conn, asset, "mcap")
            else:
                pair = _latest_two(conn, asset, "close")
            if pair is None:
                continue
            now_val, prev_val = pair
            pct = ((now_val - prev_val) / prev_val) * 100
            abs_delta = now_val - prev_val
            moves.append((label, pct, now_val, abs_delta, kind, line))
        conn.close()
    except (sqlite3.Error, OSError):
        pass
    return moves


TYPE_LABELS = {"atlas-edit": "text edit", "parameter-change": "param change"}


def _section_header(title: str, since_label: str | None = None) -> None:
    suffix = f" {dim(f'(since {since_label})')}" if since_label else ""
    print(f"\n{bold(f'=== {title} ===')}{suffix}")


def _subheader(label: str) -> None:
    print(f"  {bold(label + ':')}")


def get_active_polls(matrix: dict | None) -> list[dict]:
    """Polls currently open for voting."""
    if not matrix:
        return []
    polls = []
    for pid, poll in matrix.get("polls", {}).items():
        if _poll_has_ended(poll):
            continue
        polls.append({
            "id": pid,
            "title": poll.get("title", ""),
            "end_date": poll.get("end_date", ""),
            "poll_type": poll.get("poll_type", ""),
            "non_voters": poll.get("ad_non_voters", []),
        })
    polls.sort(key=lambda x: x["end_date"])
    return polls


def _executive_key_map(proposals: list | None) -> dict[str, str]:
    """Map spell address (lowercase) → vote.sky.money URL slug."""
    if not isinstance(proposals, list):
        return {}
    return {
        (p.get("address") or "").lower(): p.get("key", "")
        for p in proposals
        if p.get("address") and p.get("key")
    }


def _spell_vote_url(addr: str, key_map: dict[str, str]) -> str:
    key = key_map.get(addr.lower(), "")
    return EXECUTIVE_URL.format(key) if key else ""


def get_current_executive(
    lifecycle: dict | None,
    hat_data: dict | None,
    proposals: list | None = None,
) -> dict | None:
    """Return the spell at the current on-chain hat address, with its status.

    Returns dict with title, date, status, url; or None if no hat or
    the hat spell isn't in lifecycle data.
    """
    if not lifecycle or not hat_data:
        return None
    hat_addr = (hat_data.get("hatAddress") or "").lower()
    if not hat_addr:
        return None
    key_map = _executive_key_map(proposals)
    for addr, spell in lifecycle.get("spells", {}).items():
        if addr.lower() != hat_addr:
            continue
        etypes = {e["type"] for e in spell.get("events", [])}
        if "cast" in etypes:
            status = "cast"
        elif "expired" in etypes:
            status = "expired"
        elif "hat" in etypes:
            status = "hat, not yet cast"
        else:
            status = "proposed"
        return {
            "title": short_title(spell.get("title", ""), 60),
            "date": spell.get("date", ""),
            "status": status,
            "url": _spell_vote_url(addr, key_map),
        }
    return None


def get_pending_non_hat_spells(
    lifecycle: dict | None,
    hat_data: dict | None,
    proposals: list | None = None,
) -> list[dict]:
    """Spells proposed in the lookback window, not cast/expired, excluding the current hat."""
    if not lifecycle:
        return []
    hat_addr = ((hat_data or {}).get("hatAddress") or "").lower()
    key_map = _executive_key_map(proposals)
    cutoff = (datetime.now(timezone.utc) - timedelta(days=PENDING_SPELL_LOOKBACK_DAYS)).strftime("%Y-%m-%d")
    pending = []
    for addr, spell in lifecycle.get("spells", {}).items():
        if hat_addr and addr.lower() == hat_addr:
            continue
        etypes = {e["type"] for e in spell.get("events", [])}
        if "cast" in etypes or "expired" in etypes:
            continue
        if "proposed" not in etypes:
            continue
        spell_date = spell.get("date", "")
        if spell_date < cutoff:
            continue
        pending.append({
            "title": short_title(spell.get("title", ""), 60),
            "date": spell_date,
            "url": _spell_vote_url(addr, key_map),
        })
    pending.sort(key=lambda x: x["date"], reverse=True)
    return pending


OPEN_PR_LOOKBACK_DAYS = 7


def get_open_atlas_proposals(since: datetime) -> list[dict]:
    """Open PRs created after the last session, capped at OPEN_PR_LOOKBACK_DAYS.

    Filters out PRs already surfaced in a prior session (created before `since`)
    and PRs older than the lookback window (likely stale/not actively discussed).
    """
    data = load_json(OPEN_PRS_FILE)
    if not isinstance(data, list):
        return []
    week_cutoff = datetime.now(timezone.utc) - timedelta(days=OPEN_PR_LOOKBACK_DAYS)
    cutoff = max(since, week_cutoff)
    filtered = []
    for pr in data:
        created = pr.get("created_at", "")
        if not created:
            continue
        try:
            created_dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
        except ValueError:
            continue
        if created_dt >= cutoff:
            filtered.append(pr)
    return filtered


def get_recent_forum_posts(since: datetime) -> list[dict]:
    index = load_json(FORUM_INDEX_FILE)
    if not index or not isinstance(index, list):
        return []
    since_str = since.strftime("%Y-%m-%d")
    recent = [p for p in index if p.get("published", "") >= since_str]
    recent.sort(key=lambda x: x.get("published", ""), reverse=True)
    return recent


# ---------------------------------------------------------------------------
# Section printers
# ---------------------------------------------------------------------------

def _fmt_abs_delta(delta: float) -> str:
    """Format an absolute dollar delta in B/M/K with sign."""
    sign = "+" if delta >= 0 else "-"
    mag = abs(delta)
    if mag >= 1e9:
        return f"{sign}${mag / 1e9:.2f}B"
    if mag >= 1e6:
        return f"{sign}${mag / 1e6:.0f}M"
    return f"{sign}${mag / 1e3:.0f}K"


def print_market_section(moves: list[tuple] | None) -> bool:
    if not moves:
        return False
    print(f"\n{bold('=== MARKET ACTIVITY ===')} {dim('(daily)')}")
    lines: dict[int, list[str]] = {}
    for label, pct, value, abs_delta, kind, line in moves:
        direction = "+" if pct > 0 else ""
        if kind in ("supply", "stablecoin_sum"):
            delta_str = _fmt_abs_delta(abs_delta)
            entry = f"{label} {direction}{pct:.1f}% ({delta_str}, ${value / 1e9:.2f}B)"
        elif value >= 1000:
            entry = f"{label} {direction}{pct:.1f}% (${value:,.0f})"
        else:
            entry = f"{label} {direction}{pct:.1f}% (${value:.4f})"
        lines.setdefault(line, []).append(entry)
    for line_num in sorted(lines):
        print(f"  {', '.join(lines[line_num])}")
    return True


def _format_ended_poll(p: dict) -> None:
    tag = f" [{TYPE_LABELS.get(p['poll_type'], '')}]" if p["poll_type"] in TYPE_LABELS else ""
    pr_num = p.get("atlas_pr")
    pr_ref = f" -> PR #{pr_num}" if pr_num else ""
    nv = f" | non-voters: {', '.join(p['non_voters'])}" if p["non_voters"] else ""
    print(f"    Poll #{p['id']} ended {p['end_date']}: {p['result']}{tag}{pr_ref}{nv}")
    print(f"      {dim(POLL_URL.format(p['id']))}")


def _format_active_poll(p: dict) -> None:
    tag = f" [{TYPE_LABELS.get(p['poll_type'], '')}]" if p["poll_type"] in TYPE_LABELS else ""
    nv = f" | not yet voted: {', '.join(p['non_voters'])}" if p["non_voters"] else ""
    print(f"    #{p['id']} {short_title(p['title'], 50)}{tag} (ends {p['end_date']}{nv})")
    print(f"      {dim(POLL_URL.format(p['id']))}")


def print_polls_section(ended: list[dict], active: list[dict], since_label: str) -> bool:
    if not ended and not active:
        return False
    _section_header("POLLS", since_label)
    if ended:
        _subheader("Ended")
        for p in ended:
            _format_ended_poll(p)
    if active:
        _subheader("Active")
        for p in active:
            _format_active_poll(p)
    return True


def print_spells_section(current: dict | None, pending: list[dict]) -> bool:
    if not current and not pending:
        return False
    print(f"\n{bold('=== SPELLS ===')}")
    if current:
        _subheader("Current")
        date_label = dim(f"({current['date']})")
        status_tag = dim(f"[{current['status']}]")
        print(f"    {current['title']} {date_label} {status_tag}")
        if current.get("url"):
            print(f"      {dim(current['url'])}")
    if pending:
        _subheader("Pending")
        for s in pending:
            date_label = dim(f"({s['date']})")
            print(f"    {s['title']} {date_label}")
            if s.get("url"):
                print(f"      {dim(s['url'])}")
    return True


def print_proposals_section(open_prs: list[dict], since_label: str) -> bool:
    """Open (non-draft) Atlas PRs — early signal of upcoming governance changes."""
    if not open_prs:
        return False
    print(f"\n{bold('=== ATLAS PROPOSALS ===')} {dim(f'({len(open_prs)} new since {since_label})')}")
    for pr in open_prs:
        opened = (pr.get("created_at") or "")[:10]
        user = pr.get("user", "")
        title = short_title(pr.get("title", ""), 55)
        user_tag = dim(f"@{user}") if user else ""
        opened_label = dim(f"(opened {opened})")
        print(f"  #{pr['number']} {title} {opened_label} {user_tag}")
        if pr.get("url"):
            print(f"    {dim(pr['url'])}")
    return True


def print_forum_section(posts: list[dict], since_label: str) -> bool:
    if not posts:
        return False
    print(f"\n{bold('=== FORUM ACTIVITY ===')} {dim(f'({len(posts)} new since {since_label})')}")
    for p in posts:
        cat = dim(f"[{p.get('category', '')}]") if p.get("category") else ""
        print(f"  {p.get('published', '')} {p.get('title', '')[:65]} {cat}")
        if p.get("url"):
            print(f"    {dim(p['url'])}")
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
    since_label = since.strftime("%b %d %H:%M UTC")
    lifecycle = load_json(LIFECYCLE_FILE)
    hat_data = load_json(HAT_FILE)
    proposals = load_json(EXECUTIVE_PROPOSALS_FILE)
    matrix = load_json(VOTE_MATRIX_FILE)

    moves = get_market_moves()
    current_spell = get_current_executive(lifecycle, hat_data, proposals)
    pending_spells = get_pending_non_hat_spells(lifecycle, hat_data, proposals)
    ended_polls = get_ended_polls_since(matrix, since)
    active_polls = get_active_polls(matrix)
    open_prs = get_open_atlas_proposals(since)
    forum_posts = get_recent_forum_posts(since)

    print(dim(f"Session briefing — new activity since {since_label}"))

    # Always-on (state-of-now) sections
    print_market_section(moves)
    print_spells_section(current_spell, pending_spells)

    # Time-bounded sections — only show the window fallback if all three are empty
    any_new = False
    any_new |= print_polls_section(ended_polls, active_polls, since_label)
    any_new |= print_proposals_section(open_prs, since_label)
    any_new |= print_forum_section(forum_posts, since_label)

    if not any_new:
        print(dim(f"\n  (no new polls, atlas proposals, or forum activity since {since_label})"))

    if not MARKET_DB_FILE.exists():
        print(dim("\n  Set MESSARI_API_KEY in .env for price data."))

    save_session_timestamp()


if __name__ == "__main__":
    main()
