#!/usr/bin/env python3
"""Build data/forum/registry.json from the Atlas Authorized Forum Accounts table.

WIP stub. Implementation plan: plans/forum-account-registry.md (local).

Depends on Atlas Edit poll 1630 (PR sky-ecosystem/next-gen-atlas#227) merging.
The new Atlas section A.2.7.1.1.1.1 introduces an Active Data table at
UUID b71564fd-22e0-4c69-99d1-5b23fc1fa329 that maps forum handles to entities
and roles. Once merged, this script parses that table into a registry consumed
by /forum-search, the session briefing, and /atlas-track.
"""

from __future__ import annotations

import sys


def main() -> int:
    # TODO: locate section b71564fd-22e0-4c69-99d1-5b23fc1fa329 via data/index.json
    # TODO: parse the markdown table (handle "N/A", comma-separated handles, transitive ARs)
    # TODO: build entities map + by_handle reverse map; collect validation warnings
    # TODO: write data/forum/registry.json
    print("build-account-registry: stub — see plans/forum-account-registry.md", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
