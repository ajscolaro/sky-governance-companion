"""BA Labs Sky accounting API client + cache accessor.

Single source of truth for the protocol financial statements (balance sheet,
profit & loss, cash flow) served by BA Labs / Block Analitica. Full endpoint
contract: docs/financials-api.md.

Two layers:
    FinancialsClient  — live HTTP against the API, with mandatory retries
                        (the server drops large responses mid-stream).
    FinancialsCache   — read the JSON snapshots written to data/financials/
                        by fetch-financials.py (offline, no network).

Values arrive as high-precision decimal strings; this module preserves them as
strings and exposes `to_decimal` / formatting helpers rather than coercing to
float (which would lose precision). Attribute figures as "per BA Labs / SkyEco",
never as an official protocol statement.

Usage:
    from scripts.financials.financials import FinancialsClient, FinancialsCache

    c = FinancialsClient()
    bs = c.balance_sheet()                       # point-in-time snapshot
    pnl = c.profit_and_loss(date_from="2026-07-01", date_to="2026-07-31")
    series = c.headline_history("cash-flow", group_by="month")
    latest = c.balance_sheet_items_latest()      # block-stamped, BS only

    cache = FinancialsCache()                     # offline reads
    bs = cache.balance_sheet()
"""

from __future__ import annotations

import http.client
import json
import time
import urllib.error
import urllib.request
from decimal import Decimal
from pathlib import Path
from urllib.parse import urlencode

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
CACHE_DIR = PROJECT_DIR / "data" / "financials"

API_BASE = "https://sky.data.blockanalitica.com/v1/accounting"
USER_AGENT = "sky-governance-companion/financials (read-only)"

FETCH_TIMEOUT = 45
MAX_RETRIES = 6
RETRY_BACKOFF = 0.6

# The three statement families. Balance sheet is a stock (point-in-time); P&L and
# cash flow are flows (period-summed). Only the balance sheet has an items/latest/.
STATEMENTS = ("balance-sheet", "profit-and-loss", "cash-flow")

# Rejected by the API; kept here so callers can validate before a wasted request.
VALID_GROUP_BY = ("day", "month", "quarter", "year")


class FinancialsError(RuntimeError):
    """Raised when the API cannot be reached after retries, or returns non-JSON."""


# ----------------------------------------------------------------------------
# Live client
# ----------------------------------------------------------------------------

class FinancialsClient:
    """Live HTTP client for the BA Labs accounting API."""

    def __init__(self, base: str = API_BASE, timeout: int = FETCH_TIMEOUT,
                 retries: int = MAX_RETRIES):
        self.base = base.rstrip("/")
        self.timeout = timeout
        self.retries = retries

    def _get(self, path: str, params: dict | None = None):
        """GET {base}/{path}/ and return the unwrapped `data`.

        Retries on transient stream drops — the server routinely closes large
        responses early (IncompleteRead / connection reset), which is a
        transport failure, not an application error, so a plain re-request
        succeeds. HTTP 4xx/5xx are surfaced immediately (no point retrying a 400).
        """
        url = f"{self.base}/{path.strip('/')}/"
        if params:
            clean = {k: v for k, v in params.items() if v is not None}
            if clean:
                url += "?" + urlencode(clean)
        last_err = None
        for attempt in range(self.retries):
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    raw = resp.read()
                payload = json.loads(raw)
                return payload.get("data") if isinstance(payload, dict) else payload
            except urllib.error.HTTPError as e:
                raise FinancialsError(f"{url} -> HTTP {e.code}") from e
            except (urllib.error.URLError, http.client.HTTPException, ConnectionError,
                    json.JSONDecodeError, OSError, TimeoutError) as e:
                # http.client.IncompleteRead (a HTTPException, not an OSError) is the
                # server dropping a large response mid-stream — the common case here.
                last_err = e
                time.sleep(RETRY_BACKOFF * (attempt + 1))
        raise FinancialsError(f"{url} failed after {self.retries} attempts: {last_err}")

    # -- Statement snapshots -------------------------------------------------

    def balance_sheet(self, date_from: str | None = None, date_to: str | None = None) -> dict:
        """Point-in-time balance sheet. With a range, returns the as-of `date_to`."""
        return self._get("balance-sheet", {"date_from": date_from, "date_to": date_to})

    def profit_and_loss(self, date_from: str | None = None, date_to: str | None = None) -> dict:
        """P&L over the given period (defaults to full history when unbounded)."""
        return self._get("profit-and-loss", {"date_from": date_from, "date_to": date_to})

    def cash_flow(self, date_from: str | None = None, date_to: str | None = None) -> dict:
        """Cash flow over the given period (defaults to full history when unbounded)."""
        return self._get("cash-flow", {"date_from": date_from, "date_to": date_to})

    def statement(self, name: str, date_from: str | None = None, date_to: str | None = None) -> dict:
        _require_statement(name)
        return self._get(name, {"date_from": date_from, "date_to": date_to})

    # -- Time series ---------------------------------------------------------

    def headline_history(self, statement: str, group_by: str = "month",
                         date_from: str | None = None, date_to: str | None = None) -> list:
        """Headline totals over time.

        Balance sheet has no dedicated statement/history endpoint — its headline
        totals live under /history/ keyed by item_type; P&L and cash flow expose
        /statement/history/ as {date, revenue, expense, net}.
        """
        _require_statement(statement)
        _require_group_by(group_by)
        path = f"{statement}/history" if statement == "balance-sheet" else f"{statement}/statement/history"
        return self._get(path, {"group_by": group_by, "date_from": date_from, "date_to": date_to})

    def component_history(self, statement: str, group_by: str = "month",
                          date_from: str | None = None, date_to: str | None = None) -> list:
        """Component totals over time (/history/) — rows keyed by item_type/type."""
        _require_statement(statement)
        _require_group_by(group_by)
        return self._get(f"{statement}/history", {"group_by": group_by, "date_from": date_from, "date_to": date_to})

    # -- Item-level ----------------------------------------------------------

    def categories(self, statement: str) -> list:
        """The category taxonomy for a statement (item_type/type, category, subcategory)."""
        _require_statement(statement)
        return self._get(f"{statement}/categories")

    def items(self, statement: str, page: int = 1, limit: int = 100) -> dict:
        """Paginated latest value per item. Returns {results, pagination}."""
        _require_statement(statement)
        return self._get(f"{statement}/items", {"page": page, "limit": limit})

    def balance_sheet_items_latest(self) -> list:
        """Flat, block-stamped current balances per item — the live-snapshot source.

        Balance-sheet only; the flow statements have no meaningful "latest" and 404.
        """
        return self._get("balance-sheet/items/latest")

    def item_history(self, statement: str, uid: str, page: int = 1, limit: int = 100) -> dict:
        """Paginated history for a single item by uid. Returns {results, pagination}."""
        _require_statement(statement)
        return self._get(f"{statement}/items/{uid}", {"page": page, "limit": limit})

    def items_history(self, statement: str) -> list:
        """Full flat time series of every item (large — hundreds of KB)."""
        _require_statement(statement)
        return self._get(f"{statement}/items/history")

    def events(self, page: int = 1, limit: int = 100,
               date_from: str | None = None, date_to: str | None = None) -> dict:
        """Transaction-level cash-flow events (onchain). ~760k rows — always paginate."""
        return self._get("cash-flow/events",
                         {"page": page, "limit": limit, "date_from": date_from, "date_to": date_to})

    # -- Composite -----------------------------------------------------------

    def live_snapshot(self, fetched_at: str) -> dict:
        """Fetch the three statements + block-stamped balance-sheet items in one call.

        `fetched_at` is passed in (not stamped here) so callers control the clock —
        keeps this deterministic and testable.
        """
        latest = self.balance_sheet_items_latest()
        block = max((row.get("block_number") for row in latest if row.get("block_number")), default=None)
        return {
            "fetched_at": fetched_at,
            "block_number": block,
            "balance_sheet": self.balance_sheet(),
            "profit_and_loss": self.profit_and_loss(),
            "cash_flow": self.cash_flow(),
            "balance_sheet_items_latest": latest,
        }


