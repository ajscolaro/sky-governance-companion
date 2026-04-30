# Governance Scope — Change History

Atlas path: `A.1` — The Governance Scope

---

## PR #227 — Atlas Edit Proposal — 2026-04-27
**Merged:** 2026-04-30 | **Type:** Weekly edit (Atlas Axis — Poll #1630)

### Material Changes
- **Protocol Security Workstream Lead** (`A.1.7.1.2`, UUID `93651fb8…`): New specialized role for a Professional Ecosystem Actor providing security oversight and incident coordination across the Sky Ecosystem. No conflicting business activities allowed. Currently held by Vamsi.
- **GSM Pause Delay**: 24 hours → **48 hours** (`A.1.9.3.1.2`)
- **Plasma SkyLink Bridge deployment deferred**: "April 23, 2026 Executive Vote" → "a future Executive Vote" (`A.1.9.4.1.4.2`); timing now determined (not merely modifiable) by Core Facilitator in consultation with relevant Ecosystem Actors

### Context
The GSM delay doubling to 48h provides a wider security window for contested spells. The Plasma bridge deferral held back the deployment from the April 23 exec — that exec still ran and recorded parameter changes in PR #226. Poll #1630 passed (non-voters: excel, kuzmich, opex).

---

## PR #224 — Atlas Edit Proposal — 2026-04-20
**Merged:** 2026-04-24 | **Type:** Weekly edit (Atlas Axis — Poll #1629)

### Material Changes
- **Novel Spell Items process** (`A.1.9.2.3.3`, UUID `af13ac4b…`): new definition and multi-step process for out-of-cadence Executive Vote items — Core GovOps/Core Facilitator requests → confirms novelty → spell teams conduct technical feasibility analysis → Core Facilitator obtains stakeholder approval and schedules; complements the Recurring Items section at `A.1.9.2.3.1`
- **Plasma SkyLink Bridge** (`A.1.9.4.1.4`): full documentation for USDS/sUSDS token bridge and governance bridge between Ethereum Mainnet and Plasma, deployed in the April 23, 2026 Executive Vote
  - Freezer Multisig on Plasma: `0xB3d26eF66F53C9546d1365F417a85B0Aa69049eE`, 2/5 (3× Soter Labs + 1× Redline Facilitation Group + 1× Launch Agent 6)
  - USDS rate limit: 5M/day (net accounting); sUSDS: no rate limit set at launch
  - Token Bridge and Governance Bridge validators specified
- **Plasma SkyLink Freezer Multisig** added to governance-controlled multisig list (`A.1.9.3.2.17`)

### Housekeeping
- Solana SkyLink Bridge docs updated: removed forward-looking deployment language; confirmed both phases completed (Phase 1: Nov 13, 2025 Executive Vote; Phase 2: Nov 17, 2025 Out-Of-Schedule Executive Vote).

---

## PR #219 — Atlas Edit Proposal — 2026-04-06
**Merged:** 2026-04-09 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Avalanche SkyLink Bridge added** (A.1.9.4.1.3, new): Full documentation for USDS/sUSDS bridge to Avalanche C-Chain, scheduled for deployment in the April 9, 2026 Executive Vote.
  - **Token Bridge:** validators LayerZero and Nethermind, quorum 2/2
  - **Governance Bridge:** validators Horizen, LayerZero, Nethermind, Deutsche Telekom, Canary, Luganodes, P2P — quorum 4/7
  - **USDS rate limit:** 5,000,000 USDS/day (net accounting); sUSDS: no limit set
  - **Avalanche-side Freezer Multisig:** `0x4deb1B5372dd3271691A9E80bCBfd98F5aa27f30` — 2/5 (Soter Labs ×2, Endgame Edge ×2, Grove ×1)
  - Rate limits modifiable by Core Facilitator + Risk Advisor via Executive Vote (no Governance Poll required)

### Housekeeping
- "Solana LayerZero Bridge" → "Solana SkyLink Bridge" and bridge hierarchy restructured under A.1.9.4.1.1–.3 (Ethereum/Solana/Avalanche); same UUIDs, renumbering only for Solana docs
- "Ethereum LayerZero Freezer Multisig" → "Ethereum SkyLink Freezer Multisig" (A.1.9.3.2.14) and "Solana LayerZero Freezer Multisig" → "Solana SkyLink Freezer Multisig" (A.1.9.3.2.15) — cosmetic rename, no content change
- "Scope Facilitator" → "Core Facilitator" in multiple governance process documents (A.1.1.2.1, A.1.2.3.1, A.1.4.9.3.0.4.1, A.1.10.2.2, AD operational security allegation process); subject-verb agreement fixes

### Context
The Avalanche bridge deployment is coordinated with two Grove-specific changes in this same PR (Grove designated Avalanche Pioneer Prime; Grove as a Freezer Multisig signer). The bridge follows the same architectural pattern as Solana — identical quorum structures, same multisig governance — though notably the Avalanche Token Bridge uses a 2/2 quorum (only LayerZero + Nethermind) versus the Solana bridge's higher validator count. The "LayerZero → SkyLink" renaming across A.1.9.4 suggests a broader rebranding of the bridge infrastructure away from the vendor name toward a protocol-native name.

---

## PR #186 — 2026-02-16 AEW proposal
**Merged:** 2026-02-22 | **Type:** Weekly edit (Atlas Axis — Poll 1618) | **+2119/-158 lines**

### Material Changes

- **New: Aligned Delegate Responsibilities Section** (`A.1.5.2`, new): AD compliance framework is formalized with specific, enforceable requirements:
  - **Voting participation: ≥75% over past six months** (`A.1.5.2.1`) — failure is a Tier 1 (Procedural) breach. Measured from formal recognition date; applies only to votes with delegated SKY
  - **Excessive Abstention** (`A.1.5.2.1.1`): Core Facilitator may issue Tier 1 notice for abstention patterns suggesting disengagement (no fixed threshold; discretionary)
  - **Vote explanations required** (`A.1.5.2.2`): must (1) demonstrate understanding, (2) articulate reasoning, (3) address substantive aspect; posted within 1 week of vote end
- **New: Graduated Response Framework** (`A.1.5.6.1`, new) — replaces the old single-tier "Warnings Appropriate For Mild Breach" system (the entire A.1.4.9.2.1 "Warning Notice / Warning Recording / List of Formally Warned ACs" apparatus is deleted):
  - **Tier 1 (Procedural) breaches** (`A.1.5.6.1.1`): procedural failures (late vote explanations, minor lapses). First offense → public Forum notice by Core Facilitator. Notice expires 12 months after issuance. Subsequent Tier 1 while ≥2 active notices outstanding = Tier 2.
  - **Tier 2 (Integrity) breaches** (`A.1.5.6.1.2`): fundamental integrity failures — unsubstantiated public accusations, proven dishonesty, collusion, kickbacks, opsec violations, voting against pure-Atlas-recorded Executives, Voting Estoppel violations. **Result: immediate derecognition regardless of prior record.**
  - **Good-Faith Criticism safe harbor** (`A.1.5.6.1.2.0.3.1`): neutral/professional criticism with supporting facts is protected — preserves dissent/whistleblowing
  - **Breach Registry** (`A.1.5.6.1.3`, Active Data Controller): Core Facilitator is Responsible Party; updates via 'Alignment Conserver Changes' protocol
- **New: Voting Estoppel Rule** (`A.1.5.6.2`, new): ADs who vote **in favor** of a proposal are deemed to have read and understood it. Claims of ignorance are not accepted as defenses; a subsequent ignorance claim is a Tier 2 breach. Only applies to yes votes — no/abstain retain standing to raise concerns. Exception: materially misleading proposal text or newly-emerged material facts (burden on the AD).
- **New: Probationary Period** (`A.1.5.1.4`, new): first 90 days after AD recognition = Probationary Period. During this window, Tier 1 breaches → **immediate derecognition without prior warning**.
- **New: Core Facilitator Conflict-of-Interest recusal** (`A.1.4.9.5`, new): Core Facilitator must recuse from adjudications where conflicted; Core GovOps conducts. In case of doubt, recuse.
- **New: AD membership in ERG gated** (`A.1.8.1.2.4`, new): AD participation in the Emergency Response Group is no longer automatic from SKY delegation or RD status; Core GovOps must approve based on competence/reliability
- **New: Level 1/2 RDs are compliance monitors** (`A.1.5.4.5`, new): Level 1 and Level 2 Ranked Delegates must monitor AD communications compliance as a condition of their compensated position; failure to submit an assessment when prompted by the Core Facilitator is a Tier 1 breach
- **New Aligned Delegates added** (`A.1.5.1.5.0.6.1`): OPEX (EA `0xE3dc…604f`), AxisLegati (EA `0x9B4A…dcb6`) — admitted to the AD roster in this cycle

### Housekeeping

- **Section renumbering cascade** in A.1.5: new A.1.5.2 ("AD Responsibilities") pushes old A.1.5.2→A.1.5.3 ("In General"), A.1.5.3→A.1.5.4 ("Ranked Delegates"), A.1.5.4→A.1.5.5 ("Kickbacks Prohibited"), A.1.5.5→A.1.5.6 ("Swift Action"), A.1.5.6→A.1.5.7 ("Operational Security"), A.1.5.7→A.1.5.8 ("Derecognition"), A.1.5.8→A.1.5.9 ("Err On Side Of Caution"), A.1.5.9→A.1.5.10 ("Emergency Contact Mechanism"). UUIDs unchanged — all Ranked Delegate budgets, Triggering Threshold references, Signal Account rules, etc., renumbered in place with no value changes.
- `A.1.5.1.4` → `A.1.5.1.5` ("List Of Recognized Aligned Delegates") renumbered to make room for the new Probationary Period at `A.1.5.1.4`
- "Scope Facilitator" → "any Facilitator" in `A.1.5.6` (misalignment allegation authority expanded to all Facilitators, not just Scope Facilitators)
- Duplicate/restructured research-track content in the Adjudication Article (`A.1.4.9.1` area) — same content, reordered paragraphs; no substantive change

### Context

This AEW represents the **largest structural change to AD governance since the Core Council transition** in September 2025 (PR #59). The deletion of the old "formal warning + list of warned ACs" model in favor of the two-tier Graduated Response Framework fundamentally rewrites how Sky handles delegate misconduct: Tier 2 is now a bright-line *immediate derecognition* trigger with no discretionary warning step, and the Voting Estoppel Rule closes a previously-available "I didn't understand it" defense for yes votes. Combined with the 90-day Probationary Period and the new Level-1/2 peer-review responsibility, the framework pushes accountability earlier, makes Tier-2 penalties non-negotiable, and gives Core Facilitator structured discretion for the gray zone between procedural and integrity breaches. The Good-Faith Criticism safe harbor is the one intentional counterweight — protecting whistleblowing and dissent from being swept into "unsubstantiated public accusation" Tier 2 classifications. Ratification Poll 1618 passed 10-0 with 2 non-voters. SKY ~$0.065, USDS supply ~$9.9B at merge.

---

## PR #181 — Add AxisLegati
**Merged:** 2026-02-10 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New AD recognized: AxisLegati** — added to the Active AD roster (`A.1.5.1` table):
  - Cold wallet: `0x9B4AF496CC72c432586e85a1D8264A2708c4dcb6` (verified sig #301787)
  - Hot wallet: `0x7bc5a420b6524Fa925F1321A01825438369E3c2e` (verified sig #301786)
  - Recognition submission: https://forum.sky.money/t/axislegati-ad-recognition-submission/27677

---

## PR #139 — Fix delegate document numbering
**Merged:** 2025-12-08 | **Type:** Housekeeping

Renumbered the entire Ranked Delegates section from `A.1.5.4` to `A.1.5.3` (and downstream docs correspondingly, e.g. `A.1.5.4.1.1.2` → `A.1.5.3.1.1.2`), plus two cross-reference fixes: `A.1.4.5.1` link updated from `A.1.5.4.5.2` → `A.1.5.3.5.2`, and `A.1.5.16.0.4.1` renumbered to `A.1.4.8.0.4.1`. All UUIDs unchanged; no content changes.
- **Modified** `A.1.5.4.4.2` - AD Buffer And Loss Of Budget [Core]
- **Modified** `A.1.5.4.1.3.3` - Selection Of Level 3 Ranked Delegates [Core]
- **Modified** `A.1.5.4.1.3.2` - Budget For Level 3 Ranked Delegates [Core]
- **Modified** `A.1.5.7` - Mandate To Maintain High Level of Operational Security [Section]
- **Modified** `A.1.5.4.3.2.0.3.2` - Voting-Communication Metrics - Element Annotation [Annotation]
- **Modified** `A.1.5.4.1.1` - Level 1 Ranked Delegates [Core]
- **Modified** `A.1.5.10` - Emergency Contact Mechanism [Section]
- **Modified** `A.1.5.4.1.2.1` - Number Of Level 2 Ranked Delegates [Core]
- **Modified** `A.1.5.4.2` - Budget Accrual [Core]
- **Modified** `A.1.4.8.0.4.1` - Facilitators’ Authority To Raise Formal Allegation [Action Tenet]
- **Modified** `A.1.5.4.1.2.3.1` - Current Level 2 Ranked Delegates [Core]
- **Modified** `A.1.5.4.5.2` - Atlas Workstreams [Core]
- **Modified** `A.1.5.4.3.2` - Voting-Communication Metrics [Core]
- **Modified** `A.1.5.4.1` - Levels Of Ranked Delegates [Core]
- **Modified** `A.1.5.4.1.1.3` - Selection Of Level 1 Ranked Delegates [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #133 — 2025-12-01 AEW Proposal
**Merged:** 2025-12-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Level 1 Ranked Delegate budget**: 600,000 USDS/year → **400,000 USDS/year** (A.1.5.4.1.1.2)
- **Whistleblower Bounty sections removed**: `A.1.5.17` (AD misalignment bounty) and `A.1.5.20` (opsec breach bounty) deleted entirely, along with their Action Tenets and Annotations. The AD Buffer's "collateral for whistleblower bounty" function is removed; buffer now purely holds compensation and triggering-threshold reserves.
- **AD Buffer renamed to "Deduction Of Penalties From AD Buffer"** (A.1.5.4.4.3): the former section on whistleblower bounty collateral becomes a deduction-of-penalties section — penalties can be deducted from the buffer but the whistleblower bounty mechanism is gone.
- **Triggering Threshold formalized** (A.1.5.4.4.2.1.1, new): defined as one month of Level 3 Ranked Delegate compensation. Applied consistently to both Atlas Edit Weekly Cycle and Atlas Edit Monthly Cycle proposal triggering requirements (previously only referenced one cycle type).
- **Payout Limitations scope expanded** (A.1.5.4.4.2.1): now blocks payouts that would reduce AD Buffer below the Triggering Threshold for either AEW or AEM cycle proposals (not just AEW).

### Housekeeping
- Removed five element annotations related to the whistleblower bounty mechanism (collateral, one-month allocation, opsec/privacy definitions).

### Context
The Level 1 RD budget cut (600K → 400K USDS/year) and whistleblower bounty removal are the two material governance changes. The budget reduction brings L1 RD compensation closer to the L3/L2 level — possibly reflecting a policy decision to compress the compensation differential. The whistleblower bounty removal simplifies the AD Buffer to a pure compensation/triggering-threshold vehicle, eliminating a complex collateral mechanism that was likely unused.

---

## PR #135 — fix typos
**Merged:** 2025-12-03 | **Type:** Housekeeping

Two typos fixed: "Multsig" → "Multisig" in the SparkLend Security Access Multisig description; "Protego Eta Parameter Definitio" → "Protego Eta Parameter Definition" in the document title at `A.1.9.5.3.1.3.4`. No content changes.

---

## PR #121 — Nov 24 Atlas edit
**Merged:** 2025-11-30 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **"Agent Spell" → "Prime Spell" terminology normalized** in Prime Spell Security Enforcement framework: `A.1.9.2.3.2.2.3` "Execution Of Agent Spells" → "Execution Of Prime Spells"; `A.1.9.2.3.2.2.3.2.1` "Sky Core Spell Executes Agent Spell" → "Sky Core Spell Executes Prime Spell". Aligns wording with the broader framework introduced in PR #110.

### Context
Terminology cleanup in the A.1.9 Prime Spell Security Enforcement section. Rename-only backfill — this PR primarily renamed LA4 → Obex (see A.6 changelogs); other governance content not processed in detail.

---

## PR #110 — Nov 10 edit
**Merged:** 2025-11-13 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Prime Spell Security Enforcement framework added** (A.1.9, new): Comprehensive enforcement system for Prime Agent spell security — see A.0 changelog for full detail. Key additions to governance scope: Incident Registry (Active Data, Core Facilitator as Responsible Party), penalty authority (Core Facilitator + Core GovOps), and linkage to Prime Agent Credit Rating System.

### Context
See A.0--preamble changelog for comprehensive description. The governance scope additions establish the formal recordkeeping and enforcement authority components.

---

## PR #79 — Oct 16th Spell updates
**Merged:** 2025-10-24 | **Type:** Spell recording (2025-10-16)

### Material Changes
- **DC-IAM vault list expanded** (A.1.9 governance security): Added 6 vault types to the Debt Ceiling Instant Access Module list: ALLOCATOR-SPARK-A, ALLOCATOR-BLOOM-A, ALLOCATOR-NOVA-A, ALLOCATOR-OBEX-A, LSE-MKR-A, LSEV2-SKY-A

### Context
Records on-chain vault types that were already deployed but not yet listed in the Atlas DC-IAM documentation. The body notes that Spark changes were pending from the prior week's poll and Grove changes from the current week's poll.

---

## PR #89 — 2025-10-20 Atlas Weekly Cycle Proposal
**Merged:** 2025-10-23 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core Council Risk Advisor role created** (A.1.7, new): BA Labs designated; provides financial analysis and risk management advice to Core Council. Limited conflict-of-interest waiver for BA Labs' Ethena work.
- **Interim Deployments framework added** (A.1.9, new): Allows Prime Agents to deploy Allocation Instances under testing constraints before full risk assessment. 100% CRR required during interim period.
- **Agent Artifact Review framework added** (A.1.14, new): Core GovOps enforcement authority over Agent Artifact compliance — review, findings, remediation, appeals process.

### Housekeeping
- "Stability Scope Advisors" → "Core Council Risk Advisor" throughout governance documents

### Context
See A.0--preamble changelog for comprehensive description covering all scopes affected by this PR.

---

## PR #82 — HTML linting
**Merged:** 2025-10-16 | **Type:** Housekeeping

### Housekeeping
- Pure HTML linting fixes across the entire Atlas: `<oL>` → `<ol>`, `<uL>` → `<ul>`, `<lI>` → `<li>`, unclosed `</td>` tags, stray `</tr>` tags, unclosed `<p>` tags, `</code>` → `<code>` typo fix, `<ol start=1>` → `<ol>`, double `<tr>` tags removed, missing `</tr>` tags added, `</dfn>` references fixed in closing tags
- No data or content changes — HTML structure corrections only

### Context
Comprehensive HTML cleanup pass. All changes are tag-level corrections that do not alter any document content or parameter values.

---

## PR #78 — October 13 edit
**Merged:** 2025-10-16 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **A.1.6 Facilitators section restructured — 17 documents deleted:** Entire Facilitator management framework removed including named roster (JanSky, Endgame Edge, Ecosystem) and budget table (42,000 USDS + 432,000 SKY/month per facilitator). See A.0 changelog for full detail.
- **"Governance Facilitators' Review" → "Core Facilitators' Review"** (A.1.12): Core Facilitator now sole authority for AEP review and blocking for misalignment

### Housekeeping
- Continued "Governance Facilitators" → "Core Facilitator" propagation across A.1 governance documents

### Context
See A.0--preamble changelog for comprehensive description. The deletion of A.1.6 Facilitator management is the structural anchor of the Core Council transition.

---

## PR #66 — 2025-10-06 Weekly Edit Proposal
**Merged:** 2025-10-09 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Full Executive Process Definition added** (A.1.9 A2): ~100+ new documents comprehensively defining the end-to-end Executive Process. Defines roles (Governance Point, Technical Point, Content Liaisons), Spell Roster (Sidestream + Dewiz), 13-step process breakdown, Smart Contract Deployment Verification, and recurring items (Office Hours, Global Line Modifier). See A.0 changelog for full detail.

### Housekeeping
- "Governance Facilitators" → "Core Facilitator" in governance security and weekly/monthly cycle documents

### Context
See A.0--preamble changelog for comprehensive description. The Executive Process Definition is the largest single structural addition to A.1 in this period.

---

## PR #63 — September 29 edit
**Merged:** 2025-10-02 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- Grammar fixes in A.1.4 adjudication process and penalty sections
- Misalignment allegation process simplified: Core GovOps now adjudicates allegations against Core Facilitator (replaces "any Scope Facilitator")
- Continued "Governance Facilitators" → "Core Facilitator" propagation

### Context
See A.0--preamble changelog. Primarily housekeeping continuing the Core Facilitator terminology migration.

---

## PR #59 — Atlas Edit Weekly Cycle Proposal 2025 09 15
**Merged:** 2025-09-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **"Governance Facilitators" → "Core Facilitator"** propagated across A.1 governance documents: Atlas Interpretation, conflict resolution, AC misalignment handling, adjudication, derecognition, and more
- **Core Council structure** introduced — see A.0 changelog for foundational changes

### Context
See A.0--preamble changelog for the comprehensive description of the Core Council introduction. A.1 changes are primarily the propagation of the "Governance Facilitators" → "Core Facilitator" rename.

---

## PR #57 — Sept 8 atlas edit
**Merged:** 2025-09-11 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core Simplification Buffer Budget removed** (A.5.10 deleted): the entire Article covering the Core Simplification Buffer Budget (10M USDS + 70M SKY budget) and its sub-documents (including the 8M USDS one-time transfer authorization) were deleted. A prior AEP had authorized the transfer; this edit formally removes the now-exhausted budget article.
- **DAOcraft renamed to Amatsu** (A.2.x, Spark SLL instance): the Executor Accord Primitive instance previously named DAOcraft is renamed to Amatsu throughout — covers Spark's SLL instance config docs and the Near-Term Accessibility Reward process (calculates Accessibility Reward on behalf of Support Facilitators). Name change only; no parameter changes.
- **Sky Forum definition added** (A.0.1): new canonical definition of the Sky Forum at `https://forum.sky.money/`. Posts must use the "Sky Core" category for core governance; Prime-related posts use the Prime's category.
- **stUSDS BEAM exception refined** (A.1.x): "modify rates" narrowed to "modify certain parameters" — clarifies that the BEAM doesn't bypass the GSM for all rate changes, only specific parameters.
- **stUSDS Rate Normalization Logic added** (A.4.4): added Update Methodology specifying Stability Scope Advisors may deviate from methodology during manual phase but must reduce deviations over time before automation.
- **Monthly Settlement Cycle Implementation text restructured** (A.2.6): "initial implementation will occur in three stages" → "The documents herein define the initial implementation" — editorial cleanup, content unchanged.
- **Star Agent → Prime Agent** remaining reference updated in Spark delegate voluntary offboarding process: "Spark Star category" → "Spark Prime category."

### Context
PR #57 finalizes a major housekeeping pass from the September 8 weekly edit cycle. The Core Simplification Buffer Budget deletion is the most significant material item — removes a temporary governance budget article that served its purpose (8M USDS transfer). DAOcraft→Amatsu is a name change that doesn't affect operational logic.

---

## PR #54 — Atlas Edit Weekly Cycle Proposal - Week of 2025-09-01
**Merged:** 2025-09-05 | **Type:** Weekly edit (Atlas Axis — Poll 1562)

### Material Changes
- **`LastAmount` parameter defined** (A.2.4): new `lastAmount` definition added — remaining allowance at last update, used in rate limit formula. Companion to the existing `lastUpdated` definition.
- **stUSDS BEAM Automatic Updates** (A.4.4): new document added specifying that once the Operator Hot Wallet is added as Operator of the stUSDS BEAM, all parameter updates must be made by that Hot Wallet (not the Operator Multisig).
- **A.5.10 Core Simplification Buffer Budget formatting fix** (housekeeping in this PR; budget itself removed in PR #57).

### Housekeeping
- `cap`/`line` parameters wrapped in `<code>` tags in STUSDS_MOM description.
- Multiple `<dfn>` tag punctuation fixes throughout A.4.4 (trailing period removed from cross-references).
- `stUSDS BEAMparameters` → `stUSDS BEAM parameters` (missing space).
- `"Outflow limits are unlimited` quote mark cleanup in Outflow Rate Limits definition.
- A.5.10 multi-line `<dfn>` collapsed to single line; content unchanged.
- HTML whitespace normalization in A.1.8 Emergency Response Group Membership list.

### Context
Primarily a formatting and minor clarification pass on A.4.4 (stUSDS BEAM) and A.2.4 (rate limits). The new `lastAmount` and automatic Operator Hot Wallet documents are the only substantive additions. Poll 1562 passed.

---

## PR #52 — 2025-08-25 Atlas Weekly Cycle Proposal Edits
**Merged:** 2025-08-29 | **Type:** Weekly edit (Atlas Axis — Poll 1561)

### Material Changes
- **SparkLend Security Access Multisig signing requirement**: 2/5 → **3/5**
- **SparkLend Security Access Multisig signer change**: Rema removed, LucasManuel added
- **Emergency replacement exception clarified**: signer replacement after self-reported key loss or voluntary exit "does not require a Governance Poll" — previously implied but not stated explicitly.

### Context
Raising SparkLend's security multisig threshold from 2/5 to 3/5 meaningfully increases the security bar for emergency parameter changes. The signer rotation (Rema out, LucasManuel in) coincides with the threshold change. Poll 1561 passed.

---

## PR #51 — Update warned alignment list
**Merged:** 2025-08-25 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **SkyStaking added to warned alignment list** (A.1.5.x): new entry dated 2025-08-15, entity type "Aligned Delegate," reason linked to forum notice at `https://forum.sky.money/t/atlas-edit-weekly-cycle-proposal-week-of-2025-08-04/26957/9`.

---

## PR #43 — August 11 edits
**Merged:** 2025-08-15 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **"Prime Delegate" → "Ranked Delegate"** throughout A.1.5 and A.1.11: documents renamed ("Number of Ranked Delegate Slots", "Budget For Ranked Delegate Slots", "Budget Amount For Ranked Delegate Slots" — 48,000 USDS/year unchanged), all PD/Prime Delegate references in voting-activity metrics, voting-communication metrics, emergency comms requirement, signal account, AD Buffer, triggering requirements, and rejection clauses updated to RD/Ranked Delegate.
- **"Star Agent" → "Prime Agent"** throughout A.1 governance documents: Agent Artifact intent-to-suspend notices and related process documents updated; content unchanged.
- **Whistleblower bounty rule clarified** (A.1.5): penalties may be deducted (not automatic confiscation); remaining AD Buffer must be paid back to the derecognized AD.

---

## PR #38 — Atlas Edit Weekly Cycle Proposal 2025-08-04
**Merged:** 2025-08-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Linear Interpolation Module (lerp) formally documented** (A.1.9, new section): defines the `lerp` contract as a governance tool to adjust parameters linearly over time without additional Executive Votes. Key rules: activated via Executive Vote; each instance has `start`, `end`, `duration`; governance process mirrors that of the parameter being adjusted — if param needs a poll first, lerp also needs a poll. Factory contract (LERP_FAB) maintains registry of active instances.
- **Monthly Settlement Cycle Stage 1 P&L details added** (A.2.6): Stage 1 Simplified P&L Calculation fully specified — amounts due from Sky to Stars (Accessibility Reward + Agent Rate) and from Stars to Sky (Allocation System Revenue and Profit, Instance Expense = interest on allocated principal at Base Rate).

### Housekeeping
- "yUSDS" → "stUSDS" in SKY Staking Mechanism article description (A.3).

---

## PR #31 — Atlas Edit Weekly Cycle Proposal 2025-07-21
**Merged:** 2025-07-25 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **TGE deadline fixed to July 1, 2025** (A.2.10): Token Launch Penalty and Income Generation commencement date changed from "upon Risk Framework finalization" to a concrete date of July 1, 2025. Pre-TGE expense advances now apply to expenses incurred "after July 1, 2025" (was "60 days prior to Risk Framework finalization"). 70% income credit accumulation begins from July 1.
- **Chainlog formally defined** (A.1.9, new): The Chainlog is documented as an on-chain governance-managed registry of official Sky contract addresses, available at `https://chainlog.sky.money/`. Updates classified as housekeeping items and can be included directly in Executive Votes.
- **Forum tag → category** for Spark, Grove, Launch Agent 2, Launch Agent 3: "Spark" tag → "Spark Star" category; "Grove" tag → "Grove Star" category; "Launch Agent 2" tag → "Launch Agent 2 Star" category; "Launch Agent 3" tag → "Launch Agent 3 Star" category — affects root edit submission requirements, rebate review processes, and general forum usage rules.
- **Short-Term Transitionary Measures added** for Launch Agents 2 and 3: until Powerhouse supports Artifact Edit Proposals, token holders may submit via Forum; until it supports Artifact updates, Operational Facilitators work with Governance Facilitators via GitHub.

### Housekeeping
- Contract names aligned with Chainlog keys: "SparkLend Freezer Mom" → "FREEZER_MOM"; "SplitterMom" → "SPLITTER_MOM"; "PSM_MOM" → "LITE_PSM_MOM"; "SP_BEAM_MOM" → "SPBEAM_MOM". Adds inline reference to "GSM Pause Delay" where previously just "GSM delay". Typo fix: "Afer" → "After" in ADs' Standby Spell requirements.

---

## PR #30 — Atlas edit weekly cycle proposal 2025 07 14
**Merged:** 2025-07-18 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Emergency Standby Spell process language tightened** (A.1.9): "decision to use a Standby Spell" → "decision to initiate the process to use a Standby Spell" (for TechOps trigger); "After the Support Facilitators decide" → "If the Support Facilitators decide" (both Standby and Protego); ADs' Standby Spell checklist changed from ordered list to bullet list; TechOps trigger phrasing parallelized with Protego section. Substantive effect: softens the mandatory implication of the TechOps trigger.
- **Custom Spell Voting Page restriction clarified** (A.1.9): permitted "without having a visible spell on the Voting Portal" → "without using the standard Spell process" (broader framing). Applied to both Standby Spell and Protego sections.

---

## PR #25 — New AD added - Kuzmich
**Merged:** 2025-07-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New AD recognized**: Kuzmich — recognition address `0x2847540606a790E5083d0D63470fAb01344c8e92`, vote contract `0x2C89024c13A80bC1B662A3dB990524652C15221C`, forum: https://forum.sky.money/t/ad-recognition-submission/26743

---

## PR #7 — AEP-11: Edit
**Merged:** 2025-06-23 | **Type:** AEP-11

### Material Changes
- **Communication channel moderation framework added** (A.2.7 in support scope, new): See A.2--support changelog for full detail. A.1 note: only Governance Facilitators may ban a user from the Sky Forum when doing so would block an active governance process.

### Context
AEP-11 ratified. Forum: https://forum.sky.money/t/aep-11-moderation-policies-of-the-sky-ecosystem-communication-channels/26225

---

## PR #15 — 2025-06-16 weekly atlas edit proposal
**Merged:** 2025-06-19 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- MKR references removed from Voting Power definition and AD annotations: "SKY or MKR holder" → "SKY holder"; "SKY/MKR" → "SKY" in cumulative Voting Power annotation.
- Delegate Contract registration URL updated: `vote.makerdao.com/account` → `vote.sky.money/account`.

---

## PR #6 — Update Multiple ADs
**Merged:** 2025-06-16 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **8 ADs updated to v3 voting contracts**: Bonapublica, PBG, WBC, BLUE, Cloaky, AegisD, Excel, Tango — new contract addresses and verification signatures recorded in the AD Active Data table.
- **New AD recognized**: Sky Staking (recognition address `0x05c73AE49fF0ec654496bF4008d73274a919cB5C`).

---

## PR #14 — Derecognize ADs that failed to migrate
**Merged:** 2025-06-13 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **12 ADs derecognized** from the AD roster: JAG, Penguin Soldier, Vision, Nimsen, Ikagai, Byteron, Shanah, Pipkin, JuliaChang, StoneWill, Rocky, Jiaozi — all removed for failure to migrate to v3 contracts (context: PR #6 updated v3 addresses for the remaining active ADs).

---

## PR #12 — governance scope cleanup
**Merged:** 2025-06-13 | **Type:** Housekeeping

Whitespace and inline formatting cleanup across A.1 governance scope documents — multi-line cell text collapsed to single lines, bullet lists converted to `<ul>`/`<li>` HTML where appropriate, and `<dfn>` references with internal newlines normalized. No content changes.

---

## PR #1 — 2025-05-26 Atlas Edit Weekly Cycle Proposal
**Merged:** 2025-06-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Agent Role Delineation added** (A.1.14, new): New section delineating roles between Sky Core and Agents.
- **Known And Uncontentious Remedies added** (A.1.8.1, new subsection): Emergency Response System gains a pathway for uncontentious remedies that can bypass the full emergency process.

### Context
First Atlas PR in the repository — a massive weekly edit primarily restructuring A.2 (Allocation System, Ecosystem Accords) and A.3 (risk framework). A.1 changes are relatively minor. See A.2--support and A.3--stability changelogs for the bulk of this PR's impact.

---

## PR #3 — New AD added: Max Staking Yield
**Merged:** 2025-06-03 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New AD recognized**: Max Staking Yield (recognition address `0x9746bDaB7ab2609247332324400cc1fbE887095C`, forum: max-staking-yield-ad-recognition-submission/26462).

---
