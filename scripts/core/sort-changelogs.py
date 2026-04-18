#!/usr/bin/env python3
"""
Sort changelog.md entries by merge date, most-recent first.

Each changelog has a header block (title + description + first `---`), then
a series of `## PR #N` entries separated by `---` lines. Entries are sorted
by the `**Merged:** YYYY-MM-DD` date.

Usage:
    python3 scripts/core/sort-changelogs.py           # sort all history/**/changelog.md
    python3 scripts/core/sort-changelogs.py --dry     # show what would change without writing
    python3 scripts/core/sort-changelogs.py <path>... # sort specific files
"""
import argparse
import re
import sys
from pathlib import Path

MERGED_RE = re.compile(r"\*\*Merged:\*\*\s*(\d{4}-\d{2}-\d{2})")
ENTRY_START_RE = re.compile(r"^## PR #\d+", re.MULTILINE)


def split_file(text: str) -> tuple[str, list[str]]:
    """Return (header, [entries]) where each entry is the full text from
    `## PR #N` through (but not including) the next entry's `## PR #` marker.
    Header is everything before the first `## PR` entry."""
    match = ENTRY_START_RE.search(text)
    if not match:
        return text, []
    header = text[: match.start()]
    rest = text[match.start() :]
    # Split on lines that are entry starts
    starts = [m.start() for m in ENTRY_START_RE.finditer(rest)]
    entries = []
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(rest)
        entries.append(rest[start:end])
    return header, entries


def entry_date(entry: str) -> str:
    m = MERGED_RE.search(entry)
    return m.group(1) if m else "0000-00-00"


def entry_pr_number(entry: str) -> int:
    m = re.match(r"## PR #(\d+)", entry)
    return int(m.group(1)) if m else 0


def sort_file(path: Path, dry: bool) -> bool:
    original = path.read_text()
    header, entries = split_file(original)
    if not entries:
        return False

    # Normalize each entry: strip trailing whitespace, ensure it ends with `\n---\n\n`
    normalized = []
    for e in entries:
        body = e.rstrip()
        if body.endswith("---"):
            body = body[: -len("---")].rstrip()
        normalized.append(body + "\n\n---\n\n")

    # Sort: newest merge date first; tiebreak on higher PR number (generally = later)
    sorted_entries = sorted(
        normalized,
        key=lambda e: (entry_date(e), entry_pr_number(e)),
        reverse=True,
    )

    # Ensure header ends with exactly one blank line separator before first entry.
    # Canonical header shape ends with `---\n\n`.
    header_norm = header.rstrip() + "\n\n"

    new_text = header_norm + "".join(sorted_entries)
    # Trim trailing empty lines to a single newline
    new_text = new_text.rstrip() + "\n"

    if new_text == original:
        return False
    if dry:
        print(f"  would rewrite: {path}")
    else:
        path.write_text(new_text)
        print(f"  sorted: {path}")
    return True


def sort_log(path: Path, dry: bool) -> bool:
    """Sort history/_log.md table rows by merge date, most recent first."""
    original = path.read_text()
    lines = original.split("\n")
    # Find the table: first line starting with `| PR |`, next is separator, then data rows
    try:
        header_idx = next(i for i, l in enumerate(lines) if l.startswith("| PR |"))
    except StopIteration:
        return False
    separator_idx = header_idx + 1
    data_start = separator_idx + 1
    # Data rows: consecutive lines starting with `|`
    data_end = data_start
    while data_end < len(lines) and lines[data_end].startswith("|"):
        data_end += 1

    rows = lines[data_start:data_end]

    def row_key(row: str):
        parts = [p.strip() for p in row.split("|")]
        # parts[0] is empty (leading |), parts[1] = #N, parts[2] = title, parts[3] = merged
        pr_num = int(parts[1].lstrip("#")) if len(parts) > 1 and parts[1].lstrip("#").isdigit() else 0
        date = parts[3] if len(parts) > 3 else "0000-00-00"
        return (date, pr_num)

    sorted_rows = sorted(rows, key=row_key, reverse=True)

    new_lines = lines[:data_start] + sorted_rows + lines[data_end:]
    new_text = "\n".join(new_lines)
    if new_text == original:
        return False
    if dry:
        print(f"  would rewrite: {path}")
    else:
        path.write_text(new_text)
        print(f"  sorted: {path}")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", help="Specific changelog.md files to sort")
    ap.add_argument("--dry", action="store_true", help="Show what would change without writing")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    if args.paths:
        files = [Path(p) for p in args.paths]
    else:
        files = sorted((repo_root / "history").rglob("changelog.md"))

    changed = 0
    for f in files:
        if sort_file(f, args.dry):
            changed += 1

    # Also sort _log.md
    log_file = repo_root / "history" / "_log.md"
    if log_file.exists() and sort_log(log_file, args.dry):
        changed += 1

    print(f"\n{'Would change' if args.dry else 'Changed'}: {changed} files")


if __name__ == "__main__":
    main()
