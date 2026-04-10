#!/usr/bin/env python3
"""Build an address-to-slug lookup map from delegate profile.md files.

Reads EA Address and Delegation Contract from each delegates/{slug}/profile.md,
producing data/voting/address-map.json. This map is the join key between the
voting portal API (which uses addresses) and the delegate tracking system
(which uses slugs).

All address lookups use lowercased keys for case-insensitive matching.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
DELEGATES_DIR = PROJECT_DIR / "delegates"
OUTPUT_DIR = PROJECT_DIR / "data" / "voting"
OUTPUT_FILE = OUTPUT_DIR / "address-map.json"


def extract_address(text: str, label: str) -> str | None:
    """Extract an Ethereum address following a label in markdown."""
    pattern = rf"\*\*{label}:\*\*\s*`(0x[0-9a-fA-F]{{40}})`"
    m = re.search(pattern, text)
    return m.group(1) if m else None


def build_map() -> dict:
    by_address: dict[str, str] = {}
    by_slug: dict[str, dict] = {}

    for profile in sorted(DELEGATES_DIR.glob("*/profile.md")):
        slug = profile.parent.name
        if slug.startswith("_"):
            continue

        content = profile.read_text(encoding="utf-8")
        delegation = extract_address(content, "Delegation Contract")
        ea = extract_address(content, "EA Address")

        if not delegation:
            print(f"Warning: No Delegation Contract found for {slug}", file=sys.stderr)
            continue

        # Extract creation date
        created_match = re.search(r"\*\*Delegate Contract Created:\*\*\s*(\d{4}-\d{2}-\d{2})", content)
        created = created_match.group(1) if created_match else None

        by_address[delegation.lower()] = slug
        by_slug[slug] = {
            "delegation_contract": delegation,
            "ea_address": ea,
            "created": created,
        }

        # Also index the EA address for reverse lookups
        if ea:
            by_address[ea.lower()] = slug

    return {"by_address": by_address, "by_slug": by_slug}


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    address_map = build_map()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(address_map, f, indent=2)

    delegate_count = len(address_map["by_slug"])
    print(f"Address map: {delegate_count} delegates → {OUTPUT_FILE.relative_to(PROJECT_DIR)}")


if __name__ == "__main__":
    main()
