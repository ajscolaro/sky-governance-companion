# Obex — Change History

Atlas path: `A.6.1.1.5` (509 docs)

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
