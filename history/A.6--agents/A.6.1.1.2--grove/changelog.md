# Grove (GLL) — Change History

Atlas path: `A.6.1.1.2` (1489 docs)

---

## PR #290 — Grove proposal - [Ethereum] - One-time `collect` on the Grove Uniswap V3 position
**Merged:** 2026-08-07 | **Type:** Housekeeping

### Material Changes
- **New: Fee Collection** (`A.6.1.1.2.2.6.1.3.1.12.2.3.1`, UUID `2e23a8a7…2bcd`): Grove is authorized to execute a one-time collect of all fees accrued on this Instance's Uniswap V3 position (tokenId 1192575 in the Uniswap V3 `NonfungiblePositionManager`), with proceeds received by the ALM Proxy.

### Context
Authorizes a one-time `collect` of accrued fees on Grove's Uniswap V3 position (tokenId 1192575), with proceeds to the ALM Proxy.

---

## PR #285 — Grove proposal - [Ethereum] One-time collect on the Grove Uniswap V3 position
**Merged:** 2026-08-07 | **Type:** Housekeeping

### Material Changes
- **Deposit Rate Limits** (`A.6.1.1.2.2.6.1.3.1.13.1.2.4.1`): `50,000,000 USDC` → `0`; `50,000,000 USDC per day` → `0`

### Context
Zeroes the deposit rate limit (from 50M USDC) on this Grove Uniswap V3 instance, halting new deposits — consistent with winding the position down ahead of a fee collection.

---

## PR #284 — Grove proposal - [Ethereum] Enable the UniswapV3 facet on the Grove DPAU controller
**Merged:** 2026-08-07 | **Type:** Housekeeping

### Material Changes
- **New: Ethereum Mainnet - Grove Diamond PAU Uniswap v3 AUSD/USDC Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.1.12.3`, UUID `bac4c092…1efb`): This Instance's associated Instance Configuration Document is located at `A.6.1.1.2.2.6.1.3.1.12.3`.
- **New: Uniswap v3 Facet** (`A.6.1.1.2.2.6.1.2.2.1.2.2.4`, UUID `5b6d7110…4517`): The Grove Liquidity Layer uses the Uniswap v3 Facet (`A.2.2.10.1.1.1.4.2.20`) to add liquidity to, remove liquidity from, and swap through a Uniswap v3 pool.
- **New: Ethereum Mainnet - Grove Diamond PAU Uniswap v3 AUSD/USDC Instance Configuration Document** (`A.6.1.1.2.2.6.1.3.1.12.3`, UUID `4a3fdcf1…2d83`): The documents herein contain the Instance Configuration Document for the Grove Diamond PAU Uniswap v3 AUSD/USDC Instance.
  - **RRC Framework Full Implementation Coverage** (`A.6.1.1.2.2.6.1.3.1.12.3.1`): **`Pending`**.
  - **Network** (`A.6.1.1.2.2.6.1.3.1.12.3.2.1.1`): Ethereum Mainnet.
  - **Target Protocol** (`A.6.1.1.2.2.6.1.3.1.12.3.2.1.2`): Uniswap v3 AUSD/USDC.
  - **Asset Supplied By Grove Liquidity Layer** (`A.6.1.1.2.2.6.1.3.1.12.3.2.1.3`): USDC and AUSD.
  - **Token** (`A.6.1.1.2.2.6.1.3.1.12.3.2.1.4`): Uniswap V3 AUSD/USDC Pool.
  - **Underlying Asset Address (USDC)** (`A.6.1.1.2.2.6.1.3.1.12.3.2.2.1`): `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`.
  - **Underlying Asset Address (AUSD)** (`A.6.1.1.2.2.6.1.3.1.12.3.2.2.2`): `0x00000000eFE302BEAA2b3e6e1b18d08D69a9012a`.
  - **Pool Address** (`A.6.1.1.2.2.6.1.3.1.12.3.2.2.3`): `0xbAFeAd7c60Ea473758ED6c6021505E8BBd7e8E5d`.
  - **Rate Limit IDs** (`A.6.1.1.2.2.6.1.3.1.12.3.2.3`): The specific `RateLimitID`(s) for this Instance's deposit, withdrawal, and swap operations are defined in the subdocuments herein.
  - **Aggregate Deposit RateLimitID** (`A.6.1.1.2.2.6.1.3.1.12.3.2.3.1`): The aggregate deposit RateLimitID is: `0xd3384d5424cd179640223010fed859f38b86b26e5e0b9ee88b87321b98882f57`.
  - **Deposit RateLimitID (AUSD)** (`A.6.1.1.2.2.6.1.3.1.12.3.2.3.2`): The deposit RateLimitID for AUSD is: `0x89c0cb8c17898781d7c1776eafcf73fd0b570659ad5c3791ddcbefe66b001541`.
  - **Deposit RateLimitID (USDC)** (`A.6.1.1.2.2.6.1.3.1.12.3.2.3.3`): The deposit RateLimitID for USDC is: `0x71efb11b03476e40dcc1ade629d360114fcbf838d70a3211270f69414ba9a187`.
  - **Aggregate Withdrawal RateLimitID** (`A.6.1.1.2.2.6.1.3.1.12.3.2.3.4`): The aggregate withdrawal RateLimitID is: `0xbe8cbf4b779bbe60101d88f64a8afcc8fdf78863df4303da9047b66fcf427734`.
  - **Withdrawal RateLimitID (AUSD)** (`A.6.1.1.2.2.6.1.3.1.12.3.2.3.5`): The withdrawal RateLimitID for AUSD is: `0xf353a8cb19089be9c21260f788c98069b2cef6a8a4bf9d061b3e5e7629a85671`.
  - **Withdrawal RateLimitID (USDC)** (`A.6.1.1.2.2.6.1.3.1.12.3.2.3.6`): The withdrawal RateLimitID for USDC is: `0x17c7a2da0785bd1ad67b8207080dbc243cfc4e573cbac18a68d0bd4b788a1dfc`.
  - **Swap RateLimitID (AUSD)** (`A.6.1.1.2.2.6.1.3.1.12.3.2.3.7`): The swap RateLimitID for AUSD is: `0x7dd93dac252469b97c259284118454a6a09efd0e5f781dec59acc240f8f88402`.
  - **Swap RateLimitID (USDC)** (`A.6.1.1.2.2.6.1.3.1.12.3.2.3.8`): The swap RateLimitID for USDC is: `0x6e850dcb18bea10055c82d1e3753f551b1228d04b81350ba117235de19f9a0da`.
  - **Rate Limits** (`A.6.1.1.2.2.6.1.3.1.12.3.2.4`): The current `maxAmount` and `slope` for this Instance's deposit, withdrawal, and swap operations are defined in the subdocuments herein.
  - **Deposit Rate Limits** (`A.6.1.1.2.2.6.1.3.1.12.3.2.4.1`): The deposit rate limits are.
  - **Withdrawal Rate Limits** (`A.6.1.1.2.2.6.1.3.1.12.3.2.4.2`): The withdrawal rate limits are.
  - **Swap Rate Limits** (`A.6.1.1.2.2.6.1.3.1.12.3.2.4.3`): The swap rate limits are.
  - **Maximum Exposure** (`A.6.1.1.2.2.6.1.3.1.12.3.2.5.1`): Total exposure through this Instance may not exceed 5,000,000 USDS.
  - **CRR** (`A.6.1.1.2.2.6.1.3.1.12.3.2.5.2`): The CRR for this Instance, as specified in `A.3.2.1.1.1`, is 100%.
  - **Instance-specific Operational Processes** (`A.6.1.1.2.2.6.1.3.1.12.3.3`): The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.
  - **Parameters For Stable Stable Pools** (`A.6.1.1.2.2.6.1.3.1.12.3.4.1`): - `twapSecondsAgo`: 600.

### Housekeeping
- `A.6.1.1.2.2.6.1.2.1.1.3.2` (Diamond PAU Rate Limits): `The per` → `Instance`

### Context
Enables the Uniswap v3 facet on Grove's Diamond PAU controller and onboards an AUSD/USDC pool Instance capped at 5,000,000 USDS exposure (100% CRR). The generic Uniswap v3 facet operations it relies on were formalized in the support-scope Diamond PAU edit (#286).

---

## PR #286 — Atlas Edit Proposal — 2026-08-03
**Merged:** 2026-08-06 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Whitelisting Of ALM Proxy** (`A.6.1.1.2.2.6.1.2.1.1.4.2`): `7` → `4.1`; `8` → `4.2`

### Housekeeping
- `7` → `4.1` across 1 doc.
- `8` → `4.2` across 1 doc.

---

## PR #283 — Atlas Edit Proposal — 2026-07-27
**Merged:** 2026-07-30 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core A.6.1.1.2.2.2.2.2.1.2.1.4.1 deleted: Circulating Supply Definition** (UUID `4cd4f590…225e`)
- **Core A.6.1.1.2.2.6.1.2.1.1.1.4.1.6 deleted: Basin Facet Contract** (UUID `206662a7…dc80`)
- **Core A.6.1.1.2.2.6.1.2.1.1.1.4.1.7 deleted: USDS Facet Contract** (UUID `3c70071b…892c`)
- **Core A.6.1.1.2.2.6.1.2.1.1.1.4.1.8 deleted: PSM Facet Contract** (UUID `e95ee55f…51bc`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.3.1 deleted: Encode Mint Function Call** (UUID `137c1b88…1211`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.3.2 deleted: Send Encoded Call** (UUID `79ee81f3…f1c6`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.4.1 deleted: Encode Transfer Function** (UUID `2a0d2948…58c7`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.4.2 deleted: Send Encoded Call** (UUID `043d3c4c…9bce`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.3.1 deleted: Encode Transfer Function Call** (UUID `285f4224…4c84`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.3.2 deleted: Send Encoded Call** (UUID `cdab9e7d…dbaf`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.4.1 deleted: Encode Wipe Function Call** (UUID `f571c4cc…e953`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.4.2 deleted: Send Encoded Call** (UUID `d9ecb48d…0490`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.8 deleted: Swap DAI To USDC** (UUID `fcf618b7…2ca5`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.10 deleted: Convert USDC Amount To DAI Amount** (UUID `810ef030…4d5b`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.11 deleted: Approve Contract Spend** (UUID `fda81f79…ec16`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.12 deleted: Swap DAI to USDS** (UUID `77750a12…277a`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.8 deleted: Split Into Multiple Swaps If Limit Exceeded** (UUID `20dba0ba…1c5d`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.9 deleted: Split Into Multiple Swaps If Limit Exceeded** (UUID `fcd50c06…35c1`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.1.1 deleted: Allocator Role** (UUID `255ff22b…98f0`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.1.2 deleted: Check Rate Limits** (UUID `aa178e60…b3db`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.1.3 deleted: Deposit Asset Into Basin** (UUID `f8f084db…9ac0`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.2.1 deleted: Allocator Role** (UUID `c34e9845…14e5`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.2.2 deleted: Check Rate Limits** (UUID `29e0071b…634e`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.2.3 deleted: Withdraw Asset From Basin** (UUID `4098975f…c0d7`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.3.1 deleted: Allocator Role** (UUID `24c508b8…9672`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.3.2 deleted: Check Rate Limits** (UUID `4f71fb49…e192`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.3.3 deleted: Mint USDS To ALM Proxy** (UUID `08e29676…c412`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.4.1 deleted: Allocator Role** (UUID `a9e7e4c1…5e1f`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.4.2 deleted: Check Rate Limits** (UUID `1eb7a0b0…2d7c`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.4.3 deleted: Burn USDS From ALM Proxy** (UUID `cfdfeb73…64ae`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.4 deleted: Burn USDS** (UUID `f36b04cf…6ba7`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.5.1 deleted: Allocator Role** (UUID `1bcd7223…e1a3`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.5.2 deleted: Check Rate Limits** (UUID `e6412f1c…eab9`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.5.3 deleted: Swap USDS For USDC Through The PSM** (UUID `4ea315ea…9710`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.5 deleted: Swap USDS To USDC** (UUID `5ca78e1e…3b93`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.6.1 deleted: Allocator Role** (UUID `4f91b44b…43ff`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.6.2 deleted: Check Rate Limits** (UUID `6ce4787a…bd4f`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.6.3 deleted: Swap USDC For USDS Through The PSM** (UUID `d5c668a6…29ef`)
- **Core A.6.1.1.2.2.6.1.2.2.1.2.2.6 deleted: Swap USDC To USDS** (UUID `e9b1c13b…07da`)
- **New: Short-Term Transitionary Measures** (`A.6.1.1.2.2.2.2.2.1.2.4`, UUID `a65302b4…b4d6`): During the initial decentralization phase of GROVE token, all decisions on the parameters specified in `A.6.1.1.2.2.6.1` resulting in an increase in the on-chain risk to th.
- **New: Set The LayerZero Recipient** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.2`, UUID `cd46a4fa…0ec2`): The documents herein define the process to set the `layerZeroRecipient` for a specific `destinationEndpointId`.
  - **Admin Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.2.1`): The operator must ensure they are working as an Admin.
  - **Associate LayerZero Recipient With Endpoint** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.2.2`): The operator must associate the `layerZeroRecipient` with the `destinationEndpointId` such that any tokens bridged to this endpoint will go to this recipient.
  - **Emit Event To Logs** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.2.3`): The operator must emit the event to the blockchain logs.
- **New: Set The Max Slippage** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.3`, UUID `7aedf5dd…c616`): The documents herein define the process to set the `maxSlippage` for a specific `pool`.
  - **Admin Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.1`): The operator must ensure they are working as an Admin.
  - **Validate Max Slippage Bound** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.2`): The operator must ensure the provided `maxSlippage` does not exceed `1e18`, reverting with `MainnetController/max-slippage-out-of-bounds` otherwise.
  - **Set Max Slippage For Pool** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.3`): The operator must record the `maxSlippage` for the given `pool` in the `maxSlippages` mapping, which is stored with `1e18` precision.
  - **Emit Event To Logs** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.4`): The operator must emit the event to the blockchain logs.
- **New: Set The Uniswap V3 Pool Max Tick Delta** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.4`, UUID `bf5c8eae…9c21`): The documents herein define the process to set the `swapMaxTickDelta` for a given Uniswap V3 `pool`.
  - **Admin Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.1`): The operator must ensure they are working as an Admin.
  - **Check Max Tick Delta Bounds** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.2`): The operator must ensure the `maxTickDelta` is greater than `0` and does not exceed `UniswapV3Lib.MAX_TICK_DELTA` (`887272`), otherwise the call reverts with `max-tick-delta-out-of-bounds`.
  - **Set The Pool Max Tick Delta** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.3`): The operator must set the `swapMaxTickDelta` on the `uniswapV3PoolParams` for the given `pool` to the supplied `maxTickDelta`.
  - **Emit Event To Logs** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.4`): The operator must emit the event to the blockchain logs.
- **New: Set The Uniswap V3 Add Liquidity Lower Tick Bound** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.5`, UUID `2f4ebdcc…368c`): The documents herein define the process to set the lower `addLiquidityTickBounds` bound for a specific Uniswap V3 `pool`.
  - **Admin Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.1`): The operator must ensure they are working as an Admin.
  - **Validate The Lower Tick Bound** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.2`): The operator must retrieve the stored `UniswapV3PoolParams` for the `pool` and ensure the supplied `lowerTickBound` is greater than or equal to `MIN_TICK` (-887272) and strictly less than the pool's current upper `addLiquidityTickBounds`.
  - **Set The Lower Tick Bound** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.3`): The operator must set the pool's lower `addLiquidityTickBounds` to the supplied `lowerTickBound`, which constrains the lower end of the price range used when adding liquidity to the `pool`.
  - **Emit Event To Logs** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.4`): The operator must emit the event to the blockchain logs.
