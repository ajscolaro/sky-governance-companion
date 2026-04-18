# Support Scope — Change History

Atlas path: `A.2` — The Support Scope

---

## PR #222 — Atlas Edit Proposal — 2026-04-13
**Merged:** 2026-04-16 | **Type:** Weekly edit (Atlas Axis — Poll 1628) | **+1232/-32 lines**

### Material Changes

- **Integrator Program responsibility transferred from Viridian Advisors to Operational GovOps** (`A.2.2.8.1.2.1`): this is a material authority change across the Distribution Reward Primitive's Integrator onboarding pipeline. Affected subsections:
  - **Alignment determination** (`A.2.2.8.1.2.1.1.1.1`): "Operational GovOps in consultation with Viridian Advisors" → **Operational GovOps** (Viridian consultation removed)
  - **Application Process** (`A.2.2.8.1.2.1.1.2.1`): applications, thread management, review, Prime coordination, and Reward Code issuance move from Viridian to Operational GovOps; Responsible Party for the Integrator Applications Active Data list also transfers
  - **Onboarding Process** (`A.2.2.8.1.2.1.1.3`): Near-Term and Long-Term bifurcation collapsed into a single "Process" document — Operational GovOps is now the sole gatekeeper from the outset. Operational GovOps may contract with another actor to perform review/issuance work
  - **Reward Code assignment** (`A.2.2.8.1.2.1.2.1`): same Near-/Long-Term collapse. Operational GovOps assigns Reward Codes directly; may contract out at its discretion
  - **Tracking Methodology** (`A.2.2.8.1.2.1.2.2.1`): FIFO net-deposit processing moves from Viridian to **Operational GovOps**; "long term" Operational-Executor-Agent language removed
  - **Reward Code List Management** (`A.2.2.8.1.2.1.2.3`): list is now managed by Operational GovOps (was Viridian)
- **Safe Harbor Avalanche coverage added** (`A.2.11.1.2.2.3.3.1` and `.3.3.2`): Avalanche added to the covered chains list — chainId **43114**; Asset Recovery Address (Avalanche Governance Relay) **`0xe928885BCe799Ed933651715608155F01abA23cA`**
- **Transfer flow documentation added for Near-Term Integrator process** (`A.2.2.8.1.2.1.1.5` process-flow doc): updated references from Viridian to Operational GovOps throughout (the process-flow bullet list previously referenced Viridian in two places; now references Operational GovOps)

### Housekeeping

- "Long Term Process" documents under `A.2.2.8.1.2.1.1.3` (Onboarding) and `A.2.2.8.1.2.1.2.1` (Reward Code Assignment) deleted — the transitional/near-term framing is no longer needed once Operational GovOps takes full ownership

### Context

This PR executes the Viridian-to-Operational-GovOps handoff for the Integrator Program that was previously flagged as the "long-term" endpoint. The near-term/long-term bifurcation is collapsed — Operational GovOps takes full ownership of Integrator onboarding, Reward Code issuance, and the Integrator list. Operational GovOps may still contract with another actor (including Viridian), but the accountable party is now singular. The Safe Harbor Avalanche addition complements the broader Avalanche buildout in this cycle (Grove Avalanche expansion; see grove changelog). Ratification Poll 1628 passed 10-0 with 3 non-voters. SKY ~$0.075, USDS supply ~$11.3B at merge.

---

## PR #219 — Atlas Edit Proposal — 2026-04-06
**Merged:** 2026-04-09 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Three-stage staking rewards framework introduced** (A.2.3.1.4.2): The prior flat allocation rule (37,600 USDS/day to SKY buybacks, remainder to Surplus Buffer) is replaced by three sequential stages:

  | | Stage 0 (current) | Stage 1 | Stage 2 |
  |---|---|---|---|
  | **Trigger** | Default | Executive Vote at Core Facilitator's discretion | When SKY reserves fall to ~15 days of supply |
  | **SKY staking** | 75% of prior month's Step 4 Capital (from SKY token reserves) | 50% of prior month's Step 4 Capital (from SKY token reserves) | All SKY bought via buybacks |
  | **SKY buybacks** | 37,600 USDS/day | 37,600 USDS/day | 25% of prior month's Step 4 Capital |
  | **USDS staking** | None | None | 25% of prior month's Step 4 Capital |
  | **Remainder** | → Surplus Buffer | → Surplus Buffer | → Surplus Buffer |

  - Stages 0/1 fund SKY staking from Protocol Treasury SKY token reserves (not Step 4 Capital directly); rate recalculated monthly by Core Facilitator + Risk Advisor
  - Stage 1 and Stage 2 transitions authorized directly via Executive Vote (no Governance Poll needed)

