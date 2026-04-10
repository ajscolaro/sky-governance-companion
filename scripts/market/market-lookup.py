#!/usr/bin/env python3
"""Look up market data for a given date or date range.

Reads cached JSON from data/voting/market/ (no API calls).

Usage:
    python3 scripts/market-lookup.py --date 2025-10-24
    python3 scripts/market-lookup.py --date 2025-10-24 --format context
    python3 scripts/market-lookup.py --range 2025-10-01 2025-10-31
    python3 scripts/market-lookup.py --range 2025-10-01 2025-10-31 --format json
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
MARKET_DIR = PROJECT_DIR / "data" / "voting" / "market"

# Point schemas (implicit in Messari API response):
#   price:     [timestamp, open, high, low, close, volume]
#   marketcap: [timestamp, marketcap, ?, fully_diluted_marketcap]
# For stablecoins (USDS, sUSDS), marketcap ≈ circulating supply.

ASSETS = [
    {"slug": "sky",   "name": "SKY",   "type": "governance", "datasets": ["price", "marketcap"]},
    {"slug": "spk",   "name": "SPK",   "type": "agent",      "datasets": ["price", "marketcap"]},
    {"slug": "usds",  "name": "USDS",  "type": "stablecoin",  "datasets": ["marketcap"]},
    {"slug": "susds", "name": "sUSDS", "type": "stablecoin",  "datasets": ["marketcap"]},
    {"slug": "btc",   "name": "BTC",   "type": "benchmark",   "datasets": ["price"]},
    {"slug": "eth",   "name": "ETH",   "type": "benchmark",   "datasets": ["price"]},
]


def load_points(slug: str, dataset: str) -> list[tuple[datetime, list]]:
    """Load data points from a market JSON file. Returns [(datetime, raw_point), ...]."""
    path = MARKET_DIR / f"{slug}-{dataset}.json"
    if not path.exists():
        return []
    with open(path) as f:
        data = json.load(f)
    points = data.get("points", [])
    result = []
    for p in points:
        ts = datetime.utcfromtimestamp(p[0])
        result.append((ts, p))
    return result


def find_nearest(points: list[tuple[datetime, list]], target: datetime,
                 max_days: int = 7) -> tuple[datetime, list] | None:
    """Find the data point nearest to target date, within max_days tolerance."""
    if not points:
        return None
    best = None
    best_delta = timedelta(days=max_days + 1)
    for ts, p in points:
        delta = abs(ts - target)
        if delta < best_delta:
            best = (ts, p)
            best_delta = delta
    if best_delta > timedelta(days=max_days):
        return None
    return best


def find_prior(points: list[tuple[datetime, list]], target: datetime,
               days_back: int = 7) -> tuple[datetime, list] | None:
    """Find the data point ~days_back before target for computing deltas."""
    prior_target = target - timedelta(days=days_back)
    return find_nearest(points, prior_target, max_days=4)


def fmt_price(value: float) -> str:
    if value >= 1:
        return f"${value:,.2f}"
    elif value >= 0.01:
        return f"${value:.4f}"
    else:
        return f"${value:.6f}"


def fmt_supply(value: float) -> str:
    if value >= 1e9:
        return f"${value / 1e9:.2f}B"
    elif value >= 1e6:
        return f"${value / 1e6:.1f}M"
    else:
        return f"${value:,.0f}"


def fmt_volume(value: float) -> str:
    if value >= 1e6:
        return f"${value / 1e6:.1f}M"
    elif value >= 1e3:
        return f"${value / 1e3:.0f}K"
    else:
        return f"${value:,.0f}"


def fmt_pct(old: float, new: float) -> str:
    if old == 0:
        return "n/a"
    pct = (new - old) / old * 100
    sign = "+" if pct >= 0 else ""
    return f"{sign}{pct:.1f}%"


def lookup_date(target: datetime) -> list[dict]:
    """Look up all asset data for a single date. Returns list of asset snapshots."""
    results = []
    for asset in ASSETS:
        entry = {"slug": asset["slug"], "name": asset["name"], "type": asset["type"]}

        if "price" in asset["datasets"]:
            points = load_points(asset["slug"], "price")
            match = find_nearest(points, target)
            if match:
                ts, p = match
                entry["price_date"] = ts.strftime("%Y-%m-%d")
                entry["close"] = p[4]
                entry["volume"] = p[5]
                prior = find_prior(points, ts)
                if prior:
                    entry["price_7d_change"] = fmt_pct(prior[1][4], p[4])

        if "marketcap" in asset["datasets"]:
            points = load_points(asset["slug"], "marketcap")
            match = find_nearest(points, target)
            if match:
                ts, p = match
                entry["mcap_date"] = ts.strftime("%Y-%m-%d")
                entry["marketcap"] = p[1]
                prior = find_prior(points, ts)
                if prior:
                    entry["mcap_7d_change"] = fmt_pct(prior[1][1], p[1])

        results.append(entry)
    return results


def format_table(results: list[dict], target_date: str) -> str:
    """Format results as a readable table."""
    lines = [f"Market snapshot for {target_date}:", ""]
    for r in results:
        parts = [f"  {r['name']:6s}"]
        if "close" in r:
            parts.append(f"{fmt_price(r['close']):>12s} (close)")
            if "price_7d_change" in r:
                parts.append(f"7d: {r['price_7d_change']}")
            if "volume" in r:
                parts.append(f"vol: {fmt_volume(r['volume'])}")
        if "marketcap" in r:
            label = "supply" if r["type"] == "stablecoin" else "mcap"
            parts.append(f"{label}: {fmt_supply(r['marketcap'])}")
            if "mcap_7d_change" in r:
                parts.append(f"7d: {r['mcap_7d_change']}")
        if len(parts) == 1:
            parts.append("no data available")
        lines.append("  ".join(parts))
    return "\n".join(lines)


def format_context(results: list[dict]) -> str:
    """Format as a prose sentence for pasting into a ### Context section."""
    parts = []
    for r in results:
        if "close" in r:
            s = f"{r['name']} ~{fmt_price(r['close'])}"
            if "price_7d_change" in r:
                pct = r["price_7d_change"]
                direction = "up" if pct.startswith("+") else "down"
                s += f" ({direction} {pct.lstrip('+-')} WoW)"
            parts.append(s)
        elif "marketcap" in r:
            label = "supply" if r["type"] == "stablecoin" else "mcap"
            parts.append(f"{r['name']} {label} {fmt_supply(r['marketcap'])}")
    return ", ".join(parts) + "."


