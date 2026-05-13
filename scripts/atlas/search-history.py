#!/usr/bin/env python3
"""Search committed history/ changelogs.

Each per-entity changelog.md contains zero-or-more entries of the form:
  ## PR #N — Title
  **Merged:** YYYY-MM-DD | **Type:** governance-path
  ...body (Material Changes / Housekeeping / Context sections)...

This tool finds entries matching combinations of keyword, entity slug,
governance type, merged-date range, and exact PR number. Default output is
one line per match (most-recent-first); use --show for full entry bodies.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HISTORY = Path(__file__).resolve().parents[2] / "history"

ENTRY_HEADER = re.compile(r"^## PR #(\d+)\s+—\s+(.+?)\s*$")
META_DATE = re.compile(r"\*\*Merged:\*\*\s+(\d{4}-\d{2}-\d{2})")
META_TYPE = re.compile(r"\*\*Type:\*\*\s+([^|]+?)(?:\s*\||\s*$)")


def parse_meta(line: str):
    """Pull merged date and (just) the Type label out of a meta line.

    Trailing pipe segments (e.g. ``**+2119/-158 lines**``) are ignored so the
    type field stays canonical and ``--type`` filters match cleanly.
    """
    if "**Merged:**" not in line:
        return None, None
    dm = META_DATE.search(line)
    tm = META_TYPE.search(line)
    return (dm.group(1) if dm else None,
            tm.group(1).strip() if tm else None)


def parse_entries(path: Path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    rel = path.parent.relative_to(HISTORY)
    entity = "." if str(rel) == "." else str(rel)

    i = 0
    while i < len(lines):
        m = ENTRY_HEADER.match(lines[i])
        if not m:
            i += 1
            continue
        pr = int(m.group(1))
        title = m.group(2).strip()
        merged = None
        type_ = None
        body_start = i + 1
        for j in range(i + 1, min(i + 5, len(lines))):
            d, t = parse_meta(lines[j])
            if d or t:
                merged = d
                type_ = t
                body_start = j + 1
                break
        k = body_start
        while k < len(lines) and not ENTRY_HEADER.match(lines[k]):
            k += 1
        body = "\n".join(lines[body_start:k]).strip()
        yield {
            "pr": pr,
            "title": title,
            "merged": merged,
            "type": type_,
            "body": body,
            "entity": entity,
            "file": str(path.relative_to(HISTORY.parent)),
        }
        i = k


def iter_changelogs(entity_filter: str | None):
    for path in sorted(HISTORY.rglob("changelog.md")):
        rel = path.parent.relative_to(HISTORY)
        rel_str = "." if str(rel) == "." else str(rel)
        if entity_filter and entity_filter.lower() not in rel_str.lower():
            continue
        yield path


def first_match_line(body: str, kw: str | None) -> str:
    """Pick a representative one-liner. Skip blanks and `###` section headers."""
    lines = [l for l in body.splitlines() if l.strip() and not l.lstrip().startswith("###")]
    if not lines:
        return ""
    if not kw:
        return lines[0].lstrip(" -*").rstrip()
    pat = re.compile(re.escape(kw), re.IGNORECASE)
    for line in lines:
        if pat.search(line):
            return line.lstrip(" -*").rstrip()
    return lines[0].lstrip(" -*").rstrip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("keyword", nargs="?", help="Case-insensitive keyword (title or body)")
    ap.add_argument("--entity", help="Filter by substring of path under history/")
    ap.add_argument("--type", dest="type_filter", help="Filter by **Type:** substring")
    ap.add_argument("--since", help="Earliest merged date (YYYY-MM-DD)")
    ap.add_argument("--until", help="Latest merged date (YYYY-MM-DD)")
    ap.add_argument("--pr", type=int, help="Exact PR number")
    ap.add_argument("--show", action="store_true", help="Print full entry bodies")
    ap.add_argument("--list-entities", action="store_true",
                    help="List all changelog dirs with entry counts")
    ap.add_argument("--limit", type=int, default=50, help="Max matches (default 50)")
    args = ap.parse_args()

    if args.list_entities:
        for path in sorted(HISTORY.rglob("changelog.md")):
            rel = path.parent.relative_to(HISTORY)
            count = sum(1 for _ in parse_entries(path))
            print(f"{rel}\t{count} entries")
        return 0

    kw_pat = re.compile(re.escape(args.keyword), re.IGNORECASE) if args.keyword else None

    matches = []
    for path in iter_changelogs(args.entity):
        for entry in parse_entries(path):
            if args.pr is not None and entry["pr"] != args.pr:
                continue
            if kw_pat and not (kw_pat.search(entry["title"]) or kw_pat.search(entry["body"])):
                continue
            if args.type_filter and (entry["type"] is None or
                                     args.type_filter.lower() not in entry["type"].lower()):
                continue
            if entry["merged"] is not None:
                if args.since and entry["merged"] < args.since:
                    continue
                if args.until and entry["merged"] > args.until:
                    continue
            elif args.since or args.until:
                continue
            matches.append(entry)

    matches.sort(key=lambda e: (e["merged"] or "", e["pr"]), reverse=True)
    matches = matches[: args.limit]

    if not matches:
        print("No matches.", file=sys.stderr)
        return 1

    for e in matches:
        if args.show:
            print(f"## PR #{e['pr']} — {e['title']}")
            print(f"**Merged:** {e['merged']} | **Type:** {e['type']}")
            print(f"**Entity:** {e['entity']}  ({e['file']})")
            print()
            print(e["body"])
            print()
            print("---")
            print()
        else:
            snippet = first_match_line(e["body"], args.keyword)
            if len(snippet) > 160:
                snippet = snippet[:157] + "..."
            print(f"PR #{e['pr']} | {e['merged']} | {e['entity']} | {e['type']}")
            if snippet:
                print(f"  → {snippet}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