- **Grove designated Avalanche Pioneer Prime** (A.2.2.8.3.1.1.2 Active Data): Grove added to the Active Pioneer Primes list alongside Keel. Pioneer Prime Requirements also updated: the clause requiring designation "from genesis moment" was removed, opening the designation to agents not created solely for that purpose.

- **Keel Ecosystem Accord — three provisions removed** (A.2.8.2.3.2): Following the Genesis Capital Allocation transfer in the March 26, 2026 Executive Vote, three now-obsolete Keel Ecosystem Accord provisions were deleted:
  1. Transfer from Liquidity Bootstrapping Budget to Keel (500,000 USDS advance for Solana DeFi, address `6cTVPDJ8WR1XGxdgnjzhpYKRqcv78T4Nqt95DY8dvMmn`)
  2. Use of Funds for Keel Development Expenses
  3. Keel Senior Risk Capital (7.5M USDS short-term credit toward Total Risk Capital)

### Housekeeping
- Spark Foundation Grant documents (A.2.8.2.2.2.5.5.2–.3): "SubDAO Proxy" → "Spark's Prime Treasury" for Dec 2025 and Q2 2026 grants; Forum link format corrected from `[Forum Post](url)` to plain URL
- Resilience Fund beneficiary list: "Scope Facilitators" → "Facilitators"
- "Scope Facilitator" → "Core Facilitator" in several A.2 documents

### Context
The three-stage staking rewards framework is a structural precursor to full SKY Treasury Management. Stage 2 is the first Atlas policy that allocates Step 4 Capital to USDS staking rewards, though the trigger (near-depletion of SKY token reserves) means it won't activate for some time. The removal of the Keel bootstrapping provisions signals that Keel's initial capitalization period is complete — the 10M USDS Genesis Capital Allocation transferred in March replaced the earlier patchwork of advances and credits documented in the Ecosystem Accord.

---

## PR #186 — 2026-02-16 AEW proposal
**Merged:** 2026-02-22 | **Type:** Weekly edit (Atlas Axis — Poll 1618) | **+2119/-158 lines**

### Material Changes
- **New framework: Security Alliance Safe Harbor Agreement** (`A.2.11.1.2`, new): Sky Ecosystem formally adopts the SEAL Safe Harbor whitehat-rescue agreement. The agreement is onchain; execution requires the Core Facilitator to include `adoptSafeHarbor` in an upcoming Executive Spell. Key parameters:
  - **Safe Harbor Registry:** `0x326733493E143b8904716E7A64A9f4fb6A185a2c` (Ethereum Mainnet)
  - **Agreement Address:** `0x9E5Cf4a9C806fE1F4392788b21342a442E14Cc20`
  - **Bounty Cap:** `10,000,000` USD; **Bounty Percentage:** `10`; **Retainable:** false (whitehat must first return full amount)
  - **Identity requirement:** `Named` (legal name required); **Diligence:** KYC + OFAC/UK/EU sanctions screening via trusted third-party, data deleted within 30 days if successful
  - **Covered chains (chainId + Asset Recovery Address):** Ethereum Mainnet (1, Pause Proxy `0xbe8e…98fb`), Arbitrum (42161), Optimism (10), Base (8453), Unichain (130), Solana. Each non-Mainnet Asset Recovery Address is the respective Governance Relay
  - **Maintenance** assigned to Spell Teams (must add new Bug Bounty contracts to Safe Harbor as they are deployed); Core Facilitator reviews compliance
  - **Frontends:** Core GovOps must work with Ecosystem Actors to incorporate Exhibit D language into frontend T&Cs
  - **Prime Responsibilities:** Primes must register deployed contracts with Safe Harbor and incorporate Exhibit D in their frontends

