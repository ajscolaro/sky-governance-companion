# Obex — Change History

Atlas path: `A.6.1.1.5` (509 docs)

---

## PR #277 — Atlas Edit Proposal — 2026-07-13
**Merged:** 2026-07-16 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- `A.6.1.1.5.2.6.2.1.2` (Active Instances Directory): removed `Junior`
- `A.6.1.1.5.2.6.2.1.3` (Completed Instances Directory): removed `Junior`
- `A.6.1.1.5.2.6.2.1.4` (In Progress Invocations Directory): removed `Junior`
- `A.6.1.1.5.2.6.2.1.5.1.1` (Failed Invocations): removed `Junior`
- `A.6.1.1.5.2.6.2.1.5.1.2` (Suspended Instances): removed `Junior`
- `A.6.1.1.5.2.6.2.1.5.1` (Archived Invocations/Instances): removed `Junior`
- `A.6.1.1.5.2.6.2.1` (Primitive Hub Document): removed `Junior`
- `A.6.1.1.5.2.6.2.2` (Active Instances): removed `Junior`
- `A.6.1.1.5.2.6.2.3` (Completed Instances): removed `Junior`
- `A.6.1.1.5.2.6.2.4` (In Progress Invocations): removed `Junior`
- `A.6.1.1.5.2.6.2` (Risk Capital Rental Primitive): removed `Junior`

### Context
"Junior" dropped from the agent's Risk Capital Rental Primitive artifacts as part of the ecosystem-wide risk-capital terminology cleanup.

---

## PR #273 — Atlas Edit Proposal — 2026-07-06
**Merged:** 2026-07-10 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- `A.6.1.1.5.2.6.1.2.1.1.3.1.3.1.1` (Maximum USDC Bridged To Ethereum Mainnet Via Circle CCTP): `ALM Proxy` → `Bridged To Ethereum Mainnet Via`
- `Cross-Chain Transfer Protocol Maximum` → `CCTP` across 1 doc.

