# Stability Scope — Change History

Atlas path: `A.3` — The Stability Scope

---

## PR #246 — Atlas Edit Proposal — 2026-05-18
**Merged:** 2026-05-21 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- `A.3.2.1.2.2.1.2.1` (Initial Loss Absorption By "Tip JRC"): `“` → `"`
- `A.3.7.1.2.1.6` (ALLOCATOR-PRYSM-A Parameters): `Launch Agent 6` → `Osero`
- `A.3.7.1.6.5` (Genesis Agents): `Launch Agent 6` → `Osero`
- `A.3.7.1.6.6.1` (Amount Of Capital Contributed By Sky To Agents): `Launch Agent 6` → `Osero`
- `A.3.7.1.6.6.2.3.0.6.1` (Current Phased-Out Genesis Capital): `Launch Agent 6` → `Osero`
- `Launch Agent 6` → `Osero` across 4 docs.

---

## PR #242 — Atlas Edit Proposal — 2026-05-11
**Merged:** 2026-05-15 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Relationship To Base Rate** (`A.3.1.2.5.1`): `9` → `10`
- **Conservatorship For Breach Of Capital Requirements** (`A.3.2.2.7.2.1.4`): `8` → `9`
- **Termination Of Executor Accord** (`A.3.2.2.7.2.2.2`): `8` → `9`
- **Requirements** (`A.3.7.1.5.4.1`): `8` → `9`
- **Implementation** (`A.3.7.1.6.1`): `9` → `10`; `8` → `9`; `9` → `10`

### Housekeeping
- `9` → `10` across 2 docs.
- `Facilitators` → `Facilitator` across 1 doc.
- `8` → `9` across 4 docs.