### Context
Safe Harbor is the headline A.2 change of this AEW — it transitions Sky's Bug Bounty program from a purely off-chain framework into an enforceable onchain agreement (via the SEAL registry contract) with clear bounty economics (10% / $10M cap) and a legally-named-hacker requirement. The Named identity choice is notably stricter than the anonymous/pseudonymous options Safe Harbor allows, consistent with Sky's KYC/sanctions posture. The cross-chain scope (6 chains) anticipates L2 expansion — Avalanche is not yet included here but is added in PR #222. Ratification Poll 1618 passed 10-0 with 2 non-voters. SKY ~$0.065, USDS supply ~$9.9B at merge.

---

## PR #133 — 2025-12-01 AEW Proposal
**Merged:** 2025-12-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Net Revenue income categories expanded** (A.2.4.1.2.1.2): new "Other Income" section added with two sub-items:
  - **Sky Core Vault Income** (A.2.4.1.2.1.2.6.1): all income from Sky Core Vaults (collateral vaults + SKY-Backed Borrowing vault), including liquidation penalties
  - **LitePSM Income** (A.2.4.1.2.1.2.6.2): all income from the LitePSM
- **Net Revenue cash-basis accounting added** (A.2.4.1.2.1.2): "All items of Income and Expense are recognized on a 'cash basis' based on when USDS/DAI enter or leave the Sky Surplus Buffer, Core Council Buffer, or Aligned Delegates Buffer."
- **Sky Savings Rate Expense broadened** (A.2.4.1.2.1.3.1): was "interest to sUSDS holders and sDai holders" → now covers "all savings-related expenses (other than Integration Boost), including Dai Savings Rate and stUSDS interest."

---

## PR #110 — Nov 10 edit
**Merged:** 2025-11-13 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Sky Direct Exposures list expanded** (A.2.4 Active Data): added "PSMs — Investments by Spark or Grove in USDC in PSMs on non-Ethereum chains" and "Curve Pools — Investments by Spark in USDT in sUSDS/USDT Curve pools"
- **No ASC requirements for Sky Direct Exposures** (A.2.4, new): Primes not required to hold Actively Stabilizing Collateral for Direct Sky Exposures
- **Ecosystem Accord 4 terms updated** — see A.0 changelog for Launch Agent 4 details

### Housekeeping
- "Support Facilitators" → "Core GovOps" / "Core Facilitator" propagations in A.2.2, A.2.7

### Context
See A.0--preamble changelog for comprehensive description. The expansion of Direct Sky Exposures shifts more protocol liquidity outside Prime-level risk capital requirements.

---

## PR #107 — OOS Atlas Edit
**Merged:** 2025-11-10 | **Type:** Weekly edit (out-of-schedule)

### Material Changes
- **Ecosystem Accord 4: Sky and Launch Agent 4** added (A.2.10, new): indefinite accord commencing November 13, 2025. Genesis Capital Allocation: 21,000,000 USDS to Launch Agent 4 SubProxy. Launch Agent 4 added to Pioneer Primes list.

### Context
Launch Agent 4 (Rubicon) onboarded as a new Prime Agent with 21M USDS Genesis Capital — the second-largest allocation after Spark's 25M.

---

## PR #89 — 2025-10-20 Atlas Weekly Cycle Proposal
**Merged:** 2025-10-23 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Direct Sky Exposures framework added** (A.2.4, new): JAAA through Grove designated as first Direct Sky Exposure. No Risk Capital or ASC requirements for Primes. Revenue sharing model defined.
- **Atlas Edit Proposal Process for Prime Agents** (A.2.4, new): Primes without Root Edit Primitive submit drafts to Core GovOps by Monday → formal proposal submitted following week
- **"BA Labs" → "Core Council Risk Advisor"** throughout A.2.4 and A.2.6 Settlement Cycle documents

### Housekeeping
- "Support Facilitators" → "Core GovOps" in A.2.2 governance process support

### Context
See A.0--preamble changelog for comprehensive description. A.2 additions formalize the Direct Sky Exposures framework and Prime Agent Atlas edit process.

---

