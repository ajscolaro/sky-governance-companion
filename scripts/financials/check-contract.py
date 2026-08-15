#!/usr/bin/env python3
"""Drift watch for the BA Labs accounting API contract.

Validates that the endpoints scripts/financials/ depends on still return the
shapes documented in docs/financials-api.md. Exits non-zero on any drift so a
scheduled GitHub Actions run fails loudly — the signal that our client/docs need
updating. Also prints the current SkyEco app bundle hash (informational: it
changes on every BA Labs deploy, so it is reported, not asserted).

Usage:
    python3 scripts/financials/check-contract.py            # validate, exit 1 on drift
    python3 scripts/financials/check-contract.py --quiet     # only print on failure
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from financials import FinancialsClient, FinancialsError

SKYECO_URL = "https://financial.skyeco.com/"


def _keys(d: dict, *required: str) -> list[str]:
    return [f"missing key {k!r}" for k in required if k not in d]


def _first(rows) -> dict:
    if not isinstance(rows, list) or not rows or not isinstance(rows[0], dict):
        raise AssertionError(f"expected non-empty list of objects, got {type(rows).__name__}")
    return rows[0]


def build_checks(c: FinancialsClient):
    """(label, thunk) pairs; each thunk returns a list of problem strings."""

    def bs_root():
        d = c.balance_sheet()
        return _keys(d, "date", "totals", "groups") + _keys(d.get("totals", {}), "assets", "liabilities", "held", "info")

    def pnl_root():
        d = c.profit_and_loss()
        return _keys(d, "date_from", "date_to", "totals", "groups") + _keys(d.get("totals", {}), "revenue", "expense", "net")

    def cf_root():
        d = c.cash_flow()
        return _keys(d, "date_from", "date_to", "totals", "groups") + _keys(d.get("totals", {}), "inflows", "outflows", "net")

    def bs_latest():
        row = _first(c.balance_sheet_items_latest())
        return _keys(row, "uid", "balance", "item_type", "block_number", "datetime")

    def bs_hist():
        row = _first(c.headline_history("balance-sheet", group_by="month"))
        return _keys(row, "date", "item_type", "balance")

    def pnl_hist():
        row = _first(c.headline_history("profit-and-loss", group_by="month"))
        return _keys(row, "date", "revenue", "expense", "net")

    def cf_hist():
        row = _first(c.headline_history("cash-flow", group_by="month"))
        return _keys(row, "date", "opening", "inflows", "outflows", "net", "closing_computed")

    def events():
        d = c.events(limit=2)
        probs = _keys(d, "results", "pagination")
        if isinstance(d.get("results"), list) and d["results"]:
            probs += _keys(d["results"][0], "tx_hash", "amount", "event", "block_number")
        return probs

    def group_by_week_rejected():
        # Contract: week is not a valid granularity. If it starts succeeding, our
        # VALID_GROUP_BY set is stale — worth knowing.
        try:
            c.headline_history("profit-and-loss", group_by="week")
        except ValueError:
            return []  # our own guard rejected it before the request — fine
        return ["group_by=week no longer rejected by the client guard"]

    return [
        ("balance-sheet/", bs_root),
        ("profit-and-loss/", pnl_root),
        ("cash-flow/", cf_root),
        ("balance-sheet/items/latest/", bs_latest),
        ("balance-sheet/history/", bs_hist),
        ("profit-and-loss/statement/history/", pnl_hist),
        ("cash-flow/statement/history/", cf_hist),
        ("cash-flow/events/", events),
        ("group_by=week rejected", group_by_week_rejected),
    ]


def bundle_hash() -> str | None:
    try:
        req = urllib.request.Request(SKYECO_URL, headers={"User-Agent": "sky-governance-companion/drift"})
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
        m = re.search(r"/assets/(index-[A-Za-z0-9_-]+\.js)", html)
        return m.group(1) if m else None
    except Exception:
        return None


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate the BA Labs accounting API contract.")
    ap.add_argument("--quiet", action="store_true", help="print only on failure")
    args = ap.parse_args()

    client = FinancialsClient()
    failures: list[str] = []
    for label, thunk in build_checks(client):
        try:
            problems = thunk()
        except (FinancialsError, AssertionError) as e:
            problems = [str(e)]
        if problems:
            failures.append(f"  {label}: {'; '.join(problems)}")
        elif not args.quiet:
            print(f"  ok  {label}")

    bh = bundle_hash()
    if not args.quiet:
        print(f"\nSkyEco app bundle: {bh or 'unknown'} (informational — changes each deploy)")

    if failures:
        print("\nCONTRACT DRIFT DETECTED — update scripts/financials/ + docs/financials-api.md:")
        print("\n".join(failures))
        return 1
    if not args.quiet:
        print("\nContract OK — all depended-on shapes present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
