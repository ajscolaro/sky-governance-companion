#!/usr/bin/env python3
"""Build data/forum/registry.json from the Atlas Authorized Forum Accounts table.

Reads section A.2.7.1.1.1.1.4.0.6.1 (UUID b71564fd-22e0-4c69-99d1-5b23fc1fa329)
from the synced Atlas, parses the markdown table, and writes a structured registry
mapping forum handles to entities and roles. Consumed by /forum-search, the
session briefing, and the roster reconciliation script.

Sky Forum only — the Atlas section governs Sky Forum accounts specifically.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Tuple

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
INDEX_FILE = PROJECT_DIR / "data" / "index.json"
ATLAS_REPO = PROJECT_DIR / ".atlas-repo"
OUTPUT_FILE = PROJECT_DIR / "data" / "forum" / "registry.json"

REGISTRY_UUID = "b71564fd-22e0-4c69-99d1-5b23fc1fa329"
TRANSITIVE_RE = re.compile(
    r"\s*\(\s*and\s+their\s+authorized\s+representatives\s*\)\s*$",
    re.IGNORECASE,
)


def load_section_lines() -> List[str]:
    """Locate the registry document via data/index.json and return its body lines."""
    with INDEX_FILE.open() as f:
        index = json.load(f)
    entry = next((e for e in index if e.get("uuid") == REGISTRY_UUID), None)
    if entry is None:
        raise RuntimeError(
            f"Registry section UUID {REGISTRY_UUID} not found in index. "
            "Has the Atlas been synced and indexed?"
        )
    doc_path = PROJECT_DIR / entry["path"]
    text = doc_path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        end = text.index("\n---\n", 4)
        text = text[end + 5:]
    return text.splitlines(keepends=True)


def parse_ar_field(ar_str: str) -> Tuple[List[str], List[str]]:
    """Parse the Authorized Representatives column.

    Returns (direct_handles, transitive_refs). When the trailing
    "(and their authorized representatives)" parenthetical is present,
    every listed handle is also recorded as a transitive ref (its own
    ARs propagate at lookup time).
    """
    if not ar_str or ar_str.strip().upper() in {"N/A", "NA", "-"}:
        return [], []

    transitive_match = TRANSITIVE_RE.search(ar_str)
    has_transitive = bool(transitive_match)
    if has_transitive:
        ar_str = ar_str[: transitive_match.start()]

    handles = [h.strip() for h in ar_str.split(",") if h.strip()]
    transitive = list(handles) if has_transitive else []
    return handles, transitive


def parse_table(lines: List[str]) -> Tuple[List[Tuple[str, str, str, str]], List[str]]:
    """Extract rows from the markdown table. Returns (rows, warnings)."""
    rows = []
    warnings = []
    for raw in lines:
        line = raw.strip()
        if not line.startswith("|"):
            continue
        # Header separator (|---|---|...)
        if re.match(r"^\|\s*[-:]+", line):
            continue
        # Header row
        if line.lower().startswith("| entity name"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 4:
            warnings.append(f"Malformed row (expected 4 cells, got {len(cells)}): {line}")
            continue
        rows.append(tuple(cells))
    return rows, warnings


def normalize(value: str) -> str | None:
    """Treat 'N/A' and empty as null."""
    if not value or value.strip().upper() in {"N/A", "NA", "-"}:
        return None
    return value.strip()


def build_registry(rows, warnings):
    entities = {}
    by_handle: dict[str, list] = defaultdict(list)
    seen_entity_handles: dict[str, str] = {}

    for entity_name, role, entity_handle, ar_field in rows:
        eh = normalize(entity_handle)
        role_norm = normalize(role)
        ars, transitive = parse_ar_field(ar_field)

        entities[entity_name] = {
            "role": role_norm,
            "entity_handle": eh,
            "authorized_representatives": ars,
            "transitive_refs": transitive,
        }

        if eh:
            key = eh.lower()
            if key in seen_entity_handles and seen_entity_handles[key] != entity_name:
                warnings.append(
                    f"Duplicate Entity Handle '{eh}' on rows: "
                    f"{seen_entity_handles[key]} and {entity_name}"
                )
            seen_entity_handles[key] = entity_name
            by_handle[key].append(
                {
                    "entity": entity_name,
                    "role": role_norm,
                    "type": "entity_handle",
                    "display_handle": eh,
                }
            )

        for ar in ars:
            by_handle[ar.lower()].append(
                {
                    "entity": entity_name,
                    "role": role_norm,
                    "type": "authorized_representative",
                    "display_handle": ar,
                }
            )

    return entities, dict(by_handle), warnings


def get_atlas_commit() -> str | None:
    if not ATLAS_REPO.exists():
        return None
    try:
        result = subprocess.run(
            ["git", "-C", str(ATLAS_REPO), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.SubprocessError, OSError):
        pass
    return None


def main() -> int:
    quiet = "--quiet" in sys.argv

    try:
        section_lines = load_section_lines()
    except FileNotFoundError as e:
        print(f"build-account-registry: {e}", file=sys.stderr)
        return 1
    except RuntimeError as e:
        # Section not in index — Atlas may pre-date PR #227. Degrade gracefully.
        if not quiet:
            print(f"build-account-registry: {e}", file=sys.stderr)
        return 0

    rows, warnings = parse_table(section_lines)
    if not rows:
        if not quiet:
            print("build-account-registry: no rows parsed from registry table", file=sys.stderr)
        return 1

    entities, by_handle, warnings = build_registry(rows, warnings)

    registry = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "atlas_commit": get_atlas_commit(),
        "section_uuid": REGISTRY_UUID,
        "entities": entities,
        "by_handle": by_handle,
        "warnings": warnings,
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w") as f:
        json.dump(registry, f, indent=2, sort_keys=False)
        f.write("\n")

    if not quiet:
        print(
            f"build-account-registry: wrote {len(entities)} entities, "
            f"{len(by_handle)} unique handles, {len(warnings)} warnings → {OUTPUT_FILE.relative_to(PROJECT_DIR)}",
            file=sys.stderr,
        )
        for w in warnings:
            print(f"  warn: {w}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
