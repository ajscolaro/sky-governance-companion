# Launch Agent 7 — Change History

Atlas path: `A.6.1.1.8` (352 docs)

---

## PR #253 — Atlas Edit Proposal — 2026-06-01
**Merged:** 2026-06-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Agent Creation Primitive** (`A.6.1.1.8.2.1.1`): `4` → `5`
- **Prime Transformation Primitive** (`A.6.1.1.8.2.1.2`): `4` → `5`
- **Executor Transformation Primitive** (`A.6.1.1.8.2.1.3`): `4` → `5`
- **Agent Token Primitive** (`A.6.1.1.8.2.1.4`): `4` → `5`
- **Genesis Primitives** (`A.6.1.1.8.2.1`): `4` → `5`
- **Executor Accord Primitive** (`A.6.1.1.8.2.2.1`): `5` → `6`
- **Root Edit Primitive** (`A.6.1.1.8.2.2.2`): `5` → `6`
- **Light Agent Primitive** (`A.6.1.1.8.2.2.3`): `5` → `6`
- **Operational Primitives** (`A.6.1.1.8.2.2`): `5` → `6`
- **Ecosystem Upkeep Fee Primitive** (`A.6.1.1.8.2.3.1`): `6` → `7`
- **Upkeep Rebate Primitive** (`A.6.1.1.8.2.3.2`): `6` → `7`
- **Ecosystem Upkeep Primitives** (`A.6.1.1.8.2.3`): `6` → `7`
- **Token SkyLink Primitive** (`A.6.1.1.8.2.4.1`): `7` → `8`
- **SkyLink Primitives** (`A.6.1.1.8.2.4`): `7` → `8`
- **Distribution Reward Primitive** (`A.6.1.1.8.2.5.1`): `8` → `9`
- **Integration Boost Primitive** (`A.6.1.1.8.2.5.2`): `8` → `9`
- **Pioneer Chain Primitive** (`A.6.1.1.8.2.5.3`): `8` → `9`
- **Demand Side Stablecoin Primitives** (`A.6.1.1.8.2.5`): `8` → `9`
- **Allocation System Primitive** (`A.6.1.1.8.2.6.1`): `9` → `10`
- **Junior Risk Capital Rental Primitive** (`A.6.1.1.8.2.6.2`): `9` → `10`
- **Asset Liability Management Rental Primitive** (`A.6.1.1.8.2.6.3`): `9` → `10`
- **Supply Side Stablecoin Primitives** (`A.6.1.1.8.2.6`): `9` → `10`
- **Core Governance Reward Primitive** (`A.6.1.1.8.2.7.1`): `10` → `11`
- **Core Governance Primitives** (`A.6.1.1.8.2.7`): `10` → `11`

### Housekeeping
- `5` → `6` across 4 docs.
- `9` → `10` across 4 docs.
- `10` → `11` across 2 docs.
- `8` → `9` across 4 docs.
- `4` → `5` across 5 docs.
- `7` → `8` across 2 docs.
- `6` → `7` across 3 docs.

### Context
All changes are version-reference bumps propagated from the Support Scope (A.2) primitive-tree reorganization and the Capital Ratio Requirement rename — no agent-specific operational change.

---

## PR #242 — Atlas Edit Proposal — 2026-05-11
**Merged:** 2026-05-15 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Root Edit Voting Process In Emergency Situations** (`A.6.1.1.8.2.2.2.2.1.2.3.1`): `8` → `9`
- **In Progress Invocations Directory** (`A.6.1.1.8.2.6.1.1.4`): `d0c5ad5f` → `952b34e6`; `ffe6` → `7983`; `469b` → `4dd0`; `b4e8` → `a46f`; `1f77b1a24739` → `e3622c2346de`

### Housekeeping
- `8` → `9` across 1 doc.

---

## PR #224 — Atlas Edit Proposal — 2026-04-20
**Merged:** 2026-04-24 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- Distribution Requirement Primitive (`A.6.1.1.8.2.3.1`) renamed to "Ecosystem Upkeep Fee Primitive"; Market Cap Fee Primitive subtree (`A.6.1.1.8.2.3.2`) deleted; Upkeep Rebate references updated.

---

## PR #200 — 2026-03-16 Weekly Edit Proposal
**Merged:** 2026-03-20 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **SubProxy Account** (`A.6.1.1.8.2.1.1.3.1.1.2`): address set — `0x56a9bA5FE133EF4Ab1131E8ac7c4312a52284f5B` (Ethereum Mainnet).
- **StarGuard Contract** (`A.6.1.1.8.2.1.1.3.1.1.3`): new section — address `0xB36e88c02E4619Ef34C0Db76C5BCb6655747FB28` (Ethereum Mainnet); prior "Genesis Account" heading removed (UUID preserved).
- Additional new sections: Pioneer Chain / Allocation System / Junior Risk Capital / ALM Rental / Core Governance Reward Primitive directory scaffolding for Launch Agent 7's Liquidity Layer; existing instance directory link-text fixes.

---

## PR #187 — 2026-02-23 Atlas Edit Weekly Cycle Proposal
**Merged:** 2026-03-05 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Active Instances / Completed Instances / In Progress Invocations typo fixes** (`A.6.1.1.8.2.1.1.1.2`, `.1.1.3`, `.2.2.1.1.4`, `.2.6.2.1.5.1`): section title typos corrected ("Intances" → "Instances", "Invocactions" → "Invocations", "Invoecations" → "Invocations").
- **Agent-Specific Emergency Response** (`A.6.1.1.8.2.3.1.3` removed, `A.6.1.1.8.3.1.3` added): section moved from `.2.3.1.3` to `.3.1.3` (renumbering fix; UUID `3581ec81` preserved).

### Housekeeping
- Additional link-text fixes across 7 other sections.

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
