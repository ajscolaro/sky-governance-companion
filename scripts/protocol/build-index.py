#!/usr/bin/env python3
"""Parse sky-protocol-info overview.md files and emit data/protocol-index.json.

Primary output: by_address (lowercase hex → module + contract name) for spell
contract lookups. Secondary: per-module records with audit history and source repo.
"""

import json
import re
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent.parent
PROTOCOL_REPO = PROJECT_DIR / ".protocol-repo"
OUTPUT = PROJECT_DIR / "data" / "protocol-index.json"

# 0x + 40 hex chars — the only reliable Ethereum address pattern
ADDRESS_RE = re.compile(r'0x[0-9a-fA-F]{40}')
# **Name (0xADDR)** — named contract in bold with address in parens
NAMED_BOLD_RE = re.compile(r'\*\*([^*(]+?)\s*\((' + r'0x[0-9a-fA-F]{40}' + r')\)\*\*')
# GitHub org/repo in backticks or after "at": `org/repo` or "hosted at org/repo"
REPO_RE = re.compile(r'`([\w.-]+/[\w.-]+)`|hosted[^`\n]*?`([\w.-]+/[\w.-]+)`')
# Pinned commit hash in backticks
COMMIT_RE = re.compile(r'`([0-9a-f]{7,64})`')


def parse_overview(path: Path, group: str, component: str) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return {"group": group, "component": component, "error": str(e),
                "contracts": [], "audits": [], "source_repo": None, "pinned_commit": None}

    # --- Contracts ---
    contracts = []
    seen = set()

    # Named contracts first (bold + address in parens)
    for m in NAMED_BOLD_RE.finditer(text):
        name, addr = m.group(1).strip(), m.group(2)
        if addr.lower() not in seen:
            contracts.append({"name": name, "address": addr})
            seen.add(addr.lower())

    # Any remaining bare addresses in the text
    for m in ADDRESS_RE.finditer(text):
        addr = m.group(0)
        if addr.lower() not in seen:
            contracts.append({"name": None, "address": addr})
            seen.add(addr.lower())

    # --- Audits (from ## Security Audits section) ---
    audits = []
    audit_m = re.search(r'##\s+Security Audits\s*\n(.*?)(?=\n##|\Z)', text, re.DOTALL)
    if audit_m:
        section = audit_m.group(1)
        # Bold firm names
        firms = re.findall(r'\*\*([A-Z][^*]{2,40}?)\*\*', section)
        # Dates in parentheses: "April 2025", "March 2025", etc.
        dates = re.findall(r'\(([A-Za-z]+ \d{4})\)', section)
        for i, firm in enumerate(firms):
            audits.append({
                "firm": firm.strip(),
                "date": dates[i] if i < len(dates) else None,
            })

    # --- Source repo (from ## Codebase section) ---
    source_repo = None
    pinned_commit = None
    codebase_m = re.search(r'##\s+Codebase\s*\n(.*?)(?=\n##|\Z)', text, re.DOTALL)
    if codebase_m:
        section = codebase_m.group(1)
        for m in REPO_RE.finditer(section):
            candidate = m.group(1) or m.group(2)
            if candidate and '/' in candidate:
                source_repo = candidate
                break
        # Pinned commit: first long-ish hex hash in backticks in codebase section
        for m in COMMIT_RE.finditer(section):
            h = m.group(1)
            if re.fullmatch(r'[0-9a-f]{7,64}', h):
                pinned_commit = h
                break

    return {
        "group": group,
        "component": component,
        "source_repo": source_repo,
        "pinned_commit": pinned_commit,
        "contracts": contracts,
        "audits": audits,
    }


def main():
    if not PROTOCOL_REPO.exists():
        print(f"ERROR: .protocol-repo not found — run scripts/core/setup.sh first", file=sys.stderr)
        sys.exit(1)

    modules_dir = PROTOCOL_REPO / "modules"
    if not modules_dir.exists():
        print(f"ERROR: modules/ dir missing from .protocol-repo", file=sys.stderr)
        sys.exit(1)

    modules = {}
    by_address = {}
    errors = []

    for overview in sorted(modules_dir.glob("*/*/overview.md")):
        component = overview.parent.name
        group = overview.parent.parent.name
        key = f"{group}/{component}"

        try:
            record = parse_overview(overview, group, component)
            modules[key] = record
            for contract in record["contracts"]:
                addr_lower = contract["address"].lower()
                by_address[addr_lower] = {
                    "module": key,
                    "name": contract["name"],
                }
        except Exception as e:
            errors.append(f"{key}: {e}")

    if errors:
        for err in errors:
            print(f"WARN: {err}", file=sys.stderr)

    OUTPUT.parent.mkdir(exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump({"modules": modules, "by_address": by_address}, f, indent=2)

    contract_count = sum(len(r["contracts"]) for r in modules.values())
    print(f"Protocol index: {len(modules)} modules, {contract_count} contracts → {OUTPUT.relative_to(PROJECT_DIR)}")


if __name__ == "__main__":
    main()
