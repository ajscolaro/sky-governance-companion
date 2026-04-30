#!/usr/bin/env python3
"""Reconcile delegates/_roster.md against the Authorized Forum Accounts registry.

One-shot diagnostic. Prints a markdown report listing:

1. **ADs missing from the registry** — Aligned Delegates whose forum handle
   doesn't appear anywhere in the registry. Either the AD hasn't registered
   under any entity yet, or our roster's forum handle is stale.
2. **Registry handles that match AD slugs but aren't on the roster** — handles
   in the registry that look like AD handles but the AD isn't on `_roster.md`.
3. **Multi-entity handles** — handles registered under more than one entity
   (informational; allowed per A.2.7.1.1.1.1.1).

Run after `/refresh` so both `data/forum/registry.json` and
`data/delegates/<slug>/` reflect the current Atlas + forum state.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
ROSTER_FILE = PROJECT_DIR / "delegates" / "_roster.md"
DELEGATE_CACHE = PROJECT_DIR / "data" / "delegates"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from registry_lookup import load_registry  # noqa: E402

ROSTER_ROW_RE = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$"
)


def parse_roster() -> list[dict]:
    """Parse delegates/_roster.md into list of {name, slug, status} rows."""
    rows = []
    if not ROSTER_FILE.exists():
        return rows
    for line in ROSTER_FILE.read_text().splitlines():
        m = ROSTER_ROW_RE.match(line)
        if not m:
            continue
        name, slug, _thread, status = m.groups()
        # Skip header / separator
        if slug.lower() == "slug" or set(slug.replace("-", "")) <= {""}:
            continue
        if not slug or slug.startswith(":"):
            continue
        rows.append({"name": name, "slug": slug, "status": status})
    return rows


def derive_forum_handle(slug: str) -> str | None:
    """Read the most recent cached rationale to find this AD's forum handle.

    Falls back to the slug if no cache entry exists (rare — every active AD
    should have at least one fetched rationale).
    """
    cache_dir = DELEGATE_CACHE / slug
    if not cache_dir.is_dir():
        return None
    entries = sorted(cache_dir.glob("*.json"))
    if not entries:
        return None
    try:
        with entries[-1].open() as f:
            data = json.load(f)
        return data.get("author") or None
    except (OSError, json.JSONDecodeError):
        return None


def main() -> int:
    registry = load_registry()
    if registry is None:
        print(
            "check-roster-vs-registry: data/forum/registry.json missing — run /refresh first",
            file=sys.stderr,
        )
        return 1

    by_handle: dict = registry.get("by_handle", {})
    roster = parse_roster()

    # 1. ADs missing from the registry
    missing: list[dict] = []
    found: list[dict] = []
    for ad in roster:
        if ad["status"].strip().lower() != "active":
            continue
        handle = derive_forum_handle(ad["slug"])
        ad_with_handle = {**ad, "handle": handle}
        if handle and handle.lower() in by_handle:
            found.append(ad_with_handle)
        else:
            missing.append(ad_with_handle)

    # 2. Registry handles that match AD slugs but aren't on the roster
    roster_slugs = {ad["slug"].lower() for ad in roster}
    roster_handles = {(ad["handle"] or "").lower() for ad in found + missing if ad.get("handle")}
    registry_lookalikes: list[tuple[str, list[dict]]] = []
    for handle, refs in by_handle.items():
        if handle in roster_slugs and handle not in roster_handles:
            registry_lookalikes.append((handle, refs))
        elif any(handle == slug.replace("-", "") for slug in roster_slugs) and handle not in roster_handles:
            registry_lookalikes.append((handle, refs))

    # 3. Multi-entity handles
    multi_entity = [(h, refs) for h, refs in by_handle.items() if len({r["entity"] for r in refs}) > 1]

    # --- Report ---
    print("# Roster ↔ Registry Reconciliation")
    print()
    print(f"Roster: {len([a for a in roster if a['status'].strip().lower() == 'active'])} active ADs")
    print(f"Registry: {len(registry.get('entities', {}))} entities, {len(by_handle)} unique handles")
    print()

    print("## ADs missing from registry")
    print()
    if not missing:
        print("_All active ADs are registered._")
    else:
        print("| AD | Slug | Forum Handle | Note |")
        print("|----|------|--------------|------|")
        for ad in missing:
            handle = ad.get("handle") or "_(no cached posts)_"
            note = "handle not in registry" if ad.get("handle") else "no forum handle resolved"
            print(f"| {ad['name']} | `{ad['slug']}` | `{handle}` | {note} |")
    print()

    print("## ADs already in registry")
    print()
    if not found:
        print("_None._")
    else:
        print("| AD | Forum Handle | Registered as |")
        print("|----|--------------|---------------|")
        for ad in found:
            refs = by_handle[ad["handle"].lower()]
            label = "; ".join(
                f"{r['entity']} ({'EH' if r['type'] == 'entity_handle' else 'AR'})" for r in refs
            )
            print(f"| {ad['name']} | `{ad['handle']}` | {label} |")
    print()

    print("## Registry handles that look like AD slugs but aren't on the roster")
    print()
    if not registry_lookalikes:
        print("_No matches._")
    else:
        for handle, refs in sorted(registry_lookalikes):
            label = "; ".join(f"{r['entity']} ({r['type']})" for r in refs)
            print(f"- `{handle}` — {label}")
    print()

    print("## Multi-entity handles (informational)")
    print()
    if not multi_entity:
        print("_None._")
    else:
        for handle, refs in sorted(multi_entity):
            label = "; ".join(
                f"{r['entity']} ({'EH' if r['type'] == 'entity_handle' else 'AR'})" for r in refs
            )
            print(f"- `{handle}` → {label}")
    print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
