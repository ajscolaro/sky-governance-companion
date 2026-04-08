# Sky Governance Reference

Shared context for all skills that analyze or track Atlas changes. This is a reference for the agent, not a user-facing document.

## What we're looking at

The Atlas is the governance *document*. It defines rules, parameters, roles, and structures. We track changes to this document — the text, not on-chain execution. When a PR modifies an exposure limit in the Atlas, we're seeing the governance record being updated, not the on-chain transaction itself.

## How Atlas edits happen

```
1. Proposal drafted (AEP, SAEP, weekly edit, or direct authority action)
2. Forum discussion (forum.skyeco.com) — for AEPs and significant changes
3. Ratification Poll (for AEPs only) — on-chain yes/no vote
4. PR opened against next-gen-atlas
5. PR merged — the Atlas text is now updated
```

The on-chain execution of parameter changes (via Executive Votes and spells) is a separate process that we don't track. We track what the Atlas *says* should be the case.

## Proposal types

These help classify PRs during changelog rewriting.

### Atlas Edit Proposals (AEPs)
- Formal proposals requiring a ratification poll before the PR merges
- Structured format: preamble (number, author, status, dates, forum URL), motivation, list of edits, PR link
- Authored by community members or Atlas Axis; ratified by SKY token holders
- See `.atlas-repo/Atlas Edit Proposals/` for examples

### Weekly Edit Proposals
- Bundled edits proposed by Atlas Axis on a weekly cycle
- PR title pattern: "Atlas Edit Proposal — YYYY-MM-DD"
- Can include both material changes and housekeeping
- Housekeeping items can be included by the Core Facilitator without a separate ratification poll (formalized by AEP-1)

### Spark/Agent Edit Proposals (SAEPs)
- Agent-specific proposals (e.g., "SAEP-12: Document Savings Liquidity...")
- Scoped to an agent's operational domain (under A.6.1.1.X)
- Typically authored by the agent's team

### Risk Advisor recommendations
- The Core Council Risk Advisor recommends parameter changes (exposure limits, rate limits, derisking actions)
- These appear in PRs as Active Data updates
- When you see "per Risk Advisor recommendation" in a PR, this is a recognized authority acting within its mandate

### Housekeeping
- Terminology renames, formatting fixes, URL updates, linting
- No governance significance — just document maintenance

## Key governance roles

### Atlas Axis
- Maintains the Atlas document and drafts edit proposals
- Operates the next-gen-atlas GitHub repository
- Weekly edit PRs originate from Atlas Axis

### Core Facilitator (formerly Scope Facilitator)
- Discretionary powers over governance processes
- Can add housekeeping items to governance cycles without a separate ratification poll
- Manages the weekly and monthly governance cycles
- Authority defined in A.1 (Governance Scope)

### Core Council Risk Advisor
- Provides risk recommendations for protocol parameters
- Recommendations appear in PRs as parameter changes to Active Data documents

## Document types and what they mean for changes

When analyzing a PR, the document type tells you about the significance of the change:

| Type | Category | What it means when this changes |
|------|----------|-------------------------------|
| Scope | Immutable | Structural change — very rare, highest significance |
| Article | Immutable | Structural — defines major Atlas sections |
| Section | Immutable | Structural — subdivisions of articles |
| Core | Primary | Substantive rule change — the main thing to watch |
| Active Data Controller | Primary | Changes who/what can modify Active Data |
| Type Specification | Primary | Changes document type rules — very rare |
| Annotation | Supporting | Interpretive context update — lower significance |
| Action Tenet | Supporting | Decision criteria for facilitators |
| Scenario / Variation | Supporting | Specific situation handling |
| Active Data | Adaptive | Live values (addresses, parameters, lists) — changes frequently |

**Key distinction for Active Data:** these documents hold live operational values and can be updated by the designated controller outside the normal edit cycle. When a PR modifies Active Data, the interesting question is *who authorized it* — the controller acting within normal authority, or a governance action overriding the controller.

## On-chain verification (optional)

Some Atlas documents contain addresses, parameters, or rate limits that correspond to on-chain state. If `cast` (Foundry) and `ETH_RPC_URL` are available, the Chainlog contract can be used to look up contract addresses and verify parameter values.

- **Chainlog address:** `0xdA0Ab1e0017DEbCd72Be8599041a2aa3bA7e740F`
- **Query:** `cast call <chainlog> "getAddress(bytes32)(address)" $(cast --from-utf8 "KEY")`

This is useful when a PR claims "currently X, changing to Y" and you want to confirm X matches on-chain reality. It's not relevant to most text-only changes.

## Governance timing patterns

- **Weekly cycle:** Atlas Axis publishes edit proposals weekly (typically Sunday/Monday)
- **Monthly cycle:** larger AEPs may follow a monthly cadence
- **Active Data updates:** can happen independently of the governance cycle when the controller authorizes them
