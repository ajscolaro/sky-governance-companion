#!/usr/bin/env python3
"""Parse the atomized Atlas (.atlas-repo/content/) into data/index.json.

Walks every document.md file, parses YAML frontmatter, and writes a JSON
index keyed for fast lookup by UUID or doc number. Replaces the prior
monolith parser; output schema swaps line_start/line_end for path.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
CONTENT_DIR = PROJECT_DIR / ".atlas-repo" / "content"
OUTPUT_FILE = PROJECT_DIR / "data" / "index.json"

# Frontmatter keys we care about
FRONTMATTER_KEYS = {"id", "docNo", "name", "type", "depth", "childType", "targets"}

# Body-level extractors (run once per doc at index build time so downstream
# scripts don't re-parse 10K files per query). Patterns mirror what
# scripts/atlas/extract-values.py uses, kept centralized here.
ADDRESS_RE = re.compile(r"\b0x[a-fA-F0-9]{40}\b")
UUID_RE = re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b")
DATE_RE = re.compile(
    r"\b(?:(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4}"
    r"|\d{4}-\d{2}-\d{2})\b"
)

# Body that begins with one of these phrases is a scaffold/index doc — useful
# context but no substantive content of its own. The renderer can skip these.
SCAFFOLD_PREFIXES = (
    "the subdocuments herein",
    "the documents herein",
    "the subdocuments",
)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split a document.md into (frontmatter dict, body).

    Frontmatter format (per .atlas-repo/sync/decompose.py):
        ---
        id: <uuid>
        docNo: <number>
        name: <string-or-quoted-string>
        type: <type>
        depth: <int>
        childType: <string>
        targets: [<uuid>, <uuid>, ...]   # NR docs only
        ---
    """
    if not text.startswith("---\n"):
        raise ValueError("Missing frontmatter opener")
    end = text.index("\n---\n", 4)
    block = text[4:end]
    body = text[end + 5:]

    fm: dict = {}
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z]+):\s*(.*)$", line)
        if not m:
            continue
        key, raw = m.group(1), m.group(2).strip()
        if key not in FRONTMATTER_KEYS:
            continue
        if key == "targets":
            inner = raw.strip("[]").strip()
            fm[key] = [u.strip() for u in inner.split(",") if u.strip()] if inner else []
        elif key == "depth":
            fm[key] = int(raw)
        elif key == "name" and raw.startswith('"') and raw.endswith('"'):
            fm[key] = raw[1:-1].replace('\\"', '"').replace("\\\\", "\\")
        else:
            fm[key] = raw
    return fm, body


def heading_level(body: str) -> int:
    """Count leading # on the first non-blank body line."""
    for line in body.splitlines():
        if line.strip():
            return len(line) - len(line.lstrip("#"))
    return 0


def body_after_heading(body: str) -> str:
    """Strip the leading `###### A.x.y - Name [Type]` heading; return the rest."""
    lines = body.splitlines()
    skipped_heading = False
    out: list[str] = []
    for line in lines:
        if not skipped_heading:
            if line.strip().startswith("#"):
                skipped_heading = True
                continue
            if not line.strip():
                continue
            # Some docs have no leading heading — keep everything
            skipped_heading = True
        out.append(line)
    return "\n".join(out).strip()


def lead_sentence(content: str, cap: int = 240) -> str:
    """First sentence of body content (post-heading), trimmed to cap chars.

    Mirrors the heuristic in extract-values.py so the index can serve as the
    cached source of truth instead of re-parsing per PR.
    """
    for line in content.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        m = re.search(r"^(.{20,%d}?[.!?])(?:\s|$)" % cap, s)
        if m:
            return m.group(1)
        return s[:cap]
    return ""


def is_scaffold_lead(lead: str) -> bool:
    return lead.lower().lstrip().startswith(SCAFFOLD_PREFIXES)


def num_key(num: str) -> tuple:
    """Sort key for doc numbers: A.x.y.z chronological, NR-N after."""
    if num.startswith("NR-"):
        return (1, (int(num[3:]),))
    key = []
    for p in num.split("."):
        if p == "A":
            continue
        if p.startswith("var"):
            key.append((1, int(p[3:])))
        else:
            key.append((0, int(p)))
    return (0, tuple(key))


