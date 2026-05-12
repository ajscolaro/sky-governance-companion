#!/usr/bin/env python3
"""Compose a subtree of the Atlas in Atlas.md style (continuous prose).

Wraps `.atlas-repo/sync/compose.py` to produce a human-readable view of an
Atlas area — proper `# A.X.Y - Name` heading lines, NRs inserted at their
target docs, no per-doc frontmatter. Useful when reading an unfamiliar area
end-to-end rather than as 47 separate document.md files.

For PR review, prefer `/atlas-analyze` — it reads per-doc diffs and current
state directly, which is what atomization makes natural.

Usage:
  compose-subtree.py <prefix>

Output:
  tmp/compose/<prefix>.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
ATLAS_REPO = PROJECT_DIR / ".atlas-repo"
INDEX_FILE = PROJECT_DIR / "data" / "index.json"
OUTPUT_DIR = PROJECT_DIR / "tmp" / "compose"

# Heading line emitted by compose.py: `# A.0 - Name [Type]  <!-- UUID: ... -->`
HEADING_RE = re.compile(r"^(#+)\s+(\S+)\s+-\s+")


def _import_compose():
    sync_dir = ATLAS_REPO / "sync"
    if not (sync_dir / "compose.py").is_file():
        raise SystemExit(
            f"Error: {sync_dir}/compose.py not found. "
            "Run scripts/core/setup.sh to sync the Atlas."
        )
    sys.path.insert(0, str(sync_dir))
    from compose import compose  # type: ignore
    return compose


def extract_subtree(composed: str, prefix: str) -> str:
    """Return composed lines covering `prefix` and its descendants.

    Matches on document number (not heading depth) because compose.py caps
    heading levels at 6, so cousins at maximum depth share a level.
    """
    lines = composed.splitlines()
    start = None
    end = len(lines)
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if not m:
            continue
        num = m.group(2)
        if start is None:
            if num == prefix:
                start = i
        elif num != prefix and not num.startswith(prefix + "."):
            end = i
            break
    if start is None:
        raise SystemExit(
            f"Error: heading for '{prefix}' not found in composed output."
        )
    return "\n".join(lines[start:end])


def validate_prefix(prefix: str) -> None:
    if not INDEX_FILE.exists():
        return
    try:
        index = json.loads(INDEX_FILE.read_text())
    except (OSError, json.JSONDecodeError):
        return
    if not any(d.get("number") == prefix for d in index):
        print(f"Warning: prefix '{prefix}' not found in index.", file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("prefix", help="Atlas document number (e.g. A.2.3.1.4.2)")
    args = ap.parse_args()

    validate_prefix(args.prefix)

    main_content = ATLAS_REPO / "content"
    if not main_content.is_dir():
        raise SystemExit(
            f"Error: {main_content} not found. Run scripts/core/setup.sh."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    compose = _import_compose()
    composed = compose(str(main_content))
    sliced = extract_subtree(composed, args.prefix)

    out_path = OUTPUT_DIR / f"{args.prefix}.md"
    out_path.write_text(sliced)
    print(f"-> {out_path.relative_to(PROJECT_DIR)}  ({len(sliced):,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
