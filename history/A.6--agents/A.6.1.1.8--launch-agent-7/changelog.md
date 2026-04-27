# Launch Agent 7 — Change History

Atlas path: `A.6.1.1.8` (352 docs)

---

## PR #224 — Atlas Edit Proposal — 2026-04-20
**Merged:** 2026-04-24 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- Distribution Requirement Primitive (`A.6.1.1.8.2.3.1`) renamed to "Ecosystem Upkeep Fee Primitive"; Market Cap Fee Primitive subtree (`A.6.1.1.8.2.3.2`) deleted; Upkeep Rebate references updated.

---

## PR #186 — 2026-02-16 AEW proposal
**Merged:** 2026-02-22 | **Type:** Weekly edit (Atlas Axis — Poll 1618) | **+2119/-158 lines**

### Material Changes

- **Launch Agent 7 Artifact created** (`A.6.1.1.8`, new entire subtree — 352 documents): first appearance of Launch Agent 7 in the Atlas. Self-description: "an Agent focused on building structured credit infrastructure across traditional and digital financial markets… serves as a bridge between sophisticated capital and high-quality borrowers"
- **Token Primitive** (`A.6.1.1.8.2.1.4`): token name **Launch Agent 7**, symbol **AGENT7**, Genesis Supply **1 billion**. Token emissions beyond the Genesis Supply are **permanently disabled** (not revertible by LA7 Governance; Sky Governance retains override for Risk Capital violations). Token address and Admin: TBD
- **Agent Type:** Prime Agent (via Prime Transformation Primitive, Status `Completed`)
- **Executor Agent assigned:** Ozone (Operational GovOps Soter Labs, Operational Facilitator Redline Facilitation Group) per `A.6.1.1.8.2.2.1.2.1` — same Executor Accord as other Prime Agents (Skybase, Obex, Pattern, LA6)
- **Root Edit Primitive — Token Holder governance** (`A.6.1.1.8.2.2.2`): LA7 uses **Snapshot-based Prime Governance**:
  - **Proposal submission requires holding ≥1% of circulating AGENT7 supply**
  - 7-day Operational Facilitator (Redline) alignment review
  - Snapshot poll: **3-day voting period**, **≥10% circulating supply participation quorum**, **>50% in favor** to pass
  - Until Powerhouse is live, proposals submitted via Sky Forum under "Launch Agent 7 Prime" category with cryptographic proof of token holdings
  - Emergency protocol permits expedited Root Edit with public reasoning (unless doing so would endanger LA7 or its users)
- **Distribution Requirement Primitive** (`A.6.1.1.8.2.3.1.2.1.1.1`): **Launch Agent 7 will buy back and distribute 0.25% of its total token supply per year** — concrete obligation (process to be defined in future iterations)
- **Upkeep Rebate Primitive** Global Activation Status: `Active`; specific Instance configuration deferred
- **Light Agent Primitive, Market Cap Fee Primitive, Executor Transformation Primitive:** Global Activation Status `Inactive` in this initial artifact — not part of LA7's launch scope

### Housekeeping

- Standard Primitive scaffolding (Hub Documents, Active/Completed/In Progress/Suspended directories) for each Primitive, following the pattern used for other Launch Agents

### Context

Launch Agent 7 is the **second Launch Agent onboarded** (after Launch Agent 6 in PR #107), and the first to be introduced via a dedicated weekly edit rather than a cross-scope OOS edit. Its thesis — structured credit infrastructure across TradFi and DeFi — positions it alongside Pattern (credit-focused) and Obex (also credit/prime-brokerage) as part of Sky's expanding institutional-credit Agent fleet. The fixed 1B genesis supply with permanent emission disablement is stricter than the standard Agent Token model and signals a deflationary or at least non-dilutive tokenomics commitment. The 0.25%/year buyback obligation is small but concrete — the first LA7 protocol-level capital commitment. Token holder governance via Snapshot with a 1% proposal threshold and 10% quorum is comparable to LA6's setup. Key operational unknowns at merge: token address, Admin address, Genesis Account, and buyback process — all deferred to future Artifact iterations. SKY ~$0.065, USDS supply ~$9.9B at merge.

---
