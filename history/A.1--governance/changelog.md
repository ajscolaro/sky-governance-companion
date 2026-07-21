# Governance Scope — Change History

Atlas path: `A.1` — The Governance Scope

---

## PR #277 — Atlas Edit Proposal — 2026-07-13
**Merged:** 2026-07-16 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core A.1.10.4.1.2.3.1 deleted: Freezer Multisigs** (UUID `d70d5580…5808`)
- **Core A.1.10.4.1.3.3.1 deleted: Freezer Multisigs** (UUID `199661f2…b00d`)
- **Core A.1.10.4.1.4.3.1 deleted: Freezer Multisigs** (UUID `022129be…6d62`)
- **Core A.1.10.4.1.2.3.1 deleted: Freezer Multisigs** (UUID `d70d5580…5808`)
- **Core A.1.10.4.1.3.3.1 deleted: Freezer Multisigs** (UUID `199661f2…b00d`)
- **Core A.1.10.4.1.4.3.1 deleted: Freezer Multisigs** (UUID `022129be…6d62`)
- **New: Vote Timeliness** (`A.1.6.2.1.2`, UUID `0589c64f…ae1e`): A vote counts toward an Aligned Delegate's voting participation only where the Aligned Delegate casts it within three (3) business days of the Executive Vote being posted to the voting portal.
- **Ethereum SkyLink Freezer Multisig** (`A.1.10.3.2.14`): `1` → `2.2`
- **Solana SkyLink Freezer Multisig** (`A.1.10.3.2.15`): `1` → `2.2`
- **Avalanche SkyLink Freezer Multisig** (`A.1.10.3.2.16`): `1` → `2.2`
- **Plasma SkyLink Freezer Multisig** (`A.1.10.3.2.17`): `1` → `2.2`
- **SparkLend Multisig Number Of Signers** (`A.1.10.4.1.1.2`): `2` → `3`
- **SparkLend Multisig Address** (`A.1.10.4.1.1.5`): address `0x44efFc473e81632B12486866AA1678edbb7BEeC3`

### Housekeeping
- `A.1.10.1.2` (Chainlog): `sky` → `skyeco`
- `A.1.10.2.3.2.2.2.1.6` (Creation Of Public Information Dashboard): `sky` → `skyeco`
- `A.1.10.2.4.11.1.2` (Governance Point Requests TechOps Services To Whitelist Spell Address): `in the Discord channel #techops-request` → `to TechOps Services via Slack`
- `A.1.10.2.4.12.2.11` (Using The Sky Forum For Spell Validation): `The use of Discord is not required during Spell verification, as it primarily serves as a platform for public communication between the Core Facilitator and members of the current Spell Team.` → ``
- `A.1.10.2.4.12.2.8` (Using Chainlog Smart Contract For Spell Validation): `sky` → `skyeco`
- `A.1.10.2.4.12.4.8` (Public Validation Status Reporting): `using the "#new-Spells" channel in the Sky Builder Discord Group. If the Core Facilitator may be acting maliciously, issues should be reported to Aligned Delegates and wider Sky Governance using the "#governance" channel in the Sky Builder Discord Group. In cases where this is not possible, posts made to` → `on`
- `A.1.10.4.1.1.1` (SparkLend Multisig Usage Standards): `` → `The Core Council must ensure that use of the multisig is generally aligned and specifically accords with the requirements defined herein.`
- `A.1.10.4.1.1.3` (SparkLend Multisig Current Signers): `The signers of the Ethereum SkyLink Freezer Multisig are two (2) addresses controlled by the Core Facilitator and three (3) addresses controlled by Core GovOps.` → ``
- `A.1.10.4.1.1.4` (SparkLend Multisig Signer Modifications): `The Core Council must ensure that use of` → `Any changes to`; `specifically accords with these requirements` → `treated as malicious. The Core Facilitator should consider preparing an expedited Executive Vote so that Sky Governance can vote on removing external security access from the multisig`
- `A.1.10.4.1.1` (Multisig Freeze Of SparkLend): added refs to `A.1.10.3.2.7`
- `A.1.10.4.1` (Spark Agent): `SkyLink Bridges` → `Spark Agent`
- `A.1.10.4.1.1` (Multisig Freeze Of SparkLend): removed refs to `A.1.10.3.2.7`
- `A.1.10.4.1` (Spark Agent): removed `###### A.1.10.4.2 - Spark Agent [Core]`
- `A.1.6.2.1` (Aligned Delegate Voting Responsibilities): added refs to `A.1.6.2.1.2`
- `A.1.6.4.3.1` (Voting-Activity Metrics): added refs to `A.1.6.2.1.2`
- `A.1.10.4.1.1.0.3.1` renumbered (UUID stable: `1844a8bf…17bb`)
- `A.1.10.4.1.1.1.0.3.1` renumbered (UUID stable: `d373ebcb…bf05`)
- `A.1.10.4.1.1.1.0.4.1` renumbered (UUID stable: `71898c9e…dd0c`)
- `sky` → `skyeco` across 3 docs.
- `money` → `com` across 3 docs.
- `1` → `2.2` across 4 docs.
- `Ethereum SkyLink Freezer` → `SparkLend` across 5 docs.

### Context
Adds a Vote Timeliness rule crediting AD voting participation only for votes cast within three business days of an Executive Vote being posted. SkyLink freezer-multisig provisions relocate to the new A.4.2.2 SkyLink Bridges section, the SparkLend multisig signer threshold rises 2→3, and Discord references shift to Slack/forum.

---

## PR #273 — Atlas Edit Proposal — 2026-07-06
**Merged:** 2026-07-10 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- `A.1.10.2.5.1.2.1.1` (Agent Spell Reviewer Checklist): `all Agents` → `a completed Agent Spell Reviewer Checklist`

### Context
Clarifies that the Agent Spell Reviewer requirement is met per-reviewer via a completed Agent Spell Reviewer Checklist rather than "all Agents"; per an AD validator, the change takes effect for the July 16, 2026 Executive Vote.

---

## PR #270 — Atlas Edit Proposal — 2026-06-29
**Merged:** 2026-07-03 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- `A.1.10.2.4.10.1` (Spell Crafter Performs Pre-Deployment Steps): added refs to `A.1.10.2.5.1.3.2.0.6.1`
- `A.1.10.2.4.10.10` (Spell Crafter Conducts Final Checks): added refs to `A.1.10.2.5.1.3.2.0.6.1`
- `A.1.10.2.4.10.2` (Spell Reviewers Review Pre-Deployment Steps): added refs to `A.1.10.2.5.1.3.2.0.6.1`
- `A.1.10.2.4.10.3` (Spell Crafter Conducts Pre-Deployment Setup And Checks): added refs to `A.1.10.2.5.1.3.2.0.6.1`
- `A.1.10.2.4.10.4` (Spell Crafter Deploys The Spell On Mainnet): added refs to `A.1.10.2.5.1.3.2.0.6.1`
- `A.1.10.2.4.10.5` (Spell Crafter Casts Spell On Newly Deployed Tenderly Testnet): added refs to `A.1.10.2.5.1.3.2.0.6.1`
- `A.1.10.2.4.10.7` (Spell Crafter Pushes Changes And Requests Review): added refs to `A.1.10.2.5.1.3.2.0.6.1`
- `A.1.10.2.4.10.8` (Spell Reviewers Review Pull Request): added refs to `A.1.10.2.5.1.3.2.0.6.1`
- `A.1.10.2.4.10.9` (Spell Crafter Hands Over Spell): added refs to `A.1.10.2.5.1.3.2.0.6.1`
- `A.1.10.2.4.7.1` (Spell Crafting Workflow): added refs to `A.1.10.2.5.1.3.2.0.6.1`
- `A.1.10.2.4.9.1` (Spell Reviewing Workflow): added refs to `A.1.10.2.5.1.3.2.0.6.1`
- `here:` → `in the Core Spell Crafter Mainnet Workflow, as specified in` across 8 docs.
- `https://github` → `A` across 11 docs.
- `com/sky` → `1.10.2.5.1.3.2.0.6.1` across 11 docs.
- `ecosystem/pe-checklists/blob/master/` → `Registered` across 10 docs.
- `/Spell-crafter-mainnet-workflow.md` → `Checklists` across 7 docs.
- `https://github.com/sky` → `93f5b36b` across 7 docs.
- `ecosystem/pe` → `06a7` across 7 docs.
- `checklists/blob/master/spell/spell` → `4282` across 7 docs.
- `crafter` → `9fd7` across 5 docs.
- `mainnet-workflow.md` → `14e0cbafd08e` across 5 docs.
- `https://github` → `93f5b36b-06a7-4282-9fd7-14e0cbafd08e)` across 4 docs.
- `here:` → `in the Core Spell Reviewer Mainnet Checklist, as specified in` across 3 docs.

### Context
Replaces external `github.com/sky-ecosystem/pe-checklists` links in the spell-crafting and spell-reviewing mainnet workflow docs with references to a newly registered in-Atlas checklist document (`A.1.10.2.5.1.3.2.0.6.1`), moving the checklist reference in-tree.

---

## PR #265 — Atlas Edit Proposal — 2026-06-22
**Merged:** 2026-06-29 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- `A.1.6.2.1` (Aligned Delegate Voting Responsibilities): `` → `Following the issuance of a Tier 1 (Procedural) breach for failure to meet this requirement, the Core Facilitator will not issue a further Tier 1 (Procedural) breach solely because the Aligned Delegate's participation rate over the past six (6) months remains below seventy-five percent (75%), provided that the Aligned Delegate has participated in at least seventy-five percent (75%) of the votes for which they were eligible after the most recent breach was issued. A further Tier 1 (Procedural) breach on this basis is issued only where the Aligned Delegate fails to meet the seventy-five percent (75%) participation requirement in the votes for which they were eligible after the most recent breach was issued. The Core Facilitator evaluates voting participation for this purpose on a monthly basis.`
- `Facilitators` → `Core Council` across 3 docs.

### Context
Adds a grace mechanism to Aligned Delegate voting responsibilities: after a Tier 1 (Procedural) breach, no further such breach is issued solely for a sub-75% six-month participation rate provided the AD has since participated in ≥75% of eligible votes, evaluated monthly by the Core Facilitator. Ratified by poll #1638 (9-0).

---

## PR #258 — Atlas Edit Proposal — 2026-06-15
**Merged:** 2026-06-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: Core Facilitator Final Inclusion Decision** (`A.1.10.2.4.3.1.3.1`, UUID `4cbe3ee7…e233`): Where consensus cannot be reached on whether to include an item in the Spell, the disagreement must be raised in the govops channel in Slack so that the Spell Teams, Core GovOps, the Core Facilitator, and the Protocol Security Workstream Le.
- **Ethereum SkyLink Freezer Multisig Required Number Of Signers** (`A.1.10.4.1.1.2`): `4` → `5`
- **Ethereum SkyLink Freezer Multisig Signers** (`A.1.10.4.1.1.3`): `2` → `3`
- **Ethereum SkyLink Freezer Multisig Modification** (`A.1.10.4.1.1.5`): `4` → `5`

### Housekeeping
- `A.1.10.2.3.2.2.1.2` (Prime Spell Security Guidelines): `Discord` → `Slack`
- `A.1.10.2.3.2.2.3.2.2` (Prime Agent Publishes Spell Actions On Sky Forum): added refs to `A.1.10.2.5.2.1`
- `A.1.10.2.3.2.2.3.3.6` (Prime Agent Delivers Prime Spell Payload): `Discord channel` → `channel in Slack`
- `A.1.10.2.3.3.2.2` (Core Facilitator Confirms Whether Requested Item Is Novel): `Discord` → `the govops channel`
- `A.1.10.2.4.12.4.7` (Private Validation Status Reporting): `Discord` → `Slack`
- `A.1.10.2.4.13.6.1` (Spell Crafter Initiates Retrospective): removed ``#`
- `A.1.10.2.4.3.1.2` (Content Review): `Discord` → `Slack`
- `A.1.10.2.4.3.1.3` (Obtain Consensus On Content): `` → `Where consensus cannot be reached, the procedure specified in [A.1.10.2.4.3.1.3.1 - Core Facilitator Final Inclusion Decision](4cbe3ee7-a64f-4e44-8cf5-25a09a87e233) applies.`
- `A.1.10.2.4.3.1` (GovOps Meeting): removed `on Discord`
- `A.1.10.2.4.4.2` (Governance Point Must Correct Discrepancies): `Discord` → `Slack`
- `A.1.10.2.4.6` (Governance Point Finalizes Executive Sheet Week 1 Friday (Step 6)): removed `#`
- `A.1.10.2.4.8.3.8` (Core Facilitator Must Notify Spell Team Of Changes): removed `Discord in`
- `A.1.10.2.4.8.5.4` (Core Facilitator Shares Link And Hash Of Executive Document With Technical Point): `Discord` → `Slack`
- `A.1.10.2.4.8.5.5` (Core Facilitator Must Communicate Executive Document With Media Liaison): removed `This is done via the #twitter-requests channel in the Growth Core Unit Discord.`
- `A.1.10.2.4.9.2.6` (Spell Reviewers Must Raise Comments When They Find Issues): `Discord` → `Slack`
- `Discord` → `Slack` across 6 docs.

### Context
Migrates the spell-process governance comms from Discord to Slack and tightens the Ethereum SkyLink Freezer Multisig quorum (4→5 signers). Also adds a Core Facilitator tiebreak procedure (`A.1.10.2.4.3.1.3.1`) for unresolved disputes over Spell inclusion. Ratified by poll #1637 (10-0).

---

## PR #257 — Derecognize Kuzmich, add new breaches
**Merged:** 2026-06-11 | **Type:** Active Data update (Designated Controller)

