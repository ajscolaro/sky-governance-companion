# Atlas Preamble — Change History

Atlas path: `A.0` — Definitions, foundational concepts, and structural rules

---

## PR #219 — Atlas Edit Proposal — 2026-04-06

**Merged:** 2026-04-09 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping

- "Scope Facilitators" → "Core Facilitator" (singular) across multiple Preamble documents, including A.0.1.2.1.1 (Facilitators' Broad Discretionary Capacity annotations). Aligns legacy pluralized role language with the current consolidated Core Facilitator role.
- Subject-verb agreement fixes: "have" → "has" in annotations referencing the Core Facilitator.

### Context

Pure terminology maintenance. The pluralized "Scope Facilitators" language dates to an earlier governance structure; this PR continues a multi-PR campaign (also visible in A.1 and A.2 changes) to standardize all Atlas documents to "Core Facilitator" (singular).

---

## PR #110 — Nov 10 edit

**Merged:** 2025-11-13 | **Type:** Weekly edit (Atlas Axis)

### Material Changes

- **Prime Spell Security Enforcement framework added** (A.1.9, new): Comprehensive framework for enforcing spell security standards on Prime Agents:
  - Defines "Prime Spell Security Guidelines" and "Prime Spell Security Incidents"
  - **Enforcement authority:** Core Facilitator + Core GovOps, with full discretion on penalties
  - **Penalties:** financial penalties, deprioritization in spell queue, exclusion from Executive Vote cycles, mandatory additional audits, suspension of Core Council support
  - **Incident Registry:** Active Data maintained by Core Facilitator (direct edit protocol); currently empty
  - **Incident reporting:** Prime + Operational Executor must produce report promptly; delay/inaccuracy is a separate incident
  - **Registry uses:** input to Prime Agent Credit Rating System (affects Agent Credit Line Borrow Rate), risk-based insurance pricing, escalation multiplier for repeat incidents
- **Agent Credit Line Borrow Rate linkage updated** (A.3.2): now may vary by Prime Agent credit rating when variable pricing is activated per the Spell Security Registry
- **Prime Agent Credit Rating System updated** (A.3.2): now explicitly includes Spell Security Incident Registry as a factor alongside Encumbrance Ratio
- **Actively Stabilizing Collateral Incentive introduced** (A.3.4, new): Near-term incentive for Primes fulfilling ASC requirements:
  - Formula: `Eligible ASC * (Base Rate - Treasury Bill Rate)` per block
  - Eligible ASC = lesser of actual ASC and Minimum ASC
  - Treasury Bill Rate: 91-day US T-bill yield (published by US Treasury)
  - Paid monthly via Monthly Settlement Cycle
- **Resting ASC calculation updated** (A.3.4): added "Cash Stablecoins in Uniswap (paired with USDS)" to Resting ASC list
- **Latent ASC calculation updated** (A.3.4): "Cash Stablecoins in Uniswap" → "Cash Stablecoins in Uniswap (not paired with USDS)" — clarifying that Uniswap USDS-paired positions count as Resting, not Latent
- **Sky Direct Exposures list expanded** (A.2.4 Active Data): added two new categories:
  - "Peg Stability Modules — Investments by Spark or Grove in USDC in PSMs on blockchains other than Ethereum Mainnet"
  - "Curve Pools — Investments by Spark in USDT in sUSDS/USDT Curve pools"
  - Existing entries reworded: "Investments in BUIDL..." → "Investments by Grove in BUIDL..."
- **Gnosis Payment authorized** (A.4.1, new): 1,806,670 USDS to compensate Gnosis for SSR/DSR difference on xDai (March 1 - October 28, 2025). Recipient: `0x849d52316331967b6ff1198e5e32a0eb168d039d`. Authorized for next Executive Vote without Governance Poll.
- **A.2.4 No Actively Stabilizing Collateral requirements for Sky Direct Exposures** (new): Primes not required to hold ASC for Direct Sky Exposures; they also don't count toward ASC requirements
- **USDS Launch tense updated** (A.4.1): "USDS is launched" → "USDS was launched" — acknowledging launch is historical
- **Grove Interim Deployment documents removed:** Removed "Interim Deployment", "Maximum Allocation", and "Rate Limits" interim testing documents from 5 Grove instances (Curve RLUSD/USDC, Morpho Grove x Steakhouse USDC, Securitize STAC, Morpho Grove x Steakhouse USDC [second], Aave v3 USDT0) — deployments graduated from interim to normal operation

### Housekeeping

- Various "Support Facilitators" → "Core GovOps" / "Core Facilitator" propagations in A.2.2, A.2.7

### Context

PR #110 adds two significant enforcement/incentive frameworks: the Prime Spell Security Enforcement system (with teeth — financial penalties, queue exclusion, registry-linked credit rating) and the Actively Stabilizing Collateral Incentive (paying Primes the spread between Base Rate and T-bill rate for maintaining liquidity buffers). The expansion of Direct Sky Exposures to include PSMs and Curve pools is notable — it exempts a growing portion of protocol liquidity from Prime-level risk capital requirements. The removal of Grove's Interim Deployment constraints on 5 instances signals those allocations have completed their testing phase. The Gnosis payment resolves a legacy obligation from the MakerDAO-to-Sky transition. SKY was ~$0.043-0.055 and USDS supply ~$9.1-9.4B.

---

## PR #107 — OOS Atlas Edit

**Merged:** 2025-11-10 | **Type:** Weekly edit (out-of-schedule)

### Material Changes

- **Ecosystem Accord 4: Sky and Launch Agent 4** added (A.2.10, new): Full Ecosystem Accord establishing the relationship between Sky and Launch Agent 4 (comprising Launch Agent 4 Prime Agent, Launch Agent 4 Foundation, and Rubicon):
  - Duration: indefinite, commencing November 13, 2025
  - Genesis Capital Allocation: **21,000,000 USDS** to Launch Agent 4 SubProxy
  - Transfer authorized in November 13, 2025 Executive Vote (no prior Governance Poll required)
  - Launch Agent 4 added to A.4.5 Capital Contributed to Agents list
  - Launch Agent 4 added to Pioneer Primes list (A.2.2)
- **Grove Base rate limits added** (Grove Artifact): Grove Liquidity Layer on Base with USDC CCTP rate limits:
  - `maxAmount`: 50,000,000 USDC; `slope`: 50,000,000 USDC per day (both directions)
- **Launch Agent 4 Ecosystem Accords section added** to Launch Agent 4 Artifact

### Context

This out-of-schedule edit onboards Launch Agent 4 (Rubicon) as a new Prime Agent in the Sky ecosystem with a 21M USDS Genesis Capital Allocation — the second-largest after Spark's 25M. The "OOS" designation reflects the urgency of including the transfer in the November 13 Executive Vote. Grove's Base chain rate limits formalize its cross-chain USDC operations. SKY was ~$0.043-0.050 and USDS supply ~$9.3B.

---

## PR #89 — 2025-10-20 Atlas Weekly Cycle Proposal

**Merged:** 2025-10-23 | **Type:** Weekly edit (Atlas Axis)

### Material Changes

- **Core Council Risk Advisor role created** (A.1.7, new): BA Labs designated as the Core Council Risk Advisor — a specialized Professional Ecosystem Actor providing financial analysis and risk management advice. Requirements: no conflicting business activities (with limited waiver for BA Labs' work with Ethena). This replaces the former "Stability Scope Advisors" role throughout the Atlas.
- **Stability Scope Improvement section (A.3.1) deleted:** The entire "Scope Improvement" article (including Scope Advisor Requirements, BA Labs CoI Waiver, Current Scope Advisors list) was removed. BA Labs' role is now governed by the new A.1.7 Core Council Risk Advisor framework instead.
- **"BA Labs" / "Stability Scope Advisors" renamed to "Core Council Risk Advisor"** across ~20+ documents in A.2.4, A.2.6, A.3.2, and A.3.3 — including Monthly Settlement Cycle calculations, Integration Boost data verification, Base Rate setting process, Distortion Penalty consultation, and risk framework approvals
- **"Instance Financial RRC Ratio" → "Instance Financial CRR" terminology change** across A.3.3: all risk capital ratio references updated to use "Capital Requirement Ratio" (CRR) language — affects Ethena, Superstate, Fluid, Pendle, and lending market documents
- **Capital Requirement Ratio (CRR) formally defined** (A.3.3, new): CRR = Required Risk Capital / capital invested. Can be specified as Aggregate CRR, Instance CRR, or type-specific (Financial, Smart Contract, Administrative)
- **Interim Deployments framework added** (A.1.9, new): Prime Agents can deploy Allocation Instances under constrained testing conditions before full risk assessment. Process: Forum post (after external audit) → Risk Advisor specifies testing parameters → Artifact Edit Proposal → Instance Configuration Document → inclusion in Executive Cycle → full risk assessment to lift constraints
- **Direct Sky Exposures framework added** (A.2.4, new): Exposures held by Sky but implemented through a Prime Agent's Allocation System. JAAA through Grove designated as first Direct Sky Exposure. No Risk Capital or Actively Stabilizing Collateral requirements for Primes on these exposures. Revenue sharing: if yield < Agent Credit Line Borrow Rate, Prime not liable; if yield >= rate, Prime keeps the difference
- **Agent Artifact Review framework added** (A.1.14, new): Core GovOps may review Agent Artifacts for compliance at any time. Process: initial findings → agent response → final findings published → remediation (agent submits Root Edit Proposal or Core GovOps proposes direct edit) → appeals to Core Facilitator. Penalties TBD.
- **Atlas Edit Proposal Process for Prime Agents defined** (A.2.4, new): Primes without operational Root Edit Primitive must submit draft to Core GovOps by Monday 23:59 UTC → Core GovOps drafts formal proposal → Atlas Edit Weekly Cycle vote
- **Superstate RRC increased** (A.3.3): Superstate Exposures (USCC) Instance Financial CRR: 3% → **4.5%**
- **Instance Setup Deployment updated** (A.2.4): renamed to "Instance Setup Deployments" (plural); now references Interim Deployments process; pro-forma RRC estimate required (approved by Risk Advisor) before normal operation
- **"Stability Facilitators" references removed** throughout — replaced by "Core Council Risk Advisor" or "Core Facilitator" as appropriate

### Housekeeping

- "Support Facilitators" → "Core GovOps" in A.2.2 governance process support
- "Core Facilitators" → "Core Facilitator" (singular) in A.2.6 settlement documents
- Various minor text cleanups in A.2.4, A.2.6 process definitions

### Context

PR #89 is the most substantively dense weekly edit in this batch. It simultaneously: (1) formalizes the Core Council Risk Advisor role (effectively elevating BA Labs from "Scope Advisor" to a named governance role), (2) introduces the CRR terminology that becomes standard for all future risk framework references, (3) creates the Interim Deployments path that later PRs use for Grove and other agents, (4) establishes Direct Sky Exposures as a new risk-capital-exempt category, and (5) adds the Agent Artifact Review framework giving Core GovOps enforcement authority. The Superstate RRC increase from 3% to 4.5% is the only parameter tightening. SKY was ~$0.055-0.059 and USDS supply ~$9.1B.

---

## PR #78 — October 13 edit

**Merged:** 2025-10-16 | **Type:** Weekly edit (Atlas Axis)

### Material Changes

- **A.1.6 Facilitators section restructured — 17 documents deleted:** Removed the entire Facilitator management framework (A.1.6 A1 and A.2 sections) including:
  - "Bound by Scope Requirements And Rules"
  - "Enforcement of Facilitator Rules" (which referenced Governance Facilitators adjudicating)
  - "Facilitator Management" section: Appointment, Role Of Governance Scope, Scopes' Responsible Facilitators, List of Responsible Facilitators (JanSky, Endgame Edge, Ecosystem)
  - "Budgets" and "List of Facilitator Budgets" (42,000 USDS + 432,000 SKY/month per facilitator)
  - "Interim And Reserve Facilitators", "Reserve Facilitator Takeover", "Expedited Onboarding"
  - "Governance Scope Responsibility", "Full Scopes Coverage"
- **Facilitators Article description simplified** (A.1.5): removed "assigned responsibility over specific Scopes for Sky Core" — Facilitators are now described only as "contracted by Executor Agents to interpret the Atlas and Artifacts"
- **A.5.9 renamed:** "Launch Project" → "Short-Term Transitionary Measures" — no longer specifically about the Launch Project bootstrapping effort
- **"Governance Facilitators" → "Core Facilitator" propagated** across remaining A.1 governance documents (A.1.4 role doc renamed, A.1.11, A.1.12 review/verification docs, Atlas Edit template, simultaneous edit reconciliation)
- **A.1.12 Monthly Cycle — "Governance Facilitators' Review" renamed** to "Core Facilitators' Review": Core Facilitator now singular authority for AEP review, blocking for misalignment, status updates

### Housekeeping

- Various remaining "Governance Facilitators" → "Core Facilitator" updates in A.2.2 governance process support, A.2.7 communication channels
- "Support Facilitators" → "Core GovOps" in governance process coordination and ecosystem actor designation
- "Support Facilitator" → "Core Facilitator" in Atlas Core Development funding
- Sky Forum moderator list: removed "Accessibility Facilitators" — now just "The Core Facilitator"
- Minor text simplification in governance process documentation

### Context

This is the most structurally significant governance edit in this batch. The deletion of the entire A.1.6 Facilitator management framework — including the named Facilitator roster (JanSky, Endgame Edge, Ecosystem) and their 42K USDS + 432K SKY monthly budgets — represents the formal transition from the multi-Scope-Facilitator model to the Core Council model. The old framework assumed multiple independent Facilitators with scope-specific responsibilities; the new model consolidates all authority under the Core Facilitator / Core Council. The A.5.9 rename from "Launch Project" to "Short-Term Transitionary Measures" signals the end of the bootstrapping phase. SKY was ~$0.059 and USDS supply ~$8-9B.

---

## PR #66 — 2025-10-06 Weekly Edit Proposal

**Merged:** 2025-10-09 | **Type:** Weekly edit (Atlas Axis)

### Material Changes

- **Full Executive Process Definition added** (A.1.9 A2): ~100+ new documents comprehensively defining the end-to-end Executive Process for the first time in the Atlas. Key elements:
  - **Definitions:** Executive Sheet, Target Date, Executive Document, Executive Vote, Voting Portal, Custom Spell Voting Page, Spell, Ecosystem Spell Validation, Spell Roster (Sidestream + Dewiz), Spell Team, Spell Crafter, Spell Reviewer
  - **Roles:** Governance Point (selected from Core Facilitators, currently JanSky), Governance Backup, Technical Point, Content Liaisons, SKY Holders, Aligned Delegates, Shadow Delegates
  - **13-step process breakdown:** from preliminary content determination through spell deployment, validation, and publishing
  - **Smart Contract Deployment Verification:** Atlas Crafting Stage, Forum Post requirements, Core Facilitator approval, module deployment procedures
  - **Recurring items:** Office Hours, Global Line Modifier, Order of Operations
  - **EVM version validation rule updated:** now accepts either "Default" or correct default EVM version name (e.g., "London" for Solidity 0.8.16)
- **SKY Backstop definition expanded** (A.4.3): added definition of "SKY Backstop Event" — the period when the recapitalization mechanism is actively minting and selling SKY to close a collateral shortfall

### Housekeeping

- "Governance and Spell Process execution" → "an Executive Vote" in SP-BEAM and stUSDS BEAM exception descriptions
- "Governance Facilitators" → "Core Facilitator" in multiple A.1.9 governance security and A.1.11/A.1.12 process documents
- Various HTML linting fixes (unclosed `</td>`, `<oL>` → `<ol>`, `start=1` removed from `<ol>`, `</code>` → `<code>` typo)

### Context

The Executive Process Definition is the single largest structural addition to the Governance Scope in this period — it codifies what was previously informal process knowledge into over 100 Atlas documents. This provides a formal accountability framework for the spell lifecycle and establishes the Governance Point / Technical Point / Content Liaison roles that govern how Executive Votes are prepared and published. SKY was ~$0.059-0.063 and USDS supply ~$8-9B.

---

## PR #63 — September 29 edit

**Merged:** 2025-10-02 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping

- Grammar fix in A.1.4 adjudication process: "Core Facilitator are responsible" → "Core Facilitator is responsible"
- Grammar fix in A.1.4 penalty section: "Core Facilitator conclude" → "Core Facilitator concludes"
- A.1.4 misalignment allegation process: removed "Any Scope Facilitator has the authority to formally raise an allegation" clause; replaced with "Core Facilitator's failure... must be adjudicated by Core GovOps"
- A.1.4 governance security breach: "Mandated Derecognition" now by "Core Facilitator" instead of "the Facilitators"
- A.1.4 Governance Facilitator allegation: simplified — if Core Facilitator is subject of allegation, adjudication may be initiated by Core GovOps (removed reference to "Responsible Facilitator from any Scope")
- Double-space typo fixed in Core Council Executor Facilitator definition
- Various "Governance Facilitators" → "Core Facilitator" propagations in A.1.6, A.1.9, A.1.11, A.1.12 documents

### Context

Continuation of the Core Facilitator terminology migration begun in PR #59. This PR also makes substantive governance changes to the misalignment allegation process — Core GovOps now adjudicates allegations against the Core Facilitator (previously any Scope Facilitator could initiate), consolidating oversight within the Core Council structure.

---

## PR #59 — Atlas Edit Weekly Cycle Proposal 2025 09 15

**Merged:** 2025-09-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes

- **Core Council introduced** (A.0.1, new): The Core Council is defined as a group of Executors responsible for operationalizing the protocol at the Sky Core level — monitors Operational Executor compliance, enforces Atlas, oversees governance processes, evolves Risk Framework, monitors ACs, and addresses disputes. Starts with a single seat (Core Council Executor Agent 1), targeting up to seven elected seats long-term.
- **"Core Executor Agent" renamed to "Core Council Executor Agent"** (A.0.1): reflects the new Core Council structure; "Core Executors" shorthand replaced with "Core Executor Agents" throughout
- **"Core Executor GovOps" renamed to "Core Council GovOps"** (A.0.1): "Core GovOps" actors now explicitly operate within Core Executor Agents
- **"Core Executor Facilitator" renamed to "Core Council Executor Facilitator"** (A.0.1): these Facilitators now formally called "Core Facilitator" (singular)
- **Governance Facilitators replaced by Core Facilitator** across Preamble: "Governance Facilitators" → "Core Facilitator" (singular) in Bootstrapping Governance Poll authorization, Atlas Interpretation precedent, conflict resolution, and other key governance documents
- **New Article A.4.6 — Protocol Mechanisms** (A.4.6): defines maintenance/housekeeping mechanisms and contracts for administering the Sky Ecosystem

### Housekeeping

- "Core Executors" shorthand expanded to "Core Executor Agents" in Executor Agent definition text
- Subject-verb agreement and wording alignment throughout A.0.1 documents

### Context

This is the foundational PR that restructures Sky governance from the multi-Facilitator "Governance Facilitators" model to the consolidated "Core Council / Core Facilitator" model. The introduction of the Core Council as a formal body — starting with one seat and scaling to seven — is the structural backbone for many subsequent PRs that propagate this terminology change across A.1, A.2, A.3, and other scopes. SKY was trading around $0.07 at the time; USDS supply was approximately $7-8B.

---

## PR #57 — Sept 8 atlas edit

**Merged:** 2025-09-11 | **Type:** Weekly edit (Atlas Axis)

### Material Changes

- **Sky Forum definition added** (A.0.1): canonical definition of the Sky Forum at `https://forum.sky.money/` — posts must use the "Sky Core" category for Sky Core governance; Prime-related posts use the Prime's category. Authors should apply relevant tags.

### Housekeeping

- DAOcraft → Amatsu rename propagated to A.0 preamble references.

---

## PR #43 — August 11 edits

**Merged:** 2025-08-15 | **Type:** Weekly edit (Atlas Axis)

### Material Changes

- **"Star Agent" → "Prime Agent"** throughout Preamble (A.0.1): definitions for Agent, Prime Agent (was "Star Agent"), Executor Agent, Operational Executor Agent, GovOps, and Sky Primitives updated — no content change beyond the terminology rename.

---

## PR #38 — Atlas Edit Weekly Cycle Proposal 2025-08-04

**Merged:** 2025-08-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes

- **yUSDS renamed to stUSDS** (A.0.1): definition updated; all references to "yUSDS converter smart contract" replaced with "stUSDS converter smart contract".

---

## PR #30 — Atlas edit weekly cycle proposal 2025 07 14

**Merged:** 2025-07-18 | **Type:** Weekly edit (Atlas Axis)

### Material Changes

- **"Unrewarded USDS" definition added** (A.0.1): USDS balances not receiving the Sky Savings Rate, Integration Boost, or USDS Token Rewards (including both SKY and Agent token rewards). Previously the definition lived only in A.2.4; moving it to the Preamble makes it canonical.

### Housekeeping

- "Actively Stabilizing Collateral Rental Primitive" → "Asset Liability Management Rental Primitive" (A.0.1 primitives list) — cosmetic rename, no content change.

---

## PR #17 — Cleanup multiple scopes and artifacts

**Merged:** 2025-06-20 | **Type:** Housekeeping

Multi-scope formatting cleanup including Preamble documents — inline multi-line cell text collapsed to single lines, no content changes.

---

## PR #15 — 2025-06-16 weekly atlas edit proposal

**Merged:** 2025-06-19 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping

- **Voting Power definition** (A.0.1): "SKY or MKR holder" → "SKY holder"; references to MKR removed. "SKY/MKR holders retain control" → "SKY holders retain control."
- **GSM Pause Delay legacy context** (A.0): "increasing liquidity of the MKR token" → "increased liquidity of the SKY token."

---

## PR #11 — cleanup of article and preamble sections

**Merged:** 2025-06-10 | **Type:** Housekeeping

Whitespace and inline formatting cleanup in the Atlas Preamble (A.0) and Article/Scope top-level documents — multi-line table cell text collapsed to single lines throughout Scopes, Articles, and Preamble sections. No content changes.

---

## PR #1 — 2025-05-26 Atlas Edit Weekly Cycle Proposal

**Merged:** 2025-06-07 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping

- Minor wording updates in A.0 definitions: "First Loss Capital" → "Risk Capital" references updated; no new A.0 documents added.

---
