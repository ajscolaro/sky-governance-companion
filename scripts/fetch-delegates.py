#!/usr/bin/env python3
"""Fetch Aligned Delegate vote rationales via per-thread RSS feeds.

Reads the delegate roster from data/delegates/roster.json (built from the Atlas),
fetches each AD's forum thread RSS, filters to only the AD's own posts,
sanitizes all content (forum posts are untrusted), and stores per-AD post files
under data/delegates/{slug}/.

Security: All forum content is treated as untrusted anonymous input.
Same sanitization pipeline as fetch-forum.py — HTML stripping, injection
marker removal, content length limits.
"""

from __future__ import annotations

import argparse
import html
import html.parser
import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data" / "delegates"
ROSTER_FILE = DATA_DIR / "roster.json"
INDEX_FILE = PROJECT_DIR / "data" / "index.json"

FETCH_TIMEOUT = 15
USER_AGENT = "SkyAtlasExplorer/1.0 (governance research tool)"

# Limits to bound storage and injection surface
MAX_TITLE_LEN = 200
MAX_BODY_LEN = 8000  # Vote rationales can be longer than general forum posts

# Discourse uses the dc: namespace for creator
DC_NS = "http://purl.org/dc/elements/1.1/"


# --- HTML stripping (identical to fetch-forum.py) ---

class _HTMLTextExtractor(html.parser.HTMLParser):
    """Extract plain text from HTML, collapsing whitespace."""

    def __init__(self):
        super().__init__()
        self._parts: list[str] = []
        self._skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip = True
        elif tag in ("br", "p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"):
            self._parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip = False
        elif tag in ("p", "div", "li", "tr"):
            self._parts.append("\n")

    def handle_data(self, data):
        if not self._skip:
            self._parts.append(data)

    def get_text(self) -> str:
        return "".join(self._parts)


def strip_html(raw_html: str) -> str:
    """Convert HTML to plain text."""
    parser = _HTMLTextExtractor()
    try:
        parser.feed(raw_html)
        return parser.get_text()
    except Exception:
        return re.sub(r"<[^>]+>", " ", raw_html)


# --- Sanitization (identical to fetch-forum.py) ---

