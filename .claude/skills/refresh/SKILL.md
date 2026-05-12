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
2. **Auto-process merged PRs** — runs `scripts/atlas/process-pr.sh` on each unprocessed merged PR. Pipeline (classify-diff → extract-values → enrich → render → auto-context → verify) writes fully-rendered Material/Housekeeping bullets to the affected `history/<entity>/changelog.md` files (status=`auto`). The optional Context paragraph is filled by `claude -p` when available; falls through cleanly otherwise.
3. **Session briefing** — prints only sections that have content: market (daily), spells (current + pending), polls (ended since last session + active), atlas proposals (new open PRs in last 7 days), forum activity (new posts).

`/refresh` does **not** re-sync the Atlas git repo or rebuild the index — that's handled by the SessionStart hook (`scripts/core/atlas-sync.sh`). If the user asks for fresh Atlas commits mid-session, tell them to restart Claude.

## How to invoke

Run the refresh script and surface its output to the user:

```bash
bash scripts/core/refresh.sh
```


## Follow-up: legacy skeleton PRs

Most freshly-processed PRs land at status=`auto` (fully rendered by the pipeline). Legacy entries from before the pipeline existed are still marked `skeleton` and need rewriting.

Look for `Skeleton PRs awaiting finalization: <numbers>` in the refresh output. If it appears, those are pre-pipeline entries — re-process them through the auto pipeline:

```bash
bash scripts/atlas/process-pr.sh --force <PR numbers>
```

`--force` re-runs the full pipeline against the local `.atlas-repo/` and overwrites the skeleton entry with auto-rendered Material/Housekeeping bullets.

If the line reads `(5 most recent of N)` with N > 5, a backlog has accumulated. Mention the count once and offer to batch-process on request rather than auto-running for all of them.

Skip this follow-up entirely if the line doesn't appear.

## Reporting back

**Print the briefing output verbatim.** The user wants the exact text from `refresh.sh` — formatted section headers, URLs, percentages, dollar deltas, and all. Do NOT:
- Summarize or paraphrase ("Market: SKY +5.4%, SPK +6.1%...")
- Condense sections into bullet points ("Highlights:")
- Drop the URLs or specific values
- Add your own section headers ("Highlights")

Instead: wrap the briefing output in a fenced code block (or print it directly) and add only one or two optional lines after it:
- If `Auto-processing merged PRs: <numbers>` appeared, a note that those PRs were rendered by the auto pipeline (status=`auto`) and are ready unless the briefing also flagged legacy skeletons.
- If a section the user expected is missing (e.g., no market data), a brief flag — otherwise stay silent.

The briefing is already formatted for human consumption. Your job is to pass it through, not to re-interpret it.
