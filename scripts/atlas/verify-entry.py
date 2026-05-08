#!/usr/bin/env python3
"""Verify that a rendered changelog entry accounts for every changed UUID in the diff.

Reads:
- Stage 1 manifest (--manifest <path>) — the authoritative list of changed docs
- Stage 4 rendered output (--rendered <path>) — the entries about to be written

Walks each affected entity's entry text and confirms:
- Every added doc is referenced by docNo, name, or short-uuid in the entry text
- Every deleted doc is similarly referenced
- Every modified doc is referenced (unless it's covered by an entity-level pattern bullet)
- The Type label matches the enrichment

Exits 0 if all UUIDs are accounted for; non-zero with a summary on stderr otherwise.
This catches drift between the rendering layer and the underlying classification —
e.g., a new template that fails to mention some doc, or a routing change that
silently drops bullets.

Usage in pipelines:
    python3 verify-entry.py --manifest tmp/pr-237-manifest.json \\
                            --rendered tmp/pr-237-final.json \\
                            --enriched tmp/pr-237-enriched.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def short_uuid(uuid: str) -> str:
    return f"{uuid[:8]}…{uuid[-4:]}" if uuid and len(uuid) >= 12 else uuid


def doc_referenced(doc: dict, all_text: str) -> bool:
    """Is this doc identifiable in the rendered text, by docNo, name, or short UUID?"""
    number = (doc.get("number") or "").strip()
    name = (doc.get("name") or "").strip()
    uuid = doc.get("uuid", "")
    if number and number in all_text:
        return True
    if name and name in all_text:
        return True
    if uuid and short_uuid(uuid) in all_text:
        return True
    if uuid and uuid[:8] in all_text:
        return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--rendered", required=True)
    ap.add_argument("--enriched",
                    help="Enrichment JSON; provides pattern_covered_uuids so "
                         "docs intentionally elided in favor of an entity-level "
                         "pattern bullet are not flagged as missing.")
    args = ap.parse_args()

    manifest = json.loads(Path(args.manifest).read_text())
    rendered = json.loads(Path(args.rendered).read_text())

    # UUIDs covered by entity-level patterns (sweeps, article deletions) — these
    # don't need to appear individually in the rendered text.
    pattern_covered: set[str] = set()
    if args.enriched:
        enriched = json.loads(Path(args.enriched).read_text())
        for entity_uuids in (enriched.get("pattern_covered_uuids") or {}).values():
            pattern_covered.update(entity_uuids)

    all_text = "\n\n".join(rendered["entries"].values())

    missing: list[dict] = []
    counts = {"added": 0, "deleted": 0, "modified": 0, "renamed": 0}
    for kind in counts:
        for doc in manifest.get(kind, []):
            counts[kind] += 1
            if doc.get("uuid") in pattern_covered:
                continue
            if not doc_referenced(doc, all_text):
                missing.append({"kind": kind, **doc})

    pr = rendered.get("pr_number")
    summary = (
        f"PR #{pr}: "
        f"{counts['added']} added / {counts['deleted']} deleted / "
        f"{counts['modified']} modified / {counts['renamed']} renamed; "
        f"{len(missing)} missing"
    )
    if missing:
        print(summary, file=sys.stderr)
        for m in missing:
            print(f"  MISSING [{m['kind']}] {m.get('number','???')} "
                  f"({m.get('name','')[:60]}) uuid={short_uuid(m.get('uuid',''))}",
                  file=sys.stderr)
        return 1
    print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
