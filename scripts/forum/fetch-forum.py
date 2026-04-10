#!/usr/bin/env python3
"""Fetch Sky Forum posts via RSS and store locally for search.

Parses Discourse RSS feeds, sanitizes all content (forum posts are untrusted),
and writes a searchable JSON index plus per-post files under data/forum/.
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

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
FORUM_DIR = PROJECT_DIR / "data" / "forum"
POSTS_DIR = FORUM_DIR / "posts"
INDEX_FILE = FORUM_DIR / "index.json"

DEFAULT_URL = "https://forum.skyeco.com/latest.rss"
FETCH_TIMEOUT = 15
USER_AGENT = "SkyAtlasExplorer/1.0 (governance research tool)"

# Limits to bound storage and injection surface
MAX_TITLE_LEN = 200
MAX_EXCERPT_LEN = 500
MAX_BODY_LEN = 5000

# Discourse uses the dc: namespace for creator
DC_NS = "http://purl.org/dc/elements/1.1/"


# --- HTML stripping ---

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
        # Fallback: crude tag stripping
        return re.sub(r"<[^>]+>", " ", raw_html)


# --- Sanitization ---

def sanitize(text: str, max_len: int | None = None) -> str:
    """Aggressively sanitize untrusted forum text.

    Extends the process-pr.sh sanitization pattern with additional
    protections for anonymous forum content.
    """
    # Decode HTML entities
    text = html.unescape(text)
    # Strip any remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Remove HTML comments (could hide injected instructions)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # Remove ChatML-style markers (<|...|>)
    text = re.sub(r"<\|[^|]*\|>", "", text)
    # Remove common prompt injection markers
    text = re.sub(r"\[SYSTEM\]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\[INST\]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\[/INST\]", "", text, flags=re.IGNORECASE)
    # Remove control characters (except newline and tab)
    text = re.sub(r"[\x00-\x08\x0b-\x0c\x0e-\x1f]", "", text)
    # Collapse excessive whitespace (3+ newlines → 2, multiple spaces → 1)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r" {2,}", " ", text)
    text = text.strip()
    # Truncate
    if max_len and len(text) > max_len:
        text = text[:max_len] + "..."
    return text


# --- RSS parsing ---

def fetch_rss(url: str) -> bytes:
    """Fetch RSS feed content."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
        return resp.read()


def parse_date(date_str: str) -> str:
    """Parse RSS pubDate to ISO date string (YYYY-MM-DD)."""
    # RSS dates are typically like: "Tue, 08 Apr 2026 14:08:00 +0000"
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
    # Fallback: try to extract YYYY-MM-DD
    m = re.search(r"(\d{4}-\d{2}-\d{2})", date_str)
    return m.group(1) if m else "unknown"


def extract_topic_id(url: str) -> int | None:
    """Extract Discourse topic ID from URL like /t/slug/12345."""
    m = re.search(r"/t/[^/]+/(\d+)", url)
    return int(m.group(1)) if m else None


def parse_rss(xml_bytes: bytes) -> list[dict]:
    """Parse RSS XML into a list of post dicts."""
    root = ET.fromstring(xml_bytes)
    posts = []

    for item in root.iter("item"):
        link = (item.findtext("link") or "").strip()
        topic_id = extract_topic_id(link)
        if topic_id is None:
            continue

        raw_title = item.findtext("title") or ""
        raw_body = item.findtext("description") or ""
        author = item.findtext(f"{{{DC_NS}}}creator") or ""
        pub_date = item.findtext("pubDate") or ""

        # Discourse may include multiple <category> elements
        categories = [c.text for c in item.findall("category") if c.text]
        category = categories[0] if categories else ""

        # Convert HTML body to plain text, then sanitize
        plain_body = strip_html(raw_body)

        posts.append({
            "topic_id": topic_id,
            "title": sanitize(raw_title, MAX_TITLE_LEN),
            "author": sanitize(author, 100),
            "category": sanitize(category, 100),
            "published": parse_date(pub_date),
            "url": link,
            "excerpt": sanitize(plain_body, MAX_EXCERPT_LEN),
            "body": sanitize(plain_body, MAX_BODY_LEN),
        })

    return posts


# --- Storage ---

def load_existing_ids() -> set[int]:
    """Load topic IDs already in the index."""
    if INDEX_FILE.exists():
        try:
            with open(INDEX_FILE, "r", encoding="utf-8") as f:
                return {p["topic_id"] for p in json.load(f)}
        except (json.JSONDecodeError, KeyError):
            pass
    return set()


def save_post(post: dict) -> None:
    """Write a single post file."""
    post_file = POSTS_DIR / f"{post['topic_id']}.json"
    post_data = {
        "topic_id": post["topic_id"],
        "title": post["title"],
        "author": post["author"],
        "category": post["category"],
        "published": post["published"],
        "url": post["url"],
        "body": post["body"],
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    with open(post_file, "w", encoding="utf-8") as f:
        json.dump(post_data, f, indent=2)


def rebuild_index() -> list[dict]:
    """Rebuild index.json from all post files."""
    index = []
    for post_file in sorted(POSTS_DIR.glob("*.json")):
        try:
            with open(post_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Index entry: metadata only (no full body)
            index.append({
                "topic_id": data["topic_id"],
                "title": data["title"],
                "author": data["author"],
                "category": data["category"],
                "published": data["published"],
                "url": data["url"],
                "excerpt": data.get("body", "")[:MAX_EXCERPT_LEN],
            })
        except (json.JSONDecodeError, KeyError):
            continue

    # Sort by published date descending (newest first)
    index.sort(key=lambda p: p["published"], reverse=True)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    return index


# --- Main ---

def main():
    parser = argparse.ArgumentParser(description="Fetch Sky Forum RSS posts")
    parser.add_argument("--url", default=DEFAULT_URL, help="RSS feed URL")
    parser.add_argument("--quiet", action="store_true", help="Suppress output")
    args = parser.parse_args()

    # Ensure directories exist
    POSTS_DIR.mkdir(parents=True, exist_ok=True)

    existing_ids = load_existing_ids()

    try:
        xml_bytes = fetch_rss(args.url)
    except (urllib.error.URLError, OSError) as e:
        if not args.quiet:
            print(f"Warning: Could not fetch forum RSS: {e}", file=sys.stderr)
        sys.exit(0)  # Non-fatal

    posts = parse_rss(xml_bytes)

    new_count = 0
    for post in posts:
        if post["topic_id"] not in existing_ids:
            save_post(post)
            new_count += 1

    index = rebuild_index()

    if not args.quiet:
        print(f"Forum: {new_count} new post(s), {len(index)} total cached")


if __name__ == "__main__":
    main()
