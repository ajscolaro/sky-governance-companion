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
3. **AD pipeline detection** — rebuilds `data/delegates/roster.json` from Atlas (so new ADs are picked up), then diffs it against `delegates/_roster.md` to surface roster drift, and counts cached forum posts not yet rendered into each `delegates/<slug>/comms.md`. The summarization itself is judgment work, so it's not done in-script — refresh surfaces the queue and the session processes it via `/ad-track` (see follow-up below).
4. **Session briefing** — prints only sections that have content: market (daily), spells (current + pending), polls (ended since last session + active), atlas proposals (new open PRs in last 7 days), forum activity (new posts).

`/refresh` does **not** re-sync the Atlas git repo or rebuild the index — that's handled by the SessionStart hook (`scripts/core/atlas-sync.sh`). If the user asks for fresh Atlas commits mid-session, tell them to restart Claude.

## How to invoke

Run the refresh script and surface its output to the user:

```bash
bash scripts/core/refresh.sh
```

## Reporting back

**The session briefing is the primary deliverable — print it verbatim every time, even when nothing else fired.** The user wants the exact text from `refresh.sh`'s briefing section (everything from `Session briefing — new activity since ...` onward) — formatted section headers, URLs, percentages, dollar deltas, and all. Do NOT:

- Skip the briefing because no follow-up triggers fired. A "quiet" refresh (no new PRs, no drift, no skeletons) is the *most* common case and the briefing still contains current market / spells / polls / forum activity that the user wants.
- Summarize or paraphrase ("Market: SKY +5.4%, SPK +6.1%...").
- Condense sections into bullet points or add your own section headers.
- Drop URLs or specific values.

Wrap the briefing output in a fenced code block (or print it directly). The briefing is already formatted for human consumption — pass it through, don't re-interpret it.

After the briefing, optionally add one or two lines for follow-up signals only when they actually appeared in the refresh output (see follow-up sections below). If no follow-ups fired, end with the briefing — do not add a "nothing pending" summary.

## Follow-up: AD roster drift and unprocessed rationales (conditional)

Refresh.sh emits these AD pipeline signals *before* the briefing only when there is work to do. If neither appears in the output, skip this section entirely — do not mention them.

- **`AD roster drift vs delegates/_roster.md:`** — the Atlas roster contains ADs not in `_roster.md`, or vice versa. Invoke `/ad-track sync` to update `_roster.md`, create/derecognize delegate directories, and fetch any new ADs' RSS history.
- **`AD rationales awaiting processing (N across M delegate(s)):`** — cached forum posts in `data/delegates/<slug>/` that aren't yet rendered into `delegates/<slug>/comms.md`. Invoke `/ad-track` to summarize and append them. If the total is large (say > 50 across all delegates), mention the count once and offer to process in batches rather than firing off one massive run.

When invoking `/ad-track` for processing, follow the schema in `delegates/<slug>/comms.md` exactly — newest entry at the **top** (right after the header's `---`), each entry headed by `## YYYY-MM-DD — <topic>`, with the source forum URL embedded as a footnote line (`*Source: <link>*`) so `find-unprocessed.py` can detect it as processed on the next refresh.

## Follow-up: legacy skeleton PRs (conditional)

This appears only if refresh.sh printed `Skeleton PRs awaiting finalization: <numbers>`. If you don't see that line, skip this section entirely.

When it does appear, those are pre-pipeline entries — re-process them through the auto pipeline:

```bash
bash scripts/atlas/process-pr.sh --force <PR numbers>
```

`--force` re-runs the full pipeline against the local `.atlas-repo/` and overwrites the skeleton entry with auto-rendered Material/Housekeeping bullets.

If the line reads `(5 most recent of N)` with N > 5, a backlog has accumulated. Mention the count once and offer to batch-process on request rather than auto-running for all of them.

## Follow-up: auto-processed PRs (conditional)

If `Auto-processing merged PRs: <numbers>` appeared in the refresh output, add a one-line note after the briefing that those PRs were rendered by the auto pipeline (status=`auto`) and are ready unless the briefing also flagged legacy skeletons. Skip if the line didn't appear.
