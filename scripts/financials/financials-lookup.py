#!/usr/bin/env python3
"""CLI over the cached Sky financial statements (BA Labs / SkyEco).

Reads the JSON snapshot + monthly SQLite store written by fetch-financials.py;
`daily` alone goes live (daily granularity is fetched on demand, not stored).
This is the entry point the /protocol-financials skill drives. Full contract:
docs/financials-api.md. Figures are BA Labs / SkyEco — not an official statement.

Usage:
    python3 scripts/financials/financials-lookup.py snapshot
    python3 scripts/financials/financials-lookup.py metrics cash-flow
    python3 scripts/financials/financials-lookup.py series profit-and-loss net [--start 2025-01] [--end 2026-08]
    python3 scripts/financials/financials-lookup.py overlay profit-and-loss net 2026-03 [--before 3] [--after 3]
    python3 scripts/financials/financials-lookup.py daily cash-flow net --start 2026-07-01 --end 2026-07-31
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from financials import (
    STATEMENTS, STORED_STATEMENTS, FinancialsCache, FinancialsClient, FinancialsDB,
    etherscan_tx, fmt_metric, fmt_usd, normalize_headline,
)

ATTRIB = "Source: BA Labs / SkyEco (not an official protocol statement)."


def cmd_snapshot(_args) -> int:
    c = FinancialsCache()
    m = c.meta()
    bs, pnl, cf = c.balance_sheet(), c.profit_and_loss(), c.cash_flow()
    bt, pt, ct = bs.get("totals", {}), pnl.get("totals", {}), cf.get("totals", {})
    print(f"Financials snapshot — fetched {m.get('fetched_at')} (block {m.get('block_number')})")
    print(f"  Balance sheet @ {bs.get('date')}: assets {fmt_usd(bt.get('assets'))}, "
          f"liabilities {fmt_usd(bt.get('liabilities'))}, held {fmt_usd(bt.get('held'))}")
    print(f"  P&L (life-to-date): revenue {fmt_usd(pt.get('revenue'))}, "
          f"expense {fmt_usd(pt.get('expense'))}, net {fmt_usd(pt.get('net'))}")
    print(f"  Cash flow (life-to-date): inflows {fmt_usd(ct.get('inflows'))}, "
          f"outflows {fmt_usd(ct.get('outflows'))}, net {fmt_usd(ct.get('net'))}")
    print(ATTRIB)
    return 0


def cmd_metrics(args) -> int:
    db = FinancialsDB()
    print(f"{args.statement} metrics: {', '.join(db.metrics(args.statement))}")
    row = db.conn.execute(
        "SELECT MIN(date), MAX(date) FROM financials_monthly WHERE statement = ?",
        (args.statement,),
    ).fetchone()
    if row and row[0]:
        print(f"coverage: {row[0]} .. {row[1]}")
    return 0


def cmd_series(args) -> int:
    db = FinancialsDB()
    rows = db.series(args.statement, args.metric, args.start, args.end)
    if not rows:
        print(f"No data for {args.statement}/{args.metric}. "
              f"Metrics: {', '.join(db.metrics(args.statement))}")
        return 1
    print(f"{args.statement} / {args.metric} (monthly):")
    for d, v in rows:
        print(f"  {d}  {fmt_metric(args.metric, v):>12}")
    print(ATTRIB)
    return 0


def cmd_overlay(args) -> int:
    db = FinancialsDB()
    r = db.around(args.statement, args.metric, args.month, args.before, args.after)
    if not r["series"]:
        print(f"No monthly data around {args.month} for {args.statement}/{args.metric}.")
        return 1
    print(f"{args.statement} / {args.metric} around {r['month']} "
          f"(-{args.before}/+{args.after} months):")
    for d, v in r["series"]:
        mark = "  <-- " + args.month if d == r["month"] else ""
        print(f"  {d}  {fmt_metric(args.metric, v):>12}{mark}")
    if r["change_pct"] is not None:
        print(f"  window change: {r['change_pct']:+.2f}%")
    print(ATTRIB)
    return 0


def cmd_daily(args) -> int:
    # Live: daily granularity is not persisted, fetched on demand from the API.
    rows = normalize_headline(
        args.statement,
        FinancialsClient().headline_history(args.statement, group_by="day",
                                            date_from=args.start, date_to=args.end),
    )
    want = [(d, v) for d, metric, v in rows if metric == args.metric]
    if not want:
        metrics = sorted({m for _, m, _ in rows})
        print(f"No daily data for {args.statement}/{args.metric}. Metrics: {', '.join(metrics)}")
        return 1
    print(f"{args.statement} / {args.metric} (daily, live):")
    for d, v in want:
        print(f"  {d}  {fmt_usd(v):>12}")
    print(ATTRIB)
    return 0


def cmd_events(args) -> int:
    # Live drill-down: onchain cash-flow txs. Date filter is server-side; a bare
    # call spans ~760k rows, so a date range is effectively required.
    if not (args.start or args.end):
        print("events: pass --start/--end (the feed is ~760k rows without a date filter).")
        return 1
    rows, total = FinancialsClient().events_range(
        date_from=args.start, date_to=args.end,
        category=args.category, source=args.source, max_events=args.limit,
    )
    if not rows:
        print(f"No events for {args.start}..{args.end}"
              + (f" category={args.category}" if args.category else "")
              + (f" source={args.source}" if args.source else ""))
        return 1
    filt = "".join(f" {k}={v}" for k, v in (("category", args.category), ("source", args.source)) if v)
    print(f"cash-flow events {args.start}..{args.end}{filt} — showing {len(rows)} "
          f"(of {total} in date range):")
    for e in rows:
        print(f"  {e.get('datetime')}  {e.get('event'):<5} {fmt_usd(e.get('amount')):>11}  "
              f"{e.get('category')} / {e.get('source')}")
        print(f"       {etherscan_tx(e.get('tx_hash'))}")
    if total and len(rows) < total:
        print(f"  ... {total - len(rows)} more in range not shown (raise --limit or narrow the dates)")
    print(ATTRIB)
    return 0


KPI_GROUPS = [
    ("Profitability (TTM)", ["ttm_revenue", "ttm_expense", "ttm_net_income", "ttm_nii",
                             "ttm_buyback", "ttm_distributions"]),
    ("Returns & margins", ["roa", "roe", "net_margin", "gross_yield", "cost_of_funds",
                           "nim", "earnings_yield"]),
    ("Capital & balance sheet", ["total_assets", "total_liabilities", "sky_capital",
                                 "backstop_capital", "equity_ratio", "leverage",
                                 "collateralization", "backstop_coverage"]),
    ("Valuation", ["market_cap", "sky_price", "pe_ratio", "ps_ratio", "pb_ratio", "eps",
                   "nav_per_sky", "buyback_yield"]),
    ("Growth (YoY)", ["revenue_yoy", "net_income_yoy", "assets_yoy", "deposits_yoy"]),
]


def cmd_kpis(_args) -> int:
    k = FinancialsCache().kpis()
    print(f"Derived KPIs @ {k.get('date')} — bank-style view; TTM = trailing 12 months.")
    print("(raw revenue/expense here are interest income/expense, NOT the /v1 P&L totals)")
    for title, keys in KPI_GROUPS:
        print(f"  {title}:")
        for m in keys:
            if m in k:
                print(f"    {m:22s} {fmt_metric(m, k[m]):>14}")
    print("  (full 61-field object in data/financials/kpis.json)")
    print(ATTRIB)
    return 0


def cmd_settlements(_args) -> int:
    cycles = FinancialsCache().settlement_cycles()
    if not cycles:
        print("No settlement cycles cached.")
        return 1
    print(f"Monthly Settlement Cycles ({len(cycles)}):")
    for c in cycles:
        print(f"  {c.get('name')}  {c.get('reporting_start_date')}..{c.get('reporting_end_date')}  "
              f"settled {c.get('settled_date')}")
        print(f"     income {fmt_usd(c.get('income'))}, expenses {fmt_usd(c.get('expenses'))}, "
              f"net profit {fmt_usd(c.get('net_profit'))}")
        if c.get("forum_link"):
            print(f"     forum: {c['forum_link']}")
        if c.get("vote_link"):
            print(f"     vote:  {c['vote_link']}")
        if c.get("exec_tx_hash"):
            print(f"     exec:  {etherscan_tx(c['exec_tx_hash'])}")
    print(ATTRIB)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Query cached Sky financial statements.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("snapshot", help="current statement summary from cache")
    sub.add_parser("kpis", help="latest derived KPIs (TTM/ROA/ROE/valuation)")
    sub.add_parser("settlements", help="Monthly Settlement Cycles + governance links")

    p = sub.add_parser("metrics", help="list available metrics for a statement")
    p.add_argument("statement", choices=STORED_STATEMENTS)

    p = sub.add_parser("series", help="monthly series for a metric ('kpis' allowed)")
    p.add_argument("statement", choices=STORED_STATEMENTS)
    p.add_argument("metric")
    p.add_argument("--start")
    p.add_argument("--end")

    p = sub.add_parser("overlay", help="metric window around a month (governance overlay)")
    p.add_argument("statement", choices=STORED_STATEMENTS)
    p.add_argument("metric")
    p.add_argument("month", help="YYYY-MM (or YYYY-MM-DD, truncated)")
    p.add_argument("--before", type=int, default=3)
    p.add_argument("--after", type=int, default=3)

    p = sub.add_parser("daily", help="daily series for a metric (live, on-demand)")
    p.add_argument("statement", choices=STATEMENTS)
    p.add_argument("metric")
    p.add_argument("--start")
    p.add_argument("--end")

    p = sub.add_parser("events", help="onchain cash-flow event drill-down (live)")
    p.add_argument("--start", help="YYYY-MM-DD (effectively required)")
    p.add_argument("--end", help="YYYY-MM-DD")
    p.add_argument("--category", help="e.g. 'Savings Payouts', 'Collateral Stability Fees'")
    p.add_argument("--source", help="e.g. 'susds', 'buyback', 'ETH-A'")
    p.add_argument("--limit", type=int, default=50, help="max events to show")

    args = ap.parse_args()
    return {
        "snapshot": cmd_snapshot, "kpis": cmd_kpis, "settlements": cmd_settlements,
        "metrics": cmd_metrics, "series": cmd_series, "overlay": cmd_overlay,
        "daily": cmd_daily, "events": cmd_events,
    }[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