## PR #78 — October 13 edit
**Merged:** 2025-10-16 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- "Support Facilitators" → "Core GovOps" in governance process coordination, Ecosystem Actor designation, and resource budget
- "Support Facilitator" → "Core Facilitator" in Atlas Core Development funding
- Sky Forum moderator list: removed "Accessibility Facilitators"

### Context
Continuation of the governance terminology migration. The A.2 changes are primarily propagation of role renames.

---

## PR #61 — 2025-09-22 Weekly Cycle Edit Proposal
**Merged:** 2025-09-26 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Ecosystem Accords dispute resolution framework added** (A.2.10, new section): Comprehensive dispute resolution process with roles for Core GovOps (manages process, gathers information) and Core Facilitator (isolated adjudicator). Process: Formal Request → Reasonableness determination (3 working days) → Statement of Problem (5 days) → Statement of Response (5 days) → Rebuttal (3 days) → Core GovOps analysis → Core Facilitator decision (3 days) → publication on Forum and Active Data
- **First dispute recorded** (A.2.10 Active Data): "Dispute Between Spark And Grove Regarding Effective Date Of Their Ecosystem Accord" (September 2, 2025)
- **Ecosystem Accords article renumbered:** A.2.8 → A.2.10; "List Of Active Ecosystem Accords" → "Active Ecosystem Accords"
- **Ethena RRC ratios tightened** (A.3.3):
  - Direct Ethena Exposures: 2% → **3%**
  - Lending Ethena-related against Ethena-related collateral: 2% → **3%**
  - Lending non-Ethena against Ethena collateral: 3% → **4%**
- **Ethena Aggregate Exposure Limit introduced** (A.3.3, new): 1,500,000,000 USDS cap across all Prime Agents; no new investments allowed to exceed; Core Council may direct sales if exceeded
- **Superstate risk framework added** (A.3.3, new): 3% Instance Financial RRC; 500M USDS Aggregate Exposure Limit; 20M USDS Initial Deployment Limit; 50M USDS Subsequent Deployment Limits (require BA Labs/Risk Advisor approval)
- **Typo fix** (A.2.3): "Exercutive Vote" → "Executive Vote" in Accessibility Reward process

### Context
PR #61 is one of the most substantively important edits in this batch despite its unassuming title. The Ecosystem Accords dispute resolution framework formalizes a process that was previously ad hoc — and its first exercise (the Spark/Grove dispute) is already recorded. The Ethena RRC tightening (+50% across the board) and the new 1.5B USDS aggregate cap signal growing governance concern about Ethena concentration risk. The Superstate framework opens a new asset class (USCC) with graduated deployment limits. SKY was ~$0.07 and USDS supply ~$7-8B.

---

## PR #47 — Fix Ecosystem Entity Grants document type
**Merged:** 2025-08-19 | **Type:** Housekeeping

A.2.14 (Ecosystem Entity Grants) corrected from `Core` document type to `Section`; also added A.2.14 to the Articles table so it appears in the Atlas article registry.

---

## PR #43 — August 11 edits
**Merged:** 2025-08-15 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **"Star Agent" → "Prime Agent"** globally across A.2: Sky Primitives article, Risk Capital article, Asset Liability Management framework, and all Agent-related definitions updated to use "Prime Agent". No operational content changes.

---

## PR #42 — 2025-08-11 Edit 2
**Merged:** 2025-08-15 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Ecosystem Entity Grants established** (A.2.14, new): Two grants to be included in the next available Executive Vote:
  - **Sky Frontier Grant** (to `0xca5183FB9997046fbd9bA8113139bf5a5Af122A0`): 50,000,000 USDS + all SKY in Sky Pause Proxy (less Fortification share) + all UniV2 SKY/USDS LP tokens + all MKR + other non-SPK dust.
  - **Fortification Grant** (to `0x483413ccCD796Deddee88E4d3e202425d5E891C6`): 10,000,000 USDS + 200,000,000 SKY.
- **Surplus Buffer Splitter parameters updated** (A.3.3 Active Data):
  - `vow.hump`: 50M USDS → **1M USDS** (threshold for Splitter activation)
  - Buyback/staking split: 50%/50% → **25%/75%** (buyback/staking)
  - `burn`: 50% (WAD/2) → **25%** (WAD/4)
  - Override rule added: parameters must ensure 100,000 USDS/day SKY buyback and 300,000 USDS/day Staking Rewards, superseding other conflicting Atlas documents.

