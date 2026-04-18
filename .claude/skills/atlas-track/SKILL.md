---
name: atlas-track
description: >
  Process merged Atlas PRs into per-entity change history. Maintains the institutional
  memory in history/. Also detects new entities and manages the tracking infrastructure.
argument-hint: "<PR number(s), 'backfill', or 'check'>"
allowed-tools: Bash, Read, Write, Edit, Grep, Glob
---

# Atlas Track

You are maintaining the change history for the Sky Atlas. This is the institutional memory — structured records of what changed, when, and why, organized by entity.

## Commands

### Process specific PRs

```bash
bash scripts/atlas/process-pr.sh 217
bash scripts/atlas/process-pr.sh 210 211 212   # batch
```

The script generates a skeleton entry in each affected entity's changelog. After processing, **review the output and fill in the `### Context` section** with interpretive analysis:
- What is the practical impact of these changes?
- Do they relate to previous changes in this entity's history?
- Are there cross-entity implications?

### Check for unprocessed PRs

Compare `history/_log.md` against recent merged PRs:

```bash
GH_API="https://api.github.com/repos/sky-ecosystem/next-gen-atlas"

# List recent merged PRs
curl -sf "$GH_API/pulls?state=closed&sort=updated&direction=desc&per_page=20" \
    | jq -r '.[] | select(.merged_at != null) | "#\(.number) \(.merged_at[:10]) \(.title)"'

# See what's already processed
cat history/_log.md
```

Process any gaps.

### Backfill older PRs

To build deeper history, process PRs in chronological order:

```bash
# List all merged PRs (oldest first)
curl -sf "$GH_API/pulls?state=closed&sort=updated&direction=desc&per_page=50" \
    | jq -r '[.[] | select(.merged_at != null)] | sort_by(.merged_at) | .[] | "#\(.number) \(.merged_at[:10]) \(.title)"'
```

Then batch process. The script skips already-processed PRs.

## History structure

```
history/
├── _log.md                    # master PR processing log
├── entity-routing.conf        # prefix → directory mapping
├── _other/changelog.md        # catch-all for unrouted changes
│
├── A.0--preamble/changelog.md
├── A.1--governance/changelog.md
├── A.2--support/changelog.md
├── A.3--stability/changelog.md
├── A.4--protocol/changelog.md
├── A.5--accessibility/changelog.md
│
└── A.6--agents/
    ├── changelog.md                          # scope-level / cross-agent
    ├── A.6.1.1.1--spark/changelog.md
    ├── A.6.1.1.2--grove/changelog.md
    ├── A.6.1.1.3--keel/changelog.md
    ├── A.6.1.1.4--skybase/changelog.md
    ├── A.6.1.1.5--obex/changelog.md
    ├── A.6.1.1.6--pattern/changelog.md
    ├── A.6.1.1.7--launch-agent-6/changelog.md
    └── A.6.1.1.8--launch-agent-7/changelog.md
```

### Design rules

1. **Every scope gets a directory** with a `changelog.md`
2. **Agents each get their own subdirectory** under `A.6--agents/`
3. **Changes route to the most specific prefix** in `entity-routing.conf`
4. **Unmatched changes go to `_other/`** — review periodically for mis-routing

### Splitting a scope changelog

When a scope-level changelog grows too large (50+ entries), split it by creating article-level subdirectories — the same pattern as agents under `A.6`:

1. Create `history/A.1--governance/A.1.9--security/changelog.md`
2. Add a routing line: `A.1.9	A.1--governance/A.1.9--security`
3. Move relevant existing entries from the parent changelog to the new file
4. The parent changelog continues to catch changes to articles that don't have their own subdirectory

## Entity routing

`history/entity-routing.conf` maps Atlas path prefixes to history directory paths (relative to `history/`):

```
# Agents (most specific — matched before scope catch-all)
A.6.1.1.1	A.6--agents/A.6.1.1.1--spark
A.6.1.1.2	A.6--agents/A.6.1.1.2--grove
...
# Scopes (catch-all)
A.1	A.1--governance
A.6	A.6--agents
```

**Order matters.** Most specific prefixes first. The script walks top to bottom and uses the first match.

## Detecting and adding new entities

**Watch for these signals:**
- Changes routed to `_other/changelog.md` — may indicate a new entity needs its own directory
- Changes routed to `A.6--agents/changelog.md` (the scope-level catch-all) — may be a new agent
- New documents appearing under `A.6.1.1` with a previously unseen number
- PR titles mentioning new agents or organizational structures

