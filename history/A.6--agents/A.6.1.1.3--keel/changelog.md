# Keel — Change History

Atlas path: `A.6.1.1.3` (874 docs)

---

## PR #253 — Atlas Edit Proposal — 2026-06-01
**Merged:** 2026-06-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Agent Creation Primitive** (`A.6.1.1.3.2.1.1`): `4` → `5`
- **Prime Transformation Primitive** (`A.6.1.1.3.2.1.2`): `4` → `5`
- **Executor Transformation Primitive** (`A.6.1.1.3.2.1.3`): `4` → `5`
- **Agent Token Primitive** (`A.6.1.1.3.2.1.4`): `4` → `5`
- **Genesis Primitives** (`A.6.1.1.3.2.1`): `4` → `5`
- **Executor Accord Primitive** (`A.6.1.1.3.2.2.1`): `5` → `6`
- **Root Edit Primitive** (`A.6.1.1.3.2.2.2`): `5` → `6`
- **Light Agent Primitive** (`A.6.1.1.3.2.2.3`): `5` → `6`
- **Operational Primitives** (`A.6.1.1.3.2.2`): `5` → `6`
- **Ecosystem Upkeep Fee Primitive** (`A.6.1.1.3.2.3.1`): `6` → `7`
- **Upkeep Rebate Primitive** (`A.6.1.1.3.2.3.2`): `6` → `7`
- **Ecosystem Upkeep Primitives** (`A.6.1.1.3.2.3`): `6` → `7`
- **Token SkyLink Primitive** (`A.6.1.1.3.2.4.1`): `7` → `8`
- **SkyLink Primitives** (`A.6.1.1.3.2.4`): `7` → `8`
- **Routine Protocol** (`A.6.1.1.3.2.5.1.2.1.2.1`): `8` → `9`; `8` → `9`; `5` → `3`
- **Tracking Methodology** (`A.6.1.1.3.2.5.1.2.2.1.2`): `8` → `9`; `2` → `1`
- **Routine Protocol** (`A.6.1.1.3.2.5.1.2.2.2.1`): `8` → `9`; `8` → `9`; `5` → `3`
- **Distribution Reward Primitive** (`A.6.1.1.3.2.5.1`): `8` → `9`
- **Routine Protocol** (`A.6.1.1.3.2.5.2.2.1.2.1`): `8` → `9`; `8` → `9`
- **Routine Protocol** (`A.6.1.1.3.2.5.2.2.2.2.1`): `8` → `9`; `8` → `9`
- **Routine Protocol** (`A.6.1.1.3.2.5.2.2.3.2.1`): `8` → `9`; `8` → `9`
- **Routine Protocol** (`A.6.1.1.3.2.5.2.2.4.2.1`): `8` → `9`; `8` → `9`
- **Routine Protocol** (`A.6.1.1.3.2.5.2.3.1.2.1`): `8` → `9`; `8` → `9`
- **Integration Boost Primitive** (`A.6.1.1.3.2.5.2`): `8` → `9`
- **Terms** (`A.6.1.1.3.2.5.3.2.1.1.2.2`): `8` → `9`
- **Pioneer Chain Primitive** (`A.6.1.1.3.2.5.3`): `8` → `9`
- **Demand Side Stablecoin Primitives** (`A.6.1.1.3.2.5`): `8` → `9`
- **Keel’s Total Risk Capital (TRC) Management Processes** (`A.6.1.1.3.2.6.1.2.1.3.2`): `9` → `10`
- **Junior Risk Capital Rental Primitive** (`A.6.1.1.3.2.6.2`): `9` → `10`
- **Asset Liability Management Rental Primitive** (`A.6.1.1.3.2.6.3`): `9` → `10`
- **Supply Side Stablecoin Primitives** (`A.6.1.1.3.2.6`): `9` → `10`
- **Core Governance Reward Primitive** (`A.6.1.1.3.2.7.1`): `10` → `11`
- **Core Governance Primitives** (`A.6.1.1.3.2.7`): `10` → `11`

