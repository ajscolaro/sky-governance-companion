#!/usr/bin/env python3
"""Forum-handle → entity/role lookup helper for the Authorized Forum Accounts registry.

Usable two ways:

1. **As a CLI** (called by search-forum.sh and the session briefing):
   - `--enrich`: read TSV from stdin, append `(entity)` to the author column.
     With `--filter-entity NAME`, drop rows whose author is not registered to
     that entity. With `--registered-only`, drop rows with unregistered authors.
   - `--lookup HANDLE`: print the entity label (or empty if unregistered).
   - `--entity-handles NAME`: print every forum handle (one per line) that
     belongs to the named entity, expanding transitive refs.

2. **As a module** (`from registry_lookup import ...`) — used by the
   roster-reconciliation script.

Degrades gracefully when `data/forum/registry.json` is missing (e.g., before
the first /refresh after PR #227 merged).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable, Optional

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
REGISTRY_FILE = PROJECT_DIR / "data" / "forum" / "registry.json"


def load_registry() -> Optional[dict]:
    if not REGISTRY_FILE.exists():
        return None
    with REGISTRY_FILE.open() as f:
        return json.load(f)


def lookup(handle: str, registry: dict) -> list[dict]:
    """Direct (non-transitive) handle lookup. Case-insensitive."""
    if not registry or not handle:
        return []
    return registry.get("by_handle", {}).get(handle.lower(), [])


def enrichment_label(handle: str, registry: dict) -> str:
    """Compact entity label for inline display. Empty if unregistered.

    Single match: 'Endgame Edge'. Multiple matches (handle is reused as AR
    across entities): 'Soter Labs; Amatsu AR; Ozone AR'.
    """
    matches = lookup(handle, registry)
    if not matches:
        return ""
    parts = []
    seen_entities = set()
    for m in matches:
        e = m["entity"]
        if e in seen_entities:
            continue
        seen_entities.add(e)
        suffix = "" if m["type"] == "entity_handle" else " AR"
        parts.append(f"{e}{suffix}")
    return "; ".join(parts)


def is_registered(handle: str, registry: dict) -> bool:
    return bool(lookup(handle, registry))


def entity_handles(name_or_handle: str, registry: dict) -> set[str]:
    """All lowercase handles belonging to an entity (incl. transitive refs).

    Accepts either the Entity Name ('Endgame Edge') or the Entity Handle
    ('Endgame-Edge'). Walks transitive_refs depth-first with cycle protection.
    """
    if not registry:
        return set()
    target = name_or_handle.lower()
    entities: dict = registry.get("entities", {})

    handle_to_entity = {}
    for ename, info in entities.items():
        eh = info.get("entity_handle")
        if eh:
            handle_to_entity[eh.lower()] = ename

    matched_entities = []
    for ename, info in entities.items():
        if ename.lower() == target:
            matched_entities.append(ename)
        elif handle_to_entity.get(target) == ename:
            matched_entities.append(ename)

    handles: set[str] = set()
    visited: set[str] = set()

    def expand(ename: str, depth: int = 0) -> None:
        if ename in visited or depth > 5:
            return
        visited.add(ename)
        info = entities.get(ename)
        if not info:
            return
        if info.get("entity_handle"):
            handles.add(info["entity_handle"].lower())
        for ar in info.get("authorized_representatives") or []:
            handles.add(ar.lower())
        for tref in info.get("transitive_refs") or []:
            ref_entity = handle_to_entity.get(tref.lower())
            if ref_entity:
                expand(ref_entity, depth + 1)

    for ename in matched_entities:
        expand(ename)
    return handles


def cli_enrich(stdin: Iterable[str], registry: Optional[dict], filter_entity: Optional[str],
               registered_only: bool, author_col: int) -> int:
    target_handles: Optional[set[str]] = None
    if filter_entity:
        if registry is None:
            print("forum-registry: --filter-entity requires data/forum/registry.json (run /refresh)",
                  file=sys.stderr)
            return 2
        target_handles = entity_handles(filter_entity, registry)
        if not target_handles:
            print(f"forum-registry: no handles found for entity '{filter_entity}'", file=sys.stderr)
            return 1

    if registered_only and registry is None:
        print("forum-registry: --registered-only requires data/forum/registry.json (run /refresh)",
              file=sys.stderr)
        return 2

    for raw in stdin:
        line = raw.rstrip("\n")
        if not line:
            continue
        cols = line.split("\t")
        if author_col >= len(cols):
            print(line)
            continue
        author = cols[author_col]
        author_key = author.lower()

        if target_handles is not None and author_key not in target_handles:
            continue

        if registry is not None:
            label = enrichment_label(author, registry)
            if label:
                cols[author_col] = f"{author} ({label})"
            elif registered_only:
                continue
        # registry missing + no flags → pass-through

        print("\t".join(cols))
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--enrich", action="store_true",
                      help="Read TSV from stdin, append (entity) to the author column.")
    mode.add_argument("--lookup", metavar="HANDLE",
                      help="Print enrichment label for HANDLE (empty if unregistered).")
    mode.add_argument("--entity-handles", metavar="ENTITY",
                      help="Print every handle belonging to ENTITY, one per line.")

    p.add_argument("--filter-entity", metavar="ENTITY",
                   help="With --enrich: drop rows whose author is not registered to ENTITY.")
    p.add_argument("--registered-only", action="store_true",
                   help="With --enrich: drop rows with unregistered authors.")
    p.add_argument("--author-col", type=int, default=2,
                   help="0-indexed author column for --enrich (default 2).")
    args = p.parse_args()

    registry = load_registry()

    if args.lookup is not None:
        if registry is None:
            print("", end="")
            return 0
        print(enrichment_label(args.lookup, registry))
        return 0

    if args.entity_handles is not None:
        if registry is None:
            print("forum-registry: registry.json missing — run /refresh", file=sys.stderr)
            return 1
        for h in sorted(entity_handles(args.entity_handles, registry)):
            print(h)
        return 0

    if args.enrich:
        if registry is None and not (args.filter_entity or args.registered_only):
            print("forum-registry: registry.json missing — run /refresh (passing through)",
                  file=sys.stderr)
        return cli_enrich(
            sys.stdin,
            registry,
            args.filter_entity,
            args.registered_only,
            args.author_col,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