**To add a new agent (e.g., "Forge" at `A.6.1.1.9`):**

1. Create the directory and changelog:
   ```bash
   mkdir -p history/A.6--agents/A.6.1.1.9--forge
   ```
   Create `history/A.6--agents/A.6.1.1.9--forge/changelog.md`:
   ```markdown
   # Forge — Change History

   Atlas path: `A.6.1.1.9` — <description from the Atlas>

   ---
   ```

2. Add a routing entry in `entity-routing.conf`:
   ```
   A.6.1.1.9	A.6--agents/A.6.1.1.9--forge
   ```
   Insert in the agents section, before the `A.6` catch-all line.

3. Update the history structure in `CLAUDE.md`.

4. If the creation PR was already processed, move relevant entries from `_other/changelog.md` or `A.6--agents/changelog.md` to the new file.

## Governance context

Before rewriting changelog entries, read `docs/governance-reference.md` for shared governance context.

**Two governance flows produce Atlas PRs:**
- **Flow 1 (text edits):** Forum → ratification poll → PR merged same day poll ends. Covers weekly edits, AEPs, SAEPs. No executive spell involved.
- **Flow 2 (spell recording):** Executive spell cast on-chain → PR records changes 4-11 days later. These PRs have "spell changes" or "executive changes" in the title.

Flow 1 PRs are governance decisions. Flow 2 PRs are documentation of on-chain execution. Don't expect Flow 1 PRs to reference spells — they won't have any.

When writing entries:

- **Identify the proposal type** in the entry header: was this a weekly edit (Atlas Axis), an AEP, a SAEP, a Risk Advisor action, or a spell recording?
- **For Flow 1 PRs**: look up the authorizing poll in `data/voting/polls/vote-matrix.json` — polls with `atlas_pr` matching the PR number give you the poll ID, vote result, and AD participation
- **For Flow 2 PRs**: cross-reference with `data/voting/executive/lifecycle.json` to find the spell, its actions, and market context at cast time
- **For Active Data changes**: note whether the designated controller is exercising normal authority or if this is a governance override
- **Reference roles by name**: "Atlas Axis weekly edit", "per Risk Advisor recommendation", "SAEP-12 (Spark proposal)"

## Changelog entry format

The script generates a raw skeleton with document-level adds/modifies/deletes. **Your job is to rewrite the entry** into a terse, RAG-optimized record. The diff is the source of truth; this changelog is an index into it. Someone skimming for "what changed when" should be able to decide from the entry alone whether to pull up the diff.

### What to track closely (material changes)

These are the changes that matter to SKY holders, USDS holders, agent token holders, and protocol participants:

- **Parameter adjustments**: rate limits, exposure limits, allocation ratios, thresholds — always record `was X → now Y`
- **Capital allocation / spending**: anything affecting how protocol revenue flows (Step 4 Capital, Surplus Buffer, Smart Burn, staking rewards)
- **Disbursements / grants**: capital transfers, Genesis Capital allocations, reward distributions
- **Risk Advisor recommendations**: exposure caps, derisking actions, new risk parameters
- **New infrastructure**: bridges, vaults, chain expansions, new primitives being onboarded
- **Governance authority changes**: who can approve what, emergency powers, facilitator roles
- **Agent operational changes**: new chain deployments, Pioneer Prime designations, multisig signer changes

### What to summarize briefly (housekeeping)

These get a single line, not a detailed breakdown:

- Terminology renames (e.g., "Scope Facilitator → Core Facilitator across 12 documents")
- Abbreviation expansions, spelling fixes, formatting/linting
- Pure renumbering (document shifted position, no content change)
- Broken link fixes, forum URL updates

### Including identifiers (UUIDs, paths, addresses)

These are stable navigation anchors — include them where they make future cross-referencing cheaper, skip them where they add noise.

- **UUIDs**: include for new entities (new instance, new primitive, new artifact) and for renumberings where the UUID is preserved (makes it clear the identity carried over). UUIDs are immutable across Atlas renumberings, so they're the most durable anchor for grep. Don't dump UUID lists for every touched document in a sweeping edit.
- **Atlas paths** (`A.6.1.1.1.2.6.1...`): include when naming new entities — they give human-readable tree context. Fine to omit for well-known scopes.
- **Contract addresses**: include only for genuinely new infrastructure (new ALM Controller, new Bridge, new Vault). Don't reproduce full multisig signer address lists or every touched contract.

### Target entry format (RAG-optimized)

Entries are short and grep-friendly. Include specific magnitudes, before→after values, and stable identifiers (UUIDs, paths) that aid retrieval. Skip address dumps, exhaustive parameter tables, and nested sub-bullets more than one level deep.

