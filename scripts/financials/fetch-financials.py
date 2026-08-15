#!/usr/bin/env python3
"""Refresh the cached Sky financial statements from the BA Labs accounting API.

Writes a point-in-time snapshot of the three statements plus the block-stamped
balance-sheet item balances to data/financials/ as JSON. Called by /refresh
(scripts/core/refresh.sh) with --quiet; also runnable standalone.

The snapshot is deliberately the *live* current state (no history) — history is
fetched on demand by the query layer. Data source + full contract:
docs/financials-api.md. Figures are BA Labs / SkyEco, not an official statement.

Usage:
    python3 scripts/financials/fetch-financials.py            # fetch + summary
    python3 scripts/financials/fetch-financials.py --quiet    # silent (startup/refresh)
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from financials import CACHE_DIR, FinancialsClient, FinancialsError, fmt_usd


def _write(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False))


def main() -> int:
    ap = argparse.ArgumentParser(description="Refresh cached Sky financial statements.")
    ap.add_argument("--quiet", action="store_true", help="suppress output")
    args = ap.parse_args()

    def say(msg: str) -> None:
        if not args.quiet:
            print(msg)

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    fetched_at = datetime.now(timezone.utc).isoformat()

    try:
        snap = FinancialsClient().live_snapshot(fetched_at)
    except FinancialsError as e:
        # Network/API failure must not abort the whole /refresh run; the other
        # data sources are independent. Report and leave any prior cache intact.
        print(f"financials: fetch failed ({e}); keeping previous cache", file=sys.stderr)
        return 1

    _write(CACHE_DIR / "balance-sheet.json", snap["balance_sheet"])
    _write(CACHE_DIR / "profit-and-loss.json", snap["profit_and_loss"])
    _write(CACHE_DIR / "cash-flow.json", snap["cash_flow"])
    _write(CACHE_DIR / "balance-sheet-items-latest.json", snap["balance_sheet_items_latest"])
    _write(CACHE_DIR / "_meta.json", {
        "source": "BA Labs / Block Analitica accounting API",
        "attribution": "per BA Labs / SkyEco — not an official protocol statement",
        "fetched_at": fetched_at,
        "block_number": snap["block_number"],
        "endpoints": [
            "/v1/accounting/balance-sheet/",
            "/v1/accounting/profit-and-loss/",
            "/v1/accounting/cash-flow/",
            "/v1/accounting/balance-sheet/items/latest/",
        ],
    })

    bs = snap["balance_sheet"].get("totals", {})
    pnl = snap["profit_and_loss"].get("totals", {})
    cf = snap["cash_flow"].get("totals", {})
    say("Financials snapshot refreshed (BA Labs / SkyEco):")
    say(f"  Balance sheet @ {snap['balance_sheet'].get('date')} "
        f"(block {snap['block_number']}): assets {fmt_usd(bs.get('assets'))}, "
        f"liabilities {fmt_usd(bs.get('liabilities'))}")
    say(f"  P&L (life-to-date): revenue {fmt_usd(pnl.get('revenue'))}, "
        f"expense {fmt_usd(pnl.get('expense'))}, net {fmt_usd(pnl.get('net'))}")
    say(f"  Cash flow (life-to-date): inflows {fmt_usd(cf.get('inflows'))}, "
        f"outflows {fmt_usd(cf.get('outflows'))}, net {fmt_usd(cf.get('net'))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