def format_json(results: list[dict]) -> str:
    return json.dumps(results, indent=2)


def lookup_range(start: datetime, end: datetime) -> str:
    """Look up market data for a date range, showing start/end and delta."""
    start_data = lookup_date(start)
    end_data = lookup_date(end)

    lines = [f"Market data: {start.strftime('%Y-%m-%d')} → {end.strftime('%Y-%m-%d')}", ""]
    lines.append(f"  {'Asset':6s}  {'Start':>14s}  {'End':>14s}  {'Change':>10s}")
    lines.append(f"  {'─' * 6}  {'─' * 14}  {'─' * 14}  {'─' * 10}")

    for s, e in zip(start_data, end_data):
        if "close" in s and "close" in e:
            lines.append(
                f"  {s['name']:6s}  {fmt_price(s['close']):>14s}  "
                f"{fmt_price(e['close']):>14s}  {fmt_pct(s['close'], e['close']):>10s}"
            )
        if "marketcap" in s and "marketcap" in e:
            label = f"{s['name']:6s}"
            if "close" in s:
                label = f"  {'':6s}"  # indent under price row
            kind = "supply" if s["type"] == "stablecoin" else "mcap"
            lines.append(
                f"  {label}  {fmt_supply(s['marketcap']):>14s}  "
                f"{fmt_supply(e['marketcap']):>14s}  {fmt_pct(s['marketcap'], e['marketcap']):>10s}"
                f"  ({kind})"
            )
    return "\n".join(lines)


def check_data_freshness() -> list[str]:
    """Check for stale or missing data files."""
    warnings = []
    for asset in ASSETS:
        for dataset in asset["datasets"]:
            path = MARKET_DIR / f"{asset['slug']}-{dataset}.json"
            if not path.exists():
                warnings.append(f"Missing: {path.name}")
                continue
            with open(path) as f:
                data = json.load(f)
            points = data.get("points", [])
            if not points:
                warnings.append(f"Empty: {path.name}")
                continue
            last_ts = datetime.utcfromtimestamp(points[-1][0])
            age = datetime.utcnow() - last_ts
            if age > timedelta(days=14):
                warnings.append(
                    f"Stale: {path.name} — last data point {last_ts.strftime('%Y-%m-%d')} "
                    f"({age.days} days old). Run: python3 scripts/market/fetch-market-data.py --asset {asset['slug']}"
                )
    return warnings


def main():
    parser = argparse.ArgumentParser(
        description="Look up market data for a date or date range",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Reads cached data from data/voting/market/. No API calls.\n"
               "Run scripts/market/fetch-market-data.py to refresh the cache.",
    )
    parser.add_argument("--date", type=str, help="Lookup date (YYYY-MM-DD)")
    parser.add_argument("--range", type=str, nargs=2, metavar=("START", "END"),
                        help="Date range (YYYY-MM-DD YYYY-MM-DD)")
    parser.add_argument("--format", type=str, default="table",
                        choices=["table", "context", "json"],
                        help="Output format (default: table)")
    args = parser.parse_args()

    if not args.date and not args.range:
        parser.print_help()
        sys.exit(1)

    # Check freshness
    warnings = check_data_freshness()
    if warnings:
        for w in warnings:
            print(f"⚠ {w}", file=sys.stderr)
        print(file=sys.stderr)

    if args.range:
        start = datetime.strptime(args.range[0], "%Y-%m-%d")
        end = datetime.strptime(args.range[1], "%Y-%m-%d")
        if args.format == "json":
            print(json.dumps({
                "start": lookup_date(start),
                "end": lookup_date(end),
            }, indent=2))
        else:
            print(lookup_range(start, end))
    elif args.date:
        target = datetime.strptime(args.date, "%Y-%m-%d")
        results = lookup_date(target)
        if args.format == "table":
            print(format_table(results, args.date))
        elif args.format == "context":
            print(format_context(results))
        elif args.format == "json":
            print(format_json(results))


if __name__ == "__main__":
    main()