### Context
Renumbering ripples only — bullet shifts propagate from new sub-articles added elsewhere in the May 11 weekly cycle (Poll #1632). No substantive stability-scope changes.

---

## PR #237 — Atlas Edit Proposal — 2026-05-04
**Merged:** 2026-05-08 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: Sky Savings Rate Current Value** (`A.3.1.2.2.3`, UUID `aff1868f…52eb`): documents how to read the SSR on-chain — call `ssr()` on the sUSDS contract `0xa3931d71877C0E7a3148CB7Eb4463524FEc27fbD` (Ethereum mainnet); the function returns a per-second compounding rate in RAY (10^27) precision; annualized rate = `(ssr() / 1E27)^31536000 - 1`.

### Context
Documentation only — the SSR mechanism itself is unchanged. Ratified by Poll #1631 (10-0, non-voters: excel, opex, tango).

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

## PR #213 — Update Sky forum URL
**Merged:** 2026-04-02 | **Type:** Housekeeping

`forum.sky.money` → `forum.skyeco.com` in one reference inside A.3 (Sky vault user notification context).

---

## PR #200 — 2026-03-16 Weekly Edit Proposal
**Merged:** 2026-03-20 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **ACRDX exposure cap** (`A.3.2.2.1.1.1.5.3.1.2`): new restriction — total ACRDX exposure may not increase beyond **50.97 million USDS** and should be reduced to zero over time.

---

## PR #189 — Feb 26 Exec Update
**Merged:** 2026-03-05 | **Type:** Spell recording (2026-02-26)

### Material Changes
- **ALLOCATOR-PRYSM-A Parameters** (`A.3.7.1.2.1.6`): new section — Launch Agent 6 Allocator Vault. `duty` set by SP-BEAM; `line` controlled by DC-IAM with `gap` 10M USDS, `line` 10M USDS, `ttl` 24 hours.
- **ALLOCATOR-INTERVAL-A Parameters** (`A.3.7.1.2.1.7`): new section — Launch Agent 7 Allocator Vault (parameters body added).
- **ALLOCATOR-PRYSM-A SP-BEAM Parameters** (`A.3.7.1.3.3.6`): new — `max` 3,000 bps, `min` 0 bps, `step` 400 bps, `tau` per global value.
- **ALLOCATOR-INTERVAL-A SP-BEAM Parameters** (`A.3.7.1.3.3.7`): new — same structure as PRYSM-A.

---

## PR #187 — 2026-02-23 Atlas Edit Weekly Cycle Proposal
**Merged:** 2026-03-05 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **ALLOCATOR vault parameters** (`A.3.7.1.2.1.2–.5`): intro text whitespace corrected.
- **Update Process** (`A.3.7.1.2.2`): cross-reference to Prime Allocator Vault Risk Parameters converted to UUID link.
- **Genesis Agents list** (`A.3.7.1.6.5`): whitespace normalization (no entries changed).
- **Instance Financial CRRs** (`A.3.2.2.1.1.1.5.3.1`): indentation/whitespace normalization.

---

## PR #182 — remove ALLOCATOR-NOVA-A from DC-IAM and set `line` to 0
**Merged:** 2026-02-17 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **ALLOCATOR-NOVA-A vault deactivated** (`A.3.7.1.2.1.4`): DC-IAM parameters (gap: 1M USDS, line: 60M USDS, ttl: 20 hours) removed; `line` set to a fixed 0 USDS, effectively closing the vault's debt ceiling. The `duty` parameter continues to be set by the SP-BEAM.

### Context
Removing ALLOCATOR-NOVA-A from DC-IAM and zeroing the line closes off an allocator vault that was no longer active. Companions to the allocator vault management process documented in A.3.7. Forum: https://forum.sky.money/t/allocator-nova-a-parameter-changes/27692. SKY ~$0.063, USDS supply ~$9.8B.

---

## PR #180 — Feb 9 edit
**Merged:** 2026-02-12 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Capital Types → Capital Targets** (`A.3.5.3.2`): section renamed (UUID unchanged).
- **Allocator Vault parameters** (`A.3.7.1.2.1.2–.5`): minor whitespace in intro text (no parameter value change).
- **Update Process** (`A.3.7.1.2.2`): cross-reference to Prime Allocator Vault Risk Parameters section converted from plain text to UUID hyperlink.
- **Uniswap V3** (`A.3.2.2.1.1.1.1.3.9`): stray leading-space removed from heading.

---

## PR #170 — 2026-01-29 spell changes
**Merged:** 2026-02-02 | **Type:** Spell recording (2026-01-29)

### Material Changes
- **ALLOCATOR-PATTERN-A BPEAM parameters** (`A.3.7.1.2.3.5`, new): Stability Parameter Bounded External Access Module parameters for the ALLOCATOR-PATTERN-A Allocator Vault: `max` 3,000 bps, `min` 0 bps, `step` 400 bps, `tau` as globally defined at `A.3.7.1.2.1.4.1`.

### Context
Records the January 29, 2026 Executive Spell. Adds on-chain BPEAM configuration for the Pattern-A allocator vault to the Atlas.

---

## PR #172 — Jan 26 Edit
**Merged:** 2026-01-29 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Morpho Vaults Instance Financial CRRs added** (`A.3.2.2.1.1.1.1.3.8`, new):
  - Grove x Steakhouse High Yield USDC Vault: PT-USDe/USDC 91.5% CRR 4%; PT-sUSDe/USDC 91.5% CRR 4%; PT-cUSD0/USDC 91.5% CRR 1%; mF-One/USDC 91.5% CRR 100%.
  - Grove x Steakhouse High Yield AUSD Vault (via FalconX): CRR 5%; combined FalconX cap 100M USDS.
  - Uniswap V3 AUSD/USDC (via FalconX, Monad): CRR 3%; combined FalconX cap 100M USDS.
- **Superstate Instance Financial CRRs** (`A.3.2.2.1.1.1.5.3.1`): Added STAC on Ethereum (1.6% CRR) and GACLO-1 on Ethereum (0.85% CRR); formatting changed from `◦` to `-` bullets.

---

## PR #156 — January 12 edit
**Merged:** 2026-01-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Maple instance** (`A.3.2.2.1.1.1.1.3.1`): Alternative BTC/SOL slippage parameter docs removed; replaced with Instance Financial CRR of 3% for Maple SyrupUSDC. Max exposure text updated to "will be specified in future iteration."

---

## PR #143 — 2025-12-15 Edit
**Merged:** 2026-01-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Anchorage offchain lending CRR** (`A.3.2.2.1.1.1.1.3.7`) — new: 3.5% CRR, max $200M, native BTC collateral, Initial LTV 80%, Margin Call 85%/24h, Liquidation 90%, ~6-month maturity
- `A.3.2.2.1.1.1.1.3.5` (formerly "Drift", UUID 05036471) renumbered to `.3.6`; new `.3.7` is Anchorage

---

## PR #141 — Dec 8 edit
**Merged:** 2025-12-11 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Kamino CRR parameters** (`A.3.2.2.1.1.1.1.3.5`) — new article added:
  - JLP market: USDG 4.98%, USDC 4.94%, USDT 4.91%, PYUSD 4.87%
  - Main market: USDG 1.60%, USDC 1.58%, EURC 1.48%, PYUSD 0.91%
- **Anchorage offchain lending CRR** (`A.3.2.2.1.1.1.1.3.7`) — new article added: 3.5% CRR, max exposure $200M, native BTC collateral, Initial LTV 80%, Margin Call 85%/24h, Liquidation 90%, ~6-month maturity
- `A.3.2.2.1.1.1.1.3.5` (formerly "Drift", UUID 05036471) renumbered to `.3.6`

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

## PR #126 — Add ALLOCATOR-OBEX-A SP-BEAM parameters
**Merged:** 2025-12-03 | **Type:** Spell recording

### Material Changes
- **ALLOCATOR-OBEX-A SP-BEAM parameters** (`A.3.7.1.2.3.4`) — new article added:
  - `max`: **3,000 basis points**
  - `min`: **0 basis points**
  - `step`: **400 basis points**
  - `tau`: globally defined (references `A.3.7.1.2.1.4.1`)

### Context
Records the Stability Parameter Bounded External Access Module configuration for the ALLOCATOR-OBEX-A Allocator Vault, enabling automated rate adjustments within these bounds.

---

## PR #115 — Atlas Edit Weekly Proposal 2025-11-17
**Merged:** 2025-11-20 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- `A.3.2` Agent Rate — sUSDS Treatment: "0.1% Distribution Reward Fee + 0.1% Prime Agent Management Fee" → "Distribution Reward Rate (see A.2.4)" (terminology alignment)
- `A.3.3` srUSDS section renamed: "srUSDS Accessibility Reward" → "srUSDS Distribution Reward"; SKY Borrow Minimum Rate formula updated: "stUSDS Accessibility Reward" → "stUSDS Distribution Reward"

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

## PR #103 — 2025-11-02 Weekly Cycle Edit Proposal
**Merged:** 2025-11-07 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- "Accessibility Reward Fee" → "Distribution Reward Fee" across A.3.2 (SSR / Agent Rate relationship docs) and A.3.3 (Sky Spread, srUSDS reward)
- "Risk Tolerance Ratio" → "Encumbrance Ratio" in A.3.3 Spark Centrifuge v3 parameters and Agent Credit Line Borrow Rate
- "Long Term Application To Real World Assets" reference → "Legal Recourse Assets" in Direct Ethena Exposures and Superstate CRR docs

---

## PR #98 — Adjust stUSDS Beam step parameters
**Merged:** 2025-11-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **stUSDS Beam step (first instance)**: 4,000 basis points → **500 basis points**
- **stUSDS Beam step (second instance)**: 4,000 basis points → **500 basis points**

### Context
Both stUSDS Beam instances had their `step` parameter reduced from 4,000 to 500 bps. The `max` and `min` bounds were unchanged.

---

## PR #96 — October 27 edit
**Merged:** 2025-10-31 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Minimum Actively Stabilizing Collateral** (A.3.4): 25% → **5%** minimum ASC for Prime Agents
- **Penalties for failing to satisfy ASC requirement**: 200% APY penalty removed; replaced with near-term "no penalties" + reporting requirement — Core Council Risk Advisor must develop automated detection tool; each violation reported within 24 hours to Core Facilitator, Core GovOps, Operational Facilitator/GovOps, and Prime Agent; summary included in each Independent Calculation
- **Near Term Exemption For Keel** added: Keel exempt from Minimum ASC requirement due to Solana infrastructure limitations
- **Peg Defense penalties**: 20 bps penalty removed; replaced with "will be specified in a future iteration"
- **Sky Core ALM Rules** simplified: previous 30%/20%/25% PSM band + LRRWAs rules deleted; replaced with "allocates capital to the Lite PSM" (A.3.4)
- **PSM ASC adjustment guidelines** (A.3.2): "total ASC" → **"PSM ASC"** (defined as Lite PSM ASC as % of Sky Collateral Portfolio); same band thresholds kept
- **Smart Burn Engine** (A.3.6): Surplus Buffer Splitter Parameters renamed to Smart Burn Engine Parameters; new Kicker Module added:
  - `kicker.khump`: -200,000,000 USDS (negative threshold enables burns even when surplus buffer is negative)
  - `kicker.kbump`: 10,000 USDS; `splitter.hop`: 2,880 seconds
  - 100% → SKY accumulation (0% to SKY stakers); `burn` = 100% (WAD × 1)
  - LSEV2-SKY-A USDS `rewardsDuration`: 2,880 seconds (must match hop)
  - Kicker Module activation authorized directly to October 30, 2025 Executive Vote (no prior Governance Poll required)

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