- **New: Set The Uniswap V3 Add Liquidity Upper Tick Bound** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.6`, UUID `dc3dd2d9…525b`): The documents herein define the process to set the `upper` bound of the `addLiquidityTickBounds` for a given Uniswap V3 `pool`.
  - **Admin Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.6.1`): The operator must ensure they are working as an Admin.
  - **Validate The Upper Tick Bound** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.6.2`): The operator must load the `uniswapV3PoolParams` for the `pool` and ensure the provided `upperTickBound` is greater than the pool's current `addLiquidityTickBounds.lower` and is less than or equal to the `MAX_TICK` of `887272`.
  - **Set The Upper Tick Bound** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.6.3`): The operator must set the `upper` bound of the pool's `addLiquidityTickBounds` to the provided `upperTickBound`.
  - **Emit Event To Logs** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.6.4`): The operator must emit the event to the blockchain logs.
- **New: Set The Uniswap V3 TWAP Seconds Ago** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.7`, UUID `cfdaafcb…4033`): The documents herein define the process to set the `twapSecondsAgo` for a Uniswap V3 `pool`.
  - **Admin Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.1`): The operator must ensure they are working as an Admin.
  - **Validate The TWAP Seconds Ago** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.2`): The operator must load the `UniswapV3PoolParams` for the `pool` and ensure the supplied `twapSecondsAgo` is less than `uint32(type(int32).max)`, which caps the value at approximately 68 years; this bound is required due to the casting in `U.
  - **Set The Pool TWAP Seconds Ago** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.3`): The operator must set the `twapSecondsAgo` on the pool's `UniswapV3PoolParams`, which defines the length of the time-weighted average price window used when the contract consults the `pool`.
  - **Emit Event To Logs** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.4`): The operator must emit the event to the blockchain logs.
- **New: Set The Centrifuge Recipient** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.8`, UUID `869c8941…b5b6`): The documents herein define the process to set the recipient in the `centrifugeRecipients` mapping for a specific `centrifugeId`.
  - **Admin Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.8.1`): The operator must ensure they are working as an Admin.
  - **Associate Recipient With Centrifuge ID** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.8.2`): The operator must associate the `recipient` with the `centrifugeId` such that any tokens transferred to this Centrifuge chain will go to this recipient.
  - **Emit Event To Logs** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.8.3`): The operator must emit the event to the blockchain logs.
- **New: Set The Max Exchange Rate** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.9`, UUID `662ec211…90ec`): The documents herein define the process to set the maximum expected exchange rate for a specific `token`.
  - **Admin Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.9.1`): The operator must ensure they are working as an Admin.
  - **Validate Token Address** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.9.2`): The operator must ensure the `token` is not the zero address, reverting with `MainnetController/token-zero-address` otherwise.
  - **Set And Emit Max Exchange Rate** (`A.6.1.1.2.2.6.1.2.2.1.2.1.1.9.3`): The operator must set the maximum exchange rate for the `token` to the value computed by `_getExchangeRate` from the provided `shares` and `maxExpectedAssets`, which returns `1e36 * assets / shares` at `1e36` precision and reverts with `Mai.
- **New: Ethena Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10`, UUID `6c06a28a…d02d`): The documents herein define the operations performed by the Grove Liquidity Layer to prepare USDe mint and burn through the Ethena minter, manage delegated signers, and cool down and unstake sUSDe.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.1.1`): The operator must ensure they are working as a `RELAYER`.
  - **Set Delegated Signer On Ethena Minter** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.1.2`): The operator must call the `MainnetController` contract to set the `delegatedSigner` on the `ethenaMinter`.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.2.1`): The operator must ensure they are working as a `RELAYER`.
  - **Remove Delegated Signer On Ethena Minter** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.2.2`): The operator must call the `MainnetController` contract to remove the `delegatedSigner` on the `ethenaMinter`.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.3.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.3.2`): The operator must ensure the `RateLimits` allow for minting the required amount, keyed on `LIMIT_USDE_MINT`, and the rate limit is decreased before the approval is set.
  - **Approve USDC To Ethena Minter** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.3.3`): The operator must approve the `ethenaMinter` to spend the `usdcAmount` of `usdc` on behalf of the `proxy`.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.4.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.4.2`): The operator must ensure the `RateLimits` allow for redeeming the required amount, keyed on `LIMIT_USDE_BURN`, and the rate limit is decreased before the approval is set.
  - **Approve USDe To Ethena Minter** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.4.3`): The operator must approve the `ethenaMinter` to spend the `usdeAmount` of `usde` on behalf of the `proxy`.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.5.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.5.2`): The operator must ensure the `RateLimits` allow for cooling down the required amount, keyed on `LIMIT_SUSDE_COOLDOWN`, and the rate limit is decreased before the cooldown is initiated.
  - **Cooldown Assets On sUSDe** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.5.3`): The operator must call the `MainnetController` contract to `cooldownAssets` on `susde` for the `usdeAmount`.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.6.1`): The operator must ensure they are working as a `RELAYER`.
  - **Cooldown Shares On sUSDe** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.6.2`): The operator must call the `MainnetController` contract to `cooldownShares` on `susde` for the `susdeAmount`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.6.3`): The operator must ensure the `RateLimits` allow for the cooldown.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.7.1`): The operator must ensure they are working as a `RELAYER`.
  - **Unstake To ALM Proxy** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.7.2`): The operator must call the `MainnetController` contract to `unstake` from `susde` to the `proxy`.
- **New: Pendle Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.11`, UUID `fdfa763a…91d7`): The documents herein define the operations performed by the Grove Liquidity Layer to redeem expired Pendle Principal Tokens (PT) for their underlying token.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.1`): The operator must ensure they are working as a `RELAYER`.
  - **Validate Market Expiry And Minimum Output** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.2`): The operator must ensure the Pendle market has reached expiry and that a non-zero `minAmountOut` was provided.
  - **Read Market Tokens And Compute Minimum Output** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.3`): The operator must read the market's `SY`, `PT`, and `YT` tokens, resolve the underlying `tokenOut` via `ISY(sy).yieldToken()`, and derive the expected minimum output from the current PY index using `IYT(yt).pyIndexCurrent()`.
  - **Approve Router Spend And Snapshot Balance** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.4`): The operator must approve the `PENDLE_ROUTER` to spend `pyAmountIn` of the `PT` token on behalf of the `proxy`, then record the `proxy`'s `tokenOut` balance before the redemption so the amount received can be measured afterwards.
  - **Redeem PT To Token** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.5`): The operator must redeem the principal tokens for the underlying `tokenOut` by calling `redeemPyToToken` on the `PENDLE_ROUTER` through the `proxy`, sending the proceeds to the `proxy`.
  - **Verify Amount Received** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.6`): The operator must compute the amount of `tokenOut` actually received by the `proxy` and ensure it meets the caller's `minAmountOut`.
  - **Decrease RateLimit** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.7`): The operator must decrease the rate limit after the redemption by the amount of `tokenOut` received, using a key derived from `LIMIT_PENDLE_PT_REDEEM` and the `pendleMarket` address.
- **New: DAI-USDS Migrator Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.12`, UUID `ed0ce400…786d`): The documents herein define the swap operations performed by the Grove Liquidity Layer through the `daiUsds` migrator.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.1.1`): The operator must ensure they are working as a `RELAYER`.
  - **Approve USDS To Migrator** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.1.2`): The operator must approve the `daiUsds` migrator to spend the `usdsAmount` on behalf of the `proxy`.
  - **Swap USDS To DAI** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.1.3`): The operator must swap USDS to DAI.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.2.1`): The operator must ensure they are working as a `RELAYER`.
  - **Approve DAI To Migrator** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.2.2`): The operator must approve the `daiUsds` migrator to spend the `daiAmount` on behalf of the `proxy`.
  - **Swap DAI To USDS** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.2.3`): The operator must swap DAI to USDS.
- **New: LayerZero Bridging Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.13`, UUID `3362e36b…086c`): The documents herein define the operations performed by the Grove Liquidity Layer to bridge tokens cross-chain through LayerZero OFTs from the Grove ALM Proxy to a recipient on a destination endpoint.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.2`): The operator must ensure the `RateLimits` allow for transferring the required `amount`.
  - **Approve Token Transfer** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.3`): The operator must, when the OFT reports that `approvalRequired` is `true`, approve the `oftAddress` to spend the `amount` of the underlying `token` on behalf of the Grove ALM Proxy through `ERC20Lib.approve`.
  - **Build Send Parameters** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.4`): The operator must build the LayerZero `SendParam`.
  - **Quote The Transfer** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.5`): The operator must call `quoteOFT` to determine the `amountReceivedLD` on the destination chain and set `sendParams.minAmountLD` to that value, then call `quoteSend` to obtain the native `MessagingFee` required to deliver the message.
  - **Execute Cross-Chain Transfer** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.6`): The operator must call the `MainnetController` contract to execute the transfer.
- **New: Merkl Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.14`, UUID `8d3cf392…82f3`): The documents herein define the operations performed by the Grove Liquidity Layer to manage the operators authorized to claim Merkl rewards on behalf of the Grove ALM Proxy.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.14.1.1`): The operator must ensure they are working as a `RELAYER`.
  - **Toggle Operator** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.14.1.2`): The operator must toggle the authorization of the `operator` on the Merkl Distributor.
- **New: CCTP Bridging Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.15`, UUID `5511c7f2…3c38`): The documents herein define the cross-chain bridging operations performed by the Grove Liquidity Layer through Circle's Cross-Chain Transfer Protocol (CCTP).
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.2`): The operator must ensure that `RateLimits` allows the transfer, both against the global `LIMIT_USDC_TO_CCTP` limit and the per-destination `LIMIT_USDC_TO_DOMAIN` limit for the target `destinationDomain`.
  - **Check Domain Configuration** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.3`): The operator must ensure a `mintRecipient` has been configured for the target `destinationDomain`.
  - **Approve Contract Spend** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.4`): The operator must approve the `cctp` contract to spend the `usdcAmount` on behalf of the `proxy`, then read the per-message `burnLimit` from the CCTP local minter to determine whether the transfer must be split across multiple messages.
  - **Split Transfer Over Burn Limit** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.5`): The operator must, while the remaining amount exceeds the `burnLimit`, initiate a CCTP transfer of `burnLimit` USDC per message and reduce the remaining amount by `burnLimit` on each iteration.
  - **Transfer Remaining Amount** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.6`): The operator must transfer the remaining amount, which is at or below the `burnLimit`, by calling `depositForBurn` on `cctp` through the `proxy` with `destinationCaller` set to zero, `maxFee` of zero, and a `minFinalityThreshold` of 2000, t.
- **New: Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.1`, UUID `b2767d8e…2311`): The operator must ensure they are working as a `RELAYER`.
- **New: Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.2`, UUID `36c94503…6514`): The operator must ensure that `RateLimits` allow for depositing the required `amount` of the asset into the ERC-4626 vault.
- **New: Get Vault Asset** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.3`, UUID `e4132ae2…337b`): The operator must resolve the underlying `asset` of the ERC-4626 vault by calling `asset` on the `token`.
- **New: Approve Vault Spend** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.4`, UUID `02f75eaa…b066`): The operator must approve the `token` to spend `amount` of the underlying `asset` on behalf of the Grove ALM Proxy.
- **New: Deposit Asset** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.5`, UUID `58b13044…ce3e`): The operator must call `deposit` on the `token` through the `proxy`, depositing `amount` of the underlying asset and directing the minted vault shares to the `proxy`.
- **New: Enforce Exchange Rate** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.6`, UUID `381cbdf4…72ba`): The operator must ensure the realized exchange rate of the deposit does not exceed the configured `maxExchangeRates` for the `token`, otherwise the call reverts with `MainnetController/exchange-rate-too-high`.
- **New: Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2.1`, UUID `75c217fb…eeaa`): The operator must ensure they are working as a `RELAYER`.
- **New: Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2.2`, UUID `6c441069…6191`): The operator must ensure that `RateLimits` allow for withdrawing the required `amount` of the asset from the ERC-4626 vault.
- **New: Withdraw Asset** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2.3`, UUID `acda4904…4463`): The operator must call `withdraw` on the `token` through the `proxy`, withdrawing `amount` of the underlying asset with the `proxy` as both the `receiver` of the asset and the `owner` of the shares being burned.
- **New: Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3.1`, UUID `73d565c3…f9dd`): The operator must ensure they are working as a `RELAYER`.
- **New: Redeem Shares** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3.2`, UUID `0d0eae8c…322b`): The operator must call `redeem` on the `token` through the `proxy`, redeeming `shares` with the `proxy` as both the `receiver` of the underlying asset and the `owner` of the shares being redeemed.
- **New: Decrease Withdraw Rate Limit** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3.3`, UUID `6370eada…1a21`): The operator must decrease the `LIMIT_4626_WITHDRAW` rate limit for the `token` by the actual `assets` received, after the redemption is executed.
- **New: ERC-20 Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.4`, UUID `ad4e80d9…c8e2`): The documents herein define the operations performed by the Grove Liquidity Layer to transfer ERC-20 assets from the Grove ALM Proxy to an approved destination.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1.2`): The operator must ensure the `RateLimits` allow for transferring the required `amount` of the `asset` to the `destination`.
  - **Transfer Asset To Destination** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1.3`): The operator must call the `MainnetController` contract to `transfer` the `amount` of the `asset` from the Grove ALM Proxy to the `destination`.
- **New: ERC-7540 Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5`, UUID `78f3cc3d…72af`): The documents herein define the Grove Liquidity Layer operational procedures for interacting with ERC-7540 asynchronous tokenized vaults.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.2`): The operator must ensure that `RateLimits` allows for depositing the required `amount` of the asset into the ERC-7540 vault.
  - **Get Vault Asset** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.3`): The operator must retrieve the underlying `asset` of the ERC-7540 vault by calling `asset` on the `token`.
  - **Approve Contract Spend** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.4`): The operator must approve the ERC-7540 vault (`token`) to spend the `amount` of the underlying `asset` on behalf of the `proxy`.
  - **Submit Deposit Request** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.5`): The operator must submit the deposit request by calling `requestDeposit` on the ERC-7540 vault, transferring the `amount` of the asset from the `proxy` into the vault.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.2`): The operator must ensure that a rate limit exists for depositing into the ERC-7540 vault.
  - **Get Claimable Shares** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.3`): The operator must determine the number of `shares` that can be claimed by calling `maxMint` for the `proxy` on the ERC-7540 vault.
  - **Claim Shares** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.4`): The operator must claim the `shares` from the vault to the `proxy` by calling `mint` on the ERC-7540 vault.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3.2`): The operator must ensure that `RateLimits` allows for redeeming the requested `shares` from the ERC-7540 vault.
  - **Submit Redeem Request** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3.3`): The operator must submit the redeem request by calling `requestRedeem` on the ERC-7540 vault, transferring the `shares` from the `proxy` into the vault.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.2`): The operator must ensure that a rate limit exists for redeeming from the ERC-7540 vault.
  - **Get Claimable Assets** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.3`): The operator must determine the amount of `assets` that can be claimed by calling `maxWithdraw` for the `proxy` on the ERC-7540 vault.
  - **Claim Assets** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.4`): The operator must claim the `assets` from the vault to the `proxy` by calling `withdraw` on the ERC-7540 vault.
- **New: Centrifuge Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6`, UUID `541710cd…8395`): The documents herein define the Grove Liquidity Layer operations for interacting with Centrifuge V3 asynchronous vaults, including canceling and claiming pending deposit and redeem requests and transferring vault shares across chains.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.1.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.1.2`): The operator must ensure a rate limit is configured for depositing this `token` into the Centrifuge vault.
  - **Cancel Deposit Request** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.1.3`): The operator must call the Centrifuge vault to `cancelDepositRequest` on behalf of the `proxy`.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2.2`): The operator must ensure a rate limit is configured for depositing this `token` into the Centrifuge vault.
  - **Claim Canceled Deposit Request** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2.3`): The operator must call the Centrifuge vault to `claimCancelDepositRequest`, returning the canceled deposit assets to the `proxy`.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.3.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.3.2`): The operator must ensure a rate limit is configured for redeeming this `token` from the Centrifuge vault.
  - **Cancel Redeem Request** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.3.3`): The operator must call the Centrifuge vault to `cancelRedeemRequest` on behalf of the `proxy`.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4.2`): The operator must ensure a rate limit is configured for redeeming this `token` from the Centrifuge vault.
  - **Claim Canceled Redeem Request** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4.3`): The operator must call the Centrifuge vault to `claimCancelRedeemRequest`, returning the canceled redeem shares to the `proxy`.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.1`): The operator must ensure they are working as a `RELAYER`.
  - **Get Configured Recipient** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.2`): The operator must look up the configured recipient for the `destinationCentrifugeId` from the `centrifugeRecipients` mapping.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.3`): The operator must ensure the `RateLimits` allow for transferring the required `amount` of shares.
  - **Check Recipient Configured** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.4`): The operator must ensure a recipient is configured for the `destinationCentrifugeId`.
  - **Get Spoke Address** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.5`): The operator must resolve the `spoke` contract that initiates the cross-chain transfer, obtained from the vault's async redeem `manager`.
  - **Transfer Shares Cross-Chain** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.6`): The operator must initiate the cross-chain share transfer through the resolved `spoke`, forwarding `msg.value` to cover the messaging fee.
- **New: Aave Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.7`, UUID `6ee853cb…cd4d`): The documents herein define the operations performed by the Grove Liquidity Layer to supply and withdraw assets through the Aave protocol.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.1`): The operator must ensure they are working as a `RELAYER`.
  - **Check RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.2`): The operator must ensure the `RateLimits` allow for depositing the required `amount` of the underlying asset.
  - **Check Max Slippage** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.3`): The operator must ensure a maximum slippage has been configured for the `aToken`.
  - **Resolve Pool And Snapshot Balance** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.4`): The operator must resolve the `underlying` asset and the Aave `pool` from the `aToken`, then snapshot the `proxy` current `aToken` balance so the amount of newly minted `aToken` can be measured after the deposit.
  - **Approve Aave Pool Spend** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.5`): The operator must approve the Aave `pool` to spend the `amount` of `underlying` on behalf of the `proxy`, which assumes the `proxy` holds enough of the `underlying` asset.
  - **Supply To Aave Pool** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.6`): The operator must `supply` the `underlying` into the Aave `pool` on behalf of the `proxy`, so that the `proxy` receives the corresponding `aToken`.
  - **Check Slippage** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.7`): The operator must verify the `proxy` received enough `aToken`, measured as the balance increase since the snapshot.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.1`): The operator must ensure they are working as a `RELAYER`.
  - **Resolve Aave Pool** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.2`): The operator must resolve the Aave `pool` from the `aToken` in order to withdraw the underlying asset.
  - **Withdraw Underlying** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.3`): The operator must `withdraw` the underlying asset from the Aave `pool` to the `proxy`, assuming the `proxy` holds adequate `aToken`, and decode the returned `amountWithdrawn`.
  - **Update RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.4`): The operator must decrease the `RateLimits` by the `amountWithdrawn` after the withdrawal completes.
