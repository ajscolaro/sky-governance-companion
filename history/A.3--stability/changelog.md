# Stability Scope — Change History

Atlas path: `A.3` — The Stability Scope

---

## PR #227 — Atlas Edit Proposal — 2026-04-27
**Merged:** 2026-04-30 | **Type:** Weekly edit (Atlas Axis — Poll #1630)

### Material Changes
- **Target Aggregate Backstop Capital** (`A.3.5.3.2.1`): fixed **150 million USDS** → dynamic **1.5% of total USDS supply** (~$158M at current ~$10.5B USDS supply)
- **Turbo-Fill Floor** (`A.3.5.3.2.2`, UUID `db2aaf07…`): new parameter at **150 million USDS** — the threshold below which accelerated 50% Step 2 Capital retention applies in the new TMF
- **Genesis Capital Backstop haircut cap** (`A.3.7.1.6`): haircut now explicitly capped at Aggregate Backstop Capital (previously uncapped up to full loss amount)
- **Post-backstop settlement** (`A.3.7.1.6.2`): removed the 24 billion SKY distribution to Genesis Agents when haircut fully covers the loss; now SKY Backstop activates directly when losses exceed Prime Agent capital plus Aggregate Backstop Capital

### Context
The Target ABC shift from fixed 150M to 1.5% of USDS supply scales the target with protocol growth. The Turbo-Fill Floor preserves 150M as the accelerated-retention threshold, maintaining the prior target's practical effect while allowing the formal target to grow. The haircut cap and post-backstop settlement changes are complementary to the PR #224 loss-absorption reordering (Genesis Capital Backstop before SKY Backstop).

---

## PR #226 — Update April 23 Parameters
**Merged:** 2026-04-30 | **Type:** Spell recording (2026-04-23)

### Material Changes
- **Grove Allocator Vault DC-IAM** (ALLOCATOR-BLOOM-A): `gap` 250M → **500M USDS** (line 5B USDS, ttl 24h unchanged)
- **Pattern Allocator Vault DC-IAM** (ALLOCATOR-PATTERN-A): `gap` 10M → **50M USDS**; `line` 10M → **2.5B USDS** (ttl 24h unchanged)

---

## PR #219 — Atlas Edit Proposal — 2026-04-06
**Merged:** 2026-04-09 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Target Aggregate Backstop Capital raised** (A.3.5.3.2.1): 125 million USDS → **150 million USDS**

- **Genesis Capital Phase-Out mechanism introduced** (A.3.7.1.6.6.2, new): As backstop capital grows, Genesis Capital contributions from Sky to agents will be progressively reduced. Mechanics:
  - **Sky-level trigger:** Phase-out active when Aggregate Backstop Capital ≥ 125M USDS; pauses if it drops below
  - **Agent-level trigger:** Agent must have launched a liquid token with ≥ 10M avg daily trading volume over 30 days
  - **Monthly phase-out per eligible agent:** Base 1M USDS + Additional (ABC − 125M) ÷ 10
  - **Controller:** Core Council Risk Advisor (Active Data, direct edit protocol)
  - **Current Phased-Out Genesis Capital:** 0 USDS for all agents (Spark, Obex, Skybase, Core Council Executor Agent 1, Keel, Launch Agent 6, Amatsu, Ozone)
  - Genesis Capital definition updated: now = min(Eligible Genesis Capital, total agent capital), where Eligible Genesis Capital = Sky-contributed capital minus Phased-Out Genesis Capital

### Context
The Target Backstop Capital raise and the Phase-Out mechanism are complementary: raising the target to 150M means more buffer before phases kick in, while the phase-out formula builds in acceleration — every USDS above 125M reduces each eligible agent's Genesis Capital by 100,000 USDS/month. No agent is currently eligible for phase-out (none have yet met the 10M daily volume criterion for a liquid token). The mechanism signals governance intent to reduce Sky's exposure to Genesis Agent backstop obligations as the ecosystem matures.

---

## PR #182 — remove ALLOCATOR-NOVA-A from DC-IAM and set `line` to 0
**Merged:** 2026-02-17 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **ALLOCATOR-NOVA-A vault deactivated** (`A.3.7.1.2.1.4`): DC-IAM parameters (gap: 1M USDS, line: 60M USDS, ttl: 20 hours) removed; `line` set to a fixed 0 USDS, effectively closing the vault's debt ceiling. The `duty` parameter continues to be set by the SP-BEAM.

### Context
Removing ALLOCATOR-NOVA-A from DC-IAM and zeroing the line closes off an allocator vault that was no longer active. Companions to the allocator vault management process documented in A.3.7. Forum: https://forum.sky.money/t/allocator-nova-a-parameter-changes/27692. SKY ~$0.063, USDS supply ~$9.8B.

---

## PR #133 — 2025-12-01 AEW Proposal
**Merged:** 2025-12-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Sky Capital framework introduced** (A.3.5.3, new section): three capital metrics formally defined:
  - **Aggregate Capital Buffer**: Surplus Buffer + Core Council Buffer + Aligned Delegates Buffer + SubProxy capital of each Prime Agent
  - **Aggregate Backstop Capital**: (Genesis Capital in each Genesis Agent's SubProxy) + Core Council Buffer + Aligned Delegates Buffer − Allocated Genesis Capital
  - **Allocated Genesis Capital**: the negative of the Surplus Buffer (capital deployed into Genesis Agents)
- **Target Aggregate Backstop Capital**: **125 million USDS** (A.3.5.3.2.1)
- **Capital retention rule added** (A.3.5.3.2.2): when Aggregate Backstop Capital is below 125M USDS target, Sky Governance retains **25% of Net Revenue** monthly to grow the buffer (implemented via Treasury Management System and Smart Burn Engine parameter adjustments).

### Context
The Sky Capital framework formalizes a balance-sheet view of the protocol's safety net. The 125M USDS Target Aggregate Backstop Capital and the 25% Net Revenue retention rule are the first explicit capital adequacy targets in the Atlas — giving governance a clear metric and a defined response. This appeared alongside PR #133's Launch Agent 5 (Pattern) onboarding, suggesting the capital framework was added in anticipation of scaling Agent deployment.

---

## PR #110 — Nov 10 edit
**Merged:** 2025-11-13 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Actively Stabilizing Collateral Incentive introduced** (A.3.4, new): `Eligible ASC * (Base Rate - Treasury Bill Rate)` per block; paid monthly via Settlement Cycle. Treasury Bill Rate = 91-day US T-bill yield.
- **Resting ASC updated** (A.3.4): added "Cash Stablecoins in Uniswap (paired with USDS)"
- **Latent ASC updated** (A.3.4): "Cash Stablecoins in Uniswap" → "Cash Stablecoins in Uniswap (not paired with USDS)"
- **Agent Credit Line Borrow Rate** (A.3.2): now may vary by Prime Agent credit rating per Spell Security Registry
- **Prime Agent Credit Rating System** (A.3.2): Spell Security Incident Registry added as explicit factor

### Context
The ASC Incentive compensates Primes for the opportunity cost of maintaining liquid stablecoin buffers — the spread between the Sky Base Rate and risk-free T-bill rate. Combined with the Spell Security Registry linkage to credit ratings, this creates a dual incentive: maintain liquidity (ASC Incentive) and maintain spell quality (favorable credit rating).

---

## PR #89 — 2025-10-20 Atlas Weekly Cycle Proposal
**Merged:** 2025-10-23 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **A.3.1 Scope Improvement deleted:** Entire "Stability Scope Advisors" framework removed — replaced by Core Council Risk Advisor in A.1.7
- **"Instance Financial RRC Ratio" → "Instance Financial CRR"** throughout A.3.3: terminology standardized to Capital Requirement Ratio across Ethena, Superstate, Fluid, Pendle, and lending market documents
- **Capital Requirement Ratio (CRR) defined** (A.3.3, new): formal definition with examples
- **Superstate Instance Financial CRR raised:** 3% → **4.5%**
- **"Stability Scope Advisors" / "Stability Facilitators" → "Core Council Risk Advisor"** across A.3.2 (Base Rate setting), A.3.3 (lending market approvals), and other documents

### Context
The CRR terminology standardization and Superstate tightening are the key A.3 changes. The deletion of A.3.1 completes the migration of BA Labs from "Stability Scope Advisor" to "Core Council Risk Advisor."

---

## PR #61 — 2025-09-22 Weekly Cycle Edit Proposal
**Merged:** 2025-09-26 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Ethena RRC ratios tightened** (A.3.3):
  - Direct Ethena Exposures: 2% → **3%**
  - Lending Ethena-related against Ethena collateral: 2% → **3%**
  - Lending non-Ethena against Ethena collateral: 3% → **4%**
- **Ethena risk framework restructured** (A.3.3): new parent documents (Ethena, Ethena Required Risk Capital) added; Ethena Smart Contract/Administrative RRC text updated to reference "Direct Ethena Exposures" definition
- **Ethena Aggregate Exposure Limit introduced** (A.3.3, new): 1,500,000,000 USDS cap; prohibition on investments exceeding limit; Core Council may direct sales
- **Superstate risk framework added** (A.3.3, new): 3% Instance Financial RRC; 500M USDS Aggregate Exposure Limit; deployment limits (20M initial, 50M subsequent with approval); Smart Contract/Administrative RRC = zero in short term

### Context
Comprehensive risk framework tightening. Ethena RRC increased 50% across the board with a new aggregate cap. Superstate introduced as a new exposure category with graduated deployment limits.

---

## PR #46 — Atlas Edit Weekly Cycle Proposal 2025-08-18
**Merged:** 2025-08-22 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Near-term RRC model structure reorganized** (A.3.3): Pending Risk Models section restructured — "Near-Term Treatment" subsections removed from parent model descriptions (Perpetual Positions, Direct Exposures, Bond-Like Instruments, Real World Assets, Cash Stablecoins) and relocated under new named model containers. RRC ratios unchanged:
  - Perpetual Positions (Ethena): direct 2%, indirect through lending markets 3%
  - Direct Exposures: 25%
  - Bond-Like (PT-USDS): 0%; other PT tokens: 4%
  - RWA (BUIDL/JTRSY Mainnet/USTB): 0%; JTRSY Avalanche: 0.5%; JAAA Mainnet: 1.6%; JAAA Avalanche: 2.1%
  - Cash Stablecoins: 0%
- **Application-to-RWA and Application-to-Ethena exceptions moved** (A.3.3): Previously inline, now placed under a new "Real World Assets" exception block within Instance Smart Contract RRC Implementation (no rate changes).
- **Additional Restrictions On JTRSY And JAAA On Avalanche re-documented** under new location: initial deployment cap 20M USDS; additional deployments require Stability Scope Advisor approval; must be below 90% RTR (pro forma 100% RRC) until Centrifuge v3 audits approved; total cap 250M USDS.
- **Approved auditors list** (A.3.3): yAudit → **Electisec** (name change for the same firm).

### Housekeeping
- "Pending Risk Models" description simplified: removed "along with near-term Instance Financial RRC Ratios to be used until the models are fully implemented" — the models now have their own subdocuments.

---

## PR #33 — Weekly cycle edit 2025 07 28
**Merged:** 2025-08-01 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Slippage cap defined** (A.3.3): Slippage $S$ must not exceed 25%. Aave and SparkLend exception: use half-position slippage (50% max liquidation per block), so only slippage on half the position.
- **Aave and SparkLend slippage exception added** (A.3.3, new document): explicit rule acknowledging 50% max liquidation ceiling, ensuring correct calculation for these protocols.

---

## PR #30 — Atlas edit weekly cycle proposal 2025 07 14
**Merged:** 2025-07-18 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **"Asset Liability Management Rental" replaces "Actively Stabilizing Collateral Rental"** (A.3.4): Document title, header, and body text updated. Mechanism unchanged — allows Star Agents to trade ALM obligations between each other.
- **Andromeda noted as not operational** (A.3.5): "Andromeda is not currently operational and its debt ceiling has been reduced to zero" added to the Andromeda document.
- **Blocktower removed as active Arranger** (A.3.5): List of current active Arrangers → "No current active Arrangers." Wind-down notice for Clydesdale (previously mentioning Monetalis) removed.
- **Perpetual Yield Strategy exposure adjustment documents removed** (A.3.5): "Adjustment Of Perpetual Exposure Direct Accumulation" and its requirements document deleted. Active Data documents for Andromeda Direct Exposure (0), Andromeda Legal Rails Exposure (0), and Clydesdale Legal Rails Exposure (0) also deleted — all were already set to zero.

### Housekeeping
- "risk framework" → "Risk Framework" (capitalized) in approximately 10 documents across A.3.3 (financial risk introduction, implementation sections, JRC, SRC, short-term exemption).
- **Agent Rate** (A.3.2): "unrewarded USDS" → "Unrewarded USDS" (capitalized) — aligns with A.0.1 canonical definition.

---

## PR #26 — Weekly Cycle Atlas Edit 2025-07-07
**Merged:** 2025-07-11 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Sky Spread increased**: 0.05% → **0.1%** (A.3.3). Total spread between Sky Savings Rate and Base Rate: 0.25% → **0.3%**.
- **Sky Savings Rate relationship updated** (A.3.2): SSR = Base Rate − 0.3% (was 0.25%). Breakdown: 0.2% Accessibility Reward Fee + 0.1% Sky Spread.
- **Agent Rate relationship updated** (A.3.2): Agent Rate = Base Rate − 0.1% (was 0.05%).
- **USDC PSM And Coinbase Custody document removed** (A.3.4): Legacy document specifying 400M/550M/700M USDC PSM rebalancing triggers deleted — PSM management fully transitioned to Grove.
- **Other PSMs document removed** (A.3.4): "All PSMs other than Lite PSM must be offboarded" document deleted; Peg Stability Modules section updated to note transition to Grove.

### Context
The Sky Spread increase doubles the protocol's margin on the savings/base rate spread. Removing the legacy PSM documents formally closes out the Coinbase Custody rebalancing regime. Poll 1527 passed.

---

## PR #27 — Minor fixes
**Merged:** 2025-07-10 | **Type:** Housekeeping

Forum links in A.3.9 stability documents updated: `forum.makerdao.com` → `forum.sky.money` (Collateral Offboarding legacy context and Operational Security Protocols Research Track). No content changes.

---

## PR #22 — Weekly Cycle Atlas Edit 2025-06-30
**Merged:** 2025-07-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **JAAA onboarded as eligible RWA** (A.3.3): Invesco JAAA CLO ETF added to RWA Near Term Treatment — BUIDL/JTRSY/USTB retain 0% Instance Financial RRC Ratio; JAAA gets 1.6% Instance Financial RRC Ratio.
- **Ethena indirect exposure through lending markets** (A.3.3): "Indirect Ethena exposure through Morpho" → "Indirect Ethena exposure through lending markets" (broader scope). Only the portion backed by Ethena-related assets (PT-USDe, PT-sUSDe, PT-eUSDe) subject to the Ethena RRC; remainder calculated by asset backing.
- **PT-USDS bond-like RRC set to 0%** (A.3.3): Near-Term Treatment for bond-like exposures updated — PT-USDS gets 0% RRC; all other Pendle PT tokens remain at 4%.
- **Fluid RRC clarified** (A.3.3): 3% applies to "amount of funds supplied to Fluid that are borrowed" (not total supply).
- **Agent Credit Line Use of Funds rule added** (A.3.2, new): Borrowed funds must be deposited into Agent's Allocation Vault and used for Allocation System Instances; may not be transferred to SubProxy.
- **ASC Calculations defined** (A.3.4, new): Explicit formula: USDC in LitePSM + USDC in PSM3 (Base/Arb/Unichain/Optimism) + USDT in Curve + USDC in GUNI 0.01%/0.05% + USDC/USDT in Star ALM Proxy.

---

## PR #19 — 2025-06-26 spell changes
**Merged:** 2025-06-30 | **Type:** Spell recording (2025-06-26)

### Material Changes
- **Surplus Buffer Splitter: vow.hump**: 70 million USDS → **50 million USDS** (threshold for Splitter to activate).
- **Surplus Buffer Splitter: splitter.hop**: 1,728 seconds → **2,160 seconds** (frequency of Splitter runs).
- **LSEV2-SKY-A farms updated** (A.3.x): LSSKY→USDS farm address `0x38E4254bD82ED5Ee97CD1C4278FAae748d998865` and LSSKY→SPK farm address `0x99cBC0e4E6427F6939536eD24d1275B95ff77404` added (replaced placeholder).

---

## PR #18 — Weekly Cycle Atlas Edit 2025-06-23
**Merged:** 2025-06-27 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Ethena indirect RRC updated** (A.3.3): "Indirect Ethena exposure through Morpho" renamed to "Indirect Ethena exposure through lending markets"; PT-USDS added as a 0% bond-like exposure category.
- **Agent Credit Line interest accrual clarified** (A.3.2): Rewording to make clear that interest is reflected in the Allocation Vault balance and must be regularly transferred to reduce vault balance to principal.

### Housekeeping
- "Near Term Treatment" → "Near-Term Treatment" (hyphen) in two A.3.3 documents.
- Agent Rate document (`A.3.2 - Core Stability Parameters - Agent Rate - Spark`) path corrected to include "Parameters" segment.

---

## PR #15 — 2025-06-16 weekly atlas edit proposal
**Merged:** 2025-06-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Direct Ethena exposure RRC reduced** (A.3.3): 5% → **3%** Instance Financial RRC Ratio. (Indirect Ethena through Morpho: unchanged at 3%; all other: 4%.)
- **Risk Tolerance Ratio breach definitions corrected** (A.3.3):
  - Low Severity Breach: RTR ≥ 97% and < 100% → now **RTR ≥ 100% and < 103%**
  - High Severity Breach: RTR < 97% → now **RTR > 103%**
- **Penalty payment exemption phrasing corrected** (A.3.3): Star Agents must maintain RTR "of at least 90%" → "of less than or equal to 90%" (correcting apparent inversion).
- **Penalty collection authority updated** (A.3.3): Penalties collected "by the Star Agent's Operational Executor Agent" → **by Sky Governance**.

### Context
The Ethena RRC reduction from 5%→3% lowers required risk capital for direct Ethena exposure, aligning with the indirect Morpho exposure rate. The RTR breach definition corrections appear to fix a drafting error in the original thresholds.

---

## PR #9 — Add 2025-06-12 spell changes
**Merged:** 2025-06-16 | **Type:** Spell recording (2025-06-12)

### Material Changes
- **Spark SLL inflow rate limits raised** (Spark Artifact, two instances):
  - One Spark SLL instance: maxAmount 25M → 100M USDS; slope 5M → 20M USDS/day
  - Second Spark SLL instance: maxAmount TBD → 200M; slope TBD → 100M per day
- **SparkLend reserve factors raised** for DAI, USDS, USDT, USDC: 0% / 5% → 10% across all four assets
- **ezETH cap automator parameters increased**: supply cap gap 2,000 → 5,000 ezETH; max 20,000 → 40,000 ezETH

### Context
Records the June 12, 2025 executive spell. The reserve factor increases align SparkLend stablecoin assets with risk management norms; ezETH caps double as liquid staking demand grows.

---

## PR #1 — 2025-05-26 Atlas Edit Weekly Cycle Proposal
**Merged:** 2025-06-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core Stability Parameters restructured** (A.3.2): New subsections added:
  - Role Of Core Executor Agents (A.3.2 A1, new)
  - Agent Rate and Agent Credit Line Borrow Rate parameters with explicit formulas: Base Rate relationship, subsidized rate conditions, settlement process, treatment of USDS/sUSDS/DAI balances
  - Dai Savings Rate Modification via Bounded External Access Module (BEAM) parameters
  - Star Agent Credit Rating System linkage to borrow rate
- **Risk Capital terminology established** (A.3.3): Documents reworded from "First Loss Capital" to "Junior Risk Capital (JRC)" and "Senior Risk Capital (SRC)" throughout. Full risk capital taxonomy (JRC, SRC, OVRC, TRC, RRC) formalized.

### Context
The A.3 changes in PR #1 formalize the interest rate mechanics (Agent Rate, Base Rate spread) and rename the risk capital framework. These are companion changes to the A.2 Allocation System overhaul in the same PR.

---

## PR #4 — add 2025-05-29 spell changes
**Merged:** 2025-06-04 | **Type:** Spell recording (2025-05-29)

### Material Changes
- **GSM Pause Delay**: 48 hours → **24 hours**
- **Surplus Buffer Splitter**: SKY burn allocation 100% → **50%**; SKY staker reward allocation 0% → **50%** (`burn` parameter: `1*WAD` → `WAD/2`)
- **Morpho sUSDe/USDe DDM Vault**: target exposure 375M → **275M USDS**
- **Launch Project remaining budget**: 5,000,001 USDS → **1 USDS** (SKY budget unchanged at 8,400,000)

### Context
Records the May 29, 2025 executive spell. The GSM Pause Delay halving (48h → 24h) significantly reduces the governance security buffer window. The Splitter change redirects half of the Smart Burn Engine allocation to SKY stakers. The Morpho exposure reduction and near-zero USDS Launch Project budget reflect risk reduction actions. See also Spark SLL additions (Unichain, Optimism) and rate limit increases tracked in the Spark changelog.

---
