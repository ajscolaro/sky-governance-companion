# Obex — Change History

Atlas path: `A.6.1.1.5` (509 docs)

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
