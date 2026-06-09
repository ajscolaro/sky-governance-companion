#!/usr/bin/env python3
"""Build the Atlas UUID link graph from data/index.json → data/link-graph.json.

The atomized Atlas links documents by UUID: a doc body contains
`[A.x.y - Name](<uuid>)` cross-references, which build-index.py already extracts
into each index record's `uuid_refs` field (forward links). This script inverts
those into backlinks and emits a persistent, queryable graph.

Because it derives entirely from the index (no re-parsing of doc bodies), it
must run after build-index.py — atlas-sync.sh runs both at session start. The
output is gitignored and rebuilt each session alongside the index.

Schema (data/link-graph.json):
{
  "generated_from": "data/index.json",
  "node_count": N, "edge_count": M, "dangling_refs": D,
  "nodes": {
    "<uuid>": {
      "number": "A.x.y", "name": "...", "type": "...",
      "links_to":   ["<uuid>", ...],   # docs this doc references
      "linked_from": ["<uuid>", ...]   # docs that reference this doc (backlinks)
    }, ...
  }
}

UUIDs are immutable, so the graph stays valid across renumbering — a node's
identity never changes even when its `number` does.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
INDEX_FILE = PROJECT_DIR / "data" / "index.json"
OUTPUT_FILE = PROJECT_DIR / "data" / "link-graph.json"


def build() -> dict:
    if not INDEX_FILE.exists():
        print(f"Error: index not found at {INDEX_FILE}. Run build-index.py first.",
              file=sys.stderr)
        sys.exit(1)

    index = json.loads(INDEX_FILE.read_text())

    nodes: dict[str, dict] = {}
    for d in index:
        u = d.get("uuid")
        if not u:
            continue
        nodes[u] = {
            "number": d.get("number"),
            "name": d.get("name"),
            "type": d.get("type"),
            "links_to": sorted(set(d.get("uuid_refs", []))),
            "linked_from": [],
        }

    # Invert forward links into backlinks. Refs to UUIDs not in the index
    # (cross-references to deleted/external docs) are counted but can't carry
    # a backlink onto a node that doesn't exist.
    edge_count = 0
    dangling = 0
    backlinks: dict[str, set] = {u: set() for u in nodes}
    for u, node in nodes.items():
        for tgt in node["links_to"]:
            edge_count += 1
            if tgt in backlinks:
                backlinks[tgt].add(u)
            else:
                dangling += 1
    for u in nodes:
        nodes[u]["linked_from"] = sorted(backlinks[u])

    return {
        "generated_from": "data/index.json",
        "node_count": len(nodes),
        "edge_count": edge_count,
        "dangling_refs": dangling,
        "nodes": nodes,
    }


def main() -> int:
    graph = build()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(graph, indent=2))
    print(f"Link graph built: {graph['node_count']} nodes, "
          f"{graph['edge_count']} edges ({graph['dangling_refs']} dangling) "
          f"→ {OUTPUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