- **New: Curve Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8`, UUID `fc9d9964…627b`): The documents herein define the Curve StableSwap operations performed by the Grove Liquidity Layer, including swapping tokens and providing or withdrawing pool liquidity.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.1`): The operator must ensure they are working as a `RELAYER`.
  - **Validate Swap Parameters** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.2`): The operator must ensure the `inputIndex` and `outputIndex` differ, otherwise the call reverts with `CurveLib/invalid-indices`.
  - **Check Pool Coin Count** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.3`): The operator must ensure both `inputIndex` and `outputIndex` are less than the pool's `N_COINS`, otherwise the call reverts with `CurveLib/index-too-high`.
  - **Enforce Minimum Output** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.4`): The operator must ensure `minAmountOut` is at least the minimum output implied by the pool's `stored_rates` and the configured `maxSlippage`, otherwise the call reverts with `CurveLib/min-amount-not-met`.
  - **Decrease Swap Rate Limit** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.5`): The operator must decrease the `LIMIT_CURVE_SWAP` rate limit for the `pool` by the value of the tokens being swapped in, before the exchange is executed.
  - **Approve Pool Spend** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.6`): The operator must approve the `pool` to spend `amountIn` of the input token on behalf of the `proxy`.
  - **Execute Swap** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.7`): The operator must call `exchange` on the `pool` through the `proxy`, swapping the input token for the output token and returning the received `amountOut` to the `proxy`.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.1`): The operator must ensure they are working as a `RELAYER`.
  - **Validate Deposit Amounts** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.2`): The operator must ensure a `maxSlippage` has been configured for the `pool`, otherwise the call reverts with `CurveLib/max-slippage-not-set`.
  - **Approve And Aggregate Deposit Value** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.3`): The operator must approve the `pool` to spend each deposited token on behalf of the `proxy` and aggregate the total value deposited using the pool's `stored_rates`.
  - **Enforce Minimum LP Amount** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.4`): The operator must ensure `minLpAmount` is at least the aggregated deposit value scaled by `maxSlippage` and the pool's `get_virtual_price`, otherwise the call reverts with `CurveLib/min-amount-not-met`.
  - **Decrease Deposit Rate Limit** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.5`): The operator must decrease the `LIMIT_CURVE_DEPOSIT` rate limit for the `pool` by the aggregated value deposited, before liquidity is added.
  - **Add Liquidity** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.6`): The operator must call `add_liquidity` on the `pool` through the `proxy`, depositing the tokens and returning the minted LP `shares` to the `proxy`.
  - **Decrease Swap Rate Limit** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.7`): The operator must compute the swap implied by the imbalance between the deposited amounts and the value of the minted shares, then decrease the `LIMIT_CURVE_SWAP` rate limit for the `pool` by this implied `averageSwap`, after liquidity is a.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.1`): The operator must ensure they are working as a `RELAYER`.
  - **Validate Minimum Withdraw Amounts** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.2`): The operator must ensure a `maxSlippage` has been configured for the `pool`, otherwise the call reverts with `CurveLib/max-slippage-not-set`.
  - **Aggregate Minimum Withdrawal Value** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.3`): The operator must aggregate the minimum value to be withdrawn from `minWithdrawAmounts` using the pool's `stored_rates`.
  - **Enforce Minimum Withdrawal Value** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.4`): The operator must ensure the aggregated minimum withdrawal value is at least `lpBurnAmount` scaled by the pool's `get_virtual_price` and `maxSlippage`, otherwise the call reverts with `CurveLib/min-amount-not-met`.
  - **Remove Liquidity** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.5`): The operator must call `remove_liquidity` on the `pool` through the `proxy`, burning `lpBurnAmount` LP shares and returning the withdrawn tokens to the `proxy`.
  - **Decrease Withdraw Rate Limit** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.6`): The operator must aggregate the value of the withdrawn tokens using the pool's `stored_rates`, then decrease the `LIMIT_CURVE_WITHDRAW` rate limit for the `pool` by this value, after liquidity is removed.
- **New: Uniswap V3 Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9`, UUID `6f7d6270…9af6`): The documents herein define the operations performed by the Grove Liquidity Layer to swap tokens and provide liquidity through Uniswap V3 pools.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.1`): The operator must ensure they are working as a `RELAYER`.
  - **Validate Swap Parameters** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.2`): The operator must ensure the requested `tickDelta` does not exceed the pool's configured `swapMaxTickDelta`, that the pool's `twapSecondsAgo` is set, and that `minAmountOut` is greater than zero before the swap is routed through `UniswapV3L.
  - **Compute Price Limit** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.3`): The operator must confirm `tokenIn` is one of the pool's two tokens, consult the pool's TWAP tick, and compute the `sqrtPriceLimitX96` bound from the TWAP tick offset by `tickDelta` and bounded to the `TickMath` minimum and maximum, so the.
  - **Approve The Router** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.4`): The operator must approve the Uniswap V3 `router` to spend `amountIn` of `tokenIn` on behalf of the `proxy`, then record the `proxy` starting balance of `tokenIn`.
  - **Execute The Swap** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.5`): The operator must execute the swap by calling `exactInputSingle` on the `router` through the `proxy`, receiving `amountOut` of the output token, then record the `proxy` ending balance of `tokenIn`.
  - **Clear Dust Approval** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.6`): The operator must reset the `router` allowance for `tokenIn` back to zero to clear any dust approval left after the swap.
  - **Decrease RateLimit** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.7`): The operator must decrease the `LIMIT_UNISWAP_V3_SWAP` rate limit for the `tokenIn` and `pool` pair by the amount of `tokenIn` actually spent, which is the difference between the starting and ending balances.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.1`): The operator must ensure they are working as a `RELAYER`.
  - **Validate Deposit Parameters** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.2`): The operator must ensure at least one of the target amounts is greater than zero, that `maxSlippage` is set for the pool, and that the pool's `twapSecondsAgo` is set before the deposit is routed through `UniswapV3Lib`.
  - **Approve The Position Manager** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.3`): The operator must read `token0` and `token1` from the pool and approve the `positionManager` to spend the target amount of each token on behalf of the `proxy`.
  - **Validate Minimum Amounts** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.4`): The operator must validate the minimum amounts by consulting the TWAP tick, computing the expected token amounts for the target liquidity, and requiring each `min` amount to be at least the expected amount scaled by `maxSlippage`.
  - **Mint Or Increase Liquidity** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.5`): The operator must, when `tokenId` is zero, mint a new position after checking the requested `tick` range is within the governance-set bounds and aligned to the pool's tick spacing; otherwise the operator must increase liquidity on the exist.
  - **Clear Dust Approvals** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.6`): The operator must ensure that the liquidity added is not zero, then reset the `positionManager` allowance for both tokens back to zero to clear any dust approval.
  - **Decrease RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.7`): The operator must decrease the `LIMIT_UNISWAP_V3_DEPOSIT` rate limit for the `token0` and `pool` pair by `amount0`, and for the `token1` and `pool` pair by `amount1`, reflecting the tokens actually deposited.
  - **Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.1`): The operator must ensure they are working as a `RELAYER`.
  - **Validate Position Parameters** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.2`): The operator must validate the removal parameters, ensuring the position's tokens and fee match the `pool` and that the requested `liquidity` is greater than zero and does not exceed the position's liquidity.
  - **Verify Ownership And Snapshot Balances** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.3`): The operator must ensure the `proxy` owns the position `tokenId`, then record the `proxy` starting balances of `token0` and `token1` before the withdrawal.
  - **Decrease Liquidity** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.4`): The operator must decrease the position's liquidity by calling `decreaseLiquidity` on the `positionManager` through the `proxy`, passing the requested `liquidity`, the minimum amounts, and the `deadline`.
  - **Collect Tokens** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.5`): The operator must collect the withdrawn tokens by calling `collect` on the `positionManager` through the `proxy`, receiving `amount0Collected` and `amount1Collected`, then record the `proxy` ending balances of `token0` and `token1`.
  - **Validate Minimum Amounts** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.6`): The operator must ensure each `min` amount is at least the collected balance delta scaled by `maxSlippage`, so the withdrawal does not settle below the acceptable bound.
  - **Decrease RateLimits** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.7`): The operator must, for each token collected in a non-zero amount, decrease the `LIMIT_UNISWAP_V3_WITHDRAW` rate limit for that token and `pool` pair by the amount collected.
- **New: Freezer Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.3`, UUID `9e827633…cc56`): The documents herein define the operations performed by the freezer role (see Freezer Role) within the `MainnetController` contract.
  - **Freezer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.3.1.1`): The operator must ensure they are working as a `FREEZER`.
  - **Revoke Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.2.1.3.1.2`): The operator must revoke the `RELAYER` role from the relayer address being removed so that it can no longer operate the contract.
  - **Emit Event To Logs** (`A.6.1.1.2.2.6.1.2.2.1.2.1.3.1.3`): The operator must emit the event to the blockchain logs.
- **New: Monolithic Foreign Controller Contract Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.3`, UUID `a3d8a2af…ea54`): The documents herein define the functions controlled by the `ForeignController` contract for Grove Liquidity Layer operations on foreign chains.
  - **Set The Mint Recipient** (`A.6.1.1.2.2.6.1.2.2.1.2.3.1.1`): The process for setting the mint recipient through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.1 - Set The Mint Recipient](c4c09a75-ef25-4aa.
  - **Set The Max Exchange Rate** (`A.6.1.1.2.2.6.1.2.2.1.2.3.1.10`): The process for setting the max exchange rate through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.9 - Set The Max Exchange Rate](662ec211-4b.
  - **Set The LayerZero Recipient** (`A.6.1.1.2.2.6.1.2.2.1.2.3.1.2`): The process for setting the LayerZero recipient through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.2 - Set The LayerZero Recipient](cd46a4f.
  - **Set The Max Slippage** (`A.6.1.1.2.2.6.1.2.2.1.2.3.1.3`): The process for setting the max slippage through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.3 - Set The Max Slippage](7aedf5dd-c454-4eb3-b9.
  - **Set The Centrifuge Recipient** (`A.6.1.1.2.2.6.1.2.2.1.2.3.1.4`): The process for setting the Centrifuge recipient through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.8 - Set The Centrifuge Recipient](869c8.
  - **Set The Uniswap V3 Pool Max Tick Delta** (`A.6.1.1.2.2.6.1.2.2.1.2.3.1.5`): The process for setting the Uniswap V3 pool max tick delta through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.4 - Set The Uniswap V3 Pool M.
  - **Set The Uniswap V3 Add Liquidity Lower Tick Bound** (`A.6.1.1.2.2.6.1.2.2.1.2.3.1.6`): The process for setting the Uniswap V3 add liquidity lower tick bound through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.5 - Set The Uniswa.
  - **Set The Uniswap V3 Add Liquidity Upper Tick Bound** (`A.6.1.1.2.2.6.1.2.2.1.2.3.1.7`): The process for setting the Uniswap V3 add liquidity upper tick bound through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.6 - Set The Uniswa.
  - **Set The Uniswap V3 TWAP Seconds Ago** (`A.6.1.1.2.2.6.1.2.2.1.2.3.1.8`): The process for setting the Uniswap V3 TWAP seconds ago through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.7 - Set The Uniswap V3 TWAP Seco.
  - **Set The Merkl Distributor** (`A.6.1.1.2.2.6.1.2.2.1.2.3.1.9`): The document herein defines the process to set the `merklDistributor` address used by the `ForeignController` contract to claim Merkl rewards.
  - **Remove Relayer** (`A.6.1.1.2.2.6.1.2.2.1.2.3.2.1`): The process for removing a relayer through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.3.1 - Remove Relayer](a9be43b5-8ddd-4b8e-b64c-c93f05a13.
  - **Deposit To PSM** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.1.1`): The operator, acting as a Relayer, calls `depositPSM` to deposit `amount` of `asset` from the ALM Proxy into the PSM, receiving the corresponding PSM `shares` in return.
  - **Withdraw From PSM** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.1.2`): The operator, acting as a Relayer, calls `withdrawPSM` to withdraw up to `maxAmount` of `asset` from the PSM to the ALM Proxy, returning the amount actually withdrawn as `assetsWithdrawn`.
  - **Toggle Operator Merkl** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.10.1`): The process for toggling an operator on Merkl through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.14.1 - Toggle Operator Merkl](b21fe176-bcb.
  - **Redeem Pendle PT** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.11.1`): The process for redeeming a Pendle PT through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1 - Redeem Pendle PT](ed3e546f-88a2-4a74-b768-5.
  - **Swap Tokens Through Uniswap V3** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.12.1`): The process for swapping tokens through Uniswap V3 through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1 - Swap Tokens Through Uniswap V3].
  - **Add Liquidity To Uniswap V3** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.12.2`): The process for adding liquidity to Uniswap V3 through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2 - Add Liquidity To Uniswap V3](222d77.
  - **Remove Liquidity From Uniswap V3** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.12.3`): The process for removing liquidity from Uniswap V3 through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3 - Remove Liquidity From Uniswap V.
  - **Transfer USDC To CCTP** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.2.1`): The process for transferring USDC to CCTP through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1 - Transfer USDC To CCTP](e8a77685-3069-48.
  - **Transfer Token LayerZero** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.3.1`): The process for transferring a token through LayerZero through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1 - Transfer Token LayerZero](.
  - **Transfer Asset** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.4.1`): The process for transferring an asset through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1 - Transfer Asset](daa8abb8-db47-4dec-845f-fefb.
  - **General Deposit to ERC-4626 Tokens Procedure** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.5.1`): The process for depositing into ERC-4626 tokens through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1 - Deposit To ERC-4626 Vault](4876005.
  - **General Withdraw from ERC-4626 Tokens Procedure** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.5.2`): The process for withdrawing from ERC-4626 tokens through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2 - Withdraw From ERC-4626 Vault](7b5.
  - **General Redeem from ERC-4626 Tokens Procedure** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.5.3`): The process for redeeming from ERC-4626 tokens through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3 - Redeem From ERC-4626 Vault](7e90e50.
  - **Request Deposit To ERC-7540 Vault** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.6.1`): The process for requesting a deposit to an ERC-7540 vault through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1 - Request Deposit To ERC-7.
  - **Claim Deposit From ERC-7540 Vault** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.6.2`): The process for claiming a deposit from an ERC-7540 vault through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2 - Claim Deposit From ERC-7.
  - **Request Redeem From ERC-7540 Vault** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.6.3`): The process for requesting a redeem from an ERC-7540 vault through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3 - Request Redeem From ERC.
  - **Claim Redeem From ERC-7540 Vault** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.6.4`): The process for claiming a redeem from an ERC-7540 vault through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4 - Claim Redeem From ERC-754.
  - **Cancel Centrifuge Deposit Request** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.7.1`): The process for cancelling a Centrifuge deposit request through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.1 - Cancel Centrifuge Deposit.
  - **Claim Centrifuge Cancel Deposit Request** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.7.2`): The process for claiming a Centrifuge cancel deposit request through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2 - Claim Centrifuge Canc.
  - **Cancel Centrifuge Redeem Request** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.7.3`): The process for cancelling a Centrifuge redeem request through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.3 - Cancel Centrifuge Redeem Re.
  - **Claim Centrifuge Cancel Redeem Request** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.7.4`): The process for claiming a Centrifuge cancel redeem request through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4 - Claim Centrifuge Cance.
  - **Transfer Shares Centrifuge** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.7.5`): The process for transferring shares through Centrifuge through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5 - Transfer Shares Centrifuge].
  - **Deposit Into Aave** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.8.1`): The process for depositing into Aave through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1 - Deposit Into Aave](c159a99f-da73-477e-8052-f6.
  - **Withdraw From Aave** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.8.2`): The process for withdrawing from Aave through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2 - Withdraw From Aave](793e928c-9b1f-480f-ab56-.
  - **Swap On Curve** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.9.1`): The process for swapping on Curve through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1 - Swap On Curve](fce783bb-d1b9-4b5e-9577-5149dc494.
  - **Add Liquidity On Curve** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.9.2`): The process for adding liquidity on Curve through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2 - Add Liquidity On Curve](69c7bee3-40d6-44.
  - **Remove Liquidity On Curve** (`A.6.1.1.2.2.6.1.2.2.1.2.3.3.9.3`): The process for removing liquidity on Curve through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3 - Remove Liquidity On Curve](7f63d8d5-51.
- **New: Delegation Framework** (`A.6.1.1.2.3.1.4`, UUID `2cdb1ad7…5f0b`): The documents herein specify Grove's governance delegation system, defining the rights and duties of Delegates and Delegators, as well as the processes for onboarding and offboarding Delegates.
  - **Delegate Definition** (`A.6.1.1.2.3.1.4.1`): A "Delegate" is a recognized actor empowered to exercise governance voting power on behalf of one or more GROVE holders ("Delegators").
  - **How Delegation Works** (`A.6.1.1.2.3.1.4.2`): GROVE holders may assign ("delegate") the full voting power of their wallet to an Active Delegate at any time (see `A.6.1.1.2.3.1.4.8`).
  - **Interfaces** (`A.6.1.1.2.3.1.4.2.1`): Delegation can be executed through (i) the Grove App or (ii) directly on Grove's Snapshot page.
  - **Snapshot Voting-Power Lock** (`A.6.1.1.2.3.1.4.2.2`): A snapshot records voting power at each proposal snapshot-block height.
  - **Undelegation and Re-delegation** (`A.6.1.1.2.3.1.4.2.3`): Delegators may revoke or move their delegation whenever no proposal is live.
  - **Restrictions** (`A.6.1.1.2.3.1.4.2.4`): GROVE holders may only assign their voting power to Active Delegates.
  - **Delegate Responsibilities** (`A.6.1.1.2.3.1.4.3`): The responsibilities for Delegates are defined in the subdocuments herein.
  - **Monitor Governance Channels** (`A.6.1.1.2.3.1.4.3.1`): The Delegate must track the Sky Forum ("Grove Prime" category), Discord, and any other official communication venues for new proposals and discussions.
  - **Review Proposals Thoroughly** (`A.6.1.1.2.3.1.4.3.2`): The Delegate must evaluate technical, economic, and risk implications before voting.
  - **Vote on Every Proposal** (`A.6.1.1.2.3.1.4.3.3`): The Delegate is expected to cast a vote on every governance proposal within the designated voting window.
  - **Abstain Only for Disclosed Conflicts** (`A.6.1.1.2.3.1.4.3.4`): The "Abstain" option may be used solely in cases where the Delegate has a documented conflict of interest for the specific proposal.
  - **Disclosure Of Conflicts** (`A.6.1.1.2.3.1.4.3.4.1`): Conflicts must be disclosed to the Grove Foundation before the voting window (see `A.6.1.1.2.2.2.2.2.1.2.1.4`) for the proposal begins.
  - **Abstaining For Non-Disclosed Conflicts** (`A.6.1.1.2.3.1.4.3.4.2`): Abstaining for any reason other than a disclosed conflict is treated as non-performance under `A.6.1.1.2.3.1.4.5`.
  - **Report Rationale** (`A.6.1.1.2.3.1.4.3.5`): The Delegate must post a concise rationale for each vote on the proposal thread.
  - **Maintain Independence** (`A.6.1.1.2.3.1.4.3.6`): The Delegate must disclose conflicts of interest and abstain where impartiality is compromised (see `A.6.1.1.2.3.1.4.3.4.1`).
  - **Delegate Onboarding** (`A.6.1.1.2.3.1.4.4`): The Delegate onboarding process is specified in the subdocuments herein.
  - **Delegate Onboarding Process** (`A.6.1.1.2.3.1.4.4.1`): The Grove Foundation manages Delegate onboarding.
  - **Application Requirements** (`A.6.1.1.2.3.1.4.4.2`): Prospective Delegates must submit (i) identity and contact information, (ii) delegate wallet address, and (iii) a signed statement accepting the responsibilities in [A.6.1.1.2.3.1.4.3 - Delegate Responsibilities](4493277e-8568-4507-8f7c-ee7.
  - **Requirement To Verify Identity** (`A.6.1.1.2.3.1.4.4.2.1`): Every prospective Delegate must complete an initial, confidential identity verification process with the Grove Foundation, subject to additional KYC verification as necessary in the future.
  - **Conflict-of-Interest Disclosure** (`A.6.1.1.2.3.1.4.4.2.2`): At onboarding, prospective Delegates must provide any known conflicts of interest to the Grove Foundation.
  - **Eligibility** (`A.6.1.1.2.3.1.4.4.2.3`): Individuals or entities listed on any international sanctions list are ineligible to serve as Delegates.
  - **Ongoing Compliance** (`A.6.1.1.2.3.1.4.4.2.4`): Delegates must promptly update the Grove Foundation on any material change in their legal status.
  - **Grounds For Disqualification** (`A.6.1.1.2.3.1.4.4.2.5`): Submission of fraudulent information, criminal indictment for financial crime, or repeated governance negligence (see `A.6.1.1.2.3.1.4.5.2`) constitutes grounds for the Grove F.
  - **Application Does Not Guarantee Acceptance** (`A.6.1.1.2.3.1.4.4.2.6`): Submission of a Delegate Application does not guarantee acceptance.
  - **Minimum Term** (`A.6.1.1.2.3.1.4.4.3`): Delegates are appointed by the Grove Foundation to fixed six (6) month terms aligned to calendar half-years (January 1 – June 30; July 1 – December 31).
  - **Delegate Record** (`A.6.1.1.2.3.1.4.4.4`): Accepted Delegates are appended to `A.6.1.1.2.3.1.4.8`.
  - **Delegate Offboarding** (`A.6.1.1.2.3.1.4.5`): The delegation offboarding process is specified in the subdocuments herein.
  - **Voluntary Offboarding** (`A.6.1.1.2.3.1.4.5.1`): A Delegate can voluntarily offboard by submitting a resignation message in the Grove Prime category of Sky Forum with a signed message from their Delegate wallet as proof.
  - **Non-Performance Removal** (`A.6.1.1.2.3.1.4.5.2`): A Delegate is automatically offboarded if they.
  - **Emergency Removal** (`A.6.1.1.2.3.1.4.5.3`): The Grove Foundation can immediately offboard a delegate if they.
  - **Updating Of Status** (`A.6.1.1.2.3.1.4.5.4`): Upon offboarding, the Delegate's status in `A.6.1.1.2.3.1.4.8` is updated to Inactive.
  - **Incentives And Compensation** (`A.6.1.1.2.3.1.4.6`): Delegates are compensated for their service as follows.
  - **Security Requirements And Compromise Procedure** (`A.6.1.1.2.3.1.4.7`): The security requirements and procedure for a compromised key are specified in the subdocuments herein.
  - **Operational Security** (`A.6.1.1.2.3.1.4.7.1`): Delegates must.
  - **Compromised Key Response** (`A.6.1.1.2.3.1.4.7.2`): If a Delegate suspects key compromise, the following steps must be taken.
  - **Non-Compliance** (`A.6.1.1.2.3.1.4.7.3`): Failure to execute the steps in `A.6.1.1.2.3.1.4.7.2` within 48 hours constitutes grounds for emergency removal.
  - **Template Information For Each Delegate** (`A.6.1.1.2.3.1.4.8.1`): The list of Delegates must follow this template for each recorded Delegate.
  - **Updating List Of Delegates** (`A.6.1.1.2.3.1.4.8.2`): The list of Delegates is defined as Active Data in `A.6.1.1.2.3.1.4.8.2.0.6.1`.
  - **List Of Delegates** (`A.6.1.1.2.3.1.4.8.2.0.6.1`): The information for each Delegate is listed below.
  - **Subject to Change** (`A.6.1.1.2.3.1.4.9`): Grove reserves the right to vary or amend the terms set out in this Delegation Framework (see `A.6.1.1.2.3.1.4`) at its discretion, subject to the established Grove Artifact gover.
- **AccessControls Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.4.1.3`): address `0x4F6d1704700cd494DD4cd9bF59c0C39DA1Bc9164`
- **ALM Rate Limits Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.4.1.4`): address `0xE016Ae733A77Ba77E7907aAA749394Fc5e75C0e1`
- **AdministeredAgent Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.4.1.5`): address `0xdBD17832df0e57b1732cE1C84c652E820e549BAa`
- **Whitelisting Of ALM Proxy** (`A.6.1.1.2.2.6.1.2.1.1.4.2`): `2` → `1.5`; `5619` → `7043`
- **ERC-4626 Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.1.2.2`): `ERC4626` → `ERC-4626`; `ERC20 token` → `ERC-20 asset, and each vault is whitelisted through its configured `RateLimits``
- **Underlying Asset Address** (`A.6.1.1.2.2.6.1.3.4.1.1.2.2.2`): address `0xB8CE59FC3717ada4C02eaDF9682A9e934F625ebb`

