# Spark (SLL) — Change History

Atlas path: `A.6.1.1.1` (2116 docs)

---

## PR #219 — Atlas Edit Proposal — 2026-04-06
**Merged:** 2026-04-09 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- "SLL" abbreviation expanded to "Spark Liquidity Layer" throughout Spark's Allocation System Primitive section (A.6.1.1.1.2.6.1): affects document titles (e.g., "Asset Supplied By SLL" → "Asset Supplied By Spark Liquidity Layer" across ~20 documents), section headers, and introductory text. Same UUIDs; no content changes.

### Context
Pure cosmetic rename following the SLL/GLL abbreviation expansion policy introduced in this weekly edit. No operational impact.

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

Forum discussion: https://forum.sky.money/t/october-16-2025-proposed-changes-to-spark-for-upcoming-spell/27215

---

## PR #83 — Changes to SLL (assorted fixes)
**Merged:** 2025-10-16 | **Type:** Housekeeping | **+2/-3 lines**

### Housekeeping
- Avalanche ALM Relayer Multisig address description changed from referencing `<dfn>TBD</dfn>` placeholders to plain text: "will be specified in a future iteration of the artifact"
- Removed stray whitespace before the Superstate instance section

### Context
Minor cleanup PR accompanying the larger SLL restructuring in PR #72. No parameter or operational changes.

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

Forum discussion: https://forum.sky.money/t/september-29-2025-proposal-1-set-target-risk-tolerance-ratio/27239/

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

Forum discussion: https://forum.sky.money/t/october-16-2025-proposed-changes-to-spark-for-upcoming-spell/27215

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

Forum discussion: https://forum.sky.money/t/october-16-2025-proposed-changes-to-spark-for-upcoming-spell/27215

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

Forum discussion: https://forum.sky.money/t/october-16-2025-proposed-changes-to-spark-for-upcoming-spell/27215

---

## PR #108 — Minor fixes
**Merged:** 2025-11-19 | **Type:** Housekeeping

### Housekeeping
- Fixed copy-pasted Target Liquidity descriptions: "Spark Savings USDC on Ethereum" → correct token name for USDT, ETH, and Avalanche USDC instances
- Added accidentally skipped "Rewards Rate Current Configuration" parent document for Spark Savings

### Context
Corrective housekeeping — the Target Liquidity text for three Spark Savings instances was erroneously copy-pasted from the USDC template. No parameter values changed.

---

## PR #64 — Oct 2 spell changes
**Merged:** 2025-10-14 | **Type:** Spell changes

### Material Changes
- **SparkLend USDT Reserve Factor:** 10% → **1%**
- **SparkLend USDC Reserve Factor:** 10% → **1%**
- **SparkLend LBTC cap automator supply cap:** gap 250 → **500** LBTC; max 2,500 → **10,000** LBTC
- **SparkLend ETH Instance Configuration Document added** (new): wETH on Ethereum Mainnet, spwETH token, inflow 50K ETH / 10K ETH per day, outflow unlimited, RRC: Covered

### Context
Reserve Factor reductions from 10% to 1% for USDT and USDC substantially increase supplier yields. LBTC cap expansion (4x) opens room for more wrapped BTC. ETH instance formalizes wETH as an SLL asset.

---

## PR #60 — 2025-09-18 executive changes
**Merged:** 2025-09-29 | **Type:** Spell changes

### Material Changes
- **LSEV2-SKY-A Mat (liquidation ratio):** 125% → **145%**
- **USDC CCTP rate limits set** (Ethereum and Base ALM Proxy): maxAmount `max` → **200M USDC**; slope `0` → **500M USDC/day** (both directions)
- **Curve pyUSD/USDS Pool Instance added** (new): USDS+PYUSD pool, inflow 5M/50M per day, outflow 5M/100M per day, swap 5M/50M per day with 0.2% max slippage
- **SparkLend USDT cap automator:** supply gap 100M → **1B**, max 500M → **5B**; borrow gap 50M → **200M**, max 450M → **5B**

