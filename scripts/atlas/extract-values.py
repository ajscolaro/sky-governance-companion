#!/usr/bin/env python3
"""Extract structured before/after values from a PR diff against the atomized Atlas.

Stage 2 of the auto-changelog pipeline. Reads:
- A unified diff (path or stdin)
- The Stage 1 manifest (--manifest <path>) emitted by classify-diff.py

Emits JSON to stdout describing per-document body-level changes plus
cross-document patterns (terminology sweeps, identifier fixes).

Output schema:
{
  "documents": [
    {
      "uuid", "number", "name", "type", "kind",
      "path",                          # post-rename path
      "body_diff": {                   # raw body-only diff (excludes frontmatter)
        "added_lines": [...],
        "removed_lines": [...]
      },
      "extracted": {
        "numerics_before": [{value, unit, context}, ...],
        "numerics_after":  [...],
        "addresses_before": [...],
        "addresses_after":  [...],
        "uuid_refs_before": [...],
        "uuid_refs_after":  [...],
        "dates_before": [...],
        "dates_after":  [...],
        "param_pairs":  [{label, before, after}, ...],     # explicit -X +Y pairs
        "tbd_resolutions": [{label, value}, ...],          # X: TBD → X: <value>
        "lead_sentence": "...",                            # for added docs
        "name_change": {old, new} | null
      }
    },
    ...
  ],
  "patterns": {
    "terminology_sweeps": [
      {"old", "new", "uuids": [...], "scope": "body"|"name"}
    ],
    "solidity_identifier_fixes": [
      {"old", "new", "uuids": [...]}
    ],
    "article_deletions": [
      {"article_uuid", "section_uuids": [...], "leaf_uuids": [...]}
    ]
  }
}

The script does not interpret meaning — it only surfaces machine-readable
deltas. Stage 3 (enrich.py) decides what each delta implies; Stage 4
(render.py) chooses how to phrase it.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
INDEX_FILE = PROJECT_DIR / "data" / "index.json"

# --- Diff parsing ----------------------------------------------------------

UUID_RE = re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b")
ADDRESS_RE = re.compile(r"\b0x[a-fA-F0-9]{40}\b")
DATE_RE = re.compile(
    r"\b(?:(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},\s*\d{4}|\d{4}-\d{2}-\d{2})\b"
)
# Numerics with units: amounts (M/K/B), percentages, hours/days, rates, USD
NUMERIC_RE = re.compile(
    r"""
    (?P<value>-?\d{1,3}(?:[,\d]*\.?\d*|\.\d+))\s*
    (?P<unit>%|million|billion|bps|hours?|hrs?|days?|seconds?|sec|years?|
             [MBK]\b|USD|USDS|DAI|SKY|sUSDS|ETH|BTC|USDC|USDT)?
    """,
    re.VERBOSE | re.IGNORECASE,
)
# Markdown link to UUID: [Anything - Name](uuid)
MD_UUID_REF_RE = re.compile(r"\[[^\]]+\]\(([0-9a-f-]{36})\)")
# Solidity identifiers in backticks: `Foo Bar` where there's a space (broken ident)
BACKTICK_RE = re.compile(r"`([^`]+)`")
# Inline-code-fenced patterns commonly used in Sky Atlas: token names, fn names


def split_blocks(diff: str) -> list[tuple[str, str]]:
    """Yield (a_path, b_path, block) per file. Strips the leading 'diff --git '."""
    parts = re.split(r"(?m)^diff --git ", diff)
    out: list[tuple[str, str, str]] = []
    for part in parts[1:]:
        if not part:
            continue
        first_line, _, rest = part.partition("\n")
        m = re.match(r"(\S+)\s+(\S+)", first_line)
        if not m:
            continue
        a = m.group(1)[2:] if m.group(1).startswith(("a/", "b/")) else m.group(1)
        b = m.group(2)[2:] if m.group(2).startswith(("a/", "b/")) else m.group(2)
        out.append((a, b, rest))
    return out


def is_doc_block(a: str, b: str) -> bool:
    a_doc = a.endswith("/document.md") and a.startswith("content/")
    b_doc = b.endswith("/document.md") and b.startswith("content/")
    return a_doc or b_doc


_HUNK_RE = re.compile(r"^@@\s+-(\d+)(?:,(\d+))?\s+\+(\d+)(?:,(\d+))?\s+@@")
# Standard docs: 8-line frontmatter (---, 6 fields, ---). NR docs add a
# `targets:` field, making theirs 9 lines.
_FRONTMATTER_LINES_STANDARD = 8
_FRONTMATTER_LINES_NR = 9


def frontmatter_lines_for(a_path: str, b_path: str) -> int:
    """Return frontmatter line count for an atomized Atlas doc block."""
    is_nr = a_path.startswith("content/NR/") or b_path.startswith("content/NR/")
    return _FRONTMATTER_LINES_NR if is_nr else _FRONTMATTER_LINES_STANDARD


def split_frontmatter_from_body(
    block: str, frontmatter_lines: int = _FRONTMATTER_LINES_STANDARD
) -> tuple[list[str], list[str]]:
    """Return (added_body_lines, removed_body_lines), excluding frontmatter changes.

    Body membership is determined by tracking the current line position within
    each hunk and skipping any line whose old or new position lies within the
    frontmatter window. This handles both partial hunks (where git omits
    unchanged context) and whole-file adds/deletes where the entire document
    appears in one hunk.
    """
    added_body: list[str] = []
    removed_body: list[str] = []

    # Track line positions within the current hunk
    old_line = new_line = 0
    in_hunk = False

    for line in block.split("\n"):
        if line.startswith(("diff ", "index ", "--- ", "+++ ", "new file", "deleted file",
                            "rename from", "rename to", "similarity index")):
            in_hunk = False
            continue

        m = _HUNK_RE.match(line)
        if m:
            old_line = int(m.group(1)) if m.group(1) else 1
            new_line = int(m.group(3)) if m.group(3) else 1
            in_hunk = True
            continue

        if not in_hunk:
            continue

        if not line:
            # Empty line in the diff — treat as a context line that advances both sides
            old_line += 1
            new_line += 1
            continue

        prefix = line[0]
        rest = line[1:]
        if prefix == "+":
            if new_line > frontmatter_lines:
                added_body.append(rest)
            new_line += 1
        elif prefix == "-":
            if old_line > frontmatter_lines:
                removed_body.append(rest)
            old_line += 1
        elif prefix == " ":
            old_line += 1
            new_line += 1
        # any other prefix is ignored
    return added_body, removed_body


def extract_frontmatter_changes(block: str) -> dict:
    """Detect frontmatter-level changes: name, docNo, depth, type, etc."""
    out: dict = {}
    # Grab +/- lines from the frontmatter window only
    in_fm = False
    fm_count = 0
    plus_lines: list[str] = []
    minus_lines: list[str] = []
    for line in block.split("\n"):
        if line.startswith(("@@", "diff ", "index ", "--- ", "+++ ", "new file",
                            "deleted file", "rename from", "rename to", "similarity")):
            continue
        bare = line[1:] if line and line[0] in "+- " else line
        if bare.strip() == "---":
            fm_count += 1
            continue
        if fm_count >= 2:
            break
        if line.startswith("+"):
            plus_lines.append(line[1:])
        elif line.startswith("-"):
            minus_lines.append(line[1:])

    def field(lines: list[str], name: str) -> str | None:
        for L in lines:
            m = re.match(rf"^{re.escape(name)}:\s*(.*)$", L)
            if m:
                v = m.group(1).strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                return v
        return None

    for fname in ("name", "docNo", "type", "depth", "childType"):
        old = field(minus_lines, fname)
        new = field(plus_lines, fname)
        if old is not None or new is not None:
            if old != new:
                out[fname] = {"old": old, "new": new}
    return out


def extract_lead_sentence(added_lines: list[str]) -> str:
    """First substantive sentence of an added doc body. Skip headings and empty lines."""
    for line in added_lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            # Atomized docs always begin with a `###### A.x.y - Name [Type]` heading;
            # skip it and continue
            continue
        # Cap at first sentence boundary or 240 chars
        m = re.search(r"^(.{20,240}?[.!?])(?:\s|$)", s)
        if m:
            return m.group(1)
        return s[:240]
    return ""


def _word_tokenize(s: str) -> list[str]:
    """Split into runs of word chars / non-word chars / whitespace.

    Each run is a token. Joining the tokens reproduces the original string.
    Word-level diffing gives more meaningful sub-substring deltas than
    char-level (which breaks on letters within shared words).
    """
    return re.findall(r"\w+|\s+|[^\w\s]", s)


def _diff_pair(removed: str, added: str) -> list[dict]:
    """Word-level diff between two lines; emit per-region changes.

    Adjacent replace ops separated only by whitespace are merged. Without this
    step, difflib reports `Governance Facilitators` → `Core Council` as two
    separate pairs (`Governance`→`Core`, `Facilitators`→`Council`), losing the
    multi-word phrase that's the meaningful edit.
    """
    import difflib
    r_tokens = _word_tokenize(removed)
    a_tokens = _word_tokenize(added)
    sm = difflib.SequenceMatcher(a=r_tokens, b=a_tokens, autojunk=False)

    # Pass 1: collect all opcodes
    ops = list(sm.get_opcodes())

    # Pass 2: merge "replace, whitespace-equal, replace" sequences into one
    # replace spanning the whole region. Run iteratively until stable.
    def merge_once(ops: list[tuple]) -> tuple[list[tuple], bool]:
        merged: list[tuple] = []
        i = 0
        changed = False
        while i < len(ops):
            if (i + 2 < len(ops)
                    and ops[i][0] == "replace"
                    and ops[i + 1][0] == "equal"
                    and ops[i + 2][0] == "replace"
                    and "".join(r_tokens[ops[i + 1][1]:ops[i + 1][2]]).strip() == ""):
                # Merge ops[i], ops[i+1], ops[i+2] into a single replace
                _, i1, _, j1, _ = ops[i]
                _, _, i2, _, j2 = ops[i + 2]
                merged.append(("replace", i1, i2, j1, j2))
                i += 3
                changed = True
            else:
                merged.append(ops[i])
                i += 1
        return merged, changed

    while True:
        ops, changed = merge_once(ops)
        if not changed:
            break

    out: list[dict] = []
    CONTEXT_TOKENS = 3
    for tag, i1, i2, j1, j2 in ops:
        if tag == "equal":
            continue
        before = "".join(r_tokens[i1:i2])
        after = "".join(a_tokens[j1:j2])
        before_s = before.strip()
        after_s = after.strip()
        if not before_s and not after_s:
            continue
        ctx_before = "".join(r_tokens[max(0, i1 - CONTEXT_TOKENS):i1])
        ctx_after = "".join(r_tokens[i2:i2 + CONTEXT_TOKENS])
        out.append({
            "before": before_s,
            "after": after_s,
            "context_before": ctx_before,
            "context_after": ctx_after,
            "kind": "insert" if not before_s else ("delete" if not after_s else "sub"),
        })
    return out


def find_paired_changes(
    added: list[str], removed: list[str]
) -> list[dict]:
    """Identify substring substitutions across paired added/removed lines.

    When line counts match, pair by index. When they don't, fall back to
    pairing by best similarity (handles cases where one line splits into
    two or unrelated lines were inserted alongside edits).
    """
    pairs: list[dict] = []
    if len(added) == len(removed):
        for r, a in zip(removed, added):
            if r != a:
                pairs.extend(_diff_pair(r, a))
    else:
        # Best-effort pairing: for each removed line, find the most-similar
        # added line and treat them as a pair. Surplus lines (unpaired)
        # are recorded as insertions/deletions.
        import difflib
        used = set()
        for r in removed:
            best_idx, best_ratio = -1, 0.0
            for i, a in enumerate(added):
                if i in used:
                    continue
                ratio = difflib.SequenceMatcher(None, r, a).ratio()
                if ratio > best_ratio:
                    best_idx, best_ratio = i, ratio
            if best_idx >= 0 and best_ratio > 0.5:
                used.add(best_idx)
                pairs.extend(_diff_pair(r, added[best_idx]))
            else:
                pairs.append({"before": r.strip(), "after": "", "context_before": "",
                              "context_after": "", "kind": "delete"})
        for i, a in enumerate(added):
            if i not in used:
                pairs.append({"before": "", "after": a.strip(), "context_before": "",
                              "context_after": "", "kind": "insert"})
    return pairs


def find_tbd_resolutions(added: list[str], removed: list[str]) -> list[dict]:
    """Find lines where '...: TBD' or '...: To Be Determined' becomes a real value."""
    tbd_re = re.compile(r"\b(?:TBD|To Be Determined|to be determined)\b", re.IGNORECASE)
    out: list[dict] = []
    for r in removed:
        if tbd_re.search(r):
            # Pull a label: text before colon
            m = re.match(r"\s*[-*]?\s*\*?\*?(.+?):\s*(.+)$", r.strip())
            if m:
                label = m.group(1).strip().strip("*").strip()
                # Look in added for a line with same label
                for a in added:
                    am = re.match(r"\s*[-*]?\s*\*?\*?(.+?):\s*(.+)$", a.strip())
                    if am and am.group(1).strip().strip("*").strip() == label:
                        out.append({"label": label, "before": "TBD", "after": am.group(2).strip()})
                        break
    return out


def classify_pattern(pair: dict) -> str:
    """Tag what kind of edit a paired change represents."""
    before = pair["before"]
    after = pair["after"]
    # Solidity identifier whitespace fix: identifier with internal whitespace
    # becomes the same identifier without the space (keeps all alphanumerics).
    if (before and after
            and re.fullmatch(r"[A-Za-z][A-Za-z0-9 ]*", before)
            and re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", after)
            and " " in before
            and before.replace(" ", "") == after):
        return "solidity_identifier"
    # Authority-role rename signal
    if (any(k in before for k in ("Facilitator", "Council", "Executor"))
            or any(k in after for k in ("Facilitator", "Council", "Executor"))):
        return "role_or_authority"
    return "general"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("diff_path", nargs="?", help="Path to unified diff (default stdin)")
    ap.add_argument("--manifest", required=True, help="Stage 1 manifest JSON")
    args = ap.parse_args()

    diff = (Path(args.diff_path).read_text(encoding="utf-8", errors="replace")
            if args.diff_path else sys.stdin.read())
    manifest = json.loads(Path(args.manifest).read_text())

    # Build a UUID → manifest entry lookup so we can attach kind/number/name
    uuid_to_entry: dict[str, dict] = {}
    for kind in ("added", "deleted", "modified", "renamed"):
        for entry in manifest.get(kind, []):
            uuid_to_entry[entry["uuid"]] = {**entry, "kind": kind}
    name_changes = {n["uuid"]: n for n in manifest.get("name_changed", [])}

    # Build path→UUID for diff blocks
    if INDEX_FILE.exists():
        index = json.loads(INDEX_FILE.read_text())
        path_to_uuid = {d["path"]: d["uuid"] for d in index}
    else:
        path_to_uuid = {}

    documents: list[dict] = []
    blocks = split_blocks(diff)

    for a_path, b_path, block in blocks:
        if not is_doc_block(a_path, b_path):
            continue

        # Identify uuid for this block: prefer +id frontmatter, then path lookup
        m_add = re.search(r"^\+id:\s*([0-9a-f-]{36})", block, re.M)
        m_rem = re.search(r"^-id:\s*([0-9a-f-]{36})", block, re.M)
        uuid = (m_add.group(1) if m_add else None) or (m_rem.group(1) if m_rem else None)
        if not uuid:
            full_path = ".atlas-repo/" + (b_path if b_path != "/dev/null" else a_path)
            uuid = path_to_uuid.get(full_path)
        if not uuid:
            continue

        manifest_entry = uuid_to_entry.get(uuid)
        if not manifest_entry:
            continue

        fm_lines = frontmatter_lines_for(a_path, b_path)
        added_body, removed_body = split_frontmatter_from_body(block, fm_lines)
        fm_changes = extract_frontmatter_changes(block)

        extracted = {
            "addresses_before": list(set(ADDRESS_RE.findall("\n".join(removed_body)))),
            "addresses_after": list(set(ADDRESS_RE.findall("\n".join(added_body)))),
            "uuid_refs_before": list(set(UUID_RE.findall("\n".join(removed_body)))),
            "uuid_refs_after": list(set(UUID_RE.findall("\n".join(added_body)))),
            "dates_before": list(set(DATE_RE.findall("\n".join(removed_body)))),
            "dates_after": list(set(DATE_RE.findall("\n".join(added_body)))),
            "tbd_resolutions": find_tbd_resolutions(added_body, removed_body),
            "paired_changes": find_paired_changes(added_body, removed_body),
            "lead_sentence": (extract_lead_sentence(added_body)
                              if manifest_entry["kind"] == "added" else ""),
            "fm_changes": fm_changes,
        }

        # Tag patterns within paired changes
        for pair in extracted["paired_changes"]:
            pair["pattern"] = classify_pattern(pair)

        documents.append({
            "uuid": uuid,
            "number": manifest_entry.get("number"),
            "name": manifest_entry.get("name"),
            "type": manifest_entry.get("type"),
            "kind": manifest_entry["kind"],
            "path": manifest_entry.get("path") or manifest_entry.get("to"),
            "name_change": name_changes.get(uuid),
            "extracted": extracted,
        })

    # ---- Cross-document patterns -----------------------------------------

    # Terminology sweep: same (before, after) pair appearing across ≥3 docs
    sweep_buckets: dict[tuple[str, str, str], list[str]] = defaultdict(list)
    for doc in documents:
        for pair in doc["extracted"]["paired_changes"]:
            key = (pair["before"], pair["after"], pair["pattern"])
            if pair["before"] and pair["after"]:
                sweep_buckets[key].append(doc["uuid"])

    terminology_sweeps: list[dict] = []
    solidity_fixes: list[dict] = []
    for (before, after, pattern), uuids in sweep_buckets.items():
        unique_uuids = sorted(set(uuids))
        # Solidity-identifier fixes are high-confidence even at 2 occurrences
        # (the same compile-correctness pattern across two files almost
        # never coincides with unrelated edits); narrative sweeps need more
        # signal to avoid surfacing every 2-doc tweak.
        threshold = 2 if pattern == "solidity_identifier" else 3
        if len(unique_uuids) < threshold:
            continue
        record = {"old": before, "new": after, "uuids": unique_uuids}
        if pattern == "solidity_identifier":
            solidity_fixes.append(record)
        else:
            terminology_sweeps.append(record)

    # Article deletion: a deleted Article whose entire subtree is also deleted
    article_deletions: list[dict] = []
    deleted_by_number = {d["number"]: d for d in documents
                         if d["kind"] == "deleted" and d["number"]}
    for d in documents:
        if d["kind"] == "deleted" and d.get("type") == "Article":
            prefix = d["number"] + "."
            children = [x for x in deleted_by_number.values()
                        if x["number"] != d["number"] and x["number"].startswith(prefix)]
            article_deletions.append({
                "article_uuid": d["uuid"],
                "article_name": d["name"],
                "article_number": d["number"],
                "subtree_uuids": [c["uuid"] for c in children],
                "subtree_count": len(children),
            })

    out = {
        "documents": documents,
        "patterns": {
            "terminology_sweeps": terminology_sweeps,
            "solidity_identifier_fixes": solidity_fixes,
            "article_deletions": article_deletions,
        },
    }
    json.dump(out, sys.stdout, indent=2, default=str)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
