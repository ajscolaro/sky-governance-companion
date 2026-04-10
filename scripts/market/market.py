"""Market data query module backed by SQLite.

Single source of truth for daily price and market cap data. Any script
can import this module to query market data on the fly.

Database: data/market.db (gitignored, rebuilt from Messari API)

Schema:
    daily(date TEXT, asset TEXT, close REAL, mcap REAL,
          PRIMARY KEY (date, asset))

Usage:
    from scripts.market.market import MarketDB

    db = MarketDB()
    db.get_price("SKY", "2026-04-09")          # -> 0.078 or None
    db.get_mcap("USDS", "2026-04-09")           # -> 11500000000 or None
    db.get_context("2026-04-09")                 # -> {"sky": 0.078, "usds_mcap": 11.5e9, ...}
    db.get_delta("SKY", "2026-04-09", days=3)    # -> 4.2 (percent) or None
    db.get_range("SKY", "2026-04-01", "2026-04-10")  # -> [(date, close), ...]
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = PROJECT_DIR / "data" / "market.db"

# Tracked assets and their data types
ASSETS = {
    "sky":   {"name": "SKY",   "has_price": True,  "has_mcap": True,  "type": "governance"},
    "usds":  {"name": "USDS",  "has_price": False, "has_mcap": True,  "type": "stablecoin"},
    "susds": {"name": "sUSDS", "has_price": False, "has_mcap": True,  "type": "stablecoin"},
    "spk":   {"name": "SPK",   "has_price": True,  "has_mcap": True,  "type": "agent"},
    "btc":   {"name": "BTC",   "has_price": True,  "has_mcap": False, "type": "benchmark"},
    "eth":   {"name": "ETH",   "has_price": True,  "has_mcap": False, "type": "benchmark"},
}


class MarketDB:
    """Query interface for the market SQLite database."""

    def __init__(self, db_path: Path | str | None = None):
        self.db_path = Path(db_path) if db_path else DB_PATH
        self._conn: sqlite3.Connection | None = None

    @property
    def conn(self) -> sqlite3.Connection:
        if self._conn is None:
            if not self.db_path.exists():
                raise FileNotFoundError(
                    f"Market database not found at {self.db_path}. "
                    "Run: python3 scripts/market/fetch-market.py"
                )
            self._conn = sqlite3.connect(str(self.db_path))
        return self._conn

    def close(self):
        if self._conn:
            self._conn.close()
            self._conn = None

    # ------------------------------------------------------------------
    # Core queries
    # ------------------------------------------------------------------

    def get_price(self, asset: str, date: str, tolerance_days: int = 5) -> float | None:
        """Get closing price for an asset on a date. Falls back to nearest within tolerance."""
        return self._get_field("close", asset.lower(), date, tolerance_days)

    def get_mcap(self, asset: str, date: str, tolerance_days: int = 5) -> float | None:
        """Get market cap for an asset on a date. For stablecoins this is circulating supply."""
        return self._get_field("mcap", asset.lower(), date, tolerance_days)

    def get_range(self, asset: str, start: str, end: str,
                  field: str = "close") -> list[tuple[str, float]]:
        """Get daily values for an asset over a date range.

        Returns list of (date, value) tuples. Field can be 'close' or 'mcap'.
        """
        cur = self.conn.execute(
            f"SELECT date, {field} FROM daily WHERE asset = ? AND date BETWEEN ? AND ? "
            f"AND {field} IS NOT NULL ORDER BY date",
            (asset.lower(), start, end),
        )
        return cur.fetchall()

    def get_delta(self, asset: str, date: str, days: int = 3,
                  field: str = "close") -> float | None:
        """Get percent change from date to date+days.

        Returns percentage (e.g., 4.2 for +4.2%), or None if data unavailable.
        """
        cur = self.conn.execute(
            f"SELECT date, {field} FROM daily WHERE asset = ? "
            f"AND date >= ? AND {field} IS NOT NULL ORDER BY date LIMIT 1",
            (asset.lower(), date),
        )
        row_start = cur.fetchone()
        if not row_start:
            return None

        # Find the point ~days later
        from datetime import datetime, timedelta
        target = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=days)
        target_str = target.strftime("%Y-%m-%d")

        cur = self.conn.execute(
            f"SELECT date, {field} FROM daily WHERE asset = ? "
            f"AND date >= ? AND {field} IS NOT NULL ORDER BY date LIMIT 1",
            (asset.lower(), target_str),
        )
        row_end = cur.fetchone()
        if not row_end:
            return None

        # Verify the end point isn't too far from target (allow +3 day drift)
        end_date = datetime.strptime(row_end[0], "%Y-%m-%d")
        if abs((end_date - target).days) > 3:
            return None

        if row_start[1] == 0:
            return None
        return round((row_end[1] - row_start[1]) / row_start[1] * 100, 2)

    def get_context(self, date: str) -> dict:
        """Get a market snapshot for a date across all tracked assets.

        Returns dict like:
            {"date": "2026-04-09", "sky": 0.078, "sky_mcap": 1.2e9,
             "usds_mcap": 11.5e9, "btc": 85000, "eth": 2100, ...}
        """
        ctx = {"date": date}
        for slug, info in ASSETS.items():
            if info["has_price"]:
                price = self.get_price(slug, date)
                if price is not None:
                    ctx[slug] = price
            if info["has_mcap"]:
                mcap = self.get_mcap(slug, date)
                if mcap is not None:
                    ctx[f"{slug}_mcap"] = mcap
        return ctx

    def get_event_window(self, date: str, before: int = 3, after: int = 7) -> dict:
        """Get price data in a window around a governance event.

        Returns dict with before/after prices and deltas for each priced asset.
        Useful for analyzing market reaction to polls, spells, PR merges.
        """
        from datetime import datetime, timedelta
        dt = datetime.strptime(date, "%Y-%m-%d")
        start = (dt - timedelta(days=before)).strftime("%Y-%m-%d")
        end = (dt + timedelta(days=after)).strftime("%Y-%m-%d")

        window = {"date": date, "window": f"-{before}d/+{after}d", "assets": {}}

        for slug, info in ASSETS.items():
            if not info["has_price"]:
                continue
            price_at = self.get_price(slug, date)
            if price_at is None:
                continue

            entry = {"price": price_at}
            delta_before = self.get_delta(slug, start, days=before, field="close")
            if delta_before is not None:
                entry["pct_before"] = delta_before
            delta_after = self.get_delta(slug, date, days=after, field="close")
            if delta_after is not None:
                entry["pct_after"] = delta_after

            window["assets"][slug] = entry

        return window

    # ------------------------------------------------------------------
    # Derived ratios
    # ------------------------------------------------------------------

    def get_ratio(self, asset: str, denominator: str, date: str) -> float | None:
        """Get the price ratio asset/denominator on a date (e.g., SKY/BTC)."""
        p = self.get_price(asset, date)
        d = self.get_price(denominator, date)
        if p is None or d is None or d == 0:
            return None
        return p / d

    def get_ratio_range(self, asset: str, denominator: str,
                        start: str, end: str) -> list[tuple[str, float]]:
        """Get daily ratio values over a date range.

        Returns list of (date, ratio) tuples for dates where both prices exist.
        """
        a_data = {d: v for d, v in self.get_range(asset.lower(), start, end)}
        d_data = {d: v for d, v in self.get_range(denominator.lower(), start, end)}
        result = []
        for date in sorted(a_data.keys() & d_data.keys()):
            if d_data[date] != 0:
                result.append((date, a_data[date] / d_data[date]))
        return result

    def get_ratio_delta(self, asset: str, denominator: str,
                        date: str, days: int = 7) -> float | None:
        """Get percent change in the ratio over a period."""
        from datetime import datetime, timedelta
        r1 = self.get_ratio(asset, denominator, date)
        target = (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=days)).strftime("%Y-%m-%d")
        r2 = self.get_ratio(asset, denominator, target)
        if r1 is None or r2 is None or r1 == 0:
            return None
        return round((r2 - r1) / r1 * 100, 2)

    # ------------------------------------------------------------------
    # Stablecoin market share
    # ------------------------------------------------------------------

    def get_stablecoin_share(self, date: str) -> dict | None:
        """Get USDS market share relative to other stablecoins on a date.

        Reads from the stablecoin_snapshot table for rankings. For USDS,
        uses the asset-level marketcap value from the daily table for
        consistency with our other USDS metrics.

        USDS is labeled "USDS+DAI" since Messari aggregates DAI into USDS.
        """
        cur = self.conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='stablecoin_snapshot'"
        )
        if not cur.fetchone():
            return None

        cur = self.conn.execute(
            "SELECT asset, supply FROM stablecoin_snapshot "
            "WHERE date = ? AND supply IS NOT NULL ORDER BY supply DESC",
            (date,),
        )
        rows = cur.fetchall()
        if not rows:
            return None

        # Use the asset-level marketcap for USDS for consistency
        usds_mcap = self.get_mcap("usds", date)
        corrected = []
        for asset, supply in rows:
            if asset.lower() == "usds" and usds_mcap is not None:
                corrected.append(("USDS+DAI", usds_mcap))
            else:
                corrected.append((asset, supply))

        # Re-sort after correction
        corrected.sort(key=lambda x: x[1], reverse=True)

        total = sum(s for _, s in corrected)
        result = {"date": date, "total_supply": total, "stablecoins": []}
        usds_rank = None
        for i, (asset, supply) in enumerate(corrected, 1):
            entry = {
                "rank": i,
                "asset": asset,
                "supply": supply,
                "share_pct": round(supply / total * 100, 3) if total else 0,
            }
            result["stablecoins"].append(entry)
            if "usds" in asset.lower():
                usds_rank = i
                result["usds"] = entry

        result["usds_rank"] = usds_rank
        return result

    def latest_date(self) -> str | None:
        """Return the most recent date in the database."""
        cur = self.conn.execute("SELECT MAX(date) FROM daily")
        row = cur.fetchone()
        return row[0] if row else None

    def date_range(self) -> tuple[str, str] | None:
        """Return (earliest, latest) dates in the database."""
        cur = self.conn.execute("SELECT MIN(date), MAX(date) FROM daily")
        row = cur.fetchone()
        return (row[0], row[1]) if row and row[0] else None

    def row_count(self) -> int:
        cur = self.conn.execute("SELECT COUNT(*) FROM daily")
        return cur.fetchone()[0]

    # ------------------------------------------------------------------
    # Write interface (used by fetch script)
    # ------------------------------------------------------------------

    @staticmethod
    def init_db(db_path: Path | str | None = None) -> sqlite3.Connection:
        """Create or open the database and ensure the schema exists."""
        path = Path(db_path) if db_path else DB_PATH
        path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(str(path))
        conn.execute("""
            CREATE TABLE IF NOT EXISTS daily (
                date  TEXT NOT NULL,
                asset TEXT NOT NULL,
                close REAL,
                mcap  REAL,
                PRIMARY KEY (date, asset)
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_daily_asset ON daily(asset, date)")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS stablecoin_snapshot (
                date   TEXT NOT NULL,
                asset  TEXT NOT NULL,
                supply REAL,
                PRIMARY KEY (date, asset)
            )
        """)
        conn.commit()
        return conn

    @staticmethod
    def upsert_rows(conn: sqlite3.Connection, rows: list[tuple]) -> int:
        """Insert or update rows. Each row is (date, asset, close, mcap).

        Returns number of rows upserted.
        """
        if not rows:
            return 0
        conn.executemany(
            "INSERT INTO daily (date, asset, close, mcap) VALUES (?, ?, ?, ?) "
            "ON CONFLICT(date, asset) DO UPDATE SET "
            "close = COALESCE(excluded.close, close), "
            "mcap = COALESCE(excluded.mcap, mcap)",
            rows,
        )
        conn.commit()
        return len(rows)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _get_field(self, field: str, asset: str, date: str,
                   tolerance_days: int) -> float | None:
        """Get a field value, falling back to nearest date within tolerance."""
        # Try exact match first
        cur = self.conn.execute(
            f"SELECT {field} FROM daily WHERE asset = ? AND date = ? AND {field} IS NOT NULL",
            (asset, date),
        )
        row = cur.fetchone()
        if row:
            return row[0]

        if tolerance_days <= 0:
            return None

        # Fallback: nearest within tolerance window
        from datetime import datetime, timedelta
        dt = datetime.strptime(date, "%Y-%m-%d")
        start = (dt - timedelta(days=tolerance_days)).strftime("%Y-%m-%d")
        end = (dt + timedelta(days=tolerance_days)).strftime("%Y-%m-%d")

        cur = self.conn.execute(
            f"SELECT date, {field} FROM daily WHERE asset = ? "
            f"AND date BETWEEN ? AND ? AND {field} IS NOT NULL "
            "ORDER BY ABS(julianday(date) - julianday(?)) LIMIT 1",
            (asset, start, end, date),
        )
        row = cur.fetchone()
        return row[1] if row else None


# ------------------------------------------------------------------
# Formatting utilities (for CLI and context strings)
# ------------------------------------------------------------------

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


def fmt_pct(pct: float) -> str:
    sign = "+" if pct >= 0 else ""
    return f"{sign}{pct:.1f}%"


def format_context(db: MarketDB, date: str) -> str:
    """One-line prose summary for pasting into changelog Context sections."""
    parts = []
    for slug, info in ASSETS.items():
        if info["has_price"]:
            price = db.get_price(slug, date)
            if price is None:
                continue
            s = f"{info['name']} ~{fmt_price(price)}"
            delta = db.get_delta(slug, date, days=-7)
            if delta is None:
                # try backward delta
                from datetime import datetime, timedelta
                week_ago = (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=7)).strftime("%Y-%m-%d")
                price_week_ago = db.get_price(slug, week_ago)
                if price_week_ago and price_week_ago != 0:
                    delta = round((price - price_week_ago) / price_week_ago * 100, 1)
            if delta is not None:
                direction = "up" if delta >= 0 else "down"
                s += f" ({direction} {abs(delta):.1f}% WoW)"
            parts.append(s)
        elif info["has_mcap"]:
            mcap = db.get_mcap(slug, date)
            if mcap is not None:
                label = "supply" if info["type"] == "stablecoin" else "mcap"
                parts.append(f"{info['name']} {label} {fmt_supply(mcap)}")
    return ", ".join(parts) + "." if parts else "No market data available."