# ----------------------------------------------------------------------------
# Offline cache reader
# ----------------------------------------------------------------------------

class FinancialsCache:
    """Read the JSON snapshots written by fetch-financials.py (no network)."""

    def __init__(self, cache_dir: Path | str | None = None):
        self.dir = Path(cache_dir) if cache_dir else CACHE_DIR

    def _read(self, name: str):
        path = self.dir / name
        if not path.exists():
            raise FileNotFoundError(
                f"{path} not found. Run: python3 scripts/financials/fetch-financials.py"
            )
        return json.loads(path.read_text())

    def meta(self) -> dict:
        return self._read("_meta.json")

    def balance_sheet(self) -> dict:
        return self._read("balance-sheet.json")

    def profit_and_loss(self) -> dict:
        return self._read("profit-and-loss.json")

    def cash_flow(self) -> dict:
        return self._read("cash-flow.json")

    def balance_sheet_items_latest(self) -> list:
        return self._read("balance-sheet-items-latest.json")

    def is_stale(self, max_age_hours: float = 24.0) -> bool:
        """True when the cached snapshot is older than max_age_hours (or missing)."""
        try:
            meta = self.meta()
        except FileNotFoundError:
            return True
        from datetime import datetime, timezone
        try:
            fetched = datetime.fromisoformat(meta["fetched_at"].replace("Z", "+00:00"))
        except (KeyError, ValueError):
            return True
        age = (datetime.now(timezone.utc) - fetched).total_seconds() / 3600
        return age > max_age_hours


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------

def _require_statement(name: str) -> None:
    if name not in STATEMENTS:
        raise ValueError(f"unknown statement {name!r}; expected one of {STATEMENTS}")


def _require_group_by(group_by: str) -> None:
    if group_by not in VALID_GROUP_BY:
        raise ValueError(f"invalid group_by {group_by!r}; expected one of {VALID_GROUP_BY}")


def to_decimal(value) -> Decimal | None:
    """Parse an API decimal string to Decimal, tolerating None/empty."""
    if value is None or value == "":
        return None
    try:
        return Decimal(str(value))
    except (ArithmeticError, ValueError):
        return None


def fmt_usd(value) -> str:
    """Format a decimal-string/number as a compact USD figure."""
    d = to_decimal(value)
    if d is None:
        return "n/a"
    a = abs(d)
    if a >= 1_000_000_000:
        return f"${d / Decimal(1_000_000_000):.2f}B"
    if a >= 1_000_000:
        return f"${d / Decimal(1_000_000):.1f}M"
    if a >= 1_000:
        return f"${d / Decimal(1_000):.1f}K"
    return f"${d:,.0f}"
