# Spark (SLL) — Change History

Atlas path: `A.6.1.1.1` (2116 docs)

---

## PR #216 — Spark Proposal - Spark Savings - Raise Deposit Caps for spUSDC, spUSDT, spETH
**Merged:** 2026-04-27 | **Type:** Spark proposal (parameter update)

### Material Changes
- **spUSDC** (Ethereum, `A.6.1.1.1.3.5.2.2.1`) supply cap: 250M → **10B**
- **spUSDT** (Ethereum, `A.6.1.1.1.3.5.2.2.2`) supply cap: 250M → **10B**
- **spETH** (Ethereum, `A.6.1.1.1.3.5.2.2.3`) supply cap: 50,000 → **1M ETH**

### Context
40× increase in USDC/USDT deposit caps and 20× for ETH, effectively removing binding supply constraints on all three products. USDS supply at ~$11B at merge.

Forum: https://forum.skyeco.com/t/april-9-2026-proposed-changes-to-spark-for-upcoming-spell/27804

---

## PR #215 — Spark Proposal - Spark Liquidity Layer - Update Rate Limits
**Merged:** 2026-04-27 | **Type:** Spark proposal (SLL rate limit update)

### Material Changes
- **Aave Core USDT** inflow `maxAmount`: 250M → **500M USDT**
- **SparkLend ETH** inflow `slope`: 10,000 → **250,000 ETH/day**
- **Ethena USDT** inflow `maxAmount`: 10M → **100M USDT**
- **BlackRock BUIDL USDT** inflow `maxAmount`: 25M → **50M USDT**; Request Redemption `maxAmount`: 50M → **Unlimited**
- **Morpho USDT vault** (Ethereum) inflow `maxAmount`: 50M → **100M USDT**
- **Maple Finance USAT** transferAsset `maxAmount`: 5M → **50M USAT**
- **Maple Finance USDT** transferAsset `maxAmount`: 5M → **50M USDT**
- **SKY↔token swap** (`A.6.1.1.1.2.6.1.3.1.7.1`): `maxAmount` 5M → 10M, `slope` 20M → 200M/day, max slippage 0.15% → **0.25%**
- **Secondary swap** (`A.6.1.1.1.2.6.1.3.1.7.5`): `maxAmount` 100 → 1,000, `slope` 1,000 → **50,000/day**
- **Conduit closures** (`maxAmount` and outflow set to 0): 3× USDS conduits, 2× USDC conduits, 1× sUSDS/fsUSDS conduit on Ethereum; additional USDC/USDS conduits on Base and Avalanche

### Context
Batch rate limit update ahead of the April 23, 2026 Executive Vote. The SparkLend ETH slope increase (25× to 250K ETH/day) and swap rate expansions indicate SLL scaling capacity across multiple protocols. Conduit closures decommission inactive pathways.

Forum: https://forum.skyeco.com/t/april-9-2026-proposed-changes-to-spark-for-upcoming-spell/27804

---

