#!/usr/bin/env python3
"""Enrich extracted PR data with governance metadata, routing, and cross-references.

Stage 3 of the auto-changelog pipeline. Reads:
- Stage 2 output (--extracted <path>) from extract-values.py
- PR metadata (--pr-meta <path>) — JSON with title/body/merged_at/additions/deletions

Looks up:
- Ratification poll for Flow 1 PRs (via data/voting/polls/vote-matrix.json)
- Executive spell for Flow 2 PRs (via data/voting/executive/lifecycle.json)
- UUID → name resolution for cross-references
- Entity routing (which history changelog each doc maps to)
- Governance flow classification (1=text-edit, 2=spell-recording, 3=active-data-direct)
- Type label (Weekly edit / SAEP-N / Spell recording / Active Data update / etc.)

Emits enriched JSON to stdout, with the same shape as Stage 2 plus:
- Top-level: pr_meta, governance_flow, type_label, poll, spell, entity_groups
- Per-document: entity (history dir), uuid_refs_resolved (uuid → name)

The script does no rendering — Stage 4 (render.py) consumes this.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
INDEX_FILE = PROJECT_DIR / "data" / "index.json"
ROUTING_FILE = PROJECT_DIR / "history" / "entity-routing.conf"
VOTE_MATRIX = PROJECT_DIR / "data" / "voting" / "polls" / "vote-matrix.json"
LIFECYCLE = PROJECT_DIR / "data" / "voting" / "executive" / "lifecycle.json"


def load_routing() -> list[tuple[str, str, str | None]]:
    """Return [(prefix, dirname, anchor_uuid|None), ...] in file order.

    The conf carries an optional third tab-separated column: the immutable UUID
    of the subtree root. It's the primary routing key (see route_doc_anchored);
    the prefix is the legacy fallback.
    """
    rules: list[tuple[str, str, str | None]] = []
    if not ROUTING_FILE.exists():
        return rules
    for line in ROUTING_FILE.read_text().splitlines():
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        if "\t" not in line:
            continue
        parts = line.split("\t")
        prefix, dirname = parts[0], parts[1]
        anchor = parts[2].strip() if len(parts) > 2 and parts[2].strip() else None
        rules.append((prefix, dirname, anchor))
    return rules


def route_doc(number: str | None, rules: list[tuple[str, str, str | None]]) -> str:
    """Legacy number-prefix match; first prefix wins. Fallback for route_doc_anchored."""
    if not number:
        return "_non-content"
    for prefix, dirname, _anchor in rules:
        if number == prefix or number.startswith(prefix + "."):
            return dirname
    return "_non-content"


def ancestor_uuids(number: str | None, own_uuid: str | None,
                   number_to_uuid: dict) -> set:
    """UUID set for a doc: its own UUID plus every ancestor's UUID, resolved
    from the doc's CURRENT number via the index.

    Renumber-proof: even if an ancestor's number changed, number_to_uuid maps
    the current number to the same immutable UUID an anchor was pinned to.
    """
    uuids: set = set()
    if own_uuid:
        uuids.add(own_uuid)
    if number and not number.startswith("NR-"):
        segs = number.split(".")
        for i in range(2, len(segs) + 1):
            u = number_to_uuid.get(".".join(segs[:i]))
            if u:
                uuids.add(u)
    return uuids


def route_doc_anchored(doc: dict, rules: list[tuple[str, str, str | None]],
                       by_uuid: dict, number_to_uuid: dict) -> str:
    """Route by UUID anchor (primary), falling back to number-prefix (legacy).

    A doc routes to the first rule whose anchor UUID is the doc's own UUID or
    one of its ancestors' UUIDs. This holds across renumbering because the UUID
    chain is rebuilt from the doc's current number each run.
    """
    num = routing_number(doc, by_uuid)
    cand = ancestor_uuids(num, doc.get("uuid"), number_to_uuid)
    for _prefix, dirname, anchor in rules:
        if anchor and anchor in cand:
            return dirname
    # Fallback: legacy number-prefix (un-anchored rules; deleted docs whose
    # number is no longer in the index; anything the UUID chain didn't cover).
    return route_doc(num, rules)


def routing_number(doc: dict, by_uuid: dict) -> str | None:
    """Resolve the doc number used for entity routing.

    For most docs this is just doc["number"]. For NR (Needed Research) docs
    the doc number ("NR-N") has no scope prefix, so we instead route by the
    number of the doc the NR attaches to via its frontmatter `targets` field.
    Falls back to the doc's own number if the target can't be resolved.
    """
    number = doc.get("number") or ""
    if not number.startswith("NR-"):
        return number

    # Targets either came from the manifest (added/deleted, parsed from the
    # diff frontmatter) or from the index (modified/renamed, resolved at
    # build-index time). Try both.
    targets = doc.get("targets") or []
    if not targets:
        idx_entry = by_uuid.get(doc.get("uuid"))
        if idx_entry:
            targets = idx_entry.get("targets") or []
    if not targets:
        return number  # falls through to _non-content via route_doc

    target_entry = by_uuid.get(targets[0])
    if target_entry and target_entry.get("number"):
        return target_entry["number"]
    return number


def is_reference_renumber_only(doc: dict) -> bool:
    """True if a modified doc's only body deltas are reference renumbers.

    Such a doc carries no content change — a *linked* doc moved and the dotted
    cross-reference path in this doc shifted (`…2.5.1` → `…2.6.1`) while the
    UUID target stayed put. The renderer collapses these into one entity-level
    summary line rather than a per-doc bullet, so they're marked pattern-covered
    (and thus not flagged by verify-entry). Single source of truth: render.py
    and verify-entry both rely on this classification via enrich's output.
    """
    if doc.get("kind") != "modified" or doc.get("name_change"):
        return False
    ext = doc.get("extracted", {})
    pairs = [p for p in ext.get("paired_changes", []) if p.get("before") or p.get("after")]
    if not pairs or not all(p.get("pattern") == "reference_renumber" for p in pairs):
        return False
    # Any genuine value/structure change keeps the doc material.
    if ext.get("tbd_resolutions"):
        return False
    if ext.get("addresses_after") and ext.get("addresses_after") != ext.get("addresses_before"):
        return False
    if set(ext.get("uuid_refs_before", [])) != set(ext.get("uuid_refs_after", [])):
        return False
    return True


def lookup_poll(pr_number: int) -> dict | None:
    """Find the ratification poll for a Flow 1 PR via the atlas_pr field."""
    if not VOTE_MATRIX.exists():
        return None
    data = json.loads(VOTE_MATRIX.read_text())
    polls = data.get("polls", {}) if isinstance(data, dict) else {}
    for pid, p in polls.items():
        if not isinstance(p, dict):
            continue
        if p.get("atlas_pr") == pr_number:
            ad_votes = p.get("ad_votes", {})
            tally = Counter(v.get("option") for v in ad_votes.values())
            return {
                "poll_id": pid,
                "title": p.get("title"),
                "start_date": p.get("start_date"),
                "end_date": p.get("end_date"),
                "poll_type": p.get("poll_type"),
                "result": p.get("result"),
                "tally": dict(tally),
                "ad_voter_count": len(ad_votes),
                "ad_non_voters": p.get("ad_non_voters", []),
                "poll_url": p.get("poll_url"),
            }
    return None


def lookup_spell_for_pr(pr_number: int) -> dict | None:
    """Find a spell whose atlas_prs include this PR (Flow 2 recording).

    Returns spell metadata plus the list of authorizing governance polls
    (resolved into title/result/atlas_pr triplets so render.py can cite them).
    """
    if not LIFECYCLE.exists():
        return None
    data = json.loads(LIFECYCLE.read_text())
    spells = data.get("spells", {})
    polls_by_id: dict = {}
    if VOTE_MATRIX.exists():
        vm = json.loads(VOTE_MATRIX.read_text())
        polls_by_id = vm.get("polls", {}) if isinstance(vm, dict) else {}

    for addr, sp in spells.items():
        prs = sp.get("atlas_prs", []) or []
        for ref in prs:
            if isinstance(ref, dict) and ref.get("pr") == pr_number:
                # Resolve each authorizing poll
                authorizing: list[dict] = []
                for poll_id in sp.get("governance_polls", []) or []:
                    p = polls_by_id.get(str(poll_id)) or polls_by_id.get(poll_id) or {}
                    authorizing.append({
                        "poll_id": poll_id,
                        "title": p.get("title"),
                        "result": p.get("result"),
                        "atlas_pr": p.get("atlas_pr"),
                    })
                return {
                    "address": addr,
                    "title": sp.get("title"),
                    "date": sp.get("date"),
                    "key": sp.get("key"),
                    "actions": [a.get("title") for a in sp.get("actions", [])][:8],
                    "proposal_url": sp.get("proposal_url"),
                    "authorizing_polls": authorizing,
                }
    return None


def classify_governance_flow(pr_meta: dict, extracted: dict, poll: dict | None,
                             spell: dict | None) -> tuple[int, str]:
    """Determine governance flow (1/2/3) and type label.

    Flow 1: Text edits ratified by poll (Atlas Edit Proposal, AEP, SAEP, etc.)
    Flow 2: Executive spell recordings (post-cast documentation)
    Flow 3: Direct edits to Active Data by designated controller
    """
    title = pr_meta.get("title", "") or ""
    title_low = title.lower()

    # Flow 2 detection: title mentions "spell changes" or "executive changes"
    # OR a spell record links back to this PR
    if spell or "spell change" in title_low or "executive change" in title_low:
        date = (spell or {}).get("date") or _extract_date_from_title(title) or "?"
        return 2, f"Spell recording ({date})"

    # Flow 3 detection: only Active Data documents modified, no governance poll
    docs = extracted.get("documents", [])
    if docs and poll is None:
        all_active_data = all(d.get("type") == "Active Data" for d in docs)
        if all_active_data:
            return 3, "Active Data update (Designated Controller)"

    # Flow 1: classify the specific text-edit subtype
    m = re.search(r"\bSAEP-(\d+)\b", title)
    if m:
        return 1, f"SAEP-{m.group(1)} (Spark proposal)"
    m = re.search(r"\bAEP-(\d+)\b", title)
    if m:
        return 1, f"AEP-{m.group(1)}"
    if "atlas edit proposal" in title_low or "atlas edit weekly" in title_low:
        return 1, "Weekly edit (Atlas Axis)"
    if "spark proposal" in title_low:
        return 1, "Spark proposal (informal)"
    if "saep" in title_low:
        return 1, "Spark proposal (SAEP)"
    # Fallback: if poll exists it's a governance text edit; otherwise housekeeping
    if poll:
        return 1, "Weekly edit (Atlas Axis)"
    return 1, "Housekeeping"


def _extract_date_from_title(title: str) -> str | None:
    m = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", title)
    if m:
        return m.group(1)
    m = re.search(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4}\b", title)
    return m.group(0) if m else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--extracted", required=True)
    ap.add_argument("--pr-meta", required=True)
    args = ap.parse_args()

    extracted = json.loads(Path(args.extracted).read_text())
    pr_meta = json.loads(Path(args.pr_meta).read_text())
    pr_number = int(pr_meta["number"])

    # Load index for UUID → name resolution and number → UUID anchoring
    by_uuid: dict[str, dict] = {}
    number_to_uuid: dict[str, str] = {}
    if INDEX_FILE.exists():
        index = json.loads(INDEX_FILE.read_text())
        by_uuid = {d["uuid"]: d for d in index}
        number_to_uuid = {d["number"]: d["uuid"] for d in index}

    rules = load_routing()

    # Validate anchors: warn (don't fail) if a rule's anchor UUID is missing
    # from the current index — that means the anchored root doc was deleted or
    # replaced upstream and the rule needs re-anchoring. Routing still falls
    # back to the number prefix for that rule.
    if by_uuid:
        for prefix, dirname, anchor in rules:
            if anchor and anchor not in by_uuid:
                print(f"Warning: routing anchor {anchor} for {dirname} "
                      f"(prefix {prefix}) not found in index — re-anchor needed.",
                      file=sys.stderr)
    poll = lookup_poll(pr_number)
    spell = lookup_spell_for_pr(pr_number)
    flow, type_label = classify_governance_flow(pr_meta, extracted, poll, spell)

    # Group documents by entity (routing destination). NR docs route by the
    # number of the parent doc they target, not by their own NR-N which has
    # no scope prefix.
    entity_groups: dict[str, list[str]] = defaultdict(list)
    for doc in extracted["documents"]:
        entity = route_doc_anchored(doc, rules, by_uuid, number_to_uuid)
        doc["entity"] = entity
        entity_groups[entity].append(doc["uuid"])
        doc["reference_renumber_only"] = is_reference_renumber_only(doc)

        # Resolve UUID refs in body deltas
        resolved: dict[str, dict] = {}
        for ref_uuid in (doc["extracted"].get("uuid_refs_before", [])
                         + doc["extracted"].get("uuid_refs_after", [])):
            entry = by_uuid.get(ref_uuid)
            if entry:
                resolved[ref_uuid] = {"number": entry["number"], "name": entry["name"],
                                      "type": entry["type"]}
        doc["extracted"]["uuid_refs_resolved"] = resolved

    # Per-entity sweep partitioning: a sweep belongs to an entity if any of its
    # affected UUIDs route there. The sweep is reported once per entity.
    # `global_uuid_count` preserves the cross-entity scope so the renderer can
    # cite "across N docs" using the global figure even when an entity only
    # contains a subset.
    sweeps_by_entity: dict[str, dict] = defaultdict(lambda: {
        "terminology_sweeps": [],
        "solidity_identifier_fixes": [],
        "article_deletions": [],
    })
    uuid_to_entity = {d["uuid"]: d["entity"] for d in extracted["documents"]}
    for sweep in extracted["patterns"]["terminology_sweeps"]:
        global_count = len(set(sweep["uuids"]))
        entities = {uuid_to_entity.get(u, "_non-content") for u in sweep["uuids"]}
        for e in entities:
            entity_uuids = [u for u in sweep["uuids"] if uuid_to_entity.get(u) == e]
            sweeps_by_entity[e]["terminology_sweeps"].append(
                {**sweep, "uuids": entity_uuids, "global_uuid_count": global_count})
    for sweep in extracted["patterns"]["solidity_identifier_fixes"]:
        global_count = len(set(sweep["uuids"]))
        entities = {uuid_to_entity.get(u, "_non-content") for u in sweep["uuids"]}
        for e in entities:
            entity_uuids = [u for u in sweep["uuids"] if uuid_to_entity.get(u) == e]
            sweeps_by_entity[e]["solidity_identifier_fixes"].append(
                {**sweep, "uuids": entity_uuids, "global_uuid_count": global_count})
    for art in extracted["patterns"]["article_deletions"]:
        entity = uuid_to_entity.get(art["article_uuid"], "_non-content")
        sweeps_by_entity[entity]["article_deletions"].append(art)

    # Build a UUID set that's covered by entity-level patterns so the renderer
    # can suppress per-doc bullets that would duplicate the sweep.
    pattern_covered_uuids: dict[str, set] = defaultdict(set)
    for entity, p in sweeps_by_entity.items():
        for sweep in p["solidity_identifier_fixes"]:
            pattern_covered_uuids[entity].update(sweep["uuids"])
        for sweep in p["terminology_sweeps"]:
            pattern_covered_uuids[entity].update(sweep["uuids"])
        for art in p["article_deletions"]:
            pattern_covered_uuids[entity].add(art["article_uuid"])
            pattern_covered_uuids[entity].update(art.get("subtree_uuids", []))

    # Reference-renumber-only docs are covered by the renderer's entity-level
    # "Reference renumbering across N docs" summary line, not a per-doc bullet,
    # so mark them covered to keep verify-entry's UUID accounting happy.
    for doc in extracted["documents"]:
        if doc.get("reference_renumber_only"):
            pattern_covered_uuids[doc["entity"]].add(doc["uuid"])

    out = {
        "pr_meta": pr_meta,
        "governance_flow": flow,
        "type_label": type_label,
        "poll": poll,
        "spell": spell,
        "entity_groups": dict(entity_groups),
        "documents": extracted["documents"],
        "patterns": extracted["patterns"],
        "patterns_by_entity": dict(sweeps_by_entity),
        "pattern_covered_uuids": {k: sorted(v) for k, v in pattern_covered_uuids.items()},
    }
    json.dump(out, sys.stdout, indent=2, default=str)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
