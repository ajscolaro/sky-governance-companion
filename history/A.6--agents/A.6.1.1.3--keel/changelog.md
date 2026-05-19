# Keel — Change History

Atlas path: `A.6.1.1.3` (874 docs)

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

## PR #133 — 2025-12-01 AEW Proposal
**Merged:** 2025-12-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Keel Ethereum Freezer Multisig signing requirement**: 2/4 → **2/5**
- **Freezer Multisig signers specified** for the first time: two addresses controlled by Operational GovOps Amatsu, two addresses controlled by Operational Facilitator Endgame Edge, one address controlled by Keel
- **Freezer Multisig usage standards simplified**: removed Amatsu consultation requirement (previously signers "should consult with Operational GovOps Amatsu before exercising authority unless delay would cause loss"). Now states signers may freeze Keel Liquidity Layer for risk-capital/ALM non-compliance or other emergency, with the consultation clause removed from the on-chain record.

### Context
Raising the Freezer threshold from 2/4 to 2/5 while specifying actual signer identities (Amatsu, Endgame Edge, Keel) formalizes Keel's emergency governance structure. The 2/5 threshold with five named signer groups mirrors other Freezer Multisig configurations used across agents in this era.

---

## PR #66 — 2025-10-06 Weekly Edit Proposal
**Merged:** 2025-10-09 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Launch Agent 2 renamed to Keel** throughout the Atlas: agent Artifact header (A.6.1.1.3), full Primitives scaffold, Ecosystem Accord 3 parties and all sub-provisions (Liquidity Bootstrapping transfer, Pre-Pioneer Incentive Pool, Use of Idle Funds, development expenses clause), Pioneer Primes list, and forum references. Keel's operating company introduced as **Matariki Labs**.

### Context
Public-name reveal for Launch Agent 2 — parallels the Grove (LA1) rename in PR #22. Atlas was still in HTML format at this point (HTML→MD migration came later in PR #117). Rename-only backfill — the rest of this PR's content has not been processed in detail.

---