### Context
The Ecosystem Entity Grants represent a large non-recurring capital transfer from Sky Core treasury to two new foundations. The vow.hump reduction from 50M to 1M and the split shift to 75% staking marks an aggressive pivot toward rewarding stakers over buybacks.

---

## PR #38 — Atlas Edit Weekly Cycle Proposal 2025-08-04
**Merged:** 2025-08-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Monthly Settlement Cycle Stage 1 fully specified** (A.2.6): Stage 1 Simplified P&L Calculation detailed:
  - Sky → Star: Accessibility Reward earnings + Agent Rate earnings (sum = Amount Due From Sky)
  - Star → Sky: Step 1 Total Allocation System Revenue (sum of Instance Revenue); Step 2 Total Allocation System Profit (Revenue minus Instance Expense, floor zero); Step 3 Adjusted Profit; net amount due
  - Instance Expense defined as interest on Sky Collateral Portfolio principal at Base Rate (per block)

---

## PR #33 — Weekly cycle edit 2025 07 28
**Merged:** 2025-08-01 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Monthly Settlement Cycle implementation roadmap added** (A.2.6, new): Three-stage rollout defined:
  - **Stage 1**: Simplified P&L via off-chain calculation; Star Allocator Vault stability fees reduced to zero via SP-BEAM; target August 21, 2025 Executive Vote for July 2025 period.
  - **Stage 2**: Full P&L calculation with Virtual Base Rate (off-chain interest calc, paid via Executive Vote).
  - **Stage 3**: Full on-chain Base Rate accrual into Allocator Vaults; Executive Votes only for interest paydown and settlement.
- **Launch Agent 2 development expense flexibility added** (A.2.10, new): LA2 may redirect the 500,000 USDS Liquidity Bootstrapping advance (previously restricted to DeFi liquidity on Solana) to fund development expenses at its discretion, with notification to its Operational Executor Agent.
- **Transfer document updated** (A.2.10): "Sky will transfer" → "Sky has transferred" 500,000 USDS to LA2 — confirming completion.
- **Slippage cap added** (A.3.3 risk framework): Slippage $S$ must not exceed 25%; Aave/SparkLend exception: use half-position slippage (max 50% liquidation per block).
- **Resilience Research approval process clarified** (A.2.12): projects under 15,000 USDS approved directly by Support Facilitator (included in Executive Vote without a prior poll); at or above 15,000 USDS require a Governance Poll first. Formal approval step added: Facilitator must reply to their Forum post evaluation.

### Housekeeping
- Duplicate "Trigger" element annotation removed (was duplicated twice).
- "Resilience Research Proposals" → "Research Proposals" throughout A.2.12; "A.2.9" cross-reference → "A.2.11".

---

## PR #30 — Atlas edit weekly cycle proposal 2025 07 14
**Merged:** 2025-07-18 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Integration Boost description updated** (A.2.4): "Integration Boost" payments clarified as covering SSR-equivalent on "Unrewarded USDS balances" in partner protocols; reference to the new canonical A.0.1 definition.
- **"Unrewarded USDS Balances" document removed** (A.2.4): Legacy definition deleted; canonical definition now lives in A.0.1 (covers SSR, Integration Boost, and USDS Token Rewards — broader than the old A.2.4 definition which only covered SSR and USDS Token Rewards).
- **Pioneer Benefits and Pioneer Incentive Pool updated** (A.2.4): "Second form" of Pioneer benefits clarified — unrewarded USDS bridged to Pioneer Chain (per A.0.1 definition) counts toward Pioneer Incentive Pool payments; formula updated to "SSR multiplied by balance of Unrewarded USDS" (was "SSR applied to unrewarded USDS").
- **Monthly Settlement Cycle overview reformatted** (A.2.6): inline text list converted to numbered `<ol>` list; Pioneer Incentive Pool item updated to reflect new Unrewarded USDS formula.
- **Launch Agent 2 — Ecosystem Accord 3 reference added** (A.6.1.1.X): LA2 formally acknowledges it has agreed to Ecosystem Accord 3 (located at A.2.10).

