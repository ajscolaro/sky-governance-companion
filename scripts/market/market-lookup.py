#!/usr/bin/env python3
"""Look up market data for a date or date range from the SQLite database.

No API calls — reads from data/market.db.

Usage:
    python3 scripts/market/market-lookup.py --date 2026-04-09
    python3 scripts/market/market-lookup.py --date 2026-04-09 --format context
    python3 scripts/market/market-lookup.py --range 2026-04-01 2026-04-10
    python3 scripts/market/market-lookup.py --window 2026-04-09
    python3 scripts/market/market-lookup.py --check
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from market import MarketDB, ASSETS, fmt_price, fmt_supply, fmt_pct, format_context


def format_table(db: MarketDB, date: str) -> str:
    lines = [f"Market snapshot for {date}:", ""]
    for slug, info in ASSETS.items():
        parts = [f"  {info['name']:6s}"]
        if info["has_price"]:
            price = db.get_price(slug, date)
            if price is not None:
                parts.append(f"{fmt_price(price):>12s}")
                delta = db.get_delta(slug, date, days=-7)
                if delta is None:
                    week_ago = (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=7)).strftime("%Y-%m-%d")
                    prev = db.get_price(slug, week_ago)
                    if prev and prev != 0:
                        delta = round((price - prev) / prev * 100, 1)
                if delta is not None:
                    parts.append(f"7d: {fmt_pct(delta)}")
        if info["has_mcap"]:
            mcap = db.get_mcap(slug, date)
            if mcap is not None:
                label = "supply" if info["type"] == "stablecoin" else "mcap"
                parts.append(f"{label}: {fmt_supply(mcap)}")
        if len(parts) == 1:
            parts.append("no data")
        lines.append("  ".join(parts))
    return "\n".join(lines)


def format_range(db: MarketDB, start: str, end: str) -> str:
    lines = [f"Market data: {start} -> {end}", ""]
    lines.append(f"  {'Asset':6s}  {'Start':>14s}  {'End':>14s}  {'Change':>10s}")
    lines.append(f"  {'─' * 6}  {'─' * 14}  {'─' * 14}  {'─' * 10}")

    for slug, info in ASSETS.items():
        if info["has_price"]:
            p1 = db.get_price(slug, start)
            p2 = db.get_price(slug, end)
            if p1 and p2:
                pct = (p2 - p1) / p1 * 100
                lines.append(
                    f"  {info['name']:6s}  {fmt_price(p1):>14s}  "
                    f"{fmt_price(p2):>14s}  {fmt_pct(pct):>10s}"
                )
        if info["has_mcap"]:
            m1 = db.get_mcap(slug, start)
            m2 = db.get_mcap(slug, end)
            if m1 and m2:
                pct = (m2 - m1) / m1 * 100
                label = "supply" if info["type"] == "stablecoin" else "mcap"
                name = info["name"] if not info["has_price"] else ""
                lines.append(
                    f"  {name:6s}  {fmt_supply(m1):>14s}  "
                    f"{fmt_supply(m2):>14s}  {fmt_pct(pct):>10s}  ({label})"
                )
    return "\n".join(lines)


def format_window(db: MarketDB, date: str) -> str:
    w = db.get_event_window(date, before=3, after=7)
    lines = [f"Event window for {date} (-3d / +7d):", ""]
    for slug, data in w.get("assets", {}).items():
        parts = [f"  {ASSETS[slug]['name']:6s}  {fmt_price(data['price']):>12s}"]
        if "pct_before" in data:
            parts.append(f"3d before: {fmt_pct(data['pct_before'])}")
        if "pct_after" in data:
            parts.append(f"7d after: {fmt_pct(data['pct_after'])}")
        lines.append("  ".join(parts))
    return "\n".join(lines)


def check_freshness(db: MarketDB) -> list[str]:
    dr = db.date_range()
    if not dr:
        return ["Database is empty. Run: python3 scripts/market/fetch-market.py --backfill"]
    warnings = []
    latest = datetime.strptime(dr[1], "%Y-%m-%d")
    age = (datetime.utcnow() - latest).days
    if age > 7:
        warnings.append(f"Data is {age} days stale (latest: {dr[1]}). "
                        "Run: python3 scripts/market/fetch-market.py")
    else:
        warnings.append(f"Data: {dr[0]} to {dr[1]} ({db.row_count()} rows)")
    return warnings


def main():
    parser = argparse.ArgumentParser(
        description="Look up market data from SQLite database",
        epilog="Reads data/market.db. Run scripts/market/fetch-market.py to refresh.",
    )
    parser.add_argument("--date", type=str, help="Lookup date (YYYY-MM-DD)")
    parser.add_argument("--range", type=str, nargs=2, metavar=("START", "END"),
                        help="Date range")
    parser.add_argument("--window", type=str, metavar="DATE",
                        help="Event window: price around a governance event")
    parser.add_argument("--ratio", type=str, nargs=2, metavar=("ASSET", "DENOM"),
                        help="Price ratio (e.g., --ratio SKY BTC)")
    parser.add_argument("--stablecoins", type=str, nargs="?", const="latest", metavar="DATE",
                        help="Stablecoin market share snapshot (default: latest)")
    parser.add_argument("--format", type=str, default="table",
                        choices=["table", "context", "json"],
                        help="Output format (default: table)")
    parser.add_argument("--check", action="store_true", help="Check data freshness")
    args = parser.parse_args()

    if not any([args.date, args.range, args.window, args.ratio,
                args.stablecoins, args.check]):
        parser.print_help()
        sys.exit(1)

    try:
        db = MarketDB()
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    if args.check:
        for msg in check_freshness(db):
            print(msg)
        db.close()
        return

    if args.stablecoins:
        date = args.stablecoins
        if date == "latest":
            date = db.latest_date() or datetime.utcnow().strftime("%Y-%m-%d")
        share = db.get_stablecoin_share(date)
        if not share:
            print(f"No stablecoin data for {date}. Run: python3 scripts/market/fetch-market.py")
        elif args.format == "json":
            print(json.dumps(share, indent=2))
        else:
            print(f"Stablecoin market share — {share['date']}")
            print(f"Total supply: {fmt_supply(share['total_supply'])}")
            if share.get("usds"):
                u = share["usds"]
                print(f"USDS: #{u['rank']} — {fmt_supply(u['supply'])} ({u['share_pct']:.2f}%)")
            print()
            for sc in share["stablecoins"][:15]:
                marker = " <--" if sc["asset"].lower() == "usds" else ""
                print(f"  #{sc['rank']:2d}  {sc['asset']:8s}  {fmt_supply(sc['supply']):>12s}  "
                      f"({sc['share_pct']:.2f}%){marker}")
    elif args.ratio:
        asset, denom = args.ratio[0].lower(), args.ratio[1].lower()
        if args.range:
            data = db.get_ratio_range(asset, denom, args.range[0], args.range[1])
            for date, ratio in data:
                print(f"  {date}: {ratio:.10f}")
        elif args.date:
            ratio = db.get_ratio(asset, denom, args.date)
            if ratio:
                print(f"{asset.upper()}/{denom.upper()} on {args.date}: {ratio:.10f}")
            else:
                print(f"No data for {asset.upper()}/{denom.upper()} on {args.date}")
        else:
            # Default: last 30 days
            end = db.latest_date() or datetime.utcnow().strftime("%Y-%m-%d")
            start = (datetime.strptime(end, "%Y-%m-%d") - timedelta(days=30)).strftime("%Y-%m-%d")
            data = db.get_ratio_range(asset, denom, start, end)
            print(f"{asset.upper()}/{denom.upper()} — last 30 days:")
            for date, ratio in data:
                print(f"  {date}: {ratio:.10f}")
    elif args.window:
        print(format_window(db, args.window))
    elif args.range:
        if args.format == "json":
            print(json.dumps({
                "start": db.get_context(args.range[0]),
                "end": db.get_context(args.range[1]),
            }, indent=2))
        else:
            print(format_range(db, args.range[0], args.range[1]))
    elif args.date:
        if args.format == "table":
            print(format_table(db, args.date))
        elif args.format == "context":
            print(format_context(db, args.date))
        elif args.format == "json":
            print(json.dumps(db.get_context(args.date), indent=2))

    db.close()


if __name__ == "__main__":
    main()
