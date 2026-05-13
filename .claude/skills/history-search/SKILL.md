---
name: history-search
description: >
  Search the committed history/ changelogs to find when Atlas changes happened.
  Filter by keyword, entity, governance type, merged-date range, or PR number.
argument-hint: "<keyword or filters — e.g., 'renamed to Skybase' --since 2026-01-01>"
allowed-tools: Bash, Read
---

# History Search

You are searching the curated per-entity changelogs in `history/` — the institutional memory of every merged Atlas PR. Each leaf has a `changelog.md` with `## PR #N — Title` entries sorted most-recent-first.

## When to use this skill

- "When was X first added / renamed / removed?"
- "Show me every change that touched <entity>"
- "What governance events happened between <dates>?"
- "Find every PR that mentions <term>"
- "What PR introduced <feature>?"

For *current* Atlas state, use `/atlas-navigate` instead — this skill is for change history. For deep analysis of a single PR's diff, use `/atlas-analyze`.

## Quick usage

```bash
# Keyword search across all entities (default — most-recent-first)
python3 scripts/atlas/search-history.py "renamed to Skybase"

# Restrict to one entity (substring of path under history/)
python3 scripts/atlas/search-history.py "Foundation" --entity skybase

# Filter by governance type (substring of **Type:** label)
python3 scripts/atlas/search-history.py "Genesis Capital" --type "Spell recording"

# Date range
python3 scripts/atlas/search-history.py --since 2026-01-01 --until 2026-03-01 --entity spark

# Find a specific PR across all entities
python3 scripts/atlas/search-history.py --pr 167

# Print full entry bodies instead of one-line hits
python3 scripts/atlas/search-history.py "tokenomics" --show

# List every changelog dir with entry counts
python3 scripts/atlas/search-history.py --list-entities
```

Default output (one line per match):
```
PR #167 | 2026-01-22 | A.6--agents/A.6.1.1.4--skybase | Weekly edit (Atlas Axis)
  → Launch Agent 3 renamed to Skybase throughout the Atlas: agent Artifact header (A.6.1.1.4)...
```

Use `--show` for the full entry block (header + meta + body). `--limit` caps matches (default 50).

## Filters

| Flag | Matches | Example |
|------|---------|---------|
| (positional) | Keyword in entry title or body (case-insensitive) | `"tokenomics"` |
| `--entity <slug>` | Substring of path under `history/` | `--entity skybase`, `--entity A.6--agents` |
| `--type <text>` | Substring of `**Type:**` label | `--type "Weekly edit"`, `--type Spell` |
| `--since YYYY-MM-DD` | Merged on or after | `--since 2026-01-01` |
| `--until YYYY-MM-DD` | Merged on or before | `--until 2026-03-01` |
| `--pr N` | Exact PR number (any entity) | `--pr 167` |

All filters AND together.

## Governance type vocabulary

The `**Type:**` field uses these recurring labels (substring-match with `--type`):
- `Weekly edit (Atlas Axis)` — may include `— Poll <N>` suffix
- `AEP-N` / `SAEP-N (Spark proposal)`
- `Spell recording (<date>)`
- `Active Data update (Designated Controller)`
- `Housekeeping`

## Fallback strategy

**Never retry the exact same query twice.** If a search returns no matches:

1. **Broaden the keyword** — try the most distinctive word alone, or a shorter prefix
2. **Try synonyms** — "renamed" vs "rename" vs both the old and new names
3. **Drop `--entity`** if you're unsure of the slug — run `--list-entities` to see exact spellings
4. **Widen the date range** or remove it entirely
5. **Switch to `--show`** to read full entries when a one-line snippet isn't enough

If still nothing, the change may predate the curated history. The repo's `history/` is incomplete for the pre-2025 Atlas era and may also be missing post-2025 PRs that haven't been processed yet (check `history/_log.md` for the master PR index). Report the gap honestly — don't silently scrape upstream.

## Reading more than the snippet

The default one-line summary is fine for grep-style retrieval. When you need to actually understand a change:

- Use `--show` to print full Material Changes / Housekeeping / Context bodies for matched entries
- Open the source file directly with `Read` — the `**Entity:** <path>  (<file>)` line under `--show` gives you the relative file path

## Complementary skills

- `/atlas-navigate` — current Atlas state ("what does the Atlas say *now*?")
- `/atlas-analyze` — deep analysis of one PR's diff (the why, not just the index)
- `/governance-data` — voting portal / spell lifecycle (on-chain context for entries)
- `/forum-search` — community discussion that preceded a change
