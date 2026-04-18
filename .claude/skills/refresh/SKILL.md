---
name: refresh
description: >
  Refresh all cached governance, market, and forum data, auto-process any
  unprocessed merged Atlas PRs, and display the session briefing. Use when
  the user wants to see what's changed, check current governance state, or
  verify all data sources are up to date.
allowed-tools: Bash, Read
---

# /refresh

You are updating all cached data sources and surfacing what's changed since the user's last session.

## What this does

`scripts/core/refresh.sh` runs these steps:

1. **Parallel fetches** — every data source in one go:
   - Voting portal polls, executives, executive proposals, delegates
   - Forum posts and per-AD vote rationales
   - Market prices/supply (if `MESSARI_API_KEY` is set)
   - Open Atlas PRs from GitHub
   - Discovery of merged PRs that aren't yet in `history/_log.md`
2. **Auto-process merged PRs** — runs `scripts/atlas/process-pr.sh` on each unprocessed merged PR, writing skeleton entries to the affected `history/<entity>/changelog.md` files (status=`skeleton`).
3. **Session briefing** — prints only sections that have content: market (daily), spells (current + pending), polls (ended since last session + active), atlas proposals (new open PRs in last 7 days), forum activity (new posts).

`/refresh` does **not** re-sync the Atlas git repo or rebuild the index — that's handled by the SessionStart hook (`scripts/core/atlas-sync.sh`). If the user asks for fresh Atlas commits mid-session, tell them to restart Claude.

## How to invoke

Run the refresh script and surface its output to the user:

```bash
bash scripts/core/refresh.sh
```


## Follow-up: finalize skeleton PRs

A **skeleton** is a merged PR whose structural changes have been recorded in `history/` but whose interpretive context (Material/Housekeeping sections, before→after values, narrative Context) hasn't been filled in yet. Only merged PRs ever become skeletons — unmerged ones go to the Atlas Proposals section of the briefing instead.

Look for `Skeleton PRs awaiting finalization: <numbers>` in the refresh output. This lists the 5 most-recently-added skeletons in `_log.md` — both ones just auto-processed in this `/refresh` and any that lingered from prior sessions where the follow-up was skipped. **Proactively** run on that list, without waiting for the user to ask:

1. `/atlas-track <PR numbers>` — rewrite each skeleton into `### Material Changes` / `### Housekeeping` sections with before→after values.
2. `/atlas-analyze <PR numbers>` — summarize impact and fill in each entry's `### Context` section.

If the line reads `(5 most recent of N)` with N > 5, a backlog has accumulated across sessions. Do **not** auto-finalize those — mention the count once and offer to batch-finalize on request. `grep 'skeleton' history/_log.md` lists the full set; `scripts/core/sort-changelogs.py` re-sorts chronologically after a batch finalization if ordering drifts.

Skip this follow-up entirely if the line doesn't appear.

## Reporting back

**Print the briefing output verbatim.** The user wants the exact text from `refresh.sh` — formatted section headers, URLs, percentages, dollar deltas, and all. Do NOT:
- Summarize or paraphrase ("Market: SKY +5.4%, SPK +6.1%...")
- Condense sections into bullet points ("Highlights:")
- Drop the URLs or specific values
- Add your own section headers ("Highlights")

Instead: wrap the briefing output in a fenced code block (or print it directly) and add only one or two optional lines after it:
- If `Auto-processing merged PRs: <numbers>` appeared, a note that you're running `/atlas-track` + `/atlas-analyze` next.
- If a section the user expected is missing (e.g., no market data), a brief flag — otherwise stay silent.

The briefing is already formatted for human consumption. Your job is to pass it through, not to re-interpret it.