### Context
USDC CCTP rate limits transition from uncapped to bounded values, establishing formal cross-chain flow controls. USDT cap automator expansion (10x) reflects growing demand on SparkLend.

---

## PR #131 — Spark proposal - Launch Spark Savings spPYUSD
**Merged:** 2025-12-11 | **+116/-0 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.2.5` - Off-chain Operational Parameters [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4` - Ethereum Mainnet - Spark Savings v2 spPYUSD Instance Configuration Document [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.3` - Instance-specific Operational Processes [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.4.1.3` - Setter [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.2.3` - Rate Limit IDs [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.4.1.4` - Taker [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.2.2.1` - Token Address [Core]
- **Added** `A.6.1.1.1.2.6.1.1.2.1.11.4` - Ethereum Mainnet - Spark Savings v2 PYUSD Instance Configuration Document Location [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.4.1.1` - Spark Vault v2 Implementation [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.2.1.2` - Target Protocol [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.2.1.3` - Asset Supplied By Users [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.4.2.1` - Spark Savings spPYUSD Risk Parameters [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.4.2` - Risk Parameters Current Configuration [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.2.1.1` - Network [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.4.2.3` - Take Rate Limits [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.4.2.2` - Rate Limits [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.2.4` - Rate Limits [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.2` - Parameters [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.1` - RRC Framework Full Implementation [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.2.1.4` - Token [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.4.1` - Contract Addresses [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.2.1` - Instance Identifiers [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.2.2.2` - Underlying Asset Address [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.2.2` - Contract Addresses [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.4.1.2` - Default admin [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.4` - Instance-specific Operational Parameters [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.9.4.4.2.4` - TransferAssets Rate Limits [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #132 — Spark proposal - Update allocator roles to ALM Proxy Freezable
**Merged:** 2025-12-11 | **+12/-0 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.6.1.1.1.2.6.1.3.2.1.1.2.2.3` - Allocator Role Address [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.3.2.2.3` - Allocator Role Address [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.2.2.2.3` - Allocator Role Address [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #134 — Spark proposal - Onboard Spark Prime / Arkis
**Merged:** 2025-12-15 | **+95/-0 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.1.2` - Target Protocol [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.3` - Instance-specific Operational Processes [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.5` - Off-chain Operational Parameters [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.2` - Contract Addresses [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.1` - Instance Identifiers [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1` - Ethereum Mainnet - Arkis Instance Configuration Document [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.1` - RRC Framework Full Implementation [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.1.3` - Asset Supplied By Spark Liquidity Layer [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.3` - Rate Limit IDs [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10` - Arkis [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.4.2` - Outflow Rate Limits [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.2.3` - Pool Address [Core]
- **Added** `A.6.1.1.1.2.6.1.1.2.1.12.1` - Ethereum Mainnet - Arkis Instance Configuration Document Location [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.5.1` - Maximum Exposure [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.2.1` - Token Address [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.5.2` - Instance Capital Requirement Ratio [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.1.1` - Network [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.4.1` - Inflow Rate Limits [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.1.4` - Token [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2` - Parameters [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.2.2` - Underlying Asset Address [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.10.1.2.4` - Rate Limits [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #137 — Filling in Spark Savings v2 Instance Configuration Document Locations and fixing titles
**Merged:** 2025-12-04 | **+6/-6 lines**

### Raw Changes (rewrite with /atlas-track)
- **Modified** `A.6.1.1.1.2.6.1.1.2.1.11.3` - Ethereum Mainnet - Spark Savings v2 USDT Instance Configuration Document Location [Core]
- **Modified** `A.6.1.1.1.2.6.1.1.2.1.11.1` - Ethereum Mainnet - Spark Savings v2 ETH Instance Configuration Document Location [Core]
- **Modified** `A.6.1.1.1.2.6.1.1.2.1.11.2` - Ethereum Mainnet - Spark Savings v2 USDC Instance Configuration Document Location [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #138 — SAEP-07
**Merged:** 2025-12-11 | **+301/-0 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.6.1.1.1.3.7.2.3.1` - Approved Venues Parameters Definitions [Core]
- **Added** `A.6.1.1.1.3.7.2.3.2` - Approved Venues Current Configuration [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2` - Marginable Assets Current Configuration [Core]
- **Added** `A.6.1.1.1.3.7.2.2.1.1` - Collateral Haircut [Core]
- **Added** `A.6.1.1.1.3.7.2.1` - Counterparty Requirements [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.13` - Tether (USDT) [Core]
- **Added** `A.6.1.1.1.3.7.2.4.2.2` - Borrow Rate [Core]
- **Added** `A.6.1.1.1.3.7.2.7.2` - Address Whitelist [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.9` - Avalanche (AVAX) [Core]
- **Added** `A.6.1.1.1.3.7.2.3.2.3` - OKX [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.8` - Zcash (ZEC) [Core]
- **Added** `A.6.1.1.1.3.7.1.2` - Spark Prime Brokerage Policy Change Execution [Core]
- **Added** `A.6.1.1.1.3.7.2.6` - Delegation of Rights and Responsibilities [Core]
- **Added** `A.6.1.1.1.3.7.2.7.3` - Quorum and Signers [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.3` - Ripple (XRP) [Core]
- **Added** `A.6.1.1.1.3.7.2.5.5` - Emergency Parameter Updates [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.4` - Solana (SOL) [Core]
- **Added** `A.6.1.1.1.3.7.2.5.4` - Parameter Updates in Non Emergency Situations [Core]
- **Added** `A.6.1.1.1.3.7.2.2.5` - Unapproved Assets and Products [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.5` - Dogecoin (DOGE) [Core]
- **Added** `A.6.1.1.1.3.7.2.4.1.1` - Duration [Core]
- **Added** `A.6.1.1.1.3.7.2.3.2.1` - Onchain [Core]
- **Added** `A.6.1.1.1.3.7.2.4.2` - Loan Terms Current Configuration [Core]
- **Added** `A.6.1.1.1.3.7.2.3.1.1` - Exposure Limit [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.1` - Bitcoin (BTC) [Core]
- **Added** `A.6.1.1.1.3.7.2.2.1.2` - Exposure Limit [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.6` - Cardano (ADA) [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.7` - Hyperliquid (HYPE) [Core]
- **Added** `A.6.1.1.1.3.7.2.3.2.5` - Bitget [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.14` - Circle (USDC) [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.12` - Ethena (USDe) [Core]
- **Added** `A.6.1.1.1.3.7.2.7.1` - Critical Actions [Core]
- **Added** `A.6.1.1.1.3.7.2.5.1` - Borrower Insolvency [Core]
- **Added** `A.6.1.1.1.3.7.2.2.4` - Perpetual and Calendar Futures [Core]
- **Added** `A.6.1.1.1.3.7.2.3.2.8` - Bitgo [Core]
- **Added** `A.6.1.1.1.3.7` - Spark Prime Brokerage [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.11` - Near (NEAR) [Core]
- **Added** `A.6.1.1.1.3.7.2.5.2` - Unapproved Products [Core]
- **Added** `A.6.1.1.1.3.7.2.5.3` - Borrow Rate Shortfall [Core]
- **Added** `A.6.1.1.1.3.7.2.2.1` - Marginable Assets Parameters Definitions [Core]
- **Added** `A.6.1.1.1.3.7.1.1` - Spark Prime Brokerage Policy Changes [Core]
- **Added** `A.6.1.1.1.3.7.2.4.1.2` - Borrow Rate [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.10` - Sui (SUI) [Core]
- **Added** `A.6.1.1.1.3.7.2.4` - Loan Terms [Core]
- **Added** `A.6.1.1.1.3.7.2.2.2.2` - Ether (ETH) [Core]
- **Added** `A.6.1.1.1.3.7.2.3` - Approved Venues [Core]
- **Added** `A.6.1.1.1.3.7.2.4.1` - Loan Term Definitions [Core]
- **Added** `A.6.1.1.1.3.7.1` - Operational Process Definition [Core]
- **Added** `A.6.1.1.1.3.7.2.3.2.4` - Bybit [Core]
- **Added** `A.6.1.1.1.3.7.2.3.2.6` - Hyperliquid (Hypercore) [Core]
- **Added** `A.6.1.1.1.3.7.2.7.4` - Transfers [Core]
- **Added** `A.6.1.1.1.3.7.2` - Policies and Mandate [Core]
- **Added** `A.6.1.1.1.3.7.2.5` - Recall and Acceleration [Core]
- **Added** `A.6.1.1.1.3.7.2.2.1.3` - Staked and Wrapped Versions [Core]
- **Added** `A.6.1.1.1.3.7.2.7` - Account Management [Core]
- **Added** `A.6.1.1.1.3.7.2.2.3` - Pendle PTs [Core]
- **Added** `A.6.1.1.1.3.7.2.3.2.2` - Binance [Core]
- **Added** `A.6.1.1.1.3.7.2.2` - Marginable Assets [Core]
- **Added** `A.6.1.1.1.3.7.2.3.2.7` - Anchorage [Core]
- **Added** `A.6.1.1.1.3.7.2.4.2.1` - Duration [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #140 — SAEP-08
**Merged:** 2025-12-11 | **+225/-0 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.6.1.1.1.3.8.2.4.1.3` - Margin Call Cure Period [Core]
- **Added** `A.6.1.1.1.3.8.2.4.1.2` - Borrow Rate [Core]
- **Added** `A.6.1.1.1.3.8.2.2` - Marginable Assets [Core]
- **Added** `A.6.1.1.1.3.8.2.5` - Recall and Acceleration [Core]
- **Added** `A.6.1.1.1.3.8.2.3.1` - Approved Venues Parameters Definitions [Core]
- **Added** `A.6.1.1.1.3.8.2.7.4` - Transfers [Core]
- **Added** `A.6.1.1.1.3.8.2.2.2` - Marginable Assets Current Configuration [Core]
- **Added** `A.6.1.1.1.3.8.2.6` - Delegation of Rights and Responsibilities [Core]
- **Added** `A.6.1.1.1.3.8.2.1` - Counterparty Requirements [Core]
- **Added** `A.6.1.1.1.3.8.2.2.1.1` - Initial LTV [Core]
- **Added** `A.6.1.1.1.3.8.2.2.1.3` - Liquidation LTV [Core]
- **Added** `A.6.1.1.1.3.8.2.2.1.5` - Staked and Wrapped Versions [Core]
- **Added** `A.6.1.1.1.3.8.2.4.2.2` - Borrow Rate [Core]
- **Added** `A.6.1.1.1.3.8.2.5.5` - Emergency Parameter Updates [Core]
- **Added** `A.6.1.1.1.3.8.2.3.1.2` - Collateral Agent [Core]
- **Added** `A.6.1.1.1.3.8` - Offchain Collateralized Lending [Core]
- **Added** `A.6.1.1.1.3.8.2.5.3` - Borrow Rate Shortfall [Core]
- **Added** `A.6.1.1.1.3.8.2.2.1.2` - Maintenance LTV [Core]
- **Added** `A.6.1.1.1.3.8.1` - Operational Process Definition [Core]
- **Added** `A.6.1.1.1.3.8.2.3.2` - Approved Venues Current Configuration [Core]
- **Added** `A.6.1.1.1.3.8.2.5.1` - Borrower Insolvency [Core]
- **Added** `A.6.1.1.1.3.8.2.7.2` - Address Whitelist [Core]
- **Added** `A.6.1.1.1.3.8.2.7.3` - Quorum and Signers [Core]
- **Added** `A.6.1.1.1.3.8.2.2.2.1` - Bitcoin (BTC) [Core]
- **Added** `A.6.1.1.1.3.8.2.5.4` - Parameter Updates in Non Emergency Situations [Core]
- **Added** `A.6.1.1.1.3.8.2.5.2` - Cross Default [Core]
- **Added** `A.6.1.1.1.3.8.2.2.1` - Marginable Assets Parameters Definitions [Core]
- **Added** `A.6.1.1.1.3.8.2.4.2.3` - Margin Call Cure Period [Core]
- **Added** `A.6.1.1.1.3.8.2.3` - Approved Venues [Core]
- **Added** `A.6.1.1.1.3.8.2.4.1` - Loan Terms Definitions [Core]
- **Added** `A.6.1.1.1.3.8.2` - Policies and Mandate [Core]
- **Added** `A.6.1.1.1.3.8.2.7.1` - Critical Actions [Core]
- **Added** `A.6.1.1.1.3.8.2.2.2.4` - Solana (SOL) [Core]
- **Added** `A.6.1.1.1.3.8.2.4.2.1` - Duration [Core]
- **Added** `A.6.1.1.1.3.8.1.2` - Offchain Collateralized Lending Policy Change Execution [Core]
- **Added** `A.6.1.1.1.3.8.1.1` - Offchain Collateralized Lending Policy Changes [Core]
- **Added** `A.6.1.1.1.3.8.2.7` - Account Management [Core]
- **Added** `A.6.1.1.1.3.8.2.4.1.1` - Duration [Core]
- **Added** `A.6.1.1.1.3.8.2.4.2` - Loan Terms Current Configuration [Core]
- **Added** `A.6.1.1.1.3.8.2.2.2.5` - Hyperliquid (HYPE) [Core]
- **Added** `A.6.1.1.1.3.8.2.2.1.4` - Exposure Limit [Core]
- **Added** `A.6.1.1.1.3.8.2.3.1.1` - Exposure Limit [Core]
- **Added** `A.6.1.1.1.3.8.2.2.2.2` - Ether (ETH) [Core]
- **Added** `A.6.1.1.1.3.8.2.4` - Loan Terms [Core]
- **Added** `A.6.1.1.1.3.8.2.3.2.1` - Anchorage [Core]
- **Added** `A.6.1.1.1.3.8.2.2.2.3` - Ripple (XRP) [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #183 — Spark Proposal - SLL - Adjust Rate Limits for SparkLend USDT, Aave Core USDT, and Maple syrupUSDT
**Merged:** 2026-03-20 | **+16/-6 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.6.1.1.1.2.6.1.3.1.3.2.4.1` - Request Redemption Parameters [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.3.2.4` - Instance-specific Operational Parameters [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #184 — Spark Proposal - SLL - Onboard Morpho v2 USDT Vault
**Merged:** 2026-03-20 | **+100/-0 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.1` - RRC Framework Full Implementation [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.4` - Instance-specific Operational Parameters [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.1` - Instance Identifiers [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.4.1` - Inflow Rate Limits [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.2` - Contract Addresses [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.2.3` - Allocator Role Address [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.3` - Instance-specific Operational Processes [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.5` - Off-chain Operational Parameters [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2` - Parameters [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.1.4` - Token [Core]
- **Added** `A.6.1.1.1.2.6.1.1.2.1.10.4` - Ethereum Mainnet - Morpho USDT Instance Configuration Document Location [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.4.2` - Timelock [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.4.2` - Outflow Rate Limits [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.4.1.2` - Guardian Role Address [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.4` - Rate Limits [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.1.3` - Asset Supplied By Spark Liquidity Layer [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4` - Ethereum Mainnet - Morpho USDT Instance Configuration Document [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.2.2` - Underlying Asset Address [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.1.2` - Target Protocol [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.3` - Rate Limit IDs [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.1.1` - Network [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.2.2.1` - Token Address [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.4.1` - Contract Addresses [Core]
- **Added** `A.6.1.1.1.2.6.1.3.1.8.4.4.1.1` - Curator Role Address [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #109 — SAEP-04: Strategic Investment in Arkis
**Merged:** 2025-11-19 | **Type:** SAEP (Spark agent proposal) | **+94/-0 lines**

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

Forum discussion: https://forum.sky.money/t/saep-04-strategic-investment-in-arkis/27378

---

## PR #87 — SAEP-02: Modify Spark Liquidity Layer Core Relayer and Freezer Multisig Configuration
**Merged:** 2025-10-24 | **Type:** SAEP (Spark agent proposal) | **+12/-8 lines**

### Material Changes
- **Core Operator Relayer Multisig — control expanded:** was controlled solely by Amatsu → now jointly controlled by Amatsu and Spark Assets Foundation (SAF)
- **Core Operator Relayer Multisig — threshold changed:** 2/3 → **2/5** signing requirement
- **Core Operator Relayer Multisig — signers restructured:** was 3 Amatsu addresses → now **Amatsu (2), SAF (2), Phoenix Labs (1)**. Phoenix Labs may create and propose transactions but execution still requires the 2/5 threshold.
- **Freezer Multisig — control transferred:** was controlled by Governance Facilitators → now controlled by **SAF, Phoenix Labs, and VoteWizard**
- **Freezer Multisig — threshold lowered:** 2/4 → **1/4** signing requirement
- **Freezer Multisig — signers replaced:** was VoteWizard, JanSky, LDR, CivicSage (all Governance Facilitator-aligned) → now **SAF (1), Phoenix Labs (2), VoteWizard (1)**

### Context
SAEP-02 restructures operational security for Spark's two critical multisigs, shifting control from Governance Facilitator-aligned signers toward the Spark-adjacent entities (SAF, Phoenix Labs). The Relayer multisig controls the RELAYER_ROLE for Spark Liquidity Layer operations; the Freezer multisig can invoke the FREEZER_ROLE to halt operations in emergencies. The 1/4 Freezer threshold means any single signer can freeze — optimizing for emergency response speed over consensus. This is part of a broader pattern of Spark operational decentralization from Sky governance. SKY was ~$0.059, USDS supply ~$9.1B.

Forum discussion: https://forum.sky.money/t/saep-02-modify-spark-liquidity-layer-core-relayer-and-freezer-multisig-configuration/27318

---

## PR #105 — Spark proposal - Increase Deposit Caps for spUSDC, spUSDT, and spETH
**Merged:** 2025-11-07 | **Type:** Spark proposal (risk parameter update) | **+3/-3 lines**

### Material Changes
- **Spark Savings spETH supply cap:** 50,000 WETH → **100,000 WETH** (2x increase)
- **Spark Savings spUSDC supply cap:** 250,000,000 USDC → **500,000,000 USDC** (2x increase)
- **Spark Savings spUSDT supply cap:** 250,000,000 USDT → **500,000,000 USDT** (2x increase)

### Context
A straightforward doubling of deposit caps across all three Spark Savings v2 vaults launched in PR #90, likely in response to vaults approaching their initial caps faster than expected. The increases signal strong demand for Spark's yield products. At the time, SKY was trading around $0.043–0.055 and USDS supply was ~$9.1–9.4B.

Forum discussion: https://forum.sky.money/t/november-13-2025-proposed-changes-to-spark-for-upcoming-spell/27354

---

## PR #106 — Spark proposal: Onboard cbETH and ETH market exposure to Morpho USDC vault
**Merged:** 2025-11-07 | **Type:** Spark proposal (new market exposure) | **+42/-0 lines**

### Material Changes
- **New section: Instance-specific Operational Parameters** added to the Morpho USDC Instance Configuration Document, with Market Exposure subsection
- **New market: ETH/USDC 86% LLTV Pool** onboarded — Pool ID `0x8793cf...1bda`, supply cap 1,000,000,000
- **New market: cbETH/USDC 86% LLTV Pool** onboarded — Pool ID `0x1c21c5...2fad`, supply cap 50,000,000

### Context
This proposal extends Spark's Morpho USDC vault exposure by adding two ETH-denominated collateral pools, enabling the vault to earn yield from ETH and cbETH borrowers against USDC. The 20:1 ratio between the ETH pool cap (1B) and cbETH pool cap (50M) reflects the relative liquidity and risk profiles of the two assets. This is part of Spark's broader strategy to diversify SLL yield sources beyond stablecoin-on-stablecoin lending. SKY was ~$0.043–0.055, USDS supply ~$9.1–9.4B.

Forum discussion: https://forum.sky.money/t/november-13-2025-proposed-changes-to-spark-for-upcoming-spell/27354

---

## PR #80 — Spark Proposal - [Ethereum] SparkLend - Increase cbBTC Supply and Borrow Caps
**Merged:** 2025-10-29 | **Type:** Spark proposal (risk parameter update) | **+1/-1 lines**

### Material Changes
- **cbBTC cap automator — supply cap max:** 10,000 cbBTC → **20,000 cbBTC** (2x increase)
- **cbBTC cap automator — borrow cap max:** 500 cbBTC → **10,000 cbBTC** (20x increase)

### Context
A significant increase in cbBTC caps, particularly on the borrow side (20x), reflecting growing demand for borrowing against Coinbase's wrapped Bitcoin on SparkLend. The supply cap increase is more conservative (2x), suggesting Spark is cautiously expanding collateral capacity while substantially unlocking borrowing demand. SKY was ~$0.059–0.063, USDS supply ~$8–9B.

Forum discussion: https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309

---

## PR #81 — Spark Proposal - [Ethereum] SparkLend - Increase tBTC Supply and Borrow Caps
**Merged:** 2025-10-29 | **Type:** Spark proposal (risk parameter update) | **+1/-1 lines**

### Material Changes
- **tBTC cap automator — supply cap max:** 500 tBTC → **1,000 tBTC** (2x increase)
- **tBTC cap automator — borrow cap max:** 250 tBTC → **900 tBTC** (3.6x increase)

### Context
Companion to PR #80 (cbBTC cap increase), this raises tBTC limits with a similar pattern — moderate supply expansion with more aggressive borrow cap growth. The borrow cap max (900 tBTC) approaches the new supply cap (1,000 tBTC), indicating high utilization expectations for Threshold's wrapped BTC product. SKY was ~$0.059–0.063, USDS supply ~$8–9B.

Forum discussion: https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309

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

Forum discussion: https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309

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

Forum discussion: https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309

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

Forum discussion: https://forum.sky.money/t/october-2-2025-proposed-changes-to-spark-for-upcoming-spell/27191

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

Forum discussion: https://forum.sky.money/t/october-30-2025-proposed-changes-to-spark-for-upcoming-spell/27309

---

## PR #93 — Fix location of Ethena PT documents from 2025-10-13 edit
**Merged:** 2025-10-24 | **Type:** Fix (document relocation) | **+1102/-1102 lines**

### Housekeeping
- Moved Ethena PT-USDe and PT-sUSDe Instance Configuration Documents from incorrect inline location to proper Instance Configuration Document sections, replacing the inline content with Location pointer documents
- Large line count (+1102/-1102) is entirely structural relocation — no parameter values, contract addresses, or policy content changed

### Context
A pure structural fix correcting the placement of Ethena PT (Pendle Token) documents that were incorrectly positioned in the October 13 weekly edit. The documents needed to be in the Instances Directory as location pointers, with full configuration documents in the proper Instance Configuration Document section. No operational impact.

---