### Housekeeping
- `5` → `6` across 4 docs.
- `9` → `10` across 4 docs.
- `10` → `11` across 2 docs.
- `8` → `9` across 13 docs.
- `4` → `5` across 5 docs.
- `7` → `8` across 2 docs.
- `2` → `1` across 1 doc.
- `5` → `3` across 2 docs.
- `6` → `7` across 3 docs.

### Context
All changes are version-reference bumps propagated from the Support Scope (A.2) primitive-tree reorganization and the Capital Ratio Requirement rename — no Keel-specific operational change.

---

## PR #242 — Atlas Edit Proposal — 2026-05-11
**Merged:** 2026-05-15 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: 1inch Instance Configuration Document Location** (`A.6.1.1.3.2.5.1.1.2.2`, UUID `60982fac…d4a5`): This Instance's associated Instance Configuration Document is located at `A.6.1.1.3.2.5.1.2.2`.
- **New: 1inch Instance Configuration Document** (`A.6.1.1.3.2.5.1.2.2`, UUID `eca1c14e…a1d2`): The documents herein contain the Instance Configuration Document for the 1inch Distribution Reward Primitive Instance.
  - **Reward Code** (`A.6.1.1.3.2.5.1.2.2.1.1`): `4011`.
  - **Tracking Methodology** (`A.6.1.1.3.2.5.1.2.2.1.2`): This Instance uses the Tracking Methodology specified in `A.2.2.8.1.2.1.2.2.1`.
  - **Custom Instance Parameters** (`A.6.1.1.3.2.5.1.2.2.1.3`): The documents herein define the custom parameters of the 1inch Instance of the Distribution Reward Primitive, if any.
  - **Routine Protocol** (`A.6.1.1.3.2.5.1.2.2.2.1`): This document defines the protocol for routine ongoing management of the 1inch Instance.
  - **Agent Customizations** (`A.6.1.1.3.2.5.1.2.2.2.1.1`): The Prime Agent may define instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas.
  - **Non-Routine Protocol** (`A.6.1.1.3.2.5.1.2.2.2.2`): The documents herein define the protocol for non-routine ongoing management of the 1inch Instance of this Distribution Reward Primitive.
  - **Emergency Protocol** (`A.6.1.1.3.2.5.1.2.2.2.3`): The documents herein define the protocol for handling emergency situations in the ongoing management of the 1inch Instance of this Distribution Reward Primitive.
  - **Initial Planning** (`A.6.1.1.3.2.5.1.2.2.3.1`): The materials associated with initial planning of the Invocation of this Instance are contained herein.
  - **Operational GovOps Review** (`A.6.1.1.3.2.5.1.2.2.3.2`): The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.
  - **Artifact Edit Proposal** (`A.6.1.1.3.2.5.1.2.2.3.3`): The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.
  - **Distribution Reward Payments** (`A.6.1.1.3.2.5.1.2.2.3.4`): The Distribution Reward payments for the 1inch Instance of the Distribution Reward Primitive are defined as Active Data.
  - **List Of Distribution Reward Payments** (`A.6.1.1.3.2.5.1.2.2.3.4.0.6.1`): The Distribution Reward Payments are.
- **Root Edit Voting Process in Urgent and Emergency Situations** (`A.6.1.1.3.2.2.2.2.1.2.3.1`): `8` → `9`

### Housekeeping
- `A.6.1.1.3.2.5.3.2.1.1.2.2` (Terms): removed refs to `A.2.8.2.3`
- `8` → `9` across 1 doc.
- `Facilitators` → `Core Facilitator` across 2 docs.