### Housekeeping
- `A.6.1.1.2.2.2.2.2.1.2.1.3` (Root Edit Proposal Review By Operational Facilitator): `` → `As part of this review, the Operational Facilitator must determine whether the proposal results in an increase in the on-chain risk to the protocol as described in [A.6.1.1.2.2.2.2.2.1.2.4 - Short-Term Transitionary Measures](a65302b4-5222-48a9-b37f-282498acb4d6), and must state this determination in its finding on the Forum post.`
- `A.6.1.1.2.2.2.2.2.1.2.1.4` (Root Edit Token Holder Vote): `` → `Grove's governance runs in a weekly cycle that begins every Monday. Upon receiving all approvals, the proposal is automatically included in the next cycle. The cut-off time for submitting the proposal in a Forum post is Wednesday 16:00 UTC. After the cut-off time, it is at the discretion of the Operational Facilitator whether the proposal can be included in the immediate next cycle, or the following cycle.`; `` → `Where the proposal is risk-increasing (see [A.6.1.1.2.2.2.2.2.1.2.4 - Short-Term Transitionary Measures](a65302b4-5222-48a9-b37f-282498acb4d6)), the Operational Facilitator triggers the Snapshot poll only after the Core Council Risk Advisor's approval has been obtained.`
- `A.6.1.1.2.2.6.1.1.2.1.15.1` (Ethereum Mainnet - USDC To USDG Via Paxos Instance Configuration Document Location): `to` → `To`
- `A.6.1.1.2.2.6.1.1.2.7.2.1` (Robinhood Chain - USDG To USDC Via Paxos Instance Configuration Document Location): `to` → `To`
- `A.6.1.1.2.2.6.1.2.1.1.1.3.1.1` (Basin Factory Contract): removed `Instance`
- `A.6.1.1.2.2.6.1.2.1.1.1.4.1.5` (AdministeredAgent Contract): removed refs to `A.6.1.1.2.2.6.1.2.2.1.1.3`
- `A.6.1.1.2.2.6.1.2.1.1.1.4` (Diamond PAU Contracts): added refs to `A.2.2.10.1.1.1.4`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.1` (Relayer Role): removed `The operator must ensure they are working as a `Relayer`. Only the `RELAYER` role is allowed to `mintUSDS`. Also, they must ensure the contr…`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.2` (Check RateLimits): `must ensure` → `call decreases`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.3` (Draw USDS To Buffer): `Mint` → `Draw`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.4` (Transfer USDS To ALM Proxy): `The operator must call the `MainnetController` contract to `transfer`` → ``// Transfer`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1` (Mint USDS): `the steps` → `a series of operations`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.1` (Relayer Role): `. They must also ensure` → `, enforced by`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.2` (Check RateLimits): `must ensure` → `call increases (refunds)`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.3` (Transfer USDS To Buffer): `The operator must call the `MainnetController` to `transfer`` → ``// Transfer`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.4` (Burn USDS From Buffer): removed `The operator must call the `MainnetController` contract to `burn` USDS.`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2` (Burn USDS): `the steps` → `a series of operations`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1` (Deposit To ERC-4626 Vault): `to` → `To`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2` (Withdraw From ERC-4626 Vault): `from` → `From`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3` (Redeem From ERC-4626 Vault): `from` → `From`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.1` (Relayer Role): `they must ensure` → `which`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.2` (Check RateLimits): removed `The operator must ensure that `RateLimits` allows for swapping the required USDS amount to USDC.`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.3` (Convert To 18 Token Format): `USDC amounts to an` → `the 6-decimal `usdcAmount` into the`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.4` (Approve Migrator Spend): `Check ALM Proxy` → `Approve Migrator Spend`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.5` (Swap USDS To DAI): `Approve Contract Spend` → `Swap USDS To DAI`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.6` (Approve PSM Spend): `Swap USDS To DAI` → `Approve PSM Spend`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.7` (Swap DAI To USDC): `Approve PSM Spend` → `Swap DAI To USDC`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1` (Swap USDS To USDC): `swap` → `swapUSDSToUSDC`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.1` (Relayer Role): `they must ensure` → `which`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.2` (Refund RateLimit): `Check RateLimits` → `Refund RateLimit`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.3` (Approve PSM Spend): `Check ALM Proxy` → `Approve PSM Spend`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.4` (Swap USDC To DAI): `Approve Contract Spend` → `Swap USDC To DAI`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.5` (Convert To 18 Token Format): `Calculate Swap Limit` → `Convert To 18 Token Format`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.6` (Approve Migrator Spend): `Swap USDC To DAI Directly If Possible` → `Approve Migrator Spend`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.7` (Swap DAI To USDS): `USDC` → `DAI`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2` (Swap USDC To USDS): `swap` → `swapUSDCToUSDS`
- `A.6.1.1.2.2.6.1.2.2.1.2.2.1` (Basin Facet): added refs to `A.2.2.10.1.1.1.4.2.2`
- `A.6.1.1.2.2.6.1.2.2.1.2.2.2` (USDS Facet): added refs to `A.2.2.10.1.1.1.4.2.22`
- `A.6.1.1.2.2.6.1.2.2.1.2.2.3` (PSM Facet): added refs to `A.6.1.1.2.2.6.1.2.1.1.4.2`, `A.2.2.10.1.1.1.4.2.16`
- `A.6.1.1.2.2.6.1.2.2.1.2.2` (Diamond PAU Controller Functions): added refs to `A.2.2.10.1.1.1.5.2`
- `A.6.1.1.2.2.6.1.2.2.3.2.1` (ERC-4626 Withdrawal Action): `from` → `From`
- `A.6.1.1.2.2.6.1.3.1.15.1.2` (Parameters): `to` → `To`
- `A.6.1.1.2.2.6.1.3.1.15.1` (Ethereum Mainnet - USDC To USDG Via Paxos Instance Configuration Document): `to` → `To`
- `A.6.1.1.2.2.6.1.3.7.2.1.2` (Parameters): `to` → `To`
- `A.6.1.1.2.2.6.1.3.7.2.1` (Robinhood Chain - USDG To USDC Via Paxos Instance Configuration Document): `to` → `To`
- Reference renumbering across 1 doc (linked docs moved elsewhere in this edit; UUID targets unchanged).
- `to` → `To` across 7 docs.
- `via` → `Via` across 6 docs.
- `isActive` → `onlyRole(RELAYER)` across 3 docs.
- `Tokens Procedure` → `Vault` across 4 docs.
- `from` → `From` across 3 docs.

### Context
Large structural sync of Grove's Diamond PAU controller documentation — retires the per-operation Encode/Send-Encoded-Call and facet-contract sub-nodes and consolidates the Basin/PSM/mint-burn operations, mirroring the support-scope Allocation System Primitive restructuring in the same edit. Also adds a Short-Term Transitionary Measures clause constraining onchain-risk-increasing parameter changes during the GROVE token decentralization phase.

---

## PR #280 — Atlas Edit Proposal — 2026-07-20
**Merged:** 2026-07-23 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Root Edit Proposal Submission Requirements Exception For Nested Contributors** (`A.6.1.1.2.2.2.2.2.1.2.1.1.1`): `4.2` → `5`

### Housekeeping
- `A.6.1.1.2.2.1.1.3.1.1.4` (Foundation): `Custom Instance Parameters` → `Foundation`
- `A.6.1.1.2.2.1.1.3.1.1.5` renumbered (UUID stable: `830f6fb5…a3d0`)
- `Custom Instance Parameters` → `Foundation` across 1 doc.
- `4.2` → `5` across 2 docs.

---

## PR #277 — Atlas Edit Proposal — 2026-07-13
**Merged:** 2026-07-16 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- `A.6.1.1.2.2.6.2.1.2` (Active Instances Directory): removed `Junior`
- `A.6.1.1.2.2.6.2.1.3` (Completed Instances Directory): removed `Junior`
- `A.6.1.1.2.2.6.2.1.4` (In Progress Invocations Directory): removed `Junior`
- `A.6.1.1.2.2.6.2.1.5.1.1` (Failed Invocations): removed `Junior`
- `A.6.1.1.2.2.6.2.1.5.1.2` (Suspended Instances): removed `Junior`
- `A.6.1.1.2.2.6.2.1.5.1` (Archived Invocations/Instances): removed `Junior`
- `A.6.1.1.2.2.6.2.1` (Primitive Hub Document): removed `Junior`
- `A.6.1.1.2.2.6.2.2` (Active Instances): removed `Junior`
- `A.6.1.1.2.2.6.2.3` (Completed Instances): removed `Junior`
- `A.6.1.1.2.2.6.2.4` (In Progress Invocations): removed `Junior`
- `A.6.1.1.2.2.6.2` (Risk Capital Rental Primitive): removed `Junior`

### Context
"Junior" dropped from the agent's Risk Capital Rental Primitive artifacts as part of the ecosystem-wide risk-capital terminology cleanup.

---

## PR #273 — Atlas Edit Proposal — 2026-07-06
**Merged:** 2026-07-10 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: Paxos** (`A.6.1.1.2.2.6.1.1.2.1.15`, UUID `f1c5403d…8431`): The Ethereum Mainnet Instances Directory of Paxos with `Active` Status are stored herein.
  - **Ethereum Mainnet - USDC to USDG via Paxos Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.1.15.1`): This Instance’s associated Instance Configuration Document is located at `A.6.1.1.2.2.6.1.3.1.15.1`.
- **New: Robinhood Chain** (`A.6.1.1.2.2.6.1.1.2.7`, UUID `c10c4d5a…01f1`): The documents herein contain a Directory of all Instances on Robinhood Chain of the Allocation System Primitive with Instance status of `Active`.
  - **Morpho** (`A.6.1.1.2.2.6.1.1.2.7.1`): The Robinhood Chain Instances Directory of the Morpho Protocol with `Active` Status are stored herein.
  - **Robinhood Chain - Grove x Steakhouse USDG Morpho Vault V2 Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.7.1.1`): This Instance’s associated Instance Configuration Document is located at `A.6.1.1.2.2.6.1.3.7.1.1`.
  - **Paxos** (`A.6.1.1.2.2.6.1.1.2.7.2`): The Robinhood Chain Instances Directory of Paxos with `Active` Status are stored herein.
  - **Robinhood Chain - USDG to USDC via Paxos Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.7.2.1`): This Instance’s associated Instance Configuration Document is located at `A.6.1.1.2.2.6.1.3.7.2.1`.
- **New: Robinhood Chain** (`A.6.1.1.2.2.6.1.2.1.1.1.1.4`, UUID `3b6d2fe2…f1ef`): The documents herein contain the Allocator Contract Addresses on Robinhood Chain.
  - **Grove Executor** (`A.6.1.1.2.2.6.1.2.1.1.1.1.4.1`): The address of the Grove executor on Robinhood Chain is: `0x5ff98717a18833de1A49e11B498866d6Fa1c9296`.
  - **Grove Arbitrum Governance Relay Receiver** (`A.6.1.1.2.2.6.1.2.1.1.1.1.4.2`): The address of the Grove Arbitrum governance relay receiver on Robinhood Chain is: `0xa02eC279eEA9E56F4E14449a07C5ca5FDAAdc51d`.
- **New: Robinhood Chain** (`A.6.1.1.2.2.6.1.2.1.1.1.2.6`, UUID `51488328…9c79`): The documents herein contain the ALM Contract Addresses for the Grove Liquidity Layer on Robinhood Chain.
  - **ALM Controller Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.2.6.1`): The address of the ALM_CONTROLLER contract is: `0x2c10885ddec8d52ecF3Ad2B3833765bf36eD80cf`.
  - **ALM Controller Contract Version** (`A.6.1.1.2.2.6.1.2.1.1.1.2.6.2`): The ALM_CONTROLLER contract version is: 1.8.0.
  - **ALM Freezer Multisig Address** (`A.6.1.1.2.2.6.1.2.1.1.1.2.6.3`): The address of the Multisig that has the Freezer Role is: `0xB0113804960345fd0a245788b3423319c86940e5`.
  - **ALM Relayer Multisig Addresses** (`A.6.1.1.2.2.6.1.2.1.1.1.2.6.4`): The addresses of the Multisigs that have the Relayer Role are: `0x0eEC86649E756a23CBc68d9EFEd756f16aD5F85f` and `0x9187807e07112359C481870feB58f0c117a29179`.
  - **ALM Proxy Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.2.6.5`): The address of the ALM_PROXY contract is: `0x29626c2d8Ca49A51E4dECEEc5499e52983c42BD5`.
  - **ALM Rate Limits Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.2.6.6`): The address of the ALM_RATE_LIMITS contract is: `0xC13e5ff7993c5df911aE562a7736B0eBA12b2010`.
- **New: Paxos** (`A.6.1.1.2.2.6.1.3.1.15`, UUID `bc8cc6e7…ff04`): The Ethereum Mainnet Instances of Paxos with `Active` Status are stored herein.
  - **RRC Framework Full Implementation Coverage** (`A.6.1.1.2.2.6.1.3.1.15.1.1`): **`Pending`**.
  - **Network** (`A.6.1.1.2.2.6.1.3.1.15.1.2.1.1`): Ethereum Mainnet.
  - **Target Protocol** (`A.6.1.1.2.2.6.1.3.1.15.1.2.1.2`): Paxos.
  - **Asset Supplied By Grove Liquidity Layer** (`A.6.1.1.2.2.6.1.3.1.15.1.2.1.3`): USDC.
  - **Token to Receive** (`A.6.1.1.2.2.6.1.3.1.15.1.2.1.4`): USDG.
  - **Token Address** (`A.6.1.1.2.2.6.1.3.1.15.1.2.2.1`): `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`.
  - **Underlying Asset Address** (`A.6.1.1.2.2.6.1.3.1.15.1.2.2.2`): `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`.
  - **Paxos Deposit Address** (`A.6.1.1.2.2.6.1.3.1.15.1.2.2.3`): `0x8C0A9E5939B97979f85d9aDA3d983C6E713Cc2dB`.
  - **Rate Limit IDs** (`A.6.1.1.2.2.6.1.3.1.15.1.2.3`): The transferAssets `RateLimitID` for this conduit is: `0x4139045de2f11ba23865c6cdf20084f6566d834b50716e469c5dbd8ed71faaf1`.
  - **Rate Limits** (`A.6.1.1.2.2.6.1.3.1.15.1.2.4`): The current TransferAsset rate limits for this conduit’s transferAssets operations are defined in the subdocuments herein.
  - **TransferAssets Rate Limits** (`A.6.1.1.2.2.6.1.3.1.15.1.2.4.1`): The transferAssets rate limits are.
  - **Off-chain Operational Parameters** (`A.6.1.1.2.2.6.1.3.1.15.1.2.5`): The documents herein contain specific off-chain parameters for this Instance.
  - **Instance-specific Operational Processes** (`A.6.1.1.2.2.6.1.3.1.15.1.3`): The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.