def sanitize(text: str, max_len: int | None = None) -> str:
    """Aggressively sanitize untrusted forum text."""
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"<\|[^|]*\|>", "", text)
    text = re.sub(r"\[SYSTEM\]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\[INST\]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\[/INST\]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"[\x00-\x08\x0b-\x0c\x0e-\x1f]", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r" {2,}", " ", text)
    text = text.strip()
    if max_len and len(text) > max_len:
        text = text[:max_len] + "..."
    return text


# --- Roster management ---

def extract_topic_info(forum_url: str) -> tuple[str, int] | None:
    """Extract (slug, topic_id) from a Discourse forum URL.

    Handles URLs like:
      https://forum.skyeco.com/t/cloaky-ad-recognition-submission/21082
      https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/90
    """
    m = re.search(r"/t/([^/]+)/(\d+)", forum_url)
    if m:
        return m.group(1), int(m.group(2))
    return None


def build_roster_from_atlas() -> list[dict]:
    """Parse the Atlas index to find the AD roster and extract forum URLs.

    Reads the Active Data table at A.1.5.1.5.0.6.1 from the Atlas source file
    using line offsets from the index.
    """
    if not INDEX_FILE.exists():
        print("Error: Atlas index not found. Run scripts/setup.sh first.", file=sys.stderr)
        return []

    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        index = json.load(f)

    # Find the Active Data entry for current ADs
    ad_entry = None
    for doc in index:
        if doc.get("number") == "A.1.5.1.5.0.6.1":
            ad_entry = doc
            break

    if not ad_entry:
        print("Warning: Could not find AD roster (A.1.5.1.5.0.6.1) in index.", file=sys.stderr)
        return []

    # Read the relevant lines from the Atlas file
    atlas_file = PROJECT_DIR / ".atlas-repo" / "Sky Atlas" / "Sky Atlas.md"
    if not atlas_file.exists():
        print("Error: Atlas file not found.", file=sys.stderr)
        return []

    line_start = ad_entry.get("line_start", 0)
    line_end = ad_entry.get("line_end", line_start + 100)

    with open(atlas_file, "r", encoding="utf-8") as f:
        lines = []
        for i, line in enumerate(f, 1):
            if i >= line_start and i <= line_end:
                lines.append(line)
            elif i > line_end:
                break

    content = "".join(lines)

    # Parse the markdown table for forum URLs
    # Table format: | Delegate Name | EA Address | Delegation Contract | Forum Post |
    roster = []
    for line in content.split("\n"):
        if not line.strip().startswith("|"):
            continue
        # Skip header and separator rows
        if "Delegate Name" in line or line.strip().startswith("|--") or line.strip().startswith("|-"):
            continue

        # Extract delegate name (first cell)
        cells = [c.strip() for c in line.split("|")]
        cells = [c for c in cells if c]  # Remove empty strings from leading/trailing pipes
        if len(cells) < 4:
            continue

        delegate_name = cells[0].strip()

        # Extract forum URL from last cell
        forum_cell = cells[-1]
        url_match = re.search(r"https://forum\.skyeco\.com/t/[^\s\)]+", forum_cell)
        if not url_match:
            continue

        forum_url = url_match.group(0)
        topic_info = extract_topic_info(forum_url)
        if not topic_info:
            continue

        topic_slug, topic_id = topic_info

        # Derive a filesystem-safe slug from the delegate name
        fs_slug = re.sub(r"[^a-z0-9]+", "-", delegate_name.lower()).strip("-")

        roster.append({
            "delegate_name": delegate_name,
            "slug": fs_slug,
            "topic_id": topic_id,
            "topic_slug": topic_slug,
            "forum_url": forum_url.rstrip("/"),
            "forum_username": None,  # Discovered on first RSS fetch
        })

    return roster


def load_roster() -> list[dict]:
    """Load existing roster or build from Atlas."""
    if ROSTER_FILE.exists():
        with open(ROSTER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_roster(roster: list[dict]) -> None:
    """Save roster to disk."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(ROSTER_FILE, "w", encoding="utf-8") as f:
        json.dump(roster, f, indent=2)


# --- RSS fetching ---

def fetch_rss(url: str) -> bytes:
    """Fetch RSS feed content."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
        return resp.read()


def parse_date(date_str: str) -> str:
    """Parse RSS pubDate to ISO date string (YYYY-MM-DD)."""
    for fmt in (
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%Y-%m-%dT%H:%M:%S%z",
    ):
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    m = re.search(r"(\d{4}-\d{2}-\d{2})", date_str)
    return m.group(1) if m else "unknown"


def parse_datetime(date_str: str) -> str:
    """Parse RSS pubDate to ISO datetime string."""
    for fmt in (
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%Y-%m-%dT%H:%M:%S%z",
    ):
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            continue
    return date_str.strip()


def fetch_delegate_posts(delegate: dict, quiet: bool = False) -> list[dict]:
    """Fetch and parse RSS for a single delegate, filtering to their posts only."""
    topic_id = delegate["topic_id"]
    topic_slug = delegate["topic_slug"]
    rss_url = f"https://forum.skyeco.com/t/{topic_slug}/{topic_id}.rss"

    try:
        xml_bytes = fetch_rss(rss_url)
    except (urllib.error.URLError, OSError) as e:
        if not quiet:
            print(f"  Warning: Could not fetch RSS for {delegate['delegate_name']}: {e}",
                  file=sys.stderr)
        return []

    root = ET.fromstring(xml_bytes)
    all_posts = []

    for item in root.iter("item"):
        author = sanitize(item.findtext(f"{{{DC_NS}}}creator") or "", 100)
        pub_date_raw = item.findtext("pubDate") or ""
        raw_title = item.findtext("title") or ""
        raw_body = item.findtext("description") or ""
        link = (item.findtext("link") or "").strip()
        guid = (item.findtext("guid") or "").strip()

        plain_body = strip_html(raw_body)

        all_posts.append({
            "author": author,
            "date": parse_date(pub_date_raw),
            "datetime": parse_datetime(pub_date_raw),
            "title": sanitize(raw_title, MAX_TITLE_LEN),
            "body": sanitize(plain_body, MAX_BODY_LEN),
            "link": link,
            "guid": guid,
        })

    # Auto-discover forum username if not yet known.
    # Strategy: fetch the thread's first post (the recognition submission) via
    # the Discourse topic JSON endpoint, which returns the thread creator reliably.
    # Fallback: use the dc:creator from the oldest RSS item (RSS may not include
    # post #1 if the feed is capped, but the oldest available post is most likely
    # from the AD themselves).
    if all_posts and not delegate.get("forum_username"):
        # Try Discourse JSON API for the thread creator (post #1 author)
        json_url = f"https://forum.skyeco.com/t/{topic_slug}/{topic_id}.json"
        try:
            req = urllib.request.Request(json_url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
                topic_data = json.loads(resp.read())
            # The first post stream entry's username is the thread creator
            post_stream = topic_data.get("post_stream", {}).get("posts", [])
            if post_stream:
                creator = sanitize(post_stream[0].get("username", ""), 100)
                if creator:
                    delegate["forum_username"] = creator
        except (urllib.error.URLError, OSError, json.JSONDecodeError, KeyError):
            pass

        # Fallback: oldest RSS item's dc:creator
        if not delegate.get("forum_username"):
            sorted_posts = sorted(all_posts, key=lambda p: p["date"])
            delegate["forum_username"] = sorted_posts[0]["author"]

    # Filter to only the AD's own posts
    username = delegate.get("forum_username")
    if username:
        ad_posts = [p for p in all_posts if p["author"].lower() == username.lower()]
    else:
        # Can't filter without username — return all (will be filtered on next run)
        ad_posts = all_posts

    return ad_posts


# --- Storage ---

def load_existing_posts(delegate_slug: str) -> set[str]:
    """Load GUIDs of already-cached posts for a delegate."""
    posts_dir = DATA_DIR / delegate_slug
    if not posts_dir.exists():
        return set()
    existing = set()
    for f in posts_dir.glob("*.json"):
        try:
            with open(f, "r", encoding="utf-8") as fh:
                data = json.load(fh)
                if "guid" in data:
                    existing.add(data["guid"])
        except (json.JSONDecodeError, KeyError):
            continue
    return existing


def save_post(delegate_slug: str, post: dict) -> None:
    """Save a single post file."""
    posts_dir = DATA_DIR / delegate_slug
    posts_dir.mkdir(parents=True, exist_ok=True)

    # Use date + hash of guid for filename to ensure uniqueness and sort order
    date = post.get("date", "unknown")
    guid_hash = abs(hash(post.get("guid", ""))) % 100000
    filename = f"{date}_{guid_hash:05d}.json"

    post_data = {
        "delegate": delegate_slug,
        "author": post["author"],
        "date": post["date"],
        "datetime": post["datetime"],
        "title": post["title"],
        "body": post["body"],
        "link": post["link"],
        "guid": post["guid"],
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    with open(posts_dir / filename, "w", encoding="utf-8") as f:
        json.dump(post_data, f, indent=2)


# --- Main ---

def main():
    parser = argparse.ArgumentParser(description="Fetch AD vote rationales via RSS")
    parser.add_argument("--quiet", action="store_true", help="Suppress output")
    parser.add_argument("--rebuild-roster", action="store_true",
                        help="Rebuild roster from Atlas (overwrites forum_username discovery)")
    parser.add_argument("--delegate", type=str, help="Fetch only this delegate (by slug)")
    args = parser.parse_args()

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Load or build roster
    roster = load_roster()
    if not roster or args.rebuild_roster:
        if not args.quiet:
            print("Building delegate roster from Atlas...")
        new_roster = build_roster_from_atlas()
        if new_roster:
            # Preserve discovered forum_usernames from existing roster
            existing_usernames = {d["topic_id"]: d.get("forum_username")
                                  for d in roster if d.get("forum_username")}
            for d in new_roster:
                if d["topic_id"] in existing_usernames:
                    d["forum_username"] = existing_usernames[d["topic_id"]]
            roster = new_roster
            save_roster(roster)
            if not args.quiet:
                print(f"  Roster: {len(roster)} delegates")
        elif not roster:
            print("Error: Could not build roster and no existing roster found.", file=sys.stderr)
            sys.exit(1)

    # Filter to single delegate if requested
    targets = roster
    if args.delegate:
        targets = [d for d in roster if d["slug"] == args.delegate]
        if not targets:
            print(f"Error: Delegate '{args.delegate}' not found in roster.", file=sys.stderr)
            sys.exit(1)

    total_new = 0
    for delegate in targets:
        existing_guids = load_existing_posts(delegate["slug"])
        posts = fetch_delegate_posts(delegate, quiet=args.quiet)

        new_count = 0
        for post in posts:
            if post["guid"] not in existing_guids:
                save_post(delegate["slug"], post)
                new_count += 1
                existing_guids.add(post["guid"])

        total_new += new_count
        if not args.quiet and new_count > 0:
            print(f"  {delegate['delegate_name']}: {new_count} new post(s)")

    # Save roster (forum_usernames may have been discovered)
    save_roster(roster)

    if not args.quiet:
        print(f"Delegates: {total_new} new post(s) across {len(targets)} delegate(s)")


if __name__ == "__main__":
    main()