### Context
Adds the 1inch Distribution Reward Instance Configuration Document at `A.6.1.1.3.2.5.1.2.2` (reward code 4011) — the latest Distribution Reward Primitive instance under Keel — as one of nine edits bundled in the May 11 weekly cycle (Poll #1632).

---

## PR #237 — Atlas Edit Proposal — 2026-05-04
**Merged:** 2026-05-08 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- Solidity identifier whitespace fix across Keel ALM Controller and Rate Limit Management docs (`A.6.1.1.3.2.6.1.2.2.1.1.{1.3, 2.1.2.1.1.1, 2.1.2.2.1.1, 3, 3.1–3.5}`): `Rate Limits` → `RateLimits`, `Rate LimitData` → `RateLimitData`, `setRate LimitData` → `setRateLimitData`, `getCurrentRate Limit` → `getCurrentRateLimit`, `triggerRate LimitDecrease` → `triggerRateLimitDecrease`, plus revert-string and event-name corrections.

### Context
Cosmetic but consequential — the previous spaced forms were not valid Solidity and would not compile if copied. Same fix applied to Obex and Pattern in this PR. Ratified by Poll #1631 (10-0).

---

## PR #224 — Atlas Edit Proposal — 2026-04-20
**Merged:** 2026-04-24 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- Distribution Requirement Primitive (`A.6.1.1.3.2.3.1`) renamed to "Ecosystem Upkeep Fee Primitive"; Market Cap Fee Primitive subtree (`A.6.1.1.3.2.3.2`) deleted; Upkeep Rebate references updated.

---

## PR #222 — Atlas Edit Proposal — 2026-04-13
**Merged:** 2026-04-16 | **Type:** Weekly edit (Atlas Axis — Poll 1628) | **+1232/-32 lines**

### Material Changes

- **New instance: Solana Bridge Distribution Reward** (`A.6.1.1.3.2.5.1.2.1`, new Instance Configuration Document): first Solana-specific Keel instance
  - **Reward Code: `4001`**
  - **Tracking Methodology:** synthetic tagging of deposits and withdrawals from the LayerZero contract on Ethereum (**`0x1e1D4278…d01B8`**) minus running balances already attributed to other Distribution Reward Instances
  - Inherits base routine protocol from `A.2.2.8.1.2.4.1`, scoped to the "Near-Term Process" qualifications at `A.2.2.8.1.2.1.5.3.1`; no agent-specific customizations
  - Distribution Reward Payments Active Data list initialized empty; Responsible Party: Operational GovOps; Update Process: 'Direct Edit'

### Housekeeping

- Added Instance Configuration Document Location pointer at `A.6.1.1.3.2.5.1.1.2.1` in Keel's Distribution Reward Primitive Active Instances Directory

### Context

Keel tags USDS that bridges to Solana via LayerZero for Distribution Reward eligibility — this is the on-chain instrumentation of the "Solana SkyLink Bridge" infrastructure that was established in PR #219 (which renamed "Solana LayerZero Bridge" → "Solana SkyLink Bridge" and formalized its freezer multisig). Reward Code 4001 sits alongside other bridge-related codes in Keel's growing Distribution Reward portfolio, and the synthetic-tagging methodology (deposits minus already-attributed balances from the same LayerZero contract address) accounts for the fact that the underlying LZ contract is shared across multiple Reward Code claimants. Empty Payments list indicates the instance is configured but not yet accruing at merge. SKY ~$0.075, USDS supply ~$11.3B at merge.

---

## PR #219 — Atlas Edit Proposal — 2026-04-06
**Merged:** 2026-04-09 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Solana Pioneer Chain Instance Configuration Document added** (A.6.1.1.3.2.5.3.2.1, new): Formalizes Keel's Solana Pioneer Chain Primitive instance with:
  - Network: Solana
  - Pioneer Incentive Pool address: `8JmDPG5BFQ6gpUPJV9xBixYJLqTKCSNotkXksTmNsQfj` (previously referenced in Ecosystem Accord text only)
  - Terms: governed by A.2.2.8.3.1.4 (Pioneer Incentive Pool) and A.2.8.2.3 (Ecosystem Accord 3)

- **Three Keel Ecosystem Accord provisions removed** (A.2.8.2.3.2): Became obsolete after the Genesis Capital Allocation transfer in the March 26, 2026 Executive Vote:
  1. Transfer from Liquidity Bootstrapping Budget to Keel — 500,000 USDS advance for Solana DeFi liquidity (Solana multisig `6cTVPDJ8WR1XGxdgnjzhpYKRqcv78T4Nqt95DY8dvMmn`) and associated development expense clause
  2. Keel Senior Risk Capital — 7.5M USDS short-term Senior Risk Capital credited to Total Risk Capital (not transferred via SubProxy)
  - Remaining Ecosystem Accord 3 provisions renumbered (A.2.8.2.3.2.1 onward)

### Context
The Solana Instance Configuration Document formalizes what was previously only embedded in Ecosystem Accord narrative text — the Pioneer Incentive Pool address is unchanged, just moved to the proper structural location. The Ecosystem Accord cleanup closes out the bootstrapping chapter: Keel received 10M USDS Genesis Capital in the March 26 spell, superseding the earlier piecemeal advances and credit mechanisms. Keel's capitalization is now governed by the standard Genesis Agent framework rather than bespoke provisions.

---

## PR #217 — Atlas Edit Proposal — 2026-03-30
**Merged:** 2026-04-02 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Keel operating company renamed: Matariki Labs → Elodin** (`A.2.8.2.3.1.1.2` Keel Details): the party "Keel" now comprises the Keel Prime Agent, Keel Foundation, and **Elodin** (previously Matariki Labs).
- **Pre-Pioneer Incentive Pool → Pioneer Incentive Pool** (Ecosystem Accord 3, `A.2.8.2.3`): Keel's eligibility restructured from a Pre-Pioneer Incentive Pool to the standard Pioneer Incentive Pool (`A.2.2.8.3.1.4`), with a Keel-specific carve-out — Keel **retains 100%** of allocated funds and is not required to distribute any to third parties; use is supervised by the Operational Executor Agent. Monthly payments now sourced from the **Demand Side Buffer** rather than the Integration Boost wallets. Pioneer Incentive Pool wallet on Solana unchanged: `8JmDPG5BFQ6gpUPJV9xBixYJLqTKCSNotkXksTmNsQfj`.

### Context
First appearance of "Elodin" as Keel's operating company (rebrand from Matariki Labs, which was introduced in PR #66). Part of a larger weekly edit that also migrated the Emergency Response and Spell framework to the Agent Framework (see `../../A.1--governance/changelog.md`). Precedes the March 26 Genesis Capital transfer recorded in PR #219, which closed out Keel's bespoke bootstrapping provisions.

---

## PR #200 — 2026-03-16 Weekly Edit Proposal
**Merged:** 2026-03-20 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core Operator Relayer Multisig** (`A.6.1.1.3.2.6.1.2.1.2.2.2`, `.2.3.3`, `.2.3.3.4`, `.2.3.3.6`): "Operational GovOps Amatsu" → **"Operational GovOps Soter Labs"** throughout (relayer role holder and multisig signer/modifier).
- **Freezer Multisig Signers** (`A.6.1.1.3.2.6.1.2.1.2.3.4.4`): "Operational GovOps Amatsu" → "Operational GovOps Soter Labs."

---

## PR #187 — 2026-02-23 Atlas Edit Weekly Cycle Proposal
**Merged:** 2026-03-05 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- 6 sections: link-text normalization in Keel instance config documents. No parameter values changed.

---

## PR #172 — Jan 26 Edit
**Merged:** 2026-01-29 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- Global "Launch Agent 2" → "Keel" rename across all subdocs in `A.6.1.1.3`: token/doc descriptions, buy-back references, Upkeep Rebate, Market Cap Fee, SkyLink, Demand Side Stablecoin Primitives, Omni Documents. No parameter changes. (~27 docs updated.)

---

## PR #156 — January 12 edit
**Merged:** 2026-01-19 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- Freezer Multisig (`A.6.1.1.3.2.6.1.2.1.2.3.4`): threshold 2/4 → **2/5**; signers now 2× Amatsu + 2× Endgame Edge + 1× Keel (previously "will be specified in future iteration"); "on the Solana" → "on Solana" minor fix; usage-standards text simplified.

---

## PR #150 — 2026 01 05 edit branch
**Merged:** 2026-01-09 | **Type:** Active Data update (Designated Controller)

### Material Changes
- **Solana ALM Controller USDC TokenAccount** (new `A.6.1.1.3.2.6.1.2.1.1.1.2.2.5`): `4UA2CC9fQDTbX1SnJcanYn2QU5PtyB1MGfezDvGFPVwd`
- Subsection renumbering: Freezer Multisig `.2.5` → `.2.6`; Relayer Multisig `.2.6` → `.2.7`

---

## PR #141 — Dec 8 edit
**Merged:** 2025-12-11 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- 9 Interim Deployment subtrees removed across Kamino instances (`.3.1.1.1.2.5.1`, `.1.2.2.5.1`, `.1.3.2.5.1`, `.1.4.2.5.1`, `.1.5.2.5.1`) and Solend instances (`.3.1.2.1.2.5.1`, `.2.2.2.5.1`, `.2.3.2.5.1`, `.2.4.2.5.1`) — 27 sections, 108 lines removed. All Keel Interim Deployments graduated; CRR 100% test parameters no longer apply.

---

## PR #133 — 2025-12-01 AEW Proposal
**Merged:** 2025-12-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Keel Ethereum Freezer Multisig signing requirement**: 2/4 → **2/5**
- **Freezer Multisig signers specified** for the first time: two addresses controlled by Operational GovOps Amatsu, two addresses controlled by Operational Facilitator Endgame Edge, one address controlled by Keel
- **Freezer Multisig usage standards simplified**: removed Amatsu consultation requirement (previously signers "should consult with Operational GovOps Amatsu before exercising authority unless delay would cause loss"). Now states signers may freeze Keel Liquidity Layer for risk-capital/ALM non-compliance or other emergency, with the consultation clause removed from the on-chain record.

### Context
Raising the Freezer threshold from 2/4 to 2/5 while specifying actual signer identities (Amatsu, Endgame Edge, Keel) formalizes Keel's emergency governance structure. The 2/5 threshold with five named signer groups mirrors other Freezer Multisig configurations used across agents in this era.

---

## PR #115 — Atlas Edit Weekly Proposal 2025-11-17
**Merged:** 2025-11-20 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Keel Artifact restructured**: "Allocation System Primitive" references renamed to "Keel Liquidity Layer" throughout; Active/Completed/In-Progress Instances directories reformatted with `<code>` tags
- **Keel Liquidity Layer Architecture section added**: full contract address registry for Ethereum Mainnet — Allocator Buffer (`0x065E…640c`), Allocator Oracle (`0xc7B9…bB7`), Allocator Registry (`0xCdCF…3B`), Allocator Roles (`0x9A86…803`), Allocator Vault/Nova (`0xe447…e77`); ALM Controller v1.7.0 (`0xEF26…3`)
- **Solana Instance directories added** (new protocol coverage):
  - Kamino on Solana: USDS, USDC, USDT, USDG, PYUSD instances (ICDs referenced)
  - Drift on Solana: USDS, USDC, USDT, PYUSD instances — Drift flagged as Interim Deployment (max $25M); deposit limit for Drift PYUSD: `maxAmount` 25M, `slope` 10M/day; withdrawals: unlimited

### Context
PR 115 substantially expands the Keel Artifact from a skeletal framework into a fully populated Liquidity Layer document, adding all Solana instance directories and on-chain contract addresses.

---

## PR #96 — October 27 edit
**Merged:** 2025-10-31 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Keel Liquidity Bootstrapping Budget transfer**: 500,000 USDS transferred from Sky Ecosystem Liquidity Bootstrapping Budget to Keel (corrected from "Launch Agent 2") for Solana DeFi liquidity; treated as advance against Genesis Capital Allocation; Solana multisig: `6cTVPDJ8…vmn`
- **Near Term Exemption For Keel** (A.3.4): Keel exempt from Minimum Actively Stabilizing Collateral requirement due to Solana infrastructure limitations

### Context
The reference correction from "Launch Agent 2" to "Keel" appears to formalize Keel's identity in the liquidity bootstrapping record.

---

## PR #66 — 2025-10-06 Weekly Edit Proposal
**Merged:** 2025-10-09 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Launch Agent 2 renamed to Keel** throughout the Atlas: agent Artifact header (A.6.1.1.3), full Primitives scaffold, Ecosystem Accord 3 parties and all sub-provisions (Liquidity Bootstrapping transfer, Pre-Pioneer Incentive Pool, Use of Idle Funds, development expenses clause), Pioneer Primes list, and forum references. Keel's operating company introduced as **Matariki Labs**.

### Context
Public-name reveal for Launch Agent 2 — parallels the Grove (LA1) rename in PR #22. Atlas was still in HTML format at this point (HTML→MD migration came later in PR #117). Rename-only backfill — the rest of this PR's content has not been processed in detail.

---