- **New: Max Exchange Rate** (`A.6.1.1.2.2.6.1.3.1.7.2.2.4.3`, UUID `6894aa1a…df00`): Controllers now have protections that require a `maxExchangeRate` to be set for deposits.
- **New: Max Exchange Rate** (`A.6.1.1.2.2.6.1.3.1.7.4.4.1`, UUID `c7a016f1…b149`): Controllers now have protections that require a `maxExchangeRate` to be set for deposits.
- **New: Maximum Exposure** (`A.6.1.1.2.2.6.1.3.1.7.5.2.5.1`, UUID `8c1e6098…5dc2`): The Maximum Exposure for this Instance is 0 USD.
- **New: Robinhood Chain** (`A.6.1.1.2.2.6.1.3.7`, UUID `f6cfd29f…6aae`): The Robinhood Chain Instances of the Grove Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.
  - **Morpho** (`A.6.1.1.2.2.6.1.3.7.1`): The Robinhood Chain Instances of the Morpho Protocol with `Active` Status are stored herein.
  - **RRC Framework Full Implementation Coverage** (`A.6.1.1.2.2.6.1.3.7.1.1.1`): **`Pending`**.
  - **Network** (`A.6.1.1.2.2.6.1.3.7.1.1.2.1.1`): Robinhood Chain.
  - **Target Protocol** (`A.6.1.1.2.2.6.1.3.7.1.1.2.1.2`): Morpho.
  - **Asset Supplied By Grove Liquidity Layer** (`A.6.1.1.2.2.6.1.3.7.1.1.2.1.3`): USDG.
  - **Token** (`A.6.1.1.2.2.6.1.3.7.1.1.2.1.4`): groveUSDG.
  - **Token Address** (`A.6.1.1.2.2.6.1.3.7.1.1.2.2.1`): `0xBEEff039907422219Fb367e525954DDC092854d9`.
  - **Underlying Asset Address** (`A.6.1.1.2.2.6.1.3.7.1.1.2.2.2`): `0x5fc5360D0400a0Fd4f2af552ADD042D716F1d168`.
  - **Rate Limit IDs** (`A.6.1.1.2.2.6.1.3.7.1.1.2.3`): The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.
  - **Inflow RateLimitID** (`A.6.1.1.2.2.6.1.3.7.1.1.2.3.1`): The inflow RateLimitID is: `0x056c8e9e2046ef2d9e785dd5ffd9eeb475b862bf46f551cf91825eab45225e48`.
  - **Outflow RateLimitID** (`A.6.1.1.2.2.6.1.3.7.1.1.2.3.2`): The outflow `RateLimitID` will be specified in a future iteration of the Grove Artifact.
  - **Rate Limits** (`A.6.1.1.2.2.6.1.3.7.1.1.2.4`): The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.
  - **Deposit Rate Limits** (`A.6.1.1.2.2.6.1.3.7.1.1.2.4.1`): The deposit rate limits are.
  - **Max Exchange Rate** (`A.6.1.1.2.2.6.1.3.7.1.1.2.4.3`): Controllers now have protections that require a `maxExchangeRate` to be set for deposits.
  - **Maximum Exposure** (`A.6.1.1.2.2.6.1.3.7.1.1.2.5.1`): Total USDG exposure may not exceed 100 million USDS.
  - **CRR** (`A.6.1.1.2.2.6.1.3.7.1.1.2.5.2`): The CRR for this Instance, as specified in `A.3.2.1.1.1`, applies to the approved spUSDG/USDG market and is initialized at 3%, decreasing linearly to 0.65% over the four (4).
  - **Paxos** (`A.6.1.1.2.2.6.1.3.7.2`): The Robinhood Chain Instances of Paxos with `Active` Status are stored herein.
  - **RRC Framework Full Implementation Coverage** (`A.6.1.1.2.2.6.1.3.7.2.1.1`): **`Pending`**.
  - **Network** (`A.6.1.1.2.2.6.1.3.7.2.1.2.1.1`): Robinhood Chain.
  - **Target Protocol** (`A.6.1.1.2.2.6.1.3.7.2.1.2.1.2`): Paxos.
  - **Asset Supplied By Grove Liquidity Layer** (`A.6.1.1.2.2.6.1.3.7.2.1.2.1.3`): USDG.
  - **Token to Receive** (`A.6.1.1.2.2.6.1.3.7.2.1.2.1.4`): USDC.
  - **Token Address** (`A.6.1.1.2.2.6.1.3.7.2.1.2.2.1`): `0x5fc5360D0400a0Fd4f2af552ADD042D716F1d168`.
  - **Underlying Asset Address** (`A.6.1.1.2.2.6.1.3.7.2.1.2.2.2`): `0x5fc5360D0400a0Fd4f2af552ADD042D716F1d168`.
  - **Paxos Deposit Address** (`A.6.1.1.2.2.6.1.3.7.2.1.2.2.3`): `0xfC0a7Ed7C5146B26eB38FA92c71F434A7178b06e`.
  - **Rate Limit IDs** (`A.6.1.1.2.2.6.1.3.7.2.1.2.3`): The transferAssets `RateLimitID` for this conduit is: `0x6514f636131e8989437496ad745c5671d7794873c5c1cd6d0a8b5b42031e5c9d`.
  - **Rate Limits** (`A.6.1.1.2.2.6.1.3.7.2.1.2.4`): The current TransferAsset rate limits for this conduit’s transferAssets operations are defined in the subdocuments herein.
  - **TransferAssets Rate Limits** (`A.6.1.1.2.2.6.1.3.7.2.1.2.4.1`): The transferAssets rate limits are.
  - **Off-chain Operational Parameters** (`A.6.1.1.2.2.6.1.3.7.2.1.2.5`): The documents herein contain specific off-chain parameters for this Instance.
  - **Instance-specific Operational Processes** (`A.6.1.1.2.2.6.1.3.7.2.1.3`): The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.
- **Ethereum Mainnet - Grove x Steakhouse USDC Morpho Vault v2 Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.1.7.2`): `27f06e65` → `6ec606f0`; `8397` → `bc47`; `449a` → `4f36`; `b002` → `8591`; `abaa0416badc` → `75784bb78b00`
- **Ethereum Mainnet - Steakhouse PYUSD Morpho Vault Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.1.7.3`): `8591` → `9729`
- **Ethereum Mainnet - Grove x Steakhouse AUSD Morpho Vault V2 Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.1.7.4`): `9729` → `9578`
- **Ethereum Mainnet - Sentora PYUSD Morpho Vault V2 Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.1.7.5`): `2c21462b` → `3e940e02`; `2925` → `80eb`; `48d8` → `4e37`; `9578` → `bce6`; `5fc21aa96563` → `95939089da46`
- **Ethereum Mainnet - Sentora RLUSD Morpho Vault V2 Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.1.7.6`): `3e940e02` → `dff6df5f`; `80eb` → `f8ab`; `4e37` → `4df1`; `bce6` → `be1e`; `95939089da46` → `f71510c3534e`
- **Ethereum Mainnet - Grove x Steakhouse RLUSD Morpho Vault V2 Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.1.7.7`): `dff6df5f` → `cfb29474`; `f8ab` → `ea48`; `4df1` → `4370`; `be1e` → `aad6`; `f71510c3534e` → `23af1cf4d11a`
- **Token Address** (`A.6.1.1.2.2.6.1.3.1.7.2.2.2.1`): address `0xBeefF08dF54897e7544aB01d0e86f013DA354111`
- **Inflow RateLimitID** (`A.6.1.1.2.2.6.1.3.1.7.2.2.3.1`): `0x098ad67dc41c1a5892ec3ef5fd411198dc11962475e9ef2e0362e6cb7f5a2174` → `0xe9ff67ad8829919752eee93c75433e7e23f3460ca6b1d9576fae94f669fbc4d6`
- **Deposit Rate Limits** (`A.6.1.1.2.2.6.1.3.1.7.2.2.4.1`): `50` → `20`; `50` → `20`
- **Token Address** (`A.6.1.1.2.2.6.1.3.1.7.3.2.2.1`): address `0xd8A6511979D9C5D387c819E9F8ED9F3a5C6c5379`
- **Underlying Asset Address** (`A.6.1.1.2.2.6.1.3.1.7.3.2.2.2`): address `0x6c3ea9036406852006290770BEdFcAbA0e23A0e8`
- **Inflow RateLimitID** (`A.6.1.1.2.2.6.1.3.1.7.3.2.3.1`): `0xe9ff67ad8829919752eee93c75433e7e23f3460ca6b1d9576fae94f669fbc4d6` → `0xfc4e1f8ba7b0389a287411c3f6b97cc0ec60fb2816bfaa31e12a21561486321a`
- **Outflow RateLimitID** (`A.6.1.1.2.2.6.1.3.1.7.3.2.3.2`): `0xb6204f88cd26e1d2b5c27fe0beb10cc2c6a33aac17f228baffcb5cc3c8429a7b` → `0xa0c827fea02219c83969babf0bd29df5bb5fe923e6b38491a5eea797984995e8`
- **Max Exchange Rate** (`A.6.1.1.2.2.6.1.3.1.7.3.2.4.3`): `2e6` → `4e6`
- **Token Address** (`A.6.1.1.2.2.6.1.3.1.7.4.2.2.1`): address `0xBEEfF0d672ab7F5018dFB614c93981045D4aA98a`
- **Underlying Asset Address** (`A.6.1.1.2.2.6.1.3.1.7.4.2.2.2`): address `0x00000000eFE302BEAA2b3e6e1b18d08D69a9012a`
- **Inflow RateLimitID** (`A.6.1.1.2.2.6.1.3.1.7.4.2.3.1`): `0xfc4e1f8ba7b0389a287411c3f6b97cc0ec60fb2816bfaa31e12a21561486321a` → `0x09b5f924263c1b33d619ff1c9c794ddf57bc2eb0f618e2cf5cfd838abecb541d`
- **Outflow RateLimitID** (`A.6.1.1.2.2.6.1.3.1.7.4.2.3.2`): `0xa0c827fea02219c83969babf0bd29df5bb5fe923e6b38491a5eea797984995e8` → `0xdd975e5dc9904260242e80bbe7035784e9108c619e23f21b62342fae3226e0fe`
- **Token Address** (`A.6.1.1.2.2.6.1.3.1.7.5.2.2.1`): address `0xb576765fB15505433aF24FEe2c0325895C559FB2`
- **Underlying Asset Address** (`A.6.1.1.2.2.6.1.3.1.7.5.2.2.2`): address `0x6c3ea9036406852006290770BEdFcAbA0e23A0e8`
- **Inflow RateLimitID** (`A.6.1.1.2.2.6.1.3.1.7.5.2.3.1`): `0x09b5f924263c1b33d619ff1c9c794ddf57bc2eb0f618e2cf5cfd838abecb541d` → `0x4dc0c7cd471560aa12324cb36f720d7d301ef230d3ae772ae07b681725ae7b66`
- **Outflow RateLimitID** (`A.6.1.1.2.2.6.1.3.1.7.5.2.3.2`): `0xdd975e5dc9904260242e80bbe7035784e9108c619e23f21b62342fae3226e0fe` → `0x8edef92c8bf76460b6b832a88c63768022ac5aa2bd862fb858905a0f024bff8b`
- **Deposit Rate Limits** (`A.6.1.1.2.2.6.1.3.1.7.5.2.4.1`): `20` → `50`; `20` → `50`
- **Max Exchange Rate** (`A.6.1.1.2.2.6.1.3.1.7.5.4.1`): `2 AUSD` → `3 PYUSD`; `GROVE_X_STEAKHOUSE_AUSD_V2` → `SENTORA_PYUSD_MAIN_V2`; `2e6` → `3e6`
- **Token Address** (`A.6.1.1.2.2.6.1.3.1.7.6.2.2.1`): address `0x6dC58a0FdfC8D694e571DC59B9A52EEEa780E6bf`
- **Underlying Asset Address** (`A.6.1.1.2.2.6.1.3.1.7.6.2.2.2`): address `0x8292Bb45bf1Ee4d140127049757C2E0fF06317eD`
- **Inflow RateLimitID** (`A.6.1.1.2.2.6.1.3.1.7.6.2.3.1`): `0x4dc0c7cd471560aa12324cb36f720d7d301ef230d3ae772ae07b681725ae7b66` → `0x944bbb34c3717aacc72419f43d62f5a01d2ebd7a9157ba9975fd7d971deb803f`
- **Outflow RateLimitID** (`A.6.1.1.2.2.6.1.3.1.7.6.2.3.2`): `0x8edef92c8bf76460b6b832a88c63768022ac5aa2bd862fb858905a0f024bff8b` → `0xfc41a8cf89ec93b54bbf6960204c29c48a7ed98ec4a88dade68149dee919e788`
- **Max Exchange Rate** (`A.6.1.1.2.2.6.1.3.1.7.6.4.1`): `SENTORA_PYUSD_MAIN_V2` → `SENTORA_RLUSD_MAIN_V2`; `3e6` → `3e18`
- **Token Address** (`A.6.1.1.2.2.6.1.3.1.7.7.2.2.1`): address `0xBeEff4fD39F8e48b6a6e475445D650cb11e9599F`
- **Inflow RateLimitID** (`A.6.1.1.2.2.6.1.3.1.7.7.2.3.1`): `0x944bbb34c3717aacc72419f43d62f5a01d2ebd7a9157ba9975fd7d971deb803f` → `0xf655bc101a615fbcb591acce756dacae96cb119ff1beec548d9cc5d4558ea53a`
- **Outflow RateLimitID** (`A.6.1.1.2.2.6.1.3.1.7.7.2.3.2`): `0xfc41a8cf89ec93b54bbf6960204c29c48a7ed98ec4a88dade68149dee919e788` → `0xa6e68f8214d2fb32e0deb2888ef4644c36401d18605447843e4f936529f6a3cb`
- **Deposit Rate Limits** (`A.6.1.1.2.2.6.1.3.1.7.7.2.4.1`): `50` → `100`; `50` → `100`
- **Max Exchange Rate** (`A.6.1.1.2.2.6.1.3.1.7.7.4.1`): `SENTORA_RLUSD_MAIN_V2` → `GROVE_X_STEAKHOUSE_RLUSD_V2`

