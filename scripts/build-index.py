#!/usr/bin/env python3
"""Parse Sky Atlas.md into a structured index (data/index.json).

Reads every title line from the Atlas file, extracts document metadata
(number, name, type, UUID, line offsets), computes semantic depth and
parent relationships, and writes a JSON index for fast lookup.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

ATLAS_FILE = Path(__file__).resolve().parent.parent / ".atlas-repo" / "Sky Atlas" / "Sky Atlas.md"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "data" / "index.json"

# Matches title lines like:
#   #### A.0.1.1.3 - Aligned Structure [Core]  <!-- UUID: fad68392-... -->
#   #### NR-1 - Systematic Basis ... [Needed Research]  <!-- UUID: 2da58ba2-... -->
TITLE_RE = re.compile(
    r'^(#{1,6})\s+'           # heading level
    r'((?:A\.\S+|NR-\d+))'   # document number (A.x.y.z or NR-N)
    r'\s+-\s+'                # separator
    r'(.+?)'                  # document name
    r'\s+\[([^\]]+)\]'        # [Type]
    r'\s+<!--\s*UUID:\s*'     # UUID comment start
    r'([a-f0-9-]+)'           # UUID
    r'\s*-->'                 # UUID comment end
)

# Document types and their categories
REGULAR_TYPES = {"Scope", "Article", "Section", "Core", "Type Specification", "Active Data Controller"}
SUPPORTING_TYPES = {"Annotation", "Action Tenet", "Scenario", "Scenario Variation", "Active Data", "Needed Research"}


def compute_semantic_depth(number: str, doc_type: str) -> int:
    """Compute semantic depth from document number and type.

    Rules from ATLAS_MARKDOWN_SYNTAX.md:
    - Regular docs: count segments - 1 (the A prefix doesn't count)
    - Annotations (.0.3.X): target doc depth + 1
    - Action Tenets (.0.4.X): target doc depth + 1
    - Scenarios (.1.X after tenet): parent tenet depth + 1
    - Scenario Variations (.varX): parent scenario depth + 1
    - Active Data (.0.6.X): controller doc depth + 1
    - Needed Research (NR-X): depth 1 (standalone)
    """
    if number.startswith("NR-"):
        return 1

    segments = number.split(".")

    if doc_type == "Annotation":
        # Pattern: A.x.y.z.0.3.N — target is A.x.y.z
        try:
            idx = _find_supporting_root(segments, "0", "3")
            target_depth = idx - 1  # segments before .0.3 minus the A prefix
            return target_depth + 1
        except ValueError:
            pass

    elif doc_type == "Action Tenet":
        # Pattern: A.x.y.z.0.4.N — target is A.x.y.z
        try:
            idx = _find_supporting_root(segments, "0", "4")
            target_depth = idx - 1
            return target_depth + 1
        except ValueError:
            pass

    elif doc_type == "Scenario":
        # Pattern: A.x.y.z.0.4.N.1.M — parent tenet is A.x.y.z.0.4.N
        # Tenet depth = target depth + 1, scenario depth = tenet depth + 1
        try:
            idx = _find_supporting_root(segments, "0", "4")
            target_depth = idx - 1
            return target_depth + 2  # tenet + 1, then scenario + 1
        except ValueError:
            pass

    elif doc_type == "Scenario Variation":
        # Pattern: A.x.y.z.0.4.N.1.M.varV
        # Scenario depth + 1
        try:
            idx = _find_supporting_root(segments, "0", "4")
            target_depth = idx - 1
            return target_depth + 3  # tenet +1, scenario +1, variation +1
        except ValueError:
            pass

    elif doc_type == "Active Data":
        # Pattern: A.x.y.z.0.6.N — controller is A.x.y.z
        try:
            idx = _find_supporting_root(segments, "0", "6")
            controller_depth = idx - 1
            return controller_depth + 1
        except ValueError:
            pass

    # Regular documents: segments - 1
    return len(segments) - 1


def _find_supporting_root(segments: list, marker1: str, marker2: str) -> int:
    """Find the index of the supporting root marker (e.g., .0.3 or .0.4 or .0.6).

    Returns the index of marker1 in the segments list.
    """
    for i in range(1, len(segments) - 1):
        if segments[i] == marker1 and i + 1 < len(segments) and segments[i + 1] == marker2:
            return i
    raise ValueError(f"Supporting root {marker1}.{marker2} not found in {'.'.join(segments)}")


def find_parent_number(number: str, doc_type: str, segments: list) -> str | None:
    """Determine the parent document number."""
    if number.startswith("NR-"):
        return None  # Needed Research docs are standalone

    if doc_type == "Scope":
        return None  # Top-level scopes have no parent

    if doc_type in ("Annotation", "Action Tenet"):
        # Parent is the target document (before .0.3 or .0.4)
        marker = "3" if doc_type == "Annotation" else "4"
        try:
            idx = _find_supporting_root(segments, "0", marker)
            return ".".join(segments[:idx])
        except ValueError:
            pass

    elif doc_type == "Scenario":
        # Parent is the action tenet: everything before .1.N
        # Find the .0.4 root, then parent is up to .0.4.N
        try:
            idx = _find_supporting_root(segments, "0", "4")
            # Tenet is segments up to idx + 2 (e.g., A.x.y.z.0.4.N)
            return ".".join(segments[:idx + 3])
        except ValueError:
            pass

    elif doc_type == "Scenario Variation":
        # Parent is the scenario (drop the .varN)
        return ".".join(segments[:-1])

    elif doc_type == "Active Data":
        # Parent is the controller (before .0.6)
        try:
            idx = _find_supporting_root(segments, "0", "6")
            return ".".join(segments[:idx])
        except ValueError:
            pass

    # Regular docs: drop last segment
    if len(segments) > 2:
        return ".".join(segments[:-1])
    return None


def build_ancestors(number: str, doc_type: str) -> list[str]:
    """Build the ancestor path prefixes for a document number.

    For regular docs like A.6.1.1.2, ancestors are: [A.6, A.6.1, A.6.1.1]
    For supporting docs, we go up to the target/controller document.
    """
    if number.startswith("NR-"):
        return []

    segments = number.split(".")
    ancestors = []
    # Build prefixes from A.X up to (but not including) the full number
    for i in range(2, len(segments)):
        ancestors.append(".".join(segments[:i]))
    return ancestors


def parse_atlas(atlas_path: Path) -> list[dict]:
    """Parse the Atlas file and return a list of document entries."""
    documents = []
    current_line = 0

    with open(atlas_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # First pass: find all title lines
    for i, line in enumerate(lines):
        m = TITLE_RE.match(line)
        if m:
            heading_level = len(m.group(1))
            number = m.group(2)
            name = m.group(3).strip()
            doc_type = m.group(4)
            uuid = m.group(5)

            # Handle varN segments (they contain non-dot separators)
            segments = number.replace("var", ".var").split(".") if "var" in number else number.split(".")

            documents.append({
                "uuid": uuid,
                "number": number,
                "name": name,
                "type": doc_type,
                "depth": compute_semantic_depth(number, doc_type),
                "heading_level": heading_level,
                "line_start": i + 1,  # 1-indexed
                "line_end": None,     # filled in second pass
                "parent_number": find_parent_number(number, doc_type, segments),
                "ancestors": build_ancestors(number, doc_type),
            })

    # Second pass: compute line_end for each document
    for i, doc in enumerate(documents):
        if i + 1 < len(documents):
            doc["line_end"] = documents[i + 1]["line_start"] - 1
        else:
            doc["line_end"] = len(lines)

    # Third pass: resolve parent_number to parent_uuid
    number_to_uuid = {doc["number"]: doc["uuid"] for doc in documents}
    for doc in documents:
        parent_num = doc.pop("parent_number")
        doc["parent_uuid"] = number_to_uuid.get(parent_num) if parent_num else None

    return documents


def main():
    if not ATLAS_FILE.exists():
        print(f"Error: Atlas file not found at {ATLAS_FILE}", file=sys.stderr)
        print("Run scripts/setup.sh first to clone the Atlas repo.", file=sys.stderr)
        sys.exit(1)

    print(f"Parsing {ATLAS_FILE}...")
    documents = parse_atlas(ATLAS_FILE)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2)

    print(f"Index built: {len(documents)} documents → {OUTPUT_FILE}")

    # Print summary by type
    type_counts = {}
    for doc in documents:
        type_counts[doc["type"]] = type_counts.get(doc["type"], 0) + 1
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")


if __name__ == "__main__":
    main()
