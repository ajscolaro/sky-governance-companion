# Protocol Scope — Change History

Atlas path: `A.4` — The Protocol Scope

---

## PR #270 — Atlas Edit Proposal — 2026-06-29
**Merged:** 2026-07-03 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: GROVE Token Rewards** (`A.4.3.2.3`, UUID `b2ede2ee…f0d5`): GROVE token rewards are available to USDS users as specified in `A.2.8.2.2.2.1.2.2.1`.

### Context
Adds GROVE token rewards for USDS users at the protocol level, paired with the Grove distribution schedule finalized in A.2 (`A.2.8.2.2.2.1.2.2.1`) the same week; the July 2 executive "Initialize GROVE Token Rewards" activates it onchain.

---

## PR #258 — Atlas Edit Proposal — 2026-06-15
**Merged:** 2026-06-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: Cap Parameter** (`A.4.4.1.3.9.2`, UUID `532ed9cb…a3d5`): The subdocuments herein further describe the `cap` parameter and the process for its modification.
  - **Definition** (`A.4.4.1.3.9.2.1`): The `cap` parameter represents one of the potential inputs for the SKY-Backed Borrowing Capped OSM Wrapper.
- **Chronicle Scribe Oracle** (`A.4.4.1.3.9.1.1`): address `0xc2ffbbDCCF1466Eb8968a846179191cb881eCdff`
- **SKY Price Oracle** (`A.4.4.1.3.9.1`): address `0x511485bBd96e7e3a056a8D1b84C5071071C52D6F`

### Housekeeping
- `A.4.4.1.3.9` (SKY-Backed Borrowing Capped OSM Wrapper): added refs to `A.4.4.1.3.9.2`, `A.4.4.1.3.9.1`
- `A.4.4.1.3.9.2.2` renumbered (UUID stable: `0d86a609…be83`)
- `A.4.4.1.3.9.2.3` renumbered (UUID stable: `161ee404…0f6f`)

### Context
Documents the SKY-Backed Borrowing Capped OSM Wrapper's `cap` parameter and its modification process, and records its two oracle addresses (SKY Price Oracle and Chronicle Scribe). Ratified by poll #1637 (10-0).

---

## PR #253 — Atlas Edit Proposal — 2026-06-01
**Merged:** 2026-06-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **stUSDS Distribution Reward** (`A.4.4.1.3.7`): `8` → `9`; `05` → `1`; `1%` → `2`

### Housekeeping
- `8` → `9` across 1 doc.

---

## PR #242 — Atlas Edit Proposal — 2026-05-11
**Merged:** 2026-05-15 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Operator Execution** (`A.4.4.1.3.8.5.2.2`): `11` → `12`
- **Vesting Stream Parameter Modification** (`A.4.4.1.4.2.1.3.3`): `2` → `4`; `4` → `1`

### Housekeeping
- `A.4.4.1.4.2` (Short Term SKY Rewards For SKY Stakers): added refs to `A.2.3.1.4.1`, `A.2.3.1.2.4`
- `11` → `12` across 1 doc.

### Context
Cross-link added in A.4.4.1.4.2 points to the Short Term SKY Staking Rewards rate restored in the same PR (A.2.3.1.4.1). Otherwise, numbering ripples only.

---