### Housekeeping
- `A.6.1.1.2.2.6.1.2.1.1.3.1.1.1` (USDS Mint Maximum): removed `(USDS)`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.1.2` (USDS Burn Maximum): removed `(USDS)`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.1.4` (USDC Mainnet ALM Proxy Maximum): removed `(USDC)`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.1.5` (Maximum USDC Bridged To Ethereum Mainnet Via Circle CCTP): `ALM Proxy` → `Via`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.1.6` (Maximum USDS Bridged From Ethereum Mainnet To Avalanche Via SkyLink): added `Maximum`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.2.1` (USDC Avalanche ALM Proxy Maximum): removed `(USDC)`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.2.2` (Maximum USDC Bridged From Ethereum Mainnet To Avalanche Via Circle CCTP): `ALM Proxy` → `Via`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.2.3` (Maximum USDC Bridged From Avalanche To Ethereum Mainnet Via Circle CCTP): `ALM Proxy` → `Via`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.2.4` (Maximum USDS Bridged From Avalanche To Ethereum Mainnet Via SkyLink): added `Maximum`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.3.2` (Maximum USDC Bridged From Ethereum Mainnet To Base Via Circle CCTP): `ALM Proxy` → `Via`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.3.3` (Maximum USDC Bridged From Base To Ethereum Mainnet Via Circle CCTP): `ALM Proxy` → `Via`
- `A.6.1.1.2.2.6.1.2.1.1.3.2.1` (USDS Mint Maximum): removed `(USDS)`
- `A.6.1.1.2.2.6.1.2.1.1.3.2.2` (USDS Burn Maximum): removed `(USDS)`
- `A.6.1.1.2.2.6.1.3.1.1.2.2.4.1` (Inflow Rate Limits): `.` → `per day`
- `A.6.1.1.2.2.6.1.3.1.13.1.2.4.2` (Withdrawal Rate Limits): removed `USDC`
- `A.6.1.1.2.2.6.1.3.1.2.1.2.4.1` (Inflow Rate Limits): removed `(per day)`
- `A.6.1.1.2.2.6.1.3.1.7.2.1` (RRC Framework Full Implementation Coverage): content edit
- `A.6.1.1.2.2.6.1.3.1.7.2.2.1.1` (Network): content edit
- `A.6.1.1.2.2.6.1.3.1.7.2.2.1.2` (Target Protocol): `Morpho` → `Grove x Steakhouse USDC High Yield Vault V2`
- `A.6.1.1.2.2.6.1.3.1.7.2.2.1.3` (Asset Supplied By Grove Liquidity Layer): content edit
- `A.6.1.1.2.2.6.1.3.1.7.2.2.1.4` (Token): `bbqAUSD` → `bbqUSDC`
- `A.6.1.1.2.2.6.1.3.1.7.2.2.1` (Instance Identifiers): content edit
- `A.6.1.1.2.2.6.1.3.1.7.2.2.2.2` (Underlying Asset Address): content edit
- `A.6.1.1.2.2.6.1.3.1.7.2.2.2` (Contract Addresses): content edit
- `A.6.1.1.2.2.6.1.3.1.7.2.2.3.2` (Outflow RateLimitID): `N/A` → ``0xb6204f88cd26e1d2b5c27fe0beb10cc2c6a33aac17f228baffcb5cc3c8429a7b``
- `A.6.1.1.2.2.6.1.3.1.7.2.2.3` (Rate Limit IDs): content edit
- `A.6.1.1.2.2.6.1.3.1.7.2.2.4.2` (Withdrawal Rate Limits): `N/A` → `Unlimited`
- `A.6.1.1.2.2.6.1.3.1.7.2.2.4` (Rate Limits): content edit
- `A.6.1.1.2.2.6.1.3.1.7.2.2.5` (Off-chain Operational Parameters): content edit
- `A.6.1.1.2.2.6.1.3.1.7.2.2` (Parameters): `High Yield` → `USDC Morpho`
- `A.6.1.1.2.2.6.1.3.1.7.2.3` (Instance-specific Operational Processes): content edit
- `A.6.1.1.2.2.6.1.3.1.7.2` (Ethereum Mainnet - Grove x Steakhouse USDC Morpho Vault v2 Instance Configuration Document): `High Yield` → `USDC Morpho`
- `A.6.1.1.2.2.6.1.3.1.7.3.1` (RRC Framework Full Implementation Coverage): content edit
- `A.6.1.1.2.2.6.1.3.1.7.3.2.1.1` (Network): content edit
- `A.6.1.1.2.2.6.1.3.1.7.3.2.1.2` (Target Protocol): `USDC High Yield` → `PYUSD Morpho`
- `A.6.1.1.2.2.6.1.3.1.7.3.2.1.3` (Asset Supplied By Grove Liquidity Layer): `USDC` → `PYUSD`
- `A.6.1.1.2.2.6.1.3.1.7.3.2.1.4` (Token): `bbqUSDC` → `bbqPYUSD`
- `A.6.1.1.2.2.6.1.3.1.7.3.2.1` (Instance Identifiers): content edit
- `A.6.1.1.2.2.6.1.3.1.7.3.2.2` (Contract Addresses): content edit
- `A.6.1.1.2.2.6.1.3.1.7.3.2.3` (Rate Limit IDs): content edit
- `A.6.1.1.2.2.6.1.3.1.7.3.2.4.1` (Deposit Rate Limits): `USDC` → `PYUSD`
- `A.6.1.1.2.2.6.1.3.1.7.3.2.4.2` (Withdrawal Rate Limits): content edit
- `A.6.1.1.2.2.6.1.3.1.7.3.2.4` (Rate Limits): content edit
- `A.6.1.1.2.2.6.1.3.1.7.3.2.5` (Off-chain Operational Parameters): content edit
- `A.6.1.1.2.2.6.1.3.1.7.3.2` (Parameters): `USDC` → `PYUSD`
- `A.6.1.1.2.2.6.1.3.1.7.3.3` (Instance-specific Operational Processes): content edit
- `A.6.1.1.2.2.6.1.3.1.7.3` (Ethereum Mainnet - Steakhouse PYUSD Morpho Vault Instance Configuration Document): `USDC` → `PYUSD`
- `A.6.1.1.2.2.6.1.3.1.7.4.1` (RRC Framework Full Implementation Coverage): content edit
- `A.6.1.1.2.2.6.1.3.1.7.4.2.1.1` (Network): content edit
- `A.6.1.1.2.2.6.1.3.1.7.4.2.1.2` (Target Protocol): `PYUSD` → `AUSD`
- `A.6.1.1.2.2.6.1.3.1.7.4.2.1.3` (Asset Supplied By Grove Liquidity Layer): `PYUSD` → `AUSD`
- `A.6.1.1.2.2.6.1.3.1.7.4.2.1.4` (Token): `bbqPYUSD` → `bbqAUSD`
- `A.6.1.1.2.2.6.1.3.1.7.4.2.1` (Instance Identifiers): content edit
- `A.6.1.1.2.2.6.1.3.1.7.4.2.2` (Contract Addresses): content edit
- `A.6.1.1.2.2.6.1.3.1.7.4.2.3` (Rate Limit IDs): content edit
- `A.6.1.1.2.2.6.1.3.1.7.4.2.4.1` (Deposit Rate Limits): `PYUSD` → `AUSD`
- `A.6.1.1.2.2.6.1.3.1.7.4.2.4.2` (Withdrawal Rate Limits): content edit
- `A.6.1.1.2.2.6.1.3.1.7.3.2.4.3` (Max Exchange Rate): removed `###### A.6.1.1.2.2.6.1.3.1.7.4.2.4.3 - Max Exchange Rate [Core]`
- `A.6.1.1.2.2.6.1.3.1.7.4.2.4` (Rate Limits): content edit
- `A.6.1.1.2.2.6.1.3.1.7.4.2.5` (Off-chain Operational Parameters): content edit
- `A.6.1.1.2.2.6.1.3.1.7.4.2` (Parameters): `PYUSD` → `AUSD`
- `A.6.1.1.2.2.6.1.3.1.7.4.3` (Instance-specific Operational Processes): content edit
- `A.6.1.1.2.2.6.1.3.1.7.4` (Ethereum Mainnet - Grove x Steakhouse AUSD Morpho Vault V2 Instance Configuration Document): `PYUSD` → `AUSD`
- `A.6.1.1.2.2.6.1.3.1.7.5.1` (RRC Framework Full Implementation Coverage): removed `**`
- `A.6.1.1.2.2.6.1.3.1.7.5.2.1.1` (Network): content edit
- `A.6.1.1.2.2.6.1.3.1.7.5.2.1.2` (Target Protocol): `Grove x Steakhouse AUSD` → `Sentora PYUSD`
- `A.6.1.1.2.2.6.1.3.1.7.5.2.1.3` (Asset Supplied By Grove Liquidity Layer): `AUSD` → `PYUSD`
- `A.6.1.1.2.2.6.1.3.1.7.5.2.1.4` (Token): `grove-bbqAUSD` → `senPYUSDmain`
- `A.6.1.1.2.2.6.1.3.1.7.5.2.1` (Instance Identifiers): content edit
- `A.6.1.1.2.2.6.1.3.1.7.5.2.2` (Contract Addresses): content edit
- `A.6.1.1.2.2.6.1.3.1.7.5.2.3` (Rate Limit IDs): content edit
- `A.6.1.1.2.2.6.1.3.1.7.5.2.4.2` (Withdrawal Rate Limits): content edit
- `A.6.1.1.2.2.6.1.3.1.7.5.2.4` (Rate Limits): `and` → `/`
- `A.6.1.1.2.2.6.1.3.1.7.5.2.5` (Off-chain Operational Parameters): content edit
- `A.6.1.1.2.2.6.1.3.1.7.5.2` (Parameters): `Grove x Steakhouse AUSD` → `Sentora PYUSD`
- `A.6.1.1.2.2.6.1.3.1.7.5.3` (Instance-specific Operational Processes): content edit
- `A.6.1.1.2.2.6.1.3.1.7.5.4` (Instance-specific Operational Parameters): content edit
- `A.6.1.1.2.2.6.1.3.1.7.5` (Ethereum Mainnet - Sentora PYUSD Morpho Vault V2 Instance Configuration Document): `Grove x Steakhouse AUSD` → `Sentora PYUSD`
- `A.6.1.1.2.2.6.1.3.1.7.6.1` (RRC Framework Full Implementation Coverage): content edit
- `A.6.1.1.2.2.6.1.3.1.7.6.2.1.1` (Network): content edit
- `A.6.1.1.2.2.6.1.3.1.7.6.2.1.2` (Target Protocol): `PYUSD` → `RLUSD`
- `A.6.1.1.2.2.6.1.3.1.7.6.2.1.3` (Asset Supplied By Grove Liquidity Layer): `PYUSD` → `RLUSD`
- `A.6.1.1.2.2.6.1.3.1.7.6.2.1.4` (Token): `senPYUSDmain` → `senRLUSDv2`
- `A.6.1.1.2.2.6.1.3.1.7.6.2.1` (Instance Identifiers): content edit
- `A.6.1.1.2.2.6.1.3.1.7.6.2.2` (Contract Addresses): content edit
- `A.6.1.1.2.2.6.1.3.1.7.6.2.3` (Rate Limit IDs): content edit
- `A.6.1.1.2.2.6.1.3.1.7.6.2.4.1` (Deposit Rate Limits): `PYUSD` → `RLUSD`
- `A.6.1.1.2.2.6.1.3.1.7.6.2.4.2` (Withdrawal Rate Limits): content edit
- `A.6.1.1.2.2.6.1.3.1.7.6.2.4` (Rate Limits): content edit
- `A.6.1.1.2.2.6.1.3.1.7.6.2.5.1` (Maximum Exposure): content edit
- `A.6.1.1.2.2.6.1.3.1.7.6.2.5` (Off-chain Operational Parameters): content edit
- `A.6.1.1.2.2.6.1.3.1.7.6.2` (Parameters): `PYUSD` → `RLUSD`
- `A.6.1.1.2.2.6.1.3.1.7.6.3` (Instance-specific Operational Processes): content edit
- `A.6.1.1.2.2.6.1.3.1.7.6.4` (Instance-specific Operational Parameters): content edit
- `A.6.1.1.2.2.6.1.3.1.7.6` (Ethereum Mainnet - Sentora RLUSD Morpho Vault V2 Instance Configuration Document): `PYUSD` → `RLUSD`
- `A.6.1.1.2.2.6.1.3.1.7.7.1` (RRC Framework Full Implementation Coverage): content edit
- `A.6.1.1.2.2.6.1.3.1.7.7.2.1.1` (Network): content edit
- `A.6.1.1.2.2.6.1.3.1.7.7.2.1.2` (Target Protocol): `Sentora` → `Grove x Steakhouse`
- `A.6.1.1.2.2.6.1.3.1.7.7.2.1.3` (Asset Supplied By Grove Liquidity Layer): content edit
- `A.6.1.1.2.2.6.1.3.1.7.7.2.1.4` (Token): `senRLUSDv2` → `grove-bbqRLUSD`
- `A.6.1.1.2.2.6.1.3.1.7.7.2.1` (Instance Identifiers): content edit
- `A.6.1.1.2.2.6.1.3.1.7.7.2.2.2` (Underlying Asset Address): content edit
- `A.6.1.1.2.2.6.1.3.1.7.7.2.2` (Contract Addresses): content edit
- `A.6.1.1.2.2.6.1.3.1.7.7.2.3` (Rate Limit IDs): `’` → `'`
- `A.6.1.1.2.2.6.1.3.1.7.7.2.4.2` (Withdrawal Rate Limits): content edit
- `A.6.1.1.2.2.6.1.3.1.7.7.2.4` (Rate Limits): `’` → `'`
- `A.6.1.1.2.2.6.1.3.1.7.6.2.5.1` (Maximum Exposure): removed `###### A.6.1.1.2.2.6.1.3.1.7.7.2.5.1 - Maximum Exposure [Core]`
- `A.6.1.1.2.2.6.1.3.1.7.7.2.5` (Off-chain Operational Parameters): content edit
- `A.6.1.1.2.2.6.1.3.1.7.7.2` (Parameters): `Sentora` → `Grove x Steakhouse`
- `A.6.1.1.2.2.6.1.3.1.7.7.3` (Instance-specific Operational Processes): content edit
- `A.6.1.1.2.2.6.1.3.1.7.7.4` (Instance-specific Operational Parameters): content edit
- `A.6.1.1.2.2.6.1.3.1.7.7` (Ethereum Mainnet - Grove x Steakhouse RLUSD Morpho Vault V2 Instance Configuration Document): `Sentora` → `Grove x Steakhouse`
- `A.6.1.1.2.2.6.1.3.1.7.7.1` (RRC Framework Full Implementation Coverage): removed `###### A.6.1.1.2.2.6.1.3.1.7.8.1 - RRC Framework Full Implementation Coverage [Core]`
- `A.6.1.1.2.2.6.1.3.1.7.7.2.1.1` (Network): removed `###### A.6.1.1.2.2.6.1.3.1.7.8.2.1.1 - Network [Core]`
- `A.6.1.1.2.2.6.1.3.1.7.7.2.1.3` (Asset Supplied By Grove Liquidity Layer): removed `###### A.6.1.1.2.2.6.1.3.1.7.8.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]`
- `A.6.1.1.2.2.6.1.3.1.7.7.2.1.4` (Token): removed `###### A.6.1.1.2.2.6.1.3.1.7.8.2.1.4 - Token [Core]`
- `A.6.1.1.2.2.6.1.3.1.7.7.2.2.1` (Token Address): removed `###### A.6.1.1.2.2.6.1.3.1.7.8.2.2.1 - Token Address [Core]`
- `A.6.1.1.2.2.6.1.3.1.7.7.2.2.2` (Underlying Asset Address): removed `###### A.6.1.1.2.2.6.1.3.1.7.8.2.2.2 - Underlying Asset Address [Core]`
- `A.6.1.1.2.2.6.1.3.1.7.7.2.3.1` (Inflow RateLimitID): removed `###### A.6.1.1.2.2.6.1.3.1.7.8.2.3.1 - Inflow RateLimitID [Core]`
- `A.6.1.1.2.2.6.1.3.1.7.7.2.3.2` (Outflow RateLimitID): removed `###### A.6.1.1.2.2.6.1.3.1.7.8.2.3.2 - Outflow RateLimitID [Core]`
- `A.6.1.1.2.2.6.1.3.1.7.7.2.4.1` (Deposit Rate Limits): removed `###### A.6.1.1.2.2.6.1.3.1.7.8.2.4.1 - Deposit Rate Limits [Core]`
- `A.6.1.1.2.2.6.1.3.1.7.7.4.1` (Max Exchange Rate): removed `###### A.6.1.1.2.2.6.1.3.1.7.8.4.1 - Max Exchange Rate [Core]`
- `A.6.1.1.2.2.6.1.3.2.1.1.2.4.1` (Inflow Rate Limits): removed `(per day)`
- `A.6.1.1.2.2.6.1.3.2.1.2.2.4.1` (Inflow Rate Limits): `.` → `per day`
- `A.6.1.1.2.2.6.1.3.1.7.4.4` renumbered (UUID stable: `32ccb033…c5f5`)
- `A.6.1.1.2.2.6.1.3.7.1.1.2.1` renumbered (UUID stable: `fa3e9179…dfaa`)
- `A.6.1.1.2.2.6.1.3.7.1.1.2.2` renumbered (UUID stable: `e2ac9d21…0b65`)
- `A.6.1.1.2.2.6.1.3.7.1.1.2.4.2` renumbered (UUID stable: `63c0f9fd…ae90`)
- `A.6.1.1.2.2.6.1.3.7.1.1.2.5` renumbered (UUID stable: `5c7888fe…01da`)
- `A.6.1.1.2.2.6.1.3.7.1.1.3` renumbered (UUID stable: `fdc10843…8fda`)
- `ALM Proxy` → `Via` across 5 docs.
- `Cross-Chain Transfer Protocol Maximum` → `CCTP` across 5 docs.
- `max` → `Unlimited` across 1 doc.
- `High Yield` → `USDC Morpho` across 3 docs.
- `AUSD` → `v2` across 3 docs.
- `USDC` → `PYUSD` across 5 docs.
- `PYUSD` → `AUSD` across 6 docs.
- `Grove x Steakhouse AUSD` → `Sentora PYUSD` across 4 docs.
- `PYUSD` → `RLUSD` across 7 docs.
- `Sentora` → `Grove x Steakhouse` across 4 docs.
- `7.8` → `1` across 5 docs.

### Context
Deploys Grove's Liquidity Layer to Robinhood Chain — new ALM controller/proxy/rate-limit contracts, a Morpho groveUSDG instance (100M USDS exposure cap, CRR 3%→0.65%), and a Paxos USDG↔USDC conduit — and adds a Paxos USDC→USDG conduit on Ethereum Mainnet. Also adds `maxExchangeRate` deposit protections and renames/rebalances the Steakhouse and Sentora Morpho vault instances. Part of the 2026-07-06 weekly cycle (PR #273).

---

## PR #270 — Atlas Edit Proposal — 2026-06-29
**Merged:** 2026-07-03 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core A.6.1.1.2.2.6.1.3.1.9.2.2.5.1.1 deleted: Maximum Allocation** (UUID `911d3d77…4b51`)
- **Core A.6.1.1.2.2.6.1.3.1.9.2.2.5.1.2 deleted: Rate Limits** (UUID `202c9218…9666`)
- **Core A.6.1.1.2.2.6.1.3.1.9.2.2.5.1 deleted: Interim Deployment** (UUID `09aa5dea…d8a8`)

### Context
Removes Grove's interim deployment configuration (Maximum Allocation, Rate Limits), superseded by the permanent Diamond PAU contracts, roles, and rate-limit maximums added in PR #265.

---

## PR #265 — Atlas Edit Proposal — 2026-06-22
**Merged:** 2026-06-29 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core A.6.1.1.2.2.6.1.2.2.1.6.4 deleted: Tokenized Treasury Pauser Role** (UUID `abdc489a…3700`)
- **Core A.6.1.1.2.2.6.1.2.2.1.6.8 deleted: Tokenized Treasury Owner Timelock Canceller Role** (UUID `0ff6a176…c709`)
- **Core A.6.1.1.2.2.6.1.2.2.1.6.4 deleted: Tokenized Treasury Pauser Role** (UUID `abdc489a…3700`)
- **Core A.6.1.1.2.2.6.1.2.2.1.6.8 deleted: Tokenized Treasury Owner Timelock Canceller Role** (UUID `0ff6a176…c709`)
- **New: Ethereum Mainnet - Tokenized Treasury BUIDL Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.1.14.2`, UUID `8ebc6bfc…dfcc`): This Instance's associated Instance Configuration Document is located at `A.6.1.1.2.2.6.1.3.1.14.2`.
- **New: Diamond PAU Contracts** (`A.6.1.1.2.2.6.1.2.1.1.1.4`, UUID `887ff8b9…1416`): The documents herein define the addresses of the Diamond Parallelized Allocation Unit (Diamond PAU) contracts for the Grove Liquidity Layer.
  - **ALM Proxy Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.4.1.1`): The address of the ALM Proxy contract is: `0x0DcD9298e163dFD3c0B5b00F0d9093C36e40A153`.
  - **Controller Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.4.1.2`): The address of the Controller contract is: `0xbf83F5974B932c7D842254042717D6A2706CE5eE`.
  - **Beacon Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.4.1.3`): The address of the Beacon contract is: `0x829dC2b7E94B1954F0764E573f2E0d45Afa28199`.
  - **AccessControls Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.4.1.4`): The address of the AccessControls contract is: `0x4F6d1704700cd494DD4cd9bF59c0C39DA1Bc9164`.
  - **ALM Rate Limits Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.4.1.5`): The address of the ALM Rate Limits contract is: `0xE016Ae733A77Ba77E7907aAA749394Fc5e75C0e1`.
  - **Basin Facet Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.4.1.6`): The address of the Basin Facet contract is: `0xC84825BCD13AEddc372400239499380376a44A39`.
  - **USDS Facet Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.4.1.7`): The address of the USDS Facet contract is: `0x1221CC4B85Ab260660aD21C2829e0EB516dffBc7`.
  - **PSM Facet Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.4.1.8`): The address of the PSM Facet contract is: `0xE4A5dAc768a310cc2316f258901b32E499653064`.
  - **AdministeredAgent Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.4.1.9`): The address of the AdministeredAgent contract is: `0xdBD17832df0e57b1732cE1C84c652E820e549BAa`.
