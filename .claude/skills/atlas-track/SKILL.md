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
bash scripts/process-pr.sh 217
bash scripts/process-pr.sh 210 211 212   # batch
```

The script generates a skeleton entry in each affected entity's changelog. After processing, **review the output and fill in the `### Context` section** with interpretive analysis:
- What is the practical impact of these changes?
- Do they relate to previous changes in this entity's history?
- Are there cross-entity implications?

### Check for unprocessed PRs

Compare `history/_log.md` against recent merged PRs:

```bash
# List recent merged PRs
gh pr list --repo sky-ecosystem/next-gen-atlas --state merged --limit 20

# See what's already processed
cat history/_log.md
```

Process any gaps.

### Backfill older PRs

To build deeper history, process PRs in chronological order:

```bash
# List all merged PRs (oldest first)
gh pr list --repo sky-ecosystem/next-gen-atlas --state merged --limit 50 --json number,title,mergedAt | jq -r 'sort_by(.mergedAt) | .[] | "#\(.number) \(.mergedAt[:10]) \(.title)"'
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

Before rewriting changelog entries, read `docs/governance-reference.md` for shared governance context. When writing entries:

- **Identify the proposal type** in the entry header: was this a weekly edit (Atlas Axis), an AEP, a SAEP, or a Risk Advisor action?
- **For Active Data changes**: note whether the designated controller is exercising normal authority or if this is a governance override
- **Reference roles by name**: "Atlas Axis weekly edit", "per Risk Advisor recommendation", "SAEP-12 (Spark proposal)"

## Changelog entry format

The script generates a raw skeleton with document-level adds/modifies/deletes. **Your job is to rewrite the entry** into a useful record by reading the actual diff and current Atlas content. The goal: someone reading this changelog months from now should understand what *actually* changed without re-reading any diffs.

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

### Target entry format

```markdown
## PR #219 — Atlas Edit Proposal — 2026-04-06
**Merged:** 2026-04-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Step 4 Capital allocation** restructured from flat split (80% Smart Burn / 20% Staking) to three-stage framework:
  - Stage 0 (current): 37,600 USDS/day to buybacks via Smart Burn, staking rewards funded from SKY token reserves at 75% of prior cycle's Step 4 Capital, remainder to Surplus Buffer
  - Stage 1: same buyback rate, staking from reserves drops to 50%, remainder to Surplus Buffer
  - Stage 2: [specific details]
  - Transition triggers: [thresholds if specified]
- **Target Aggregate Backstop Capital**: 125M → 150M USDS, with Genesis Agent phase-out as aggregate grows
- **Avalanche SkyLink Bridge** added: USDS/sUSDS bridge, 5M USDS/day rate limit, Freezer Multisig 0x4deb...f30 (2/5: Soter×2, Endgame Edge×2, Grove×1)
- **Grove designated Avalanche Pioneer Prime**, added as Freezer Multisig signer
- **Maple syrupUSDC Maximum Exposure** set to [value] per Risk Advisor recommendation

### Housekeeping
- Scope Facilitator → Core Facilitator terminology (12 docs across A.0)
- SubDAO Proxy → Prime Treasury in Spark grant docs
- SLL/GLL abbreviations expanded to full names

### Context
The Avalanche expansion is the headline — three edits together (bridge, Grove as Pioneer Prime,
distribution rewards) establish full operational presence. The staking rewards restructure is
structurally significant: moving from a simple percentage split to a staged framework where
the protocol's revenue distribution evolves as backstop capital grows.

---
```

### The rewrite process

After `process-pr.sh` generates the skeleton:

1. **Read the PR body** from `tmp/pr-<N>-body.md` to understand the intent and edit descriptions
2. **Read the full diff** from `tmp/pr-<N>.diff` (already saved by the script)
3. **Read the current Atlas baseline** for each affected section using `scripts/read-section.sh`
4. **Identify the governance path**: is this a weekly edit (Atlas Axis), AEP, SAEP, or Risk Advisor action? Add a `**Type:**` line to the entry header.
5. **Classify each change** as material or housekeeping
6. **For material changes**: document the specific before→after values by comparing current Atlas vs diff
7. **For housekeeping**: collapse into summary lines
8. **Write the Context section** with cross-cutting interpretation
9. **Replace the script's raw skeleton** with the rewritten entry
10. **Update `_log.md`**: change the entry's status from `skeleton` to `complete`

The script skeleton is a starting point, not the final product. The value of the changelog is in the material changes and context you write, not in the list of document numbers.

### Governance path labels

Use these labels in the `**Type:**` field:

| Label | When to use |
|-------|-------------|
| Weekly edit (Atlas Axis) | PR title matches "Atlas Edit Proposal — YYYY-MM-DD" |
| AEP-N | PR references a formal Atlas Edit Proposal |
| SAEP-N (Spark proposal) | Spark agent edit proposal |
| Risk Advisor action | Changes citing Risk Advisor recommendation |
| Housekeeping | Pure formatting, linting, URL fixes |
| Agent proposal (agent name) | Other agent-specific proposals |
