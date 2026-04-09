# Governance Scope — Change History

Atlas path: `A.1` — The Governance Scope

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

## PR #133 — 2025-12-01 AEW Proposal
**Merged:** 2025-12-04 | **+1987/-171 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.1.5.4.4.2.1.1` - Triggering Threshold [Core]
- **Deleted** `A.1.5.4.4.3.0.3.1` - Collateral - Element Annotation [Annotation]
- **Deleted** `A.1.5.20.0.4.2` - Useful - Whistleblower Evidence Must Have Material Impact [Action Tenet]
- **Deleted** `A.1.5.20` - Whistleblower Bounty [Section]
- **Deleted** `A.1.5.17` - Whistleblower Bounty [Section]
- **Deleted** `A.1.5.4.4.3.0.3.4` - Whistleblower Bounty - Element Annotation [Annotation]
- **Deleted** `A.1.5.17.0.4.2` - Useful - Whistleblower Evidence Must Have Material Impact [Action Tenet]
- **Deleted** `A.1.5.4.4.2.0.3.1` - AD Buffer And Loss Of Budget - Element Annotation [Annotation]
- **Deleted** `A.1.5.17.0.4.1` - Responsibly Provided - Whistleblower Evidence Of Misalignment Must Be Secured Ethically [Action Tenet]
- **Deleted** `A.1.5.20.0.4.1` - Responsibly Provided - Whistleblower Evidence Of Operational Security Breach Must Be Secured Ethically [Action Tenet]
- **Deleted** `A.1.5.4.4.3.0.3.3` - Operational Security Or Privacy - Element Annotation [Annotation]
- **Deleted** `A.1.5.4.4.3.0.3.2` - One Month's Budget Allocation - Element Annotation [Annotation]
- **Modified** `A.1.5.4.4.3` - Deduction Of Penalties From AD Buffer [Core]
- **Modified** `A.1.5.4.4.2.1` - Payout Limitations For ADs Triggering Atlas Edit Proposals [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #135 — fix typos
**Merged:** 2025-12-03 | **+2/-2 lines**

### Raw Changes (rewrite with /atlas-track)
- **Modified** `A.1.9.5.3.1.3.4` - Protego Eta Parameter Definition [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #139 — Fix delegate document numbering
**Merged:** 2025-12-08 | **+49/-49 lines**

### Raw Changes (rewrite with /atlas-track)
- **Modified** `A.1.5.4.1.1.2` - Budget For Level 1 Ranked Delegates [Core]
- **Modified** `A.1.5.4.1.2.2` - Budget For Level 2 Ranked Delegates [Core]
- **Modified** `A.1.5.4.4` - AD Buffer [Core]
- **Modified** `A.1.5.4` - Ranked Delegates [Section]
- **Modified** `A.1.5.9` - Facilitators Must Err On Side Of Caution [Section]
- **Modified** `A.1.5.4.5` - Short-Term Transitionary Measures [Core]
- **Modified** `A.1.5.4.1.1.1` - Number Of Level 1 Ranked Delegates [Core]
- **Modified** `A.1.5.4.3.3.1` - Signal Account Requirement [Core]
- **Modified** `A.1.5.4.4.2.1.1` - Triggering Threshold [Core]
- **Modified** `A.1.5.4.1.2` - Level 2 Ranked Delegates [Core]
- **Modified** `A.1.5.4.5.1` - Levels Of Ranked Delegates [Core]
- **Modified** `A.1.5.8.0.4.1` - Promptly Derecognized - Mandated Timeline For AD Derecognition For Operational Security Breach [Action Tenet]
- **Modified** `A.1.5.4.3.3` - Emergency Communications Requirement [Core]
- **Modified** `A.1.5.5` - Kickbacks Prohibited [Section]
- **Modified** `A.1.5.4.1.1.3.1` - Current Level 1 Ranked Delegates [Core]
- **Modified** `A.1.5.4.4.1.0.3.1` - One Month's Budget Allocation - Element Annotation [Annotation]
- **Modified** `A.1.5.4.4.3` - Deduction Of Penalties From AD Buffer [Core]
- **Modified** `A.1.5.4.3.1.0.3.1` - Proportional Linear Scale - Element Annotation [Annotation]
- **Modified** `A.1.5.4.3.2.0.3.1` - Proportional Linear Scale - Element Annotation [Annotation]
- **Modified** `A.1.5.4.4.1` - AD Monthly Compensation Cycle [Core]
- **Modified** `A.1.5.8` - Derecognition Required Where AD Operational Security Is Compromised [Section]
- **Modified** `A.1.5.4.1.2.3` - Selection Of Level 2 Ranked Delegates [Core]
- **Modified** `A.1.5.4.1.3.3.0.3.1` - Delegated Voting Power - Element Annotation [Annotation]
- **Modified** `A.1.5.4.3` - Budget Contingency [Core]
- **Modified** `A.1.5.4.1.3.1` - Number Of Level 3 Ranked Delegates [Core]
- **Modified** `A.1.5.6` - Swift Action Is Required From Facilitators To Redress AD Misalignment [Section]
- **Modified** `A.1.5.4.1.3` - Level 3 Ranked Delegates [Core]
- **Modified** `A.1.5.4.4.2.1` - Payout Limitations For ADs Triggering Atlas Edit Proposals [Core]
- **Modified** `A.1.5.4.3.1` - Voting-Activity Metrics [Core]
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

## PR #186 — 2026-02-16 AEW proposal
**Merged:** 2026-02-22 | **+2119/-158 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.1.5.2.1.1` - Excessive Abstention [Core]
- **Added** `A.1.5.6.1.3.0.6.1` - Aligned Delegate Breach Registry [Active Data]
- **Added** `A.1.5.6.1` - Graduated Response Framework [Core]
- **Added** `A.1.5.6.1.3` - Aligned Delegate Breach Record [Active Data Controller]
- **Added** `A.1.5.2.2` - Aligned Delegate Communication Responsibilities [Core]
- **Added** `A.1.5.1.4.1` - Heightened Accountability Standards During Probationary Period [Core]
- **Added** `A.1.5.6.0.3.1` - Act Swiftly - Element Annotation [Annotation]
- **Added** `A.1.5.6.1.2.0.3.1` - Good-Faith Criticism - Element Annotation [Annotation]
- **Added** `A.1.5.2` - Aligned Delegate Responsibilities [Section]
- **Added** `A.1.5.4.5` - Ranked Delegate Voting Communication Review Responsibility [Core]
- **Added** `A.1.5.6.0.3.2` - Credible Evidence - Element Annotation [Annotation]
- **Added** `A.1.5.1.4` - Probationary Period [Core]
- **Added** `A.1.4.9.5` - Core Facilitator Is Subject To Conflict Of Interest [Core]
- **Added** `A.1.5.2.1` - Aligned Delegate Voting Responsibilities [Core]
- **Added** `A.1.4.9.2.1` - Graduated Response Framework For Breaches By Aligned Delegates [Core]
- **Added** `A.1.5.6.1.2` - Tier 2 (Integrity) Breaches [Core]
- **Added** `A.1.5.6.2` - Voting Estoppel Rule [Core]
- **Added** `A.1.8.1.2.4` - Aligned Delegate Membership In Emergency Response Group [Core]
- **Added** `A.1.5.6.1.1` - Tier 1 (Procedural) Breaches [Core]
- **Deleted** `A.1.4.9.2.1.1` - Warning Notice [Core]
- **Deleted** `A.1.4.9.2.1.0.4.2` - Mild Slippery Slope Breaches - Evaluating Whether A Misaligned Act Is ‘Very Mild' [Action Tenet]
- **Deleted** `A.1.4.9.2.1.0.4.1` - Adjudication Guidelines to be applied to a second misaligned act or a first misaligned act that is not mild [Action Tenet]
- **Deleted** `A.1.4.9.2.1.0.4.3` - Mild Slippery Slope Breaches - Facilitators Required To Be Proactive Against Even Mild Misalignment [Action Tenet]
- **Deleted** `A.1.4.9.2.1.2` - Warning Recording [Active Data Controller]
- **Deleted** `A.1.4.9.2.1.2.0.6.1` - List of Formally Warned Alignment Conservers [Active Data]
- **Deleted** `A.1.4.9.2.1` - Warnings Appropriate For Mild Breach [Core]
- **Modified** `A.1.5.4.1.1.2` - Budget For Level 1 Ranked Delegates [Core]
- **Modified** `A.1.5.4.1.2.2` - Budget For Level 2 Ranked Delegates [Core]
- **Modified** `A.1.5.4.4` - AD Buffer [Core]
- **Modified** `A.1.5.4` - Ranked Delegates [Section]
- **Modified** `A.1.5.9` - Facilitators Must Err On Side Of Caution [Section]
- **Modified** `A.1.5.4.1.1.1` - Number Of Level 1 Ranked Delegates [Core]
- **Modified** `A.1.5.4.3.3.1` - Signal Account Requirement [Core]
- **Modified** `A.1.5.4.4.2.1.1` - Triggering Threshold [Core]
- **Modified** `A.1.5.4.1.2` - Level 2 Ranked Delegates [Core]
- **Modified** `A.1.5.8.0.4.1` - Promptly Derecognized - Mandated Timeline For AD Derecognition For Operational Security Breach [Action Tenet]
- **Modified** `A.1.5.4.3.3` - Emergency Communications Requirement [Core]
- **Modified** `A.1.5.5` - Kickbacks Prohibited [Section]
- **Modified** `A.1.5.4.1.1.3.1` - Current Level 1 Ranked Delegates [Core]
- **Modified** `A.1.5.4.4.1.0.3.1` - One Month's Budget Allocation - Element Annotation [Annotation]
- **Modified** `A.1.5.4.4.3` - Deduction Of Penalties From AD Buffer [Core]
- **Modified** `A.1.5.3` - In General [Section]
- **Modified** `A.1.5.4.3.1.0.3.1` - Proportional Linear Scale - Element Annotation [Annotation]
- **Modified** `A.1.5.4.3.2.0.3.1` - Proportional Linear Scale - Element Annotation [Annotation]
- **Modified** `A.1.5.1.5.0.6.1` - Current Aligned Delegates [Active Data]
- **Modified** `A.1.5.4.4.1` - AD Monthly Compensation Cycle [Core]
- **Modified** `A.1.5.1.5` - List Of Recognized Aligned Delegates [Active Data Controller]
- **Modified** `A.1.5.8` - Derecognition Required Where AD Operational Security Is Compromised [Section]
- **Modified** `A.1.5.4.1.2.3` - Selection Of Level 2 Ranked Delegates [Core]
- **Modified** `A.1.5.4.1.3.3.0.3.1` - Delegated Voting Power - Element Annotation [Annotation]
- **Modified** `A.1.5.4.3` - Budget Contingency [Core]
- **Modified** `A.1.5.4.1.3.1` - Number Of Level 3 Ranked Delegates [Core]
- **Modified** `A.1.5.6` - Swift Action Is Required From Facilitators To Redress AD Misalignment [Section]
- **Modified** `A.1.5.4.1.3` - Level 3 Ranked Delegates [Core]
- **Modified** `A.1.5.4.4.2.1` - Payout Limitations For ADs Triggering Atlas Edit Proposals [Core]
- **Modified** `A.1.5.3.0.3.1` - Delegated Voting Power - Element Annotation [Annotation]
- **Modified** `A.1.5.4.3.1` - Voting-Activity Metrics [Core]
- **Modified** `A.1.5.4.4.2` - AD Buffer And Loss Of Budget [Core]
- **Modified** `A.1.5.4.1.3.3` - Selection Of Level 3 Ranked Delegates [Core]
- **Modified** `A.1.5.6.0.4.1` - Facilitators’ Authority To Raise Formal Allegation [Action Tenet]
- **Modified** `A.1.5.4.1.3.2` - Budget For Level 3 Ranked Delegates [Core]
- **Modified** `A.1.5.7` - Mandate To Maintain High Level of Operational Security [Section]
- **Modified** `A.1.5.4.3.2.0.3.2` - Voting-Communication Metrics - Element Annotation [Annotation]
- **Modified** `A.1.5.4.1.1` - Level 1 Ranked Delegates [Core]
- **Modified** `A.1.5.10` - Emergency Contact Mechanism [Section]
- **Modified** `A.1.5.4.1.2.1` - Number Of Level 2 Ranked Delegates [Core]
- **Modified** `A.1.5.4.2` - Budget Accrual [Core]
- **Modified** `A.1.5.4.1.2.3.1` - Current Level 2 Ranked Delegates [Core]
- **Modified** `A.1.5.4.3.2` - Voting-Communication Metrics [Core]
- **Modified** `A.1.5.4.1` - Levels Of Ranked Delegates [Core]
- **Modified** `A.1.5.4.1.1.3` - Selection Of Level 1 Ranked Delegates [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---
