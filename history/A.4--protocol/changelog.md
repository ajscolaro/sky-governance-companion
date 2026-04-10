# Protocol Scope — Change History

Atlas path: `A.4` — The Protocol Scope

---

## PR #219 — Atlas Edit Proposal — 2026-04-06
**Merged:** 2026-04-09 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **USDS staking rewards for SKY stakers now active** (A.4.4.1.4.1): Previously: "USDS rewards for SKY stakers are not currently available." Now: "available as specified in A.2.3.1.4.2" (the new stage framework). Stages 0 and 1 allocate nothing; Stage 2 allocates 25% of Step 4 Capital.
- **SKY vesting stream parameters despecified** (A.4.4.1.4.2.1.3.2): Hardcoded values removed:
  - `vestTau` (Vesting Duration): was 180 days → now no hardcoded value (governed by stage framework)
  - `vestTot` (Vesting Total): was 838,182,330 SKY → now no hardcoded value (governed by stage framework)
  - Vesting modification authority updated: Core Facilitator now modifies parameters "to achieve the target reward rate as specified in A.2.3.1.4.2" (previously: "on recommendation of Risk Advisor, every ~90 days")
- **Smart Burn Engine parameter updates authorized** (A.3.5.2): Stage-transition parameter updates may proceed directly to Executive Vote without a prior Governance Poll.

### Context
These are the Protocol Scope mirror of the Support Scope changes in A.2.3.1.4.2. The vesting parameter despecification is notable: the 838M SKY/180-day hardcoded values were the operational machinery for Stage 0 SKY staking rewards. Removing them from the Atlas means the actual figures will be set and updated via Executive Votes each settlement cycle, rather than being governed-by-default. This gives more flexibility to adapt as Step 4 Capital fluctuates but removes the Atlas as a source of ground truth for the current distribution rate.

---

## PR #110 — Nov 10 edit
**Merged:** 2025-11-13 | **Type:** Weekly edit

### Material Changes
- **Gnosis Payment authorized** (A.4.1, new): 1,806,670 USDS to compensate Gnosis for SSR/DSR difference on xDai (March 1 - October 28, 2025). Authorized for next Executive Vote without Governance Poll.
- **USDS Launch tense updated** (A.4.1): "USDS is launched" → "USDS was launched"

### Context
The Gnosis payment resolves a legacy obligation from the DAI-to-USDS transition, compensating for the rate differential during the migration period.

---

## PR #107 — OOS Atlas Edit
**Merged:** 2025-11-10 | **Type:** Weekly edit (out-of-schedule)

### Material Changes
- **Capital Contributed to Agents updated** (A.4.5): Launch Agent 4 added with 21,000,000 USDS allocation

### Context
Records the Launch Agent 4 Genesis Capital Allocation in the Protocol Scope capital tracking.

---

## PR #66 — 2025-10-06 Weekly Edit Proposal
**Merged:** 2025-10-09 | **Type:** Weekly edit

### Material Changes
- **SKY Backstop definition expanded** (A.4.3): added "SKY Backstop Event" — the period when the recapitalization mechanism is actively minting and selling SKY

### Context
Formalizes the "SKY Backstop Event" concept referenced in multiple risk documents.

---

## PR #59 — Atlas Edit Weekly Cycle Proposal 2025 09 15
**Merged:** 2025-09-19 | **Type:** Weekly edit

### Material Changes
- **New Article A.4.6 — Protocol Mechanisms** added: defines maintenance/housekeeping mechanisms and contracts for administering the Sky Ecosystem

### Context
Structural addition creating a home for protocol-level administrative mechanisms.

---

## PR #186 — 2026-02-16 AEW proposal
**Merged:** 2026-02-22 | **+2119/-158 lines**

### Raw Changes (rewrite with /atlas-track)
- **Modified** `A.4.4.1.3.8.6.2.2` - Calculations For Update [Core]
- **Modified** `A.4.4.1.3.8.6.1.3` - Growth Of Market Size [Core]
- **Modified** `A.4.4.1.3.8.5.1` - Initial Parameter Values Set In Executive Vote [Core]
- **Modified** `A.4.4.1.3.8.6.2.2.3.1` - Short Term Calculation [Core]
- **Modified** `A.4.4.1.3.8.4.1.5` - Operator Multisig Modification [Core]
- **Modified** `A.4.4.1.3.8.5.2.2` - Operator Execution [Core]
- **Modified** `A.4.4.1.3.8.4.1.1` - Operator Multisig Address [Core]
- **Modified** `A.4.4.1.3.8.4.3` - Operator Update Process [Core]
- **Modified** `A.4.4.1.3.8.4.1.4` - Operator Multisig Usage Standards [Core]
- **Modified** `A.4.4.1.3.8.5.2.3` - Review By Core Facilitator And Core Council Risk Advisor [Core]
- **Modified** `A.4.4.1.3.8.6.2.2.2` - Duty Calculation [Core]
- **Modified** `A.4.4.1.3.8.5` - Update Process [Core]
- **Modified** `A.4.4.1.3.8.6.1.2` - Gradual Reduction In Supply Rate [Core]
- **Modified** `A.4.4.1.3.8.4.2.2` - Update Of stUSDS Parameters For Hot Wallet [Core]
- **Modified** `A.4.4.1.3.8.4.1.2` - Operator Multisig Required Number Of Signers [Core]
- **Modified** `A.4.4.1.3.8.4` - Operators [Core]
- **Modified** `A.4.4.1.3.8.5.2` - Manual Parameter Updates By Operator Multisig [Core]
- **Modified** `A.4.4.1.3.8.5.3` - Automatic Updates By Operator Hot Wallet [Core]
- **Modified** `A.4.4.1.3.8.4.1.3` - Operator Multisig Signers [Core]
- **Modified** `A.4.4.1.3.8.6.2.2.1` - Str Calculation [Core]
- **Modified** `A.4.4.1.3.8.6.2` - Long Term Process [Core]
- **Modified** `A.4.4.1.3.8.4.2.1` - Operator Hot Wallet Address [Core]
- **Modified** `A.4.4.1.3.8.4.2` - Operator Hot Wallet [Core]
- **Modified** `A.4.4.1.3.8.6.2.2.4.1` - Short Term Calculation [Core]
- **Modified** `A.4.4.1.3.8.6.2.2.3.2` - Long Term Calculation [Core]
- **Modified** `A.4.4.1.3.8.6.1` - Short Term Process [Core]
- **Modified** `A.4.4.1.3.8.6.1.1` - Initial Supply Rate [Core]
- **Modified** `A.4.4.1.3.8.6.2.2.4.2` - Long Term Calculation [Core]
- **Modified** `A.4.4.1.3.8.6.2.1` - Conditions For Update [Core]
- **Modified** `A.4.4.1.3.8.5.2.1` - Instructions By Core Council Risk Advisor [Core]
- **Modified** `A.4.4.1.3.8.6` - Update Methodology [Core]
- **Modified** `A.4.4.1.3.8.6.2.2.4` - Line Calculation [Core]
- **Modified** `A.4.4.1.3.8.4.1` - Operator Multisig [Core]
- **Modified** `A.4.4.1.3.8.6.2.2.3` - Cap Calculation [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---
