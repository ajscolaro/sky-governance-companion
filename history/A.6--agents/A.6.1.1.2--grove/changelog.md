# Grove (GLL) — Change History

Atlas path: `A.6.1.1.2` (1489 docs)

---

## PR #253 — Atlas Edit Proposal — 2026-06-01
**Merged:** 2026-06-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core A.6.1.1.2.2.6.1.2.1.1.1.1.2.4 deleted: Circle CCTP v2 Base To Mainnet** (UUID `16efc874…0706`)
- **New: Circle CCTP v2 TokenMessenger** (`A.6.1.1.2.2.6.1.2.1.1.1.1.3.4`, UUID `2d54c733…b16d`): The address of the Circle CCTP v2 TokenMessenger contract for transferring USDC between Ethereum Mainnet and Avalanche is: `0x28b5a0e9C621a5BadaA536219b3a228C8168cf5d`.
- **Agent Creation Primitive** (`A.6.1.1.2.2.1.1`): `4` → `5`
- **Prime Transformation Primitive** (`A.6.1.1.2.2.1.2`): `4` → `5`
- **Executor Transformation Primitive** (`A.6.1.1.2.2.1.3`): `4` → `5`
- **Agent Token Primitive** (`A.6.1.1.2.2.1.4`): `4` → `5`
- **Genesis Primitives** (`A.6.1.1.2.2.1`): `4` → `5`
- **Executor Accord Primitive** (`A.6.1.1.2.2.2.1`): `5` → `6`
- **Root Edit Primitive** (`A.6.1.1.2.2.2.2`): `5` → `6`
- **Light Agent Primitive** (`A.6.1.1.2.2.2.3`): `5` → `6`
- **Operational Primitives** (`A.6.1.1.2.2.2`): `5` → `6`
- **Ecosystem Upkeep Fee Primitive** (`A.6.1.1.2.2.3.1`): `6` → `7`
- **Upkeep Rebate Primitive** (`A.6.1.1.2.2.3.2`): `6` → `7`
- **Ecosystem Upkeep Primitives** (`A.6.1.1.2.2.3`): `6` → `7`
- **Token SkyLink Primitive** (`A.6.1.1.2.2.4.1`): `7` → `8`
- **SkyLink Primitives** (`A.6.1.1.2.2.4`): `7` → `8`
- **Tracking Methodology** (`A.6.1.1.2.2.5.1.2.1.1.2`): `8` → `9`; `2` → `1`
- **Routine Protocol** (`A.6.1.1.2.2.5.1.2.1.2.1`): `8` → `9`; `8` → `9`; `5` → `3`
- **Distribution Reward Primitive** (`A.6.1.1.2.2.5.1`): `8` → `9`
- **Integration Boost Primitive** (`A.6.1.1.2.2.5.2`): `8` → `9`
- **Terms** (`A.6.1.1.2.2.5.3.2.1.1.2.3`): `8` → `9`
- **Pioneer Chain Primitive** (`A.6.1.1.2.2.5.3`): `8` → `9`
- **Demand Side Stablecoin Primitives** (`A.6.1.1.2.2.5`): `8` → `9`
- **Grove Development Company’s Total Risk Capital (TRC) Management Processes** (`A.6.1.1.2.2.6.1.2.1.3.2`): `9` → `10`
- **Junior Risk Capital Rental Primitive** (`A.6.1.1.2.2.6.2`): `9` → `10`
- **Asset Liability Management Rental Primitive** (`A.6.1.1.2.2.6.3`): `9` → `10`
- **Supply Side Stablecoin Primitives** (`A.6.1.1.2.2.6`): `9` → `10`
- **Core Governance Reward Primitive** (`A.6.1.1.2.2.7.1`): `10` → `11`
- **Core Governance Primitives** (`A.6.1.1.2.2.7`): `10` → `11`

### Housekeeping
- `A.6.1.1.2.2.6.1.2.1.1.1.1.2.3` (Circle CCTP v2 TokenMessenger): `Mainnet To Base` → `TokenMessenger`
- `5` → `6` across 4 docs.
- `9` → `10` across 4 docs.
- `10` → `11` across 2 docs.
- `8` → `9` across 7 docs.
- `4` → `5` across 5 docs.
- `7` → `8` across 2 docs.
- `2` → `1` across 1 doc.
- `5` → `3` across 1 doc.
- `6` → `7` across 3 docs.

### Context
Adds the previously-missing Circle CCTP v2 TokenMessenger address for Avalanche (`0x28b5a0e9…cf5d`) and consolidates two duplicate Base documents recording the same contract into one; the remaining churn is version-reference propagation from the Support Scope (A.2) reorganization.

---

