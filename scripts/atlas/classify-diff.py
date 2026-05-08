#!/usr/bin/env python3
"""Classify documents touched by a PR diff against the atomized Atlas.

Reads a unified diff from stdin (or argv[1]) and the current index from
data/index.json, emitting JSON to stdout describing which document.md files
were added/deleted/modified/renamed and what UUIDs they correspond to.

Output schema:
    {
      "added":    [{"uuid", "path"}, ...],
      "deleted":  [{"uuid", "path"}, ...],
      "modified": [{"uuid", "path"}, ...],
      "renamed":  [{"uuid", "from", "to"}, ...],
      "name_changed": [{"uuid", "old", "new"}, ...]
    }
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
INDEX_FILE = PROJECT_DIR / "data" / "index.json"

# Strip leading a/ b/ prefixes that show up in diff headers
def _strip(p: str) -> str:
    return p[2:] if p.startswith(("a/", "b/")) else p


def split_blocks(diff: str) -> list[str]:
    """Split unified diff into per-file blocks (without leading 'diff --git ')."""
    parts = re.split(r'(?m)^diff --git ', diff)
    return [p for p in parts[1:] if p]


def classify_block(block: str, by_path: dict) -> dict | None:
    """Return one classification entry for a document.md block, or None to skip."""
    # First line: "a/<path> b/<path>"
    first_line, _, rest = block.partition("\n")
    m = re.match(r"(\S+)\s+(\S+)", first_line)
    if not m:
        return None
    a_path = _strip(m.group(1))
    b_path = _strip(m.group(2))

    # Filter to document.md files under content/
    if not (a_path.endswith("/document.md") or b_path.endswith("/document.md")):
        return None
    if not (a_path.startswith("content/") or b_path.startswith("content/")):
        return None

    head_lines = rest.split("\n", 10)[:10]
    is_new = any(l.startswith("new file mode") for l in head_lines)
    is_deleted = any(l.startswith("deleted file mode") for l in head_lines)
    rename_from = next((l for l in head_lines if l.startswith("rename from ")), None)
    rename_to = next((l for l in head_lines if l.startswith("rename to ")), None)
    is_rename = rename_from is not None and rename_to is not None

    # Extract id: from frontmatter +/- lines (only present if id changes,
    # which happens only on add/delete; for modifies/renames id is on a
    # context line and we resolve via the index path lookup).
    id_added = re.search(r"^\+id:\s*([0-9a-f-]{36})", rest, re.M)
    id_removed = re.search(r"^-id:\s*([0-9a-f-]{36})", rest, re.M)

    uuid: str | None = None
    if id_added:
        uuid = id_added.group(1)
    elif id_removed:
        uuid = id_removed.group(1)
    else:
        # Use the path-based lookup: prefer the new path (b_path) for surviving docs.
        path_key = ".atlas-repo/" + (b_path if b_path != "/dev/null" else a_path)
        entry = by_path.get(path_key)
        if entry:
            uuid = entry["uuid"]

    if not uuid:
        return None

    if is_new:
        kind = "added"
    elif is_deleted:
        kind = "deleted"
    elif is_rename:
        kind = "renamed"
    else:
        kind = "modified"

    # Capture frontmatter fields for deleted/added docs so callers can label
    # them without relying on the current index (which lacks deleted docs).
    def _fm(field: str, prefix: str) -> str | None:
        m = re.search(rf"^{re.escape(prefix)}{field}:\s*(.+)$", rest, re.M)
        return m.group(1).strip().strip('"') if m else None

    if kind == "deleted":
        number = _fm("docNo", "-")
        name = _fm("name", "-")
        doc_type = _fm("type", "-")
    elif kind == "added":
        number = _fm("docNo", "+")
        name = _fm("name", "+")
        doc_type = _fm("type", "+")
    else:
        # Modified or renamed: pull from current index if available
        path_key = ".atlas-repo/" + (b_path if b_path != "/dev/null" else a_path)
        entry = by_path.get(path_key)
        if entry:
            number, name, doc_type = entry["number"], entry["name"], entry["type"]
        else:
            number = name = doc_type = None

    out: dict = {"kind": kind, "uuid": uuid}
    if number:
        out["number"] = number
    if name:
        out["name"] = name
    if doc_type:
        out["type"] = doc_type
    if kind == "renamed":
        out["from"] = a_path
        out["to"] = b_path
    else:
        out["path"] = b_path if kind != "deleted" else a_path

    # Name-change detection (UUID stable, name field differs)
    name_added = re.search(r"^\+name:\s*(.+)$", rest, re.M)
    name_removed = re.search(r"^-name:\s*(.+)$", rest, re.M)
    if (
        kind != "added"
        and kind != "deleted"
        and name_added
        and name_removed
        and name_added.group(1).strip() != name_removed.group(1).strip()
    ):
        out["name_change"] = {
            "old": name_removed.group(1).strip().strip('"'),
            "new": name_added.group(1).strip().strip('"'),
        }
    return out


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] not in ("-", "--stdin"):
        diff = Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace")
    else:
        diff = sys.stdin.read()

    by_path: dict = {}
    if INDEX_FILE.exists():
        index = json.loads(INDEX_FILE.read_text())
        by_path = {d["path"]: d for d in index}

    manifest: dict = {
        "added": [],
        "deleted": [],
        "modified": [],
        "renamed": [],
        "name_changed": [],
    }

    for block in split_blocks(diff):
        entry = classify_block(block, by_path)
        if not entry:
            continue
        kind = entry.pop("kind")
        if "name_change" in entry:
            nc = entry.pop("name_change")
            manifest["name_changed"].append({"uuid": entry["uuid"], **nc})
        manifest[kind].append(entry)

    json.dump(manifest, sys.stdout, indent=2)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
