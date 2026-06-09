#!/usr/bin/env python3
"""Query the Atlas UUID link graph (data/link-graph.json).

Two modes:

  links.py <uuid-or-number>
      Show what a doc references (forward links) and what references it
      (backlinks), each resolved to current number + name. Use this to follow
      cross-references in one hop instead of grepping doc bodies.

  links.py --impact <uuid-or-number> [<uuid-or-number> ...]
      Given a set of changed docs, list the EXTERNAL dependents — docs outside
      the changed set that link to any changed doc and may now be stale. Feeds
      impact analysis for /atlas-analyze and changelog Context.

Run build-link-graph.py first (atlas-sync.sh does this at session start).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
GRAPH_FILE = PROJECT_DIR / "data" / "link-graph.json"
INDEX_FILE = PROJECT_DIR / "data" / "index.json"


def load_graph() -> dict:
    if not GRAPH_FILE.exists():
        print(f"Error: link graph not found at {GRAPH_FILE}. "
              f"Run scripts/atlas/build-link-graph.py first.", file=sys.stderr)
        sys.exit(1)
    return json.loads(GRAPH_FILE.read_text())


def resolve_to_uuid(token: str, graph: dict) -> str | None:
    """Map a UUID (full/prefix) or an Atlas number to a node UUID."""
    t = token.lower()
    nodes = graph["nodes"]
    if t in nodes:
        return t
    # UUID prefix
    for u in nodes:
        if u.startswith(t):
            return u
    # Atlas number
    for u, n in nodes.items():
        if (n.get("number") or "").lower() == t:
            return u
    return None


def label(uuid: str, graph: dict) -> str:
    n = graph["nodes"].get(uuid)
    if not n:
        return f"{uuid} (not in index)"
    return f"`{n['number']}` [{n['type']}] {n['name']}"


def show_node(token: str, graph: dict) -> int:
    uuid = resolve_to_uuid(token, graph)
    if not uuid:
        print(f"'{token}' not found in link graph.", file=sys.stderr)
        return 1
    node = graph["nodes"][uuid]
    print(f"{label(uuid, graph)}  (UUID {uuid})")
    print(f"\n  Links to ({len(node['links_to'])}):")
    for t in node["links_to"]:
        print(f"    → {label(t, graph)}")
    if not node["links_to"]:
        print("    (none)")
    print(f"\n  Linked from / backlinks ({len(node['linked_from'])}):")
    for s in node["linked_from"]:
        print(f"    ← {label(s, graph)}")
    if not node["linked_from"]:
        print("    (none)")
    return 0


def show_impact(tokens: list[str], graph: dict) -> int:
    changed: set[str] = set()
    for t in tokens:
        u = resolve_to_uuid(t, graph)
        if u:
            changed.add(u)
        else:
            print(f"Warning: '{t}' not found in link graph — skipped.", file=sys.stderr)
    if not changed:
        print("No resolvable changed docs.", file=sys.stderr)
        return 1

    # External dependents: docs outside the changed set that link to a changed doc.
    dependents: dict[str, set] = {}
    for c in changed:
        for src in graph["nodes"].get(c, {}).get("linked_from", []):
            if src in changed:
                continue
            dependents.setdefault(src, set()).add(c)

    print(f"Changed docs: {len(changed)}; external dependents: {len(dependents)}")
    for src in sorted(dependents, key=lambda u: graph["nodes"][u].get("number") or ""):
        targets = ", ".join(sorted(graph["nodes"][t].get("number") or t
                                   for t in dependents[src]))
        print(f"  {label(src, graph)}\n      → references: {targets}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("ids", nargs="+", help="UUID(s) (full/prefix) or Atlas number(s)")
    ap.add_argument("--impact", action="store_true",
                    help="Treat IDs as a changed set; list external dependents")
    args = ap.parse_args()

    graph = load_graph()
    if args.impact:
        return show_impact(args.ids, graph)
    if len(args.ids) != 1:
        print("Single-node mode takes one ID; use --impact for a set.", file=sys.stderr)
        return 2
    return show_node(args.ids[0], graph)


if __name__ == "__main__":
    raise SystemExit(main())