## PR #251 — Atlas Edit Proposal — 2026-05-25
**Merged:** 2026-05-29 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core A.6.1.1.2.2.1.4.2.1.2.4 deleted: Transfer Of Tokens To Grove Labs** (UUID `ebca156f…0f39`)
- **Core A.6.1.1.2.2.1.4.2.1.2.4 deleted: Transfer Of Tokens To Grove Labs** (UUID `ebca156f…0f39`)
- **New: Transfer Of Tokens To Grove Foundation Multisig** (`A.6.1.1.2.2.1.4.2.1.2.3.2`, UUID `0bff1d91…36a4`): Grove will transfer 500 million GROVE tokens from the Grove SubProxy to the Grove Foundation Multisig. (address: `0xE3EC4CC359E68c9dCE15Bf667b1aD37Df54a5a42`)
- **New: Grove Circle CCTP Governance Relay Receivers** (`A.6.1.1.2.2.6.1.2.1.1.1.1.3.3`, UUID `fa8dccc5…ebc4`): The Grove Circle CCTP governance relay receivers on Avalanche are. (addresses: `0x26e9512547feC1906C55256e491DfB6673D8C23f`, `0x8Ea8Dff8c29f568eA1E716E2C3AfbD003EB83cfA`)

### Housekeeping
- `A.6.1.1.2.2.1.4.2.1.2.3` (Transfer Of Tokens To Grove): added `The documents herein specify the subsequent distribution of those tokens from the Grove SubProxy.`
- `A.6.1.1.2.2.6.1.2.1.1.1.1.3.2` (Grove LayerZero v2 Governance Relay Receiver): added `LayerZero v2 Governance Relay`

### Context
Redirects the 500M GROVE distribution from Grove Labs to the new Grove Foundation Multisig (`0xE3EC…5a42`), pairing with the Grove Foundation Grant Authorization multisig edit in A.2. Also adds Avalanche Circle CCTP governance relay receivers, extending Grove's cross-chain relay footprint.

---

## PR #242 — Atlas Edit Proposal — 2026-05-11
**Merged:** 2026-05-15 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Root Edit Voting Process in Urgent and Emergency Situations** (`A.6.1.1.2.2.2.2.2.1.2.3.1`): `8` → `9`
- **Interim Deployment** (`A.6.1.1.2.2.6.1.3.1.9.2.2.5.1`): `9` → `10`

### Housekeeping
- `A.6.1.1.2.3.4.2.2.1` (Parameter Modification): `Facilitators` → `Facilitator`
- `9` → `10` across 1 doc.
- `Facilitators` → `Facilitator` across 1 doc.
- `8` → `9` across 1 doc.
- `Facilitators` → `Core Facilitator` across 1 doc.

---

## PR #237 — Atlas Edit Proposal — 2026-05-04
**Merged:** 2026-05-08 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Ecosystem Accord 10 reference added under Grove** (`A.6.1.1.2.3.5.3`, UUID `e7057828…3e25a`): pointer to the full Accord at `A.2.8.2.10` (UUID `0cb00b28…dc97`) — see `A.2--support` changelog for the Accord's compensation formula (20% of Base Rate × USDS in Chronicle Point Reward Instance, monthly MSC settlement, retroactive to 2025-07-24).

### Context
First ongoing USDS revenue stream Grove receives directly from Sky outside per-spell capital flows. Ratified by Poll #1631 (10-0).

---