### Context
Cross-chain document-name standardization for Obex — direction-explicit CCTP bridge label; no parameter change. Part of the 2026-07-06 weekly cycle (PR #273).

---

## PR #258 — Atlas Edit Proposal — 2026-06-15
**Merged:** 2026-06-19 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- Reference renumbering across 1 doc (linked docs moved elsewhere in this edit; UUID targets unchanged).

### Context
Reference-number propagation from documents renumbered elsewhere in this edit; UUID targets and content unchanged.

---

## PR #253 — Atlas Edit Proposal — 2026-06-01
**Merged:** 2026-06-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Agent Creation Primitive** (`A.6.1.1.5.2.1.1`): `4` → `5`
- **Prime Transformation Primitive** (`A.6.1.1.5.2.1.2`): `4` → `5`
- **Executor Transformation Primitive** (`A.6.1.1.5.2.1.3`): `4` → `5`
- **Agent Token Primitive** (`A.6.1.1.5.2.1.4`): `4` → `5`
- **Genesis Primitives** (`A.6.1.1.5.2.1`): `4` → `5`
- **Executor Accord Primitive** (`A.6.1.1.5.2.2.1`): `5` → `6`
- **Root Edit Primitive** (`A.6.1.1.5.2.2.2`): `5` → `6`
- **Light Agent Primitive** (`A.6.1.1.5.2.2.3`): `5` → `6`
- **Operational Primitives** (`A.6.1.1.5.2.2`): `5` → `6`
- **Ecosystem Upkeep Fee Primitive** (`A.6.1.1.5.2.3.1`): `6` → `7`
- **Upkeep Rebate Primitive** (`A.6.1.1.5.2.3.2`): `6` → `7`
- **Ecosystem Upkeep Primitives** (`A.6.1.1.5.2.3`): `6` → `7`
- **Token SkyLink Primitive** (`A.6.1.1.5.2.4.1`): `7` → `8`
- **SkyLink Primitives** (`A.6.1.1.5.2.4`): `7` → `8`
- **Distribution Reward Primitive** (`A.6.1.1.5.2.5.1`): `8` → `9`
- **Integration Boost Primitive** (`A.6.1.1.5.2.5.2`): `8` → `9`
- **Pioneer Chain Primitive** (`A.6.1.1.5.2.5.3`): `8` → `9`
- **Demand Side Stablecoin Primitives** (`A.6.1.1.5.2.5`): `8` → `9`
- **Treadstone's Total Risk Capital (TRC) Management Processes** (`A.6.1.1.5.2.6.1.2.1.3.2`): `9` → `10`
- **Junior Risk Capital Rental Primitive** (`A.6.1.1.5.2.6.2`): `9` → `10`
- **Asset Liability Management Rental Primitive** (`A.6.1.1.5.2.6.3`): `9` → `10`
- **Supply Side Stablecoin Primitives** (`A.6.1.1.5.2.6`): `9` → `10`
- **Core Governance Reward Primitive** (`A.6.1.1.5.2.7.1`): `10` → `11`
- **Core Governance Primitives** (`A.6.1.1.5.2.7`): `10` → `11`

### Housekeeping
- `5` → `6` across 4 docs.
- `9` → `10` across 4 docs.
- `10` → `11` across 2 docs.
- `8` → `9` across 4 docs.
- `4` → `5` across 5 docs.
- `7` → `8` across 2 docs.
- `6` → `7` across 3 docs.

### Context
All changes are version-reference bumps propagated from the Support Scope (A.2) primitive-tree reorganization and the Capital Ratio Requirement rename — no Obex-specific operational change.

---

## PR #238 — Add Obex StarGuard Contract sections
**Merged:** 2026-05-20 | **Type:** Housekeeping

### Material Changes
- **New: StarGuard Max Delay** (`A.6.1.1.5.2.1.1.3.1.1.3.1`, UUID `b037c4fd…1f60`): The Obex StarGuard `maxDelay` is seven (7) days.
- **New: Custom Instance Parameters** (`A.6.1.1.5.2.1.1.3.1.1.5`, UUID `6b501d73…29da`): The documents herein define the custom parameters of the Single Instance of the Agent Creation Primitive, if any.
- **StarGuard Contract** (`A.6.1.1.5.2.1.1.3.1.1.3`): address `0x987f1C31f9935e9926555BcFB76516bb2EcEccaD`

### Housekeeping
- `A.6.1.1.5.2.1.1.3.1.1.4` (Genesis Account): `Custom Instance Parameters` → `Genesis Account`
- `A.6.1.1.5.2.1.1.3.1.1.5.1` renumbered (UUID stable: `57b0ac97…3806`)
- `A.6.1.1.5.2.1.1.3.1.1.5.2` renumbered (UUID stable: `44a4e626…0773`)

### Context
Documents Obex's deployed StarGuard security contract (`0x987f…ccaD`) and its 7-day `maxDelay`, populating the Agent Creation Primitive's previously-empty parameters section. No ratification poll or spell — merged same-day as a documentation edit to record the on-chain binding.

---

## PR #242 — Atlas Edit Proposal — 2026-05-11
**Merged:** 2026-05-15 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Root Edit Voting Process in Emergency Situations** (`A.6.1.1.5.2.2.2.2.1.2.3.1`): `8` → `9`
- **Required Number Of Signers** (`A.6.1.1.5.2.6.1.2.1.2.2.3.2`): `4` → `5`
- **Signers** (`A.6.1.1.5.2.6.1.2.1.2.2.3.3`): `4` → `3`

### Housekeeping
- `A.6.1.1.5.2.6.1.2.1.2.2.3.4` (Usage Standards): removed `The usage standards for the Freezer Multisig will be specified in a future iteration of the Obex Artifact.`
- `A.6.1.1.5.2.6.1.2.1.2.2.3.5` (Modification): `` → `Any changes to the Multisig signers that do not fall within the two exceptions listed above, or that have not been ratified by Sky Governance, should be questioned immediately and treated as malicious. Where malicious activity is suspected, the Core Facilitator must prepare an expedited Executive Vote so that Sky Governance can vote on removing external security access from the Multisig.`
- `A.6.1.1.5.2.6.1.2.1.2.2.3` (Freezer Multisig): removed `and is controlled by Obex`
- `8` → `9` across 1 doc.
- `4` → `5` across 1 doc.

### Context
Raises the Freezer Multisig signing threshold from 2/4 to 2/5, broadening control from Obex alone to include the Operational Executor Agent. Concurrently adds explicit modification-protection language directing the Core Facilitator to treat unsanctioned signer changes as malicious and trigger an expedited Executive Vote.

---

## PR #237 — Atlas Edit Proposal — 2026-05-04
**Merged:** 2026-05-08 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- Solidity identifier whitespace fix across Obex ALM Controller and Rate Limit Management docs (`A.6.1.1.5.2.6.1.2.2.1.{1.3, 2.1.2.1.1.1, 2.1.2.2.1.1, 3, 3.1–3.5}`): same `Rate Limits` → `RateLimits`, `setRate LimitData` → `setRateLimitData`, `getCurrentRate Limit` → `getCurrentRateLimit`, etc. as the parallel Keel/Pattern fixes.

### Context
Same compile-correctness sweep applied to Keel and Pattern in this PR. Ratified by Poll #1631 (10-0).

---

## PR #224 — Atlas Edit Proposal — 2026-04-20
**Merged:** 2026-04-24 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- Distribution Requirement Primitive (`A.6.1.1.5.2.3.1`) renamed to "Ecosystem Upkeep Fee Primitive"; Market Cap Fee Primitive subtree (`A.6.1.1.5.2.3.2`) deleted; Upkeep Rebate references updated.

---

## PR #200 — 2026-03-16 Weekly Edit Proposal
**Merged:** 2026-03-20 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core Operator Relayer Multisig** (`A.6.1.1.5.2.6.1.2.1.2.2.2`): operational GovOps reference updated (Ozone listed as GovOps provider).

---

## PR #187 — 2026-02-23 Atlas Edit Weekly Cycle Proposal
**Merged:** 2026-03-05 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- 1 section: minor link-text fix in Obex. No substantive change.

---

## PR #186 — 2026-02-16 AEW proposal
**Merged:** 2026-02-22 | **Type:** Weekly edit (Atlas Axis — Poll 1618) | **+2119/-158 lines**

### Material Changes

- **Treadstone introduced as Obex's development company** (`A.6.1.1.5.2.1.1.3.1.1.4.2`, new): "Treadstone is the development company that provides services to Rubicon."
- **Rubicon role formalized** (`A.6.1.1.5.2.1.1.3.1.1.4.1`, new Core document — previously only referenced): "Rubicon is the Prime Foundation associated with Obex. Its mandate is to support the development, growth, and adoption of Obex."
- **Obex 'party' composition updated** (`A.2.8.2.4.1.1.2`, under Support Scope): the party 'Obex' now comprises Obex Prime Agent, **Rubicon**, and **Treadstone** — was previously Obex Prime Agent, Obex Foundation, and Rubicon. Obex Foundation removed; Treadstone added
- **Operational responsibility for Obex Liquidity Layer transferred from Rubicon to Treadstone:**
  - `A.6.1.1.5.2.6.1.2.1.3.1` — **"Treadstone will operate the Obex Liquidity Layer and agrees to stay at or below a 90% Encumbrance Ratio"** (was Rubicon)
  - `A.6.1.1.5.2.6.1.2.1.3.2` — **Treadstone** inherits the base TRC management operational requirements (was Rubicon)

### Context

Structural clarification of Obex's operational architecture: Rubicon remains the Prime Foundation (governance/support role), while a new entity **Treadstone** is formally designated as the development company operating the Obex Liquidity Layer day-to-day. The 90% Encumbrance Ratio ceiling is preserved but the accountable operator changes. The A.2 "party Obex" composition swap (removing Obex Foundation, adding Treadstone) aligns the Accord-level party definition with the new operational model — though note that this suggests "Obex Foundation" as a distinct entity is being retired, with Rubicon stepping into the Foundation role. No rate-limit or capital-allocation parameters changed. SKY ~$0.065, USDS supply ~$9.9B at merge.

---

## PR #121 — Nov 24 Atlas edit
**Merged:** 2025-11-30 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Launch Agent 4 renamed to Obex** throughout the Atlas: agent Artifact header (A.6.1.1.5), full Primitives scaffold, Ecosystem Accord 4 title and parties (party "Obex" defined as Obex Prime Agent, Obex Foundation, and Rubicon), Initial Allocation (21,000,000 USDS to Obex SubProxy), Genesis Capital Allocation transfer provisions, Pioneer Primes list, and all LA4 cross-references.

### Context
Public-name reveal for Launch Agent 4. At this stage Obex's party composition is Obex Prime Agent + Obex Foundation + Rubicon; the later PR #186 restructure drops Obex Foundation and adds Treadstone as the operating dev company. Rename-only backfill — the rest of this PR's content has not been processed in detail.

---
