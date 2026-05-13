#!/usr/bin/env python3
"""Find cached AD rationale posts not yet rendered into comms.md.

Each rendered comms.md entry embeds the source forum post URL (the cached
JSON's `.link` field). This script lists cached posts whose `.link` does not
appear in the corresponding delegates/<slug>/comms.md.

Output modes:
  default: human-readable per-delegate summary (skips delegates with zero pending)
  --json:  machine-readable mapping {slug: pending_count}

Invoked by scripts/core/refresh.sh to surface pending AD work in the briefing.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = PROJECT_DIR / "data" / "delegates"
COMMS_DIR = PROJECT_DIR / "delegates"


def count_unprocessed(slug: str) -> int:
    """Return number of cached posts for `slug` whose link is not in comms.md."""
    cache_dir = DATA_DIR / slug
    comms_file = COMMS_DIR / slug / "comms.md"
    if not cache_dir.is_dir():
        return 0
    comms_text = comms_file.read_text(encoding="utf-8") if comms_file.exists() else ""

    pending = 0
    for post_file in cache_dir.glob("*.json"):
        try:
            with open(post_file, "r", encoding="utf-8") as f:
                post = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue
        link = post.get("link", "")
        if not link:
            continue
        if link not in comms_text:
            pending += 1
    return pending


def all_slugs() -> list[str]:
    if not DATA_DIR.is_dir():
        return []
    return sorted(p.name for p in DATA_DIR.iterdir() if p.is_dir())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", help="Only check this delegate slug")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args()

    slugs = [args.slug] if args.slug else all_slugs()
    counts = {slug: count_unprocessed(slug) for slug in slugs}

    if args.json:
        print(json.dumps(counts, indent=2))
        return 0

    pending = {slug: n for slug, n in counts.items() if n > 0}
    if not pending:
        return 0

    total = sum(pending.values())
    print(f"AD rationales awaiting processing ({total} across {len(pending)} delegate(s)):")
    for slug in sorted(pending, key=lambda s: -pending[s]):
        print(f"  {slug}: {pending[slug]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