**Substantive PR** (weekly edit, AEP, SAEP, spell recording):

```markdown
## PR #N — <Title>
**Merged:** YYYY-MM-DD | **Type:** <governance path label>

### Material Changes
- **<Thing>**: <terse before→after or key fact>
- **<New entity/instance>** (`<Atlas path>`, UUID `<short>…<short>`): <1-line summary>

### Housekeeping
- <one-line summary, collapsed>

### Context
<0-2 sentences. Cross-reference prior PRs where obvious. Skip the section entirely if nothing worth saying.>

---
```

**Trivial housekeeping PR** (whitespace, typos, renumbers, single-file cleanup):

```markdown
## PR #N — <Title>
**Merged:** YYYY-MM-DD | **Type:** Housekeeping

<1-2 sentences describing what was cleaned up and where.>

---
```

Target length: 5-15 lines substantive, 3-5 lines trivial. If you catch yourself writing three-level bullet sub-lists or reproducing multisig signer rosters, you're over the bar — drop the detail and let the diff carry it.

### The rewrite process

After `process-pr.sh` generates the skeleton:

1. **Read the PR body** from `tmp/pr-<N>-body.md` to understand the intent and edit descriptions
2. **Read the full diff** from `tmp/pr-<N>.diff` (already saved by the script). For huge diffs (>5000 lines), sample with `head -500` and lean on the body + `gh pr view <N> --repo sky-ecosystem/next-gen-atlas --json files`.
3. **Identify the governance path** (weekly edit, AEP, SAEP, spell recording, etc. — see label table below)
4. **Classify each change** as material or housekeeping
5. **For material changes**: document specific before→after values from the diff. Only read the current Atlas baseline (`scripts/atlas/read-section.sh`) if the diff alone doesn't make the prior value clear.
6. **For housekeeping**: collapse into one or two summary lines
7. **(Optional) Market context**: For genuinely significant capital allocation, exposure, or framework changes, run `python3 scripts/market/market-lookup.py --date <merge-date> --format context` and weave the 1-line summary into the Context section. Skip for routine edits.
8. **Write the Context section** (or skip if nothing interesting to say — don't pad)
9. **Replace the script's raw skeleton** with the rewritten entry
10. **Update `_log.md`**: change status from `skeleton` to `complete` and populate the "Sections Affected" column
11. **Re-sort if needed**: `/atlas-track` appends new entries in processing order. If the parent changelog ends up out of order, run `python3 scripts/core/sort-changelogs.py` for a repo-wide chronological sort (most-recent-first).

The script skeleton is a starting point, not the final product. The value of the changelog is in terse, searchable material-change bullets with stable identifiers for navigation — not in exhaustive reconstruction of the diff.

### Governance path labels

Use these labels in the `**Type:**` field:

| Label | When to use | Flow |
|-------|-------------|------|
| Weekly edit (Atlas Axis) | PR title matches "Atlas Edit Proposal — YYYY-MM-DD" | 1 (text edit) |
| Weekly edit (out-of-schedule) | Weekly-style edit merged outside the normal Axis cadence | 1 (text edit) |
| AEP-N | PR references a formal Atlas Edit Proposal | 1 (text edit) |
| SAEP-N (Spark proposal) | Formal numbered Spark Atlas Edit Proposal | 1 (text edit) |
| Spark proposal (<descriptor>) | Informal (non-SAEP) Spark-initiated proposal — e.g., "Spark proposal (new SLL instance)", "Spark proposal (risk parameter update)" | 1 (text edit) |
| Risk Advisor action | Changes citing Risk Advisor recommendation | 1 (text edit) |
| Spell recording (YYYY-MM-DD) | PR title contains "spell changes" or "executive changes"; date is the spell cast date (from the title, not the merge date) | 2 (on-chain) |
| Housekeeping | Pure formatting, linting, URL fixes | 1 (admin) |
| Agent proposal (agent name) | Informal agent-initiated proposals from agents other than Spark | 1 (text edit) |

## Complementary skills

When writing changelog Context sections, use other skills for richer analysis — see "Cross-domain questions" in CLAUDE.md:
- `/messari-market-data` — market environment at merge date (the `--window` and `--format context` CLI flags are especially useful)
- `/governance-data` — poll results (`atlas_pr` field links polls to PRs), spell lifecycle for Flow 2 PRs
- `/atlas-analyze` — if you need a deeper diff analysis before writing the changelog entry
- `/forum-search` — discussion context behind proposals