## PR #214 — SAEP-14: Update Offchain Collateralized Lending Artifact Section
**Merged:** 2026-04-27 | **+11/-3 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.6.1.1.1.3.8.2.2.2.6` - Gold (AU) [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #210 — Spark proposal - Morpho Vault Curation
**Merged:** 2026-04-27 | **Type:** Spark proposal (Morpho vault curation)

### Material Changes
- **Market Exposure section added** to Spark Blue Chip USDT Morpho Vault (`A.6.1.1.1.2.6.1.3.1.8.4`, Ethereum): 4 approved pool exposure limits:
  - sUSDS/USDT 96.5% LLTV: Unlimited absolute / 100% relative
  - wstETH/USDT 86% LLTV: 250M absolute / 100% relative
  - WBTC/USDT 86% LLTV: 100M absolute / 100% relative
  - cbBTC/USDT 86% LLTV: 250M absolute / 100% relative

### Housekeeping
- Contract Addresses renumbered `.4.4.1` → `.4.4.2`, Timelock renumbered `.4.4.2` → `.4.4.3` to accommodate the new Market Exposure section at `.4.4.1`.

### Context
First use of the SAEP-13 Risk Curation Framework (PR #209): the pool exposure limits represent governance-approved bounds within which Soter Labs (Curator) can operate. Note the inflow `maxAmount` for this same vault was also raised 50M → 100M USDT in the same week (PR #215).

---

## PR #209 — SAEP-13: Risk Curation Framework
**Merged:** 2026-04-27 | **Type:** SAEP-13 (Spark proposal)

### Material Changes
- **New: Risk Curation Framework** (`A.6.1.1.1.3.9`, UUID `78018ebc…190edca1`): governance framework for delegating on-chain risk management to approved Curator roles within Morpho vaults; requires prior governance poll approval for each action, minimum 3-day public timelock, and independent Guardian with cancellation authority (also cancellable by Spark subdao proxy)
- **4 approved instances:**
  - Spark USDS Morpho Vault (Ethereum) — `0xe41a0583…FE0597`
  - Spark Blue Chip USDC Morpho Vault (Ethereum) — `0x56A76b42…d581D`
  - Spark Blue Chip USDT Morpho Vault (Ethereum) — `0xc7CDcFDE…bD22`
  - Spark USDC Morpho Vault (Base) — `0x7BfA7C4f…CBF34A`
  - Curator for all: Soter Labs at `0x0f963A8A…0646A3` (3/5 multisig)
  - Guardian for all: Spark Foundation at `0xf5748bBe…C908B` (3/5 multisig)

### Context
SAEP-13 codifies the governance layer for Spark's Morpho vault curator operations. Curator actions are now subject to explicit poll approval and a mandatory 3-day onchain timelock, with forum reporting within 24 hours required. PR #210 is the first use of this framework.

Forum: https://forum.skyeco.com/t/saep-13-risk-curation-framework/27796/1

---

## PR #224 — Atlas Edit Proposal — 2026-04-20
**Merged:** 2026-04-24 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- Distribution Requirement Primitive (`A.6.1.1.1.2.3.1`) renamed to "Ecosystem Upkeep Fee Primitive"; Market Cap Fee Primitive subtree (`A.6.1.1.1.2.3.2` — Market Cap Fee) deleted; Upkeep Rebate docs updated to reference unified fee structure. Same UUID preserved.

---

## PR #219 — Atlas Edit Proposal — 2026-04-06

**Merged:** 2026-04-09 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping

- "SLL" abbreviation expanded to "Spark Liquidity Layer" throughout Spark's Allocation System Primitive section (A.6.1.1.1.2.6.1): affects document titles (e.g., "Asset Supplied By SLL" → "Asset Supplied By Spark Liquidity Layer" across ~20 documents), section headers, and introductory text. Same UUIDs; no content changes.

### Context

Pure cosmetic rename following the SLL/GLL abbreviation expansion policy introduced in this weekly edit. No operational impact.

---

## PR #185 — SAEP-10: Update Offchain Collateralized Lending Artifact Section

**Merged:** 2026-03-20 | **Type:** SAEP-10 (Spark proposal) | **+7/-5 lines**

### Material Changes

- **Anchorage offchain lending — capacity 5× expansion** (`A.3.2.2.1.1.1.1.3.7`, referenced from Stability Scope): Venue exposure limit $200M → **$1B**; Anchorage Innovations sub-limit $200M → **$1B**. Note: the Anchorage CRR is concurrently recorded as 3.5% → **3%** in the Stability Scope document for this instance (cross-referenced here, tracked in A.3)
- **Critical actions — whitelist-based framing** (`A.6.1.1.1.3.8.2.7`): the "Transferring funds to an address under control of an external entity other than SAF / Spark Foundation / approved collateral agent / SLL" criterion was replaced with **"Transferring funds to an address outside of the preexisting withdrawal address whitelist"** — simpler bright-line test
- **Address whitelist — borrower addresses permitted** (`A.6.1.1.1.3.8.2.7.2`): whitelist may now include **borrower addresses in connection with offchain collateralized lending agreements** in addition to collateral agents and the SLL
- **Transfers — added fee-payment authorization** (`A.6.1.1.1.3.8.2.7.4`): transfers to collateral agents now require SAF confirmation of pre-disbursement completion (language clarified); new authorization for transfers to **custodian/collateral-manager fee addresses** upon valid invoice per governance-approved arrangements

### Context

SAEP-10 is an agent-specific Spark proposal loosening the operational framework for offchain collateralized lending as Anchorage-routed capacity scales 5x to $1B. The whitelist-based "critical action" test is a material simplification: previously the rule enumerated which entity types were non-critical (SAF, Spark Foundation, collateral agents, SLL), which made any transfer to a borrower require complex legal review; now the criterion is purely whether the destination appears on the preexisting whitelist. Combined with the explicit authorization to whitelist borrower addresses directly and pay custodian invoices, this transitions offchain lending from a narrow infrastructure-transfer model toward an operationally richer model where SAF-approved whitelists carry the governance weight. The scale-up to $1B is the headline risk change. SKY ~$0.074, USDS supply ~$11.5B at merge.

Forum discussion: [https://forum.sky.money/t/saep-10-update-offchain-collateralized-lending-artifact-section/27718](https://forum.sky.money/t/saep-10-update-offchain-collateralized-lending-artifact-section/27718)

---

## PR #184 — Spark Proposal - SLL - Onboard Morpho v2 USDT Vault

**Merged:** 2026-03-20 | **Type:** Spark proposal (new SLL instance) | **+100/-0 lines**

### Material Changes

- **New instance: Ethereum Mainnet — Morpho USDT Instance** (`A.6.1.1.1.2.6.1.3.1.8.4`): fourth Morpho SLL instance after DAI/USDS/USDC, rounding out Spark's Morpho-based stablecoin vault coverage on Ethereum
  - Network: Ethereum Mainnet, Protocol: Morpho, Asset: USDT, Token: **sparkUSDT**
  - Token Address: `0xc7CDcFDEfC64631ED6799C95e3b110cd42F2bD22`
  - Underlying: `0xdac17f958d2ee523a2206206994597c13d831ec7` (USDT)
  - Allocator Role: `0x9Ad87668d49ab69EEa0AF091de970EF52b0D5178`
  - Curator Role: `0x0f963A8A8c01042B69054e787E5763ABbB0646A3`
  - Guardian Role: `0xf5748bBeFa17505b2F7222B23ae11584932C908B`
  - Timelock: **240 hours (10 days)**
  - Inflow rate limits: `maxAmount` **50M USDT**, `slope` **1B USDT/day**
  - Outflow rate limits: Unlimited / Unlimited
  - RRC Framework Full Implementation: `Pending`
  - Rate Limit IDs: to be specified in a future iteration of the Spark Artifact

### Context

Fourth Morpho-protocol USDT vault onboarded to the SLL, completing the USDC/USDS/DAI/USDT matrix for Morpho after PR #71/#72 first established Morpho as an SLL venue in October 2025. The 50M inflow cap with a 1B/day slope is the same sizing pattern as the USDT rate-limit adjustments made concurrently in PR #183 (SparkLend/Aave USDT inflow slopes set to 2B and 1B per day respectively), indicating a coordinated push to expand Spark's USDT-denominated lending exposure. The `Pending` RRC framework status means the Risk Advisor has not yet certified this instance, consistent with other newly-onboarded Morpho vaults. SKY ~$0.074, USDS supply ~$11.5B at merge.

Forum discussion: [https://forum.sky.money/t/february-26-2026-proposed-changes-to-spark-for-upcoming-spell/27719](https://forum.sky.money/t/february-26-2026-proposed-changes-to-spark-for-upcoming-spell/27719)

---

## PR #183 — Spark Proposal - SLL - Adjust Rate Limits for SparkLend USDT, Aave Core USDT, and Maple syrupUSDT

**Merged:** 2026-03-20 | **Type:** Spark proposal (SLL rate limit adjustments) | **+16/-6 lines**

### Material Changes

- **SparkLend USDT Instance — inflow rate limits raised:**
  - `maxAmount`: 100M USDT → **250M USDT**
  - `slope`: 200M USDT/day → **2B USDT/day** (10x)
- **Aave Core USDT Instance — inflow rate limits reset and denominated in USDT** (previously recorded as USDC due to copy-paste): was `maxAmount` 50M USDC / `slope` 25M USDC/day → now **`maxAmount` 10M USDT / `slope` 1B USDT/day** (40x slope expansion)
- **Maple syrupUSDT Instance — inflow rate limits rescaled for redemption-request model:**
  - `maxAmount`: 50M USDT → **25M USDT** (halved)
  - `slope`: 10M USDT/day → **100M USDT/day** (10x)
  - Outflow: added explicit `slope: Unlimited` alongside existing `maxAmount: Unlimited`
- **Maple syrupUSDT — new Request Redemption Parameters** (`A.6.1.1.1.2.6.1.3.1.3.2.4.1`): `maxAmount` 50M USDT, `slope` 500M USDT/day. New "Instance-specific Operational Parameters" parent section (`A.6.1.1.1.2.6.1.3.1.3.2.4`) added to host the redemption rate-limit subsection.

### Context

These three parameter adjustments were bundled with PR #184 (Morpho v2 USDT Vault onboarding) and originate from the same February 26, 2026 Spark proposal. The slope expansions on SparkLend and Aave USDT inflows indicate strong USDT demand — SparkLend's 10x slope increase to 2B USDT/day is the most aggressive individual rate-limit change in Spark's Ethereum SLL to date. The Aave Core correction is noteworthy: the prior values were denominated in USDC, which appears to have been an error carried from the instance template; this PR both expands the cap and corrects the denomination. The new Request Redemption Parameters section for Maple operationalizes the redemption-request mechanics specific to syrupUSDT's queued-withdrawal model. SKY ~$0.074, USDS supply ~$11.5B, BTC ~$70.5K at merge.

Forum discussion: [https://forum.sky.money/t/february-26-2026-proposed-changes-to-spark-for-upcoming-spell/27719](https://forum.sky.money/t/february-26-2026-proposed-changes-to-spark-for-upcoming-spell/27719)

---

## PR #134 — Spark proposal - Onboard Spark Prime / Arkis

**Merged:** 2025-12-15 | **Type:** Spark proposal (new SLL instance)

### Material Changes

- **New SLL instance: Arkis (Ethereum Mainnet)** — first prime-brokerage-style instance in the Spark Liquidity Layer (`A.6.1.1.1.2.6.1.3.1.10`)
  - **Asset:** USDC; **Token:** spUSDC (`0x377C3bd93f2a2984E1E7bE6A5C22c525eD4A4815`); Underlying: USDC (`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`)
  - **Inflow rate limits:** maxAmount 5,000,000 USDC; slope 5,000,000 USDC/day
  - **Outflow rate limits:** maxAmount Unlimited
  - **RRC Framework:** Pending
  - **Interim Deployment status:** CRR 100%; Maximum Exposure $20 million across all Arkis interim deployments
  - Pool address and Rate Limit IDs deferred to a future Spark Artifact iteration

### Context

This instance accompanies SAEP-07 (PR #138, same spell) which established the full Spark Prime Brokerage policy framework (`A.6.1.1.1.3.7`). The SLL instance gives Spark a funded conduit into the Arkis prime brokerage infrastructure; the modest 5M USDC inflow cap and Interim Deployment designation reflect an initial testing phase. SKY ~$0.058, USDS supply ~$9.9B.

Forum discussion: https://forum.sky.money/t/december-11-2025-proposed-changes-to-spark-for-upcoming-spell/27481

---

## PR #140 — SAEP-08

**Merged:** 2025-12-11 | **Type:** SAEP-08 (Spark proposal)

### Material Changes

- **New framework: Offchain Collateralized Lending** (`A.6.1.1.1.3.8`) — traditional secured lending to institutional borrowers, distinct from the Arkis prime brokerage model (+225 lines)
  - **Counterparty requirements:** KYC/KYB handled by custodians/collateral agents; borrowers self-certify solvency; insolvency triggers immediate full repayment
  - **Marginable assets (5 types with LTV tiers):**
    - BTC: Initial 80% / Maintenance 85% / Liquidation 90%; exposure unlimited; wrapped: cbBTC, LBTC
    - ETH: Initial 70% / Maintenance 85% / Liquidation 90%; exposure unlimited; wrapped: WETH, stETH, weETH, lsETH
    - XRP: Initial 60% / Maintenance 70% / Liquidation 80%; exposure $25M
    - SOL: Initial 70% / Maintenance 80% / Liquidation 85%; exposure $100M; wrapped: JitoSOL
    - HYPE: Initial 60% / Maintenance 70% / Liquidation 80%; exposure $25M; wrapped: kHYPE
  - **Approved venues:** Anchorage only — venue exposure limit $200M; collateral agent Anchorage Innovations $200M
  - **Loan terms:** revolving/evergreen or fixed up to 6 months (longer than prime brokerage's 1-month cap); minimum borrow rate = max(Sky Savings Rate + 1.5%, SOFR + 2%)
  - **Margin call cure period:** 24 hours from Maintenance LTV breach
  - **Cross-default clause:** default on one Spark loan permits Spark to accelerate all other loans from same borrower
  - **Account management:** 3-signer quorum for critical actions; signers from Spark Asset Foundation, Phoenix Labs, Spark Operational Executor Agent

### Context

SAEP-08 creates a simpler, more conventional secured-lending product alongside SAEP-07's prime brokerage. Key differences: lower borrow rate floor (SSR+1.5% vs SSR+2%), longer fixed terms (6 months vs 1 month), LTV-based risk model rather than margin account haircuts, and a single venue (Anchorage) versus SAEP-07's multi-exchange setup. The unlimited BTC and ETH exposure limits signal high confidence in these assets as collateral; the $200M Anchorage cap is the binding constraint for initial deployments. SKY ~$0.055, USDS supply ~$9.7B.

Forum discussion: https://forum.sky.money/t/saep-08-offchain-collateralized-lending/27487

---

## PR #138 — SAEP-07

**Merged:** 2025-12-11 | **Type:** SAEP-07 (Spark proposal)

### Material Changes

- **New framework: Spark Prime Brokerage** (`A.6.1.1.1.3.7`) — full governance and policy architecture for allocating capital via the Arkis prime brokerage infrastructure (+301 lines)
  - **Counterparty requirements:** KYC/KYB handled by Arkis; borrowers must be solvent and not sanctions-listed; insolvency triggers immediate full repayment
  - **Marginable assets (14 categories):** BTC (±20% haircut, unlimited exposure), ETH (±20%, unlimited), XRP (±20%, $50M), SOL (±20%, $100M), DOGE/ADA (±25%, $25M each), HYPE (±25%, $50M), ZEC/AVAX/SUI/NEAR (±30%, $20M each), USDe (−10%, $500M), USDT/USDC (0%, unlimited); plus Pendle PTs, perpetual/calendar futures on approved assets
  - **Approved venues:** Onchain (unlimited), Binance/OKX/Bybit/Anchorage/Bitgo ($100M each), Hyperliquid Hypercore ($50M), Bitget ($25M)
  - **Loan terms:** duration revolving/evergreen or fixed up to 1 month; minimum borrow rate = max(Sky Savings Rate + 2%, SOFR + 2.5%)
  - **Policy change mechanism:** Root Edit Primitive; policy changes must be executed promptly or all Arkis funding must be withdrawn
  - **Account management:** critical actions (whitelist changes, signer changes, external transfers) require 3-signer quorum with no single entity holding sufficient signers alone; signers from Spark Asset Foundation, Phoenix Labs, or Spark Operational Facilitator

### Context

SAEP-07 establishes Spark's entry into prime brokerage — a qualitatively new business line that allows leveraged trading by institutional borrowers against a broad collateral set. Paired with PR #134 (Arkis SLL instance) and PR #140 (SAEP-08, offchain collateralized lending), December 2025 marks Spark's pivot beyond on-chain lending into institutional capital markets. The $500M USDe exposure limit is striking — reflecting Ethena's stablecoin characteristics and deep liquidity. SKY ~$0.055, USDS supply ~$9.7B.

Forum discussion: https://forum.sky.money/t/saep-07-spark-prime-brokerage/27486

---

## PR #132 — Spark proposal - Update allocator roles to ALM Proxy Freezable
**Merged:** 2025-12-11 | **Type:** Spark proposal (role rotation)

### Material Changes
- **Allocator Role Address added** for three Spark Savings instances:
  - Spark Savings spUSDC (Ethereum): Allocator Role → `0x9Ad87668d49ab69EEa0AF091de970EF52b0D5178`
  - Spark Savings spUSDT (Ethereum): Allocator Role → `0x9Ad87668d49ab69EEa0AF091de970EF52b0D5178`
  - Spark Savings spUSDC (Base): Allocator Role → `0xCBA0C0a2a0B6Bb11233ec4EA85C5bFfea33e724d`

### Context
Sets the Allocator Role to the ALM Proxy Freezable contract for Spark Savings instances — the same address (`0x9Ad87...`) used as the Setter role in PR #130. Coordinates with PR #130's Setter role update; both PRs shipped on 2025-12-11.

---

---

## PR #131 — Spark proposal - Launch Spark Savings spPYUSD
**Merged:** 2025-12-11 | **Type:** Spark proposal (new Spark Savings instance)

### Material Changes
- **Spark Savings spPYUSD onboarded** (A.6.1.1.1.2.6.1.3.1.9.4, new): new Spark Savings v2 instance accepting PYUSD deposits on Ethereum Mainnet
  - Token: spPYUSD (`0x80128DbB9f07b93DDE62A6daeadb69ED14a7D354`), underlying PYUSD (`0x6c3ea9036406852006290770bedfcaba0e23a0e8`)
  - Supply cap: 250,000,000 PYUSD; Max yield: 10%; Current yield (at launch): 0%
  - Default admin: `0x3300f198988e4C9C63F75dF86De36421f06af8c4`; Setter: `0x9Ad87668d49ab69EEa0AF091de970EF52b0D5178` (ALM Proxy Freezable); Taker: `0x1601843c5E9bC251A3272907010AFa41Fa18347E`
  - Rate limits: Take unlimited; Transfer unlimited; RRC: Covered

---

## PR #130 — Spark Proposal - Spark Savings - Update Setter Role to ALM Proxy Freezable for spUSDC, spUSDT, spETH
**Merged:** 2025-12-11 | **Type:** Spark proposal (role rotation)

### Material Changes
- **Setter role updated** on four Spark Savings instances (Ethereum Mainnet + Avalanche):
  - spUSDC (Ethereum): Setter `0x2E1b01adABB8D4981863394bEa23a1263CBaeDfC` → `0x9Ad87668d49ab69EEa0AF091de970EF52b0D5178`
  - spUSDT (Ethereum): same rotation as above
  - spETH (Ethereum): same rotation as above
  - spUSDC (Avalanche): Setter `0x2E1b01adABB8D4981863394bEa23a1263CBaeDfC` → `0x45d91340B3B7B96985A72b5c678F7D9e8D664b62`

### Context
Migrates yield-setting authority on Spark Savings from the prior Setter multisig to the ALM Proxy Freezable contract. The new Setter (`0x9Ad87...` on Ethereum, `0x45d91...` on Avalanche) is a freezable proxy — adds an emergency freeze capability to rate-setting authority. Coordinates with PR #132 which adds matching Allocator Role addresses on the same day.

---

## PR #137 — Filling in Spark Savings v2 Instance Configuration Document Locations and fixing titles

**Merged:** 2025-12-04 | **Type:** Housekeeping

Three Spark Savings v2 instance location documents (ETH, USDC, USDT at `A.6.1.1.1.2.6.1.1.2.1.11.1–.3`) had placeholder titles containing redundant document-name suffixes and missing hyperlink targets — both corrected. Document titles trimmed to standard format; body text now points to the correct instance configuration documents (`A.6.1.1.1.2.6.1.3.1.9.1–.3`). No parameter changes.

---

## PR #109 — SAEP-04: Strategic Investment in Arkis

**Merged:** 2025-11-19 | **Type:** SAEP-04 (Spark proposal) | **+94/-0 lines**

### Material Changes

- **New framework: Strategic Investments** (`A.6.1.1.1.3.9`): establishes Spark's authority and governance process for undertaking strategic investments — policy changes via Root Edit Primitive, new investments require Spark governance approval
- **Delegation of authority:** Spark Foundation and/or Spark Assets Foundation may hold legal ownership and exercise rights (shareholder voting, conversion, information rights) on behalf of the Spark ecosystem
- **First investment: Arkis** (`A.6.1.1.1.3.9.2.1`): $4M USDS investment via SAFE + token warrant at $45M post-money valuation
  - Investing entity: Spark Foundation → PRM LBS LTD (`0xD5FF...77a5`)
  - Deal structure: YCombinator-style SAFE, token warrant (≥50% of equity-proportional token share), side letter with MFN/pro-rata/information/major-investor rights, board seat
  - Fee reduction: 50% discount vs. lowest rate for any other Arkis user, 5 years + 2-year extension option
  - Spark Foundation empowered to exercise all investment rights per professional judgement

### Context

SAEP-04 marks Spark's first strategic investment, establishing both the framework and the inaugural deal simultaneously. Arkis provides prime brokerage infrastructure that complements Spark's existing lending products — the investment aligns with Spark's expansion into institutional-grade lending (see SAEP-07/SAEP-08 for the Prime Brokerage and Offchain Collateralized Lending frameworks added in the same period). At the time of the merge, SKY was trading around $0.043–0.050 and USDS supply was ~$9.3B.

Forum discussion: [https://forum.sky.money/t/saep-04-strategic-investment-in-arkis/27378](https://forum.sky.money/t/saep-04-strategic-investment-in-arkis/27378)

---

## PR #108 — Minor fixes

**Merged:** 2025-11-19 | **Type:** Housekeeping

### Housekeeping

- Fixed copy-pasted Target Liquidity descriptions: "Spark Savings USDC on Ethereum" → correct token name for USDT, ETH, and Avalanche USDC instances
- Added accidentally skipped "Rewards Rate Current Configuration" parent document for Spark Savings

### Context

Corrective housekeeping — the Target Liquidity text for three Spark Savings instances was erroneously copy-pasted from the USDC template. No parameter values changed.

---

## PR #106 — Spark proposal: Onboard cbETH and ETH market exposure to Morpho USDC vault

**Merged:** 2025-11-07 | **Type:** Spark proposal (new market exposure) | **+42/-0 lines**

### Material Changes

- **New section: Instance-specific Operational Parameters** added to the Morpho USDC Instance Configuration Document, with Market Exposure subsection
- **New market: ETH/USDC 86% LLTV Pool** onboarded — Pool ID `0x8793cf...1bda`, supply cap 1,000,000,000
- **New market: cbETH/USDC 86% LLTV Pool** onboarded — Pool ID `0x1c21c5...2fad`, supply cap 50,000,000

### Context

This proposal extends Spark's Morpho USDC vault exposure by adding two ETH-denominated collateral pools, enabling the vault to earn yield from ETH and cbETH borrowers against USDC. The 20:1 ratio between the ETH pool cap (1B) and cbETH pool cap (50M) reflects the relative liquidity and risk profiles of the two assets. This is part of Spark's broader strategy to diversify SLL yield sources beyond stablecoin-on-stablecoin lending. SKY was ~$0.043–0.055, USDS supply ~$9.1–9.4B.

Forum discussion: [https://forum.sky.money/t/november-13-2025-proposed-changes-to-spark-for-upcoming-spell/27354](https://forum.sky.money/t/november-13-2025-proposed-changes-to-spark-for-upcoming-spell/27354)

---

## PR #105 — Spark proposal - Increase Deposit Caps for spUSDC, spUSDT, and spETH

**Merged:** 2025-11-07 | **Type:** Spark proposal (risk parameter update) | **+3/-3 lines**

### Material Changes

- **Spark Savings spETH supply cap:** 50,000 WETH → **100,000 WETH** (2x increase)
- **Spark Savings spUSDC supply cap:** 250,000,000 USDC → **500,000,000 USDC** (2x increase)
- **Spark Savings spUSDT supply cap:** 250,000,000 USDT → **500,000,000 USDT** (2x increase)

### Context

A straightforward doubling of deposit caps across all three Spark Savings v2 vaults launched in PR #90, likely in response to vaults approaching their initial caps faster than expected. The increases signal strong demand for Spark's yield products. At the time, SKY was trading around $0.043–0.055 and USDS supply was ~$9.1–9.4B.

Forum discussion: [https://forum.sky.money/t/november-13-2025-proposed-changes-to-spark-for-upcoming-spell/27354](https://forum.sky.money/t/november-13-2025-proposed-changes-to-spark-for-upcoming-spell/27354)

---

## PR #81 — Spark Proposal - [Ethereum] SparkLend - Increase tBTC Supply and Borrow Caps

**Merged:** 2025-10-29 | **Type:** Spark proposal (risk parameter update) | **+1/-1 lines**

### Material Changes

- **tBTC cap automator — supply cap max:** 500 tBTC → **1,000 tBTC** (2x increase)
- **tBTC cap automator — borrow cap max:** 250 tBTC → **900 tBTC** (3.6x increase)

### Context

Companion to PR #80 (cbBTC cap increase), this raises tBTC limits with a similar pattern — moderate supply expansion with more aggressive borrow cap growth. The borrow cap max (900 tBTC) approaches the new supply cap (1,000 tBTC), indicating high utilization expectations for Threshold's wrapped BTC product. SKY was ~$0.059–0.063, USDS supply ~$8–9B.

Forum discussion: [https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309](https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309)

---

## PR #80 — Spark Proposal - [Ethereum] SparkLend - Increase cbBTC Supply and Borrow Caps

**Merged:** 2025-10-29 | **Type:** Spark proposal (risk parameter update) | **+1/-1 lines**

### Material Changes

- **cbBTC cap automator — supply cap max:** 10,000 cbBTC → **20,000 cbBTC** (2x increase)
- **cbBTC cap automator — borrow cap max:** 500 cbBTC → **10,000 cbBTC** (20x increase)

### Context

A significant increase in cbBTC caps, particularly on the borrow side (20x), reflecting growing demand for borrowing against Coinbase's wrapped Bitcoin on SparkLend. The supply cap increase is more conservative (2x), suggesting Spark is cautiously expanding collateral capacity while substantially unlocking borrowing demand. SKY was ~$0.059–0.063, USDS supply ~$8–9B.

Forum discussion: [https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309](https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309)

---

## PR #93 — Fix location of Ethena PT documents from 2025-10-13 edit

**Merged:** 2025-10-24 | **Type:** Fix (document relocation) | **+1102/-1102 lines**

### Housekeeping

- Moved Ethena PT-USDe and PT-sUSDe Instance Configuration Documents from incorrect inline location to proper Instance Configuration Document sections, replacing the inline content with Location pointer documents
- Large line count (+1102/-1102) is entirely structural relocation — no parameter values, contract addresses, or policy content changed

### Context

A pure structural fix correcting the placement of Ethena PT (Pendle Token) documents that were incorrectly positioned in the October 13 weekly edit. The documents needed to be in the Instances Directory as location pointers, with full configuration documents in the proper Instance Configuration Document section. No operational impact.

---

## PR #91 — Spark proposal: Spark Liquidity Layer - Update Controller to v1.7

**Merged:** 2025-10-24 | **Type:** Spark proposal (contract upgrade) | **+60/-12 lines**

### Material Changes

- **ALM Controller (MainnetController) — contract address updated:** `0xF8Dff673b555a225e149218C5005FC88f4a13870` → `0x577Fa18a498e1775939b668B0224A5e5a1e56fc3`
- **ALM Controller (MainnetController) — version document added:** new "Contract Version" document, value: 1.7
- **ALM Controller (ForeignController Base) — contract address updated:** `0xB94378b5347a3E199AF3575719F67A708a5D8b9B` → `0xC0bcbb2554D4694fe7b34bB68b9DdfbB55D896BC`
- **ALM Controller (ForeignController Base) — version document added:** version 1.7
- **ALM Controller (ForeignController Arbitrum) — contract address changed:** previous address → **TBC** (pending deployment)
- **ALM Controller (ForeignController Arbitrum) — version document added:** version 1.7
- **ALM Controller (ForeignController Unichain) — contract address changed:** `0x9B1BEB11CFE05117029a30eb799B6586125321FF` → **TBC** (pending deployment)
- **ALM Controller (ForeignController Unichain) — version document added:** version 1.7
- **ALM Controller (ForeignController Optimism) — contract address changed:** `0x1d54A093b8FDdFcc6fBB411d9Af31D96e034B3D5` → **TBC** (pending deployment)
- **ALM Controller (ForeignController Optimism) — version document added:** version 1.7
- **ALM Controller (ForeignController Avalanche) — contract address changed:** `TBD` → `0x4E64b576F72c237690F27727376186639447f096`
- **ALM Controller (ForeignController Avalanche) — version document added:** version 1.7

### Housekeeping

- All "Contract" document titles split into separate "Contract Address" and "Contract Version" documents (6 controllers x 2 = 12 title changes)
- "ALM Rate Limits (Mainnet) Contract" renamed to "ALM Rate Limits (Mainnet) Contract Address" (no value change)

### Context

A coordinated upgrade of all ALM Controller contracts across six chains to version 1.7. Mainnet and Base received new contract addresses immediately, while Arbitrum, Unichain, and Optimism were marked TBC (pending deployment at time of merge). Avalanche went from TBD to a concrete address, consistent with PR #90's Avalanche expansion in the same batch. The structural change of splitting contract documents into separate Address and Version fields improves auditability for future upgrades. SKY was ~$0.059–0.063, USDS supply ~$8–9B.

Forum discussion: [https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309](https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309)

---

## PR #90 — Spark Savings

**Merged:** 2025-10-24 | **Type:** Spark proposal (new product launch) | **+976/-0 lines**

### Material Changes

- **New product: Spark Savings v2** — complete framework added with three initial vaults on Ethereum Mainnet and one on Avalanche
- **Ethereum Mainnet — spETH vault** (Spark Savings v2 ETH Instance):
  - Token: spETH (`0xfE6eb3b609a7C8352A241f7F3A21CEA4e9209B8f`), underlying: wETH (`0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`)
  - Supply cap: 50,000 WETH, max yield: 5%, current yield: 0%
  - Take and TransferAssets rate limits: Unlimited
- **Ethereum Mainnet — spUSDC vault** (Spark Savings v2 USDC Instance):
  - Token: spUSDC (`0x28B3a8fb53B741A8Fd78c0fb9A6B2393d896a43d`), underlying: USDC (`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`)
  - Supply cap: 250,000,000 USDC, max yield: 10%, current yield: 0%
  - Take and TransferAssets rate limits: Unlimited
- **Ethereum Mainnet — spUSDT vault** (Spark Savings v2 USDT Instance):
  - Token: spUSDT, underlying: USDT
  - Supply cap: 250,000,000 USDT, max yield: 10%, current yield: 0%
  - Take and TransferAssets rate limits: Unlimited
- **Avalanche — spUSDC vault** (Avalanche Spark Savings v2 USDC Instance):
  - Supply cap: 2,000,000 USDC, max yield: 10%, current yield: 0%
- **Instances Directory updated** with Spark Savings V2 sections for Ethereum Mainnet and Avalanche, plus Avalanche Aave v3 USDC location document
- **Contract roles** (shared across ETH/USDC/USDT vaults): Spark Vault v2 Implementation (`0x1b99...f455`), Default admin (`0x3300...8c4`), Setter (`0x2E1b...DfC`), Taker (`0x1601...347E`)

### Context

PR #90 is the foundational launch of Spark Savings v2, a new yield product line distinct from SparkLend. Unlike SLL instances (which allocate protocol-controlled capital to external yield sources), Spark Savings vaults accept user deposits directly and pay yield set by Spark governance. The three Ethereum vaults cover the major asset categories (ETH, USDC, USDT) with substantial initial caps ($250M each for stablecoins, 50K ETH). The Avalanche spUSDC vault with its 2M cap signals a cautious cross-chain rollout. All vaults launch at 0% yield, with governance setting rates post-deployment. SKY was ~$0.059–0.063, USDS supply ~$8–9B.

Forum discussion: [https://forum.sky.money/t/october-2-2025-proposed-changes-to-spark-for-upcoming-spell/27191](https://forum.sky.money/t/october-2-2025-proposed-changes-to-spark-for-upcoming-spell/27191)

---

## PR #87 — SAEP-02: Modify Spark Liquidity Layer Core Relayer and Freezer Multisig Configuration

**Merged:** 2025-10-24 | **Type:** SAEP-02 (Spark proposal) | **+12/-8 lines**

### Material Changes

- **Core Operator Relayer Multisig — control expanded:** was controlled solely by Amatsu → now jointly controlled by Amatsu and Spark Assets Foundation (SAF)
- **Core Operator Relayer Multisig — threshold changed:** 2/3 → **2/5** signing requirement
- **Core Operator Relayer Multisig — signers restructured:** was 3 Amatsu addresses → now **Amatsu (2), SAF (2), Phoenix Labs (1)**. Phoenix Labs may create and propose transactions but execution still requires the 2/5 threshold.
- **Freezer Multisig — control transferred:** was controlled by Governance Facilitators → now controlled by **SAF, Phoenix Labs, and VoteWizard**
- **Freezer Multisig — threshold lowered:** 2/4 → **1/4** signing requirement
- **Freezer Multisig — signers replaced:** was VoteWizard, JanSky, LDR, CivicSage (all Governance Facilitator-aligned) → now **SAF (1), Phoenix Labs (2), VoteWizard (1)**

### Context

SAEP-02 restructures operational security for Spark's two critical multisigs, shifting control from Governance Facilitator-aligned signers toward the Spark-adjacent entities (SAF, Phoenix Labs). The Relayer multisig controls the RELAYER_ROLE for Spark Liquidity Layer operations; the Freezer multisig can invoke the FREEZER_ROLE to halt operations in emergencies. The 1/4 Freezer threshold means any single signer can freeze — optimizing for emergency response speed over consensus. This is part of a broader pattern of Spark operational decentralization from Sky governance. SKY was ~$0.059, USDS supply ~$9.1B.

Forum discussion: [https://forum.sky.money/t/saep-02-modify-spark-liquidity-layer-core-relayer-and-freezer-multisig-configuration/27318](https://forum.sky.money/t/saep-02-modify-spark-liquidity-layer-core-relayer-and-freezer-multisig-configuration/27318)

---

## PR #85 — Spark proposal - Spark Liquidity Layer - Onboard syrupUSDT

**Merged:** 2025-10-24 | **Type:** Spark proposal (new SLL instance) | **+159/-0 lines**

### Material Changes

- **New SLL instance: Maple USDT** — full Instance Configuration Document added for syrupUSDT vault on Ethereum Mainnet
  - Target protocol: Maple; Asset: USDT; Token: syrupUSDT
  - Token address: `0x356B8d89c1e1239Cbbb9dE4815c39A1474d5BA7D`
  - Underlying asset: `0xdAC17F958D2ee523a2206206994597C13D831ec7` (USDT)
  - Inflow rate limits: maxAmount 50,000,000 USDT, slope 10,000,000 USDT/day
  - Outflow rate limits: maxAmount Unlimited
- **New location document:** Maple USDT Instance Configuration Document Location added to Instances Directory

### Context

Extends Spark's Maple integration from USDC-only (existing syrupUSDC instance) to include USDT, via the Maple syrupUSDT vault. The conservative inflow rate limit (50M max, 10M/day slope) with unlimited outflow is a standard pattern for new SLL onboardings — allowing rapid withdrawal while throttling inbound exposure. This diversifies Spark's USDT yield sources beyond SparkLend. SKY was ~$0.059–0.063, USDS supply ~$8–9B.

Forum discussion: [https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309](https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309)

---

## PR #84 — Spark proposal - Remove supply and borrow caps for non-collateral stablecoins

**Merged:** 2025-10-24 | **Type:** Spark proposal (risk parameter update) | **+4/-4 lines**

### Material Changes

- **USDT supply cap:** 30,000,000 USDT (fixed) → **Set by cap automator** (automated)
- **USDC cap automator — supply cap max:** 1 billion USDC → **0 (no cap)**
- **USDC cap automator — borrow cap max:** 950 million USDC → **0 (no cap)**
- **USDT cap automator — supply cap max:** 5 billion USDT → **0 (no cap)**
- **USDT cap automator — borrow cap max:** 5 billion USDT → **0 (no cap)**
- **pyUSD cap automator — supply cap max:** 500 million pyUSD → **0 (no cap)**
- **pyUSD cap automator — borrow cap max:** 475 million pyUSD → **0 (no cap)**

### Context

Removes all supply and borrow cap limits for the three non-collateral stablecoins on SparkLend (USDT, USDC, pyUSD), effectively making them uncapped. Since these assets have 0% LTV (cannot be used as collateral), the risk from removing caps is limited — they can only be supplied for borrowers to borrow against other collateral. This simplifies operations and removes a growth bottleneck. SKY was ~$0.059–0.063, USDS supply ~$8–9B.

Forum discussion: [https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309](https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309)

---

## PR #83 — Changes to SLL (assorted fixes)

**Merged:** 2025-10-16 | **Type:** Housekeeping | **+2/-3 lines**

### Housekeeping

- Avalanche ALM Relayer Multisig address description changed from referencing `<dfn>TBD</dfn>` placeholders to plain text: "will be specified in a future iteration of the artifact"
- Removed stray whitespace before the Superstate instance section

### Context

Minor cleanup PR accompanying the larger SLL restructuring in PR #72. No parameter or operational changes.

---

## PR #72 — Changes to the Spark Liquidity Layer

**Merged:** 2025-10-16 | **Type:** Spark proposal (SLL restructuring) | **+280/-199 lines**

### Material Changes

- **Superstate USTB instance — replaced by Curve USDC/USDT Pool:** the former Superstate slot was repurposed as a Curve USDC/USDT swap pool (token: crv2pool, address `0x4f493B7dE8aAC7d55F71853688b1F7C8F0243C85`). Inflow/outflow set to "N/A - swap only"; Swap Rate Limits added: maxAmount 5M, slope 20M/day, max slippage 0.15%
- **Curve sUSDS/USDT Pool — replaced by Curve pyUSD/USDC Pool:** token changed sUSDSUSDT → PYUSDUSDC, token address `0x383E6b4437b59fff47B619CBA855CA29342A8559`. Inflow/outflow rate limits zeroed (maxAmount: 0). Swap rate limits: maxAmount 5M (was 25M), slope 100M/day, max slippage 0.1% (was 0.15%)
- **Curve USDC/USDT Pool — replaced by Curve pyUSD/USDS Pool:** asset changed to "USDS and PYUSD", token PYUSDUSDS, address `0xA632D59b9B804a956BfaA9b48Af3A1b74808FC1f`. Inflow: 5M/50M per day (was N/A). Outflow: 5M/100M per day (was N/A). Swap: slope 50M/day (was 20M), slippage 0.2% (was 0.15%)
- **Curve pyUSD/USDC Pool — replaced by Morpho Dai instance:** new Morpho protocol integration for DAI (token: spDAI, `0x73e65DBD630f90604062f6E02fAb9138e713edD9`). Inflow: 200M DAI / 100M DAI per day. Outflow: TBD
- **New: Morpho USDS instance** (`A.6.1.1.1.2.6.1.3.1.8.2`): token sparkUSDS (`0xe41a0583334f0dc4E023Acd0bFef3667F6FE0597`), underlying `0xdC035D45d973E3EC169d2276DDab16f1e407384F`. Inflow: 200M USDS / 100M USDS per day. Outflow: TBD. RRC status: Pending
- **New: Morpho USDC instance** (`A.6.1.1.1.2.6.1.3.1.8.3`): token sparkUSDCbc (`0x56A76b428244a50513ec81e225a293d128fd581D`), underlying USDC (`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`). Inflow: 50M USDC / 25M per day. Outflow: TBD
- **New: Base chain** added to SLL with Morpho Blue USDC ERC4626 Vault (token: sparkUSDC, `0x7BfA7C4f149E7415b73bdeDfe609237e29CBF34A`, RRC: Covered, inflow 100M/50M per day, outflow unlimited), Fluid sUSDS ERC4626 Vault (token: fsUSDS, `0xf62e339f21d8018940f188F6987Bcdf02A849619`, inflow 10M/5M per day, outflow 10M/5M per day), and Aave USDC (token: aBasUSDC, RRC: Pending, inflow 50M/25M per day, outflow unlimited)
- **New: Arbitrum chain** added to SLL with Fluid sUSDS ERC4626 Vault (address `0x3459fcc94390C3372c0F7B4cD3F8795F0E5aFE96`) and Aave USDC instances

### Context

PR #72 is the largest single restructuring of the Spark Liquidity Layer allocation system, simultaneously deprecating unused RWA-oriented instances (Superstate, Centrifuge-lineage slots) and replacing them with DeFi-native Curve and Morpho integrations while also expanding the SLL to two new L2 chains (Base and Arbitrum). The Morpho Dai and USDS vaults with 200M inflow limits represent major new lending capacity. Combined with PR #71's earlier restructuring in the same period, this marks a strategic pivot from tokenized RWA protocols toward battle-tested DeFi venues and multi-chain deployment. SKY ~$0.059-0.063, USDS supply ~$8-9B.

Forum discussion: [https://forum.sky.money/t/october-16-2025-proposed-changes-to-spark-for-upcoming-spell/27215](https://forum.sky.money/t/october-16-2025-proposed-changes-to-spark-for-upcoming-spell/27215)

---

## PR #64 — Oct 2 spell changes

**Merged:** 2025-10-14 | **Type:** Spell recording (2025-10-02)

### Material Changes

- **SparkLend USDT Reserve Factor:** 10% → **1%**
- **SparkLend USDC Reserve Factor:** 10% → **1%**
- **SparkLend LBTC cap automator supply cap:** gap 250 → **500** LBTC; max 2,500 → **10,000** LBTC
- **SparkLend ETH Instance Configuration Document added** (new): wETH on Ethereum Mainnet, spwETH token, inflow 50K ETH / 10K ETH per day, outflow unlimited, RRC: Covered

### Context

Reserve Factor reductions from 10% to 1% for USDT and USDC substantially increase supplier yields. LBTC cap expansion (4x) opens room for more wrapped BTC. ETH instance formalizes wETH as an SLL asset.

---

## PR #69 — Spark - Proposal 1 - Set Target Risk Tolerance Ratio

**Merged:** 2025-10-10 | **Type:** Spark proposal (new framework) | **+72/-0 lines**

### Material Changes

- **New framework: SubDAO Proxy Management** (`A.6.1.1.1.3.6`): establishes Spark's strategy and governance process for managing assets held in the Spark SubDAO Proxy
- **Policy change process:** changes to SubDAO Proxy management policies use the Root Edit Primitive; preapproved activities (periodic payments, disposal of non-core assets) continue until superseded
- **Risk Tolerance Ratio policy** (`A.6.1.1.1.3.6.2.1`): defines RTR as the ratio of Required Risk Capital (RRC) to Total Risk Capital (TRC) per the Stability Scope (`A.3.3`). Spark must take immediate action when RTR exceeds the target — either risk capital actions (increase TRC) or allocation system actions (reduce RRC)
- **Target Risk Tolerance Ratio set to 90%** — parameter maintained in parallel with the Allocation System Primitive section; changes to one require corresponding update to the other

### Context

This proposal establishes Spark's first formal capital adequacy framework, creating both the governance infrastructure for SubDAO Proxy management and the concrete 90% RTR target. The 90% threshold means Spark's required risk capital can consume at most 90% of its total risk capital, leaving a 10% buffer. This complements the SLL restructuring happening concurrently (PRs #70-72) by creating a risk management overlay for Spark's rapidly expanding allocation system. SKY ~$0.059-0.063, USDS supply ~$8-9B.

Forum discussion: [https://forum.sky.money/t/september-29-2025-proposal-1-set-target-risk-tolerance-ratio/27239/](https://forum.sky.money/t/september-29-2025-proposal-1-set-target-risk-tolerance-ratio/27239/)

---

## PR #71 — Spark - SLL - Disable unused products

**Merged:** 2025-10-06 | **Type:** Spark proposal (SLL restructuring) | **+173/-133 lines**

### Material Changes

- **Blackrock BUIDL-I instance — replaced by Superstate USTB:** protocol changed Blackrock → Superstate, asset BUIDL-I → USTB, token address `0x6a9DA2D710BB9B700acde7Cb81F10F1fF8C89041` → `0x43415eB6ff9DB7E26A15b704e7A3eDCe97d31C4e`. Rate Limit IDs changed from BUIDLI_DEPOSIT/BUIDL_REDEEM/BUIDLI_REDEEM to USTB_DEPOSIT/USTB_REDEEM. Outflow maxAmount changed from TBD → Unlimited
- **Centrifuge USDC instance — replaced by Curve sUSDS/USDT Pool:** protocol changed Centrifuge → Curve, asset USDC → USDT, token JTRSY → sUSDSUSDT, token address `0x8c213ee79581Ff4984583C6a801e5263418C4b86` → `0x00836Fe54625BE242BcFA286207795405ca4fD10`, underlying `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48` → `0xdAC17F958D2ee523a2206206994597C13D831ec7` (USDT). Added second Underlying Asset Address for sUSDS (`0xa3931d71877C0E7a3148CB7Eb4463524FEc27fbD`)
- **Curve sUSDS/USDT Pool — rate limits set:** Inflow: maxAmount 5M, slope 20M/day, slippage 0.15%. Outflow: same. New Swap Rate Limits added: maxAmount 25M, slope 100M/day, slippage 0.15%
- **Superstate USTB instance — replaced by Curve USDC/USDT Pool:** protocol → Curve, asset USDC → "N/A - swap only", token USTB → crv2pool, address `0x43415eB6ff9DB7E26A15b704e7A3eDCe97d31C4e` → `0x4f493B7dE8aAC7d55F71853688b1F7C8F0243C85`. Added Underlying Asset Address and Swap Rate Limits (maxAmount 5M, slope 20M/day, slippage 0.15%). Inflow/outflow set to N/A - swap only
- **Curve sUSDS/USDT Pool (second slot) — replaced by Curve pyUSD/USDC Pool:** token sUSDSUSDT → PYUSDUSDC, address `0x00836Fe54625BE242BcFA286207795405ca4fD10` → `0x383E6b4437b59fff47B619CBA855CA29342A8559`. Removed dual underlying addresses. Inflow/outflow: maxAmount 0 (disabled). Swap: maxAmount 5M, slope 100M/day, slippage 0.1%
- **Curve USDC/USDT Pool — replaced by Curve pyUSD/USDS Pool:** asset → "USDS and PYUSD", token crv2pool → PYUSDUSDS, address → `0xA632D59b9B804a956BfaA9b48Af3A1b74808FC1f`. Inflow: 5M/50M per day. Outflow: 5M/100M per day. Swap: 5M/50M per day, slippage 0.2%
- **Curve pyUSD/USDC Pool — replaced by Morpho Dai:** protocol → Morpho, asset → Dai, token → spDAI, address → `0x73e65DBD630f90604062f6E02fAb9138e713edD9`. Inflow: 200M DAI / 100M per day. Outflow/Swap: TBD
- **Curve pyUSD/USDS Pool — replaced by Morpho USDS:** protocol → Morpho, asset → USDS, token → sparkUSDS, address → `0xe41a0583334f0dc4E023Acd0bFef3667F6FE0597`. Inflow: 200M USDS / 100M per day. Outflow: TBD
- **Morpho Dai slot — replaced by Morpho USDC:** asset Dai → USDC, token spDAI → sparkUSDCbc, address → `0x56A76b428244a50513ec81e225a293d128fd581D`. Inflow: 50M USDC / 25M per day
- **Morpho USDS slot — replaced by Base - Morpho Blue USDC ERC4626 Vault:** network Ethereum → Base, protocol → Morpho Blue (ERC4626 Vault), asset → USDC, token → sparkUSDC, address → `0x7BfA7C4f149E7415b73bdeDfe609237e29CBF34A`. RRC: Covered. Inflow: 100M/50M per day. Outflow: Unlimited
- **Morpho USDC slot — replaced by Base - Fluid sUSDS ERC4626 Vault:** protocol → Fluid Finance, asset → sUSDS, token → fsUSDS, address → `0xf62e339f21d8018940f188F6987Bcdf02A849619`. Inflow: 10M/5M per day. Outflow: 10M/5M per day
- **Morpho Blue USDC ERC4626 (Base) — replaced by Base - Aave USDC:** protocol → Aave, token → aBasUSDC. RRC: Pending. Inflow: 50M/25M per day. Outflow: Unlimited
- **Base Fluid sUSDS — replaced by Arbitrum - Fluid sUSDS:** network Base → Arbitrum, address → `0x3459fcc94390C3372c0F7B4cD3F8795F0E5aFE96`
- **Base Aave USDC — replaced by Arbitrum - Aave USDC:** network Base → Arbitrum

### Context

PR #71 is a wholesale restructuring of SLL instance configuration slots, replacing inactive RWA integrations (Blackrock BUIDL-I, Centrifuge) with a mix of Superstate USTB, multiple Curve swap pools, and Morpho lending vaults. The cascading nature of the changes — where each "disabled" slot is repurposed for a new product — reflects the Atlas's approach of reusing document positions rather than adding new ones. Despite the PR title suggesting these are "disabled" products, this is actually a net expansion: the SLL gains Curve AMM integration, three Morpho vaults (Dai, USDS, USDC), and multi-chain instances on Base and Arbitrum. SKY ~$0.059-0.063, USDS supply ~$8-9B.

Forum discussion: [https://forum.sky.money/t/october-16-2025-proposed-changes-to-spark-for-upcoming-spell/27215](https://forum.sky.money/t/october-16-2025-proposed-changes-to-spark-for-upcoming-spell/27215)

---

## PR #70 — Spark - Onboard Avalanche to SLL

**Merged:** 2025-10-06 | **Type:** Spark proposal (chain onboarding) | **+120/-0 lines**

### Material Changes

- **New chain: Avalanche onboarded to the SLL** — adds ALM contract address placeholders and global rate limits for the Avalanche network
- ALM Controller (ForeignController), Freezer Multisig, Proxy, and Rate Limits contracts: all `TBD`
- ALM Relayer Multisig: "will be specified in a future iteration of the artifact"
- **Avalanche USDC PSM limits:** Deposit maxAmount: Unlimited, slope: Unlimited. Withdrawal maxAmount: Unlimited, slope: Unlimited
- **USDC Avalanche ALM Proxy Maximum:** maxAmount 100,000,000 USDC, slope 50,000,000 USDC/day
- **USDC Avalanche CCTP Bridge Maximum:** maxAmount 100,000,000 USDC, slope 50,000,000 USDC/day (via Circle Cross-Chain Transfer Protocol)

### Context

This PR establishes the Avalanche chain as the SLL's first non-Ethereum-mainnet deployment, setting up the ALM infrastructure with placeholder contract addresses and generous 100M USDC bridging limits via both direct proxy and Circle's CCTP. The unlimited PSM deposit/withdrawal limits indicate the intent to allow full USDC liquidity on Avalanche. Paired with PR #68 which added the first Aave v3 USDC instance on the chain. SKY ~$0.059-0.063, USDS supply ~$8-9B.

Forum discussion: [https://forum.sky.money/t/october-16-2025-proposed-changes-to-spark-for-upcoming-spell/27215](https://forum.sky.money/t/october-16-2025-proposed-changes-to-spark-for-upcoming-spell/27215)

---

## PR #68 — Spark - Onboard Aave v3 Avalanche USDC

**Merged:** 2025-10-06 | **Type:** Spark proposal (new instance) | **+162/-0 lines**

### Material Changes

- **New instance: Avalanche - Aave v3 USDC Vault** — first Avalanche-native lending instance in the SLL. Network: Avalanche, Protocol: Aave, Asset: USDC, Token: aAvaxUSDC
- Token Address: `0x625E7708f30cA75bfd92586e17077590C60eb4cD`, Underlying: `0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E`
- Inflow rate limits: maxAmount 20,000,000 USDC, slope 10,000,000 USDC per day
- Outflow rate limits: Unlimited
- Rate Limit IDs: to be specified in a future iteration
- RRC Framework: Covered

### Context

First concrete Avalanche deployment for the SLL, paired with PR #70 which set up the Avalanche chain infrastructure (ALM contracts, PSM/bridging rate limits). The 20M USDC inflow cap is modest compared to Ethereum Mainnet instances, reflecting the cautious approach to a new chain. SKY ~$0.059-0.063, USDS supply ~$8-9B.

Forum discussion: [https://forum.sky.money/t/october-16-2025-proposed-changes-to-spark-for-upcoming-spell/27215](https://forum.sky.money/t/october-16-2025-proposed-changes-to-spark-for-upcoming-spell/27215)

---

## PR #60 — 2025-09-18 executive changes

**Merged:** 2025-09-29 | **Type:** Spell recording (2025-09-18)

### Material Changes

- **LSEV2-SKY-A Mat (liquidation ratio):** 125% → **145%**
- **USDC CCTP rate limits set** (Ethereum and Base ALM Proxy): maxAmount `max` → **200M USDC**; slope `0` → **500M USDC/day** (both directions)
- **Curve pyUSD/USDS Pool Instance added** (new): USDS+PYUSD pool, inflow 5M/50M per day, outflow 5M/100M per day, swap 5M/50M per day with 0.2% max slippage
- **SparkLend USDT cap automator:** supply gap 100M → **1B**, max 500M → **5B**; borrow gap 50M → **200M**, max 450M → **5B**

### Context

USDC CCTP rate limits transition from uncapped to bounded values, establishing formal cross-chain flow controls. USDT cap automator expansion (10x) reflects growing demand on SparkLend.

---

## PR #55 — 2025-09-04 changes
**Merged:** 2025-09-11 | **Type:** Spell recording (2025-09-04)

### Material Changes
- **Aave USDe instance added**: new SLL allocation to Aave Prime USDe on Ethereum Mainnet — token aEthUSDe (`0x4F5923Fc5FD4a93352581b38B7cD26943012DECF`), underlying USDe (`0x4c9EDD5852cd905f086C759E8383e09bff1E68B3`). Inflow: 250M USDe maxAmount, 100M/day slope; Outflow: Unlimited
- **Morpho USDC instance added**: new SLL allocation to Morpho USDC on Ethereum Mainnet — Instance Configuration Document location added
- **Curve sUSDS/USDT Pool renamed**: was "Curve sUSDC/USDT Pool" — corrects incorrect asset name (underlying is sUSDS, not sUSDC)
- **SLL inflow limits increased for two instances**: maxAmount 50M → **100M**, slope 25M → **100M per day** (specific instances in SLL directory)

### Housekeeping
- Addresses checksummed (EIP-55) throughout Spark Agent Scope Database.
- Unit labels (e.g., "USDS") added to SLL instance rate limit parameters for clarity.
- Placeholder pool/rate-limit ID fields updated to "will be specified in a future iteration."

### Context
PR #55 records multiple changes from the 2025-09-04 executive spell: Aave USDe is the headline new instance (250M capacity), representing a significant new yield-generating avenue for SLL capital. Also fixes the sUSDS/USDT pool naming error that had persisted from launch.

---

## PR #53 — Update WETH risk params – spell 2025-08-21
**Merged:** 2025-08-29 | **Type:** Spell recording (2025-08-21)

### Material Changes
- **SparkLend WETH LTV**: 82% → **85%**
- **SparkLend WETH Liquidation Threshold**: 83% → **86%**
- **SparkLend WETH Slope 1 Spread**: -0.50% → **-0.30%** (borrow rate slightly higher)

### Context
Recorded as a follow-on to PR #48 (2025-08-21 Spell Changes). Modest WETH collateral parameter improvements reflecting improved market conditions.

---

## PR #48 — 2025-08-21 Spell Changes
**Merged:** 2025-08-25 | **Type:** Spell recording (2025-08-21)

### Material Changes
- **Spark SLL USDS inflow limits raised** (Spark Artifact): maxAmount 150,000,000 → **200,000,000** USDS; slope 75,000,000 → **400,000,000** USDS/day (large slope increase).
- **SparkLend stablecoin Slope 1 reduced**:
  - Dai borrow rate: SSR + 1% → **SSR + 1.25%**
  - USDS borrow rate: SSR + 1% → **SSR + 1.25%**
  - USDT Slope 1: SSR + 1.5% → **SSR + 1.25%**
  - USDC Slope 1: SSR + 1.5% → **SSR + 1.25%**
- **SparkLend collateral LTVs raised** (multiple assets):
  - wstETH: LTV 79% → **83%**, LT 80% → **84%**
  - weETH: LTV 72% → **79%**, LT 73% → **80%**
  - LBTC: LTV 65% → **74%**, LT 70% → **75%**
  - tBTC: LTV 65% → **74%**, LT 70% → **75%**
  - ezETH: LTV 72% → **75%**, LT 73% → **76%**
  - rsETH: LTV 72% → **75%**, LT 73% → **76%**
  - cbBTC: LTV 74% → **81%**, LT 75% → **82%**
- **wstETH borrow cap automator max reduced**: 1,000,000 → **1 wstETH** (effectively disabling wstETH borrowing)
- **rETH borrow cap automator max reduced**: 2,400 → **1 rETH** (effectively disabling rETH borrowing)
- **Grove contract address updated**: ALM Controller on Mainnet updated to new address.

### Context
The LTV increases across multiple LSTs and wrapped BTC assets reflect improved collateral risk assessments. Setting wstETH/rETH borrow caps to 1 unit effectively disables borrowing of these assets without removing them from the protocol. The large USDS SLL slope increase (75M → 400M/day) greatly accelerates the protocol's ability to deploy capital via the Liquidity Layer.

---

## PR #49 — add Spark bootstrapping delegates
**Merged:** 2025-08-22 | **Type:** Spark proposal (delegate roster)

### Material Changes
- **Two bootstrapping delegates added** to Spark's delegate Active Data:
  - **Remi** — wallet `0xDC5D4228a42880F5bbd577A184035503Bd55799a`, effective 2025-08-21, Status: Active, no conflicts
  - **NeoNode** — wallet `0x71faa03C0cEbCbB53236763B6b118aD906d9F6d3`, effective 2025-08-21, Status: Active, no conflicts

### Context
Bootstrapping delegate phase per forum thread at https://forum.sky.money/t/spark-delegates-bootstrapping-phase/27090. Spark's delegate system requires on-chain delegates to oversee protocol decisions; these two add initial coverage.

---

## PR #34 — 2025-08-07 Executive Changes
**Merged:** 2025-08-12 | **Type:** Spell recording (2025-08-07)

### Material Changes
- **Morpho sUSDe/USDe DDM Vault exposure reduced to zero** (A.3.5 Active Data): target exposure 275,000,000 USDS → **0 USDS**.
- **SparkLend pyUSD onboarded** (Spark Artifact, new): pyUSD added as SparkLend collateral and borrowable asset.
  - Risk params: LTV 0%, LT 0%, E-mode: USD, Reserve Factor 10%, Slope 1: SSR + 1.5%.
  - Cap automator: supply gap 50M / max 500M pyUSD; borrow gap 25M / max 475M pyUSD.
  - SLL Instance: pyUSD supplied to SparkLend, token sppyUSD; inflow maxAmount 50M, slope 25M/day; outflow unlimited.
- **Spark SLL instance reorganization**: Morpho Dai instance replaced the previous "Morpho (Ethereum Mainnet)" slot; inflow raised to maxAmount 200M / slope 100M/day (was 100M/50M). Base network Fluid sUSDS ERC4626 vault and Morpho Blue USDC ERC4626 vault properly placed.
- **Curve pyUSD/USDC Pool instance** (formerly Curve sUSDS/USDT slot): inflow/outflow set to 0; swap rate limits 5M maxAmount / 25M per day / 0.05% max slippage.
- **SparkLend Dai Slope 1**: SSR + 0.75% → **SSR + 1%**. USDS Slope 1: SSR + 0.75% → **SSR + 1%**. USDT Slope 1: SSR + 1% → **SSR + 1.5%**. USDC Slope 1: SSR + 1% → **SSR + 1.5%**. USDS Flash Loan Enabled: No → **Yes**.
- **Spark SLL inflow limits set** (Spark Artifact, previously TBD): maxAmount 100M, slope 50M/day.

### Context
PR #34 records the August 7, 2025 Executive Spell. Key events: Morpho DDM vault fully derisked to zero (from 275M); pyUSD onboarded across SparkLend and SLL in one coordinated action; stablecoin borrow rates adjusted upward. PRs #42 and #44 correct follow-up issues from this same spell.

---

## PR #32 — Atlas update from 2025-07-24 Exec
**Merged:** 2025-07-29 | **Type:** Spell recording (2025-07-24)

### Material Changes
- **Spark SLL inflow limits set** (Spark Artifact, previously TBD): maxAmount **100,000,000** USDS; slope **50,000,000** USDS/day.
- **WBTC Liquidation Threshold reduced** (SparkLend WBTC risk parameters): LT 40% → **35%** (LTV unchanged at 0%).

---

## PR #18 — Weekly Cycle Atlas Edit 2025-06-23
**Merged:** 2025-06-27 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Spark Foundation address recorded** (A.6.1.1.1): `0x92e4629a4510AF5819d7D1601464C233599fF5ec` (Ethereum Mainnet).
- **Base Allocation System additions**: Fluid sUSDS ERC4626 Vault and Aave USDC Instance Configuration Document Locations added to Base Active Instances Directory.
- **"Base Mainnet" → "Base"** terminology normalized throughout SLL directory documents; internal cross-reference names updated to match.

### Housekeeping
- Root Edit Submission Exception for Spark Foundation deleted — merged into standard Nested Contributors exception.
- Token emissions language: "Junior Risk Capital requirements" → "Risk Capital requirements."

---

## PR #17 — Cleanup multiple scopes and artifacts
**Merged:** 2025-06-20 | **Type:** Housekeeping

Multi-scope cleanup pass. SparkLend parameter corrections in Spark Artifact:
- **USDS Liquidation Bonus**: 10% → **0%** (correction)
- **cbBTC E-mode Category**: N/A → **BTC** (correction)
- **sUSDS E-mode Category**: N/A → **USD** (correction)

All other changes are formatting only (whitespace, `<code>` tags on parameter names).

---

## PR #15 — 2025-06-16 weekly atlas edit proposal
**Merged:** 2025-06-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **SPK token transfer restructured** (A.6.1.1.1): "Transfer Of Tokens To Spark Foundation" language clarified — SPK Company Ltd transfers all tokens not reserved for the token launch to the Spark Foundation; "Transfer Of Tokens For Token Launch" document added as the reservation mechanism.
- **Spark Foundation Root Edit exception removed**: "Root Edit Proposal Submission Requirements Exception For Spark Foundation" deleted (Spark Foundation was given an exception to the token-holding requirement; now removed — only Nested Contributors retain this exception).

---

## PR #16 — update capitalization of daocraft
**Merged:** 2025-06-17 | **Type:** Housekeeping

"DAOCraft" → "DAOcraft" (lowercase 'c') in all Spark Artifact documents referencing the DAOcraft Executor Accord Primitive Instance. Affects document titles, body text, and `<dfn>` tags across ~8 documents.

---

## PR #9 — Add 2025-06-12 spell changes
**Merged:** 2025-06-16 | **Type:** Spell recording (2025-06-12)

### Material Changes
- **SLL inflow rate limits raised** (two Spark Mainnet SLL instances):
  - Instance 1: maxAmount 25M → 100M USDS; slope 5M → 20M per day
  - Instance 2: maxAmount TBD → 200M; slope TBD → 100M per day
- **SparkLend reserve factors raised**: DAI 0% → 10%; USDS 0% → 10%; USDT 5% → 10%; USDC 5% → 10%
- **ezETH cap automator**: supply gap 2,000 → 5,000 ezETH; max 20,000 → 40,000 ezETH

---

## PR #10 — Weekly Cycle Atlas Edit proposal 2025-06-09
**Merged:** 2025-06-12 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Spark Foundation documented** (new): Mission statement added — "support the development, growth, and adoption of Spark."
- **Phoenix Labs documented** (new): Defined as a Nested Contributor — core contributor to both Spark and Sky; provides development services to the Spark Foundation.
- **SPK token distribution records updated**: "Will transfer 6.5B SPK" changed to record of completed transfer (6.5B to Sky Pause Proxy); new "Transfer Of Tokens To Spark SubProxy Account" doc (918,760,451 SPK to Spark SubProxy); Spark Foundation allocation changed from 3.5B → 1B SPK (to be transferred); 1,581,239,549 SPK to be retained by SPK Company Ltd.
- **SPK staking added** (new): SPK token holders can stake; rewards to be specified in a future iteration.
- **SPK Genesis Supply address recorded**: `0x6FE588FDCC6A34207485cc6e47673F59cCEDF92B`
- **Root Edit governance updated**:
  - "1% of circulating supply" threshold changed to "1% of total supply"
  - Circulating Supply Definition added (excludes SKY-held distribution pool, vesting, SubProxy)
  - Root Edit Proposal Submission Requirements Exception split into two: one for Nested Contributors (Phoenix Labs), one for Spark Foundation
  - Time-Limited Root Edit Restrictions renamed to "On Removal Of Nested Contributors"; scope changed — now requires SKY holder approval (not just SPK) to remove a Nested Contributor; period fixed at 3 years from June 4, 2025
  - Multiple "Short Term Transitionary Measures" docs added (GitHub-based editing, Powerhouse-based updates, SLL/SparkLend/Savings parameter control transition)

### Context
This PR formally documents what had already happened with SPK token distributions while also materially restructuring Spark's internal governance rules. The Spark Foundation/Phoenix Labs formalization and the Root Edit threshold change from circulating to total supply are notable — total supply includes locked tokens, effectively raising the governance bar.

---

## PR #4 — add 2025-05-29 spell changes
**Merged:** 2025-06-04 | **Type:** Spell recording (2025-05-29)

### Material Changes
- **Unichain SLL added** (new): ALM Contract Addresses for Spark Liquidity Layer on Unichain — ALM_CONTROLLER `0x9B1BEB11CFE05117029a30eb799B6586125321FF`, ALM_PROXY `0x345E368fcCd62266B3f5F37C9a131FD1c39f5869`, plus PSM rate limits (USDC: 50M in/out; USDS/sUSDS: unlimited).
- **Optimism SLL added** (new): ALM Contract Addresses for Spark Liquidity Layer on Optimism — ALM_CONTROLLER `0x1d54A093b8FDdFcc6fBB411d9Af31D96e034B3D5`, ALM_PROXY `0x876664f0c9Ff24D1aa355Ce9f1680AE1A5bf36fB`, plus PSM rate limits (USDC: 50M in/out; USDS/sUSDS: unlimited).
- **SLL Mainnet USDS mint limit raised**: maxAmount 50M → 500M; slope 50M → 500M per day; USDS-to-USDC swap: maxAmount 50M → 500M; slope 50M → 300M per day
- **WBTC Liquidation Threshold**: 45% → 40%
- **Ethena (USDe/sUSDe) Mainnet rate limits specified** (previously TBD): USDe inflow 250M/100M per day, outflow 500M/200M per day; sUSDe inflow 250M/100M per day, outflow unlimited
- **DAI risk parameters**: Base Rate `SSR value` → `0%`; Slope 1 `0.75%` → `SSR + 0.75%`
- **USDS risk parameters**: Base Rate `SSR value` → `0%`; Slope 1 `0.75%` → `SSR + 0.75%`

---