- **New: USDS Mint Maximum** (`A.6.1.1.2.2.6.1.2.1.1.3.1.1.1`, UUID `104541de…f57b`): The maximum amount of USDS that can be minted within the Grove Liquidity Layer (`LIMIT_USDS_MINT`) is specified in the document herein.
- **New: USDS Burn Maximum** (`A.6.1.1.2.2.6.1.2.1.1.3.1.1.2`, UUID `cf829503…82dd`): The maximum amount of USDS that can be burned within the Grove Liquidity Layer (`LIMIT_USDS_BURN`) is specified in the document herein.
- **New: USDS For USDC Swap Maximum** (`A.6.1.1.2.2.6.1.2.1.1.3.1.1.3`, UUID `a591104c…e163`): The maximum amount of USDS that can be swapped for USDC by the Grove Liquidity Layer in the Mainnet PSM (`LIMIT_USDS_TO_USDC`) is specified in the document herein.
- **New: USDC Avalanche ALM Proxy Maximum** (`A.6.1.1.2.2.6.1.2.1.1.3.1.2.1`, UUID `00b438d4…c978`): The maximum amount of USDC that can be sent to the Avalanche ALM Proxy (`LIMIT_USDC_TO_DOMAIN`, hashed with Avalanche domain) is specified in the document herein.
- **New: USDC Avalanche ALM Proxy Circle Cross-Chain Transfer Protocol Maximum** (`A.6.1.1.2.2.6.1.2.1.1.3.1.2.2`, UUID `d5b284c1…f36e`): The maximum amount of USDC that can be bridged to Avalanche ALM Proxy using the Circle Cross-Chain Transfer Protocol (`LIMIT_USDC_TO_CCTP_Avalanche`) is specified in the document herein.
- **New: USDC Ethereum Mainnet ALM Proxy Circle Cross-Chain Transfer Protocol Maximum** (`A.6.1.1.2.2.6.1.2.1.1.3.1.2.3`, UUID `a3b52620…090c`): The maximum amount of USDC that can be bridged to Ethereum Mainnet from the Avalanche ALM Proxy using the Circle Cross-Chain Transfer Protocol (`LIMIT_USDC_TO_CCTP_Ethereum`) is specified in the document herein.
- **New: USDS To Ethereum Mainnet Via SkyLink** (`A.6.1.1.2.2.6.1.2.1.1.3.1.2.4`, UUID `dec9ce16…de2c`): The maximum amount of USDS that can be sent to the Ethereum Mainnet ALM Controller from Avalanche via SkyLink (`LIMIT_LAYERZERO_TRANSFER`, hashed with Ethereum Mainnet USDS OFT address and Ethereum Mainnet destination domain) is specified i.
- **New: Whitelisting Of ALM Proxy** (`A.6.1.1.2.2.6.1.2.1.1.4.2`, UUID `6823cc5a…006e`): The ALM Proxy for the Grove Diamond PAU will be whitelisted on the litePSM in an upcoming spell.
- **New: Default Admin Role** (`A.6.1.1.2.2.6.1.2.2.1.1.1.1`, UUID `dc515367…782f`): The admin role (`DEFAULT_ADMIN_ROLE`) is the role that can grant and revoke any role, including itself and all other roles defined in the contract.
- **New: Relayer Role** (`A.6.1.1.2.2.6.1.2.2.1.1.1.2`, UUID `4639e60c…0edd`): The `RELAYER_ROLE` is the address for the Grove Liquidity Layer ALM Planner off-chain system that calls functions on `Controller` contracts to perform actions on behalf of the `ALMProxy` contract.
- **New: ALM Controller Role** (`A.6.1.1.2.2.6.1.2.2.1.1.1.3`, UUID `955c8db9…ca97`): The `ALM_CONTROLLER_ROLE` is the address of the role that can call the `call` functions on the `ALMProxy` contract and update `RateLimits` contract.
- **New: Default Admin Role** (`A.6.1.1.2.2.6.1.2.2.1.1.3.1`, UUID `987dc000…19fc`): The `DEFAULT_ADMIN_ROLE` is the administrative role of the AccessControls contract, authorized to grant and revoke all other roles of the Diamond PAU.
- **New: Controller Role** (`A.6.1.1.2.2.6.1.2.2.1.1.3.2`, UUID `1597253b…d2c5`): The `CONTROLLER` role is authorized to call the `call` functions on the ALM Proxy contract and to update the ALM Rate Limits contract.
- **New: Allocator Role** (`A.6.1.1.2.2.6.1.2.2.1.1.3.3`, UUID `6d6622aa…fc9b`): The `ALLOCATOR_ROLE` is authorized to call functions on the Controller contract to perform operations on behalf of the ALM Proxy contract.
- **New: Freezer Role** (`A.6.1.1.2.2.6.1.2.2.1.1.3.4`, UUID `d910ae36…d094`): The Freezer Role is authorized to remove a compromised or malicious relayer actor from the AdministeredAgent contract as a rapid-response measure, without recourse to the standard governance process.
- **New: Diamond PAU Controller Functions** (`A.6.1.1.2.2.6.1.2.2.1.2.2`, UUID `6c060c28…1641`): The documents herein define the functions performed through the Diamond PAU Controller contract for Grove Liquidity Layer operations on Ethereum Mainnet.
  - **Allocator Role** (`A.6.1.1.2.2.6.1.2.2.1.2.2.1.1`): Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a Basin deposit.
  - **Check Rate Limits** (`A.6.1.1.2.2.6.1.2.2.1.2.2.1.2`): The deposit is subject to the deposit rate limit identified by `LIMIT_BASIN_DEPOSIT` for the specified asset and Basin.
  - **Deposit Asset Into Basin** (`A.6.1.1.2.2.6.1.2.2.1.2.2.1.3`): The Basin Facet deposits the specified amount of the asset into the Basin on behalf of the ALM Proxy, and Basin shares are minted to the ALM Proxy.
  - **Allocator Role** (`A.6.1.1.2.2.6.1.2.2.1.2.2.2.1`): Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a Basin withdrawal.
  - **Check Rate Limits** (`A.6.1.1.2.2.6.1.2.2.1.2.2.2.2`): The withdrawal is subject to the withdrawal rate limit identified by `LIMIT_BASIN_WITHDRAW` for the specified asset and Basin.
  - **Withdraw Asset From Basin** (`A.6.1.1.2.2.6.1.2.2.1.2.2.2.3`): The Basin Facet withdraws up to the specified maximum amount of the asset from the Basin to the ALM Proxy, burning the corresponding Basin shares.
  - **Allocator Role** (`A.6.1.1.2.2.6.1.2.2.1.2.2.3.1`): Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a USDS mint.
  - **Check Rate Limits** (`A.6.1.1.2.2.6.1.2.2.1.2.2.3.2`): The mint is subject to the rate limit identified by `LIMIT_USDS_MINT`.
  - **Mint USDS To ALM Proxy** (`A.6.1.1.2.2.6.1.2.2.1.2.2.3.3`): The USDS Facet mints the specified amount of USDS from the Allocator Vault to the ALM Proxy.
  - **Allocator Role** (`A.6.1.1.2.2.6.1.2.2.1.2.2.4.1`): Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a USDS burn.
  - **Check Rate Limits** (`A.6.1.1.2.2.6.1.2.2.1.2.2.4.2`): The burn is subject to the rate limit identified by `LIMIT_USDS_BURN`.
  - **Burn USDS From ALM Proxy** (`A.6.1.1.2.2.6.1.2.2.1.2.2.4.3`): The USDS Facet burns the specified amount of USDS held by the ALM Proxy, returning it to the Allocator Vault.
  - **Allocator Role** (`A.6.1.1.2.2.6.1.2.2.1.2.2.5.1`): Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a USDS to USDC swap.
  - **Check Rate Limits** (`A.6.1.1.2.2.6.1.2.2.1.2.2.5.2`): The swap is subject to the rate limit identified by `LIMIT_USDS_TO_USDC`.
  - **Swap USDS For USDC Through The PSM** (`A.6.1.1.2.2.6.1.2.2.1.2.2.5.3`): The PSM Facet swaps USDS held by the ALM Proxy for the specified amount of USDC through the PSM.
  - **Allocator Role** (`A.6.1.1.2.2.6.1.2.2.1.2.2.6.1`): Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a USDC to USDS swap.
  - **Check Rate Limits** (`A.6.1.1.2.2.6.1.2.2.1.2.2.6.2`): The swap is subject to the rate limit identified by `LIMIT_USDC_TO_USDS`.
  - **Swap USDC For USDS Through The PSM** (`A.6.1.1.2.2.6.1.2.2.1.2.2.6.3`): The PSM Facet swaps the specified amount of USDC held by the ALM Proxy for USDS through the PSM.
- **New: Interim Deployment** (`A.6.1.1.2.2.6.1.3.1.14.1.2.5.1`, UUID `71230664…a04e`): This Instance is currently defined as an Interim Deployment (see `A.1.10.2.3.2.2.2`) and as such has CRR of 100%.
  - **Maximum Allocation** (`A.6.1.1.2.2.6.1.3.1.14.1.2.5.1.1`): The maximum allocation for the Tokenized Treasury Basin Interim Deployments is $5 million, combined across the JTRSY and BUIDL Instances.
  - **Rate Limits** (`A.6.1.1.2.2.6.1.3.1.14.1.2.5.1.2`): The Rate Limits for this Interim Deployment are defined in `A.6.1.1.2.2.6.1.3.1.14.1.2.4`.
- **New: Ethereum Mainnet - Tokenized Treasury BUIDL Instance Configuration Document** (`A.6.1.1.2.2.6.1.3.1.14.2`, UUID `867aa6c2…9463`): The documents herein contain the Instance Configuration Document for the Tokenized Treasury BUIDL Instance.
  - **RRC Framework Full Implementation Coverage** (`A.6.1.1.2.2.6.1.3.1.14.2.1`): `Pending`.
  - **Network** (`A.6.1.1.2.2.6.1.3.1.14.2.2.1.1`): Ethereum Mainnet.
  - **Target Protocol** (`A.6.1.1.2.2.6.1.3.1.14.2.2.1.2`): Securitize.
  - **Asset Supplied By Grove Liquidity Layer** (`A.6.1.1.2.2.6.1.3.1.14.2.2.1.3`): USDS.
  - **Token** (`A.6.1.1.2.2.6.1.3.1.14.2.2.1.4`): BUIDL.
  - **Token Address** (`A.6.1.1.2.2.6.1.3.1.14.2.2.2.1`): `0x7712c34205737192402172409a8F7ccef8aA2AEc`.
  - **Securitize Redemption Wallet Address** (`A.6.1.1.2.2.6.1.3.1.14.2.2.2.2`): `0x8780Dd016171B91E4Df47075dA0a947959C34200`.
  - **BUIDL Rate Provider Address** (`A.6.1.1.2.2.6.1.3.1.14.2.2.2.3`): `0x69a171853575FFD41574EA80Abfc6337AcbC4d43`.
  - **Pocket Contract Address** (`A.6.1.1.2.2.6.1.3.1.14.2.2.2.4`): `0x39548FeF138370Db06e172eF0739894b2a613DF9`.
  - **Token Redeemer Contract Address** (`A.6.1.1.2.2.6.1.3.1.14.2.2.2.5`): `0x73414528187A4986E2Af5D551fD14871b723E506`.
  - **Owner Timelock Contract Address** (`A.6.1.1.2.2.6.1.3.1.14.2.2.2.6`): `0xdB8C7c814E9780659B23478EF4Bda9032CC9Ff34`.
  - **Basin Contract Address** (`A.6.1.1.2.2.6.1.3.1.14.2.2.2.7`): `0xCBa428fB052B365557DAf52b744DFfF20d5FbEdD`.
  - **Rate Limit IDs** (`A.6.1.1.2.2.6.1.3.1.14.2.2.3`): The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Atlas.
  - **Rate Limits** (`A.6.1.1.2.2.6.1.3.1.14.2.2.4`): The inflow and outflow rate limit configuration for this conduit is specified in the subdocuments herein.
  - **Inflow Rate Limits** (`A.6.1.1.2.2.6.1.3.1.14.2.2.4.1`): The inflow rate limits are.
  - **Outflow Rate Limits** (`A.6.1.1.2.2.6.1.3.1.14.2.2.4.2`): The outflow rate limits are.
  - **Interim Deployment** (`A.6.1.1.2.2.6.1.3.1.14.2.2.5.1`): This Instance is currently defined as an Interim Deployment (see `A.1.10.2.3.2.2.2`) and as such has CRR of 100%.
  - **Maximum Allocation** (`A.6.1.1.2.2.6.1.3.1.14.2.2.5.1.1`): The maximum allocation for the Tokenized Treasury Basin Interim Deployments is $5 million, combined across the JTRSY and BUIDL Instances.
  - **Rate Limits** (`A.6.1.1.2.2.6.1.3.1.14.2.2.5.1.2`): The Rate Limits for this Interim Deployment are defined in `A.6.1.1.2.2.6.1.3.1.14.2.2.4`.
  - **Instance-specific Operational Processes** (`A.6.1.1.2.2.6.1.3.1.14.2.3`): The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.
  - **Instance Configuration Parameters** (`A.6.1.1.2.2.6.1.3.1.14.2.4.1`): The configuration parameters for this Instance are as follows.
  - **Owner Role Holder** (`A.6.1.1.2.2.6.1.3.1.14.2.4.2.1`): The `OWNER_ROLE`, as defined in `A.6.1.1.2.2.6.1.2.2.1.1.2.1`, is held by Securitize via an OpenZeppelin `TimelockController` at the address specified in [A.6.1.1.2.2.6.1.
  - **Proposer Role Holder** (`A.6.1.1.2.2.6.1.3.1.14.2.4.2.1.1`): The `PROPOSER_ROLE` of the Owner Timelock is held by Securitize at `0x453A28B31fdc31858C35B02bc3A42BCD8bfbAd3a`.
  - **Redeemer Role Holder** (`A.6.1.1.2.2.6.1.3.1.14.2.4.2.2`): The `REDEEMER_ROLE`, as defined in `A.6.1.1.2.2.6.1.2.2.1.1.2.5`, is held by Securitize at `0x488F27168a19472c51f003fbC5b75B1ACc3B7b4c`.
- **Basin Factory Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.3.1.1`): address `0x78Dc98D689Fe9A1b0056ac1cDFC14722bDA6D49a`
- **Tokenized Treasury USDS And USDC Rate Provider Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.3.1.2`): address `0x7928A185B8137D1CD2a0996a810A04dB2837419D`
- **USDS Burn Maximum** (`A.6.1.1.2.2.6.1.2.1.1.3.2.2`): `50` → `5`; `50` → `5`
- **USDC For USDS Swap Maximum** (`A.6.1.1.2.2.6.1.2.1.1.3.2.4`): `20` → `5`; `20` → `5`
- **JTRSY Rate Provider Address** (`A.6.1.1.2.2.6.1.3.1.14.1.2.2.3`): address `0x29209ceCFeFa6f675E6f1f829320D67cE2b025E5`
- **Pocket Contract Address** (`A.6.1.1.2.2.6.1.3.1.14.1.2.2.4`): address `0x2Cd296095788A2741e72056D66B3Ae1fAeE23ea2`
- **Token Redeemer Contract Address** (`A.6.1.1.2.2.6.1.3.1.14.1.2.2.5`): address `0x7c5Ce1a1D50a6cb3Da97C9e202B3E7CD8e5b5b6c`
- **Owner Timelock Contract Address** (`A.6.1.1.2.2.6.1.3.1.14.1.2.2.6`): address `0xA52dC9876aB4A9DB6dAfbb83410554086054d140`
- **Basin Contract Address** (`A.6.1.1.2.2.6.1.3.1.14.1.2.2.7`): address `0xf08943f817e1F902dEbC884c7B19Ea5764594Ac9`
- **Inflow Rate Limits** (`A.6.1.1.2.2.6.1.3.1.14.1.2.4.1`): `0` → `5,000,000`; `0` → `5,000,000`
- **Owner Role Holder** (`A.6.1.1.2.2.6.1.3.1.14.1.4.2.1`): `6` → `1.2`
- **Redeemer Role Holder** (`A.6.1.1.2.2.6.1.3.1.14.1.4.2.2`): address `0xb6e8D3E47c4FC5606E6C24D097Dd1791885Ce05a`

### Housekeeping
- `A.6.1.1.2.2.6.1.2.1.1.1.1.1.1` (Allocator Vaults And Buffers): removed refs to `A.6.1.1.2.2.6.1.3.1.14.1`
- `A.6.1.1.2.2.6.1.2.1.1.1.2` (Monolithic ALM Contracts): added `Monolithic`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.1` (Ethereum Mainnet): `USDS Mint Maximum` → `Ethereum Mainnet`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.2` (Avalanche): `USDS Burn Maximum` → `Avalanche`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.3` (Base): `USDS For USDC Swap Maximum` → `Base`
- `A.6.1.1.2.2.6.1.2.1.1.3.1` (Monolithic ALM Rate Limits): `Ethereum Mainnet` → `Monolithic ALM Rate Limits`
- `A.6.1.1.2.2.6.1.2.1.1.3.2.1` (USDS Mint Maximum): `USDC Avalanche ALM Proxy` → `USDS Mint`
- `A.6.1.1.2.2.6.1.2.1.1.3.2.3` (USDS For USDC Swap Maximum): `Ethereum Mainnet ALM Proxy Circle Cross-Chain Transfer Protocol` → `Swap`
- `A.6.1.1.2.2.6.1.2.1.1.3.2` (Diamond PAU Rate Limits): `Avalanche` → `Diamond PAU Rate Limits`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.3` (Base): removed `###### A.6.1.1.2.2.6.1.2.1.1.3.3 - Base [Core]`
- `A.6.1.1.2.2.6.1.2.1.1.3` (RateLimits): `Ratelimits` → `rate limits`
- `A.6.1.1.2.2.6.1.2.1.2.2.1` (Prime Primary Relayer Multisig): added `1.`
- `A.6.1.1.2.2.6.1.2.1.2.2.2` (Prime Secondary Relayer Multisig): added `1.`
- `A.6.1.1.2.2.6.1.2.1.2.2.3` (Core Operator Relayer Multisig): added `1.`
- `A.6.1.1.2.2.6.1.2.1.2.2.4` (Freezer Multisig): added refs to `A.6.1.1.2.2.6.1.2.2.1.1.3.4`
- `A.6.1.1.2.2.6.1.2.2.1.1.1` (Monolithic ALM Role Hierarchy And Permissions): `Default Admin` → `Monolithic ALM`
- `A.6.1.1.2.2.6.1.2.2.1.1.2` (Tokenized Treasury Role Hierarchy And Permissions): `Relayer` → `Tokenized Treasury`
- `A.6.1.1.2.2.6.1.2.2.1.1.3` (Diamond PAU Role Hierarchy And Permissions): `ALM Controller` → `Diamond PAU`
- `A.6.1.1.2.2.6.1.2.2.1.1` (Role Hierarchies And Permissions): `Hierarchy` → `Hierarchies`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1` (Swap USDS To USDC): `to` → `To`
- `A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2` (Swap USDC To USDS): `to` → `To`
- `A.6.1.1.2.2.6.1.2.2.1.2.1` (Monolithic Mainnet Controller Contract Functions): added `Monolithic`
- `A.6.1.1.2.2.6.1.2.2.1.2` (Controller Functions): `describe` → `specify`
- `A.6.1.1.2.2.6.1.2.2.1.3` (Rate Limit Management): `Spark` → `Grove`
- `A.6.1.1.2.2.6.1.2.2.1.1.2` (Tokenized Treasury Role Hierarchy And Permissions): removed `###### A.6.1.1.2.2.6.1.2.2.1.6 - Tokenized Treasury Role Hierarchy And Permissions [Core]`
- `A.6.1.1.2.2.6.1.2.2.3.3` (USDC to USDS Swap Action): `to` → `To`
- `A.6.1.1.2.2.6.1.3.1.14.1.2.1.2` (Target Protocol): `Tokenized Treasury` → `Centrifuge`
- `A.6.1.1.2.2.6.1.3.1.14.1.2.4.2` (Outflow Rate Limits): `0 USDS` → `Unlimited`
- `A.6.1.1.2.2.6.1.3.1.14.1.2.4` (Rate Limits): `current `maxAmount`` → `inflow`
- `A.6.1.1.2.2.6.1.2.1.1.3.1.1.4` renumbered (UUID stable: `8a462b2a…7d4f`)
- `A.6.1.1.2.2.6.1.2.1.1.3.1.1.5` renumbered (UUID stable: `b43ee2cd…c693`)
- `A.6.1.1.2.2.6.1.2.1.1.3.1.1.6` renumbered (UUID stable: `f6094634…09fb`)
- `A.6.1.1.2.2.6.1.2.1.1.3.1.3.1` renumbered (UUID stable: `dba2c846…af48`)
- `A.6.1.1.2.2.6.1.2.1.1.3.1.3.2` renumbered (UUID stable: `34e5a190…6e44`)
- `A.6.1.1.2.2.6.1.2.1.1.3.1.3.3` renumbered (UUID stable: `9575357d…93a6`)
- `A.6.1.1.2.2.6.1.2.2.1.1.1.4` renumbered (UUID stable: `37871a80…ca9f`)
- `A.6.1.1.2.2.6.1.2.2.1.1.2.1` renumbered (UUID stable: `41a7e6fb…b361`)
- `A.6.1.1.2.2.6.1.2.2.1.1.2.2` renumbered (UUID stable: `4554fa6d…323e`)
- `A.6.1.1.2.2.6.1.2.2.1.1.2.3` renumbered (UUID stable: `191435aa…be01`)
- `A.6.1.1.2.2.6.1.2.2.1.1.2.5` renumbered (UUID stable: `fbeb1921…25b1`)
- `A.6.1.1.2.2.6.1.2.2.1.1.2.6` renumbered (UUID stable: `493bc01d…8cf2`)
- `A.6.1.1.2.2.6.1.2.2.1.1.2.7` renumbered (UUID stable: `35e4cd97…c92e`)
- `USDC` → `USDS` across 3 docs.
- `6` → `1.2` across 8 docs.
- `to` → `To` across 3 docs.