## PR #227 — Atlas Edit Proposal — 2026-04-27
**Merged:** 2026-04-30 | **Type:** Weekly edit (Atlas Axis — Poll #1630)

### Material Changes
- **New: Tokenized Treasury JTRSY Instance** (`A.6.1.1.2.2.6.1.3.1.14.1`, UUID `5e38198e…`): USDS-supplied Tokenized Treasury instance via Centrifuge/Anemoy
  - Token: JTRSY at `0x8c213ee79581Ff4984583C6a801e5263418C4b86`; ERC-7540 Vault: `0xFE6920eB6C421f1179cA8c8d4170530CDBdfd77A`
  - Rate limits: **0 USDS inflow / 0 USDS outflow** at launch; Max Swap Size: 50M USD; Credit Token Deposits/Withdrawals/Stablecoin Swaps: all Disabled
  - Owner: Anemoy via Timelock at `0xfB805f2f88e862e687bEBdF120306ef39380F3bf`; RRC Framework: Pending
- **New: Grove x Steakhouse RLUSD Morpho Vault V2 Instance** (`A.6.1.1.2.2.6.1.3.1.7.8`, UUID `cfb29474…`): RLUSD-supplied Morpho vault
  - Token: grove-bbqRLUSD at `0xBeEff4fD39F8e48b6a6e475445D650cb11e9599F`
  - Deposit limits: **100M RLUSD maxAmount / 100M RLUSD per day slope**; Withdrawal: Unlimited
  - maxExchangeRate: `setMaxExchangeRate(GROVE_X_STEAKHOUSE_RLUSD_V2, 1e18, 3e18)`; RRC Framework: Pending
- **New: Tokenized Treasury shared contract infrastructure** (`A.6.1.1.2.2.6.1.2.1.1.1.3`): Chronicle Rate Provider (USDS/USDC) at `0xd79B9a9f5Fc240f2DCfcf260f004110B4713A7e7`; Sky PSM Wrapper at `0xA188EEC8F81263234dA3622A406892F3D630f98c`; RWA Instance Contract address TBD
- **New: Tokenized Treasury Role Hierarchy** (`A.6.1.1.2.2.6.1.2.2.1.6`): 8 roles defined — OWNER_ROLE (via issuer Timelock), MANAGER_ADMIN_ROLE (Grove Proxy `0x1369f7b2…`), MANAGER_ROLE (Grove Relayer Multisig `0x0eEC8664…`), PAUSER_ROLE (Freezer Multisig `0xB0113804…`)

### Context
Both new instances (JTRSY Tokenized Treasury and Grove x Steakhouse RLUSD V2) launch with zero rate limits / disabled swaps, consistent with infrastructure-registration-ahead-of-activation. Note: a separate JTRSY Centrifuge vault with 500M USDS capacity was also onboarded in PR #222 — that is a different product at a different Atlas path (`A.6.1.1.2.2.6.1.3.1.1.4` vs `A.6.1.1.2.2.6.1.3.1.14.1` here).

---

## PR #234 — add Grove Genesis Capital
**Merged:** 2026-04-28 | **Type:** Spell recording (2026-04-09)

Records the Grove Genesis Capital of **25,000,000 USDS** transferred in the April 9, 2026 Executive Vote, adding Grove to the Genesis Capital contributions table alongside Spark (25M), Obex (21M), Skybase (15M), and Core Council Executor Agent 1 (25M).

---

## PR #224 — Atlas Edit Proposal — 2026-04-20
**Merged:** 2026-04-24 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- Distribution Requirement Primitive (`A.6.1.1.2.2.3.1`) renamed to "Ecosystem Upkeep Fee Primitive"; Market Cap Fee Primitive subtree (`A.6.1.1.2.2.3.2`) deleted; Upkeep Rebate references updated.

---

## PR #222 — Atlas Edit Proposal — 2026-04-13
**Merged:** 2026-04-16 | **Type:** Weekly edit (Atlas Axis — Poll 1628) | **+1232/-32 lines**

### Material Changes

- **Grove Liquidity Layer USDS Mint Maximum — 5× expansion** (`A.6.1.1.2.2.6.1.2.1.1.3.1.1`):
  - `maxAmount`: 100M USDS → **500M USDS**
  - `slope`: 50M USDS/day → **500M USDS/day** (10×)
- **New rate limit: USDS to Avalanche via SkyLink** (`A.6.1.1.2.2.6.1.2.1.1.3.1.6`, new): **50M USDS `maxAmount` / 50M USDS/day `slope`**, RateLimitID `LIMIT_LAYERZERO_TRANSFER` (hashed with Avalanche USDS OFT address + Avalanche destination domain)
- **New rate limit: USDS from Avalanche to Ethereum Mainnet via SkyLink** (`A.6.1.1.2.2.6.1.2.1.1.3.2.4`, new): **20M USDS `maxAmount` / 20M USDS/day `slope`**
- **Avalanche USDC→Ethereum CCTP rate limits unbounded** (`A.6.1.1.2.2.6.1.2.1.1.3.2.3`): `maxAmount` 50M USDC → **Unlimited**; `slope` 50M USDC/day → **Unlimited**
- **Avalanche ForeignController upgrade** (`A.6.1.1.2.2.6.1.2.1.1.1.2.2`):
  - Address: `0x734266cE1E49b148eF633f2E0358382488064999` → **`0x4236B772BEeEAFF57550Aa392A0f227C0b908Ce7`**
  - Version: **1.6.0 → 1.8.0** (LayerZero V2 support)
- **New: Grove Executor / Receiver addresses on Avalanche** (`A.6.1.1.2.2.6.1.2.1.1.1.1.3`, new Avalanche Allocator Contracts branch):
  - Grove Executor (Avalanche): `0x4b803781828b76EaBF21AaF02e5ce23596b4d60c`
  - Grove Receiver (Avalanche): `0x380Be2b91B63BF75B194913b6e2C07Df09598c22`
- **New instance: Ethereum Mainnet — Centrifuge JTRSY USDS Vault** (`A.6.1.1.2.2.6.1.3.1.1.4`, new):
  - Protocol: Centrifuge; Asset: USDS; Token: **JTRSY**
  - Token: `0x381f4F3B43C30B78C1f7777553236e57bB8AE9ff`; Underlying: `0xdC035D45…384F` (USDS)
  - Inflow RateLimitID: `0x12a7aab8…26359`; Outflow RateLimitID: `0x90f60b98…aa935`
  - **Inflow: `maxAmount` 500M USDS / `slope` 500M USDS/day**; Outflow: Unlimited
  - RRC Framework Full Implementation Coverage: `Pending`
- **New instance: Avalanche — Curve USDS/USDC Swaps** (`A.6.1.1.2.2.6.1.3.2.2.1`, new): swap-only instance
  - Pool Address: `0xA9d7d3D7…05C8D3`; Underlying USDS: `0x86Ff09db…D1D470`; Underlying USDC: `0xB97EF9Ef…c48a6E`
  - Deposit/Withdrawal: N/A - swaps only
  - **Swap rate limits: `maxAmount` 5M USDS/USDC / `slope` 100M/day / `maxSlippage` 0.1%**
  - RRC: `Pending`
- **New instance: Avalanche — Curve USDS/USDC LP** (`A.6.1.1.2.2.6.1.3.2.2.2`, new): full LP-provisioning instance
  - Same pool/underlying as the swap instance above
  - Inflow RateLimitID: `0xeff5bd77…7e9a36`; Outflow RateLimitID: `0x3361a251…5217cf`
  - **Deposit: 50M / 50M per day**; Withdrawal: Unlimited
  - RRC: `Pending`

### Housekeeping

- Added Instance Configuration Document Location pointers at `A.6.1.1.2.2.6.1.1.2.1.1.4` (Centrifuge JTRSY USDS) and under `A.6.1.1.2.2.6.1.1.2.2.2` (new Avalanche-Curve directory with two location docs)
- Added Avalanche Instances Directory branch in the Active Instances tree (`A.6.1.1.2.2.6.1.1.2.2.2` — Curve)

### Context

The "Update Grove Liquidity Layer For Future Spell Contents" edit is the headline Grove change this cycle and a major structural expansion. Three things stand out: (1) the 5× USDS mint maximum from 100M → 500M signals a significant scale-up of Grove's balance-sheet capacity, aligning with the larger aggregate allocation growth; (2) SkyLink rate limits between Ethereum and Avalanche operationalize the bridge whose governance infrastructure was established in PR #219 (with Grove designated Avalanche Pioneer Prime in that same PR) — the asymmetric rate limits (50M outbound, 20M return) suggest expected net flow from Mainnet to Avalanche; (3) the ForeignController upgrade to 1.8.0 with LayerZero V2 support is the first Grove instance on the new LZ version, consistent with the SkyLink rebranding in PR #219. The Centrifuge JTRSY USDS vault adds a third Centrifuge RWA integration and brings 500M USDS new inflow capacity, while the two new Avalanche Curve instances (swap-only and LP) complete Grove's Avalanche DeFi venue set. Ratification Poll 1628 passed 10-0 with 3 non-voters. SKY ~$0.075, USDS supply ~$11.3B at merge.

---

## PR #219 — Atlas Edit Proposal — 2026-04-06
**Merged:** 2026-04-09 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Maple syrupUSDC Maximum Exposure set to 0 USD** (A.6.1.1.2.2.6.1.3.1.13.1.2.5.2, new): New document added to Grove's Allocation System establishing a zero Maximum Exposure limit for the Maple syrupUSDC Instance, per Core Council Risk Advisor recommendation. Effectively halts new allocations to this vault.

- **Grove Distribution Reward Instance added** (A.6.1.1.2.2.5.1.2.1, new): Grove Finance onboarded to the Distribution Reward Primitive:
  - Reward Code: `2002`
  - Tracking Methodology: Ethereum Mainnet General Tracking Methodology
  - Operational GovOps controls the payment Active Data (direct edit protocol)
  - Payment list currently empty (infrastructure in place, no payments recorded yet)

- **Grove designated Avalanche Pioneer Prime** — Pioneer Chain Primitive status changes:
  - Global Activation Status: `Inactive` → `Active`
  - Avalanche Instance Configuration Document added (A.6.1.1.2.2.5.3.2.1): Network = Avalanche; Pioneer Incentive Pool address and terms defined; Operational Process Definition structure in place

### Housekeeping
- "GLL" abbreviation expanded to "Grove Liquidity Layer" throughout Grove's Allocation System Primitive (A.6.1.1.2.2.6.1): document titles and body text. Same UUIDs; no content changes.

### Context
This PR marks a significant expansion of Grove's operational scope: it simultaneously becomes Avalanche Pioneer Prime (with a Freezer Multisig signer role), activates its Pioneer Chain Primitive, and establishes Distribution Reward infrastructure. The Maple syrupUSDC derisking action (Maximum Exposure = 0) runs in parallel — a Risk Advisor-driven constraint at the same time as operational expansion. Grove is now officially active across Ethereum and Avalanche.

---

## PR #200 — 2026-03-16 Weekly Edit Proposal
**Merged:** 2026-03-20 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Centrifuge ACRDX instance** (`A.6.1.1.2.2.6.1.3.1.1.3`): new Instance Configuration Document added for Ethereum Mainnet Centrifuge ACRDX deployment via Grove Liquidity Layer, with full parameter set (identifiers, contract addresses, rate limits, max exposure).
- **Sentora PYUSD Morpho Vault V2** (`A.6.1.1.2.2.6.1.3.1.7.6`): new Instance Configuration Document added (Ethereum Mainnet; max exchange rate specified).
- **Sentora RLUSD Morpho Vault V2** (`A.6.1.1.2.2.6.1.3.1.7.7`): new Instance Configuration Document added (Ethereum Mainnet).

---

## PR #187 — 2026-02-23 Atlas Edit Weekly Cycle Proposal
**Merged:** 2026-03-05 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- 48 sections, ~59 additions / 52 deletions: systematic link-text conversion from bare UUID references to `A.x.y.z - Name` format in Grove Liquidity Layer instance config documents. No parameter values changed.

---

## PR #186 — 2026-02-16 AEW proposal
**Merged:** 2026-02-22 | **Type:** Weekly edit (Atlas Axis — Poll 1618) | **+2119/-158 lines**

### Material Changes

- **New instance: Ethereum Mainnet — Galaxy Warehouse** (`A.6.1.1.2.2.6.1.3.1.9.2`, new): Grove's first Galaxy Warehouse (Ripple-adjacent) allocation
  - Network: Ethereum Mainnet; Protocol: Galaxy; Asset: **USDC**; Token: N/A
  - Deposit Address (Mainnet): `0x3E23311f9FF660E3c3d87E4b7c207b3c3D7e04f0`
  - Underlying: `0xA0b86991…06eB48` (USDC)
  - Inflow RateLimitID: `0x110ff25f…fc9f9`
  - **Deposit rate limits: `maxAmount` 50M USDC / `slope` 50M USDC/day**; Withdrawal: N/A
  - **Interim Deployment designation** (per A.1.9.2.3.2.2.2): 100% CRR during interim testing, **Maximum Allocation $20M**
  - RRC Framework Full Implementation Coverage: `Pending`
- **New instance: Base — Steakhouse Prime Instant USDC Morpho Vault V2** (`A.6.1.1.2.2.6.1.3.3.2`, new):
  - Network: Base; Protocol: Morpho; Asset: USDC; Token: **steakUSDC**
  - Token Address: `0xbeef0e0834849aCC03f0089F01f4F1Eeb06873C9`
  - Underlying: `0x833589fC…02913` (Base USDC)
  - Inflow RateLimitID: `0xcc331568…53f3b`; Outflow RateLimitID: `0x6cbf2a34…31646`
  - **Deposit rate limits: `maxAmount` 20M USDC / `slope` 20M USDC/day**; Withdrawal: Unlimited
  - **Max Exchange Rate protection:** `setMaxExchangeRate(STEAKHOUSE_PRIME_INSTANT_USDC_V2, 1e18, 2e6)` — 1 share may represent at most 2 USDC
  - RRC Framework Full Implementation Coverage: `Pending`

### Housekeeping

- Added Instance Configuration Document Location pointers at `A.6.1.1.2.2.6.1.1.2.1.9.2` (Galaxy Warehouse) and `A.6.1.1.2.2.6.1.1.2.3.1.2` (Base Steakhouse Prime V2) in the respective Active Instances Directories

### Context

Grove's GLL footprint expands with a new Galaxy Warehouse USDC Mainnet instance (explicitly flagged as an Interim Deployment under the framework introduced by PR #89, meaning 100% CRR during testing and a $20M allocation cap) and a new Base Morpho Vault V2 via Steakhouse Prime — notable for being among the first GLL instances to use the V2 vault standard's `maxExchangeRate` protection, which caps share-to-asset inflation as a defense against faulty yield accrual. Both are Pending RRC certification. The Interim Deployment designation for Galaxy Warehouse signals cautious onboarding of a new counterparty type. SKY ~$0.065, USDS supply ~$9.9B at merge.

---

## PR #172 — Jan 26 Edit
**Merged:** 2026-01-29 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Morpho AUSD vault instance locator renamed** (`A.6.1.1.2.2.6.1.1.2.1.7.2`): "Morpho Grove x Steakhouse High Yield Vault AUSD" → "Ethereum Mainnet - Monad Morpho Grove x Steakhouse High Yield Vault AUSD".
- **Morpho AUSD ICD — Maximum Exposure removed** (`A.6.1.1.2.2.6.1.3.1.7.2.2.5.1`): 100M USDS cap doc deleted.
- **Morpho AUSD ICD — CRR removed** (`A.6.1.1.2.2.6.1.3.1.7.2.2.5.2`): 5% CRR doc deleted (now governed via `A.3` stability CRR entries).
- **Monad Morpho AUSD withdrawal rate limits swapped** (`A.6.1.1.2.2.6.1.3.1.11.1.2.4.2`): `maxAmount` 100M → **10M AUSD**; `slope` 10M → **100M AUSD/day** (transposed).
- **Morpho Vault `.12` Maximum Exposure removed** (`A.6.1.1.2.2.6.1.3.1.12.1.2.5.1`): 100M USDS cap deleted.

---

## PR #156 — January 12 edit
**Merged:** 2026-01-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Allocator Vault parameters added** (`A.6.1.1.2.2.6.1.2.1.1.4.1`, new): ALLOCATOR-BLOOM-A parameters: duty 0, gap 250M USDS, maxLine 5B USDS, ttl 24 hours.
- **Prime Relayer Multisig renamed** to "Prime Primary Relayer Multisig" (`A.6.1.1.2.2.6.1.2.1.2.2.1`); address unchanged (`0x0eEC…F85f`), 4/7 signing.
- **Prime Secondary Relayer Multisig added** (`A.6.1.1.2.2.6.1.2.1.2.2.2`, new): 1/2 signing, address `0x9187…9179`; controlled by Grove, used for `RELAYER_ROLE`.
- **Core Operator Relayer Multisig renumbered** from `.2.2.2` to `.2.2.3`.
- **Freezer Multisig** (`A.6.1.1.2.2.6.1.2.1.2.2.4`): signers changed from VoteWizard/JanSky/LDR/CivicSage (named) to 2× Amatsu GovOps + 2× Endgame Edge + 1× Grove; threshold 2/4 → **2/5**.

---

## PR #150 — 2026 01 05 edit branch
**Merged:** 2026-01-09 | **Type:** Active Data update (Designated Controller)

### Material Changes
- **CCTP upgrade: Mainnet↔Base** (`A.6.1.1.2.2.6.1.2.1.1.1.1.2.3/.4`): CCTP v1 → Circle CCTP v2; Mainnet-to-Base and Base-to-Mainnet contract addresses both updated to `0x28b5a0e9C621a5BadaA536219b3a228C8168cf5d`
- **ALM Controller (MainnetController)** (`A.6.1.1.2.2.6.1.2.1.1.1.2.1.1`): address `0x3048386E09c72C20FB268a37d2B630D7f2Ee9138` → `0xfd9dEA9a8D5B955649579Af482DB7198A392A9F5`
- **ALM Controller Contract Version** (new `A.6.1.1.2.2.6.1.2.1.1.1.2.1.2`): version **1.8.0** (Mainnet)
- **ALM Relayer Multisig** (`A.6.1.1.2.2.6.1.2.1.1.1.2.3.4`): renamed to plural "Addresses"; second relayer added: `0x9187807e07112359C481870feB58f0c117a29179` alongside existing `0x0eEC86649E756a23CBc68d9EFEd756f16aD5F85f`
- **Base ALM Controller** (`A.6.1.1.2.2.6.1.2.1.1.1.2.3.1`): `0x08b045609a673996ca10fedbAFAE2395A21ba539` → `0x7f8408eBbBC3504F83eeDa52910dd75Eba92C955`; version also updated to **1.8.0**
- **USDC CCTP label correction** (`A.6.1.1.2.2.6.1.2.1.1.3.3.3`): renamed from "USDC Base ALM Proxy CCTP Maximum" to "USDC Ethereum Mainnet ALM Proxy CCTP Maximum"
- Subsection renumbering: Freezer Multisig `.1.2` shifted to `.1.3`; Relayer `.1.3` → `.1.4`; Proxy `.1.4` → `.1.5`; Rate Limits `.1.5` → `.1.6`

---

## PR #141 — Dec 8 edit
**Merged:** 2025-12-11 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **DAO Resolution: Project Grove** (`A.6.1.1.2.3.6.6`) — new: 2025-12-11 DAO Resolution authorizing Grove Foundation and Grove (BVI) Ltd to act on Project Grove (IPFS: bafkreiamufzul447ja3prczy7cfxccvsij73vmareedlqag2xxpcwtcgxu)
- **DAO Resolution: Galaxy CLO notes** (`A.6.1.1.2.3.6.7`) — new: 2025-12-11 DAO Resolution authorizing Grove Foundation and Cedar Grove Ltd to subscribe for Class B notes in Galaxy CLO 2025-1 LLC
- Galaxy Interim Deployment articles (`.9.1.2.5.1`, `.5.1.1`, `.5.1.2`) removed — Interim Deployment status graduated

---

## PR #133 — 2025-12-01 AEW Proposal
**Merged:** 2025-12-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Four new GLL instances added** to Grove's Allocation System:
  - **Galaxy Arch CLOs** (A.6.1.1.2.2.6.1.3.1.9): CLO (Collateralized Loan Obligation) allocation via Galaxy protocol on Ethereum Mainnet; RRC: Covered
  - **Ripple RLUSD** (A.6.1.1.2.2.6.1.3.1.10): RLUSD stablecoin instance on Ethereum Mainnet; RRC: Covered
  - **Agora AUSD** (A.6.1.1.2.2.6.1.3.1.11): AUSD stablecoin allocation via Agora protocol; RRC: Covered
  - **Monad Uniswap AUSD/USDC** (A.6.1.1.2.2.6.1.3.1.12): Uniswap pool instance (Monad network) for AUSD/USDC
- **Morpho Grove x Steakhouse High Yield Vault AUSD** (A.6.1.1.2.2.6.1.3.1.7.2): AUSD variant of the existing Steakhouse Morpho vault added on Monad network
- **Base chain infrastructure added** (A.6.1.1.2.2.6.1.2.1.1.1.1.2): Grove Executor, Grove Receiver, and Circle CCTP v2 Base↔Mainnet bridge addresses documented
- **FalconX authorization added** (A.6.1.1.2.3.6.5): authorization document for Grove's use of FalconX (OTC/trading venue)
- **Allocator Contract addresses restructured**: Ethereum Mainnet sub-level added; Securitize instance renamed from "Securitize Tokenized AAA CLO Fund (STAC)" to just "Securitize"

### Context
PR #133 is a significant expansion of Grove's liquidity layer — four new instances in a single edit, including cross-chain (Monad) and new asset classes (RLUSD, AUSD). The Galaxy CLO and Agora/Ripple stablecoin additions reflect Grove's strategy of diversifying beyond traditional DeFi protocols into institutional and stablecoin counterparties.

---

## PR #115 — Atlas Edit Weekly Proposal 2025-11-17
**Merged:** 2025-11-20 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **DAO Resolution — Onboard with Ripple, Agora, and Paxos** added: On 2025-11-20, DAO Resolution passed authorizing Grove Foundation and Bamboo Grove Ltd to onboard with Ripple, Agora, and Paxos. IPFS: `bafkreia7…`

---

## PR #110 — Nov 10 edit
**Merged:** 2025-11-13 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Interim Deployment documents removed from 5 instances:** Curve RLUSD/USDC, Morpho Grove x Steakhouse USDC (x2), Securitize STAC, Aave v3 USDT0 — all graduated from interim testing to normal operation (removed Interim Deployment, Maximum Allocation, and Rate Limits interim testing docs)

### Context
These 5 Grove instances completed their constrained testing period and are now operating under standard risk parameters rather than interim $25M maximum allocation limits.

---

## PR #107 — OOS Atlas Edit
**Merged:** 2025-11-10 | **Type:** Weekly edit (out-of-schedule)

### Material Changes
- **Base rate limits added** to Grove Liquidity Layer: USDC CCTP to Base ALM Proxy and back to Ethereum:
  - maxAmount: 50,000,000 USDC; slope: 50,000,000 USDC per day (both directions)

### Context
Formalizes Grove's cross-chain USDC operations on Base with symmetric 50M USDC rate limits.

---

## PR #96 — October 27 edit
**Merged:** 2025-10-31 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Relayer Multisig** renamed to **Prime Relayer Multisig** (`0x0eEC…5f`); 7 signers controlled by Grove; majority signing required; Grove may change signers at any time (min 2 signers, majority required)
- **Core Operator Relayer Multisig** added: separate multisig for fallback relayer operations
- **Freezer Multisig usage standards** added: detail on when to exercise freeze authority (non-compliance with Risk Capital or ALM rules, or emergency); consultation with Amatsu except when delay would risk fund loss
- **Aave Core v3 RLUSD Instance Configuration Document** added: RLUSD supplied; token `aEthRLUSD` (`0xFa82…c0`); deposit limit: `maxAmount` 50M RLUSD, `slope` 25M/day; withdrawal: unlimited
- **Aave Horizon Interim Deployment** sections removed from two instances (JAAA and one other) — Interim Deployment caps and rate-limit references deleted, replaced with structured ICDs
- **"Governance Facilitators"** → **"Core Facilitator"** in Atlas GitHub update process references
- Spark Artifact also corrected: "Governance Facilitators" → "Core Facilitator" for Atlas GitHub update reference
- Duplicate `<tr>` tag fixed in Spark (Curve pyUSD/USDC section); `<dfn>Avalanche/dfn>` → `<dfn>Avalanche</dfn>` tag fixed in Spark

### Housekeeping
- Grove: "Governance Facilitators" → "Core Facilitator" in update process reference

---

## PR #48 — 2025-08-21 Spell Changes
**Merged:** 2025-08-25 | **Type:** Spell recording (2025-08-21)

### Material Changes
- **Grove Avalanche instances added** (Grove Artifact, new): Full Instance Configuration Document for Centrifuge JTRSY on Avalanche (token JTRSY, asset USDC). Contract addresses for ALM Controller (`0xEc4Cb675AF8C8665903025C2812d1234A1708bb6`), ALM Proxy (`0x7107DD8F56642327945294a18A4280C78e153644`), ALM Rate Limits (`0x6ba2e6bCCe3d2A31F1e3e1d3e11CDffBaA002A21`) recorded.
- **Grove GLL contract address updated** (Mainnet ALM Controller): `0x36036fFd9B1C6966ab23209E073c68Eb9A992f50` → `0xFE6920eB6C421f1179cA8c8d4170530CDBdfd77A`.
- **Grove USDS Mainnet inflow limits**: units corrected (USDC denomination clarified); second SLL inflow instance addresses filled in.
- **SparkLend Dai/USDS/USDT/USDC Slope 1 adjustments** recorded (follow-on to #34 exec, recorded in Spark artifact but also affects Grove cross-references in rate limits).

---

## PR #44 — extra fixes for 2025-08-07 executive
**Merged:** 2025-08-12 | **Type:** Housekeeping

Corrects follow-up issues from PR #34 (2025-08-07 Executive): Grove Avalanche Freezer Multisig address filled in (`0xB0113804960345fd0a245788b3423319c86940e5`); Relayer Multisig filled in (`0x0eEC86649E756a23CBc68d9EFEd756f16aD5F85f`); duplicate "Spark" column in ALM Rate Limits table removed; `MAINNET_MIN_OPERATION_SIZE` code key corrected to `AVALANCHE_MIN_OPERATION_SIZE` for Avalanche off-chain params; `Off-chain Operational Parameters` section added for Ethena sUSDe instance.

---

## PR #34 — 2025-08-07 Executive Changes
**Merged:** 2025-08-12 | **Type:** Spell recording (2025-08-07)

### Material Changes
- **Grove Avalanche GLL infrastructure added** (Grove Artifact, new): ALM Controller (ForeignController Avalanche) `0xEc4Cb675AF8C8665903025C2812d1234A1708bb6`, ALM Proxy `0x7107DD8F56642327945294a18A4280C78e153644`, ALM Rate Limits `0x6ba2e6bCCe3d2A31F1e3e1d3e11CDffBaA002A21` — Freezer and Relayer Multisig addresses TBD (filled in PR #44).
- **USDC Avalanche CCTP rate limits set**: maxAmount 50,000,000 USDC; slope 50,000,000 USDC/day. Ethereum Mainnet CCTP return: maxAmount 50,000,000 / slope 50,000,000/day.
- **USDC Mainnet CCTP limit added**: maxAmount unlimited; slope 0/day.
- **Grove SLL inflow limits set** (two Mainnet instances, previously TBD): both at maxAmount 50,000,000 / slope 50,000,000/day; outflow maxAmount: Unlimited.
- **Grove Mainnet Controller address**: `0x8c213ee79581Ff4984583C6a801e5263418C4b86` → `0x36036fFd9B1C6966ab23209E073c68Eb9A992f50`; USDC address filled in.
- **Grove Ethena USDe instance added** (Ethereum Mainnet, new): USDC → USDe via EthenaMinter; USDe token `0x4c9edd5852cd905f086c759e8383e09bff1e68b3`; EthenaMinter `0xe3490297a08d6fC8Da46Edb7B6142E4F461b62D3`. Inflow: 250M maxAmount / 100M/day; outflow: 500M maxAmount / 200M/day. Full operational procedures for setDelegatedSigner, prepareUSDeMint, approveBurning documented.
- **Grove Ethena sUSDe instance** directory location documents added.

### Context
This is Grove's Avalanche expansion spell — establishing the full GLL infrastructure on Avalanche and enabling Ethena USDe minting via the Mainnet controller. The large inflow/outflow asymmetry on the Ethena instance (250M in vs 500M out) reflects a derisking posture.

---

## PR #32 — Atlas update from 2025-07-24 Exec
**Merged:** 2025-07-29 | **Type:** Spell recording (2025-07-24)

### Material Changes
- **Grove GLL inflow/outflow limits set** (two Mainnet SLL instances, previously TBD): both at maxAmount **50,000,000** / slope **50,000,000/day** inflow; outflow maxAmount: **Unlimited**.
- **Grove Mainnet ALM Controller and USDC addresses** filled in (previously TBD).

---

## PR #22 — Weekly Cycle Atlas Edit 2025-06-30
**Merged:** 2025-07-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Grove public name established**: Atlas renamed "Launch Agent 1" to "Grove" in Ecosystem Accord 1 and all cross-references (parties, exclusivity, right-of-first-refusal, revenue share, DeFi opportunity terms).
- **New Allocation Instance Document Locations added** (Ethereum Mainnet Active Instances Directory):
  - Centrifuge JTRSY
  - Centrifuge JAAA (Invesco CLO ETF)
  - Blackrock BUIDL-I
  - Superstate USTB

### Context
The Grove name reveal is the significant event here — the "Launch Agent 1" pseudonym is retired across the Atlas. The four new Instance Configuration Document Locations formalize Grove's RWA allocation infrastructure. See A.2 changelog for the Ecosystem Accord 3 and Pre-Pioneer Incentive Pool additions in the same PR.

---
