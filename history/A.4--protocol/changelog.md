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

## PR #186 — 2026-02-16 AEW proposal
**Merged:** 2026-02-22 | **Type:** Weekly edit (Atlas Axis — Poll 1618) | **+2119/-158 lines**

### Housekeeping

- **stUSDS BEAM section renumbering** (`A.4.4.1.3.8.3` → distributed across `A.4.4.1.3.8.4`, `.5`, `.6`): the pre-existing "Operators" subtree (Operator Multisig, Hot Wallet, Update Process) was hoisted out of `A.4.4.1.3.8.3.1` and given top-level siblings — "Operators" at `A.4.4.1.3.8.4`, "Update Process" at `A.4.4.1.3.8.5`, "Update Methodology" at `A.4.4.1.3.8.6`. All UUIDs preserved; all parameter values (Operator Multisig `0xBB86…EA16`, 2/3 threshold, Hot Wallet `0xd06C…8896`, initial `str`/`duty`/`cap`/`line` of 200M USDS, 90% target utilization, 2.4% update threshold) unchanged. Internal cross-references updated to the new paths.

### Context

Pure structural reorganization of the stUSDS BEAM documentation — the three sibling sections (Operators / Update Process / Update Methodology) are no longer nested under a single parent, which makes the hierarchy flatter and easier to cross-reference. No functional or parameter changes; the stUSDS BEAM's operator set, thresholds, and calculation methodology all remain identical.

---

## PR #110 — Nov 10 edit
**Merged:** 2025-11-13 | **Type:** Weekly edit (Atlas Axis)

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
**Merged:** 2025-10-09 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **SKY Backstop definition expanded** (A.4.3): added "SKY Backstop Event" — the period when the recapitalization mechanism is actively minting and selling SKY

### Context
Formalizes the "SKY Backstop Event" concept referenced in multiple risk documents.

---

## PR #59 — Atlas Edit Weekly Cycle Proposal 2025 09 15
**Merged:** 2025-09-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New Article A.4.6 — Protocol Mechanisms** added: defines maintenance/housekeeping mechanisms and contracts for administering the Sky Ecosystem

### Context
Structural addition creating a home for protocol-level administrative mechanisms.

---

## PR #54 — Atlas Edit Weekly Cycle Proposal - Week of 2025-09-01
**Merged:** 2025-09-05 | **Type:** Weekly edit (Atlas Axis — Poll 1562)

### Material Changes
- **stUSDS BEAM Automatic Updates by Operator Hot Wallet** (A.4.4, new): once the Operator Hot Wallet is added as Operator of the stUSDS BEAM, all parameter updates must be made by that Hot Wallet (not the Operator Multisig). Specifies the automation path for eventual fully-automated rate setting.
- **`lastAmount` defined** (A.2.4): remaining allowance at last rate-limit update; used in rate limit formula to calculate current available capacity.

### Housekeeping
- `cap`/`line` wrapped in `<code>` tags in STUSDS_MOM contract description.
- `<dfn>` cross-reference punctuation normalized across A.4.4 (trailing periods removed).
- `stUSDS BEAMparameters` → `stUSDS BEAM parameters` (space fix).
- Quote formatting in Outflow Rate Limits definition normalized.

---

## PR #17 — Cleanup multiple scopes and artifacts
**Merged:** 2025-06-20 | **Type:** Housekeeping

Multi-scope formatting cleanup across Stability, Protocol, Preamble, Support, and Spark Artifact. Inline multi-line text collapsed to single lines; `<code>` tags added to parameter names (e.g., `max`, `min`, `step`, `tau`); paragraph tags added for readability. No parameter values changed.

---

## PR #10 — Weekly Cycle Atlas Edit proposal 2025-06-09
**Merged:** 2025-06-12 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Disabling Legacy Conversion Contract** (A.4.1, new): New document specifying the Legacy MKR-to-SKY conversion contract will be disabled in the June 26, 2025 Executive Vote; authorized to proceed directly to an Executive Vote without a prior Governance Poll.
- **MKR To SKY Conversion Emissions** (A.4.1): Text updated to reference the new Disabling Legacy Conversion Contract document.

### Context
See Spark changelog for the bulk of PR #10 changes (Spark Foundation docs, SPK token transfer records, Root Edit governance updates).

---

## PR #1 — 2025-05-26 Atlas Edit Weekly Cycle Proposal
**Merged:** 2025-06-07 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- Distribution Of Agent Tokens article text updated: prior multi-stakeholder distribution formula replaced by "distributed per terms of the Ecosystem Accord."
- "First Loss Capital" → "Risk Capital" terminology in agent token primitive and allocation system documents (A.4 references).

---

## PR #5 — 2025-06-02 changes
**Merged:** 2025-06-05 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **SKY Deflationary Tokenomics framework added** (A.4.1, new — ~7 documents):
  - **Initial Token Supply**: SKY supply derived from legacy MKR × 24,000 conversion ratio; SKY is the exclusive governance and economic rights token
  - **No New Token Emissions**: prohibits new SKY issuance except for insolvency recapitalization or deprecated emissions being wound down
  - **Burning of Existing Tokens**: SKY bought back and burned via Smart Burn Engine (Treasury Management Step 4)
  - **Deprecated Emissions Mechanisms** (parent): SKY Token Rewards Emissions and MKR-to-SKY Conversion Emissions — both being phased out with equivalent burns to ensure net zero supply impact
  - **SKY Token Rewards Emissions**: current rewards funded by new emissions; will be replaced with SKY held by the protocol + equivalent burn
  - **MKR To SKY Conversion Emissions**: Legacy Conversion Contract burns MKR / mints SKY; New Conversion Contract uses preminted supply instead

### Context
This edit formalizes the deflationary tokenomics intent that was implicit in the Smart Burn Engine mechanics. The "Deprecated Emissions Mechanisms" structure creates a formal deprecation pathway — emissions continue temporarily but must be offset by burns to maintain net supply neutrality.

---

## PR #4 — add 2025-05-29 spell changes
**Merged:** 2025-06-04 | **Type:** Spell recording (2025-05-29)

### Material Changes
- **GSM Pause Delay**: 48 hours → **24 hours** (governance security parameter)

### Context
See A.3--stability changelog for full spell parameter changes (Splitter, Morpho vault exposure). The GSM Pause Delay halving is the most consequential Protocol Scope change — it reduces the emergency brake window from 48 to 24 hours.

---