### Material Changes
- **Registry row added** in Derecognized Alignment Conservers (`A.1.5.10.2.0.6.1`): | 2026-06-11 | AD | Kuzmich | - | [https://forum.skyeco.com/t/ad-recognition-submission/26743/54](https://forum.skyeco.com/t/ad-recognition-submission/26743/54) |

### Context
Records Kuzmich's AD derecognition (moved to the Derecognized list) alongside new breach entries; the delegate tables were also reformatted to the compact style in the same Direct Edit.

---

## PR #255 — Atlas Edit Proposal — 2026-06-08
**Merged:** 2026-06-11 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Action Tenet A.1.11.2.3.0.4.1 deleted: Unanimity Is Not Required To Block Proposal For Misalignment** (UUID `824e78be…7665`)
- **New: Audit Process** (`A.1.10.2.7`, UUID `a8334e19…c8e6`): The documents herein define the audit process for smart contracts and deployment scripts that require independent security review before inclusion in a Spell or deployment within the Sky Ecosystem.
  - **Audit Triggers** (`A.1.10.2.7.1`): An audit is required before new smart contract code is introduced to the Sky Ecosystem, including.
  - **Deployment And Initialization Script Structure** (`A.1.10.2.7.1.1.1`): Deployment logic and initialization logic must be structured as follows.
  - **General Requirements** (`A.1.10.2.7.1.1.2.1`): The following requirements apply to all deployment and initialization scripts.
  - **Deployment Script Requirements** (`A.1.10.2.7.1.1.2.2`): Deployment scripts must satisfy the following requirements.
  - **Initialization Script Requirements** (`A.1.10.2.7.1.1.2.3`): Initialization scripts must satisfy the following requirements.
  - **Audit Request And Intake** (`A.1.10.2.7.2`): The team responsible for the code to be audited fills in a standardized audit intake form containing, at minimum.
  - **Code Review Requirement** (`A.1.10.2.7.2.1`): The commit hash submitted for audit must correspond to a Pull Request that has been reviewed and approved by at least one (1) member of the team responsible for the code who is not an author of the Pull Request.
  - **Audit Execution And Report Delivery** (`A.1.10.2.7.3`): The auditor performs the audit against the scope and commit hash specified in the audit request.
  - **Report Review And Acceptance** (`A.1.10.2.7.4`): Upon delivery of the interim audit report, the team responsible for the audited code reviews the report and confirms that the audited scope and commit hash match the audit request.
  - **Findings Remediation** (`A.1.10.2.7.5`): If the interim audit report contains findings, the team responsible for the audited code must address each finding based on its severity.
  - **Audit Recordkeeping** (`A.1.10.2.7.6`): The Forum post for the associated Spell or deployment must include a link to each applicable final audit report, the audited commit hash, and confirmation that the deployed code matches the audited commit, as specified in [A.1.10.2.3.2.1.2.

### Housekeeping
- `A.1.10.2.3.2.1.1` (Preparatory Phase for Module Deployment): added refs to `A.1.10.2.7`
- `A.1.10.2.3.2.1.2.1.2.1` (Requirements For Forum Post): added refs to `A.1.10.2.7.6`
- `A.1.10.2.3.2.2.2.1.1` (Forum Post By Prime Agent): added refs to `A.1.10.2.7`
- `A.1.10.2.3.2.2.3.1.1` (Prime Agent Submits Prime Spell Form): added refs to `A.1.10.2.7`
- `A.1.10.2.3.3.2.3` (Core Spell Teams Conduct A Technical Feasibility Analysis And Develop An Implementation Proposal): added refs to `A.1.10.2.7`
- `A.1.10.2.4.12.4.5` (Primary Reporting Counterparty): `Facilitators, not a single` → ``
- `A.1.10.2.4.12.4.6` (Secondary Reporting Counterparty): `Facilitators are` → `Facilitator is`; `, even if all Core Facilitators are compromised or acting maliciously` → ``
- `A.1.10.2.4.12.4.7` (Private Validation Status Reporting): `a group of Core Facilitators` → `multiple trusted parties`; `Core Facilitator` → `actor`
- `A.1.12.2.1.7.1` (Procedure For Blocking AEP For Misalignment): `Unanimity among the Core Facilitators is not required to block an AEP for misalignment.` → ``

### Context
Adds a formal Audit Process framework (`A.1.10.2.7`) mandating independent security review of smart-contract and deployment-script code before inclusion in a Spell, with structured intake, code-review, remediation, and recordkeeping requirements. Removes the now-redundant "unanimity not required to block" clauses. Ratified by poll #1636 (9-0).

---

## PR #253 — Atlas Edit Proposal — 2026-06-01
**Merged:** 2026-06-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core A.1.5.5.1 deleted: Temporary Exception for Facilitator “Ecosystem”** (UUID `6aa88317…c767`)
- **Core A.1.5.7.1 deleted: Exemption From Facilitator Anonymity Requirement** (UUID `cb2ae821…c5b5`)
- **Atlas Edit Proposal Drafting And Submission** (`A.1.10.2.3.2.2.3.2.4`): `5` → `6`
- **Prime Spell Process Breakdown** (`A.1.10.2.3.2.2.3`): `5` → `6`; `5` → `6`
- **Root Edit Process** (`A.1.14.2.7.1`): `5` → `6`
- **Agent Role Delineation** (`A.1.14.3.4`): `9` → `10`
- **Initiation Of Agent Termination Process** (`A.1.14.5.1`): `5` → `6`

### Housekeeping
- `A.1.10.2.3.2.2.2.1.2` (Specification Of Testing Parameters By Core Council Risk Advisor): removed `Ratio`
- `A.1.10.2.3.2.2.2.1.8` (Completion Of Full Risk Assessment): removed `Ratio`
- `5` → `6` across 4 docs.
- `9` → `10` across 1 doc.

### Context
Removes two obsolete exemptions tied to the retired Facilitator "Ecosystem" role, defunct since the scope-facilitator structure gave way to the Agent framework; remaining changes are footnote-reference renumbering. Poll #1635 passed 11–0.

---

## PR #251 — Atlas Edit Proposal — 2026-05-25
**Merged:** 2026-05-29 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: Executive Process Liaison Delivers Items To Core Council Tracker** (`A.1.10.2.3.2.2.3.1.2.1`, UUID `e55cfedb…4527`): The Executive Process Liaison reviews the submitted Prime Spell Form for completeness and clarity, and discusses possible Prime Spell content and potential blockers with the Prime Agent.
- **New: Core Council Risk Advisor Conducts Pre-Risk Review** (`A.1.10.2.3.2.2.3.1.2.2`, UUID `6bde7e9e…540b`): The `A.1.8.1.1` conducts a pre-risk review of the proposed Prime Spell content.
- **New: Core Spell Checklists** (`A.1.10.2.5.1.1`, UUID `e3c56b04…6ac8`): The documents herein define Core Spell Checklists.
  - **Core Spell Crafter Checklist** (`A.1.10.2.5.1.1.1.1`): The Core Spell Crafter Checklist defines standardized steps for Spell Crafters.
  - **Core Spell Reviewer Checklist** (`A.1.10.2.5.1.1.1.2`): The Core Spell Reviewer Checklist defines the mandatory steps for internal and external Spell Reviewers.
  - **Module Onboarding Checklists** (`A.1.10.2.5.1.1.1.3`): Module Onboarding Checklists define use-case specific steps that must be followed when a Core Spell includes the onboarding of a new module.
  - **Core Spell Checklist Update Process** (`A.1.10.2.5.1.1.2`): Updates to Core Spell Checklists are submitted as Pull Requests to the Spell Checklists repository (https://github.com/sky-ecosystem/pe-checklists/tree/master/spell).
- **New: Agent Spell Checklists** (`A.1.10.2.5.1.2`, UUID `21eb7269…7aff`): The documents herein define Agent Spell Checklists.
  - **Agent Spell Reviewer Checklist** (`A.1.10.2.5.1.2.1.1`): The Agent Spell Reviewer Checklist defines standardized steps for Agent Spell Reviewers.
  - **Agent Spell Checklist Update Process** (`A.1.10.2.5.1.2.2`): Agent Spell Crafters and Reviewers, including external auditors, are encouraged to extend and improve Agent Spell Checklists as improvements are identified during Spell crafting.
- **New: Spell Checklists Registry** (`A.1.10.2.5.1.3`, UUID `13e783a5…717a`): All Spell Checklists must be recorded in the Spell Checklists Registry at `A.1.10.2.5.1.3.2.0.6.1`.
  - **Spell Checklist Registration Requirements** (`A.1.10.2.5.1.3.1`): Each entry in the Spell Checklists Registry must contain the following information.
  - **List Of Registered Spell Checklists** (`A.1.10.2.5.1.3.2`): The list of registered Spell Checklists is defined as Active Data in `A.1.10.2.5.1.3.2.0.6.1`.
  - **Registered Spell Checklists** (`A.1.10.2.5.1.3.2.0.6.1`): The registered Spell Checklists are.
- **New: Technical Scope Template** (`A.1.10.2.5.2.1`, UUID `b9ba6658…a450`): The Technical Scope Template is a standardized template for announcing any infrastructure changes, whether on-chain or off-chain.
  - **Technical Scope Template Submission Requirements** (`A.1.10.2.5.2.1.1`): The completed Technical Scope Template must be published as a Forum post on the Sky Forum, providing enough technical detail for an independent external team to review the proposed changes without requiring additional context.
  - **Technical Scope Template Update Process** (`A.1.10.2.5.2.1.2`): The Technical Scope Template is maintained by Core GovOps.
- **New: Deployment Checklist** (`A.1.10.2.5.2.2`, UUID `2ac3532b…0fe7`): The Deployment Checklist defines standardized steps for contract deployments, covering deployer hygiene, foundry setup, test deployments, and verification.
  - **Deployment Checklist Submission Requirements** (`A.1.10.2.5.2.2.1`): The Deployment Checklist must be completed for every contract deployment.
  - **Deployment Checklist Update Process** (`A.1.10.2.5.2.2.2`): The Deployment Checklist is maintained by Core GovOps.
- **New: Voting Process For Executive Votes** (`A.1.10.2.6`, UUID `3aa5bc98…2366`): The subdocuments herein provide a high-level summary of the voting process for Executive Votes within the Sky Protocol.
  - **Voting Requirements** (`A.1.10.2.6.1`): Participation in Executive Votes requires access to SKY for voting, the governance token of the Sky Protocol, whether through direct ownership or delegated authority.
  - **Voting Validation** (`A.1.10.2.6.2`): Once an Executive Vote is live on the Voting Portal, it enters the Ecosystem Spell Validation Window, a critical period for community review.

### Housekeeping
- `A.1.10.2.3.2.2.3.1.2` (Delivery And Pre-Risk Review): `Executive Process Liaison Delivers Items To Core Council Tracker` → `Delivery And Pre-Risk Review`; `` → `and the Core Council Risk Advisor conducts a pre-risk review of the items submitted on Monday. Both must be completed`
- `A.1.10.2.3.2.2.3.1.3` (Strategic Team Approves Spell Scope): `Core Council Risk Advisor Conducts Pre-Risk Review` → `Strategic Team Approves Spell Scope`; `the Core Council Tracker,` → `be advanced through`
- `A.1.10.2.3.2.2.3.1.4` (Communication Of Approved Scope): `Sky Ecosystem's broader objectives` → `Core Council Risk Advisor`
- `A.1.10.2.3.2.2.3.1.4` (Communication Of Approved Scope): `Following the Strategic Team's approval as specified in [A.1.10.2.3.2.2.3.1.4 - Strategic Team Approves Spell Scope](05e33459-9ee6-430c-af72-13db2004c505), the Executive Process Liaison should communicate the approved scope to the Prime Agent and the Core Council Risk Advisor.` → ``
- `A.1.10.2.5.1` (Spell Checklists): removed refs to `A.1.10.2.2.4`
- `A.1.10.2.5.2` (Operational Reference Materials): removed refs to `A.1.10.2.4.12`
- `A.1.10.2.5` (Checklists And Reference Materials): `Voting Process For Executive Votes` → `Checklists And Reference Materials`
- `A.1.2.2.1.0.4.1` (Determine How They Are Modified - Immutable Documents Can Be Amended In The Transition To Endgame): removed `[**`
- `A.1.3.2.1.1` (Designated Synome Editor): `Labs` → `Tech`
- `A.1.5.5.0.4.1.1.1.var1` (Alternating Between Two Roles In Separate Time Intervals - var. 1): added `A.1.5.5.0.4.3 -`
- `A.1.10.2.6.3` renumbered (UUID stable: `9b43b664…d10e`)
- `A.1.10.2.6.4` renumbered (UUID stable: `9c5cae66…5623`)

### Context
Formalizes the Core Council spell-crafting pipeline: standardized Core/Agent Spell Checklists (maintained in the pe-checklists repo), a public Technical Scope Template and Deployment Checklist requirement for infrastructure changes, and a high-level Executive Vote voting process section. The Delivery/Pre-Risk Review steps were restructured so delivery and the Risk Advisor pre-risk review must both complete before scope advances.

---

## PR #246 — Atlas Edit Proposal — 2026-05-18
**Merged:** 2026-05-21 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: Executive Process Liaison** (`A.1.10.2.1.13`, UUID `abd8ac0d…eac5`): The Executive Process Liaison is the liaison between each Prime Agent and Sky Core in the Prime Spell Process.
- **New: Strategic Team** (`A.1.10.2.1.14`, UUID `f5decc3b…8916`): The Strategic Team is the actor responsible for reviewing submitted items and approving the scope of Prime Agent content advancing through the Prime Spell Process.
- **New: Prime Agents** (`A.1.10.2.2.5`, UUID `1d5adab9…dd95`): Prime Agents (see `A.0.1.1.42`) participate in the Executive Process by submitting their spell items for inclusion in the Executive Vote.
- **Alternating Between Two Roles In Separate Time Intervals** (`A.1.5.5.0.4.1.1.1`): `- A10 - Alignment Conservers - Accountability And Misalignment Handling` → `.10`
- **Alternating Between Two Roles In Separate Time Intervals - var. 1** (`A.1.5.5.0.4.1.1.1.var1`): `- A10 - Alignment Conservers - Accountability And Misalignment Handling` → `.10`
- **On-Call Or Stand-By Role** (`A.1.5.5.0.4.1.1.2`): `- A10 - Alignment Conservers - Accountability And Misalignment Handling` → `.10`
- **On-Call Or Standby Role - var. 1** (`A.1.5.5.0.4.1.1.2.var1`): `- A10 - Alignment Conservers - Accountability And Misalignment Handling` → `.10`
- **Resignation Notice Not Received - var. 1** (`A.1.5.5.0.4.1.1.3.var1`): `- A10 - Alignment Conservers - Accountability And Misalignment Handling` → `.10`
- **Should Ban Against Occupying Two Ecosystem Roles Apply to All Sky Stakeholder Roles?** (`NR-2`): `- A5 - Alignment Conservers - Powers And Constraints` → `.5`

### Housekeeping
- `A.1.10.2.2` (Roles in the Executive Process): `are categorized into four` → `include the following`
- `A.1.10.4.1.4.3.1.1.3` (Plasma SkyLink Freezer Multisig Signers): `Launch Agent 6` → `Osero`
- `A.1.10.4.1.4.3.1.1.5` (Plasma SkyLink Freezer Multisig Modification): `Launch Agent 6` → `Osero`
- `A.1.6.4.4.2.1.1.0.3.1` (One Month's Budget Allocation - Element Annotation): `’` → `'`
- `Launch Agent 6` → `Osero` across 2 docs.
- `- A10 - Alignment Conservers - Accountability And Misalignment Handling` → `.10` across 5 docs.
- `’` → `'` across 1 doc.

### Context
Formalizes two new roles in the Prime Spell Process: the Executive Process Liaison (each Prime Agent's interface to Sky Core) and the Strategic Team (approves the scope of Prime Agent content advancing through the Executive Vote). Ratified by Poll #1633 (10-0, non-voters: axislegati, excel, opex).

---

## PR #244 — Edit breach registry with new entries
**Merged:** 2026-05-15 | **Type:** Active Data update (Designated Controller)

### Material Changes
- **Registry row added** in Aligned Delegate Breach Registry (`A.1.6.6.1.3.0.6.1`): | 2026-05-15 | MaxStakingYield | 1           | [Core Facilitator Post](https://forum.skyeco.com/t/max-staking-yield-ad-recognition-submission/26462/80) |

---

## PR #242 — Atlas Edit Proposal — 2026-05-11
**Merged:** 2026-05-15 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Annotation A.1.10.1.4.1.0.3.1 deleted: Current Spell Team - Element Annotation** (UUID `2946ed2d…5f56`)
- **Annotation A.1.10.1.4.2.0.3.1 deleted: Current Spell Team - Element Annotation** (UUID `5e035410…d0e4`)
- **Annotation A.1.10.1.4.3.0.3.1 deleted: Current Spell Team - Element Annotation** (UUID `95b3197a…8e34`)
- **Core A.1.9.2.1.8 deleted: Ecosystem Spell Validation** (UUID `e2bc30b0…1d65`)
- **Core A.1.9.2.2.1 deleted: Governance Point And Governance Backup** (UUID `b8d55094…5b26`)
- **Core A.1.9.2.3.2.1.2 deleted: Forum Post And Deployment Of Module** (UUID `8dc369b7…fa89`)
- **Core A.1.9.2.3.2.1.3.1 deleted: Governance Point Includes Module Deployment In The Executive Sheet** (UUID `d2a2b598…fa9d`)
- **Core A.1.9.2.3.2.1.3.2 deleted: Confirmation Of Module Deployment In The Executive Sheet** (UUID `10ccad57…72f9`)
- **Core A.1.9.2.3.2.1.3 deleted: Populating Content Regarding Module Deployment In Executive Votes** (UUID `5e125907…4179`)
- **Core A.1.9.2.3.2.1.4 deleted: Populating Content Regarding Module Deployment In Executive Document** (UUID `fb98f4b8…c42e`)
- **Core A.1.9.2.3.2.2.1.4.1.3 deleted: Core Facilitator Records Prime Spell Security Incident Report In Prime Spell Security Incident Registry** (UUID `0da6c412…2c62`)
- **Core A.1.9.2.4.12.4.8 deleted: Public Validation Status Reporting** (UUID `2a14eed2…9e59`)
- **Core A.1.9.2.4.13.4 deleted: Casting And Execution Of Approved Spell** (UUID `a900623d…c139`)
- **Core A.1.9.2.4.3.1.4 deleted: Confirming Values Of Recurring Items** (UUID `d79509f0…9482`)
- **Core A.1.9.2.4.7.2.1 deleted: Previous Spell Code Cleanup** (UUID `3889281f…7ef8`)
- **Core A.1.9.2.4.7.3.5 deleted: Resolving the Issue and Following Up** (UUID `8b86845a…8a23`)
- **Core A.1.9.4.1.2.3.1 deleted: Freezer Multisigs** (UUID `d70d5580…5808`)
- **Core A.1.9.4.1.3.3.1 deleted: Freezer Multisigs** (UUID `199661f2…b00d`)
- **Core A.1.9.4.1.4.3.1 deleted: Freezer Multisigs** (UUID `022129be…6d62`)
- **Core A.1.9.5.2.3.2.1 deleted: Requirement To Validate Authenticity Of Standby Spell** (UUID `82393e1d…f2e7`)
- **Core A.1.9.5.2.3.3.2 deleted: Misalignment To Vote For Unvalidated Standby Spell** (UUID `75cdffe9…4fbe`)
- **Core A.1.9.5.3.1.3.6 deleted: Determining Protego Parameters** (UUID `49997c91…259b`)
- **Core A.1.9.5.3.2.2.1 deleted: Requirement To Validate Authenticity Of Emergency Drop Spell** (UUID `44b9503d…eba2`)
- **Core A.1.9.5.3.2.3.2 deleted: Misalignment To Vote For Unvalidated Emergency Drop Spell** (UUID `fc62902d…8c19`)
- **Annotation A.1.10.1.4.1.0.3.1 deleted: Current Spell Team - Element Annotation** (UUID `2946ed2d…5f56`)
- **Annotation A.1.10.1.4.2.0.3.1 deleted: Current Spell Team - Element Annotation** (UUID `5e035410…d0e4`)
- **Annotation A.1.10.1.4.3.0.3.1 deleted: Current Spell Team - Element Annotation** (UUID `95b3197a…8e34`)
- **Core A.1.13.1.5.1 deleted: Sky Core Facilitator Review** (UUID `81e59b78…c021`)
- **Core A.1.13.1.5.2 deleted: Sky Core Facilitator Determination** (UUID `5ab97ecc…f951`)
- **Core A.1.13.1.5.3 deleted: Intent to Suspend Notice Process** (UUID `011846e4…625c`)
- **Core A.1.13.1.5.4.2 deleted: Emergency Suspension Review Process** (UUID `584801d6…0c09`)
- **Core A.1.13.1.5 deleted: Conflict Protocol Between Agent Artifacts And The Sky Core Atlas** (UUID `ecb0b102…fa2b`)
- **Core A.1.13.5.1 deleted: Initiation Of Agent Termination Process** (UUID `023540ad…ea77`)
- **Core A.1.13.5.3 deleted: End Of Agent Termination Process** (UUID `52fb64c4…93fc`)
- **Core A.1.13.5.4 deleted: Agent Termination Process Dispute Resolution** (UUID `065c176d…3cf4`)
- **Core A.1.13.1.5.1 deleted: Sky Core Facilitator Review** (UUID `81e59b78…c021`)
- **Core A.1.13.1.5.2 deleted: Sky Core Facilitator Determination** (UUID `5ab97ecc…f951`)
- **Core A.1.13.1.5.3 deleted: Intent to Suspend Notice Process** (UUID `011846e4…625c`)
- **Core A.1.13.1.5.4.2 deleted: Emergency Suspension Review Process** (UUID `584801d6…0c09`)
- **Core A.1.13.1.5 deleted: Conflict Protocol Between Agent Artifacts And The Sky Core Atlas** (UUID `ecb0b102…fa2b`)
- **Core A.1.13.5.1 deleted: Initiation Of Agent Termination Process** (UUID `023540ad…ea77`)
- **Core A.1.13.5.3 deleted: End Of Agent Termination Process** (UUID `52fb64c4…93fc`)
- **Core A.1.13.5.4 deleted: Agent Termination Process Dispute Resolution** (UUID `065c176d…3cf4`)
- **Core A.1.9.2.1.8 deleted: Ecosystem Spell Validation** (UUID `e2bc30b0…1d65`)
- **Core A.1.9.2.2.1 deleted: Governance Point And Governance Backup** (UUID `b8d55094…5b26`)
- **Core A.1.9.2.3.2.1.2 deleted: Forum Post And Deployment Of Module** (UUID `8dc369b7…fa89`)
- **Core A.1.9.2.3.2.1.3.1 deleted: Governance Point Includes Module Deployment In The Executive Sheet** (UUID `d2a2b598…fa9d`)
- **Core A.1.9.2.3.2.1.3.2 deleted: Confirmation Of Module Deployment In The Executive Sheet** (UUID `10ccad57…72f9`)
- **Core A.1.9.2.3.2.1.3 deleted: Populating Content Regarding Module Deployment In Executive Votes** (UUID `5e125907…4179`)
- **Core A.1.9.2.3.2.1.4 deleted: Populating Content Regarding Module Deployment In Executive Document** (UUID `fb98f4b8…c42e`)
- **Core A.1.9.2.3.2.2.1.4.1.3 deleted: Core Facilitator Records Prime Spell Security Incident Report In Prime Spell Security Incident Registry** (UUID `0da6c412…2c62`)
- **Core A.1.9.2.4.12.4.8 deleted: Public Validation Status Reporting** (UUID `2a14eed2…9e59`)
- **Core A.1.9.2.4.13.4 deleted: Casting And Execution Of Approved Spell** (UUID `a900623d…c139`)
- **Core A.1.9.2.4.3.1.4 deleted: Confirming Values Of Recurring Items** (UUID `d79509f0…9482`)
- **Core A.1.9.2.4.7.2.1 deleted: Previous Spell Code Cleanup** (UUID `3889281f…7ef8`)
- **Core A.1.9.2.4.7.3.5 deleted: Resolving the Issue and Following Up** (UUID `8b86845a…8a23`)
- **Core A.1.9.4.1.2.3.1 deleted: Freezer Multisigs** (UUID `d70d5580…5808`)
- **Core A.1.9.4.1.3.3.1 deleted: Freezer Multisigs** (UUID `199661f2…b00d`)
- **Core A.1.9.4.1.4.3.1 deleted: Freezer Multisigs** (UUID `022129be…6d62`)
- **Core A.1.9.5.2.3.2.1 deleted: Requirement To Validate Authenticity Of Standby Spell** (UUID `82393e1d…f2e7`)
- **Core A.1.9.5.2.3.3.2 deleted: Misalignment To Vote For Unvalidated Standby Spell** (UUID `75cdffe9…4fbe`)
- **Core A.1.9.5.3.1.3.6 deleted: Determining Protego Parameters** (UUID `49997c91…259b`)
- **Core A.1.9.5.3.2.2.1 deleted: Requirement To Validate Authenticity Of Emergency Drop Spell** (UUID `44b9503d…eba2`)
- **Core A.1.9.5.3.2.3.2 deleted: Misalignment To Vote For Unvalidated Emergency Drop Spell** (UUID `fc62902d…8c19`)
- **New: Prime Spell Process Breakdown** (`A.1.10.2.3.2.2.3`, UUID `a67d672a…f152`): The documents herein define the Prime Spell Process, the end-to-end procedure through which Prime Agents bring proposed actions through governance and into Sky Core Spells for on-chain execution.
  - **Step 1: Propose And Prioritize (Week 0)** (`A.1.10.2.3.2.2.3.1`): During week 0 of the Prime Spell Process, the Prime Agent's proposed Prime Spell content for the upcoming Executive Vote cycle is submitted, prioritized, and approved, as specified in the subdocuments herein.
  - **Prime Agent Submits Prime Spell Form** (`A.1.10.2.3.2.2.3.1.1`): The Prime Agent submits a Prime Spell Form to the Executive Process Liaison by Monday, 16:00 UTC of week 0.
  - **Executive Process Liaison Delivers Items To Core Council Tracker** (`A.1.10.2.3.2.2.3.1.2`): The Executive Process Liaison reviews the submitted Prime Spell Form for completeness and clarity, and discusses possible Prime Spell content and potential blockers with the Prime Agent.
  - **Core Council Risk Advisor Conducts Pre-Risk Review** (`A.1.10.2.3.2.2.3.1.3`): After the items are delivered to the Core Council Tracker, the `A.1.8.1.1` conducts a pre-risk review of the proposed Prime Spell content.
  - **Strategic Team Approves Spell Scope** (`A.1.10.2.3.2.2.3.1.4`): The Strategic Team reviews the items and approves the scope of Prime Agent content to be advanced through the Prime Spell Process for the upcoming Executive Vote cycle.
  - **Communication Of Approved Scope** (`A.1.10.2.3.2.2.3.1.5`): Following the Strategic Team's approval as specified in `A.1.10.2.3.2.2.3.1.4`, the Executive Process Liaison should communicate the approved scope to the Prime Age.
  - **Step 2: Finalize Scope (Week 1)** (`A.1.10.2.3.2.2.3.2`): During week 1 of the Prime Spell Process, the scope of approved Prime Spell content is finalized through Forum publication, risk review, and Atlas Edit Proposal submission, as specified in the subdocuments herein.
  - **Pre-Publication Review Of Forum Posts** (`A.1.10.2.3.2.2.3.2.1`): Prior to publication of Forum posts as specified in `A.1.10.2.3.2.2.3.2.2`, the Prime Agent must complete an internal review of the draft posts by at l.
  - **Prime Agent Publishes Spell Actions On Sky Forum** (`A.1.10.2.3.2.2.3.2.2`): Each proposed Prime Spell action must be included in a Forum post on the Sky Forum.
  - **Risk Assessment Review** (`A.1.10.2.3.2.2.3.2.3`): The items included in the Prime Agent's Forum posts must undergo a financial risk assessment.
  - **Atlas Edit Proposal Drafting And Submission** (`A.1.10.2.3.2.2.3.2.4`): The Edit Proposal codifying the Prime Spell content for the cycle is drafted and submitted.
  - **Step 3: Governance (Week 2)** (`A.1.10.2.3.2.2.3.3`): During week 2 of the Prime Spell Process, the Edit Proposal is voted on, the Prime Spell payload is reviewed and delivered, and approved content is ratified into the Atlas or applicable Agent Artifact, as specified in the subdocuments herei.
  - **Prime Agent Delivers Signed-Off Prime Spell For Review** (`A.1.10.2.3.2.2.3.3.1`): By Monday, 08:00 UTC of week 2, the Prime Agent must deliver a signed-off Prime Spell Pull Request ready for external review.
  - **Governance Vote** (`A.1.10.2.3.2.2.3.3.2`): The governance vote on the Edit Proposal is published on Monday, 16:00 UTC of week 2 and runs through Thursday of week 2.
  - **Prime Spell Review** (`A.1.10.2.3.2.2.3.3.3`): The Prime Spell delivered in `A.1.10.2.3.2.2.3.3.1` must be externally reviewed during week 2, before the Prime Spell payload delivery specified.
  - **Sky Core GovOps Meeting** (`A.1.10.2.3.2.2.3.3.4`): The Sky Core GovOps meeting on Tuesday of week 2 includes review of the Prime Spell content alongside Sky Core content for the same Executive Vote cycle.
  - **Vote Outcome And Atlas Or Artifact Update** (`A.1.10.2.3.2.2.3.3.5`): If the governance vote passes, the approved Edit Proposal must be incorporated into the Atlas or applicable Agent Artifact by Thursday, 23:59 UTC of week 2, establishing the provenance for the Prime Spell to be included in the Sky Core Exec.
  - **Prime Agent Delivers Prime Spell Payload** (`A.1.10.2.3.2.2.3.3.6`): By Friday, 16:00 UTC of week 2, the Prime Agent must deliver the final Prime Spell payload in the #govops Discord channel.
  - **Prime Spell Recorded In Executive Sheet** (`A.1.10.2.3.2.2.3.3.7`): By Friday, 16:00 UTC of week 2, the Core Facilitator must record the Prime Spell address, codehash, and execution type in the Executive Sheet for the corresponding Executive Vote.
  - **Step 4: Crafting And Publication (Week 3)** (`A.1.10.2.3.2.2.3.4`): During week 3 of the Prime Spell Process, a retrospective on the cycle is held and the Prime Spell payload is incorporated into the Sky Core Spell and published, as specified in the subdocuments herein.
  - **Prime Spell Retrospective** (`A.1.10.2.3.2.2.3.4.1`): A retrospective on the Prime Spell Process for the cycle is held on Monday of week 3, attended by the Executive Process Liaison, the Prime Agent, and the Prime Spell reviewer designated in [A.1.10.2.3.2.2.3.3.3 - Prime Spell Review](d09636e.
  - **Sky Core Spell Crafting And Publication** (`A.1.10.2.3.2.2.3.4.2`): The Sky Core Spell that includes the Prime Spell payload is crafted, reviewed, and published during week 3, as specified in `A.1.10.2.4.7` through [A.
- **New: Edits To The Atlas** (`A.1.11.1.1`, UUID `6a1ef4ee…495d`): The Operational Weekly Cycle may be used to edit the Atlas only if the pertinent Atlas document specifies that it, or a related unit of governance logic which it expressly controls, is modifiable through the Operational Weekly Cycle.
- **New: Definitions** (`A.1.11.1.2`, UUID `a7c4d100…ef73`): The subdocuments herein contain essential definitions pertinent to the Operational Weekly Cycle.
- **New: Language Disallowing Simultaneous Edits Not Allowed** (`A.1.11.2.5.1`, UUID `aa76a7ea…77d3`): Atlas Edit Weekly Cycle Proposals cannot include language that aims to prevent other Atlas Edit Weekly Cycle Proposals from editing the same component of the Atlas within the same Governance Cycle.
- **New: Simultaneous Edit Reconciliation Process Definition** (`A.1.11.2.5.2`, UUID `edb3b979…27ea`): Where voters approve multiple Atlas Edit Weekly Cycle Proposals that seek to edit the same component or components of the Atlas within the same Governance Cycle, the process described below must be followed.
- **New: Atlas Edit Monthly Cycle** (`A.1.12.2`, UUID `d2cbddd2…4cb5`): This Section defines the Atlas Edit Monthly Cycle, which provides a predictable framework for monthly edits to the Atlas.
  - **Origination** (`A.1.12.2.1.1`): The author of an Atlas Edit Monthly Cycle proposal ("proposal", "Atlas Edit Proposal", "AEP", "Monthly Cycle Proposal", or "AEM Proposal") must post the proposal in the Sky Forum under the appropriate category.
  - **Triggering Requirement** (`A.1.12.2.1.2`): An Atlas Edit Monthly Cycle Proposal can proceed to verification by the Core Facilitator only if it is triggered by a Ranked Delegate whose AD Buffer contains at least the Triggering Threshold (see [A.1.6.4.4.2.1.1 - Triggering Threshold](2.
  - **Core Facilitator’s Initial Verification** (`A.1.12.2.1.3`): After the Atlas Edit Proposal is triggered, the Core Facilitator must verify that the Atlas Edit Proposal follows the template specified in `A.1.12.2.3`.
  - **Atlas Edit Proposal Requirements** (`A.1.12.2.2`): The requirements for an Atlas Edit Proposal are defined in the subdocuments herein.
  - **Atlas Edit Proposal Template** (`A.1.12.2.3`): All Atlas Edit Proposals must use the following template.
  - **Atlas Edit Proposal Statuses** (`A.1.12.2.4`): An Atlas Edit Proposal can be assigned several different statuses: RFC, Formal Submission, Rejected-Misaligned, Accepted, Rejected, and Obsolete.
  - **Process Definition** (`A.1.12.2.5`): The first Monday of each calendar month marks the beginning of the Monthly Governance Cycle.
- **New: Pre-Eminence Of The Sky Core Atlas** (`A.1.14.1.3`, UUID `0f55f573…3eb6`): The first five (5) Scopes of the Sky Atlas, together with the Preamble, serve as the foundational governance ruleset for the entire Sky ecosystem.
- **New: Scope Bootstrapping** (`A.1.15`, UUID `ba97b4dd…c6bf`): This Article defines rules and procedures for swiftly resolving issues that may arise in the Governance Scope during the transition to the Endgame State.
  - **Scope Bootstrapping** (`A.1.15.1`): This Section defines bootstrapping measures that can override requirements and specifications in the Atlas.
  - **Multiple Conflicting Atlas Edit Proposals** (`A.1.15.1.1`): When conflicting Atlas Edit Proposals are approved within a short period of each other, the Core Facilitator can decide to merge parts of the proposals together to ensure that the aggregate changes incorporate the best updates from each of.
  - **Governance Security & Ecosystem Actor Embedding** (`A.1.15.1.2`): As a temporary bootstrapping measure, incubating Ecosystem Actor Atlas Axis will be embedded in Core Facilitator-permissioned communication channels where Executive Vote-coordination work is performed.
- **New: Atlas Within The Synome** (`A.1.3.1.1`, UUID `91a22c90…ad96`): The Atlas is part of a larger Synome.
- **New: Characteristics Of Synome Documents** (`A.1.3.1.2`, UUID `a7ccee03…ffb4`): Synome Documents are machine-readable documents within the Synome that are not Atlas Documents.
- **New: Organization Of Synome Documents** (`A.1.3.1.3`, UUID `f90ef30f…e7ac`): Synome Documents do not follow the hierarchical Document Identifier scheme of Atlas Documents specified in `A.1.2.1.1`.
- **New: Supremacy Of Atlas Documents** (`A.1.3.1.4`, UUID `614e00fe…67b3`): In any case of conflict between an Atlas Document and a Synome Document, the Atlas Document takes precedence.
- **New: Delegated Authority Updates** (`A.1.3.2`, UUID `d29815ff…2a31`): The documents herein specify the designation of the Synome Editor and the process by which the Synome Editor modifies Synome Documents through delegated authority.
  - **Synome Editor** (`A.1.3.2.1`): The Synome Editor has the authority to modify Synome Documents.
  - **Designated Synome Editor** (`A.1.3.2.1.1`): The Synome Editor role is held by Archon Labs.
  - **Review Obligation** (`A.1.3.2.2`): Core GovOps, the Core Facilitator, and the Aligned Delegates must review modifications to Synome Documents made by the Synome Editor for conformance with the Atlas Documents as specified in [A.0.1.1.53 - Conformance](cb66c28b-c05f-4ccc-ad44.
  - **Correction Of Non-Conformance** (`A.1.3.2.3`): Where the parties specified in `A.1.3.2.2` identify non-conformance between modifications to Synome Documents and the Atlas Documents, they must promptly report the non-conformance t.
  - **Reports Of Misalignment** (`A.1.3.2.4`): Any party may report misalignment of the Synome Editor to Core GovOps.
  - **Removal Of Designation** (`A.1.3.2.5`): If Core GovOps determines that the Synome Editor is in misalignment as specified in `A.0.1.1.11`, Core GovOps must promptly propose removal of the designation specified in [A.1.3.2.1.1 -.
  - **Emergency Pause** (`A.1.3.2.6`): The Core Facilitator may pause the designation specified in `A.1.3.2.1.1` on an emergency basis pending consideration of removal as specified in [A.1.3.2.5 - Removal Of Design.
- **New: Mandate to Enforce Rules** (`A.1.6.1.1`, UUID `88a86033…e6b1`): The Core Facilitator must enforce all rules governing Aligned Delegates.
- **New: Emergency Contact Mechanism** (`A.1.6.10`, UUID `d5d4cc4a…7b92`): Aligned Delegates must safeguard the security of the Sky Protocol through the Executive Vote process.
- **New: Delegated Voting Power - Element Annotation** (`A.1.6.3.0.3.1`, UUID `9446b896…5afd`): The element "delegated voting power" refers to the ability of SKY holders and Staking users to entrust their voting power to a Delegate Contract, allowing the Aligned Delegate controlling that contract to cast votes in the Sky Governance pr.
- **New: Facilitators’ Authority To Raise Formal Allegation** (`A.1.6.6.0.4.1`, UUID `c5146fa6…d588`): Any community member or Aligned Delegate with information pertinent to suspected Alignment Conserver misalignment may take their concerns directly to the Core Facilitator.
- **New: Core Executor Facilitator** (`A.1.7.2`, UUID `29a92947…fbdb`): Every Core Executor Agent must have a Facilitator.
- **New: Facilitators Must Maintain High Level Of Operational Security** (`A.1.7.3`, UUID `014feb92…1b30`): Facilitators are required to maintain a high level of operational security, adhering to best practices in privacy, cybersecurity, and physical resilience.
- **New: Derecognition Required Where Facilitator Operational Security Is Compromised** (`A.1.7.4`, UUID `c3ba34f0…90ea`): The Core Facilitator must act swiftly to investigate a Facilitator who is suspected of breaching their requirements regarding operational security and privacy.
- **New: Facilitators Must Err On Side Of Caution** (`A.1.7.5`, UUID `ac9df70a…dcdc`): The Core Facilitator is required to err on the side of caution and take action whenever there is any real possibility that the operational security of a Facilitator is compromised.
- **New: Acting Against Misalignment** (`A.1.7.6`, UUID `7aafa61e…9f18`): The Core Facilitator is empowered with broad discretion in addressing situations where an Alignment Conserver, Ecosystem Actor or other relevant governance participant's actions are misaligned.
- **New: Justification For Operational Decisions** (`A.1.7.7`, UUID `36be7725…ef2d`): The Core Facilitator must ensure that their decisions related to ordinary operations are clearly explained and justified using publicly available information.
- **New: Prohibition On Engaging With Counterparties** (`A.1.7.8`, UUID `3f056c21…80ca`): Facilitators are generally prohibited from engaging with counterparties.
  - **Clearly Detail Their Interactions - Facilitators' Documentation Mandate** (`A.1.7.8.0.4.1`): Facilitators are required to thoroughly document all aspects of their communications and dealings with counterparties.
- **New: Governance Process And Interaction Documentation** (`A.1.7.9`, UUID `f88d568e…e709`): The operational security of Sky is reliant on clear, thorough documentation of governance processes.
- **New: Emergency Response Group Membership Criteria** (`A.1.9.1.2.1`, UUID `f83f2e87…1cbc`): The membership of the Emergency Response Group may change at the discretion of Core GovOps, and as circumstances require.
- **New: Emergency Response Group Membership** (`A.1.9.1.2.2`, UUID `6ad02ee6…7162`): The membership of the Emergency Response Group is defined as Active Data in `A.1.9.1.2.2.0.6.1`.
- **Determine How They Are Modified - Immutable Documents Can Be Amended In The Transition To Endgame** (`A.1.2.2.1.0.4.1`): `10` → `11`; `11` → `12`
- **Swift Action Is Required From Facilitators To Redress AD Misalignment** (`A.1.6.6`): `4.9` → `5`
- **Should Ban Against Occupying Two Ecosystem Roles Apply to All Sky Stakeholder Roles?** (`NR-2`): `4` → `5`

### Housekeeping
- `A.1.10.1.1` (Spell Team Anonymity): `Edits To The Atlas` → `Spell Team Anonymity`
- `A.1.10.1.2` (Chainlog): added refs to `A.1.11.1.5.1.2`, `A.1.11.1.5.1.1`
- `A.1.10.1` (General Provisions): `Operational Weekly Cycle` → `General Provisions`
- `A.1.10.2.1.1` (Executive Sheet): `` → `The Executive Sheet is used by several actors in the Executive Process. It is managed and populated by the Governance Point, used by stakeholders, who are required to provide confirmation for proposed executive items, and by the Spell Team. The Executive Sheet is the source of truth for the Spell Crafter who crafts the Spell based on its content. Only the Core Facilitator has write access to the Executive Sheet.`
- `A.1.10.2.1.2` (Target Date): `Origination Via Forum Post` → `Target Date`
- `A.1.10.2.1.3` (Executive Document): `An Atlas Edit Weekly Cycle Proposal (also "Weekly Cycle Proposal" or "AEW Proposal") can proceed to a vote only if it is triggered by a Ranked Delegate whose AD Buffer contains at least the Triggering Threshold (see [A.1.5.4.4.2.1.1 - Triggering Threshold](2c2b201e-b95f-4852-8e76-6dfe4c3c6a4f)) at the time of triggering the Proposal. The Core Facilitator is responsible for confirming that these requirements are met.` → ``; `` → `Each Executive Document corresponds to a specific Spell and describes the actions that the Spell will perform if executed. It is a critical tool for ensuring transparency, clarity, and alignment among stakeholders. The document serves as a proposal that can be voted on and either approved or rejected by Sky Governance. The Core Facilitator is responsible for producing and finalizing the Executive Document; and any changes must be made by them.`
- `A.1.10.2.1` (Definitions): `Cycle Breakdown` → `Definitions`
- `A.1.10.2.2` (Roles in the Executive Process): `An Atlas Edit Weekly Cycle Proposal should be posted to the Forum by Friday at 8:00 am UTC to ensure the Core Facilitator has sufficient time to prepare the needed polls for the following Monday.` → ``; `Every Monday, the Atlas Edit Weekly Cycle is carried out via Governance Polls. The Core Facilitator must publish the set of Governance Polls to the community Github and the official Voting Portal.` → ``
- `A.1.10.2.3` (Content Of The Executive Vote): `The Core Facilitator can reject an Atlas Edit Weekly Cycle Proposal if they deem it to be misaligned. If the Facilitator rejects an Atlas Edit Weekly Cycle Proposal for misalignment, the Ranked Delegate who triggered the poll loses their AD buffer.` → ``
- `A.1.10.2.4` (Executive Process Breakdown): `Minimum Positive Participation` → `Executive Process Breakdown`
- `A.1.10.2.5.1` (Voting Requirements): added refs to `A.1.10.2.2.4`
- `A.1.10.2.5.2` (Voting Validation): `Where simultaneous edits are non-conflicting / logically compatible: the Core Facilitator will consolidate them into a single edit either by stitching them together in the affected component or by stringing one after the other as a new component. Any action taken by the Core Facilitator in this regard will be documented publicly and should be available for examination prior to the end date of the relevant polls.` → ``; `In the event there are more than two conflicting Atlas Edit Weekly Cycle Proposals, the Core Facilitator may choose a suitable polling method that allows voters to choose between multiple options. The difference between the conflicting amendments must be clearly presented so that voters can make an informed choice on their preferred option.` → ``
- `A.1.10.2.5` (Voting Process For Executive Votes): `Reconciliation` → `Voting`
- `A.1.10.2` (Executive Process Definition): `Atlas Edit Weekly Cycle` → `Executive Process Definition`
- `A.1.10` (Sky Core Governance Security): `Weekly` → `Sky Core`
- `A.1.11.1` (Operational Weekly Cycle): `Calendar Exceptions` → `Operational Weekly Cycle`
- `A.1.11.2.1.1` (Proposals In General): `Origination` → `Proposals In General`
- `A.1.11.2.1.2` (Origination Via Forum Post): `An Atlas Edit Monthly Cycle Proposal can proceed to verification by the Core Facilitator only if it is triggered by a Ranked Delegate whose AD Buffer contains at least the Triggering Threshold (see [A.1.5.4.4.2.1.1 - Triggering Threshold](2c2b201e-b95f-4852-8e76-6dfe4c3c6a4f)) at the time of triggering the Proposal. The Core Facilitator is responsible for confirming that these requirements are met.` → ``
- `A.1.11.2.1.3` (Triggering Requirement): `Core Facilitators’ Initial Verification` → `Triggering Requirement`; `After the Atlas Edit Proposal is triggered, the Core Facilitator must verify that the Atlas Edit Proposal follows the template specified in [A.1.11.2.3 - Atlas Edit Proposal Template](3af371ae-cc75-47c8-bd51-9446d68afea7).` → ``
- `A.1.11.2.1` (Cycle Breakdown): `define infrastructure and processes for` → `provide a breakdown of`
- `A.1.11.2.2` (Preparation And Publication of Governance Poll): `` → `An Atlas Edit Weekly Cycle Proposal should be posted to the Forum by Friday at 8:00 am UTC to ensure the Core Facilitator has sufficient time to prepare the needed polls for the following Monday.`; `` → `Every Monday, the Atlas Edit Weekly Cycle is carried out via Governance Polls. The Core Facilitator must publish the set of Governance Polls to the community Github and the official Voting Portal.`
- `A.1.11.2.3` (Rejecting A Proposal For Misalignment): `- Link to the Pull Request containing the proposed Atlas Edit. The Core Facilitator can create the Pull Request on request.` → ``; `` → `The Core Facilitator can reject an Atlas Edit Weekly Cycle Proposal if they deem it to be misaligned. If the Facilitator rejects an Atlas Edit Weekly Cycle Proposal for misalignment, the Ranked Delegate who triggered the poll loses their AD buffer.`
- `A.1.11.2.4` (Minimum Positive Participation): `An AEP has been blocked by the Core Facilitator from entering the Monthly Cycle due to misalignment.` → ``
- `A.1.11.2.5` (Reconciliation Process): `After reviewing the AEPs, the Core Facilitator must decide whether each submitted AEP warrants moving forward to a Ratification Poll.` → ``; `The Core Facilitator publish the set of Ratification Polls. The format of these is defined in [A.1.11.2.6 - Ratification Poll Requirements](13e6da57-ee8e-4593-90f2-698642b1c82f).` → ``
- `A.1.11.2` (Atlas Edit Weekly Cycle): `Monthly` → `Weekly`
- `A.1.11` (Weekly Governance Cycle): `Monthly` → `Weekly`
- `A.1.13.1.1` (Overview): removed refs to `A.1.2.2.2.17`
- `A.1.13.1.2` (Responsible Party): removed `###### A.1.12.1.2 - Responsible Party [Core]`
- `A.1.13.1.3` (Update Process): removed `###### A.1.12.1.3 - Update Process [Core]`
- `A.1.12.1` (Calendar Exceptions): `Updating Active Data` → `Calendar Exceptions`
- `A.1.12` (Monthly Governance Cycle): `modifications to Active Data documents. Active Data documents can be directly modified by Facilitators or other recognized actors through processes that occur outside` → ``
- `A.1.13.1.1` (Overview): added refs to `A.1.2.2.2.17`
- `A.1.13.1.2` (Responsible Party): `Sky Core Atlas` → `Responsible Party`
- `A.1.13.1.3` (Update Process): removed refs to `A.1.14.1.2`
- `A.1.13.1` (Updating Active Data): `Agents And The Sky Atlas` → `Updating Active Data`
- `A.1.13` (Updating Active Data): `governs` → `regulates modifications to Active Data documents. Active Data documents can be directly modified by Facilitators or other recognized actors through processes that occur outside`
- `A.1.14.1.1` (Sky Atlas Jurisdiction): `Core Facilitator can decide to merge parts of` → `overarching governance framework for`
- `A.1.14.1.2` (Sky Core Atlas): `Facilitator-permissioned communication channels where Executive Vote-coordination work is performed` → `Atlas"`
- `A.1.14.1` (Agents And The Sky Atlas): `Scope Bootstrapping` → `Agents And The Sky Atlas`
- `A.1.14` (Relationship Between Sky Core And Agents): `Scope Bootstrapping` → `Relationship Between Sky Core And Agents`
- `A.1.3.1` (Definition): `Atlas Operational Platform` → `Definition`
- `A.1.3` (Synome Documents): `Governance Accessibility` → `Synome Documents`
- `A.1.5.1.1` (Role Of Core Facilitator): `###### A.1.4.1.1 - Role Of Core Facilitator [Core]` → ``; `The Core Facilitator must be vigilant in enforcing all rules applicable to Alignment Conservers. The Core Facilitator must take prompt action against Alignment Conservers if they break rules specified in the Atlas, or otherwise act misaligned.` → ``
- `A.1.4.1` (Atlas Operational Platform): `ACs Subject To Strict Requirements` → `Atlas Operational Platform`
- `A.1.5.10` (AC Derecognition): `Derecognition is the ultimate accountability measure for misalignment and entails permanently removing the individual or entity from their role as an Alignment Conserver. An individual/entity who has been derecognized from a Facilitator role is not eligible to serve as an Aligned Delegate, and vice versa.` → ``
- `A.1.5.2` (ACs Must Safeguard The Spirit Of The Atlas): removed `##### A.1.4.2 - ACs Must Safeguard The Spirit Of The Atlas [Section]`
- `A.1.5.3.0.3.1` (Circumvent - Element Annotation): removed `###### A.1.4.3.0.3.1 - Circumvent - Element Annotation [Annotation]`
- `A.1.5.3` (Universal Alignment Requirements): removed `##### A.1.4.3 - Universal Alignment Requirements [Section]`
- `A.1.5.4` (Standard of Proof In Universal Alignment Controversies): removed `##### A.1.4.4 - Standard of Proof In Universal Alignment Controversies [Section]`
- `A.1.5.5` (ACs Can Be Operationally Active In Only One Role At A Time): `An Alignment Conserver can assume one of two roles: Aligned Delegate (AD) and Facilitator. ACs may only be operationally active in a single AC role and may not simultaneously assume multiple AC roles or other ecosystem roles such as Ecosystem Actors.` → ``
- `A.1.5.6.0.4.1` (Evaluating AC breach of role-specific requirement vs. general requirement): `When an Alignment Conserver breaches a role-specific requirement, this is misalignment on par with a breach of a general AC requirement, and vice versa. Facilitators must not default to assigning greater or lesser culpability on the sole basis of whether the breached rule is role-specific or general. Apart from this caveat, misaligned acts can have varying degrees of severity or harm, and should be individually evaluated by the Facilitator in any action.` → ``
- `A.1.5.6` (ACs Subject To Both General And Role-specific Requirements): `In addition, Aligned Delegates and Facilitators must adhere to the specific requirements tied to their specialized roles. These specific requirements are detailed in [A.1.5 - Aligned Delegates](75f0063c-ad70-49e4-b356-9b76097ced7b) and [A.1.6 - Facilitators](1ce24b08-84ff-4524-9710-49bba429c6ef). Breaching these role-specific requirements and responsibilities is misalignment equivalent to breaching the general AC-requirements.` → ``
- `A.1.5.7` (AC Requirements Of Anonymity And High Operational Security): `The Alignment Conserver roles of Facilitator and Aligned Delegate require anonymity and high levels of operational security. Breaches of these anonymity and operational security requirements are considered serious misalignment. In the event of such breaches, the known identities of individuals holding these AC roles shall be promptly derecognized, and they will be barred from further participation as Alignment Conservers.` → ``
- `A.1.5.8.0.4.1` (Facilitators’ Authority To Raise Formal Allegation): `###### A.1.4.8.0.4.1 - Facilitators’ Authority To Raise Formal Allegation [Action Tenet]` → ``; `Any community member or Aligned Delegate with information pertinent to suspected Alignment Conserver misalignment may take their concerns directly to the Core Facilitator. Upon receiving such information, the Core Facilitator must promptly conduct an initial review to quickly assess the credibility of the concern. Based on this preliminary review, the Core Facilitator must decide whether to initiate a formal adjudication process in accordance with [A.1.4.9 - Adjudication Process](560e1024-0897-4f1e-ae71-3ba31e29ed57).` → ``
- `A.1.5.8` (Swift Action Is Required From Facilitators To Redress AC Misalignment): `##### A.1.4.8 - Swift Action Is Required From Facilitators To Redress AC Misalignment [Section]` → ``; `The Core Facilitator must act swiftly when an AC is suspected of breaching the requirements defined in this Article, or the requirements defined in the Articles specific to the Aligned Delegate or Facilitator role.` → ``
- `A.1.5.9` (Adjudication Process): `The Core Facilitator is responsible for adjudicating formal allegations of misalignment or operational security breaches brought against Alignment Conservers (ACs).` → ``; `In the adjudication of these matters, the Core Facilitator is mandated to hold ACs to the highest standard of Universal Alignment, without granting them the benefit of the doubt.` → ``
- `A.1.4` (Governance Accessibility): `Alignment Conservers` → `Governance Accessibility`
- `A.1.5.1.1` (Role Of Core Facilitator): `Mandate to Enforce Rules` → `Role Of Core Facilitator`; `` → `The Core Facilitator must take prompt action against Alignment Conservers if they break rules specified in the Atlas, or otherwise act misaligned.`
- `A.1.5.1` (ACs Subject To Strict Requirements): `Core Facilitator Responsibilities` → `ACs Subject To Strict Requirements`; `Core Facilitator with regard to Aligned Delegates` → `Sky Ecosystem`
- `A.1.5.10` (AC Derecognition): `` → `Derecognition is the ultimate accountability measure for misalignment and entails permanently removing the individual or entity from their role as an Alignment Conserver. An individual/entity who has been derecognized from a Facilitator role is not eligible to serve as an Aligned Delegate, and vice versa.`
- `A.1.5.2` (ACs Must Safeguard The Spirit Of The Atlas): `Aligned Delegate Responsibilities` → `ACs Must Safeguard The Spirit Of The Atlas`
- `A.1.5.3.0.3.1` (Circumvent - Element Annotation): `Delegated Voting Power` → `Circumvent`
- `A.1.5.3` (Universal Alignment Requirements): `In General` → `Universal Alignment Requirements`
- `A.1.5.4` (Standard of Proof In Universal Alignment Controversies): `Ranked Delegates` → `Standard of Proof In Universal Alignment Controversies`
- `A.1.5.5` (ACs Can Be Operationally Active In Only One Role At A Time): `Delegates are` → `Delegate (AD) and Facilitator. ACs may only be operationally active in a single AC role and may`
- `A.1.5.6.0.4.1` (Evaluating AC breach of role-specific requirement vs. general requirement): `###### A.1.5.6.0.4.1 - Facilitators’ Authority To Raise Formal Allegation [Action Tenet]` → ``; `Any community member or Aligned Delegate with information pertinent to suspected Alignment Conserver misalignment may take their concerns directly to the Core Facilitator.  Upon receiving such information, the Core Facilitator must promptly conduct an initial review to quickly assess the credibility of the concern. Based on this preliminary review, the Core Facilitator must decide whether to initiate a formal adjudication process in accordance with [A.1.4.9 - Adjudication Process](560e1024-0897-4f1e-ae71-3ba31e29ed57).` → ``
- `A.1.5.6` (ACs Subject To Both General And Role-specific Requirements): `##### A.1.5.6 - Swift Action Is Required From Facilitators To Redress AD Misalignment [Section]` → ``; `The Facilitator must act swiftly when an AD is suspected of breaching the requirements defined in this Article, or the requirements defined in [A.1.4 - Alignment Conservers](df4f9bfd-e743-44b5-9c62-9c5f10b15340).` → ``
- `A.1.5.7` (AC Requirements Of Anonymity And High Operational Security): `` → `The Alignment Conserver roles of Facilitator and`
- `A.1.5.8.0.4.1` (Facilitators’ Authority To Raise Formal Allegation): `Promptly Derecognized - Mandated Timeline For AD Derecognition For Operational Security Breach` → `Facilitators’ Authority To Raise Formal Allegation`; `The element '` → `Any community member or Aligned Delegate with information pertinent to suspected Alignment Conserver misalignment may take their concerns directly to the Core Facilitator. Upon receiving such information, the Core Facilitator must`
- `A.1.5.8` (Swift Action Is Required From Facilitators To Redress AC Misalignment): `All Facilitators must act swiftly to investigate ADs who are suspected of breaching their requirements regarding operational security and privacy.` → ``; `The Core Facilitator must initiate a formal adjudication pursuant to [A.1.4.9 - Adjudication Process](560e1024-0897-4f1e-ae71-3ba31e29ed57) where there is an allegation concerning AD breach of operational security.` → ``
- `A.1.5.9` (Adjudication Process): `Facilitators Must Err On Side Of Caution` → `Adjudication Process`; `Facilitators are required to err on the side of caution and take action whenever there is any real possibility that the operational security of an Aligned Delegate (AD) is compromised. Facilitators are afforded significant discretion in making judgement calls related to operational security standards for ADs.` → ``
- `A.1.5` (Alignment Conservers): `Aligned Delegates` → `Alignment Conservers`
- `A.1.6.1` (Core Facilitator Responsibilities): `Operational Executor` → `Core`; `Every Operational Executor Agent must have a Facilitator. The Operational Executor Agent and Facilitator must enter into an agreement where the Facilitator agrees to interpret the Atlas and Artifacts on behalf` → `This Section defines specific responsibilities`
- `A.1.6.2` (Aligned Delegate Responsibilities): `Core Executor Facilitator` → `Aligned Delegate Responsibilities`; `Every Core Executor Agent must have a Facilitator. The Core Executor Agent and Facilitator must enter into an agreement where the Facilitator agrees to interpret the Atlas and Artifacts on behalf` → `This Section defines specific responsibilities`
- `A.1.6.3` (In General): `Facilitators Must Maintain High Level Of Operational Security` → `In General`; `Facilitators` → `Delegate Contracts`
- `A.1.6.4` (Ranked Delegates): `##### A.1.6.4 - Derecognition Required Where Facilitator Operational Security Is Compromised [Section]` → ``; `The Core Facilitator must act swiftly to investigate a Facilitator who is suspected of breaching their requirements regarding operational security and privacy.` → ``
- `A.1.6.5` (Kickbacks Prohibited): `Facilitators Must Err On Side Of Caution` → `Kickbacks Prohibited`; `The Core Facilitator is required to err on the side of caution and take action whenever there is any real possibility that the operational security of a Facilitator is compromised. The Core Facilitator is afforded significant discretion in making judgement calls related to operational security standards for Facilitators.` → ``
- `A.1.6.7` (Mandate To Maintain High Level of Operational Security): `The Core Facilitator must ensure that their decisions related to ordinary operations are clearly explained and justified using publicly available information. The Core Facilitator is generally prohibited from basing their decisions on internal knowledge or undisclosed data that is not accessible to the public.` → ``; `Limited exceptions to this rule apply when Facilitators' decisions involve sensitive security matters. However, even in these situations, the Core Facilitator should ensure that the rationale for their decision is communicated in a manner that respects security concerns while maintaining as much transparency as possible.` → ``
- `A.1.6.8.0.4.1` (Promptly Derecognized - Mandated Timeline For AD Derecognition For Operational Security Breach): `###### A.1.6.8.0.4.1 - Clearly Detail Their Interactions - Facilitators' Documentation Mandate [Action Tenet]` → ``; `Facilitators are required to thoroughly document all aspects of their communications and dealings with counterparties. This includes the content of discussions, the context of interactions (date and time), and any decisions made or actions taken as a result.` → ``
- `A.1.6.8` (Derecognition Required Where AD Operational Security Is Compromised): `Facilitators are generally prohibited from engaging with counterparties. The sole exception to this rule is where Facilitators must communicate with counterparties to set up governance processes. In such cases, the Facilitators must clearly detail their interactions with the counterparties.` → ``; `` → `All Facilitators must act swiftly to investigate ADs who are suspected of breaching their requirements regarding operational security and privacy.`
- `A.1.6.9` (Facilitators Must Err On Side Of Caution): `Governance Process And Interaction Documentation` → `Facilitators Must Err On Side Of Caution`; `The operational security of Sky is reliant on clear, thorough documentation of governance processes. Facilitators must document all operational and governance processes, as well as all interactions with ecosystem stakeholders.` → ``
- `A.1.6` (Aligned Delegates): `Facilitators` → `Aligned Delegates`; `Facilitators are contracted` → `Aligned Delegates (ADs) possess considerable influence over the Sky Protocol through their control of delegated voting power. Their primary focus is to prevent the abuse of this power, whether`
- `A.1.8.1.1` (Core Council Risk Advisor): `###### A.1.7.1.1 - Core Council Risk Advisor [Core]` → ``; `The Core Council Risk Advisor is a specialized role for a designated Professional Ecosystem Actor to provide financial analysis and risk management advice to the Core Council and other relevant parties within Sky.` → ``
- `A.1.8.1.2.1` (Protocol Security Workstream Lead Requirements): removed `###### A.1.7.1.2.1 - Protocol Security Workstream Lead Requirements [Core]`
- `A.1.8.1.2.2` (Designated Protocol Security Workstream Lead): removed `###### A.1.7.1.2.2 - Designated Protocol Security Workstream Lead [Core]`
- `A.1.8.1.2` (Protocol Security Workstream Lead): removed `###### A.1.7.1.2 - Protocol Security Workstream Lead [Core]`
- `A.1.7.1` (Operational Executor Facilitator): `Active Ecosystem Actors` → `Operational Executor Facilitator`; `Active or Incubating Ecosystem Actors work according` → `Every Operational Executor Agent must have a Facilitator. The Operational Executor Agent and Facilitator must enter into an agreement where the Facilitator agrees`
- `A.1.7` (Facilitators): `Professional Ecosystem Actors` → `Facilitators`; `Professional Ecosystem Actors` → `A type of Alignment Conserver, Facilitators`
- `A.1.8.1.1` (Core Council Risk Advisor): `Definition Of Emergency Situations` → `Core Council Risk Advisor`; `Pursuant to [A.0.1.2.1 - Facilitators’ Broad Discretionary Capacity](f18229fe-fbc3-4dc8-ad84-4bca2915f6c4), the Facilitators have broad discretion to apply the emergency-situation processes defined in [A.1.8.1 - Emergency Response](20dcf582-8862-48b3-9ca9-c3703871bd14) to urgent situations. Urgent situations are defined as any situation that involves a time-sensitive matter that would need an expedited governance process, where following a standard governance cycle would be too slow, risk a larger problem, or constitute an important missed opportunity.` → ``
- `A.1.8.1.2.1` (Protocol Security Workstream Lead Requirements): `Emergency Response Group Membership Criteria` → `Protocol Security Workstream Lead Requirements`
- `A.1.8.1.2.2` (Designated Protocol Security Workstream Lead): removed refs to `A.1.9.1.2.2.0.6.1`
- `A.1.8.1.2` (Protocol Security Workstream Lead): `group of Facilitators` → `specialized role for a designated Professional Ecosystem Actor to provide security oversight`
- `A.1.8.1` (Active Ecosystem Actors): removed refs to `A.1.10.5`
- `A.1.8` (Professional Ecosystem Actors): `Emergency Response System` → `Professional Ecosystem Actors`
- `A.1.9.1.1` (Definition Of Emergency Situations): `` → `Pursuant to [A.0.1.2.1 - Facilitators’ Broad Discretionary Capacity](f18229fe-fbc3-4dc8-ad84-4bca2915f6c4), the Facilitators have broad discretion to apply the emergency-situation processes defined in [A.1.9.1 - Emergency Response](20dcf582-8862-48b3-9ca9-c3703871bd14) to urgent situations. Urgent situations are defined as any situation that involves a time-sensitive matter that would need an expedited governance process, where following a standard governance cycle would be too slow, risk a larger problem, or constitute an important missed opportunity.`
- `A.1.9.1.2` (Emergency Response Group): `Sky’s core smart contracts. Each contract entry in the Chainlog is identified by a unique key ("Chainlog key")` → `Facilitators`
- `A.1.9.1` (Emergency Response): added refs to `A.1.10.5`
- `A.1.10.2.1.1` (Executive Sheet): `The Executive Sheet is used by several actors in the Executive Process. It is managed and populated by the Governance Point, used by stakeholders, who are required to provide confirmation for proposed executive items, and by the Spell Team. The Executive Sheet is the source of truth for the Spell Crafter who crafts the Spell based on its content. Only the Core Facilitators have write access to the Executive Sheet.` → ``
- `A.1.10.2.1.2` (Target Date): removed `###### A.1.9.2.1.2 - Target Date [Core]`
- `A.1.10.2.1.3` (Executive Document): `Each Executive Document corresponds to a specific spell and describes the actions that the spell will perform if executed. It is a critical tool for ensuring transparency, clarity, and alignment among stakeholders. The document serves as a proposal that can be voted on and either approved or rejected by Sky Governance. The Core Facilitators are responsible for producing and finalizing the Executive Document; and any changes must be made by them.` → ``
- `A.1.10.2.1` (Definitions): removed `###### A.1.9.2.1 - Definitions [Core]`
- `A.1.10.2.2` (Roles in the Executive Process): removed `###### A.1.9.2.2 - Roles in the Executive Process [Core]`
- `A.1.10.2.3` (Content Of The Executive Vote): removed `###### A.1.9.2.3 - Content Of The Executive Vote [Core]`
- `A.1.10.2.4` (Executive Process Breakdown): removed `###### A.1.9.2.4 - Executive Process Breakdown [Core]`
- `A.1.10.2.5.1` (Voting Requirements): removed refs to `A.1.10.2.2.4`
- `A.1.10.2.5.2` (Voting Validation): removed refs to `A.1.10.2.4.12`
- `A.1.10.2.5` (Voting Process For Executive Votes): removed `###### A.1.9.2.5 - Voting Process For Executive Votes [Core]`
- `A.1.10.2` (Executive Process Definition): removed `##### A.1.9.2 - Executive Process Definition [Section]`
- `A.1.9` (Emergency Response System): `Sky Core Governance Security` → `Emergency Response System`
- `A.1.10.2.1.10` renumbered (UUID stable: `202874e5…6395`)
- `A.1.10.2.1.11` renumbered (UUID stable: `e007c08a…366f`)
- `A.1.10.2.1.12` renumbered (UUID stable: `8d7a61c4…3cdd`)
- `A.1.10.2.1.4` renumbered (UUID stable: `c0aea3f8…5ecf`)
- `A.1.10.2.1.5` renumbered (UUID stable: `0919d4bd…ba54`)
- `A.1.10.2.1.6` renumbered (UUID stable: `7171aa68…b5e9`)
- `A.1.10.2.1.7` renumbered (UUID stable: `7d798e34…61e6`)
- `A.1.10.2.1.9` renumbered (UUID stable: `34fb69c2…b993`)
- `A.1.10.2.2.1.1` renumbered (UUID stable: `4137e37c…c9ce`)
- `A.1.10.2.2.1.2` renumbered (UUID stable: `6de84303…b9bc`)
- `A.1.10.2.2.2.1` renumbered (UUID stable: `4862ed4e…0a77`)
- `A.1.10.2.2.2` renumbered (UUID stable: `6474ab2e…d471`)
- `A.1.10.2.2.3` renumbered (UUID stable: `4ed84898…27e9`)
- `A.1.10.2.2.4.1` renumbered (UUID stable: `891a72ff…36ac`)
- `A.1.10.2.2.4.2` renumbered (UUID stable: `c38ceb17…24b5`)
- `A.1.10.2.2.4` renumbered (UUID stable: `3e1d0486…11e6`)
- `A.1.10.2.3.1.1` renumbered (UUID stable: `11cf1764…3192`)
- `A.1.10.2.3.1.2` renumbered (UUID stable: `df0835ea…13b9`)
- `A.1.10.2.3.1.3` renumbered (UUID stable: `18b4c424…8f3b`)
- `A.1.10.2.3.1` renumbered (UUID stable: `d1d16776…c45b`)
- `A.1.10.2.3.2.1.1.1.1` renumbered (UUID stable: `1ab0de04…cde8`)
- `A.1.10.2.3.2.1.1.1.2` renumbered (UUID stable: `7ac692f1…3302`)
- `A.1.10.2.3.2.1.1.1.3` renumbered (UUID stable: `7b41e751…e172`)
- `A.1.10.2.3.2.1.1.1.4` renumbered (UUID stable: `0465a8ef…8364`)
- `A.1.10.2.3.2.1.1.1` renumbered (UUID stable: `12a9e981…01d4`)
- `A.1.10.2.3.2.1.1` renumbered (UUID stable: `9ad39944…1d5a`)
- `A.1.10.2.3.2.1.2.1.1` renumbered (UUID stable: `22ee3dc8…53aa`)
- `A.1.10.2.3.2.1.2.1.2.1` renumbered (UUID stable: `3d031b7c…2ab2`)
- `A.1.10.2.3.2.1.2.1.2` renumbered (UUID stable: `ef6d73e5…80bf`)
- `A.1.10.2.3.2.1.2.1.3` renumbered (UUID stable: `d0c4f880…3ac1`)
- `A.1.10.2.3.2.1.2.1` renumbered (UUID stable: `769c850b…c32c`)
- `A.1.10.2.3.2.1.4.1` renumbered (UUID stable: `b81371c0…5a3a`)
- `A.1.10.2.3.2.1` renumbered (UUID stable: `55e774c1…d557`)
- `A.1.10.2.3.2.2.1.1` renumbered (UUID stable: `0782d6bf…1d82`)
- `A.1.10.2.3.2.2.1.2` renumbered (UUID stable: `0bc23932…4a7a`)
- `A.1.10.2.3.2.2.1.3.1` renumbered (UUID stable: `109ba764…6188`)
- `A.1.10.2.3.2.2.1.3.2` renumbered (UUID stable: `9433535a…3ca1`)
- `A.1.10.2.3.2.2.1.3.3` renumbered (UUID stable: `b3cd3112…b6ca`)
- `A.1.10.2.3.2.2.1.3.4` renumbered (UUID stable: `20aece61…4222`)
- `A.1.10.2.3.2.2.1.3` renumbered (UUID stable: `c14b730a…3076`)
- `A.1.10.2.3.2.2.1.4.1.1.1` renumbered (UUID stable: `01b44f43…fb35`)
- `A.1.10.2.3.2.2.1.4.1.1` renumbered (UUID stable: `8323c8af…ebd9`)
- `A.1.10.2.3.2.2.1.4.1.2` renumbered (UUID stable: `e480b8f8…9a83`)
- `A.1.10.2.3.2.2.1.4.1` renumbered (UUID stable: `13e611c6…cb29`)
- `A.1.10.2.3.2.2.1.4.2.1` renumbered (UUID stable: `4c165fcc…e591`)
- `A.1.10.2.3.2.2.1.4.2.2` renumbered (UUID stable: `fd1f682c…2021`)
- `A.1.10.2.3.2.2.1.4.2.3.1` renumbered (UUID stable: `540e8f4e…e39e`)
- `A.1.10.2.3.2.2.1.4.2.3.2` renumbered (UUID stable: `9555c38c…453a`)
- `A.1.10.2.3.2.2.1.4.2.3` renumbered (UUID stable: `59d5aa08…5e6f`)
- `A.1.10.2.3.2.2.1.4.2` renumbered (UUID stable: `160bf31b…024e`)
- `A.1.10.2.3.2.2.1.4` renumbered (UUID stable: `3921d0c0…2cc1`)
- `A.1.10.2.3.2.2.1.5.0.6.1` renumbered (UUID stable: `7bcaaa37…438f`)
- `A.1.10.2.3.2.2.1.5` renumbered (UUID stable: `a2777f65…2f8a`)
- `A.1.10.2.3.2.2.1` renumbered (UUID stable: `e44ede45…303f`)
- `A.1.10.2.3.2.2.2.1.1` renumbered (UUID stable: `de77dbbc…a543`)
- `A.1.10.2.3.2.2.2.1.2` renumbered (UUID stable: `a93952b9…3df4`)
- `A.1.10.2.3.2.2.2.1.3` renumbered (UUID stable: `0c0e09e7…bca1`)
- `A.1.10.2.3.2.2.2.1.4` renumbered (UUID stable: `1fc1ba29…f2ab`)
- `A.1.10.2.3.2.2.2.1.5` renumbered (UUID stable: `fe8e5e31…2d81`)
- `A.1.10.2.3.2.2.2.1.6` renumbered (UUID stable: `14954d6a…9ca7`)
- `A.1.10.2.3.2.2.2.1.7` renumbered (UUID stable: `02cb6865…9258`)
- `A.1.10.2.3.2.2.2.1.8` renumbered (UUID stable: `b405eadc…01c7`)
- `A.1.10.2.3.2.2.2.1` renumbered (UUID stable: `db6f880b…e7f1`)
- `A.1.10.2.3.2.2.2` renumbered (UUID stable: `9b3edbbf…471f`)
- `A.1.10.2.3.2.2` renumbered (UUID stable: `8b5181e8…18e7`)
- `A.1.10.2.3.2.3.1.1.1` renumbered (UUID stable: `3123f615…ee9a`)
- `A.1.10.2.3.2.3.1.1.2.1` renumbered (UUID stable: `e6ec35bc…6017`)
- `A.1.10.2.3.2.3.1.1.2.2` renumbered (UUID stable: `3deb3282…cd1d`)
- `A.1.10.2.3.2.3.1.1.2.3` renumbered (UUID stable: `f23f9ea7…f451`)
- `A.1.10.2.3.2.3.1.1.2.4` renumbered (UUID stable: `ccb1f61a…1b03`)
- `A.1.10.2.3.2.3.1.1.2.5` renumbered (UUID stable: `a03c9e5a…0f47`)
- `A.1.10.2.3.2.3.1.1.2.6` renumbered (UUID stable: `50f71e34…422f`)
- `A.1.10.2.3.2.3.1.1.2.7.1` renumbered (UUID stable: `e15ea323…51da`)
- `A.1.10.2.3.2.3.1.1.2.7` renumbered (UUID stable: `8113159f…5cf7`)
- `A.1.10.2.3.2.3.1.1.2` renumbered (UUID stable: `04712596…7abd`)
- `A.1.10.2.3.2.3.1.1` renumbered (UUID stable: `e5cbb61a…c155`)
- `A.1.10.2.3.2.3.1` renumbered (UUID stable: `78ec918d…8a8b`)
- `A.1.10.2.3.2.3.2.1` renumbered (UUID stable: `a109ad0d…da43`)
- `A.1.10.2.3.2.3.2` renumbered (UUID stable: `ffc88a5e…2f14`)
- `A.1.10.2.3.2.3` renumbered (UUID stable: `5b0fd894…0c0c`)
- `A.1.10.2.3.2` renumbered (UUID stable: `64edb1ca…d240`)
- `A.1.10.2.3.3.1` renumbered (UUID stable: `af13ac4b…25de`)
- `A.1.10.2.3.3.2.1` renumbered (UUID stable: `47a584fe…a8bd`)
- `A.1.10.2.3.3.2.2` renumbered (UUID stable: `390d239c…1b2d`)
- `A.1.10.2.3.3.2.3` renumbered (UUID stable: `0e7a4416…8307`)
- `A.1.10.2.3.3.2.4` renumbered (UUID stable: `00a4c49c…c1eb`)
- `A.1.10.2.3.3.2` renumbered (UUID stable: `0ed7559c…c904`)
- `A.1.10.2.3.3` renumbered (UUID stable: `867cad8c…09ae`)
- `A.1.10.2.4.1.1` renumbered (UUID stable: `2c99fa29…cd6e`)
- `A.1.10.2.4.1.2.1` renumbered (UUID stable: `4aa6a4d5…41e0`)
- `A.1.10.2.4.1.2.2` renumbered (UUID stable: `465c6f95…aa82`)
- `A.1.10.2.4.1.2.3` renumbered (UUID stable: `ea70f102…ef39`)
- `A.1.10.2.4.1.2` renumbered (UUID stable: `35d0ed69…538d`)
- `A.1.10.2.4.1.3` renumbered (UUID stable: `dc610140…3dd5`)
- `A.1.10.2.4.1` renumbered (UUID stable: `0f0f7021…9aa9`)
- `A.1.10.2.4.10.1` renumbered (UUID stable: `59638793…d100`)
- `A.1.10.2.4.10.10` renumbered (UUID stable: `3d0a743a…20d7`)
- `A.1.10.2.4.10.11` renumbered (UUID stable: `f394fe65…0487`)
- `A.1.10.2.4.10.2` renumbered (UUID stable: `e31813f6…3bc7`)
- `A.1.10.2.4.10.3` renumbered (UUID stable: `a7e04b56…3a91`)
- `A.1.10.2.4.10.4` renumbered (UUID stable: `81b4e7f6…4801`)
- `A.1.10.2.4.10.5` renumbered (UUID stable: `1463db73…076f`)
- `A.1.10.2.4.10.6` renumbered (UUID stable: `959dea0e…e051`)
- `A.1.10.2.4.10.7` renumbered (UUID stable: `119f1132…a1de`)
- `A.1.10.2.4.10.8` renumbered (UUID stable: `56106653…00d7`)
- `A.1.10.2.4.10.9` renumbered (UUID stable: `8411d3bb…3099`)
- `A.1.10.2.4.10` renumbered (UUID stable: `746bfb60…63ee`)
- `A.1.10.2.4.11.1.1` renumbered (UUID stable: `d3f61923…d59a`)
- `A.1.10.2.4.11.1.2` renumbered (UUID stable: `93b1ccb0…6ab4`)
- `A.1.10.2.4.11.1.3` renumbered (UUID stable: `6a1c7d77…42cf`)
- `A.1.10.2.4.11.1.4` renumbered (UUID stable: `328db91a…b7a8`)
- `A.1.10.2.4.11.1.5` renumbered (UUID stable: `75b9e342…e822`)
- `A.1.10.2.4.11.1.6` renumbered (UUID stable: `12ebd0d9…b9b0`)
- `A.1.10.2.4.11.1.7` renumbered (UUID stable: `16b127f0…ddac`)
- `A.1.10.2.4.11.1` renumbered (UUID stable: `0719e89e…09ec`)
- `A.1.10.2.4.11.2.1` renumbered (UUID stable: `3593993e…0092`)
- `A.1.10.2.4.11.2.2` renumbered (UUID stable: `047b842a…4eb4`)
- `A.1.10.2.4.11.2.3` renumbered (UUID stable: `77583ed9…86d3`)
- `A.1.10.2.4.11.2.4` renumbered (UUID stable: `6aceef83…eebd`)
- `A.1.10.2.4.11.2.5` renumbered (UUID stable: `e7f1fd21…5fb7`)
- `A.1.10.2.4.11.2.6` renumbered (UUID stable: `447d5a6d…82ae`)
- `A.1.10.2.4.11.2` renumbered (UUID stable: `5e78a59d…7db2`)
- `A.1.10.2.4.11` renumbered (UUID stable: `4a26e84d…c813`)
- `A.1.10.2.4.12.1.1` renumbered (UUID stable: `1ddd532f…2328`)
- `A.1.10.2.4.12.1.2` renumbered (UUID stable: `64c1fbdd…6744`)
- `A.1.10.2.4.12.1.3` renumbered (UUID stable: `101d5bee…9390`)
- `A.1.10.2.4.12.1` renumbered (UUID stable: `6be80bce…d373`)
- `A.1.10.2.4.12.2.1` renumbered (UUID stable: `e32e109f…353f`)
- `A.1.10.2.4.12.2.10` renumbered (UUID stable: `230c15db…9d11`)
- `A.1.10.2.4.12.2.11` renumbered (UUID stable: `3326e18a…7160`)
- `A.1.10.2.4.12.2.2` renumbered (UUID stable: `8c7fe7a6…41c6`)
- `A.1.10.2.4.12.2.3` renumbered (UUID stable: `ee18215c…7125`)
- `A.1.10.2.4.12.2.4` renumbered (UUID stable: `4800adb1…27cb`)
- `A.1.10.2.4.12.2.5` renumbered (UUID stable: `cc6f9990…063c`)
- `A.1.10.2.4.12.2.6` renumbered (UUID stable: `78db1070…b015`)
- `A.1.10.2.4.12.2.7` renumbered (UUID stable: `f26a1e7c…54fb`)
- `A.1.10.2.4.12.2.8` renumbered (UUID stable: `42979dc0…5ad7`)
- `A.1.10.2.4.12.2.9` renumbered (UUID stable: `0c457a50…f52e`)
- `A.1.10.2.4.12.2` renumbered (UUID stable: `1f2d6e6a…f446`)
- `A.1.10.2.4.12.3.1.1` renumbered (UUID stable: `ea1d866c…c158`)
- `A.1.10.2.4.12.3.1.2` renumbered (UUID stable: `a8bc220b…14ed`)
- `A.1.10.2.4.12.3.1.3` renumbered (UUID stable: `2407adac…57e9`)
- `A.1.10.2.4.12.3.1.4` renumbered (UUID stable: `438343b7…0ff8`)
- `A.1.10.2.4.12.3.1.5` renumbered (UUID stable: `354e4b28…f920`)
- `A.1.10.2.4.12.3.1.6` renumbered (UUID stable: `0ad70737…71c2`)
- `A.1.10.2.4.12.3.1.7` renumbered (UUID stable: `7f3112c8…2a11`)
- `A.1.10.2.4.12.3.1.8` renumbered (UUID stable: `a1773da6…0d85`)
- `A.1.10.2.4.12.3.1.9` renumbered (UUID stable: `46cbc700…6fca`)
- `A.1.10.2.4.12.3.1` renumbered (UUID stable: `4aa4dc55…1d71`)
- `A.1.10.2.4.12.3.2.1` renumbered (UUID stable: `fb60b182…a099`)
- `A.1.10.2.4.12.3.2.2` renumbered (UUID stable: `83f53a73…4bf3`)
- `A.1.10.2.4.12.3.2` renumbered (UUID stable: `c6b18786…1246`)
- `A.1.10.2.4.12.3.3.1` renumbered (UUID stable: `2662dc31…2eb2`)
- `A.1.10.2.4.12.3.3.10` renumbered (UUID stable: `de343461…1ad1`)
- `A.1.10.2.4.12.3.3.11` renumbered (UUID stable: `a564f010…b8fe`)
- `A.1.10.2.4.12.3.3.12` renumbered (UUID stable: `fdcea934…9b00`)
- `A.1.10.2.4.12.3.3.13` renumbered (UUID stable: `4674dbfa…ffa9`)
- `A.1.10.2.4.12.3.3.2` renumbered (UUID stable: `b28afb60…efed`)
- `A.1.10.2.4.12.3.3.3` renumbered (UUID stable: `97f4831e…5ca7`)
- `A.1.10.2.4.12.3.3.4` renumbered (UUID stable: `39f67b68…722f`)
- `A.1.10.2.4.12.3.3.5` renumbered (UUID stable: `4f7f2b2f…5a92`)
- `A.1.10.2.4.12.3.3.6` renumbered (UUID stable: `9a7a0d5e…524e`)
- `A.1.10.2.4.12.3.3.7` renumbered (UUID stable: `a6940e22…0ce7`)
- `A.1.10.2.4.12.3.3.8` renumbered (UUID stable: `353d7fab…ee4d`)
- `A.1.10.2.4.12.3.3.9` renumbered (UUID stable: `2f10b68b…2e7a`)
- `A.1.10.2.4.12.3.3` renumbered (UUID stable: `56b1cc27…c56b`)
- `A.1.10.2.4.12.3` renumbered (UUID stable: `6668e922…98eb`)
- `A.1.10.2.4.12.4.1` renumbered (UUID stable: `6f0fce93…94b4`)
- `A.1.10.2.4.12.4.2` renumbered (UUID stable: `66a80a93…fa83`)
- `A.1.10.2.4.12.4.3` renumbered (UUID stable: `6ea115ff…de6a`)
- `A.1.10.2.4.12.4.4` renumbered (UUID stable: `eca405af…d090`)
- `A.1.10.2.4.12.4.5` renumbered (UUID stable: `8bd3523a…10ad`)
- `A.1.10.2.4.12.4.6` renumbered (UUID stable: `813e403a…a755`)
- `A.1.10.2.4.12.4.7` renumbered (UUID stable: `55d6723f…096c`)
- `A.1.10.2.4.12.4` renumbered (UUID stable: `43d2fe19…a2a7`)
- `A.1.10.2.4.12` renumbered (UUID stable: `84d31eb0…8271`)
- `A.1.10.2.4.13.1` renumbered (UUID stable: `d87a286e…d235`)
- `A.1.10.2.4.13.2.1` renumbered (UUID stable: `f31bd0d0…c986`)
- `A.1.10.2.4.13.2` renumbered (UUID stable: `ee6fc86b…cd81`)
- `A.1.10.2.4.13.3` renumbered (UUID stable: `e06f6a83…2fb9`)
- `A.1.10.2.4.13.4.1` renumbered (UUID stable: `cdd724f1…a184`)
- `A.1.10.2.4.13.4.2` renumbered (UUID stable: `8ee36ed9…ee18`)
- `A.1.10.2.4.13.5` renumbered (UUID stable: `193f43fc…7906`)
- `A.1.10.2.4.13.6.1` renumbered (UUID stable: `a5959563…8b99`)
- `A.1.10.2.4.13.6.2` renumbered (UUID stable: `e3009714…16b6`)
- `A.1.10.2.4.13.6.3` renumbered (UUID stable: `2d902745…1750`)
- `A.1.10.2.4.13.6.4` renumbered (UUID stable: `f1365a6d…bd5b`)
- `A.1.10.2.4.13.6.5` renumbered (UUID stable: `0ad20a0f…2657`)
- `A.1.10.2.4.13.6` renumbered (UUID stable: `300fc1fe…5bb9`)
- `A.1.10.2.4.13` renumbered (UUID stable: `761cd866…1be1`)
- `A.1.10.2.4.2.1.1` renumbered (UUID stable: `d41c2e6a…5095`)
- `A.1.10.2.4.2.1.2` renumbered (UUID stable: `a935cfad…417e`)
- `A.1.10.2.4.2.1.3.1` renumbered (UUID stable: `f6f1efeb…afc4`)
- `A.1.10.2.4.2.1.3.2` renumbered (UUID stable: `3583410e…129c`)
- `A.1.10.2.4.2.1.3.3` renumbered (UUID stable: `e60557ed…3544`)
- `A.1.10.2.4.2.1.3.4` renumbered (UUID stable: `33ac6653…a9a7`)
- `A.1.10.2.4.2.1.3` renumbered (UUID stable: `199931bd…119a`)
- `A.1.10.2.4.2.1` renumbered (UUID stable: `bf3a5524…c94c`)
- `A.1.10.2.4.2.2.1` renumbered (UUID stable: `ec06d92c…4a72`)
- `A.1.10.2.4.2.2.2` renumbered (UUID stable: `e34b72db…1805`)
- `A.1.10.2.4.2.2.3` renumbered (UUID stable: `1dac0bce…015d`)
- `A.1.10.2.4.2.2.4` renumbered (UUID stable: `a6bab26a…6480`)
- `A.1.10.2.4.2.2` renumbered (UUID stable: `755fe505…4f9b`)
- `A.1.10.2.4.2.3.1` renumbered (UUID stable: `9e96fca0…2a48`)
- `A.1.10.2.4.2.3.2` renumbered (UUID stable: `37d03695…caf3`)
- `A.1.10.2.4.2.3.3` renumbered (UUID stable: `ea9e4dd4…49b3`)
- `A.1.10.2.4.2.3.4` renumbered (UUID stable: `9d1900e4…f845`)
- `A.1.10.2.4.2.3` renumbered (UUID stable: `7a40558a…c702`)
- `A.1.10.2.4.2` renumbered (UUID stable: `298819fe…f291`)
- `A.1.10.2.4.3.1.1` renumbered (UUID stable: `d8e11fe9…3167`)
- `A.1.10.2.4.3.1.2` renumbered (UUID stable: `25bbdd08…6286`)
- `A.1.10.2.4.3.1.3` renumbered (UUID stable: `bba8d328…6016`)
- `A.1.10.2.4.3.1.5` renumbered (UUID stable: `6361b7c7…d37e`)
- `A.1.10.2.4.3.1` renumbered (UUID stable: `b0d1a683…a716`)
- `A.1.10.2.4.3.2.1` renumbered (UUID stable: `a51689a8…8d64`)
- `A.1.10.2.4.3.2.2` renumbered (UUID stable: `28fea6ae…8272`)
- `A.1.10.2.4.3.2.3` renumbered (UUID stable: `b97f9d90…a4f5`)
- `A.1.10.2.4.3.2.4` renumbered (UUID stable: `3f90dcbd…bba7`)
- `A.1.10.2.4.3.2` renumbered (UUID stable: `c38da8ab…6e85`)
- `A.1.10.2.4.3` renumbered (UUID stable: `0f74afdf…1787`)
- `A.1.10.2.4.4.1` renumbered (UUID stable: `17f172c6…b10b`)
- `A.1.10.2.4.4.2` renumbered (UUID stable: `89d800a0…949b`)
- `A.1.10.2.4.4.3` renumbered (UUID stable: `835d1f82…e6b7`)
- `A.1.10.2.4.4` renumbered (UUID stable: `3bf7e2f3…cab7`)
- `A.1.10.2.4.5.1.1` renumbered (UUID stable: `4140df92…9284`)
- `A.1.10.2.4.5.1.2` renumbered (UUID stable: `8e18add4…c212`)
- `A.1.10.2.4.5.1.3` renumbered (UUID stable: `d6c5909e…a1a1`)
- `A.1.10.2.4.5.1.4` renumbered (UUID stable: `ea9dd463…3101`)
- `A.1.10.2.4.5.1.5` renumbered (UUID stable: `9f3b48a1…8118`)
- `A.1.10.2.4.5.1` renumbered (UUID stable: `c86c3a65…c35a`)
- `A.1.10.2.4.5.2` renumbered (UUID stable: `4c37fa46…0fa2`)
- `A.1.10.2.4.5.3` renumbered (UUID stable: `26133c1d…99f2`)
- `A.1.10.2.4.5.4` renumbered (UUID stable: `5370113e…1fe4`)
- `A.1.10.2.4.5.5` renumbered (UUID stable: `ddf293ed…9c93`)
- `A.1.10.2.4.5` renumbered (UUID stable: `558451e8…929b`)
- `A.1.10.2.4.6.1` renumbered (UUID stable: `ed4254b8…c2e2`)
- `A.1.10.2.4.6.2` renumbered (UUID stable: `d246530d…1de0`)
- `A.1.10.2.4.6` renumbered (UUID stable: `9f291bda…dd27`)
- `A.1.10.2.4.7.1` renumbered (UUID stable: `510651ca…85d2`)
- `A.1.10.2.4.7.2.2` renumbered (UUID stable: `cff7d85c…838d`)
- `A.1.10.2.4.7.2.3` renumbered (UUID stable: `816601b0…ebbd`)
- `A.1.10.2.4.7.2.4` renumbered (UUID stable: `1a0d9151…f8a9`)
- `A.1.10.2.4.7.2.5` renumbered (UUID stable: `12c126be…8339`)
- `A.1.10.2.4.7.2` renumbered (UUID stable: `c714f3b3…b8dc`)
- `A.1.10.2.4.7.3.1` renumbered (UUID stable: `38a261c4…a56e`)
- `A.1.10.2.4.7.3.2` renumbered (UUID stable: `86a2c5ba…80c8`)
- `A.1.10.2.4.7.3.3` renumbered (UUID stable: `b5740bb5…5eb1`)
- `A.1.10.2.4.7.3.4` renumbered (UUID stable: `b9cfe356…26d4`)
- `A.1.10.2.4.7.3.6` renumbered (UUID stable: `cffb2455…b236`)
- `A.1.10.2.4.7.3` renumbered (UUID stable: `2c8e81bf…4695`)
- `A.1.10.2.4.7.4.1` renumbered (UUID stable: `3f01cb21…8740`)
- `A.1.10.2.4.7.4.2` renumbered (UUID stable: `b5daecf9…688e`)
- `A.1.10.2.4.7.4.3` renumbered (UUID stable: `361f1e3c…4c06`)
- `A.1.10.2.4.7.4.4` renumbered (UUID stable: `aa0a8049…14e6`)
- `A.1.10.2.4.7.4.5` renumbered (UUID stable: `e5a69e08…99c6`)
- `A.1.10.2.4.7.4.6` renumbered (UUID stable: `c6ff5871…8219`)
- `A.1.10.2.4.7.4.7` renumbered (UUID stable: `5a4e1225…1b12`)
- `A.1.10.2.4.7.4` renumbered (UUID stable: `bd45083c…26e3`)
- `A.1.10.2.4.7` renumbered (UUID stable: `60aac647…1958`)
- `A.1.10.2.4.8.1.1` renumbered (UUID stable: `aefa846c…9410`)
- `A.1.10.2.4.8.1.2` renumbered (UUID stable: `f494539b…9603`)
- `A.1.10.2.4.8.1.3` renumbered (UUID stable: `3316956f…c043`)
- `A.1.10.2.4.8.1.4` renumbered (UUID stable: `1247b21a…ccfe`)
- `A.1.10.2.4.8.1` renumbered (UUID stable: `1fcee4d2…54a7`)
- `A.1.10.2.4.8.2.1` renumbered (UUID stable: `f57aab8a…7777`)
- `A.1.10.2.4.8.2.2` renumbered (UUID stable: `6656674a…bd91`)
- `A.1.10.2.4.8.2.3` renumbered (UUID stable: `f3b16344…9010`)
- `A.1.10.2.4.8.2.4` renumbered (UUID stable: `1e44fedd…c305`)
- `A.1.10.2.4.8.2.5` renumbered (UUID stable: `d399f662…cba1`)
- `A.1.10.2.4.8.2.6` renumbered (UUID stable: `3de17a79…598e`)
- `A.1.10.2.4.8.2.7` renumbered (UUID stable: `b6117ca8…746e`)
- `A.1.10.2.4.8.2.8` renumbered (UUID stable: `aaa621d0…f66f`)
- `A.1.10.2.4.8.2` renumbered (UUID stable: `756c8cd0…c7db`)
- `A.1.10.2.4.8.3.1` renumbered (UUID stable: `fba002f8…6c49`)
- `A.1.10.2.4.8.3.10` renumbered (UUID stable: `711c0453…fe26`)
- `A.1.10.2.4.8.3.11` renumbered (UUID stable: `ac23449a…a2a4`)
- `A.1.10.2.4.8.3.2` renumbered (UUID stable: `b99efbf0…a4fb`)
- `A.1.10.2.4.8.3.3` renumbered (UUID stable: `15a1cb2b…2fc9`)
- `A.1.10.2.4.8.3.4` renumbered (UUID stable: `63c9d3b3…0878`)
- `A.1.10.2.4.8.3.5` renumbered (UUID stable: `dd779187…94d1`)
- `A.1.10.2.4.8.3.6` renumbered (UUID stable: `c99fbfde…3dce`)
- `A.1.10.2.4.8.3.7` renumbered (UUID stable: `2724c79e…3733`)
- `A.1.10.2.4.8.3.8` renumbered (UUID stable: `e3d137d7…afeb`)
- `A.1.10.2.4.8.3.9` renumbered (UUID stable: `e33843ce…6f04`)
- `A.1.10.2.4.8.3` renumbered (UUID stable: `6d40ab22…3d6f`)
- `A.1.10.2.4.8.4.1` renumbered (UUID stable: `e6ffd366…6353`)
- `A.1.10.2.4.8.4.2` renumbered (UUID stable: `65157925…68d2`)
- `A.1.10.2.4.8.4.3` renumbered (UUID stable: `c3055900…cc62`)
- `A.1.10.2.4.8.4.4` renumbered (UUID stable: `d6e79bb0…b600`)
- `A.1.10.2.4.8.4` renumbered (UUID stable: `95c1e447…2a17`)
- `A.1.10.2.4.8.5.1` renumbered (UUID stable: `99bc6de0…647f`)
- `A.1.10.2.4.8.5.2` renumbered (UUID stable: `966fa5d7…ee8a`)
- `A.1.10.2.4.8.5.3` renumbered (UUID stable: `95c6809a…5b20`)
- `A.1.10.2.4.8.5.4` renumbered (UUID stable: `16b6e606…71bd`)
- `A.1.10.2.4.8.5.5` renumbered (UUID stable: `84a87065…8b6c`)
- `A.1.10.2.4.8.5.6` renumbered (UUID stable: `cb3303a9…43cf`)
- `A.1.10.2.4.8.5` renumbered (UUID stable: `ec5599fa…46e0`)
- `A.1.10.2.4.8` renumbered (UUID stable: `1df24674…87dd`)
- `A.1.10.2.4.9.1` renumbered (UUID stable: `4319b89d…d347`)
- `A.1.10.2.4.9.2.1` renumbered (UUID stable: `32feb38a…f92f`)
- `A.1.10.2.4.9.2.10` renumbered (UUID stable: `357b6485…4f7f`)
- `A.1.10.2.4.9.2.2` renumbered (UUID stable: `a9be4af3…38fb`)
- `A.1.10.2.4.9.2.3` renumbered (UUID stable: `952d9bdc…82b7`)
- `A.1.10.2.4.9.2.4` renumbered (UUID stable: `d3a48eb5…f4ea`)
- `A.1.10.2.4.9.2.5` renumbered (UUID stable: `eb22b81f…b531`)
- `A.1.10.2.4.9.2.6` renumbered (UUID stable: `558e18e8…f4c8`)
- `A.1.10.2.4.9.2.7` renumbered (UUID stable: `ed3350d8…b801`)
- `A.1.10.2.4.9.2.8` renumbered (UUID stable: `1de9360f…d870`)
- `A.1.10.2.4.9.2.9` renumbered (UUID stable: `83f1374d…a2af`)
- `A.1.10.2.4.9.2` renumbered (UUID stable: `fcc34865…fe9f`)
- `A.1.10.2.4.9.3` renumbered (UUID stable: `e3b236e9…de60`)
- `A.1.10.2.4.9.4` renumbered (UUID stable: `71f8c21f…d405`)
- `A.1.10.2.4.9` renumbered (UUID stable: `249a4dc7…bd12`)
- `A.1.10.2.5.3` renumbered (UUID stable: `9b43b664…d10e`)
- `A.1.10.2.5.4` renumbered (UUID stable: `9c5cae66…5623`)
- `A.1.10.3.1.1` renumbered (UUID stable: `bcf9f14d…0399`)
- `A.1.10.3.1.2` renumbered (UUID stable: `db442d8a…2b67`)
- `A.1.10.3.1` renumbered (UUID stable: `3c9545d9…02c6`)
- `A.1.10.3.2.1` renumbered (UUID stable: `3041b5f2…63b2`)
- `A.1.10.3.2.10.1` renumbered (UUID stable: `b2bffec7…c086`)
- `A.1.10.3.2.10.2` renumbered (UUID stable: `12bb55dc…8784`)
- `A.1.10.3.2.10.3` renumbered (UUID stable: `5ce20b57…2cb2`)
- `A.1.10.3.2.10` renumbered (UUID stable: `5533c091…6078`)
- `A.1.10.3.2.11` renumbered (UUID stable: `1fd7d164…5f8d`)
- `A.1.10.3.2.12` renumbered (UUID stable: `b9f3824c…b7ee`)
- `A.1.10.3.2.13.1.1` renumbered (UUID stable: `ac2fb8ab…9a70`)
- `A.1.10.3.2.13.1.2` renumbered (UUID stable: `59fecdcf…2bf9`)
- `A.1.10.3.2.13.1` renumbered (UUID stable: `c21d4246…7893`)
- `A.1.10.3.2.13.2.1.1` renumbered (UUID stable: `dd631146…9879`)
- `A.1.10.3.2.13.2.1.2` renumbered (UUID stable: `3a075a4b…03b2`)
- `A.1.10.3.2.13.2.1` renumbered (UUID stable: `9652bd2c…f574`)
- `A.1.10.3.2.13.2` renumbered (UUID stable: `2de4d031…8c05`)
- `A.1.10.3.2.13` renumbered (UUID stable: `60767684…b827`)
- `A.1.10.3.2.14` renumbered (UUID stable: `b7820ec3…c8fe`)
- `A.1.10.3.2.15` renumbered (UUID stable: `82aaec1b…5ccb`)
- `A.1.10.3.2.16` renumbered (UUID stable: `57f524b8…81e5`)
- `A.1.10.3.2.17` renumbered (UUID stable: `93089354…0e67`)
- `A.1.10.3.2.2` renumbered (UUID stable: `e604c477…acfd`)
- `A.1.10.3.2.3.1` renumbered (UUID stable: `4937205a…f421`)
- `A.1.10.3.2.3` renumbered (UUID stable: `cd57f7e4…8eba`)
- `A.1.10.3.2.4.1.1` renumbered (UUID stable: `cd377adf…0e0b`)
- `A.1.10.3.2.4.1` renumbered (UUID stable: `a228410a…bf44`)
- `A.1.10.3.2.4` renumbered (UUID stable: `54b41b8f…6cf7`)
- `A.1.10.3.2.5` renumbered (UUID stable: `2a0f27c9…8c89`)
- `A.1.10.3.2.6` renumbered (UUID stable: `d07e74b5…8768`)
- `A.1.10.3.2.7` renumbered (UUID stable: `645443f1…b1f9`)
- `A.1.10.3.2.8` renumbered (UUID stable: `5247c795…e2d4`)
- `A.1.10.3.2.9` renumbered (UUID stable: `704fbaff…a6a8`)
- `A.1.10.3.2` renumbered (UUID stable: `6781594b…eed8`)
- `A.1.10.3` renumbered (UUID stable: `c5f0e955…a568`)
- `A.1.10.4.1.1.1` renumbered (UUID stable: `4192a2f6…c3a3`)
- `A.1.10.4.1.1.2` renumbered (UUID stable: `861347b3…e44f`)
- `A.1.10.4.1.1.3` renumbered (UUID stable: `2a86809e…ce6d`)
- `A.1.10.4.1.1.4` renumbered (UUID stable: `c0337114…2b29`)
- `A.1.10.4.1.1.5` renumbered (UUID stable: `af5b97be…e328`)
- `A.1.10.4.1.1` renumbered (UUID stable: `21fa6749…0421`)
- `A.1.10.4.1.2.1` renumbered (UUID stable: `1157a0cd…f475`)
- `A.1.10.4.1.2.2` renumbered (UUID stable: `593095a6…c198`)
- `A.1.10.4.1.2.3.1.1.1` renumbered (UUID stable: `bb0b31dd…ee7d`)
- `A.1.10.4.1.2.3.1.1.2` renumbered (UUID stable: `f376a4da…fe32`)
- `A.1.10.4.1.2.3.1.1.3` renumbered (UUID stable: `a9f95fb4…036d`)
- `A.1.10.4.1.2.3.1.1.4` renumbered (UUID stable: `9f845d09…52e6`)
- `A.1.10.4.1.2.3.1.1.5` renumbered (UUID stable: `b70ebff7…ded1`)
- `A.1.10.4.1.2.3.1.1` renumbered (UUID stable: `8e618196…5fcd`)
- `A.1.10.4.1.2.3.2.1` renumbered (UUID stable: `7c0eeee4…67c0`)
- `A.1.10.4.1.2.3.2.2` renumbered (UUID stable: `8414b48b…73ba`)
- `A.1.10.4.1.2.3.2` renumbered (UUID stable: `36626f77…3922`)
- `A.1.10.4.1.2.3.3.1.1` renumbered (UUID stable: `ffb71c51…bc31`)
- `A.1.10.4.1.2.3.3.1.2` renumbered (UUID stable: `30a6d20d…023e`)
- `A.1.10.4.1.2.3.3.1` renumbered (UUID stable: `16b49e7d…2987`)
- `A.1.10.4.1.2.3.3.2.1` renumbered (UUID stable: `0939f4bf…33b4`)
- `A.1.10.4.1.2.3.3.2.2` renumbered (UUID stable: `c5850a58…5001`)
- `A.1.10.4.1.2.3.3.2` renumbered (UUID stable: `07d43b8c…922a`)
- `A.1.10.4.1.2.3.3` renumbered (UUID stable: `6d04b42a…ee78`)
- `A.1.10.4.1.2.3` renumbered (UUID stable: `2cf3dc2e…a29c`)
- `A.1.10.4.1.2` renumbered (UUID stable: `56593663…a14a`)
- `A.1.10.4.1.3.1` renumbered (UUID stable: `b71e1dec…4086`)
- `A.1.10.4.1.3.2` renumbered (UUID stable: `1c0d2cf1…612c`)
- `A.1.10.4.1.3.3.1.1.1` renumbered (UUID stable: `3f9645b2…218c`)
- `A.1.10.4.1.3.3.1.1.2` renumbered (UUID stable: `542e7e15…a9b9`)
- `A.1.10.4.1.3.3.1.1.3` renumbered (UUID stable: `22d693e8…ee43`)
- `A.1.10.4.1.3.3.1.1.4` renumbered (UUID stable: `8596233b…393f`)
- `A.1.10.4.1.3.3.1.1.5` renumbered (UUID stable: `8514341b…c67c`)
- `A.1.10.4.1.3.3.1.1` renumbered (UUID stable: `0b1162f6…3e7c`)
- `A.1.10.4.1.3.3.2.1` renumbered (UUID stable: `49041287…d2f8`)
- `A.1.10.4.1.3.3.2.2` renumbered (UUID stable: `6d550b28…85a6`)
- `A.1.10.4.1.3.3.2.3` renumbered (UUID stable: `186450c7…5b13`)
- `A.1.10.4.1.3.3.2` renumbered (UUID stable: `2fb5eb69…fe83`)
- `A.1.10.4.1.3.3.3.1.1` renumbered (UUID stable: `a9f87e05…e95d`)
- `A.1.10.4.1.3.3.3.1.2` renumbered (UUID stable: `2c6b25de…f601`)
- `A.1.10.4.1.3.3.3.1` renumbered (UUID stable: `3a3bcbb1…022a`)
- `A.1.10.4.1.3.3.3.2.1` renumbered (UUID stable: `ae25a37a…578e`)
- `A.1.10.4.1.3.3.3.2.2` renumbered (UUID stable: `d1a78b46…3e56`)
- `A.1.10.4.1.3.3.3.2` renumbered (UUID stable: `6a24fd94…5980`)
- `A.1.10.4.1.3.3.3` renumbered (UUID stable: `483d9616…3de4`)
- `A.1.10.4.1.3.3` renumbered (UUID stable: `413852e0…c482`)
- `A.1.10.4.1.3` renumbered (UUID stable: `6b0eaa0d…453b`)
- `A.1.10.4.1.4.1` renumbered (UUID stable: `b8241202…2e50`)
- `A.1.10.4.1.4.2` renumbered (UUID stable: `44af823e…bf7b`)
- `A.1.10.4.1.4.3.1.1.1` renumbered (UUID stable: `88cb9621…beda`)
- `A.1.10.4.1.4.3.1.1.2` renumbered (UUID stable: `cb8707d5…a81c`)
- `A.1.10.4.1.4.3.1.1.3` renumbered (UUID stable: `f9cd34cb…4f66`)
- `A.1.10.4.1.4.3.1.1.4` renumbered (UUID stable: `5b79ed95…3e32`)
- `A.1.10.4.1.4.3.1.1.5` renumbered (UUID stable: `a8be9d0a…5b16`)
- `A.1.10.4.1.4.3.1.1` renumbered (UUID stable: `f833edaa…0b10`)
- `A.1.10.4.1.4.3.2.1` renumbered (UUID stable: `7b6ca79a…518f`)
- `A.1.10.4.1.4.3.2.2` renumbered (UUID stable: `527a2195…97b9`)
- `A.1.10.4.1.4.3.2.3` renumbered (UUID stable: `5c722eb6…a007`)
- `A.1.10.4.1.4.3.2` renumbered (UUID stable: `cc4b7dac…2d88`)
- `A.1.10.4.1.4.3.3.1.1` renumbered (UUID stable: `07c605cc…3f4b`)
- `A.1.10.4.1.4.3.3.1.2` renumbered (UUID stable: `ccdc870c…f7af`)
- `A.1.10.4.1.4.3.3.1` renumbered (UUID stable: `658d9408…cd45`)
- `A.1.10.4.1.4.3.3.2.1` renumbered (UUID stable: `b314c96f…8a0c`)
- `A.1.10.4.1.4.3.3.2.2` renumbered (UUID stable: `8b278dd8…0680`)
- `A.1.10.4.1.4.3.3.2` renumbered (UUID stable: `6aea3973…4357`)
- `A.1.10.4.1.4.3.3` renumbered (UUID stable: `84e98241…f72e`)
- `A.1.10.4.1.4.3` renumbered (UUID stable: `0b2674c5…5214`)
- `A.1.10.4.1.4` renumbered (UUID stable: `aca54441…02fa`)
- `A.1.10.4.1` renumbered (UUID stable: `bd68f60c…6f2f`)
- `A.1.10.4.2.1.0.3.1` renumbered (UUID stable: `1844a8bf…17bb`)
- `A.1.10.4.2.1.1.0.3.1` renumbered (UUID stable: `d373ebcb…bf05`)
- `A.1.10.4.2.1.1.0.4.1` renumbered (UUID stable: `71898c9e…dd0c`)
- `A.1.10.4.2.1.1` renumbered (UUID stable: `95dd3a55…5d36`)
- `A.1.10.4.2.1.2` renumbered (UUID stable: `0c71e677…c076`)
- `A.1.10.4.2.1.3` renumbered (UUID stable: `526a954b…1d5e`)
- `A.1.10.4.2.1.4` renumbered (UUID stable: `d8e0d76b…c880`)
- `A.1.10.4.2.1.5` renumbered (UUID stable: `13ad3a13…049a`)
- `A.1.10.4.2.1` renumbered (UUID stable: `df709091…d326`)
- `A.1.10.4.2` renumbered (UUID stable: `fe525e67…7f77`)
- `A.1.10.4` renumbered (UUID stable: `19222532…c247`)
- `A.1.10.5.1` renumbered (UUID stable: `b28a2439…d3a0`)
- `A.1.10.5.2.1.1` renumbered (UUID stable: `646ed712…f325`)
- `A.1.10.5.2.1` renumbered (UUID stable: `022b27ab…cc48`)
- `A.1.10.5.2.2.1.1` renumbered (UUID stable: `d84fd214…cacc`)
- `A.1.10.5.2.2.1.2` renumbered (UUID stable: `dedab114…eeb4`)
- `A.1.10.5.2.2.1.3` renumbered (UUID stable: `7c763597…17e4`)
- `A.1.10.5.2.2.1` renumbered (UUID stable: `8b1f9d33…4af6`)
- `A.1.10.5.2.2.2.1` renumbered (UUID stable: `844d0f55…73b3`)
- `A.1.10.5.2.2.2.2` renumbered (UUID stable: `d51e41f6…ca9c`)
- `A.1.10.5.2.2.2` renumbered (UUID stable: `2f9fb16b…261e`)
- `A.1.10.5.2.2.3.1` renumbered (UUID stable: `8b4f7c2e…fe3a`)
- `A.1.10.5.2.2.3.2` renumbered (UUID stable: `f5587483…6275`)
- `A.1.10.5.2.2.3.3` renumbered (UUID stable: `4cc57ff9…87a6`)
- `A.1.10.5.2.2.3` renumbered (UUID stable: `a43090f2…6529`)
- `A.1.10.5.2.2.4.1` renumbered (UUID stable: `06f796a3…2a8d`)
- `A.1.10.5.2.2.4.2` renumbered (UUID stable: `7a151ea1…bbf9`)
- `A.1.10.5.2.2.4` renumbered (UUID stable: `ea6670a4…db11`)
- `A.1.10.5.2.2` renumbered (UUID stable: `bd8bf8d3…1cba`)
- `A.1.10.5.2.3.1` renumbered (UUID stable: `50d68397…0fd7`)
- `A.1.10.5.2.3.2.1.1` renumbered (UUID stable: `4cf98145…7f4a`)
- `A.1.10.5.2.3.2.2` renumbered (UUID stable: `387fa314…4f7e`)
- `A.1.10.5.2.3.2` renumbered (UUID stable: `832b2591…4e07`)
- `A.1.10.5.2.3.3.1` renumbered (UUID stable: `0567fc4c…4f15`)
- `A.1.10.5.2.3.3` renumbered (UUID stable: `53cea69b…7deb`)
- `A.1.10.5.2.3` renumbered (UUID stable: `eeaaa751…e3bb`)
- `A.1.10.5.2.4` renumbered (UUID stable: `1ac0d0c7…cb38`)
- `A.1.10.5.2` renumbered (UUID stable: `5e40b575…b35d`)
- `A.1.10.5.3.1.1.1` renumbered (UUID stable: `583c1a98…daf6`)
- `A.1.10.5.3.1.1.2` renumbered (UUID stable: `44bb2b0d…34b7`)
- `A.1.10.5.3.1.1` renumbered (UUID stable: `4f5e346e…021c`)
- `A.1.10.5.3.1.2.1` renumbered (UUID stable: `e4e3c3d9…e7d6`)
- `A.1.10.5.3.1.2.2` renumbered (UUID stable: `6022623f…a9da`)
- `A.1.10.5.3.1.2` renumbered (UUID stable: `540d277c…83ba`)
- `A.1.10.5.3.1.3.1` renumbered (UUID stable: `4ff6766c…8d92`)
- `A.1.10.5.3.1.3.2` renumbered (UUID stable: `29e06433…29f0`)
- `A.1.10.5.3.1.3.3` renumbered (UUID stable: `559f640c…2d03`)
- `A.1.10.5.3.1.3.4` renumbered (UUID stable: `da310ed1…f092`)
- `A.1.10.5.3.1.3.5` renumbered (UUID stable: `4a154956…87a7`)
- `A.1.10.5.3.1.3` renumbered (UUID stable: `55195cdc…0ed8`)
- `A.1.10.5.3.1` renumbered (UUID stable: `152e5205…3542`)
- `A.1.10.5.3.2.1` renumbered (UUID stable: `afa90735…e06f`)
- `A.1.10.5.3.2.2.1.1` renumbered (UUID stable: `a15e7cd9…2d05`)
- `A.1.10.5.3.2.2.1.2` renumbered (UUID stable: `5bf1e3b0…5960`)
- `A.1.10.5.3.2.2` renumbered (UUID stable: `62d53156…defd`)
- `A.1.10.5.3.2.3.1` renumbered (UUID stable: `5bff38dc…e60a`)
- `A.1.10.5.3.2.3` renumbered (UUID stable: `0cec9b17…7d52`)
- `A.1.10.5.3.2` renumbered (UUID stable: `69da8af1…5253`)
- `A.1.10.5.3.3` renumbered (UUID stable: `fd63dc4d…b68e`)
- `A.1.10.5.3` renumbered (UUID stable: `13cdbb75…dbe6`)
- `A.1.10.5` renumbered (UUID stable: `b8266c11…4ffd`)
- `A.1.11.1.0.3.1` renumbered (UUID stable: `fa682e4f…87d8`)
- `A.1.11.1.2.1` renumbered (UUID stable: `cae731e3…cb79`)
- `A.1.11.1.2.2` renumbered (UUID stable: `8bde129a…1aa3`)
- `A.1.11.1.3.0.3.1` renumbered (UUID stable: `52aef6ac…ca31`)
- `A.1.11.1.3.0.3.2` renumbered (UUID stable: `afe57048…f442`)
- `A.1.11.1.3.0.3.3` renumbered (UUID stable: `830b65d8…7bbb`)
- `A.1.11.1.3` renumbered (UUID stable: `22508894…6d31`)
- `A.1.11.1.4.1` renumbered (UUID stable: `de178e9a…9f2c`)
- `A.1.11.1.4.2` renumbered (UUID stable: `1b54a173…f506`)
- `A.1.11.1.4.3` renumbered (UUID stable: `1e89af32…8c1f`)
- `A.1.11.1.4.4.0.4.1` renumbered (UUID stable: `ef10f4bb…4db7`)
- `A.1.11.1.4.4` renumbered (UUID stable: `b0b1243a…1ccd`)
- `A.1.11.1.4` renumbered (UUID stable: `ad4fc5d1…98b8`)
- `A.1.11.1.5.1.1` renumbered (UUID stable: `7648bf12…0f4f`)
- `A.1.11.1.5.1.2` renumbered (UUID stable: `2d165c27…03d2`)
- `A.1.11.1.5.1` renumbered (UUID stable: `0d0e2e1a…19ec`)
- `A.1.11.1.5` renumbered (UUID stable: `2ef63f36…1afb`)
- `A.1.11.2.1.1.0.4.1` renumbered (UUID stable: `8139e05f…a1b5`)
- `A.1.11.2.1.3.0.4.1.1.1` renumbered (UUID stable: `9079bf46…3acb`)
- `A.1.11.2.1.3.0.4.1` renumbered (UUID stable: `fa3e83ff…d8f4`)
- `A.1.11.2.1.3.0.4.2.1.1` renumbered (UUID stable: `1ebcda5d…cc56`)
- `A.1.11.2.1.3.0.4.2` renumbered (UUID stable: `bba7fb85…e488`)
- `A.1.11.2.3.0.4.1` renumbered (UUID stable: `824e78be…7665`)
- `A.1.12.2.0.4.1` renumbered (UUID stable: `b1ffdef7…3761`)
- `A.1.12.2.1.4` renumbered (UUID stable: `45ced7a3…260a`)
- `A.1.12.2.1.5` renumbered (UUID stable: `8c1f48d7…c155`)
- `A.1.12.2.1.6` renumbered (UUID stable: `ffd09668…67eb`)
- `A.1.12.2.1.7.1` renumbered (UUID stable: `51dc4c3b…f1ce`)
- `A.1.12.2.1.7.2.0.4.1` renumbered (UUID stable: `523bfc8f…4fd6`)
- `A.1.12.2.1.7.2` renumbered (UUID stable: `90932951…4da6`)
- `A.1.12.2.1.7.3` renumbered (UUID stable: `9949588a…2895`)
- `A.1.12.2.1.7` renumbered (UUID stable: `7ba721b9…19b4`)
- `A.1.12.2.1.8` renumbered (UUID stable: `e00795ef…44bc`)
- `A.1.12.2.1.9` renumbered (UUID stable: `6402ac15…c2e5`)
- `A.1.12.2.2.1` renumbered (UUID stable: `16e06904…177b`)
- `A.1.12.2.2.2` renumbered (UUID stable: `b9da67b6…fa64`)
- `A.1.12.2.6.1.0.4.1` renumbered (UUID stable: `b1887e4a…885d`)
- `A.1.12.2.6.1` renumbered (UUID stable: `535570e7…3978`)
- `A.1.12.2.6` renumbered (UUID stable: `13e6da57…c82f`)
- `A.1.12.2.7.1` renumbered (UUID stable: `530fe959…66bb`)
- `A.1.12.2.7.2` renumbered (UUID stable: `3a7e2781…10fc`)
- `A.1.12.2.7` renumbered (UUID stable: `8fb17cf7…321f`)
- `A.1.13.1.2.0.3.1` renumbered (UUID stable: `d84b2bbf…1b1e`)
- `A.1.13.1.3.0.3.1` renumbered (UUID stable: `0a8d0081…0e19`)
- `A.1.13.1.3.1.1.0.4.1` renumbered (UUID stable: `a8be1e67…5e71`)
- `A.1.13.1.3.1.1` renumbered (UUID stable: `1604506b…5d1f`)
- `A.1.13.1.3.1` renumbered (UUID stable: `ecce1a73…591a`)
- `A.1.13.1.3.2` renumbered (UUID stable: `cfbfb3a9…8b06`)
- `A.1.14.1.4` renumbered (UUID stable: `178d80c7…1e78`)
- `A.1.14.1.5.4.1` renumbered (UUID stable: `4037c7a7…9c10`)
- `A.1.14.1.5.4` renumbered (UUID stable: `cd9b64bd…31d3`)
- `A.1.14.1.6.1` renumbered (UUID stable: `a9d8aa61…74bb`)
- `A.1.14.1.6.2` renumbered (UUID stable: `a6996fe3…efb5`)
- `A.1.14.1.6.3` renumbered (UUID stable: `e5b96bad…bcb0`)
- `A.1.14.1.6` renumbered (UUID stable: `37c79482…8022`)
- `A.1.14.1.7` renumbered (UUID stable: `26e6229d…45ff`)
- `A.1.14.2.1` renumbered (UUID stable: `e22a06b2…682a`)
- `A.1.14.2.10.1` renumbered (UUID stable: `603b2914…28d4`)
- `A.1.14.2.10.2.1` renumbered (UUID stable: `ec953006…688c`)
- `A.1.14.2.10.2.2` renumbered (UUID stable: `ed93f083…237f`)
- `A.1.14.2.10.2.3` renumbered (UUID stable: `5e737413…d238`)
- `A.1.14.2.10.2.4` renumbered (UUID stable: `453f04da…0319`)
- `A.1.14.2.10.2.5` renumbered (UUID stable: `87a0f80d…caa9`)
- `A.1.14.2.10.2.6` renumbered (UUID stable: `4fe3409f…563d`)
- `A.1.14.2.10.2` renumbered (UUID stable: `e0dd40ef…3eef`)
- `A.1.14.2.10.3` renumbered (UUID stable: `d195ee61…ceaf`)
- `A.1.14.2.10` renumbered (UUID stable: `d4bf73e7…4f78`)
- `A.1.14.2.11.1.1` renumbered (UUID stable: `8dbacc54…8b56`)
- `A.1.14.2.11.1.2` renumbered (UUID stable: `dd76b3fb…1e25`)
- `A.1.14.2.11.1` renumbered (UUID stable: `b1684804…023f`)
- `A.1.14.2.11` renumbered (UUID stable: `3458d1c7…a795`)
- `A.1.14.2.2` renumbered (UUID stable: `afab0e51…5efe`)
- `A.1.14.2.3.1` renumbered (UUID stable: `371a6946…2013`)
- `A.1.14.2.3` renumbered (UUID stable: `32495169…5e8b`)
- `A.1.14.2.4.1.1` renumbered (UUID stable: `54baff0b…c70b`)
- `A.1.14.2.4.1` renumbered (UUID stable: `3d7f42a5…a2f5`)
- `A.1.14.2.4` renumbered (UUID stable: `a132233a…9ad6`)
- `A.1.14.2.5.1.1` renumbered (UUID stable: `5875496e…1389`)
- `A.1.14.2.5.1.2.1` renumbered (UUID stable: `f9f1a5a5…154f`)
- `A.1.14.2.5.1.2.2` renumbered (UUID stable: `f04bd29a…6a60`)
- `A.1.14.2.5.1.2` renumbered (UUID stable: `a689a844…dd27`)
- `A.1.14.2.5.1` renumbered (UUID stable: `b6e391fa…2062`)
- `A.1.14.2.5` renumbered (UUID stable: `d2c31de7…5fee`)
- `A.1.14.2.6.1` renumbered (UUID stable: `fd5f6ac6…5f18`)
- `A.1.14.2.6` renumbered (UUID stable: `39dc8d4c…3009`)
- `A.1.14.2.7.1` renumbered (UUID stable: `dcdc71b3…34d9`)
- `A.1.14.2.7.2.1.1` renumbered (UUID stable: `49f808e6…98f0`)
- `A.1.14.2.7.2.1` renumbered (UUID stable: `5db28264…ce32`)
- `A.1.14.2.7.2` renumbered (UUID stable: `26ec6b08…61a4`)
- `A.1.14.2.7` renumbered (UUID stable: `2be8d2f0…a3b8`)
- `A.1.14.2.8.1` renumbered (UUID stable: `85afc135…b6da`)
- `A.1.14.2.8.2` renumbered (UUID stable: `00ee44e4…b72a`)
- `A.1.14.2.8` renumbered (UUID stable: `7c750981…b86a`)
- `A.1.14.2.9.1` renumbered (UUID stable: `3be71f09…9210`)
- `A.1.14.2.9.2` renumbered (UUID stable: `1405d49c…aeb0`)
- `A.1.14.2.9` renumbered (UUID stable: `45b3a9e8…763f`)
- `A.1.14.2` renumbered (UUID stable: `84f1702d…0b9c`)
- `A.1.14.3.1` renumbered (UUID stable: `6a6c2870…0854`)
- `A.1.14.3.2` renumbered (UUID stable: `cdf12e79…005a`)
- `A.1.14.3.3` renumbered (UUID stable: `946b8318…6d5e`)
- `A.1.14.3.4.1` renumbered (UUID stable: `bc07050a…a9ab`)
- `A.1.14.3.4.2` renumbered (UUID stable: `ca805edd…4a18`)
- `A.1.14.3.4` renumbered (UUID stable: `fdf32ca5…7216`)
- `A.1.14.3` renumbered (UUID stable: `b9afc2bf…f522`)
- `A.1.14.4.1` renumbered (UUID stable: `1b10829a…dfca`)
- `A.1.14.4.2` renumbered (UUID stable: `5dca36a5…e12c`)
- `A.1.14.4.3` renumbered (UUID stable: `8249a5d8…d031`)
- `A.1.14.4.4.1` renumbered (UUID stable: `b8cb6cf9…8adf`)
- `A.1.14.4.4` renumbered (UUID stable: `beb4109c…4268`)
- `A.1.14.4.5` renumbered (UUID stable: `d20d3a11…3665`)
- `A.1.14.4.6.1.1` renumbered (UUID stable: `76405733…a9a2`)
- `A.1.14.4.6.1.2` renumbered (UUID stable: `1b199df8…fad4`)
- `A.1.14.4.6.1` renumbered (UUID stable: `6e4b1649…7d9e`)
- `A.1.14.4.6` renumbered (UUID stable: `a878427f…f419`)
- `A.1.14.4.7.1` renumbered (UUID stable: `2dc20bcf…40e1`)
- `A.1.14.4.7.2` renumbered (UUID stable: `334c2821…e933`)
- `A.1.14.4.7.3` renumbered (UUID stable: `fed006c3…7ccb`)
- `A.1.14.4.7` renumbered (UUID stable: `4fce0fd5…17a6`)
- `A.1.14.4` renumbered (UUID stable: `79a69869…b887`)
- `A.1.14.5.2.1` renumbered (UUID stable: `d28f48be…e5ae`)
- `A.1.14.5.2` renumbered (UUID stable: `28b90058…97cc`)
- `A.1.14.5` renumbered (UUID stable: `fe833d0e…64a8`)
- `A.1.5.10.1` renumbered (UUID stable: `9c05207d…6ef9`)
- `A.1.5.10.2.0.6.1` renumbered (UUID stable: `e7aec672…2eb7`)
- `A.1.5.10.2` renumbered (UUID stable: `15def023…02f6`)
- `A.1.5.3.0.3.2` renumbered (UUID stable: `a9ad7689…5082`)
- `A.1.5.3.0.3.3` renumbered (UUID stable: `5ecf688c…31d1`)
- `A.1.5.3.0.3.4` renumbered (UUID stable: `ac81d874…59d8`)
- `A.1.5.3.0.3.5` renumbered (UUID stable: `666f3928…c354`)
- `A.1.5.3.0.3.6` renumbered (UUID stable: `21ec2c20…7531`)
- `A.1.5.3.0.4.1` renumbered (UUID stable: `61420b37…3547`)
- `A.1.5.4.0.4.1` renumbered (UUID stable: `8dfd71fc…5b55`)
- `A.1.5.5.0.3.1` renumbered (UUID stable: `8d706ce8…3feb`)
- `A.1.5.5.0.4.1.1.1` renumbered (UUID stable: `d5e82bc9…3c19`)
- `A.1.5.5.0.4.1.1.1.var1` renumbered (UUID stable: `b7eb5043…cf9e`)
- `A.1.5.5.0.4.1.1.2` renumbered (UUID stable: `01e5369d…eaee`)
- `A.1.5.5.0.4.1.1.2.var1` renumbered (UUID stable: `1b2b438f…25eb`)
- `A.1.5.5.0.4.1.1.3` renumbered (UUID stable: `5754dde6…2ca6`)
- `A.1.5.5.0.4.1.1.3.var1` renumbered (UUID stable: `b13b099c…33a0`)
- `A.1.5.5.0.4.1.1.4` renumbered (UUID stable: `6ebff450…af44`)
- `A.1.5.5.0.4.1` renumbered (UUID stable: `38c70e00…cb25`)
- `A.1.5.5.0.4.2` renumbered (UUID stable: `56fd4055…4181`)
- `A.1.5.5.0.4.3` renumbered (UUID stable: `9b3828a7…a1ca`)
- `A.1.5.5.1` renumbered (UUID stable: `6aa88317…c767`)
- `A.1.5.7.0.4.1` renumbered (UUID stable: `598ff9cf…90a1`)
- `A.1.5.7.1` renumbered (UUID stable: `cb2ae821…c5b5`)
- `A.1.5.8.0.3.1` renumbered (UUID stable: `13c4f127…1bdd`)
- `A.1.5.8.0.4.2` renumbered (UUID stable: `364aaf22…dc5b`)
- `A.1.5.9.0.4.1` renumbered (UUID stable: `8d8980b8…3198`)
- `A.1.5.9.0.4.2` renumbered (UUID stable: `3b516fa0…858c`)
- `A.1.5.9.1.0.4.1` renumbered (UUID stable: `ef3b30b9…f973`)
- `A.1.5.9.1` renumbered (UUID stable: `4217002f…fff9`)
- `A.1.5.9.2.1` renumbered (UUID stable: `9927fb45…66cb`)
- `A.1.5.9.2.2.0.3.1` renumbered (UUID stable: `c5bb1fc6…37c2`)
- `A.1.5.9.2.2.0.4.1` renumbered (UUID stable: `d7201212…0af2`)
- `A.1.5.9.2.2` renumbered (UUID stable: `12044fd7…c6dd`)
- `A.1.5.9.2` renumbered (UUID stable: `fad2c7d1…78da`)
- `A.1.5.9.3.0.4.1` renumbered (UUID stable: `f6f61fd9…5376`)
- `A.1.5.9.3` renumbered (UUID stable: `8d8dfab8…6005`)
- `A.1.5.9.4` renumbered (UUID stable: `1fd1ecc3…3514`)
- `A.1.5.9.5` renumbered (UUID stable: `6f492c50…7d88`)
- `A.1.6.1.2` renumbered (UUID stable: `e5117ac9…b192`)
- `A.1.6.1.3.1.0.3.1` renumbered (UUID stable: `e4e33492…8578`)
- `A.1.6.1.3.1.0.3.2` renumbered (UUID stable: `68f465e6…896c`)
- `A.1.6.1.3.1` renumbered (UUID stable: `eeb4c881…873a`)
- `A.1.6.1.3.2.0.3.1` renumbered (UUID stable: `5105cf0b…caf7`)
- `A.1.6.1.3.2.1` renumbered (UUID stable: `01bed493…336c`)
- `A.1.6.1.3.2.2` renumbered (UUID stable: `34cb5468…2af8`)
- `A.1.6.1.3.2` renumbered (UUID stable: `83289ee2…9e9f`)
- `A.1.6.1.3.3` renumbered (UUID stable: `a1eeced2…55cc`)
- `A.1.6.1.3` renumbered (UUID stable: `07e63bc3…cc11`)
- `A.1.6.1.4.1` renumbered (UUID stable: `3a9bb8d7…5b33`)
- `A.1.6.1.4` renumbered (UUID stable: `66183cd4…6cf6`)
- `A.1.6.1.5.0.6.1` renumbered (UUID stable: `5f584db8…ceb7`)
- `A.1.6.1.5` renumbered (UUID stable: `79e4e209…c680`)
- `A.1.6.2.1.1` renumbered (UUID stable: `0e1c91a9…1211`)
- `A.1.6.2.1` renumbered (UUID stable: `8c813d3d…aead`)
- `A.1.6.2.2` renumbered (UUID stable: `3a8c2b92…bd98`)
- `A.1.6.4.1.1.1` renumbered (UUID stable: `1c2ba550…c878`)
- `A.1.6.4.1.1.2` renumbered (UUID stable: `036babd9…e58e`)
- `A.1.6.4.1.1.3.1` renumbered (UUID stable: `46c0f334…6e2a`)
- `A.1.6.4.1.1.3` renumbered (UUID stable: `f52e46d4…aadc`)
- `A.1.6.4.1.1` renumbered (UUID stable: `cf96f0e7…495d`)
- `A.1.6.4.1.2.1` renumbered (UUID stable: `dc65cc80…817e`)
- `A.1.6.4.1.2.2` renumbered (UUID stable: `04b54378…404d`)
- `A.1.6.4.1.2.3.1` renumbered (UUID stable: `ebe4da3b…fe75`)
- `A.1.6.4.1.2.3` renumbered (UUID stable: `7c6c6579…84fd`)
- `A.1.6.4.1.2` renumbered (UUID stable: `2f07e41b…7823`)
- `A.1.6.4.1.3.1` renumbered (UUID stable: `8833de34…43fc`)
- `A.1.6.4.1.3.2` renumbered (UUID stable: `c51b75e1…af0d`)
- `A.1.6.4.1.3.3.0.3.1` renumbered (UUID stable: `8012ae3b…a7ca`)
- `A.1.6.4.1.3.3` renumbered (UUID stable: `c3ad0b9f…a8ab`)
- `A.1.6.4.1.3` renumbered (UUID stable: `8b4d704c…bb6a`)
- `A.1.6.4.1` renumbered (UUID stable: `f4857d86…0129`)
- `A.1.6.4.2` renumbered (UUID stable: `e16ac70b…b5e0`)
- `A.1.6.4.3.1.0.3.1` renumbered (UUID stable: `57a0be8f…5058`)
- `A.1.6.4.3.1` renumbered (UUID stable: `ad1ef0f4…8ccf`)
- `A.1.6.4.3.2.0.3.1` renumbered (UUID stable: `57c35484…213a`)
- `A.1.6.4.3.2.0.3.2` renumbered (UUID stable: `ca88baad…9e78`)
- `A.1.6.4.3.2` renumbered (UUID stable: `f020d1bc…ec79`)
- `A.1.6.4.3.3.1` renumbered (UUID stable: `21d0b626…276d`)
- `A.1.6.4.3.3` renumbered (UUID stable: `43db9780…0787`)
- `A.1.6.4.3` renumbered (UUID stable: `82f74f4b…3394`)
- `A.1.6.4.4.1.0.3.1` renumbered (UUID stable: `48a2c0f5…b901`)
- `A.1.6.4.4.1` renumbered (UUID stable: `688247c6…89eb`)
- `A.1.6.4.4.2.1.1.0.3.1` renumbered (UUID stable: `5de71fff…a85b`)
- `A.1.6.4.4.2.1.1` renumbered (UUID stable: `2c2b201e…6a4f`)
- `A.1.6.4.4.2.1` renumbered (UUID stable: `8eca5ff8…f213`)
- `A.1.6.4.4.2` renumbered (UUID stable: `add0e307…2e01`)
- `A.1.6.4.4.3` renumbered (UUID stable: `4a29dd32…3453`)
- `A.1.6.4.4` renumbered (UUID stable: `0625cdd6…4951`)
- `A.1.6.4.5` renumbered (UUID stable: `5417359f…7a7f`)
- `A.1.6.6.0.3.1` renumbered (UUID stable: `3a9d0848…db71`)
- `A.1.6.6.0.3.2` renumbered (UUID stable: `578ff359…8c10`)
- `A.1.6.6.1.1` renumbered (UUID stable: `ec29c919…2539`)
- `A.1.6.6.1.2.0.3.1` renumbered (UUID stable: `3cd0735f…d7ac`)
- `A.1.6.6.1.2` renumbered (UUID stable: `a95e4ab0…6b75`)
- `A.1.6.6.1.3.0.6.1` renumbered (UUID stable: `1ddd9cf6…1ffb`)
- `A.1.6.6.1.3` renumbered (UUID stable: `32862df8…1dfd`)
- `A.1.6.6.1` renumbered (UUID stable: `2544a530…635e`)
- `A.1.6.6.2` renumbered (UUID stable: `c1a5d22a…8d28`)
- `A.1.7.4.0.4.1` renumbered (UUID stable: `b8601ee2…936b`)
- `A.1.7.7.0.3.1` renumbered (UUID stable: `4fbdf196…4580`)
- `A.1.7.7.0.3.2` renumbered (UUID stable: `260f1bd6…cceb`)
- `A.1.7.7.0.3.3` renumbered (UUID stable: `88bd0a0b…3daf`)
- `A.1.7.7.0.3.4` renumbered (UUID stable: `66d51a72…8272`)
- `A.1.7.8.0.3.1` renumbered (UUID stable: `ce5d86d8…61a6`)
- `A.1.8.1.1.1` renumbered (UUID stable: `3448e169…6b50`)
- `A.1.8.1.1.2.1` renumbered (UUID stable: `a4ff45b4…7450`)
- `A.1.8.1.1.2` renumbered (UUID stable: `51b1fe46…f729`)
- `A.1.9.1.2.2.0.6.1` renumbered (UUID stable: `e9807449…1618`)
- `A.1.9.1.2.3.1` renumbered (UUID stable: `b41dc314…1a77`)
- `A.1.9.1.2.3` renumbered (UUID stable: `c56e96cc…660a`)
- `A.1.9.1.2.4` renumbered (UUID stable: `d77ed6ca…f8d8`)
- `A.1.9.1.3.1` renumbered (UUID stable: `45a7ccff…17cf`)
- `A.1.9.1.3.2.1` renumbered (UUID stable: `7baa8295…1365`)
- `A.1.9.1.3.2.2` renumbered (UUID stable: `57006d4e…94d5`)
- `A.1.9.1.3.2.3` renumbered (UUID stable: `0b6f25c1…826e`)
- `A.1.9.1.3.2.4` renumbered (UUID stable: `4627de70…9a45`)
- `A.1.9.1.3.2` renumbered (UUID stable: `3efb0238…1394`)
- `A.1.9.1.3` renumbered (UUID stable: `18418289…c866`)
- `A.1.9.1.4.1` renumbered (UUID stable: `f1587c7c…c316`)
- `A.1.9.1.4` renumbered (UUID stable: `c9c32f24…032b`)
- `A.1.9.1.5.1` renumbered (UUID stable: `97020aa2…3618`)
- `A.1.9.1.5.2` renumbered (UUID stable: `f3a647b2…cc16`)
- `A.1.9.1.5.3` renumbered (UUID stable: `34a3d273…fad5`)
- `A.1.9.1.5.4.1` renumbered (UUID stable: `3f5f79fa…aa48`)
- `A.1.9.1.5.4` renumbered (UUID stable: `e46bca7a…9709`)
- `A.1.9.1.5.5` renumbered (UUID stable: `8ce1adeb…fece`)
- `A.1.9.1.5.6` renumbered (UUID stable: `ddab726d…d1ed`)
- `A.1.9.1.5` renumbered (UUID stable: `498e151e…b861`)
- `A.1.9.1.6.1` renumbered (UUID stable: `665b3bc4…fe67`)
- `A.1.9.1.6.2` renumbered (UUID stable: `2ce9cd30…b513`)
- `A.1.9.1.6` renumbered (UUID stable: `8df982ee…6cf8`)
- `9` → `10` across 480 docs.
- `spells` → `Spells` across 8 docs.
- `spell` → `Spell` across 57 docs.
- `Facilitators` → `Facilitator` across 14 docs.
- `8` → `9` across 39 docs.
- `10` → `11` across 27 docs.
- `11` → `12` across 23 docs.
- `Monthly` → `Weekly` across 3 docs.
- `12` → `13` across 6 docs.
- `13` → `14` across 74 docs.
- `4` → `5` across 41 docs.
- `6` → `7` across 7 docs.
- `5` → `6` across 61 docs.
- `7` → `8` across 3 docs.

### Context
Major restructure authorized by Poll #1632 (Yes 8 / Abstain 1). Introduces the Synome Documents framework with a Synome Editor role (A.1.3.1–A.1.3.2), reorganizes the weekly/monthly Atlas Edit cycle definitions (A.1.10–A.1.12), codifies the four-week Prime Spell Process by which Prime Agents land actions in Sky Core Spells (A.1.10.2.3.2.2.3), and removes the deprecated Spell Validation subtree under A.1.9.2 in favor of the new structure.

---

## PR #239 — update bridge rate limits after spell
**Merged:** 2026-05-15 | **Type:** Housekeeping

### Material Changes
- **Rate Limit** (`A.1.10.4.1.2.3.2.2`): `10` → `5`
- **USDS Rate Limit** (`A.1.10.4.1.3.3.2.2`): `5,000,000` → `0`

---

## PR #237 — Atlas Edit Proposal — 2026-05-04
**Merged:** 2026-05-08 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- **"Governance Facilitators" → "Core Council"/"Core Facilitator" across SparkLend Security Access Multisig docs**:
  - `A.1.9.4.2.1.1` (SparkLend Multisig Usage Standards): "Governance Facilitators must ensure…" → "Core Council must ensure…"
  - `A.1.9.4.2.1.1.0.4.1` (Action Tenet, UUID `71898c9e…2bdd0c`): renamed "Facilitators Must Exercise Due Caution…" → "Core Council Must Exercise Due Caution…"; body references updated
  - `A.1.9.4.2.1.4` (SparkLend Multisig Signer Modifications): "Governance Facilitators should consider preparing an expedited Executive Vote…" → "Core Facilitator should consider…"

### Context
Terminology cleanup completing the September 2025 transition from Governance Facilitators to the Core Council/Core Facilitator model (see PR #59) — these SparkLend Security Access Multisig docs were missed by the original sweep. Ratified by Poll #1631 (10-0, non-voters: excel, opex, tango).

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

## PR #217 — Atlas Edit Proposal — 2026-03-30
**Merged:** 2026-04-02 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Emergency Response & Spell framework migrated to the Agent Framework**: across the Emergency Response Article (`A.1.8`) and Emergency Spells / Protego (`A.1.9.5`), authority was reassigned from the legacy "Support Scope Facilitators" / "Governance Facilitators" to the **Core Facilitator** (decision authority) and **Core GovOps** (authenticity validation). "Facilitators' Roles And Responsibilities" → "Emergency Response Roles And Responsibilities" (`A.1.8.1.4`); new `A.1.9.5.2.3.1` "The Core Facilitator Role In Standby Spells"; "Support Facilitators'/Governance Facilitators' Role" docs across Standby Spells and Protego usage renamed to Core Facilitator / Core GovOps.
- **Demand Side Buffer established** as a standalone account (in the `A.2.2.8` stablecoin-primitives scope) — becomes the funding source for Keel's Pioneer Incentive Pool (see keel changelog).

### Context
Part of the broad Facilitators → Core Facilitator / Core GovOps role consolidation under the Agent Framework. The same PR renamed Keel's operating company (Matariki Labs → Elodin) and restructured its incentive pool — see `../A.6--agents/A.6.1.1.3--keel/changelog.md`. (The Demand Side Buffer change technically sits in the A.2 support scope and is noted here only for its link to the emergency/agent-framework rework; a dedicated support-scope entry is a follow-up.)

---

## PR #213 — Update Sky forum URL
**Merged:** 2026-04-02 | **Type:** Housekeeping

`forum.sky.money` → `forum.skyeco.com` across multiple A.1 documents: AD derecognition annotation (`A.1.4.10` area), all 10 derecognised AD entries in the Derecognized Conservers registry (`A.1.4.10` Active Data table), and all 13 current AD entries in the AD Roster (`A.1.5.1.5` Active Data table).

---

## PR #208 — Atlas Edit Proposal — 2026-03-23
**Merged:** 2026-03-27 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Emergency Declaration Procedure** (`A.1.8.1.5.5`): Authority to declare an emergency shifted from "Support Facilitators" to "Core Facilitator" (singular). Obligation to post on Sky Forum and discretion over public declarations now attributed to Core Facilitator. The optional clause "Creating a signal request thread or Governance Poll is optional" removed.
- **Spell post-execution step** (`A.1.9.2.4.13.5` → new `A.1.9.2.4.13.5`): New Core document added — "Facilitator Updates Atlas To Reflect Spell Outcome". Core Facilitator is responsible for updating Sky Core Atlas documents after a spell executes; Operational Facilitator of the affected Agent handles Artifact follow-ups. All existing retrospective/follow-up sub-documents renumbered `.13.5.*` → `.13.6.*` accordingly.
- **Non-Standard Weekly Poll** (`A.1.10.1.2.2`): Definition of Non-Standard Weekly Poll removed; former `A.1.10.1.2.3` (Executive Vote definition) renumbered to `A.1.10.1.2.2`.
- **Use of Non-standard Weekly Poll** (`A.1.10.1.5`): Section "Use Of Non-Standard Weekly Poll" (former `.1.5`) removed. Former `A.1.10.1.6` ("Core Facilitators' Authority To Create Proposals") renumbered to `A.1.10.1.5`; housekeeping-item sub-docs renumbered from `.1.6.1.*` to `.1.5.1.*`.
- **Signal Requests** (`A.1.10.1.7`): "Signal Requests" section removed — Signal Requests are now entirely prohibited except where specifically triggered and required by the Atlas (this restriction was the entire content; removing the section eliminates the permissive framing).
- **Bootstrapping poll terminology**: `Facilitators' Bootstrapping Poll` → `Bootstrapping Governance Poll` in two documents (`A.1.12.1.2`, `A.1.12.1.3`).
- **Chainlog cross-reference** (`A.1.9.1.2`): Internal link to housekeeping items updated from `A.1.10.1.6.1.1`/`A.1.10.1.6.1.2` to `A.1.10.1.5.1.1`/`A.1.10.1.5.1.2` (renumbering consequence).

### Housekeeping
- SparkLend Risk Parameters Modification (`A.6.1.1.1.3.2.1.2.1`): Stability Facilitators removed from recommendation authority; "Core Council Risk Advisor, in consultation with Phoenix Labs" now the sole recommender. The two exceptions requiring a Governance Poll before Executive Vote (Liquidation Threshold and Liquidation Bonus) removed — all SparkLend parameter changes now follow the general Operational Weekly Cycle rule.

---

## PR #196 — March 9 edit
**Merged:** 2026-03-12 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **AC breach annotation ordering** (`A.1.5.6.0.3.1`, `.0.3.2`): "Credible Evidence" and "Act Swiftly" element annotations swapped positions (numbers exchanged, UUIDs travel with content — content is now correctly ordered).
- **Facilitators' Authority to Raise Formal Allegation** (`A.1.5.6.0.4.1`): whitespace normalization (double-space before "Upon receiving" removed; content unchanged).
- **Solana LayerZero Freezer Multisig Signers/Modification** (`A.1.9.4.1.3.1.2.3`, `.2.5`): "Keel" → "Operational Facilitator Endgame Edge" as co-signer authority (follow-on to PR #180's Soter Labs change).

===DEST: A.2--support===

---

## PR #196 — March 9 edit
**Merged:** 2026-03-12 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **SKY Buybacks allocation** (`A.2.3.1.4.2.1`): 300,000 USDS/day → **37,600 USDS/day** of Step 4 Capital.
- **Safe Harbor agreement address** (`A.2.11.1.2.1`, `.1.2.2.2`): `0x9E5Cf4a9C806fE1F4392788b21342a442E14Cc20` → **`0xf17bB418B4EC251f300Aa3517Cb37349f17697A1`**.
- **Safe Harbor protocol name** (`A.2.11.1.2.2.3.5`): "Sky Ecosystem" → "Sky."
- **RRC Dashboard** (`A.2.2.9.1.1.3.2.1.1`): "Dashboard And API" → "Dashboard"; URL updated to `https://info.sky.money/required-risk-capital` (removes Blockanalitica sphere-api endpoint).

### Housekeeping
- RRC Dashboard section titles updated throughout (`A.2.2.9.1.1.3.2.1.1.1`, `.1.2`); markdown list formatting normalized.

===DEST: A.4--protocol===

---

## PR #196 — March 9 edit
**Merged:** 2026-03-12 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Source of SKY Rewards** (`A.4.4.1.4.2.2`): vesting stream can now be funded by "SKY acquired through buybacks **or SKY reserves**" (previously buybacks only).

---

## PR #187 — 2026-02-23 Atlas Edit Weekly Cycle Proposal
**Merged:** 2026-03-05 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Ranked Delegate Budget annotation** (`A.1.5.4.3.1.0.3.1`): copy-paste error corrected — voting-activity and voting-communication annotation bodies had each other's text; now correct.
- **AD Buffer payout limitation** (`A.1.5.4.4.2.1`): reference to "Atlas Edit Weekly Cycle Proposal" expanded to include "or Atlas Edit Monthly Cycle Proposal."
- **One Month's Budget Allocation annotation** (`A.1.5.4.4.1.0.3.1`): new annotation added (`UUID: 48a2c0f5…`); duplicate header `A.1.5.4.4.1.1` removed (same UUID, now only one reference).
- **Solana LayerZero Freezer Multisig** (`A.1.9.4.1.3.1.2.3`, `.2.5`): signer authority updated from "Amatsu and Keel" → "Operational GovOps Soter Labs and Keel."
- **Responsibility to Maintain Agent Artifact** (`A.1.13.2.10.1`): reformatted from `◦` bullets to standard `- ` markdown bullets; A.2.2 cross-reference updated from URL to UUID link.

### Housekeeping
- `A.1.5.4.1.2.2`, `A.1.5.4.1.3.2`, `A.1.5.4.3.1.0.3.1`: trailing double-space removed from section headers.
- Cross-reference link text converted from bare names to `A.x.y.z - Name` format across multiple AD budget docs.

===DEST: A.1--governance/A.1.5.1.5--ad-roster===

---

## PR #187 — 2026-02-23 Atlas Edit Weekly Cycle Proposal
**Merged:** 2026-03-05 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Current Aligned Delegates link** (`A.1.5.1.5`): cross-reference corrected from `A.1.5.1.4.0.6.1` → `A.1.5.1.5.0.6.1` (UUID unchanged — was a typo in the doc number).

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

## PR #180 — Feb 9 edit
**Merged:** 2026-02-12 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Short-Term Transitionary Measures** (`A.1.5.3.5`, `A.1.5.3.5.1`): removed (sunset — covered period prior to 1 Jan 2026, now elapsed).
- **Emergency declaration consultation** (`A.1.8.1.4`, `A.1.8.1.5.1`): "any relevant Scope Advisor(s)" → "the Core Council Risk Advisor" — terminology update.
- **Linear Interpolation Module** (`A.1.9.3.2.13.2.1`): same Scope Advisor → Core Council Risk Advisor substitution.

### Housekeeping
- Terminology sweep: "Scope Advisor(s)" → "Core Council Risk Advisor" across governance/emergency sections.

---

## PR #181 — Add AxisLegati
**Merged:** 2026-02-10 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New AD recognized: AxisLegati** — added to the Active AD roster (`A.1.5.1` table):
  - Cold wallet: `0x9B4AF496CC72c432586e85a1D8264A2708c4dcb6` (verified sig #301787)
  - Hot wallet: `0x7bc5a420b6524Fa925F1321A01825438369E3c2e` (verified sig #301786)
  - Recognition submission: https://forum.sky.money/t/axislegati-ad-recognition-submission/27677

---

## PR #174 — Adjust Order of NR Docs and Update Markdown Syntax
**Merged:** 2026-02-02 | **Type:** Housekeeping

Reordered Needed Research (NR) subdocs within `A.1.4` governance sections: `A.1.4.4.0.4.1` (Highest Standard Tenet) moved to follow NR-1; NR-3 expanded with additional research questions (contributor scarcity, cross-team experience); NR docs shuffled to align with updated section ordering. Also updates `ATLAS_MARKDOWN_SYNTAX.md` (syntax reference file, not Atlas content) with additional blank lines for readability. No Atlas content values changed.

---

## PR #172 — Jan 26 Edit
**Merged:** 2026-01-29 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Highest Standard — AC Adjudication** (`A.1.4.4.0.4.1`): Reduced in scope — the 51% evidence standard and maximal-accountability paragraphs removed; shortened to a single principle statement.
- **AC Role Exclusivity NR docs added** (`A.1.4.5`): NR-2 ("Should ban apply to all stakeholder roles?") and NR-3 ("Should team contributors be subject to the ban?") added as Needed Research subdocs.
- **Operational Security Tenet** (`A.1.4.7.0.4.1`): Text preserved; minor formatting only.
- **Facilitator Anonymity Exemption** (`A.1.4.7.1`): Shortened — citations to specific Atlas provisions removed from the exemption statement.
- **Swift Action NR doc added** (`A.1.4.8`): NR-5 ("Derecognition Procedure") added.
- **Mandated Derecognition For Severe Breaches** (`A.1.4.9.2.2`): Converted from NR (research stub) to active **Core** doc; defines derecognition requirement for Governance Attacks; NR-7 ("Defining Severe Actions/Governance Attack") added as subdoc.
- **AC Derecognition NR doc added** (`A.1.4.10`): NR-9 ("Derecognition Uncertainty Due To Anonymous Actors") added.

### Context
Significant governance-framework update: the 51% standard for AC derecognition is removed from the active doc layer (moved/superseded), and the "Mandated Derecognition" article is elevated from research to active Core status. The three NR docs signal active research tracks for governance design.

---

## PR #156 — January 12 edit
**Merged:** 2026-01-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Sky Core Spell Executes Agent Spell** (`A.1.9.2.3.2.3.2.1`): "Prime's SubProxy contract" → "Agent's SubProxy contract" — terminology fix clarifying that the SubProxy is agent-specific.

---

## PR #143 — 2025-12-15 Edit
**Merged:** 2026-01-07 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- "Prime Spell" → "Agent Spell" terminology sweep across all StarGuard subsections (`A.1.9.2.3.2.2.3` → `A.1.9.2.3.2.3`): 29 sections updated. StarGuard deployment process (`A.1.9.2.3.2.3.1.1.1`) respecified: deploy and initialize StarGuard per new SubProxy in same Spell; StarGuard Functionality split into dedicated article (`.1.1.2`). "Sky Core Spell Executes Prime Spell" renamed to "Sky Core Spell Executes Agent Spell" (`A.1.9.2.3.2.3.2.1`).

---

## PR #141 — Dec 8 edit
**Merged:** 2025-12-11 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Execution Of Prime Spells** (`A.1.9.2.3.2.2.3`): clause "except as specified in Short-term Transitionary Measures" removed — no exceptions to the StarGuard preference rule.

### Housekeeping
- `A.1.9.2.3.2.2.3` section reorganized and renamed to "Execution Of Agent Spells" (`A.1.9.2.3.2.3`); "Prime Spell" terminology replaced with "Agent Spell" throughout 29 subsections. StarGuard Deployment article (`A.1.9.2.3.2.3.1.1.1`) rewritten: now specifies deploy-and-initialize per new SubProxy in same Spell; new StarGuard Functionality article added at `.1.1.2`.

---

## PR #139 — Fix delegate document numbering
**Merged:** 2025-12-08 | **Type:** Housekeeping

Renumbered the entire Ranked Delegates section from `A.1.5.4` to `A.1.5.3` (and downstream docs correspondingly, e.g. `A.1.5.4.1.1.2` → `A.1.5.3.1.1.2`), plus two cross-reference fixes: `A.1.4.5.1` link updated from `A.1.5.4.5.2` → `A.1.5.3.5.2`, and `A.1.5.16.0.4.1` renumbered to `A.1.4.8.0.4.1`. All UUIDs unchanged; no content changes.

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

## PR #115 — Atlas Edit Weekly Proposal 2025-11-17
**Merged:** 2025-11-20 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Interim Deployment process** (A.1.9): Two new documents added under "Executive Process Definition":
  - "Creation Of Public Information Dashboard" — Prime must publish Dune (or equivalent) dashboard showing current Interim Deployment exposure (waived if Core Council Risk Advisor already covers it at info.sky.money)
  - "Prime Agent Use Of Interim Deployment" — once requirements satisfied, Prime may begin using the Interim Deployment under approved testing parameters
  - "Completion Of Full Risk Assessment" revised: "Prime" → "Prime will work with Core Council Risk Advisor"; subsequent spell authority shifted to Core GovOps proposal route

---

## PR #110 — Nov 10 edit
**Merged:** 2025-11-13 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Prime Spell Security Enforcement framework added** (A.1.9, new): Comprehensive enforcement system for Prime Agent spell security — see A.0 changelog for full detail. Key additions to governance scope: Incident Registry (Active Data, Core Facilitator as Responsible Party), penalty authority (Core Facilitator + Core GovOps), and linkage to Prime Agent Credit Rating System.

### Context
See A.0--preamble changelog for comprehensive description. The governance scope additions establish the formal recordkeeping and enforcement authority components.

---

## PR #103 — 2025-11-02 Weekly Cycle Edit Proposal
**Merged:** 2025-11-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Solana LayerZero Bridge governance section added** (A.1.9 Governance Security Culture And Research):
  - Bridge overview: replaces Wormhole; Token Bridge (USDS Ethereum↔Solana) + Governance Bridge (SKY-issued token control on Solana)
  - Phase 1 deployment: November 13 Executive Vote; Phase 2: subsequent Out-Of-Schedule Executive Vote
  - Rate limit: 10,000,000 USDS/day (Core Facilitator + Core Council Risk Advisor can modify via Operational Weekly Cycle directly to Executive Vote)
  - **Ethereum LayerZero Freezer Multisig** added: `0x381d…776` — 2/4 signing; 2 Amatsu + 2 other signers; can freeze bridge from Ethereum side without standard spell process
  - **Solana LayerZero Freezer Multisig** added: 2 Amatsu + 2 Keel signers; can freeze bridge from Solana side; min 2 signers, equal Amatsu/Keel representation
  - Both Freezer Multisig references also added to Governance Security Delay Requirements section (replacing the former Linear Interpolation Module Consideration slot — that doc was relocated, not deleted)
- **A.5 Location Resilience article** description: "Accessibility Rewards" → "Distribution Rewards"

### Housekeeping
- Linear Interpolation Module Consideration doc moved to correct position after the Authorization section

---

## PR #96 — October 27 edit
**Merged:** 2025-10-31 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Execution Of Agent Spells** (A.1.9) — new section added covering StarGuard mechanism:
  - **StarGuard** contract per-Agent manages whitelisting and execution of Agent Spells; `exec()` triggers SubProxy `exec()`; `maxDelay` recommended 7 days; `drop()` revocation supported
  - **Permissionless execution** via StarGuardJob keeper
  - **Short-term transitionary**: only Spark uses StarGuard during transition; other Agents use Direct Execution through Sky Core Spell
- **Interim Deployment process** (A.1.9 Executive Process Definition): Two additional requirements inserted — dashboard creation (Dune or equivalent) and explicit authorization for Prime to begin using Interim Deployment
- **Stage 2 timing** (A.2.6 Monthly Settlement Cycle): "expected February 2026" → will be implemented in December 2025 Monthly Settlement Cycle for Nov period; fallback: Jan 2026 if no Dec cycle
- **Annotations** updated: "Support Facilitators" → "Core GovOps" for "Monitoring And Ensuring" and "Properly Notified" element annotations
- **Tenets**: "Key Atlas Contributors" funding — "Support Facilitators" → "Core Facilitator"; duplicate "In The Transition To Endgame" tenet added

### Housekeeping
- `A.3.3` Fluid CRR: duplicate `<tr>` tag removed (stray markup)

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