### Housekeeping
- "Actively Stabilizing Collateral Rental Primitive" → "Asset Liability Management Rental Primitive" throughout A.2.4 and all agent Artifacts (Spark, Grove, LA2, LA3). Pure rename; same mechanism.

---

## PR #22 — Weekly Cycle Atlas Edit 2025-06-30
**Merged:** 2025-07-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Grove name revealed** (formerly "Launch Agent 1"): All references to "Launch Agent 1" in Ecosystem Accord 1 (A.2.10) renamed to "Grove" — accord title, parties, exclusivity clause, right-of-first-refusal terms, revenue share language.
- **Ecosystem Accord 3 — Sky and Launch Agent 2 added** (A.2.10, new): Indefinite accord effective 2025-06-23 governing:
  - 500,000 USDS transfer from Liquidity Bootstrapping Budget to Launch Agent 2 for Solana DeFi liquidity (multisig `6cTVPDJ8WR1XGxdgnjzhpYKRqcv78T4Nqt95DY8dvMmn`)
  - Pre-Pioneer Incentive Pool for Launch Agent 2 on Solana: SSR applied to all USDS on Solana minus Integration Boost payments, paid monthly to Launch Agent 2 incentive wallet (`8JmDPG5BFQ6gpUPJV9xBixYJLqTKCSNotkXksTmNsQfj`); funds must be used for ecosystem incentives only
- **Pre-Pioneer Incentive Pool primitive defined** (A.2.4, new): Framework for pre-Pioneer chain bootstrapping before a formal Pioneer Star is established — temporary chain-specific mechanism, terms governed by Ecosystem Accord.
- **Accessibility Reward Fee references updated**: "Fee For USDS and sUSDS Balances" and "Star Agent Management Fee" references collapsed into single "Fees" reference throughout rate relationship documents.
- **AEP Formal Submission Window clarified** (A.1.3): Two-day window starting 00:00 UTC Monday of the Monthly Governance Cycle, ending 23:59 UTC Tuesday.

### Context
The Grove name reveal completes what was telegraphed in earlier PRs — "Launch Agent 1" is officially Grove across all Accord and Ecosystem documentation. The Pre-Pioneer Incentive Pool mechanism is the practical tool that funds Solana adoption work while the Pioneer Star formal structure is pending.

---

## PR #18 — Weekly Cycle Atlas Edit 2025-06-23
**Merged:** 2025-06-27 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Spark Genesis Capital Transfer authorized** (A.2.10, new): 20.6 million USDS to be transferred from Surplus Buffer to Spark SubProxy in the June 26, 2025 Executive Vote (pre-TGE expenses of 4.4M USDS deducted: 2M for market makers, 2.4M for exchanges; no token launch penalty applied). Authorized to proceed directly to Executive Vote without prior Governance Poll.
- **Spark Foundation cash grant approved** (A.2.10, new): 800,000 USDS/month for 3 months from Spark's Genesis Capital Allocation, beginning at genesis. Spark Foundation address on Ethereum: `0x92e4629a4510AF5819d7D1601464C233599fF5ec`.
- **Bonus Limitation added** (A.2.10, new): USDS/sUSDS balances held by the Star itself are excluded from the 2025 Accessibility Reward bonus.
- **Short-Term Transitionary Measures clarified** (Spark Artifact): Spark/GLL parameters controlled by Sky Governance until SPK token sufficiently decentralized (estimated September 17, 2025), then transition to Spark Governance.

### Context
This PR formally records Spark's genesis capital transfer and the Spark Foundation grant — the financial launch mechanics for the SPK token event. Poll 1525 passed.

---

## PR #7 — AEP-11: Edit
**Merged:** 2025-06-23 | **Type:** AEP-11