def find_supporting_root(segments: list, marker1: str, marker2: str) -> int:
    for i in range(1, len(segments) - 1):
        if segments[i] == marker1 and i + 1 < len(segments) and segments[i + 1] == marker2:
            return i
    raise ValueError(f"Supporting root {marker1}.{marker2} not found in {'.'.join(segments)}")


def find_parent_number(number: str, doc_type: str) -> str | None:
    if number.startswith("NR-"):
        return None
    if doc_type == "Scope":
        return None

    segments = number.split(".")

    if doc_type in ("Annotation", "Action Tenet"):
        marker = "3" if doc_type == "Annotation" else "4"
        try:
            idx = find_supporting_root(segments, "0", marker)
            return ".".join(segments[:idx])
        except ValueError:
            pass
    elif doc_type == "Scenario":
        try:
            idx = find_supporting_root(segments, "0", "4")
            return ".".join(segments[:idx + 3])
        except ValueError:
            pass
    elif doc_type == "Scenario Variation":
        return ".".join(segments[:-1])
    elif doc_type == "Active Data":
        try:
            idx = find_supporting_root(segments, "0", "6")
            return ".".join(segments[:idx])
        except ValueError:
            pass

    if len(segments) > 2:
        return ".".join(segments[:-1])
    return None


def build_ancestors(number: str) -> list[str]:
    if number.startswith("NR-"):
        return []
    segments = number.split(".")
    return [".".join(segments[:i]) for i in range(2, len(segments))]


def main():
    if not CONTENT_DIR.is_dir():
        print(f"Error: Content directory not found at {CONTENT_DIR}", file=sys.stderr)
        print("Run scripts/core/setup.sh first to clone the Atlas repo.", file=sys.stderr)
        sys.exit(1)

    docs = []
    for doc_path in CONTENT_DIR.rglob("document.md"):
        text = doc_path.read_text(encoding="utf-8")
        try:
            fm, body = parse_frontmatter(text)
        except ValueError as e:
            print(f"Warning: skipping {doc_path}: {e}", file=sys.stderr)
            continue
        for required in ("id", "docNo", "name", "type", "depth"):
            if required not in fm:
                print(f"Warning: {doc_path} missing '{required}' in frontmatter", file=sys.stderr)
                break
        else:
            content = body_after_heading(body)
            lead = lead_sentence(content)
            # Extract structured facts once at index build time
            addresses = sorted(set(ADDRESS_RE.findall(content)))
            # Filter out the doc's own UUID from cross-references
            uuid_refs = sorted(set(UUID_RE.findall(content)) - {fm["id"]})
            dates = sorted(set(DATE_RE.findall(content)))
            entry: dict = {
                "uuid": fm["id"],
                "number": fm["docNo"],
                "name": fm["name"],
                "type": fm["type"],
                "depth": fm["depth"],
                "heading_level": heading_level(body),
                "path": str(doc_path.relative_to(PROJECT_DIR)),
                "body_length": len(content),
                "body_hash": hashlib.sha256(content.encode("utf-8")).hexdigest()[:16],
                "lead_sentence": lead,
                "is_scaffold": is_scaffold_lead(lead),
                "is_active_data": fm["type"] == "Active Data",
            }
            if addresses:
                entry["addresses"] = addresses
            if uuid_refs:
                entry["uuid_refs"] = uuid_refs
            if dates:
                entry["dates"] = dates
            if "targets" in fm:
                entry["targets"] = fm["targets"]
            docs.append(entry)

    docs.sort(key=lambda d: num_key(d["number"]))

    number_to_uuid = {d["number"]: d["uuid"] for d in docs}
    for doc in docs:
        parent_num = find_parent_number(doc["number"], doc["type"])
        doc["parent_uuid"] = number_to_uuid.get(parent_num) if parent_num else None
        doc["ancestors"] = build_ancestors(doc["number"])

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(docs, f, indent=2)

    print(f"Index built: {len(docs)} documents → {OUTPUT_FILE}")
    type_counts: dict = {}
    for d in docs:
        type_counts[d["type"]] = type_counts.get(d["type"], 0) + 1
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")


if __name__ == "__main__":
    main()
