#!/usr/bin/env python3
"""Render enriched PR data into per-entity changelog entries.

Stage 4 of the auto-changelog pipeline. Reads the Stage 3 enrichment JSON
(--enriched <path>) and emits a fenced JSON document containing the rendered
markdown entry for each affected entity:

{
  "pr_number": ...,
  "merged_date": "YYYY-MM-DD",
  "type_label": "...",
  "entries": {
    "<entity-dir>": "<markdown entry>",
    ...
  },
  "summary": {
    "<entity-dir>": {"material_count": N, "housekeeping_count": M, "context_omitted": True}
  }
}

The renderer never invents content. Every bullet is derived from a structural
signal in the diff. Material vs. Housekeeping classification is rule-based.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent

# --- Helpers ---------------------------------------------------------------

def short_uuid(uuid: str | None) -> str:
    if not uuid:
        return ""
    if len(uuid) >= 12:
        return f"{uuid[:8]}…{uuid[-4:]}"
    return uuid


def is_active_data(doc: dict) -> bool:
    return (doc.get("type") or "").strip() == "Active Data"


def has_substantive_body(doc: dict) -> bool:
    """Did this added doc carry real content (vs. a pure index/scaffold)?"""
    if doc["kind"] != "added":
        return False
    lead = (doc["extracted"].get("lead_sentence") or "").strip()
    return len(lead) > 30


def find_addition_roots(docs: list[dict]) -> dict[str, list[dict]]:
    """For added docs, find tree roots: a doc is a root if no shorter ancestor
    docNo also appears in the added set. Returns {root_uuid: [descendant_docs]}.
    """
    added = [d for d in docs if d["kind"] == "added" and d.get("number")]
    by_number = {d["number"]: d for d in added}
    roots: dict[str, list[dict]] = {}
    for d in added:
        n = d["number"]
        # Walk up parent prefixes; if any ancestor is in `added`, this is not a root
        parts = n.split(".")
        is_root = True
        for k in range(2, len(parts)):
            anc = ".".join(parts[:k])
            if anc in by_number:
                is_root = False
                break
        if is_root:
            descendants = [x for x in added if x["number"] != n
                           and x["number"].startswith(n + ".")]
            roots[d["uuid"]] = descendants
    return roots


# --- Bullet templates ------------------------------------------------------

def _format_addresses(addrs: list[str]) -> str:
    if not addrs:
        return ""
    return ", ".join(f"`{a}`" for a in sorted(set(addrs)))


def _format_dates(dates: list[str]) -> str:
    return ", ".join(sorted(set(dates))) if dates else ""


_MD_UUID_LINK_RE = re.compile(r"\[([^\]]+)\]\(([0-9a-f-]{36})\)")


def _clean_lead(lead: str, resolved: dict) -> str:
    """Convert markdown-UUID links in a lead sentence into bare doc-number refs.

    The Atlas atomized format embeds cross-references as `[A.x.y - Name](uuid)`.
    For changelog readers this expands to ugly inline UUIDs; replace each link
    with its resolved doc number in backticks.
    """
    def repl(m: re.Match) -> str:
        ref_uuid = m.group(2)
        info = resolved.get(ref_uuid) or {}
        number = info.get("number")
        if number:
            return f"`{number}`"
        # Fall back to short UUID if no resolution
        return f"`{short_uuid(ref_uuid)}`"
    return _MD_UUID_LINK_RE.sub(repl, lead)


def render_addition(doc: dict, descendants: list[dict]) -> tuple[str, list[str]]:
    """Render a 'New entity' bullet plus optional sub-bullets pulled from descendants.

    Returns (main_bullet, [sub_bullets]).
    """
    name = (doc.get("name") or "").strip()
    number = doc.get("number") or ""
    uuid_short = short_uuid(doc["uuid"])
    lead = (doc["extracted"].get("lead_sentence") or "").strip()
    lead = _clean_lead(lead, doc["extracted"].get("uuid_refs_resolved", {}))
    # Trim trailing dot/colon/semicolons; render expects flowing text
    lead = lead.rstrip(".;: ")
    main = f"**New: {name}** (`{number}`, UUID `{uuid_short}`)"
    if lead:
        main += f": {lead}."

    # Surface key facts from THIS doc directly — useful for ICD / parameter
    # docs where the meaningful content is the addresses + dates + values, not
    # the lead-sentence prose. Skip if already in the lead (avoids duplicates).
    own_ext = doc.get("extracted") or {}
    own_facts: list[str] = []
    own_addrs = sorted(set(own_ext.get("addresses_after", []))
                       - set(re.findall(r"0x[a-fA-F0-9]{40}", lead)))
    if own_addrs:
        own_facts.append(f"address{'es' if len(own_addrs) > 1 else ''}: "
                         + ", ".join(f"`{a}`" for a in own_addrs))
    own_dates = sorted(set(own_ext.get("dates_after", []))
                       - set(re.findall(r"\d{4}-\d{2}-\d{2}", lead)))
    if own_dates:
        own_facts.append(f"date{'s' if len(own_dates) > 1 else ''}: "
                         + ", ".join(own_dates))
    if own_facts:
        # Append as a parenthetical to keep the bullet on one logical line
        main += f" ({'; '.join(own_facts)})"

    subs: list[str] = []
    # Gather all key facts from descendants — addresses, numerics with units, dates
    addr_set: set[str] = set()
    date_set: set[str] = set()
    uuid_ref_set: set[tuple[str, str]] = set()  # (uuid, name)
    for desc in descendants:
        ext = desc["extracted"]
        addr_set.update(ext.get("addresses_after", []))
        date_set.update(ext.get("dates_after", []))
        for ref_uuid, info in ext.get("uuid_refs_resolved", {}).items():
            uuid_ref_set.add((ref_uuid, info["name"]))

    # Per-descendant child bullets, only when the lead sentence carries a value
    for desc in sorted(descendants, key=lambda d: d.get("number") or ""):
        d_lead = (desc["extracted"].get("lead_sentence") or "").strip()
        d_name = (desc.get("name") or "").strip()
        d_number = desc.get("number") or ""
        if not d_lead:
            continue
        # Skip pure scaffold parents (those whose children carry the substance)
        if d_lead.lower().startswith(("the subdocuments herein",
                                      "the documents herein",
                                      "the subdocuments")):
            continue
        d_lead = _clean_lead(d_lead, desc["extracted"].get("uuid_refs_resolved", {}))
        d_lead = d_lead.rstrip(".;: ")
        subs.append(f"**{d_name}** (`{d_number}`): {d_lead}.")

    return main, subs


def render_deletion(doc: dict) -> str:
    name = (doc.get("name") or "").strip()
    number = doc.get("number") or ""
    dtype = (doc.get("type") or "").strip()
    uuid_short = short_uuid(doc["uuid"])
    return f"**{dtype} {number} deleted: {name}** (UUID `{uuid_short}`)"


def render_article_deletion(art: dict, all_docs: list[dict]) -> str:
    """Article deletion bullet, naming any deleted Core leaf docs in the subtree."""
    name = art.get("article_name", "")
    number = art.get("article_number", "")
    sub_count = art.get("subtree_count", 0)
    sub_uuids = set(art.get("subtree_uuids", []))

    # Pull names of deleted Core docs (the substantive leaves) for context
    leaf_summaries = []
    for d in all_docs:
        if d["kind"] != "deleted":
            continue
        if d["uuid"] not in sub_uuids:
            continue
        if (d.get("type") or "") == "Core":
            leaf_name = (d.get("name") or "").strip()
            leaf_num = d.get("number") or ""
            if leaf_name:
                leaf_summaries.append(f"`{leaf_num}` {leaf_name}")

    out = f"**Article {number} deleted: {name}**"
    if leaf_summaries:
        out += f" (incl. {'; '.join(leaf_summaries)})"
    out += f" — {sub_count} descendant doc{'s' if sub_count != 1 else ''} removed"
    return out


def render_solidity_fix_group(fixes: list[dict]) -> str:
    """One-line summary of all Solidity identifier whitespace fixes for an entity.

    Cites the number of distinct entity-local docs touched but lists every
    distinct identifier pair (which spans all entities). Counts come from the
    enrichment record so the bullet stays accurate even when a given entity
    only saw some of the patterns.
    """
    if not fixes:
        return ""
    n_docs_local = len({u for f in fixes for u in f["uuids"]})
    pairs = ", ".join(f"`{f['old']}` → `{f['new']}`" for f in fixes)
    return (f"Solidity identifier whitespace fix across {n_docs_local} doc"
            f"{'s' if n_docs_local != 1 else ''} ({pairs}).")


def render_terminology_sweep(sweep: dict) -> str:
    n_docs = len(set(sweep["uuids"]))
    return f"`{sweep['old']}` → `{sweep['new']}` across {n_docs} doc{'s' if n_docs != 1 else ''}."


def render_rename(doc: dict) -> str:
    nc = doc.get("name_change") or {}
    if not nc:
        return ""
    number = doc.get("number") or ""
    return f"`{number}` renamed: \"{nc.get('old')}\" → \"{nc.get('new')}\""


def render_modification(doc: dict, pattern_covered: set | None = None) -> tuple[str | None, str]:
    """Render a single modified doc bullet.

    Returns (bullet_text, classification): classification is "material" or
    "housekeeping". None bullet means the change is captured by an entity-level
    pattern and shouldn't be repeated as a per-doc bullet.
    """
    ext = doc["extracted"]
    name = (doc.get("name") or "").strip()
    number = doc.get("number") or ""
    pairs = ext.get("paired_changes", [])
    nc = doc.get("name_change")

    # Skip noisy single-character whitespace deltas — these are diff-format artifacts
    pairs = [p for p in pairs if (p["before"] or p["after"])]

    # If only the name (frontmatter) changed and no body deltas, render as rename
    if nc and not pairs:
        return render_rename(doc), "housekeeping"

    # If every paired change is a Solidity identifier fix, defer to the entity sweep
    if pairs and all(p.get("pattern") == "solidity_identifier" for p in pairs):
        return None, "housekeeping"

    # If this doc is fully covered by an entity-level terminology sweep, skip
    # (otherwise we'd emit redundant per-doc bullets alongside the sweep)
    if pattern_covered and doc["uuid"] in pattern_covered:
        # Only suppress if all paired changes match the swept pattern's pair
        # (we keep doc-level bullets when the doc has additional unique edits)
        sweep_subs = {(p["before"], p["after"]) for p in pairs
                      if p["kind"] == "sub" and p.get("pattern") != "general"}
        if pairs and all((p["before"], p["after"]) in sweep_subs
                         for p in pairs if p["kind"] == "sub"):
            return None, "housekeeping"

    # Active Data row insertions — pipe-delimited table rows
    inserts = [p for p in pairs if p["kind"] == "insert" and "|" in p["after"]]
    if inserts and is_active_data(doc):
        # Strip header/separator rows, keep data rows
        data_rows = [p["after"].strip() for p in inserts
                     if not re.match(r"^\|[\s\-:]+\|", p["after"])]
        # The first kept row is usually the header; keep it for context
        if data_rows:
            row = data_rows[-1]  # most recent data row
            return f"**Registry row added** in {name} (`{number}`): {row}", "material"

    # TBD resolutions are material
    tbd = ext.get("tbd_resolutions", [])
    if tbd:
        bits = "; ".join(f"`{t['label']}`: TBD → `{t['after']}`" for t in tbd)
        return f"**{name}** (`{number}`): {bits}", "material"

    # Address changes are material
    if ext.get("addresses_after") and ext.get("addresses_after") != ext.get("addresses_before"):
        addrs = _format_addresses(ext["addresses_after"])
        return f"**{name}** (`{number}`): address {addrs}", "material"

    # Numeric / parameter changes — surface every value pair, not just up to 3.
    # Pairs that are pure numeric values (with optional units) carry the
    # signal a spell-recording reader needs (rate limits, LTV, slope, etc.).
    # We split this into two flavors: explicit parameter pairs (high signal)
    # vs. any-pair-containing-a-digit (broader catch).
    PARAMETER_PAIR_RE = re.compile(
        r"^-?\d{1,3}(?:[,\d]*\.?\d*|\.\d+)\s*"
        r"(?:%|million|billion|bps|hours?|hrs?|days?|seconds?|sec|years?|"
        r"[MBK]\b|USD|USDS|DAI|SKY|sUSDS|ETH|BTC|USDC|USDT)?\s*"
        r"(?:per\s+(?:day|hour|year|second))?$",
        re.IGNORECASE,
    )

    def _is_parameter_pair(p: dict) -> bool:
        if p.get("kind") != "sub":
            return False
        b, a = p.get("before", "").strip(), p.get("after", "").strip()
        return bool(PARAMETER_PAIR_RE.match(b) and PARAMETER_PAIR_RE.match(a))

    parameter_subs = [p for p in pairs if _is_parameter_pair(p)]
    if parameter_subs:
        # All parameter changes for this doc go on a single bullet.
        bits = "; ".join(f"`{p['before']}` → `{p['after']}`" for p in parameter_subs)
        return f"**{name}** (`{number}`): {bits}", "material"

    # Broader numeric fallback: any sub where both sides contain digits.
    # Useful for parameter docs whose values include extra prose ("250M / 100M
    # per day"). Still uncapped — readers want the full delta, not a sample.
    numeric_subs = [p for p in pairs
                    if p["kind"] == "sub"
                    and re.search(r"\d", p.get("before", ""))
                    and re.search(r"\d", p.get("after", ""))]
    if numeric_subs:
        bits = "; ".join(f"`{p['before']}` → `{p['after']}`" for p in numeric_subs)
        return f"**{name}** (`{number}`): {bits}", "material"

    # Authority/role rename in body
    role_subs = [p for p in pairs if p.get("pattern") == "role_or_authority"]
    if role_subs:
        bits = "; ".join(f"`{p['before']}` → `{p['after']}`" for p in role_subs[:2])
        return f"`{number}` ({name}): {bits}", "housekeeping"

    # Cross-reference removal/addition
    refs_lost = (set(ext.get("uuid_refs_before", []))
                 - set(ext.get("uuid_refs_after", [])))
    refs_gained = (set(ext.get("uuid_refs_after", []))
                   - set(ext.get("uuid_refs_before", [])))
    resolved = ext.get("uuid_refs_resolved", {})
    if refs_lost or refs_gained:
        bits: list[str] = []
        if refs_lost:
            names = [resolved.get(u, {}).get("number", short_uuid(u)) for u in refs_lost]
            bits.append(f"removed refs to {', '.join(f'`{n}`' for n in names)}")
        if refs_gained:
            names = [resolved.get(u, {}).get("number", short_uuid(u)) for u in refs_gained]
            bits.append(f"added refs to {', '.join(f'`{n}`' for n in names)}")
        return f"`{number}` ({name}): {'; '.join(bits)}", "housekeeping"

    # Generic content edit — describe the most informative paired change.
    # Prefer subs over inserts/deletes; prefer pairs with text on both sides.
    pairs_sub = [p for p in pairs if p["kind"] == "sub"]
    pairs_delete = [p for p in pairs if p["kind"] == "delete" and p["before"]]
    pairs_insert = [p for p in pairs if p["kind"] == "insert" and p["after"]]
    if pairs_sub:
        best = pairs_sub[0]
        return (f"`{number}` ({name}): `{best['before']}` → `{best['after']}`"
                if (len(best["before"]) + len(best["after"])) < 200
                else f"`{number}` ({name}): text replacement (see diff)"), "housekeeping"
    if pairs_delete:
        snippet = pairs_delete[0]["before"]
        if len(snippet) > 140:
            snippet = snippet[:140] + "…"
        return f"`{number}` ({name}): removed `{snippet}`", "housekeeping"
    if pairs_insert:
        snippet = pairs_insert[0]["after"]
        if len(snippet) > 140:
            snippet = snippet[:140] + "…"
        return f"`{number}` ({name}): added `{snippet}`", "housekeeping"
    return f"`{number}` ({name}): content edit", "housekeeping"


# --- Per-entity assembly ---------------------------------------------------

def render_entity_entry(entity: str, enriched: dict) -> tuple[str, dict]:
    """Build the markdown entry for one entity. Returns (markdown, summary_dict)."""
    pr_meta = enriched["pr_meta"]
    pr_number = pr_meta["number"]
    title = pr_meta["title"]
    merged_date = (pr_meta.get("merged_at") or "")[:10]
    type_label = enriched["type_label"]
    poll = enriched.get("poll")

    docs = [d for d in enriched["documents"] if d.get("entity") == entity]
    patterns = enriched["patterns_by_entity"].get(entity, {})
    sol_fixes = patterns.get("solidity_identifier_fixes", [])
    term_sweeps = patterns.get("terminology_sweeps", [])
    article_dels = patterns.get("article_deletions", [])

    # Identify addition roots once
    addition_roots = find_addition_roots(docs)
    descendants_uuid_set = {x["uuid"] for ds in addition_roots.values() for x in ds}

    material: list[str] = []
    housekeeping: list[str] = []

    # 1. Article deletions (largest semantic event)
    for art in article_dels:
        material.append(render_article_deletion(art, enriched["documents"]))
    deleted_in_article = {u for art in article_dels for u in art.get("subtree_uuids", [])}
    deleted_in_article |= {art["article_uuid"] for art in article_dels}

    # 2. Standalone deletions (Core/Section docs not part of an Article deletion)
    for d in docs:
        if d["kind"] == "deleted" and d["uuid"] not in deleted_in_article:
            material.append(render_deletion(d))

    # 3. Additions: render roots; descendants accounted for in the root bullet
    seen_addition_uuids: set[str] = set()
    for d in docs:
        if d["kind"] != "added":
            continue
        if d["uuid"] in descendants_uuid_set:
            continue
        if d["uuid"] in seen_addition_uuids:
            continue
        descendants = addition_roots.get(d["uuid"], [])
        main, subs = render_addition(d, descendants)
        # Indent sub-bullets under the main one
        block = main
        if subs:
            block += "\n" + "\n".join(f"  - {s}" for s in subs)
        material.append(block)
        seen_addition_uuids.add(d["uuid"])
        for x in descendants:
            seen_addition_uuids.add(x["uuid"])

    # 4. Modified docs
    pattern_covered = set(enriched.get("pattern_covered_uuids", {}).get(entity, []))
    for d in docs:
        if d["kind"] != "modified":
            continue
        bullet, cls = render_modification(d, pattern_covered=pattern_covered)
        if bullet is None:
            continue
        (material if cls == "material" else housekeeping).append(bullet)

    # 5. Renamed-only (frontmatter docNo change)
    for d in docs:
        if d["kind"] == "renamed":
            number = d.get("number") or ""
            housekeeping.append(f"`{number}` renumbered (UUID stable: `{short_uuid(d['uuid'])}`)")

    # 6. Entity-level pattern bullets
    if sol_fixes:
        housekeeping.append(render_solidity_fix_group(sol_fixes))
    for sweep in term_sweeps:
        housekeeping.append(render_terminology_sweep(sweep))

    # --- Render markdown -----------------------------------------------
    lines: list[str] = []
    lines.append(f"## PR #{pr_number} — {title}")
    lines.append(f"**Merged:** {merged_date} | **Type:** {type_label}")

    # Flow 2 cross-PR linking: cite the authorizing governance polls (and any
    # Flow 1 Atlas PRs they pre-authorized) on a sub-line right under the
    # header. Prefer polls with cached results — old spells may list many
    # polls predating the vote-matrix cache, so trim aggressively.
    spell = enriched.get("spell")
    if spell and (spell.get("authorizing_polls") or spell.get("date")):
        bits: list[str] = []
        polls = spell.get("authorizing_polls") or []
        if polls:
            POLL_CAP = 5
            with_results = [p for p in polls if p.get("result")]
            chosen = with_results if with_results else polls
            poll_strs: list[str] = []
            for p in chosen[:POLL_CAP]:
                marker = f"#{p['poll_id']}"
                if p.get("result"):
                    marker += f" ({p['result']})"
                if p.get("atlas_pr"):
                    marker += f" → PR #{p['atlas_pr']}"
                poll_strs.append(marker)
            label = "polls"
            if len(chosen) > POLL_CAP:
                poll_strs.append(f"+{len(chosen) - POLL_CAP} more")
            bits.append(f"{label}: {', '.join(poll_strs)}")
        if spell.get("date"):
            bits.append(f"spell cast {spell['date']}")
        if bits:
            lines.append(f"**Authorizing:** {' · '.join(bits)}")
    lines.append("")
    if material:
        lines.append("### Material Changes")
        for b in material:
            lines.append(f"- {b}")
        lines.append("")
    if housekeeping:
        lines.append("### Housekeeping")
        for b in housekeeping:
            lines.append(f"- {b}")
        lines.append("")
    # Context section is left empty; auto-context.py optionally fills it
    lines.append("### Context")
    lines.append("<!-- context: pending auto-context -->")
    lines.append("")
    lines.append("---")

    summary = {
        "material_count": len(material),
        "housekeeping_count": len(housekeeping),
        "doc_count": len(docs),
        "poll_id": (poll or {}).get("poll_id"),
    }
    return "\n".join(lines), summary


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--enriched", required=True)
    args = ap.parse_args()

    enriched = json.loads(Path(args.enriched).read_text())
    pr_meta = enriched["pr_meta"]

    entries: dict[str, str] = {}
    summary: dict[str, dict] = {}
    for entity in enriched["entity_groups"]:
        text, s = render_entity_entry(entity, enriched)
        entries[entity] = text
        summary[entity] = s

    out = {
        "pr_number": pr_meta["number"],
        "merged_date": (pr_meta.get("merged_at") or "")[:10],
        "type_label": enriched["type_label"],
        "governance_flow": enriched["governance_flow"],
        "entries": entries,
        "summary": summary,
        "poll": enriched.get("poll"),
        "spell": enriched.get("spell"),
    }
    json.dump(out, sys.stdout, indent=2, default=str)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