## PR #227 — Atlas Edit Proposal — 2026-04-27
**Merged:** 2026-04-30 | **Type:** Weekly edit (Atlas Axis — Poll #1630)

### Housekeeping
- "SKY Staking Voting Rewards" → "SKY Staking Rewards" across `A.4.4.1.2` and subdocs; "voting rewards" → "rewards" in section descriptions and staking mechanism intro text
- Activity-tier staking framework deleted: HASR/SASR tier definitions, activity-level qualification criteria, and per-tier payout documents removed from `A.4.4.1.2.1.1.1`–`.3`
- Staking rewards distribution updated to continuous (previously monthly), with parameters updated at each Monthly Settlement Cycle
- Cross-references throughout updated from old transitionary `A.2.3.1.4.2` → new TMF Step 3 (`A.2.3.1.2.4`) and Step 4 (`A.2.3.1.2.5`)

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

## PR #189 — Feb 26 Exec Update
**Merged:** 2026-03-05 | **Type:** Spell recording (2026-02-26)

### Material Changes
- **SKY Staking Vesting Total** (`A.4.4.1.4.2.1.3.2.2`): `vestTot` updated from 1,000,000,000 SKY → **838,182,330 SKY**.

### Context
Records the Feb 26 executive spell: adds ALLOCATOR-PRYSM-A (Launch Agent 6) and ALLOCATOR-INTERVAL-A (Launch Agent 7) vault risk parameters and SP-BEAM configuration, and reduces the SKY staking vesting total to reflect tokens already distributed or burned.

---

## PR #186 — 2026-02-16 AEW proposal
**Merged:** 2026-02-22 | **Type:** Weekly edit (Atlas Axis — Poll 1618) | **+2119/-158 lines**

### Housekeeping

- **stUSDS BEAM section renumbering** (`A.4.4.1.3.8.3` → distributed across `A.4.4.1.3.8.4`, `.5`, `.6`): the pre-existing "Operators" subtree (Operator Multisig, Hot Wallet, Update Process) was hoisted out of `A.4.4.1.3.8.3.1` and given top-level siblings — "Operators" at `A.4.4.1.3.8.4`, "Update Process" at `A.4.4.1.3.8.5`, "Update Methodology" at `A.4.4.1.3.8.6`. All UUIDs preserved; all parameter values (Operator Multisig `0xBB86…EA16`, 2/3 threshold, Hot Wallet `0xd06C…8896`, initial `str`/`duty`/`cap`/`line` of 200M USDS, 90% target utilization, 2.4% update threshold) unchanged. Internal cross-references updated to the new paths.

### Context

Pure structural reorganization of the stUSDS BEAM documentation — the three sibling sections (Operators / Update Process / Update Methodology) are no longer nested under a single parent, which makes the hierarchy flatter and easier to cross-reference. No functional or parameter changes; the stUSDS BEAM's operator set, thresholds, and calculation methodology all remain identical.

---

## PR #180 — Feb 9 edit
**Merged:** 2026-02-12 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **stUSDS BEAM operator authority** (`A.4.4.1.3.8.3`, `.3.1.1`, `.3.1.1.3`, `.3.1.1.5`, `.3.1.2`, `.3.1.3`): "Core Executor Agents / Core Executor Agent Atlas Axis" → "Core GovOps" throughout stUSDS BEAM parameter and operator sections.

---

## PR #156 — January 12 edit
**Merged:** 2026-01-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Deprecated Emissions Mechanisms** (`A.4.1.2.2.4`): Tense shifted to past ("being deprecated" → "has been deprecated"); all related subdocs updated to reflect completed state.
- **SKY Token Rewards Emissions** (`A.4.1.2.2.4.1`): "are able to earn" → "may be able to earn"; emissions elimination described as completed action.
- **MKR to SKY Conversion Emissions** (`A.4.1.2.2.4.2`): Legacy conversion contract described as having been disabled; burn action described as completed.
- **Disabling Legacy Conversion Contract** (`A.4.1.2.2.4.2.1`): "will be executed" → "was executed in the June 26, 2025 Executive Vote."
- **Savings Rate and Token Reward Mechanism** (`A.4.3`): "benefitting" → "benefiting"; framing updated to reflect USDS users "potentially earn" rather than guaranteed.
- **Token Reward Mechanism** (`A.4.3.2`): Minor wording update.

---

## PR #142 — Dec 11 Exec Changes
**Merged:** 2026-01-04 | **Type:** Spell recording (2025-12-11)

### Material Changes
- **stUSDS `str` parameters** (`A.4.4.1.3.8.2.1`): `step` **500 → 1,500 basis points**
- **stUSDS `duty` parameters** (`A.4.4.1.3.8.2.2`): `step` **500 → 1,500 basis points**

### Context
Triple the step size for both stUSDS rate parameters, allowing larger single-adjustment moves. Recorded from the December 11, 2025 executive spell.

---

## PR #141 — Dec 8 edit
**Merged:** 2025-12-11 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **stUSDS BEAM parameter update process** (`A.4.4.1.3.8.3.2.2.1`–`.2.3`) overhauled:
  - CCRA now maintains a public stUSDS Dashboard at `https://stusds.herddefi.com/` with recommended values; operators execute against that dashboard on a regular (not forum-triggered) basis
  - Old "Request By CCRA" → "Instructions By CCRA"; old "Public Communication" → "Review By Core Facilitator And CCRA"
  - Operator execution now considers materiality, weekends/holidays, and other factors in consultation with CCRA

---

## PR #115 — Atlas Edit Weekly Proposal 2025-11-17
**Merged:** 2025-11-20 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- `A.4.4` stUSDS section renamed: "stUSDS Accessibility Reward" → "stUSDS Distribution Reward"; stUSDS Distribution Reward definition updated to reference "USDS Distribution Reward" instead of "USDS Accessibility Reward"

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

## PR #96 — October 27 edit
**Merged:** 2025-10-31 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Short-term SKY Staking Rewards** (A.4.4) significantly restructured:
  - Old section ("Short Term Staking SKY Rewards + SKY-Backed Borrowing + MKR Staking/Borrowing") replaced
  - New **Short Term USDS Rewards For SKY Stakers**: funded by Smart Burn Engine under SBE parameters; discontinued when TMF fully operational
  - New **Short Term SKY Rewards For SKY Stakers**: funded by SKY from Protocol Treasury via Staking Rewards contract (`0xB44C…0Fc`) + Rewards Distribution contract (`0x675671…Ee`) + Vesting Stream; staking token LSSKY, rewards token SKY; owner = MCD_PAUSE_PROXY
  - Old MKR staking/borrowing parameters section removed (both Short-Term MKR Staking Rewards and Short-Term MKR-Backed Borrowing)
- **Genesis Capital** (A.3.9): Spark contribution recorded — 25,000,000 USDS
- **SKY Staking description**: "In lieu of USDS rewards" → "In lieu of USDS rewards and SKY rewards, SKY stakers can earn Agent Token Rewards"

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