### Material Changes
- **Ecosystem Communication Channels moderation framework added** (A.2.7, new): 10 new Core documents under the existing A.2.7 Ecosystem Communication Channels section defining moderation policies:
  - General ban authority for responsible moderators (warn first unless egregious behavior)
  - Governance Facilitators have exclusive authority to ban users mid-governance-process on the Sky Forum
  - Public communication of bans: mandatory for Forum bans that interrupt governance; discretionary otherwise
  - Automated moderation tools (AI/bots) permitted with human oversight
  - Unbanning via Prime Delegate forum proposal + binary Weekly Cycle poll; bans permanent by default
  - Responsible moderators: Governance Facilitators + Accessibility Facilitators (Forum), TechOps (Discord), Maker Growth (X/Reddit)

### Context
AEP-11 ratified. Forum: https://forum.sky.money/t/aep-11-moderation-policies-of-the-sky-ecosystem-communication-channels/26225

---

## PR #15 — 2025-06-16 weekly atlas edit proposal
**Merged:** 2025-06-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Pioneer Phase defined** (A.2.4, new): A 3-year period beginning when a Star Agent satisfies Pioneer Star Requirements, during which the Pioneer Star benefits provisions apply.
- **Pioneer Star Benefits clarified** (A.2.4): Now includes sUSDS alongside USDS in the untagged balance count during the Pioneer Phase.
- **Spark Senior Risk Capital documented** (A.2.10, new): Sky provides Spark 15 million USDS of SRC in the short term (credited toward Total Risk Capital, not transferred to SubProxy).
- **SPK token transfers restructured** (A.2.10): "Transfer Of Tokens To Spark Foundation" revised — SPK Company Ltd transfers all tokens not reserved for the token launch to the Spark Foundation; separate "Transfer Of Tokens For Token Launch" document added.
- **SubProxy Account control simplified** (A.2.4): Description of SubProxy Account changed from agent-controlled to "controlled by Sky Governance."
- **Agent Executor Accord revocation** (A.2.4): "root access" revocation language updated to "Executor Accord" revocation.
- **Pre-TGE expense treatments updated** (A.2.10): Two liquidity bootstrapping advances to Spark clarified as deductions from Genesis Capital Allocation at time of Capital Transfer (not refunds to Liquidity Bootstrapping Budget).

### Context
This large weekly edit handles pre-SPK-TGE preparation: Pioneer Phase framework, Spark SRC, and SPK token distribution structure. Forum post: https://forum.sky.money/t/atlas-edit-weekly-cycle-proposal-week-of-2025-06-16/26681

---

## PR #1 — 2025-05-26 Atlas Edit Weekly Cycle Proposal
**Merged:** 2025-06-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Allocation System terminology overhauled** (A.2.4): "Allocation Conduit" → "Allocation Instance" throughout; "First Loss Capital" → "Junior Risk Capital (JRC)" / "Risk Capital" throughout. New documents added:
  - Capital & Operational Plan (C&O Plan) framework replacing informal pre-setup check with GovOps
  - Pro-Forma Instance RRC Estimate and Notional TRC Coverage Strategy as required C&O Plan components
  - Continuous Monitoring Of On-chain Verifiable Risk Capital (OVRC)
  - Conditions Requiring Artifact Edit Proposal (vs. discretionary management)
- **Ecosystem Accord framework added** (A.2.10, ~80 new documents): Formal documentation of two major Ecosystem Accords:
  - **Accord 1 — Spark and Launch Agent 1**: Revenue share, subsidized borrowing, right of first refusal for DeFi opportunities, ASC provision, intellectual property, agent exclusivity terms
  - **Accord 2 — Launch Agent 1 and Spark — Star Program**: Distribution structure for agent tokens; Launch Agent 1 star treasury allocation (3B AGENT1 tokens)
  - Token reward distribution schedules, income definitions, 2025 bonus provisions, grand prix airdrops
- **Agent token distribution rule updated** (Article): Changed from "distributed to USDS Token Rewards users and SKY Staking users per governance" to "distributed per the terms of the Ecosystem Accord between Sky and the respective Agent."

### Context
The first PR in this repository. The Allocation System rename (First Loss Capital → Junior/Senior Risk Capital) is a major conceptual shift — the new framework distinguishes between JRC (first-loss), SRC (senior/backstop), and OVRC (on-chain verifiable). The Ecosystem Accord documentation formalizes the economic relationship between Sky, Spark, and Launch Agent 1 that had been operating informally.

---
