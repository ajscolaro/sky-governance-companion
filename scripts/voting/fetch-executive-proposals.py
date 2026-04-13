#!/usr/bin/env python3
"""Fetch executive proposal text and track spell lifecycle events.

Syncs the index from sky-ecosystem/executive-votes, fetches full proposal markdown
for each spell, parses structured metadata, distills it into lifecycle.json, then
cleans up the raw files. lifecycle.json is the source of truth for spell tracking.

Pipeline:
  1. Fetch raw proposal text (ephemeral cache in data/voting/executive/proposals/)
  2. Parse into structured metadata
  3. Enrich lifecycle.json with distilled data (summary, actions, refs, market context)
  4. Clean up raw files after enrichment

Data flow:
  sky-ecosystem/executive-votes repo  ->  (parse)  ->  data/voting/executive/lifecycle.json
  vote.sky.money /api/executive       ->  (lifecycle events)  ->  data/voting/executive/lifecycle.json
  data/market.db                      ->  (query on the fly via scripts/market/market.py)
  history/_log.md                     ->  (cross-refs)        ->  data/voting/executive/lifecycle.json
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

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
PROPOSALS_DIR = PROJECT_DIR / "data" / "voting" / "executive" / "proposals"
INDEX_FILE = PROJECT_DIR / "data" / "voting" / "executive" / "index.json"
LIFECYCLE_FILE = PROJECT_DIR / "data" / "voting" / "executive" / "lifecycle.json"
LOG_FILE = PROJECT_DIR / "history" / "_log.md"

REPO_RAW_BASE = "https://raw.githubusercontent.com/sky-ecosystem/executive-votes/main"
API_BASE = "https://vote.sky.money/api"

FETCH_TIMEOUT = 30
USER_AGENT = "SkyAtlasExplorer/1.0 (governance research tool)"
MAX_RETRIES = 3
RETRY_BACKOFF = 5
REQUEST_DELAY = 0.5

MAX_STR_LEN = 500


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def sanitize_str(text: str, max_len: int = MAX_STR_LEN) -> str:
    """Strip control chars and cap length."""
    text = re.sub(r"[\x00-\x08\x0b-\x0c\x0e-\x1f]", "", text)
    text = text.strip()
    if len(text) > max_len:
        text = text[:max_len] + "..."
    return text


def clean_title(title: str) -> str:
    """Strip boilerplate prefixes from executive vote titles."""
    title = re.sub(
        r"^(?:Template\s*-?\s*)?(?:\[Executive (?:Vote|Proposal)\]\s*)?",
        "", title, flags=re.IGNORECASE,
    )
    # Strip trailing " - Date, Year" if it duplicates the date field
    title = re.sub(r"\s*-\s*(?:January|February|March|April|May|June|July|"
                   r"August|September|October|November|December)\s+\d{1,2},\s+\d{4}\s*$",
                   "", title)
    return title.strip()


def fetch_url(url: str, *, as_json: bool = False):
    """Fetch a URL with retries. Returns text or parsed JSON."""
    backoff = RETRY_BACKOFF
    for attempt in range(MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
                body = resp.read()
                if as_json:
                    return json.loads(body)
                return body.decode("utf-8")
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


# ---------------------------------------------------------------------------
# Proposal text fetching and parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> dict:
    """Extract YAML-ish frontmatter from proposal markdown."""
    fm = {}
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return fm
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            value = value.strip().strip('"').strip("'")
            fm[key.strip()] = value
    return fm


def extract_atlas_refs(text: str) -> list[str]:
    """Extract Atlas document address references (sky-atlas.io links)."""
    refs = re.findall(r"sky-atlas\.io/(?:#|%23)(A\.[0-9.]+)", text)
    return sorted(set(refs))


def extract_governance_polls(text: str) -> list[int]:
    """Extract governance poll references."""
    polls = []
    for match in re.finditer(
        r"Governance Poll[s]?\s+(\d+)(?:\s+and\s+(\d+))?", text, re.IGNORECASE
    ):
        polls.append(int(match.group(1)))
        if match.group(2):
            polls.append(int(match.group(2)))
    return sorted(set(polls))


def extract_forum_links(text: str) -> list[str]:
    """Extract Sky Forum thread URLs."""
    links = re.findall(r"https?://forum\.(?:sky(?:eco)?|makerdao)\.com/t/[^\s)\]]+", text)
    return sorted(set(links))


def extract_actions(text: str) -> list[dict]:
    """Extract individual action sections from the proposal details."""
    actions = []
    details_match = re.search(r"## Proposal Details\s*\n(.*)", text, re.DOTALL)
    if not details_match:
        return actions

    details_text = details_match.group(1)
    sections = re.split(r"\n### ", details_text)

    # The first chunk may itself start with a ### heading
    start = 0 if sections and sections[0].lstrip().startswith("### ") else 1
    if start == 0 and sections:
        sections[0] = re.sub(r"^[\s]*###\s*", "", sections[0])

    for section in sections[start:]:
        lines = section.strip().split("\n")
        title = sanitize_str(lines[0].strip())
        body = "\n".join(lines[1:])

        if title.lower().startswith(("review", "resources")):
            break

        action = {"title": title}

        auth_match = re.search(r"\*\*Authorization\*\*:\s*(.+)", body)
        if auth_match:
            action["authorization"] = sanitize_str(auth_match.group(1), max_len=200)

        actions.append(action)

    return actions


def parse_proposal(text: str, metadata: dict) -> dict:
    """Parse a full proposal markdown into structured metadata."""
    frontmatter = parse_frontmatter(text)

    return {
        "spell_address": metadata.get("address", frontmatter.get("address", "")),
        "date": metadata.get("date", frontmatter.get("date", "")),
        "title": sanitize_str(metadata.get("title", frontmatter.get("title", ""))),
        "summary": sanitize_str(metadata.get("summary", frontmatter.get("summary", ""))),
        "actions": extract_actions(text),
        "atlas_refs": extract_atlas_refs(text),
        "governance_polls": extract_governance_polls(text),
        "forum_links": extract_forum_links(text),
    }


def slug_from_path(path: str) -> str:
    """Derive a slug from the repo file path."""
    name = Path(path).stem
    name = re.sub(r"^(?:oos-)?executive-vote-", "", name)
    return name


def sync_proposals(*, force: bool = False, quiet: bool = False) -> list[dict]:
    """Sync the index and fetch proposal markdown for any new/missing entries.

    Returns list of parsed proposal metadata dicts (only newly fetched ones).
    """
    PROPOSALS_DIR.mkdir(parents=True, exist_ok=True)

    if not quiet:
        print("Fetching executive-votes index...")
    try:
        index = fetch_url(f"{REPO_RAW_BASE}/index.json", as_json=True)
    except (urllib.error.URLError, OSError) as e:
        print(f"Error: Could not fetch index: {e}", file=sys.stderr)
        return []

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    if not quiet:
        print(f"Index: {len(index)} proposals")

    fetched = []
    for entry in index:
        path = entry.get("path", "")
        metadata = entry.get("metadata", {})
        slug = slug_from_path(path)
        addr = (metadata.get("address") or "").lower()

        # Skip if already enriched in lifecycle (unless --force)
        if not force:
            lifecycle = load_lifecycle()
            if addr and addr in lifecycle.get("spells", {}):
                spell = lifecycle["spells"][addr]
                if spell.get("summary") and spell.get("actions"):
                    continue

        md_file = PROPOSALS_DIR / f"{slug}.md"
        json_file = PROPOSALS_DIR / f"{slug}.json"

        if md_file.exists() and json_file.exists() and not force:
            # Already cached but not yet enriched — load parsed data
            with open(json_file, "r", encoding="utf-8") as f:
                parsed = json.load(f)
            parsed.setdefault("key", slug)
            parsed.setdefault("proposal_url", f"{REPO_RAW_BASE}/{path}")
            fetched.append(parsed)
            continue

        if not quiet:
            print(f"  Fetching {slug}...")

        try:
            text = fetch_url(f"{REPO_RAW_BASE}/{path}")
        except (urllib.error.URLError, OSError) as e:
            if not quiet:
                print(f"    FAILED: {e}")
            continue

        with open(md_file, "w", encoding="utf-8") as f:
            f.write(text)

        parsed = parse_proposal(text, metadata)
        parsed["key"] = slug  # preserve the slug for lifecycle key
        parsed["proposal_url"] = f"{REPO_RAW_BASE}/{path}"
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(parsed, f, indent=2)

        fetched.append(parsed)
        time.sleep(REQUEST_DELAY)

    if not quiet:
        if fetched:
            print(f"  {len(fetched)} proposal(s) to process")
        else:
            print("  All proposals already enriched in lifecycle")

    return fetched


# ---------------------------------------------------------------------------
# Lifecycle tracking
# ---------------------------------------------------------------------------

def load_lifecycle() -> dict:
    """Load or initialize the lifecycle tracking file."""
    if LIFECYCLE_FILE.exists():
        with open(LIFECYCLE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"spells": {}, "last_updated": None}


def save_lifecycle(data: dict) -> None:
    """Write lifecycle data to committed snapshot directory."""
    LIFECYCLE_FILE.parent.mkdir(parents=True, exist_ok=True)
    data["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(LIFECYCLE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def enrich_lifecycle(lifecycle: dict, proposals: list[dict], *, quiet: bool = False) -> int:
    """Enrich lifecycle entries with distilled proposal data.

    For each proposal, ensure a lifecycle entry exists and populate it with
    summary, condensed actions, atlas_refs, governance_polls, and forum_links.
    Returns count of entries enriched.
    """
    enriched = 0

    for meta in proposals:
        addr = (meta.get("spell_address") or "").lower()
        if not addr:
            continue

        date_str = meta.get("date", "")
        if isinstance(date_str, str) and "T" in date_str:
            event_time = date_str
        else:
            event_time = f"{date_str}T00:00:00Z" if date_str else None

        raw_title = meta.get("title", "")
        title = clean_title(raw_title)

        # Condense actions: keep only title + authorization
        actions = []
        for a in meta.get("actions", []):
            condensed = {"title": a["title"]}
            if a.get("authorization"):
                condensed["authorization"] = a["authorization"]
            actions.append(condensed)

        if addr not in lifecycle["spells"]:
            lifecycle["spells"][addr] = {
                "events": [{"type": "proposed", "at": event_time}] if event_time else [],
            }

        spell = lifecycle["spells"][addr]

        # Always update these fields from the parsed proposal
        spell["title"] = title
        spell["date"] = date_str[:10] if date_str else spell.get("date", "")
        if meta.get("key"):
            spell["key"] = meta["key"]
        spell["summary"] = sanitize_str(meta.get("summary", ""), max_len=300)
        spell["actions"] = actions
        spell["atlas_refs"] = meta.get("atlas_refs", [])
        spell["governance_polls"] = meta.get("governance_polls", [])
        spell["forum_links"] = meta.get("forum_links", [])
        if meta.get("proposal_url"):
            spell["proposal_url"] = meta["proposal_url"]

        enriched += 1

    if enriched and not quiet:
        print(f"  Enriched {enriched} spell(s) with proposal data")

    return enriched


def update_lifecycle_from_api(lifecycle: dict, *, quiet: bool = False) -> int:
    """Check live API for state transitions. Returns count of new events."""
    try:
        proposals = fetch_url(f"{API_BASE}/executive", as_json=True)
        hat_data = fetch_url(f"{API_BASE}/executive/hat", as_json=True)
    except (urllib.error.URLError, OSError) as e:
        if not quiet:
            print(f"  Warning: Could not fetch live API data: {e}")
        return 0

    hat_address = (hat_data.get("hatAddress") or hat_data.get("address") or "").lower()
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    events_added = 0

    for p in proposals:
        addr = (p.get("address") or "").lower()
        if not addr:
            continue

        spell_data = p.get("spellData") or {}
        has_been_cast = spell_data.get("hasBeenCast", False)
        is_hat = (addr == hat_address)

        # Ensure spell exists in lifecycle
        if addr not in lifecycle["spells"]:
            date_str = p.get("date", "")
            lifecycle["spells"][addr] = {
                "title": clean_title(p.get("title") or ""),
                "date": date_str[:10] if date_str else "",
                "key": p.get("key", ""),
                "summary": sanitize_str(p.get("proposalBlurb") or "", max_len=300),
                "actions": [],
                "events": [{"type": "proposed", "at": date_str or now_iso}],
                "atlas_refs": [],
                "governance_polls": [],
                "forum_links": [],
            }
            events_added += 1

        spell = lifecycle["spells"][addr]
        existing_types = {e["type"] for e in spell.get("events", [])}

        # Hat transition
        if is_hat and "hat" not in existing_types:
            sky_support = (
                hat_data.get("skyOnHat")
                or hat_data.get("skySupport")
                or spell_data.get("skySupport")
                or "0"
            )
            spell.setdefault("events", []).append({
                "type": "hat",
                "at": now_iso,
                "sky_support": str(sky_support),
            })
            events_added += 1
            if not quiet:
                print(f"  Lifecycle: {spell.get('title', '')[:60]} -> hat")

        # Cast transition
        if has_been_cast and "cast" not in existing_types:
            spell.setdefault("events", []).append({"type": "cast", "at": now_iso})
            events_added += 1
            if not quiet:
                print(f"  Lifecycle: {spell.get('title', '')[:60]} -> cast")

        # Expiration
        expiration = spell_data.get("expiration", "")
        if expiration and not has_been_cast and "expired" not in existing_types:
            try:
                exp_dt = datetime.fromisoformat(expiration.replace("Z", "+00:00"))
                if datetime.now(timezone.utc) > exp_dt:
                    spell.setdefault("events", []).append({"type": "expired", "at": expiration})
                    events_added += 1
                    if not quiet:
                        print(f"  Lifecycle: {spell.get('title', '')[:60]} -> expired")
            except (ValueError, TypeError):
                pass

    return events_added


# ---------------------------------------------------------------------------
# Atlas PR cross-references
# ---------------------------------------------------------------------------

SPELL_PR_PATTERNS = [
    re.compile(r"(?:add\s+)?(\d{4}-\d{2}-\d{2})\s+(?:spell|executive)\s+(?:changes|updates?)", re.IGNORECASE),
    re.compile(r"(?:Atlas\s+update\s+from\s+)?(\d{4}-\d{2}-\d{2})\s+(?:Exec|executive)", re.IGNORECASE),
    re.compile(r"(\w+\s+\d{1,2})(?:st|nd|rd|th)?\s+(?:\d{4}\s+)?(?:Spell|Executive)\s+(?:updates?|changes)", re.IGNORECASE),
]


def parse_log_date(text: str) -> str | None:
    """Try to extract a YYYY-MM-DD date from a log title."""
    m = re.search(r"(\d{4}-\d{2}-\d{2})", text)
    if m:
        return m.group(1)
    # Try month-day patterns like "Oct 16th"
    months = {
        "jan": "01", "feb": "02", "mar": "03", "apr": "04",
        "may": "05", "jun": "06", "jul": "07", "aug": "08",
        "sep": "09", "oct": "10", "nov": "11", "dec": "12",
    }
    m = re.search(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+(\d{1,2})", text, re.IGNORECASE)
    if m:
        month = months.get(m.group(1)[:3].lower())
        day = m.group(2).zfill(2)
        # Infer year from context (check for explicit year)
        year_m = re.search(r"(\d{4})", text)
        year = year_m.group(1) if year_m else "2025"  # safe default
        return f"{year}-{month}-{day}" if month else None
    return None


def cross_reference_atlas_prs(lifecycle: dict, *, quiet: bool = False) -> int:
    """Scan history/_log.md for Flow 2 (spell-recording) PRs and link to spells.

    Only links PRs with spell-related titles (e.g., "spell changes", "executive
    changes"). Flow 1 (text-edit) PRs are correctly filtered out — they don't
    reference spells and shouldn't be linked here.

    Matches by date extraction from PR title; uses +/-3 day tolerance.
    Stores results as atlas_prs on each spell entry.
    """
    if not LOG_FILE.exists():
        return 0

    log_text = LOG_FILE.read_text(encoding="utf-8")
    linked = 0

    # Parse log entries: | #219 | Title | 2026-04-09 | sections | status |
    for match in re.finditer(
        r"\|\s*#(\d+)\s*\|\s*(.+?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|", log_text
    ):
        pr_num = int(match.group(1))
        pr_title = match.group(2).strip()
        pr_merged = match.group(3)

        # Check if this PR title references spell/executive changes
        is_spell_pr = any(p.search(pr_title) for p in SPELL_PR_PATTERNS)
        if not is_spell_pr:
            continue

        # Extract the date the spell was cast (from PR title, not merge date)
        spell_date = parse_log_date(pr_title)
        if not spell_date:
            continue

        # Find the matching spell by date (closest match within 3 days)
        best_addr = None
        best_delta = 999
        try:
            target = datetime.strptime(spell_date, "%Y-%m-%d")
        except ValueError:
            continue

        for addr, spell in lifecycle["spells"].items():
            try:
                sd = datetime.strptime(spell.get("date", ""), "%Y-%m-%d")
                delta = abs((target - sd).days)
                if delta < best_delta:
                    best_delta = delta
                    best_addr = addr
            except ValueError:
                continue

        if best_addr and best_delta <= 3:
            spell = lifecycle["spells"][best_addr]
            atlas_prs = spell.setdefault("atlas_prs", [])
            pr_entry = {"pr": pr_num, "title": pr_title, "merged": pr_merged}
            # Avoid duplicates
            if not any(p["pr"] == pr_num for p in atlas_prs):
                atlas_prs.append(pr_entry)
                linked += 1

    if linked and not quiet:
        print(f"  Linked {linked} Atlas PR(s) to executive spells")

    return linked



# ---------------------------------------------------------------------------
# Cleanup
# ---------------------------------------------------------------------------

def cleanup_proposals(lifecycle: dict, *, quiet: bool = False) -> int:
    """Delete raw proposal files that have been fully enriched into lifecycle.

    A proposal is considered fully enriched when its lifecycle entry has
    summary, actions, and atlas_refs populated.
    """
    if not PROPOSALS_DIR.exists():
        return 0

    cleaned = 0
    for f in list(PROPOSALS_DIR.iterdir()):
        if f.name == ".gitkeep":
            continue
        # Check if this proposal's data is in lifecycle
        if f.suffix == ".json" and f.name != "index.json":
            try:
                with open(f, "r", encoding="utf-8") as fh:
                    meta = json.load(fh)
                addr = (meta.get("spell_address") or "").lower()
                if addr and addr in lifecycle.get("spells", {}):
                    spell = lifecycle["spells"][addr]
                    if spell.get("summary") and spell.get("actions") is not None:
                        # Enriched — safe to delete both .json and .md
                        f.unlink(missing_ok=True)
                        f.with_suffix(".md").unlink(missing_ok=True)
                        cleaned += 1
                        continue
            except (json.JSONDecodeError, OSError):
                pass
        elif f.suffix == ".md":
            # May already be cleaned by the .json handler above
            if not f.exists():
                continue
            json_file = f.with_suffix(".json")
            if not json_file.exists():
                # Orphaned .md — clean it up
                f.unlink(missing_ok=True)
                cleaned += 1

    if cleaned and not quiet:
        print(f"  Cleaned up {cleaned} processed proposal file(s)")

    return cleaned


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Fetch executive proposal text and track spell lifecycle"
    )
    parser.add_argument("--quiet", action="store_true", help="Suppress output")
    parser.add_argument("--force", action="store_true", help="Re-fetch and re-enrich all proposals")
    parser.add_argument(
        "--no-cleanup", action="store_true",
        help="Keep raw proposal files after enrichment"
    )
    parser.add_argument(
        "--lifecycle-only", action="store_true",
        help="Only update lifecycle events from API, skip proposal sync"
    )
    args = parser.parse_args()

    lifecycle = load_lifecycle()

    # Step 1: Sync and parse proposals
    new_proposals = []
    if not args.lifecycle_only:
        new_proposals = sync_proposals(force=args.force, quiet=args.quiet)

    if not args.quiet:
        print("\nUpdating spell lifecycle...")

    # Step 2: Enrich lifecycle with distilled proposal data
    if new_proposals:
        enrich_lifecycle(lifecycle, new_proposals, quiet=args.quiet)

    # Step 2b: Backfill proposal_url for spells enriched before this field existed
    if INDEX_FILE.exists():
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            idx = json.load(f)
        for entry in idx:
            path = entry.get("path", "")
            addr = (entry.get("metadata", {}).get("address") or "").lower()
            if addr and addr in lifecycle.get("spells", {}) and not lifecycle["spells"][addr].get("proposal_url"):
                lifecycle["spells"][addr]["proposal_url"] = f"{REPO_RAW_BASE}/{path}"

    # Step 3: Update lifecycle events from live API
    new_events = update_lifecycle_from_api(lifecycle, quiet=args.quiet)
    if not args.quiet:
        if new_events:
            print(f"  {new_events} new lifecycle event(s)")
        else:
            print("  No new lifecycle events")

    # Step 4: Atlas PR cross-references
    cross_reference_atlas_prs(lifecycle, quiet=args.quiet)

    # Save lifecycle
    save_lifecycle(lifecycle)

    # Step 6: Cleanup processed proposal files
    if not args.no_cleanup and not args.lifecycle_only:
        cleanup_proposals(lifecycle, quiet=args.quiet)

    if not args.quiet:
        total = len(lifecycle["spells"])
        cast = sum(
            1 for s in lifecycle["spells"].values()
            if any(e["type"] == "cast" for e in s.get("events", []))
        )
        active = sum(
            1 for s in lifecycle["spells"].values()
            if not any(e["type"] in ("cast", "expired") for e in s.get("events", []))
        )
        with_prs = sum(1 for s in lifecycle["spells"].values() if s.get("atlas_prs"))
        print(f"\n  Summary: {total} spells ({cast} cast, {active} active)")
        print(f"  Atlas PR links: {with_prs}")


if __name__ == "__main__":
    main()