### Context
Establishes the Grove Diamond PAU (Parallelized Allocation Unit) on Ethereum Mainnet — nine contract addresses, access-control roles, USDS mint/burn/swap and USDC bridging rate-limit maximums, and Basin/PSM controller functions — while deleting the Tokenized Treasury Pauser and Timelock Canceller roles. The ALM Proxy litePSM whitelisting is deferred to the July 2 executive. Ratified by poll #1638 (9-0).

---

## PR #258 — Atlas Edit Proposal — 2026-06-15
**Merged:** 2026-06-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core A.6.1.1.2.2.6.1.2.1.1.1.1.1.5 deleted: Allocator Vault (Bloom-A) Contract** (UUID `a2060039…12b3`)
- **Core A.6.1.1.2.2.6.1.2.1.1.1.1.1.5 deleted: Allocator Vault (Bloom-A) Contract** (UUID `a2060039…12b3`)
- **New: Monad** (`A.6.1.1.2.2.6.1.1.2.6`, UUID `6018029d…a8ee`): The documents herein contain a Directory of all Instances on Monad of the Allocation System Primitive with Instance status of `Active`.
  - **Uniswap** (`A.6.1.1.2.2.6.1.1.2.6.1`): The Monad Instances Directory of the Uniswap Protocol with `Active` Status are stored herein.
  - **Monad - Uniswap AUSD/USDC Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.6.1.1`): This Instance's associated Instance Configuration Document is located at `A.6.1.1.2.2.6.1.3.6.1.1`.
- **New: Allocator Buffer (BLOOM-A) Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.1.1.1.1`, UUID `599b6748…785f`): The address of the ALLOCATOR_BLOOM_A_BUFFER contract is: `0x629aD4D779F46B8A1491D3f76f7E97Cb04D8b1Cd`.
- **New: Allocator Buffer (GROVE-A) Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.1.1.1.3`, UUID `41b76952…f1ca`): The address of the ALLOCATOR_GROVE_A_BUFFER contract is: `0x436DABce608f73BeA2b75fba35bffe72739697d5`.
- **New: Allocator Vault (GROVE-A) Contract** (`A.6.1.1.2.2.6.1.2.1.1.1.1.1.1.4`, UUID `03b954d4…d17f`): The address of the ALLOCATOR_GROVE_A_VAULT contract is: `0xf739a30c74927dc6cFA3B67E4933872a1FC5F4EB`.
- **New: Pool Address** (`A.6.1.1.2.2.6.1.3.1.12.1.2.2.3`, UUID `75920dcb…f507`): `0xbAFeAd7c60Ea473758ED6c6021505E8BBd7e8E5d`.
- **New: Monad Instances** (`A.6.1.1.2.2.6.1.3.6`, UUID `27de13c9…1136`): The Monad Instances of the Grove Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.
  - **Uniswap** (`A.6.1.1.2.2.6.1.3.6.1`): The Monad Instances of the Uniswap Protocol with `Active` Status are stored herein.
  - **RRC Framework Full Implementation Coverage** (`A.6.1.1.2.2.6.1.3.6.1.1.1`): **`Pending`**.
  - **Network** (`A.6.1.1.2.2.6.1.3.6.1.1.2.1.1`): Monad.
  - **Target Protocol** (`A.6.1.1.2.2.6.1.3.6.1.1.2.1.2`): Uniswap AUSD/USDC.
  - **Asset Supplied By Grove Liquidity Layer** (`A.6.1.1.2.2.6.1.3.6.1.1.2.1.3`): USDC.
  - **Token** (`A.6.1.1.2.2.6.1.3.6.1.1.2.1.4`): Uniswap AUSD/USDC Pool.
  - **Pool Address** (`A.6.1.1.2.2.6.1.3.6.1.1.2.2.1`): `0x6B405DCA74897c9442d369DcF6c0EC230f7E1c7C`.
  - **Underlying Asset Address (USDC)** (`A.6.1.1.2.2.6.1.3.6.1.1.2.2.2`): `0x754704Bc059F8C67012fEd69BC8A327a5aafb603`.
  - **Broker Address (Ethereum Mainnet)** (`A.6.1.1.2.2.6.1.3.6.1.1.2.2.3`): `0xD94F9ef3395BBE41C1f05ced3C9a7dc520D08036`.
  - **Inflow RateLimitID** (`A.6.1.1.2.2.6.1.3.6.1.1.2.3.1`): The inflow RateLimitID is: `0x098ad67dc41c1a5892ec3ef5fd411198dc11962475e9ef2e0362e6cb7f5a2174`.
  - **Outflow RateLimitID** (`A.6.1.1.2.2.6.1.3.6.1.1.2.3.2`): The outflow RateLimitID is: N/A.
  - **Deposit Rate Limits (via FalconX)** (`A.6.1.1.2.2.6.1.3.6.1.1.2.4.1`): The deposit rate limits are.
  - **Withdrawal Rate Limits (via FalconX)** (`A.6.1.1.2.2.6.1.3.6.1.1.2.4.2`): The withdrawal rate limits are.
- **Ethereum Mainnet - Uniswap v3 AUSD/USDC Swaps Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.1.12.1`): `c4d60460` → `ffa0ca69`; `2694` → `c416`; `4d88` → `4163`; `bf96` → `a1c6`; `4f4141482cb5` → `b863f5d38c3f`
- **Ethereum Mainnet - Uniswap v3 AUSD/USDC LP Instance Configuration Document Location** (`A.6.1.1.2.2.6.1.1.2.1.12.2`): `ffa0ca69` → `cca4236a`; `c416` → `47f9`; `4163` → `4b4f`; `a1c6` → `81ef`; `b863f5d38c3f` → `c31a5ee624aa`
- **Allocator Vaults And Buffers** (`A.6.1.1.2.2.6.1.2.1.1.1.1.1.1`): `ALLOCATOR_BUFFER contract is: `0x629aD4D779F46B8A1491D3f76f7E97Cb04D8b1Cd`` → `Tokenized Treasury JTRSY Instance, as specified in [A.6.1.1.2.2.6.1.3.1.14.1 - Ethereum Mainnet - Tokenized Treasury JTRSY Instance Configuration Document](5e38198e-1577-4ab0-900a-91b6d8284387).`
- **Underlying Asset Address (USDC)** (`A.6.1.1.2.2.6.1.3.1.12.1.2.2.1`): address `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`
- **Underlying Asset Address (AUSD)** (`A.6.1.1.2.2.6.1.3.1.12.1.2.2.2`): address `0x00000000eFE302BEAA2b3e6e1b18d08D69a9012a`
- **Inflow RateLimitID (USDC)** (`A.6.1.1.2.2.6.1.3.1.12.2.2.3.1`): `0x6e850dcb18bea10055c82d1e3753f551b1228d04b81350ba117235de19f9a0da` → `0x71efb11b03476e40dcc1ade629d360114fcbf838d70a3211270f69414ba9a187`
- **Inflow RateLimitID (AUSD)** (`A.6.1.1.2.2.6.1.3.1.12.2.2.3.2`): `0x7dd93dac252469b97c259284118454a6a09efd0e5f781dec59acc240f8f88402` → `0x89c0cb8c17898781d7c1776eafcf73fd0b570659ad5c3791ddcbefe66b001541`

### Housekeeping
- `A.6.1.1.2.2.6.1.3.1.12.1.1` (RRC Framework Full Implementation Coverage): content edit
- `A.6.1.1.2.2.6.1.3.1.12.1.2.1.1` (Network): content edit
- `A.6.1.1.2.2.6.1.3.1.12.1.2.1.2` (Target Protocol): added `v3`
- `A.6.1.1.2.2.6.1.3.1.12.1.2.1.3` (Asset Supplied By Grove Liquidity Layer): added `and AUSD`
- `A.6.1.1.2.2.6.1.3.1.12.1.2.1.4` (Token): added `V3`
- `A.6.1.1.2.2.6.1.3.1.12.1.2.1` (Instance Identifiers): content edit
- `A.6.1.1.2.2.6.1.3.1.12.1.2.2` (Contract Addresses): content edit
- `A.6.1.1.2.2.6.1.3.1.12.1.2.3.1` (Inflow RateLimitID (USDC)): removed `The inflow RateLimitID is:`
- `A.6.1.1.2.2.6.1.3.1.12.1.2.3.2` (Outflow RateLimitID (AUSD)): `N/A` → ``0x7dd93dac252469b97c259284118454a6a09efd0e5f781dec59acc240f8f88402`.`
- `A.6.1.1.2.2.6.1.3.1.12.1.2.3` (Rate Limit IDs): content edit
- `A.6.1.1.2.2.6.1.3.1.12.1.2.4.1` (Deposit Rate Limits): `50,000,000 USDC` → `N/A - swaps only`
- `A.6.1.1.2.2.6.1.3.1.12.1.2.4.2` (Withdrawal Rate Limits): removed `- `slope`: N/A`
- `A.6.1.1.2.2.6.1.3.1.12.1.2.4` (Rate Limits): content edit
- `A.6.1.1.2.2.6.1.3.1.12.1.2.5` (Off-chain Operational Parameters): content edit
- `A.6.1.1.2.2.6.1.3.1.12.1.2` (Parameters): `Monad Uniswap` → `Uniswap v3`
- `A.6.1.1.2.2.6.1.3.1.12.1.3` (Instance-specific Operational Processes): content edit
- `A.6.1.1.2.2.6.1.3.1.12.1` (Ethereum Mainnet - Uniswap v3 AUSD/USDC Swaps Instance Configuration Document): `Monad Uniswap` → `Uniswap v3`
- `A.6.1.1.2.2.6.1.3.1.12.2.1` (RRC Framework Full Implementation Coverage): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.2.1.1` (Network): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.2.1.2` (Target Protocol): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.2.1.3` (Asset Supplied By Grove Liquidity Layer): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.2.1.4` (Token): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.2.1` (Instance Identifiers): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.2.2.1` (Underlying Asset Address (USDC)): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.2.2.2` (Underlying Asset Address (AUSD)): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.2.2.3` (Pool Address): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.2.2` (Contract Addresses): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.2.3` (Rate Limit IDs): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.2.4.1` (Deposit Rate Limits): `N` → `25,000,000 AUSD`
- `A.6.1.1.2.2.6.1.3.1.12.2.2.4.2` (Withdrawal Rate Limits): `N/A - swaps only` → `Unlimited`
- `A.6.1.1.2.2.6.1.3.1.12.2.2.4` (Rate Limits): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.2.5` (Off-chain Operational Parameters): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.2` (Parameters): `Swaps` → `LP`
- `A.6.1.1.2.2.6.1.3.1.12.2.3` (Instance-specific Operational Processes): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.4.1` (Parameters For Stable Stable Pools): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2.4` (Instance-specific Operational Parameters): content edit
- `A.6.1.1.2.2.6.1.3.1.12.2` (Ethereum Mainnet - Uniswap v3 AUSD/USDC LP Instance Configuration Document): `Swaps` → `LP`
- `A.6.1.1.2.2.6.1.3.1.12.2.1` (RRC Framework Full Implementation Coverage): removed `###### A.6.1.1.2.2.6.1.3.1.12.3.1 - RRC Framework Full Implementation Coverage [Core]`
- `A.6.1.1.2.2.6.1.3.1.12.2.2.1.1` (Network): removed `###### A.6.1.1.2.2.6.1.3.1.12.3.2.1.1 - Network [Core]`
- `A.6.1.1.2.2.6.1.3.1.12.2.2.1.2` (Target Protocol): removed `###### A.6.1.1.2.2.6.1.3.1.12.3.2.1.2 - Target Protocol [Core]`
- `A.6.1.1.2.2.6.1.3.1.12.2.2.1.3` (Asset Supplied By Grove Liquidity Layer): removed `###### A.6.1.1.2.2.6.1.3.1.12.3.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]`
- `A.6.1.1.2.2.6.1.3.1.12.2.2.1.4` (Token): removed `###### A.6.1.1.2.2.6.1.3.1.12.3.2.1.4 - Token [Core]`
- `A.6.1.1.2.2.6.1.3.1.12.2.2.2.1` (Underlying Asset Address (USDC)): removed `###### A.6.1.1.2.2.6.1.3.1.12.3.2.2.1 - Underlying Asset Address (USDC) [Core]`
- `A.6.1.1.2.2.6.1.3.1.12.2.2.2.2` (Underlying Asset Address (AUSD)): removed `###### A.6.1.1.2.2.6.1.3.1.12.3.2.2.2 - Underlying Asset Address (AUSD) [Core]`
- `A.6.1.1.2.2.6.1.3.1.12.2.2.2.3` (Pool Address): removed `###### A.6.1.1.2.2.6.1.3.1.12.3.2.2.3 - Pool Address [Core]`
- `A.6.1.1.2.2.6.1.3.1.12.2.2.3.1` (Inflow RateLimitID (USDC)): removed `###### A.6.1.1.2.2.6.1.3.1.12.3.2.3.1 - Inflow RateLimitID (USDC) [Core]`
- `A.6.1.1.2.2.6.1.3.1.12.2.2.3.2` (Inflow RateLimitID (AUSD)): removed `###### A.6.1.1.2.2.6.1.3.1.12.3.2.3.2 - Inflow RateLimitID (AUSD) [Core]`
- `A.6.1.1.2.2.6.1.3.1.12.2.2.4.1` (Deposit Rate Limits): removed `###### A.6.1.1.2.2.6.1.3.1.12.3.2.4.1 - Deposit Rate Limits [Core]`
- `A.6.1.1.2.2.6.1.3.1.12.2.2.4.2` (Withdrawal Rate Limits): removed `###### A.6.1.1.2.2.6.1.3.1.12.3.2.4.2 - Withdrawal Rate Limits [Core]`
- `A.6.1.1.2.2.6.1.3.1.12.1.2.4.3` renumbered (UUID stable: `e21c0b53…7efb`)
- `A.6.1.1.2.2.6.1.3.1.12.1.4.1` renumbered (UUID stable: `dab70e48…336e`)
- `A.6.1.1.2.2.6.1.3.1.12.1.4` renumbered (UUID stable: `960ce9e1…3552`)
- `A.6.1.1.2.2.6.1.3.1.12.2.2.3.3` renumbered (UUID stable: `3377cf40…b20e`)
- `A.6.1.1.2.2.6.1.3.1.12.2.2.3.4` renumbered (UUID stable: `7e8b0d83…115b`)
- `A.6.1.1.2.2.6.1.3.6.1.1.2.1` renumbered (UUID stable: `09991d1f…9136`)
- `A.6.1.1.2.2.6.1.3.6.1.1.2.2` renumbered (UUID stable: `22326048…212c`)
- `A.6.1.1.2.2.6.1.3.6.1.1.2.3` renumbered (UUID stable: `2e3e8ebe…42ab`)
- `A.6.1.1.2.2.6.1.3.6.1.1.2.4` renumbered (UUID stable: `d7fdb0e6…a655`)
- `A.6.1.1.2.2.6.1.3.6.1.1.2.5` renumbered (UUID stable: `ad810569…27f4`)
- `A.6.1.1.2.2.6.1.3.6.1.1.3` renumbered (UUID stable: `53743f66…b8e4`)
- `Monad Uniswap` → `Uniswap v3` across 3 docs.
- `Swaps` → `LP` across 3 docs.
- `12.3` → `1` across 6 docs.

### Context
Expands the Grove Liquidity Layer: adds a Monad instances directory (Uniswap AUSD/USDC) and registers ALLOCATOR-GROVE-A / ALLOCATOR-BLOOM-A buffer and vault contracts, while the Ethereum AUSD/USDC instance is reworked into separate Uniswap v3 Swaps and LP configs (the old Bloom-A vault contract doc is deleted). Ratified by poll #1637 (10-0).

---

## PR #255 — Atlas Edit Proposal — 2026-06-08
**Merged:** 2026-06-11 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: USD Stablecoin To USDS Swap Authorization** (`A.6.1.1.2.2.6.1.2.1.2.3`, UUID `aa16daa3…0144`): Grove is authorized to swap USD stablecoins held in the Grove SubProxy Account, as specified in `A.6.1.1.2.2.1.1.3.1.1.2`, to USDS.

### Context
Grants Grove standing authorization to convert USD stablecoins held in its SubProxy Account into USDS. Ratified by poll #1636 (9-0).

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
