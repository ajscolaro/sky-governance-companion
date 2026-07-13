# Support Scope — Change History

Atlas path: `A.2` — The Support Scope

---

## PR #273 — Atlas Edit Proposal — 2026-07-06
**Merged:** 2026-07-10 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core A.2.2.9.1.2.1.2.1.1 deleted: Approval Process** (UUID `3f3162cc…4261`)
- **Core A.2.2.9.1.2.1.2.1.2 deleted: Specification In The Instance Configuration Document** (UUID `ce66fc65…032e`)
- **Core A.2.2.9.1.2.1.2.1.3 deleted: Limitations** (UUID `f2b3688f…abab`)
- **Core A.2.2.9.1.2.1.2.1 deleted: Boosted Distribution Reward Rate** (UUID `1d9219cb…4c63`)
- **New: Liquidity Layer Role Definitions** (`A.2.2.10.1.1.1.3`, UUID `2ae4b91a…6550`): The documents herein define the access-control roles of the Diamond Parallelized Allocation Unit (Diamond PAU) implementation of the Allocation System.
  - **Default Admin Role** (`A.2.2.10.1.1.1.3.1`): The Default Admin Role (`DEFAULT_ADMIN_ROLE`) is the administrative role of an Instance's access-control contract, authorized to grant and revoke all other roles.
  - **Controller Role** (`A.2.2.10.1.1.1.3.2`): The Controller Role (`CONTROLLER`) is authorized to call the asset-movement functions on the ALM Proxy and to update the Rate Limits contract.
  - **Allocator Role** (`A.2.2.10.1.1.1.3.3`): The Allocator Role (`ALLOCATOR_ROLE`) is authorized to initiate allocation operations on behalf of the ALM Proxy, through the Controller.
  - **Actor** (`A.2.2.10.1.1.1.3.4`): An Actor is an address registered on the AdministeredAgent that is authorized to submit allocation operations to the Controller through the Allocator Role, as specified in [A.2.2.10.1.1.1.3.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f2.
  - **Revoker** (`A.2.2.10.1.1.1.3.5`): A Revoker is an address registered on the AdministeredAgent that is authorized to remove an Actor as a rapid-response measure, without affecting the Allocator Role held by the AdministeredAgent.
  - **Grantor** (`A.2.2.10.1.1.1.3.6`): A Grantor is an address registered on the AdministeredAgent that is authorized to add an Actor, as specified in `A.2.2.10.1.1.1.3.4`, granting it the ability to submit operations through the Adm.
  - **Administered Agent Admin** (`A.2.2.10.1.1.1.3.7`): The Administered Agent Admin is an address registered on the AdministeredAgent with authority over its role configuration, able to add and remove the AdministeredAgent's Admins, Grantors, Actors, and Revokers.
- **New: Liquidity Layer Shared Contracts** (`A.2.2.10.1.1.1.4`, UUID `a2677d19…aab5`): The documents herein define the shared contracts of the Diamond PAU implementation of the Allocation System.
  - **Beacon** (`A.2.2.10.1.1.1.4.1`): The Beacon (`Beacon`) is the registry that whitelists the Facets approved for use by Diamond PAU Instances; an Instance may only delegate calls to Facets registered on the Beacon.
  - **Aave Facet** (`A.2.2.10.1.1.1.4.2.1`): The Aave Facet (`AaveFacet`) supplies and withdraws an underlying asset to and from an Aave v3 lending pool, or an Aave v3 fork such as SparkLend, holding the aTokens in the ALM Proxy.
  - **Farm Facet** (`A.2.2.10.1.1.1.4.2.10`): The Farm Facet (`FarmFacet`) stakes and withdraws a token in a Synthetix-style reward farm and claims accrued rewards.
  - **LayerZero Facet** (`A.2.2.10.1.1.1.4.2.11`): The LayerZero Facet (`LayerZeroFacet`) bridges tokens implementing the Omnichain Fungible Token (OFT) standard cross-chain via LayerZero v2 to a preconfigured recipient.
  - **Maple Facet** (`A.2.2.10.1.1.1.4.2.12`): The Maple Facet (`MapleFacet`) requests and cancels redemptions of Maple pool tokens.
  - **Merkl Facet** (`A.2.2.10.1.1.1.4.2.13`): The Merkl Facet (`MerklFacet`) toggles operator authorization on a Merkl distributor, delegating reward claiming to an operator.
  - **OTC Facet** (`A.2.2.10.1.1.1.4.2.14`): The OTC Facet (`OTCFacet`) executes over-the-counter swaps, sending an asset to an exchange and later claiming the counter-asset from a designated buffer, under recharge-rate and slippage checks.
  - **Pendle Facet** (`A.2.2.10.1.1.1.4.2.15`): The Pendle Facet (`PendleFacet`) redeems Pendle principal and yield tokens (PT and YT) for their underlying token after market expiry via the Pendle router.
  - **PSM Facet** (`A.2.2.10.1.1.1.4.2.16`): The PSM Facet (`PSMFacet`) swaps between USDS and USDC by routing through DAI and the Lite PSM's no-fee path.
  - **Spark Vault Facet** (`A.2.2.10.1.1.1.4.2.17`): The Spark Vault Facet (`SparkVaultFacet`) pulls assets from a Spark vault via its `take` function.
  - **Superstate Facet** (`A.2.2.10.1.1.1.4.2.18`): The Superstate Facet (`SuperstateFacet`) subscribes USDC into Superstate USTB, minting USTB.
  - **Transfer Asset Facet** (`A.2.2.10.1.1.1.4.2.19`): The Transfer Asset Facet (`TransferAssetFacet`) transfers an ERC-20 asset from the ALM Proxy to a rate-limit-authorized destination address.
  - **Basin Facet** (`A.2.2.10.1.1.1.4.2.2`): The Basin Facet (`BasinFacet`) deposits assets into and withdraws them from a Basin contract in exchange for Basin shares.
  - **Uniswap v3 Facet** (`A.2.2.10.1.1.1.4.2.20`): The Uniswap v3 Facet (`UniswapV3Facet`) executes Uniswap v3 exact-input swaps and adds or removes concentrated-liquidity positions, under tick-bound, time-weighted-average-price, and slippage guards.
  - **Uniswap v4 Facet** (`A.2.2.10.1.1.1.4.2.21`): The Uniswap v4 Facet (`UniswapV4Facet`) mints, increases, and decreases Uniswap v4 liquidity positions and executes token swaps, under tick-limit and slippage guards.
  - **USDS Facet** (`A.2.2.10.1.1.1.4.2.22`): The USDS Facet (`USDSFacet`) mints and burns USDS against an allocator vault, drawing USDS into and wiping it from the vault buffer.
  - **weETH Facet** (`A.2.2.10.1.1.1.4.2.23`): The weETH Facet (`WEETHFacet`) stakes ETH (from WETH) into ether.fi eETH and wraps it to weETH, and handles the unwrap, withdrawal-request, and claim flow back to WETH.
  - **Wrap Proxy ETH Facet** (`A.2.2.10.1.1.1.4.2.24`): The Wrap Proxy ETH Facet (`WrapProxyETHFacet`) wraps the ALM Proxy's entire native ETH balance into WETH.
  - **wstETH Facet** (`A.2.2.10.1.1.1.4.2.25`): The wstETH Facet (`WSTETHFacet`) converts WETH to ETH to wstETH (Lido) and handles the Lido withdrawal-queue request and claim flow back to WETH.
  - **CCTP Facet** (`A.2.2.10.1.1.1.4.2.3`): The CCTP Facet (`CCTPFacet`) bridges USDC cross-chain through Circle's Cross-Chain Transfer Protocol (CCTP), burning on the source domain to a preconfigured mint recipient.
  - **Centrifuge Facet** (`A.2.2.10.1.1.1.4.2.4`): The Centrifuge Facet (`CentrifugeFacet`) manages Centrifuge v3 async vault positions, cancelling and claiming pending deposit and redeem requests and initiating cross-chain share transfers.
  - **Curve Facet** (`A.2.2.10.1.1.1.4.2.5`): The Curve Facet (`CurveFacet`) swaps between assets in a Curve pool and adds or removes pool liquidity, under a max-slippage guard.
  - **DAI-USDS Facet** (`A.2.2.10.1.1.1.4.2.6`): The DAI-USDS Facet (`DAIUSDSFacet`) converts between DAI and USDS at 1:1 through the DAI-USDS converter.
  - **ERC-4626 Facet** (`A.2.2.10.1.1.1.4.2.7`): The ERC-4626 Facet (`ERC4626Facet`) deposits, withdraws, and redeems against any ERC-4626 vault, under min-shares, min-assets, and max-exchange-rate guards.
  - **ERC-7540 Facet** (`A.2.2.10.1.1.1.4.2.8`): The ERC-7540 Facet (`ERC7540Facet`) runs the asynchronous ERC-7540 vault flow, requesting and claiming deposits and redemptions.
  - **Ethena Facet** (`A.2.2.10.1.1.1.4.2.9`): The Ethena Facet (`EthenaFacet`) drives the Ethena USDe mint and burn and sUSDe staking lifecycle, managing the delegated signer, mint and burn approvals, and sUSDe cooldown and unstake.
  - **PAU Factory** (`A.2.2.10.1.1.1.4.3`): The PAU Factory (`PAUFactory`) is the contract that deploys new Diamond PAU Instances.
  - **PAU Assembler** (`A.2.2.10.1.1.1.4.4`): The PAU Assembler (`DefaultPAUAssembler`) is the contract that assembles a Diamond PAU Instance from its Beacon-approved Facets at deployment.
  - **Administered Agent Factory** (`A.2.2.10.1.1.1.4.5`): The Administered Agent Factory (`AdministeredAgentFactory`) is the contract that deploys the `AdministeredAgent` contracts that hold the Allocator Role on the Controller of a Diamond PAU Instance, with the Prime Agent's Relayer system regis.
- **New: Liquidity Layer Operational Processes** (`A.2.2.10.1.1.1.5`, UUID `3b387169…ea2c`): The documents herein define the operational processes of the Diamond PAU implementation of the Allocation System — including the addition and removal of Facets approved on the Beacon, the functions performed through the Controller, and the.
  - **Adding a Facet** (`A.2.2.10.1.1.1.5.1.1`): The process for adding a Facet will be specified in a future iteration of the Atlas.
  - **Removing a Facet** (`A.2.2.10.1.1.1.5.1.2`): The process for removing a Facet will be specified in a future iteration of the Atlas.
  - **Allocator Role** (`A.2.2.10.1.1.1.5.2.1.1`): Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a USDS mint.
  - **Check Rate Limits** (`A.2.2.10.1.1.1.5.2.1.2`): The mint is subject to the rate limit identified by `LIMIT_USDS_MINT`.
  - **Mint USDS To ALM Proxy** (`A.2.2.10.1.1.1.5.2.1.3`): The USDS Facet mints the specified amount of USDS from the allocator vault to the ALM Proxy.
  - **Allocator Role** (`A.2.2.10.1.1.1.5.2.2.1`): Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate a USDS burn.
  - **Check Rate Limits** (`A.2.2.10.1.1.1.5.2.2.2`): The burn is subject to the rate limit identified by `LIMIT_USDS_BURN`.
  - **Burn USDS From ALM Proxy** (`A.2.2.10.1.1.1.5.2.2.3`): The USDS Facet burns the specified amount of USDS held by the ALM Proxy, returning it to the allocator vault.
  - **Allocator Role** (`A.2.2.10.1.1.1.5.2.3.1`): Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate an Aave market deposit.
  - **Check Rate Limits** (`A.2.2.10.1.1.1.5.2.3.2`): The deposit is subject to the deposit rate limit identified by `LIMIT_AAVE_DEPOSIT` for the asset and market.
  - **Deposit Asset Into Aave Market** (`A.2.2.10.1.1.1.5.2.3.3`): The Aave Facet supplies the specified amount of the asset to the Aave v3 market on behalf of the ALM Proxy, and aTokens are minted to the ALM Proxy.
  - **Allocator Role** (`A.2.2.10.1.1.1.5.2.4.1`): Only an address holding the Allocator Role (`ALLOCATOR_ROLE`) may initiate an Aave market withdrawal.
  - **Check Rate Limits** (`A.2.2.10.1.1.1.5.2.4.2`): The withdrawal is subject to the withdrawal rate limit identified by `LIMIT_AAVE_WITHDRAW` for the asset and market.
  - **Withdraw Asset From Aave Market** (`A.2.2.10.1.1.1.5.2.4.3`): The Aave Facet withdraws the specified amount of the asset from the Aave v3 market to the ALM Proxy, burning the corresponding aTokens.
  - **RateLimits Query** (`A.2.2.10.1.1.1.5.3.1`): The following code implements the public view functions that query the current `RateLimits` for a specific key.
  - **Set RateLimit** (`A.2.2.10.1.1.1.5.3.2`): The following code sets the `RateLimit` for a specific key, restricted to the `DEFAULT_ADMIN_ROLE` holder (Sky Governance acting through the Prime Agent's SubProxy).
  - **Set Unlimited RateLimit** (`A.2.2.10.1.1.1.5.3.3`): The following code sets an unlimited `RateLimit` for a specific key, restricted to the `DEFAULT_ADMIN_ROLE` holder (Sky Governance acting through the Prime Agent's SubProxy).
  - **Set Trigger For RateLimit Decrease** (`A.2.2.10.1.1.1.5.3.4`): The following code decreases the `RateLimit` for a specific key, restricted to the `CONTROLLER` role (the Controller contract), called as allocations consume the limit.
  - **Set Trigger For RateLimit Increase** (`A.2.2.10.1.1.1.5.3.5`): The following code increases the `RateLimit` for a specific key, restricted to the `CONTROLLER` role (the Controller contract), called as allocations return the limit.
- **New: Agent SubProxy Account** (`A.2.2.5.1.2.5`, UUID `585dc747…9258`): The Agent Creation Primitive must specify the SubProxy address of the Agent.
- **New: Agent Genesis Account** (`A.2.2.5.1.2.6`, UUID `761966db…7d26`): The Agent Creation Primitive must designate the Genesis Account.
- **New: Maple syrupUSDC Transfer** (`A.2.8.2.1.2.10`, UUID `da2c6b16…0429`): Grove will transfer the syrupUSDC it currently holds to Spark, and Spark will transfer the equivalent value in USDS to the Grove ALM Proxy.

### Housekeeping
- `A.2.2.10.1.1.1.2` (Liquidity Layer Parameter Definitions): removed `based on the Spark Liquidity Layer, including the Grove Liquidity Layer`
- `A.2.2.5.1.2.3` (Agent Foundation): `SubProxy Account` → `Foundation`
- `A.2.2.5.1.2.4` (Agent Development Company): `Genesis Account` → `Development Company`
- `A.2.2.9.1.2.1.2` (Distribution Reward Rate): removed `standard`
- `A.2.3.1.2.2.1` (Fortification Foundation Allocation): removed `, and protocol development and growth`

### Context
Introduces the shared Diamond PAU (Parallelized Allocation Unit) framework — generic Liquidity Layer role definitions (Controller, Allocator, Actor, Revoker, Grantor), the full shared-Facet registry (Aave, Curve, CCTP, Ethena, Uniswap v3/v4, PSM, etc.), and the Beacon/Factory/Assembler contracts and operational processes — the substrate that Osero's new SLL deployment (this same edit) and future agents build on. Also adds the Maple syrupUSDC Grove→Spark transfer and Agent Creation SubProxy/Genesis inputs; the Boosted Distribution Reward Rate subtree is deleted.

---

## PR #270 — Atlas Edit Proposal — 2026-06-29
**Merged:** 2026-07-03 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: Chronicle Point Reward Instance Definition** (`A.2.8.2.10.2.1.1`, UUID `a7ccb2d1…0396`): The "Chronicle Point Reward Instance" refers to the Ethereum mainnet reward mechanism through which USDS is deposited in Sky's Rewards contract to accrue Chronicle Points.
- **New: Compensation Formula** (`A.2.8.2.10.2.1.2`, UUID `d4a5ce00…1b01`): Sky will pay Grove ongoing compensation in USDS, calculated as follows.

### Housekeeping
- `A.2.8.2.10.2.1` (Chronicle Point Reward Program): `Instance Definition` → `Program`
- `A.2.8.2.10.2.2` (Prime Revenue Credit): removed refs to `A.3.1.2.1`; added refs to `A.3.2.1.2.1`
- `A.2.8.2.2.2.1.2.2.1` (Grove Token Reward Distribution Schedule): removed `The distribution of GROVE tokens will be specified in a future iteration of the Atlas.`
- `A.2.8.2.10.2.1.3` renumbered (UUID stable: `4bed0292…ead5`)
- `A.2.8.2.10.2.1.4` renumbered (UUID stable: `31e070cf…7cc7`)
- `A.2.8.2.10.2.1.5` renumbered (UUID stable: `e19ba00b…83f8`)

### Context
Defines the Chronicle Point Reward Instance (USDS deposited in Sky's Rewards contract to accrue Chronicle Points) and the USDS compensation formula Sky pays Grove, and finalizes the previously-deferred Grove token distribution schedule (`A.2.8.2.2.2.1.2.2.1`) now referenced by the new A.4 GROVE Token Rewards.

---

## PR #265 — Atlas Edit Proposal — 2026-06-22
**Merged:** 2026-06-29 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: Reward Code Ranges** (`A.2.2.9.1.2.1.1.4`, UUID `af47ab9b…95c2`): The following Prime Agents are allocated reserved ranges of Reward Codes for use in their Distribution Reward Primitive instances.
- **New: Allocation Modification** (`A.2.3.1.5`, UUID `c4ef7fd6…3390`): In the short term, the Core Council may reduce the allocations of Step 1 Capital (see `A.2.3.1.2.2`) and Step 2 Capital (see [A.2.3.1.2.3 - Step 2: Aggregate Backstop.
- **New: Grove Foundation Grant Authorization: July 2026** (`A.2.8.2.2.2.4.5.2.2`, UUID `7b6820d0…ec74`): The founding team of Grove has proposed a cash grant of 800,000 USDS to the Grove Foundation from Grove's Prime Treasury for July 2026. (address: `0xE3EC4CC359E68c9dCE15Bf667b1aD37Df54a5a42`)
- **New: Transfers To The Sky Frontier Foundation** (`A.2.8.2.5.2.4`, UUID `e93eb85c…de8f`): Core Council Executor Agent 1 is authorized to transfer funds from its Genesis Capital Allocation to the Sky Frontier Foundation without a separate governance decision for each transfer.
- **New: Subsequent Allocation Mechanism** (`A.2.8.2.7.2.2.3`, UUID `45830abe…16a9`): Following its Genesis Capital Allocation, Skybase may request additional grants to the Skybase Foundation to fund operations and growth.
  - **Skybase Foundation Grant Authorization: July 2026** (`A.2.8.2.7.2.2.3.1`): The founding team of Skybase has proposed a one-time cash grant of 700,000 USDS to the Skybase Foundation from Skybase's SubProxy to provide operational capital.
- **New: Transfers To The Sky Frontier Foundation** (`A.2.8.2.8.2.2`, UUID `06bac1e1…ddee`): Amatsu is authorized to transfer funds from its Genesis Capital Allocation to the Sky Frontier Foundation without a separate governance decision for each transfer.
- **New: Transfers To The Sky Frontier Foundation** (`A.2.8.2.9.2.2`, UUID `9bb85c21…871d`): Ozone is authorized to transfer funds from its Genesis Capital Allocation to the Sky Frontier Foundation without a separate governance decision for each transfer.
- **Core Council Executor Agent 1 SubProxy Address** (`A.2.8.2.5.2.2.1`): address `0x64a2b7CfA832fE83BE6a7C1a67521B350519B9c1`
- **Amatsu SubProxy Address** (`A.2.8.2.8.2.1.1`): address `0xF33B14329e7115dD0B40DBb2985E1A0Df10E3fAa`
- **Ozone SubProxy Address** (`A.2.8.2.9.2.1.1`): address `0x9FE628BFc33f0352Bb1f93168881a9Ef93C8d2CF`

### Housekeeping
- `A.2.8.2.3.1.1.2` (Keel Details): `Elodin` → `Development Company`
- `will be specified in` → `on` across 3 docs.

### Context
Authorizes July 2026 foundation grants (Grove 800,000 USDS from Prime Treasury; Skybase 700,000 USDS from its SubProxy), empowers Executor Agent 1, Amatsu, and Ozone to transfer Genesis Capital to the Sky Frontier Foundation without per-transfer governance, and permits the Core Council to reduce Step 1/Step 2 Capital allocations short-term. Ratified by poll #1638 (9-0).

---

## PR #258 — Atlas Edit Proposal — 2026-06-15
**Merged:** 2026-06-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: Spark Foundation Grant Authorization: Q3 2026** (`A.2.8.2.2.2.4.5.1.4`, UUID `8dd2eb27…5d7c`): The founding team of Spark has proposed a cash grant of 1,100,000 USDS per month to the Spark Foundation from Spark's Prime Treasury for a three (3) month period to cover Q3 2026 Spark Foundation expenses.

### Context
Authorizes a 1.1M USDS/month grant (3.3M total over Q3 2026) from Spark's Prime Treasury to the Spark Foundation. Ratified by poll #1637 (10-0).

---

## PR #255 — Atlas Edit Proposal — 2026-06-08
**Merged:** 2026-06-11 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- `A.2.2.9.2.2.3.5.4.2` (Agent Artifact Updates): removed `The Agent Artifact documents specified herein are updated as the output of this process. The Output "sets" are mutually exclusive.`

---

## PR #253 — Atlas Edit Proposal — 2026-06-01
**Merged:** 2026-06-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core A.2.2.9.1.1.1.1.1 deleted: Designation Process** (UUID `3161489a…5ae9`)
- **Core A.2.2.9.1.1.2.2.1 deleted: Agent Inputs** (UUID `7a36f228…0121`)
- **Core A.2.2.9.1.1.2.3.2 deleted: Initial Deployment and Required Risk Capital / Asset Liability Management Execution** (UUID `648bcae7…f90e`)
- **Core A.2.2.9.1.1.3.2.1.3.2 deleted: Validation of TRC Report In General** (UUID `482fc286…659c`)
- **Core A.2.2.9.1.1.3.3 deleted: Allocation Instance Adjustments, Scaling, And Settlement** (UUID `93bfb0f9…081e`)
- **Core A.2.2.10.1.4.2 deleted: Allocation Based On Staked SKY** (UUID `f8d35814…7a5e`)
- **Core A.2.2.10.1.4.3 deleted: Distribution Through Prime Agents** (UUID `9a723ca1…1da6`)
- **Core A.2.2.10.1.4.2 deleted: Allocation Based On Staked SKY** (UUID `f8d35814…7a5e`)
- **Core A.2.2.8.1.2.1.5.4 deleted: Payment Errors** (UUID `1b5edf68…92cc`)
- **Core A.2.2.8.2.2.1.1.1 deleted: No Obligation To Pass Through Integration Boost Payments** (UUID `dc0bc012…a59a`)
- **Core A.2.2.8.2.2.1.1 deleted: Integration Boost Partners** (UUID `31cb3b86…cea2`)
- **Core A.2.2.8.2.2.1.3.3 deleted: Payment Errors** (UUID `8d19b08f…daec`)
- **Core A.2.2.8.2.2.1.4.3 deleted: Prime Agent May Choose Whether To Share Distribution Reward With Integration Boost Partner** (UUID `c27d41eb…0f60`)
- **Core A.2.2.8.2.2.1.4 deleted: Distribution Rewards** (UUID `d71a7b9c…26c1`)
- **Core A.2.2.9.1.1.1.1.1 deleted: Designation Process** (UUID `3161489a…5ae9`)
- **Core A.2.2.9.1.1.2.2.1 deleted: Agent Inputs** (UUID `7a36f228…0121`)
- **Core A.2.2.9.1.1.2.3.2 deleted: Initial Deployment and Required Risk Capital / Asset Liability Management Execution** (UUID `648bcae7…f90e`)
- **Core A.2.2.9.1.1.3.2.1.3.2 deleted: Validation of TRC Report In General** (UUID `482fc286…659c`)
- **Core A.2.2.9.1.1.3.3 deleted: Allocation Instance Adjustments, Scaling, And Settlement** (UUID `93bfb0f9…081e`)
- **Core A.2.2.8.1.2.1.5.4 deleted: Payment Errors** (UUID `1b5edf68…92cc`)
- **Core A.2.2.8.2.2.1.1 deleted: Integration Boost Partners** (UUID `31cb3b86…cea2`)
- **Core A.2.2.8.2.2.1.3.3 deleted: Payment Errors** (UUID `8d19b08f…daec`)
- **Core A.2.2.8.2.2.1.4.3 deleted: Prime Agent May Choose Whether To Share Distribution Reward With Integration Boost Partner** (UUID `c27d41eb…0f60`)
- **Core A.2.2.8.2.2.1.4 deleted: Distribution Rewards** (UUID `d71a7b9c…26c1`)
- **New: Base Elements** (`A.2.2.10.1.1.1`, UUID `39f3ceee…5cb0`): The documents herein define base elements of the Allocation System Primitive.
- **New: Allocation Instance Setup Process Definition** (`A.2.2.10.1.1.2`, UUID `f47513f6…70be`): The documents herein define the process for setting up an Allocation Instance as part of the Allocation System Primitive.
- **New: Allocation Instance Ongoing Management** (`A.2.2.10.1.1.3`, UUID `2db14aa7…4d4c`): The documents herein define the process for managing an Allocation Instance as part of the Allocation System Primitive.
- **New: Core Allocation Vault Address** (`A.2.2.10.1.2.2`, UUID `4655b643…9b62`): The Prime Agent Artifact must specify the address of the Prime Agent’s Core Allocation Vault.
- **New: Core Allocation Buffer Address** (`A.2.2.10.1.2.3`, UUID `2cdb447e…e80f`): The Prime Agent Artifact must specify the address of the Prime Agent’s Core Allocation Buffer.
- **New: Allocation System Core Security Parameters** (`A.2.2.10.1.2.4`, UUID `9c5e2e23…867d`): The Prime Agent Artifact must specify the rate limiters for the Allocation Vault and Core Allocation Buffer, including the address and parameters for each.
- **New: Junior Risk Capital Rental Primitive** (`A.2.2.10.2`, UUID `d8086dc0…a1ce`): The Junior Risk Capital Rental Primitive is a mechanism enabling Prime Agents to rapidly rent Junior Risk Capital from each other, ensuring that capital gets deployed to where the best opportunities are.
- **New: Asset Liability Management Rental Primitive** (`A.2.2.10.3`, UUID `bd1f1ce5…b08c`): The Asset Liability Management Rental Primitive is a mechanism enabling Prime Agents to trade Asset Liability Management obligations between each other, providing more flexibility in how capital is deployed through the Allocation System and.
- **New: Core Governance Primitives** (`A.2.2.11`, UUID `6fa54611…ae5d`): Core Governance Primitives allow Prime Agents to earn incentives for maintaining and securing Sky Governance frontends as well as borrow from the Smart Burn Engine.
  - **Core Governance Reward Primitive** (`A.2.2.11.1`): The Core Governance Reward Primitive is a reward that Sky pays to Prime Agents that provide SKY holders with secure access to the core Sky Governance features, ensuring that the Governance Security of Sky is maintained over time.
  - **Reward Pool** (`A.2.2.11.1.1`): The total reward pool for the Core Governance Reward Primitive is 1% of the Net Revenue of Sky, funded out of the Core Council Allocation (see `A.2.3.1.2.2.2`).
  - **Eligible Recipients** (`A.2.2.11.1.2`): In order for an Integrator and the Prime Agent that manages the relationship with such Integrator to be eligible for the Core Governance Reward, the frontend maintained by the Integrator must satisfy compliance requirements as specified in.
  - **Current Eligible Recipients** (`A.2.2.11.1.2.1`): The current eligible recipients for the Core Governance Reward Primitive are.
- **New: Agent Creation Primitive Results In One-Time Creation** (`A.2.2.5.1.1.2.1`, UUID `1ca2f5f3…2ae6`): Because the Agent Creation Primitive is deployed solely to effect the one-time creation of the Agent, no further management process is needed post-deployment.
- **New: Executor Accord Primitive Setup Process** (`A.2.2.6.1.1.1`, UUID `af7c2593…a163`): The documents herein define the process for setting up an Instance of the Executor Accord Primitive.
  - **Agent Inputs** (`A.2.2.6.1.1.1.1`): The Prime Agent and Operational Executor Agent must come to a consensus about the details of the Executor Accord.
  - **Validation** (`A.2.2.6.1.1.1.2`): Core GovOps validates the Agent’s inputs, ensuring that the terms of the Executor Accord are reasonably specific.
  - **Official Update Of Artifact** (`A.2.2.6.1.1.1.3`): After successful validation, the Executor Accord Primitive is considered successfully Invoked.
- **New: Executor Accord Primitive Ongoing Management** (`A.2.2.6.1.1.2`, UUID `8fe7d3f4…b562`): The documents herein define the process for the ongoing management of an Instance of the Executor Accord Primitive.
- **New: Executor Accord Primitive Activation Status** (`A.2.2.6.1.2.1`, UUID `7dcc0b40…f33a`): The Executor Accord Primitive must be Globally Activated.
- **New: Executor Accord Terms** (`A.2.2.6.1.2.2`, UUID `2ac80f9d…16dc`): The Executor Accord Primitive must include the terms of the Executor Accord between the Prime Agent and Operational Executor Agent.
- **New: Agent Agreement** (`A.2.2.6.1.2.3`, UUID `bf03d18d…5746`): The Executor Accord Primitive must include independent confirmation from each Agent that they agree to the terms of the Executor Accord.
- **New: Root Edit Primitive Process Definition** (`A.2.2.6.2.1`, UUID `f543db65…157d`): The documents herein define the Process Definition for initial setup and ongoing management of an Instance of the Root Edit Primitive.
  - **Agent Inputs** (`A.2.2.6.2.1.1.1`): The Agent must use the Powerhouse interface to specify the process by which Root Edits occur.
  - **Validation** (`A.2.2.6.2.1.1.2`): Core GovOps validates the Agent’s inputs.
  - **Official Update Of Artifact** (`A.2.2.6.2.1.1.3`): After successful validation, the Root Edit Primitive is considered successfully Invoked.
  - **Root Edit Primitive Artifact Edit Proposal** (`A.2.2.6.2.1.2.1`): The process for using the Root Edit Primitive begins with a party presenting a proposal for an Artifact Edit.
- **New: Root Edit Primitive Required Inputs** (`A.2.2.6.2.2`, UUID `cec43505…c468`): The documents herein define the required inputs for a valid Invocation of the Root Edit Primitive.
  - **Root Edit Primitive Activation Status** (`A.2.2.6.2.2.1`): The Root Edit Primitive must be Globally Activated.
  - **Artifact Edit Process** (`A.2.2.6.2.2.2`): The Root Edit Primitive must specify the process by which updates to the Agent Artifact may be made by Agent token holder vote.
- **New: Light Agent Primitive** (`A.2.2.6.3`, UUID `44028423…2b90`): The Light Agent Primitive enables users to create Light Agents, which are sub-agents operating on top of the Agent’s Executor Accord, conferring the advantages of Sky GovOps at a lower cost, but without direct access to other Sky Primitives.
- **New: Upkeep Rebate Primitive** (`A.2.2.7.2`, UUID `569e1c2b…2988`): The Upkeep Rebate Primitive allows a Prime Agent ("Holding Agent") to claim a rebate on its Ecosystem Upkeep Fees when it holds any portion of the token supply of another Prime Agent ("Issuing Agent").
- **Integrator Program** (`A.2.2.4.1`): `3` → `9.2.2.1`; `9204bcaf` → `c398b383`; `4f49` → `4534`; `a115` → `aec6`; `31fad73ebd62` → `4cd8e7292119`
- **Agent Upkeep Fees** (`A.2.3.1.2.1.2.4`): `6` → `7`
- **Sky Savings Rate Paid Through Integration Boost** (`A.2.3.1.2.1.3.2`): `8` → `9`
- **Distribution Rewards** (`A.2.3.1.2.1.3.3`): `8` → `9`
- **Pioneer Rewards** (`A.2.3.1.2.1.3.5`): `8` → `9`
- **Legacy Accounts** (`A.2.3.1.2.2.2.1.6.1`): `8` → `4`
- **Ecosystem Actors Must Consolidate All Funds From Legacy Accounts** (`A.2.3.1.2.2.2.1.6.2`): `8` → `4`
- **Legacy Accounts Are Replaced** (`A.2.3.1.2.2.2.1.6.3`): `8` → `4`
- **Expense Recognition For Legacy Account Consolidation** (`A.2.3.1.2.2.2.1.6.4`): `8` → `4`
- **Consolidation Of Funds From Legacy Accounts** (`A.2.3.1.2.2.2.1.6`): `8` → `4`
- **Core Council Allocation** (`A.2.3.1.2.2.2`): `10` → `11`
- **Operational Processes** (`A.2.4.1.1`): `8` → `9`
- **Demand Side Stablecoin Primitive Recipients** (`A.2.4.1.2.1.2.1.1`): `8` → `9`
- **Reimbursement Of Payments Made By Operational Executor Agents** (`A.2.4.1.2.1.4.3`): `8` → `9`
- **Process For July / August 2025 Monthly Settlement Cycle** (`A.2.4.1.2.1.6.2`): `8` → `9`
- **Amount Due From Sky To Primes With Respect To Distribution Reward** (`A.2.4.1.2.2.1.1.1.1`): `8` → `9`
- **Revenue Share** (`A.2.8.2.1.2.1`): `9` → `10`
- **Risk Capital Share** (`A.2.8.2.1.2.9.2`): `9` → `10`
- **Subsequent Allocation Mechanism** (`A.2.8.2.2.2.4.5`): `5` → `6`
- **Pioneer Incentive Pool** (`A.2.8.2.3.2.1`): `8` → `9`; `8` → `4`

### Housekeeping
- `A.2.11.1.1.2.1` (Assets In Scope): `makerdao` → `sky/scope`
- `A.2.11.1.1.2.3` (Impacts In Scope): `makerdao` → `sky/scope`
- `A.2.11.1.1.2.4` (Out Of Scope Vulnerabilities And Other Limitations): `makerdao` → `sky/scope`
- `A.2.11.1.1.3.1` (Rewards For Smart Contract Vulnerabilities): `makerdao` → `sky/information`
- `A.2.11.1.1.3.2` (Rewards For Website And Application Vulnerabilities): `makerdao` → `sky/information`
- `A.2.2.10.1.1` (Allocation System Process Definition): `Net Revenue of Sky, funded out of the Core Council` → ``; `2.3.1.2.2.2 - Core Council Allocation](91b281c2-0687-45a3-939d-0480c7c33f9f)). Of this, 0.5% is paid to Integrators that maintain frontends that facilitate accessible governance, with the other 0.5% paid to the Prime Agents that manage the relationship with those Integrators.` → ``
- `A.2.2.10.1.2.1` (Global Activation Status): `Current Eligible Recipients` → `Global Activation Status`
- `A.2.2.10.1.2` (Allocation System Input Requirements): removed refs to `A.2.2.11.1.3`
- `A.2.2.10.1` (Allocation System Primitive): `Core Governance Reward` → `Allocation System`
- `A.2.2.10` (Supply Side Stablecoin Primitives): `Core Governance` → `Supply Side Stablecoin`
- `A.2.2.5.1.1.1.1` (Founder Inputs): removed `###### A.2.2.4.1.1.1.1 - Founder Inputs [Core]`
- `A.2.2.5.1.1.1.2` (Validation): `Core GovOps validates the Founder’s inputs. This includes verifying that all of the documents created by the Founder using Founder Access are well-specified, that the documents are Aligned, and that all necessary Primitives to complete setup have been Activated. The necessary Primitives are the Agent Creation, Prime/Executor Transformation, Agent Token, Executor Accord, Root Edit, and Ecosystem Upkeep Fee Primitives. (See [A.2.2.1.1.3.1 - Founder Required Primitive Activation](1a48e833-d960-4bdf-8f67-0f9d9307e00d).) After confirming these conditions, Core GovOps creates a Genesis Account and a SubProxy Account for the Agent.` → ``
- `A.2.2.4.1.1.1` (Alignment): `Agent Creation Instance Setup Process` → `Alignment`
- `A.2.2.4.1.1.2.1` (Consequence For Integrator Non-Compliance With Local Laws And Regulations): `Agent Creation Primitive Results In One-Time Creation` → `Consequence For Integrator Non-Compliance With Local Laws And Regulations`
- `A.2.2.4.1.1.2` (Compliance With Local Laws And Regulations As A Condition Precedent To Integrators Receiving Distribution Rewards): removed `###### A.2.2.4.1.1.2 - Agent Creation Instance Ongoing Management [Core]`
- `A.2.2.4.1.1` (Integrator Requirements): `Agent Creation Primitive Process Definition` → `Integrator Requirements`
- `A.2.2.4.1.2.1` (Near Term Process): `Global Activation Status` → `Near Term Process`
- `A.2.2.4.1.2.2` (Long Term Process): `Agent Name And Introduction` → `Long Term Process`
- `A.2.2.4.1.2` (Integrator Applications): `Agent Creation Primitive Input Requirements` → `Integrator Applications`
- `A.2.2.5.2.1.1.1` (Agent Inputs): removed `###### A.2.2.4.2.1.1.1 - Agent Inputs [Core]`
- `A.2.2.5.2.1.1.2` (Validation): `Core GovOps validates the Proto-Agent’s inputs, namely, the Agent Type. Additionally, Core GovOps performs a further review to confirm that all the documents created by the Founder using Founder Access are well-specified, that the documents are Aligned, and that all necessary Primitives have been Activated. The necessary Primitives are the Agent Creation, Prime/Executor Transformation, Agent Token, Executor Accord, Root Edit, and Ecosystem Upkeep Fee Primitives. (See [A.2.2.1.1.3.1 - Founder Required Primitive Activation](1a48e833-d960-4bdf-8f67-0f9d9307e00d).)` → ``
- `A.2.2.4.2` (Reward Recipient And Sharing): `or Executor Agent to gain functionality` → `that manages the relationship with the Integrator`
- `A.2.2.4.3` (Demand Side Buffer): `Executor Transformation Primitive` → `Demand Side Buffer`; `Executor Transformation Primitive allows` → `Demand Side Buffer is the account used for disbursement of Distribution Reward and Integration Boost payments. The Demand Side Buffer is controlled by a multisig as specified in the documents herein. The balance of this account may be topped up through`
- `A.2.2.4` (Primitive Reward Infrastructure): `Genesis Primitives` → `Primitive Reward Infrastructure`
- `A.2.2.5.1.1.1.1` (Founder Inputs): `Prime Agent and Operational Executor Agent must come to a consensus about the details of the Executor Accord. These details must be entered into` → `Founder uses`
- `A.2.2.5.1.1.1.2` (Validation): `` → `Agent Creation, Prime/Executor Transformation, Agent Token,`
- `A.2.2.5.1.1.1.3` (Official Update Of Artifact): `Executor Accord` → `Agent Creation`; `Executor Accord` → `Agent Creation`
- `A.2.2.5.1.2.2` (Agent Name And Introduction): `Executor Accord Terms` → `Agent Name And Introduction`; `Executor Accord` → `Agent Creation`
- `A.2.2.5.1.2.3` (Agent SubProxy Account): `Executor Accord` → `Agent Creation`; `Executor Accord` → `Agent. This field is populated by Core GovOps`
- `A.2.2.5.1.2` (Agent Creation Primitive Input Requirements): `Executor Accord` → `Agent Creation`; `Executor Accord` → `Agent Creation`
- `A.2.2.5.1` (Agent Creation Primitive): `Executor Accord` → `Agent Creation`; `The Executor Accord` → `This`
- `A.2.2.5.2.1.1.1` (Agent Inputs): removed refs to `A.1.14.2.7`
- `A.2.2.5.2.1.1.2` (Validation): `` → `Additionally, Core GovOps performs a further review to confirm that all the documents created by the Founder using Founder Access are well-specified, that the documents are Aligned, and that all necessary Primitives have been Activated. The necessary Primitives are the Agent Creation, Prime/Executor Transformation, Agent Token, Executor Accord, Root Edit, and Ecosystem Upkeep Fee Primitives. (See [A.2.2.1.1.3.1 - Founder Required Primitive Activation](1a48e833-d960-4bdf-8f67-0f9d9307e00d).)`
- `A.2.2.5.2.1.1.3` (Official Update Of Artifact): `Root Edit` → `Prime Transformation`
- `A.2.2.5.2.1.1` (Prime Transformation Primitive Setup Process): `Root Edit` → `Prime Transformation`
- `A.2.2.5.2.1.2.1` (Prime Transformation Primitive Results In One-Time Creation): `Root Edit` → `Prime Transformation`
- `A.2.2.5.2.1.2` (Prime Transformation Primitive Ongoing Management): `Root Edit` → `Prime Transformation`
- `A.2.2.5.2.1` (Prime Transformation Primitive Process Definition): `Root Edit` → `Prime Transformation`
- `A.2.2.5.2.2.1` (Global Activation Status): `Root Edit Primitive` → `Global`
- `A.2.2.5.2.2.2` (Prime Agent Type): `The details of this process may be specified by the Agent, subject to the following conditions: (1) Agent token holders must vote to approve Artifact Edit proposals, (2) the Operational Facilitator must review each proposal for alignment and conformance with the process specified in the Root Edit Primitive, (3) the vote must be conducted by the Operational Facilitator, and (4) the Operational Facilitator must action the Artifact Edit if the vote passes. The process definition must include the elements included in the documents herein.` → ``
- `A.2.2.5.2.2` (Prime Transformation Primitive Input Requirements): `Root Edit` → `Prime Transformation`
- `A.2.2.5.2` (Prime Transformation Primitive): `specified in the Executor Accord` → `to gain functionality. The Prime Transformation`
- `A.2.2.5.3` (Executor Transformation Primitive): `Light Agent` → `Executor Transformation`; `Light` → `Executor Transformation Primitive allows an`
- `A.2.2.5` (Genesis Primitives): `Operational` → `Genesis`
- `A.2.2.6.1.1` (Executor Accord Primitive Process Definition): `Sky Core-Designated Address` → `Executor Accord Primitive Process Definition`; `Atlas` → `Executor Accord Primitive`
- `A.2.2.6.1.2` (Executor Accord Primitive Required Inputs): `Valuation` → `Executor Accord Primitive Required Inputs`; `token over the 24-hour period ending at 23:59 UTC on the last day of each month, immediately preceding the payment event. This value is applied in the rebate calculation under the Upkeep Rebate` → `Executor Accord`
- `A.2.2.6.1` (Executor Accord Primitive): `Ecosystem Upkeep Fee` → `Executor Accord`; `Ecosystem Upkeep Fee` → `Executor Accord`
- `A.2.2.6.2` (Root Edit Primitive): `` → `The Root Edit Primitive allows Prime Agents, through a token holder vote, to direct the Operational Executor Agent specified in the Executor Accord Primitive to directly modify the Prime Agent Artifact.`
- `A.2.2.6` (Operational Primitives): `Ecosystem Upkeep` → `Operational`
- `A.2.2.8.1.1.1` (Token SkyLink Setup Process Definition): removed `###### A.2.2.7.1.1.1 - Token SkyLink Setup Process Definition [Core]`
- `A.2.2.8.1.1.2` (Token SkyLink Ongoing Management): removed `###### A.2.2.7.1.1.2 - Token SkyLink Ongoing Management [Core]`
- `A.2.2.7.1.1` (Sky Core-Designated Address): `Token SkyLink Process Definition` → `Sky Core-Designated Address`
- `A.2.2.8.1.2.1` (Token SkyLink Activation Status): removed `###### A.2.2.7.1.2.1 - Token SkyLink Activation Status [Core]`
- `A.2.2.8.1.2.2` (List of Active Token SkyLink Deployments): removed `###### A.2.2.7.1.2.2 - List of Active Token SkyLink Deployments [Core]`
- `A.2.2.7.1.2` (Valuation): added refs to `A.2.2.7.2`
- `A.2.2.7.1` (Ecosystem Upkeep Fee Primitive): added refs to `A.2.2.7.1.1`
- `A.2.2.7` (Ecosystem Upkeep Primitives): `SkyLink` → `Ecosystem Upkeep`
- `A.2.2.8.1.1.1` (Token SkyLink Setup Process Definition): `Purpose` → `Token SkyLink Setup Process Definition`
- `A.2.2.8.1.1.2` (Token SkyLink Ongoing Management): `Allowed Number Of Instances` → `Token SkyLink Ongoing Management`
- `A.2.2.8.1.1` (Token SkyLink Process Definition): `Introduction` → `Token SkyLink Process Definition`
- `A.2.2.4.1.1.1` (Alignment): removed `###### A.2.2.8.1.2.1.1.1.1 - Alignment [Core]`
- `A.2.2.4.1.1.2.1` (Consequence For Integrator Non-Compliance With Local Laws And Regulations): removed `###### A.2.2.8.1.2.1.1.1.2.1 - Consequence For Integrator Non-Compliance With Local Laws And Regulations [Core]`
- `A.2.2.4.1.1.2` (Compliance With Local Laws And Regulations As A Condition Precedent To Integrators Receiving Distribution Rewards): removed `###### A.2.2.8.1.2.1.1.1.2 - Compliance With Local Laws And Regulations As A Condition Precedent To Integrators Receiving Distribution Rewar…`
- `A.2.2.4.1.1` (Integrator Requirements): removed `###### A.2.2.8.1.2.1.1.1 - Integrator Requirements [Core]`
- `A.2.2.4.1.2.1` (Near Term Process): removed `###### A.2.2.8.1.2.1.1.2.1 - Near Term Process [Core]`
- `A.2.2.4.1.2.2` (Long Term Process): removed `###### A.2.2.8.1.2.1.1.2.2 - Long Term Process [Core]`
- `A.2.2.4.1.2` (Integrator Applications): removed `###### A.2.2.8.1.2.1.1.2 - Integrator Applications [Core]`
- `A.2.2.4.1` (Integrator Program): removed refs to `A.2.2.9.2.2.1`
- `A.2.2.4.3` (Demand Side Buffer): removed `###### A.2.2.8.1.2.1.4 - Demand Side Buffer [Core]`
- `A.2.2.8.1.2.1` (Token SkyLink Activation Status): `Base Elements` → `Token SkyLink Activation Status`
- `A.2.2.8.1.2.2` (List of Active Token SkyLink Deployments): `Global Activation` → `List of Active Token SkyLink Deployments`
- `A.2.2.9.1.2.3` (Instance Invocation Protocol): removed `###### A.2.2.8.1.2.3 - Instance Invocation Protocol [Core]`
- `A.2.2.9.1.2.4` (Instance Ongoing Management Protocol): removed `###### A.2.2.8.1.2.4 - Instance Ongoing Management Protocol [Core]`
- `A.2.2.8.1.2` (Token SkyLink Input Requirements): `Global Specification` → `Token SkyLink Input Requirements`
- `A.2.2.8.1` (Token SkyLink Primitive): `Distribution Reward` → `Token SkyLink`
- `A.2.2.9.2` (Integration Boost Primitive): removed `###### A.2.2.8.2 - Integration Boost Primitive [Core]`
- `A.2.2.9.3` (Pioneer Chain Primitive): removed `###### A.2.2.8.3 - Pioneer Chain Primitive [Core]`
- `A.2.2.8` (SkyLink Primitives): `Demand Side Stablecoin` → `SkyLink`
- `A.2.2.9.1.1.1` (Purpose): `Base Elements` → `Purpose`
- `A.2.2.9.1.1.2` (Allowed Number Of Instances): `Allocation Instance Setup Process Definition` → `Allowed Number Of Instances`
- `A.2.2.9.1.1.3` (Multi-Instance Coordinator Document): `Allocation` → `Multi-`
- `A.2.2.9.1.1` (Introduction): `Allocation System Process Definition` → `Introduction`
- `A.2.2.9.1.2.1` (Base Elements): `Global Activation Status` → `Base Elements`
- `A.2.2.9.1.2.2` (Global Activation): `Core Allocation Vault Address` → `Global Activation`
- `A.2.2.9.1.2.3` (Instance Invocation Protocol): `Core Allocation Buffer Address` → `Instance Invocation Protocol`
- `A.2.2.9.1.2.4` (Instance Ongoing Management Protocol): `Allocation System Core Security Parameters` → `Instance Ongoing Management Protocol`
- `A.2.2.9.1.2` (Global Specification): `Allocation System Input Requirements` → `Global Specification`
- `A.2.2.9.1` (Distribution Reward Primitive): `Allocation System` → `Distribution Reward`
- `A.2.2.9.2` (Integration Boost Primitive): `Junior Risk Capital Rental` → `Integration Boost`
- `A.2.2.9.3` (Pioneer Chain Primitive): `Asset Liability Management Rental` → `Pioneer Chain`
- `A.2.2.9` (Demand Side Stablecoin Primitives): `Supply` → `Demand`
- `A.2.2.10.1.1.1.1.2.0.6.1` renumbered (UUID stable: `5f368e33…c043`)
- `A.2.2.10.1.1.1.1.2` renumbered (UUID stable: `1c0410e4…fbec`)
- `A.2.2.10.1.1.1.1.3.1` renumbered (UUID stable: `8bd63c6b…cd6d`)
- `A.2.2.10.1.1.1.1.3` renumbered (UUID stable: `cbd64e6c…aef1`)
- `A.2.2.10.1.1.1.1.4` renumbered (UUID stable: `07e0f716…3f48`)
- `A.2.2.10.1.1.1.1.5` renumbered (UUID stable: `b683953e…4870`)
- `A.2.2.10.1.1.1.1.6` renumbered (UUID stable: `bfb8013f…4107`)
- `A.2.2.10.1.1.1.1` renumbered (UUID stable: `b3fb8653…6703`)
- `A.2.2.10.1.1.1.2.1` renumbered (UUID stable: `a578830d…50ae`)
- `A.2.2.10.1.1.1.2.2.1` renumbered (UUID stable: `8b5f1ffd…fadb`)
- `A.2.2.10.1.1.1.2.2.2` renumbered (UUID stable: `ae8674bc…6e9a`)
- `A.2.2.10.1.1.1.2.2.3` renumbered (UUID stable: `8d0419a4…3694`)
- `A.2.2.10.1.1.1.2.2.4` renumbered (UUID stable: `02918cfc…cbac`)
- `A.2.2.10.1.1.1.2.2` renumbered (UUID stable: `8efb0a11…39b5`)
- `A.2.2.10.1.1.1.2.3` renumbered (UUID stable: `d59a233c…5fd8`)
- `A.2.2.10.1.1.1.2.4` renumbered (UUID stable: `e50fd86a…d171`)
- `A.2.2.10.1.1.1.2.5` renumbered (UUID stable: `b95b3bd8…aea3`)
- `A.2.2.10.1.1.1.2.6` renumbered (UUID stable: `7c6da187…3ea7`)
- `A.2.2.10.1.1.1.2` renumbered (UUID stable: `a8a3e54d…9aa3`)
- `A.2.2.10.1.1.2.1.1` renumbered (UUID stable: `b60b170f…25ba`)
- `A.2.2.10.1.1.2.1.2` renumbered (UUID stable: `8d3b553c…1c58`)
- `A.2.2.10.1.1.2.1.3.1` renumbered (UUID stable: `c3b53ee8…8706`)
- `A.2.2.10.1.1.2.1.3.2` renumbered (UUID stable: `a30447be…d6f5`)
- `A.2.2.10.1.1.2.1.3.3` renumbered (UUID stable: `a156b120…a102`)
- `A.2.2.10.1.1.2.1.3` renumbered (UUID stable: `4aa05a21…edba`)
- `A.2.2.10.1.1.2.1.4` renumbered (UUID stable: `e7d3d696…7cc6`)
- `A.2.2.10.1.1.2.1` renumbered (UUID stable: `eeeeb5ff…f833`)
- `A.2.2.10.1.1.2.2.2` renumbered (UUID stable: `dbae3918…aa70`)
- `A.2.2.10.1.1.2.2.3` renumbered (UUID stable: `2b1612b8…40de`)
- `A.2.2.10.1.1.2.2` renumbered (UUID stable: `410c84be…8948`)
- `A.2.2.10.1.1.2.3.1` renumbered (UUID stable: `6899a722…bab0`)
- `A.2.2.10.1.1.2.3` renumbered (UUID stable: `3766cb8c…0532`)
- `A.2.2.10.1.1.3.1` renumbered (UUID stable: `989512c2…6024`)
- `A.2.2.10.1.1.3.2.1.1.1` renumbered (UUID stable: `f7da0f56…7992`)
- `A.2.2.10.1.1.3.2.1.1.2` renumbered (UUID stable: `18243e7a…5f9d`)
- `A.2.2.10.1.1.3.2.1.1` renumbered (UUID stable: `4eac2c9e…4d13`)
- `A.2.2.10.1.1.3.2.1.2.1` renumbered (UUID stable: `9a8120c4…13f5`)
- `A.2.2.10.1.1.3.2.1.2.2` renumbered (UUID stable: `d034533f…765f`)
- `A.2.2.10.1.1.3.2.1.2.3.1` renumbered (UUID stable: `7e95efa7…bf31`)
- `A.2.2.10.1.1.3.2.1.2.3.2` renumbered (UUID stable: `4887e971…0fa0`)
- `A.2.2.10.1.1.3.2.1.2.3` renumbered (UUID stable: `41ca2085…b6fc`)
- `A.2.2.10.1.1.3.2.1.2` renumbered (UUID stable: `3af8a3a2…2685`)
- `A.2.2.10.1.1.3.2.1.3.1` renumbered (UUID stable: `8048bdf0…3c84`)
- `A.2.2.10.1.1.3.2.1.3.2.1` renumbered (UUID stable: `1ac3e606…98d3`)
- `A.2.2.10.1.1.3.2.1.3.3` renumbered (UUID stable: `36f3e675…6273`)
- `A.2.2.10.1.1.3.2.1.3` renumbered (UUID stable: `18d692ce…7987`)
- `A.2.2.10.1.1.3.2.1.4` renumbered (UUID stable: `12b7d480…c112`)
- `A.2.2.10.1.1.3.2.1.5` renumbered (UUID stable: `1ec5f16f…554b`)
- `A.2.2.10.1.1.3.2.1` renumbered (UUID stable: `1c5fb5bb…276e`)
- `A.2.2.10.1.1.3.2.2` renumbered (UUID stable: `ed10830e…18bb`)
- `A.2.2.10.1.1.3.2` renumbered (UUID stable: `13eb2346…46ab`)
- `A.2.2.10.1.1.3.3.1.1` renumbered (UUID stable: `3db4c73f…e166`)
- `A.2.2.10.1.1.3.3.1.2` renumbered (UUID stable: `235a7317…8dc8`)
- `A.2.2.10.1.1.3.3.1.3` renumbered (UUID stable: `aee1d848…474a`)
- `A.2.2.10.1.1.3.3.1.4` renumbered (UUID stable: `e3a00c33…00fa`)
- `A.2.2.10.1.1.3.3.1` renumbered (UUID stable: `c1b5708c…4f13`)
- `A.2.2.10.1.2.5` renumbered (UUID stable: `4b8cf927…86be`)
- `A.2.2.10.1.2.6.1` renumbered (UUID stable: `6ad0fdb4…e0ec`)
- `A.2.2.10.1.2.6.2.1` renumbered (UUID stable: `3f48dff7…e318`)
- `A.2.2.10.1.2.6.2.2` renumbered (UUID stable: `2cdd38d7…c275`)
- `A.2.2.10.1.2.6.2.3` renumbered (UUID stable: `4363d9c4…415e`)
- `A.2.2.10.1.2.6.2` renumbered (UUID stable: `0e4a5264…b46b`)
- `A.2.2.10.1.2.6` renumbered (UUID stable: `e4975062…8cb9`)
- `A.2.2.11.1.3.1` renumbered (UUID stable: `a6ab8a87…989c`)
- `A.2.2.11.1.3.2` renumbered (UUID stable: `6c53d0a0…4a28`)
- `A.2.2.11.1.3` renumbered (UUID stable: `068c37b5…dbc3`)
- `A.2.2.11.1.4.1` renumbered (UUID stable: `dc825d62…f9a6`)
- `A.2.2.11.1.4.2.1` renumbered (UUID stable: `b16cb8a3…a8e1`)
- `A.2.2.11.1.4` renumbered (UUID stable: `72ce2c27…7659`)
- `A.2.2.11.1.5` renumbered (UUID stable: `b3f97303…bd7e`)
- `A.2.2.4.1.1.2.2` renumbered (UUID stable: `0bdcef8a…dad0`)
- `A.2.2.4.1.2.1.1.0.6.1` renumbered (UUID stable: `30db9618…ff62`)
- `A.2.2.4.1.2.1.1` renumbered (UUID stable: `d251bbac…3e19`)
- `A.2.2.4.1.3.1` renumbered (UUID stable: `fc46821f…6702`)
- `A.2.2.4.1.3` renumbered (UUID stable: `361e2e68…509e`)
- `A.2.2.4.3.1` renumbered (UUID stable: `dadf97b5…345f`)
- `A.2.2.4.3.2` renumbered (UUID stable: `8e341f8c…179c`)
- `A.2.2.4.3.3` renumbered (UUID stable: `af4edd62…ab0b`)
- `A.2.2.4.3.4` renumbered (UUID stable: `f489f6b8…14b8`)
- `A.2.2.4.3.5` renumbered (UUID stable: `379f5e3c…e157`)
- `A.2.2.4.3.6.1.0.6.1` renumbered (UUID stable: `620715c0…c572`)
- `A.2.2.4.3.6.1` renumbered (UUID stable: `32e27a27…7b97`)
- `A.2.2.4.3.6` renumbered (UUID stable: `dfc22e9d…2f77`)
- `A.2.2.5.1.2.4` renumbered (UUID stable: `761966db…7d26`)
- `A.2.2.5.4.1.1.1` renumbered (UUID stable: `f74588a5…0612`)
- `A.2.2.5.4.1.1.2` renumbered (UUID stable: `6f63137d…f54a`)
- `A.2.2.5.4.1.1.3` renumbered (UUID stable: `309e17ed…a1f8`)
- `A.2.2.5.4.1.1.4` renumbered (UUID stable: `d26166c3…8ed3`)
- `A.2.2.5.4.1.1` renumbered (UUID stable: `3e49628d…aa54`)
- `A.2.2.5.4.1.2.1` renumbered (UUID stable: `0489781a…d41c`)
- `A.2.2.5.4.1.2` renumbered (UUID stable: `d8f6b024…8850`)
- `A.2.2.5.4.1` renumbered (UUID stable: `f7a81be7…4010`)
- `A.2.2.5.4.2.1` renumbered (UUID stable: `fb858d4e…f8f0`)
- `A.2.2.5.4.2.2` renumbered (UUID stable: `98fa133d…b9bb`)
- `A.2.2.5.4.2.3` renumbered (UUID stable: `46bbc08e…35f9`)
- `A.2.2.5.4.2.4` renumbered (UUID stable: `ed342c6e…ba62`)
- `A.2.2.5.4.2.5` renumbered (UUID stable: `745126ca…e74b`)
- `A.2.2.5.4.2.6` renumbered (UUID stable: `70e08dd1…37e8`)
- `A.2.2.5.4.2.7` renumbered (UUID stable: `0f71bdc3…1d27`)
- `A.2.2.5.4.2.8` renumbered (UUID stable: `3d43ba11…f1eb`)
- `A.2.2.5.4.2` renumbered (UUID stable: `9d88d70e…61fd`)
- `A.2.2.5.4` renumbered (UUID stable: `2047c361…2064`)
- `A.2.2.6.1.1.1.4` renumbered (UUID stable: `8179ca9b…91cf`)
- `A.2.2.6.2.1.2.2` renumbered (UUID stable: `823cad54…fabd`)
- `A.2.2.6.2.1.2.3` renumbered (UUID stable: `7e4574c0…0aed`)
- `A.2.2.6.2.1.2.4` renumbered (UUID stable: `34d06691…ef0f`)
- `A.2.2.6.2.2.2.1` renumbered (UUID stable: `7a473c50…08d9`)
- `A.2.2.6.2.2.2.2` renumbered (UUID stable: `b5e21f94…5cf9`)
- `A.2.2.6.2.2.2.3` renumbered (UUID stable: `0580f68b…0f81`)
- `A.2.2.6.2.2.2.4` renumbered (UUID stable: `0ca3f0ee…4848`)
- `A.2.2.6.2.2.2.5` renumbered (UUID stable: `d4ad86a0…be0e`)
- `A.2.2.6.2.2.2.6` renumbered (UUID stable: `0c36f76d…3982`)
- `A.2.2.6.2.2.2.7` renumbered (UUID stable: `dda24bc9…d198`)
- `A.2.2.6.2.2.2.8.1.1` renumbered (UUID stable: `02fb768f…9269`)
- `A.2.2.6.2.2.2.8.1.2` renumbered (UUID stable: `119efbc0…edd4`)
- `A.2.2.6.2.2.2.8.1.3` renumbered (UUID stable: `f6dc0c8e…a4d8`)
- `A.2.2.6.2.2.2.8.1.4` renumbered (UUID stable: `42cedad0…9311`)
- `A.2.2.6.2.2.2.8.1.5` renumbered (UUID stable: `56c255d4…023c`)
- `A.2.2.6.2.2.2.8.1` renumbered (UUID stable: `82f9f4b9…3b75`)
- `A.2.2.6.2.2.2.8` renumbered (UUID stable: `b6fa5678…f689`)
- `A.2.2.6.2.3.1` renumbered (UUID stable: `8c15762a…9c0f`)
- `A.2.2.6.2.3.2.1` renumbered (UUID stable: `461272f0…86c7`)
- `A.2.2.6.2.3.2.2.1` renumbered (UUID stable: `4b37392d…3743`)
- `A.2.2.6.2.3.2.2` renumbered (UUID stable: `07d1ed44…0acc`)
- `A.2.2.6.2.3.2.3` renumbered (UUID stable: `afeaa98f…667d`)
- `A.2.2.6.2.3.2.4` renumbered (UUID stable: `61414e64…53b6`)
- `A.2.2.6.2.3.2` renumbered (UUID stable: `364e52eb…baeb`)
- `A.2.2.6.2.3` renumbered (UUID stable: `459f257e…67ff`)
- `A.2.2.8.1.1.1.1.1` renumbered (UUID stable: `298ee5be…c038`)
- `A.2.2.8.1.1.1.1.2` renumbered (UUID stable: `eec4c93e…042c`)
- `A.2.2.8.1.1.1.1.3` renumbered (UUID stable: `aa9f9672…c125`)
- `A.2.2.8.1.1.1.1` renumbered (UUID stable: `f1836fc1…56b3`)
- `A.2.2.8.1.1.1.2.1` renumbered (UUID stable: `5027bb60…33e5`)
- `A.2.2.8.1.1.1.2.2` renumbered (UUID stable: `cac40223…ba00`)
- `A.2.2.8.1.1.1.2.3` renumbered (UUID stable: `79abf483…e7a8`)
- `A.2.2.8.1.1.1.2` renumbered (UUID stable: `18ce8e21…66ee`)
- `A.2.2.8.1.1.1.3.1` renumbered (UUID stable: `af88c454…e209`)
- `A.2.2.8.1.1.1.3.2` renumbered (UUID stable: `c18d8c58…0f90`)
- `A.2.2.8.1.1.1.3` renumbered (UUID stable: `21241867…0292`)
- `A.2.2.8.1.1.2.1` renumbered (UUID stable: `97fb1954…2e0e`)
- `A.2.2.9.1.2.1.1.1.1` renumbered (UUID stable: `e00e28d1…3b07`)
- `A.2.2.9.1.2.1.1.1` renumbered (UUID stable: `225454ec…a453`)
- `A.2.2.9.1.2.1.1.2.1` renumbered (UUID stable: `87fd6861…e3e2`)
- `A.2.2.9.1.2.1.1.2.2` renumbered (UUID stable: `1b5cc0ee…17dc`)
- `A.2.2.9.1.2.1.1.2.3` renumbered (UUID stable: `f710bddf…6333`)
- `A.2.2.9.1.2.1.1.2.4` renumbered (UUID stable: `5eba1c21…5f16`)
- `A.2.2.9.1.2.1.1.2.5` renumbered (UUID stable: `c0b77312…5a7c`)
- `A.2.2.9.1.2.1.1.2` renumbered (UUID stable: `ec2c6d8a…cc37`)
- `A.2.2.9.1.2.1.1.3` renumbered (UUID stable: `75ddec36…e848`)
- `A.2.2.9.1.2.1.1` renumbered (UUID stable: `cda71b0c…bfe1`)
- `A.2.2.9.1.2.1.2.1.1` renumbered (UUID stable: `3f3162cc…4261`)
- `A.2.2.9.1.2.1.2.1.2` renumbered (UUID stable: `ce66fc65…032e`)
- `A.2.2.9.1.2.1.2.1.3` renumbered (UUID stable: `f2b3688f…abab`)
- `A.2.2.9.1.2.1.2.1` renumbered (UUID stable: `1d9219cb…4c63`)
- `A.2.2.9.1.2.1.2` renumbered (UUID stable: `57384c49…4759`)
- `A.2.2.9.1.2.1.3.1` renumbered (UUID stable: `02d1e35f…a9d1`)
- `A.2.2.9.1.2.1.3.2` renumbered (UUID stable: `38cb0bfe…d08e`)
- `A.2.2.9.1.2.1.3.3.1` renumbered (UUID stable: `05fb732b…d2d2`)
- `A.2.2.9.1.2.1.3.3.2` renumbered (UUID stable: `07953e87…ba94`)
- `A.2.2.9.1.2.1.3.3` renumbered (UUID stable: `935b90bb…d2f1`)
- `A.2.2.9.1.2.1.3` renumbered (UUID stable: `8dfabd92…03dc`)
- `A.2.2.9.1.2.1.4.1.0.6.1` renumbered (UUID stable: `efbe7903…3157`)
- `A.2.2.9.1.2.1.4.1` renumbered (UUID stable: `883f1b52…3b53`)
- `A.2.2.9.1.2.1.4.2.0.6.1` renumbered (UUID stable: `eb644108…d9be`)
- `A.2.2.9.1.2.1.4.2` renumbered (UUID stable: `9a7f47ae…e1cc`)
- `A.2.2.9.1.2.1.4` renumbered (UUID stable: `f3952cc5…570b`)
- `A.2.2.9.1.2.1.5.1.0.6.1` renumbered (UUID stable: `169eb312…705e`)
- `A.2.2.9.1.2.1.5.1` renumbered (UUID stable: `2c0eb02c…f0b7`)
- `A.2.2.9.1.2.1.5` renumbered (UUID stable: `fd551536…fcaf`)
- `A.2.2.9.1.2.2.1.1.1` renumbered (UUID stable: `b4271bcd…3629`)
- `A.2.2.9.1.2.2.1.1.2` renumbered (UUID stable: `e2766ea3…e164`)
- `A.2.2.9.1.2.2.1.1` renumbered (UUID stable: `090b3f8e…3a33`)
- `A.2.2.9.1.2.2.1.2` renumbered (UUID stable: `4e4476d8…e01c`)
- `A.2.2.9.1.2.2.1` renumbered (UUID stable: `776d926e…7ea3`)
- `A.2.2.9.1.2.2.2` renumbered (UUID stable: `89d26f82…be6d`)
- `A.2.2.9.1.2.2.3` renumbered (UUID stable: `108c6d9c…5c0c`)
- `A.2.2.9.1.2.2.4.1` renumbered (UUID stable: `74003afb…c039`)
- `A.2.2.9.1.2.2.4.2` renumbered (UUID stable: `6af6cd24…badf`)
- `A.2.2.9.1.2.2.4` renumbered (UUID stable: `faf79404…92ab`)
- `A.2.2.9.1.2.3.1.1.1.1` renumbered (UUID stable: `dec5be6c…9572`)
- `A.2.2.9.1.2.3.1.1.1.2` renumbered (UUID stable: `34497a9f…6700`)
- `A.2.2.9.1.2.3.1.1.1` renumbered (UUID stable: `222fc95e…b0a0`)
- `A.2.2.9.1.2.3.1.1.2` renumbered (UUID stable: `c89c3cd1…2049`)
- `A.2.2.9.1.2.3.1.1` renumbered (UUID stable: `005beba7…ef69`)
- `A.2.2.9.1.2.3.1.2` renumbered (UUID stable: `75ff9b92…918e`)
- `A.2.2.9.1.2.3.1.3` renumbered (UUID stable: `4d5482ad…27a3`)
- `A.2.2.9.1.2.3.1.4.1.1` renumbered (UUID stable: `6857396f…6830`)
- `A.2.2.9.1.2.3.1.4.1` renumbered (UUID stable: `bab05cb6…294b`)
- `A.2.2.9.1.2.3.1.4.2` renumbered (UUID stable: `11161730…7390`)
- `A.2.2.9.1.2.3.1.4` renumbered (UUID stable: `1ad17e84…c603`)
- `A.2.2.9.1.2.3.1` renumbered (UUID stable: `f07b1cca…76f3`)
- `A.2.2.9.1.2.3.2.1.1.1` renumbered (UUID stable: `d1d3de53…340c`)
- `A.2.2.9.1.2.3.2.1.1.2` renumbered (UUID stable: `fd211726…e92b`)
- `A.2.2.9.1.2.3.2.1.1` renumbered (UUID stable: `f89a41b2…19ef`)
- `A.2.2.9.1.2.3.2.1.2` renumbered (UUID stable: `abb8f0ef…e7c9`)
- `A.2.2.9.1.2.3.2.1` renumbered (UUID stable: `da868510…9a25`)
- `A.2.2.9.1.2.3.2.2` renumbered (UUID stable: `ef743f33…1017`)
- `A.2.2.9.1.2.3.2.3` renumbered (UUID stable: `9c4653fa…9311`)
- `A.2.2.9.1.2.3.2.4.1` renumbered (UUID stable: `9a94a573…3bb8`)
- `A.2.2.9.1.2.3.2.4.2.1` renumbered (UUID stable: `66a07769…1575`)
- `A.2.2.9.1.2.3.2.4.2.2` renumbered (UUID stable: `6f457b50…9627`)
- `A.2.2.9.1.2.3.2.4.2` renumbered (UUID stable: `ec050d61…8292`)
- `A.2.2.9.1.2.3.2.4` renumbered (UUID stable: `a7a3e2d3…a5e4`)
- `A.2.2.9.1.2.3.2` renumbered (UUID stable: `5fd265ef…7636`)
- `A.2.2.9.1.2.3.3.1.1.1` renumbered (UUID stable: `e379a9d8…c490`)
- `A.2.2.9.1.2.3.3.1.1.2` renumbered (UUID stable: `94d06bae…873b`)
- `A.2.2.9.1.2.3.3.1.1` renumbered (UUID stable: `bdc8d447…5aac`)
- `A.2.2.9.1.2.3.3.1.2` renumbered (UUID stable: `a6f968d6…02db`)
- `A.2.2.9.1.2.3.3.1` renumbered (UUID stable: `9add3334…cf9a`)
- `A.2.2.9.1.2.3.3.2` renumbered (UUID stable: `ccb71126…3f32`)
- `A.2.2.9.1.2.3.3.3` renumbered (UUID stable: `6f4e7971…54af`)
- `A.2.2.9.1.2.3.3.4.1` renumbered (UUID stable: `264273c8…763d`)
- `A.2.2.9.1.2.3.3.4.2.1` renumbered (UUID stable: `b37c4266…94d9`)
- `A.2.2.9.1.2.3.3.4.2` renumbered (UUID stable: `a3294ae2…931e`)
- `A.2.2.9.1.2.3.3.4` renumbered (UUID stable: `c7ed27ce…976d`)
- `A.2.2.9.1.2.3.3` renumbered (UUID stable: `240e0e2c…6e59`)
- `A.2.2.9.1.2.3.4.1.1.1` renumbered (UUID stable: `296a23ca…0bbb`)
- `A.2.2.9.1.2.3.4.1.1.2` renumbered (UUID stable: `bee5a2d9…1f0f`)
- `A.2.2.9.1.2.3.4.1.1` renumbered (UUID stable: `48a12682…3b7b`)
- `A.2.2.9.1.2.3.4.1.2` renumbered (UUID stable: `967572c4…d440`)
- `A.2.2.9.1.2.3.4.1` renumbered (UUID stable: `4e87663b…f4e7`)
- `A.2.2.9.1.2.3.4.2` renumbered (UUID stable: `67dce065…2796`)
- `A.2.2.9.1.2.3.4.3` renumbered (UUID stable: `967f54c6…d91e`)
- `A.2.2.9.1.2.3.4.4.1` renumbered (UUID stable: `dfdf873a…d9bb`)
- `A.2.2.9.1.2.3.4.4.2` renumbered (UUID stable: `9cb3ab72…7dd8`)
- `A.2.2.9.1.2.3.4.4` renumbered (UUID stable: `b63e78d1…54a5`)
- `A.2.2.9.1.2.3.4` renumbered (UUID stable: `fd9aac63…2bd7`)
- `A.2.2.9.1.2.3.5.1.1.1` renumbered (UUID stable: `51f50be4…7571`)
- `A.2.2.9.1.2.3.5.1.1.2` renumbered (UUID stable: `b43edb36…bb2f`)
- `A.2.2.9.1.2.3.5.1.1` renumbered (UUID stable: `c743c744…9421`)
- `A.2.2.9.1.2.3.5.1.2` renumbered (UUID stable: `174e41b1…47c3`)
- `A.2.2.9.1.2.3.5.1` renumbered (UUID stable: `3b38ec56…549c`)
- `A.2.2.9.1.2.3.5.2` renumbered (UUID stable: `d0ceb4ed…2a62`)
- `A.2.2.9.1.2.3.5.3` renumbered (UUID stable: `b593ff77…e804`)
- `A.2.2.9.1.2.3.5.4.1` renumbered (UUID stable: `cc530c80…f4c6`)
- `A.2.2.9.1.2.3.5.4.2` renumbered (UUID stable: `1efa0fc5…c153`)
- `A.2.2.9.1.2.3.5.4` renumbered (UUID stable: `1e95dff0…8650`)
- `A.2.2.9.1.2.3.5` renumbered (UUID stable: `3170b9a1…0ed8`)
- `A.2.2.9.1.2.3.6.1.1.1` renumbered (UUID stable: `03ec388b…8775`)
- `A.2.2.9.1.2.3.6.1.1.2` renumbered (UUID stable: `309ac677…e7a7`)
- `A.2.2.9.1.2.3.6.1.1` renumbered (UUID stable: `9e5fb847…36b7`)
- `A.2.2.9.1.2.3.6.1.2` renumbered (UUID stable: `d7ec33fc…99bc`)
- `A.2.2.9.1.2.3.6.1` renumbered (UUID stable: `005830a0…22ab`)
- `A.2.2.9.1.2.3.6.2` renumbered (UUID stable: `3a23ed21…0f5c`)
- `A.2.2.9.1.2.3.6.3` renumbered (UUID stable: `6eb0901b…4f37`)
- `A.2.2.9.1.2.3.6.4.1.1` renumbered (UUID stable: `4287ecd9…108c`)
- `A.2.2.9.1.2.3.6.4.1.2` renumbered (UUID stable: `1c0708d0…7012`)
- `A.2.2.9.1.2.3.6.4.1` renumbered (UUID stable: `108174f5…1121`)
- `A.2.2.9.1.2.3.6.4.2.1` renumbered (UUID stable: `3401c95d…f676`)
- `A.2.2.9.1.2.3.6.4.2.2` renumbered (UUID stable: `f5b8f596…6c14`)
- `A.2.2.9.1.2.3.6.4.2` renumbered (UUID stable: `8336c1ad…0457`)
- `A.2.2.9.1.2.3.6.4` renumbered (UUID stable: `231e3527…bf76`)
- `A.2.2.9.1.2.3.6` renumbered (UUID stable: `b3ed1e74…d984`)
- `A.2.2.9.1.2.4.1.1.1.1.1` renumbered (UUID stable: `3e14118d…06a9`)
- `A.2.2.9.1.2.4.1.1.1.1.2` renumbered (UUID stable: `351bd87e…4854`)
- `A.2.2.9.1.2.4.1.1.1.1` renumbered (UUID stable: `7a9450db…b4b8`)
- `A.2.2.9.1.2.4.1.1.1.2` renumbered (UUID stable: `dfd59dc4…ff9b`)
- `A.2.2.9.1.2.4.1.1.1` renumbered (UUID stable: `a0a60c30…f4b2`)
- `A.2.2.9.1.2.4.1.1.2` renumbered (UUID stable: `70360ef3…96a1`)
- `A.2.2.9.1.2.4.1.1.3` renumbered (UUID stable: `57921647…0d76`)
- `A.2.2.9.1.2.4.1.1.4.1` renumbered (UUID stable: `34264a04…364a`)
- `A.2.2.9.1.2.4.1.1.4.2` renumbered (UUID stable: `f3ba519f…9b75`)
- `A.2.2.9.1.2.4.1.1.4` renumbered (UUID stable: `082e5d05…c2cc`)
- `A.2.2.9.1.2.4.1.1` renumbered (UUID stable: `27229032…142f`)
- `A.2.2.9.1.2.4.1.2.1.1.1` renumbered (UUID stable: `aa6d4d8e…a55a`)
- `A.2.2.9.1.2.4.1.2.1.1.2` renumbered (UUID stable: `a66e1d9d…c2c9`)
- `A.2.2.9.1.2.4.1.2.1.1` renumbered (UUID stable: `18123d66…8247`)
- `A.2.2.9.1.2.4.1.2.1.2` renumbered (UUID stable: `3741afa3…111b`)
- `A.2.2.9.1.2.4.1.2.1` renumbered (UUID stable: `a24bf9e6…0d77`)
- `A.2.2.9.1.2.4.1.2.2` renumbered (UUID stable: `3373c13d…5359`)
- `A.2.2.9.1.2.4.1.2.3` renumbered (UUID stable: `63ba8de2…f828`)
- `A.2.2.9.1.2.4.1.2.4.1` renumbered (UUID stable: `810220a0…8299`)
- `A.2.2.9.1.2.4.1.2.4.2` renumbered (UUID stable: `ede7410d…cef1`)
- `A.2.2.9.1.2.4.1.2.4` renumbered (UUID stable: `f33e0dee…4739`)
- `A.2.2.9.1.2.4.1.2` renumbered (UUID stable: `ddd65b02…f1b8`)
- `A.2.2.9.1.2.4.1.3.1.1.1` renumbered (UUID stable: `97fba609…8519`)
- `A.2.2.9.1.2.4.1.3.1.1.2` renumbered (UUID stable: `c96dd69d…1579`)
- `A.2.2.9.1.2.4.1.3.1.1` renumbered (UUID stable: `82b72cd2…4ec2`)
- `A.2.2.9.1.2.4.1.3.1.2` renumbered (UUID stable: `db7ad152…1093`)
- `A.2.2.9.1.2.4.1.3.1` renumbered (UUID stable: `e0495e9f…d19a`)
- `A.2.2.9.1.2.4.1.3.2` renumbered (UUID stable: `8b8308fd…e978`)
- `A.2.2.9.1.2.4.1.3.3` renumbered (UUID stable: `b55afaef…ef1c`)
- `A.2.2.9.1.2.4.1.3.4.1` renumbered (UUID stable: `cca17fe9…3690`)
- `A.2.2.9.1.2.4.1.3.4.2` renumbered (UUID stable: `300fca05…d7c3`)
- `A.2.2.9.1.2.4.1.3.4` renumbered (UUID stable: `7cb3c11b…6f51`)
- `A.2.2.9.1.2.4.1.3` renumbered (UUID stable: `dfd65786…0a4f`)
- `A.2.2.9.1.2.4.1.4.1.1.1` renumbered (UUID stable: `b61d8b1d…b855`)
- `A.2.2.9.1.2.4.1.4.1.1.2` renumbered (UUID stable: `c298f200…f42f`)
- `A.2.2.9.1.2.4.1.4.1.1` renumbered (UUID stable: `14d233e1…6e18`)
- `A.2.2.9.1.2.4.1.4.1.2` renumbered (UUID stable: `ae1c6021…4b60`)
- `A.2.2.9.1.2.4.1.4.1` renumbered (UUID stable: `f7bc89b8…f2ce`)
- `A.2.2.9.1.2.4.1.4.2` renumbered (UUID stable: `ffa519f8…d0de`)
- `A.2.2.9.1.2.4.1.4.3` renumbered (UUID stable: `6b90e3a1…f152`)
- `A.2.2.9.1.2.4.1.4.4.1.1` renumbered (UUID stable: `0c619a26…2da6`)
- `A.2.2.9.1.2.4.1.4.4.1` renumbered (UUID stable: `7daf5881…0534`)
- `A.2.2.9.1.2.4.1.4.4.2` renumbered (UUID stable: `594d3b57…cccb`)
- `A.2.2.9.1.2.4.1.4.4` renumbered (UUID stable: `d14fff67…ce8b`)
- `A.2.2.9.1.2.4.1.4` renumbered (UUID stable: `59259360…0f8f`)
- `A.2.2.9.1.2.4.1` renumbered (UUID stable: `c2abdd22…b701`)
- `A.2.2.9.1.2.4.2` renumbered (UUID stable: `e852bd1a…b720`)
- `A.2.2.9.1.2.4.3` renumbered (UUID stable: `81b89dda…8fd3`)
- `A.2.2.9.2.1.1` renumbered (UUID stable: `a9751ac4…e41e`)
- `A.2.2.9.2.1.2` renumbered (UUID stable: `7853b196…280c`)
- `A.2.2.9.2.1.3` renumbered (UUID stable: `71c3bf8e…f45f`)
- `A.2.2.9.2.1` renumbered (UUID stable: `84b4b5c7…a8e9`)
- `A.2.2.9.2.2.1.2.1` renumbered (UUID stable: `6a2ec8d3…9792`)
- `A.2.2.9.2.2.1.2.2` renumbered (UUID stable: `079abfa8…d2dd`)
- `A.2.2.9.2.2.1.2.3` renumbered (UUID stable: `a26ea73f…e63c`)
- `A.2.2.9.2.2.1.2` renumbered (UUID stable: `756b466e…5fe2`)
- `A.2.2.9.2.2.1.3.1` renumbered (UUID stable: `181954b6…b10d`)
- `A.2.2.9.2.2.1.3.2.1` renumbered (UUID stable: `4ab621b4…33c5`)
- `A.2.2.9.2.2.1.3.2.2` renumbered (UUID stable: `787276c9…2986`)
- `A.2.2.9.2.2.1.3.2` renumbered (UUID stable: `e27f2332…056e`)
- `A.2.2.9.2.2.1.3` renumbered (UUID stable: `3b3914d0…a8ac`)
- `A.2.2.9.2.2.1.4.1` renumbered (UUID stable: `a4ca2e70…dbc0`)
- `A.2.2.9.2.2.1.4.2` renumbered (UUID stable: `5828a3a0…c5f5`)
- `A.2.2.9.2.2.1.5.1.0.6.1` renumbered (UUID stable: `8cbff90b…2535`)
- `A.2.2.9.2.2.1.5.1` renumbered (UUID stable: `7ed013c9…5133`)
- `A.2.2.9.2.2.1.5` renumbered (UUID stable: `63ff5ae5…4598`)
- `A.2.2.9.2.2.1` renumbered (UUID stable: `c398b383…2119`)
- `A.2.2.9.2.2.2.1.1.1` renumbered (UUID stable: `7457b041…3acb`)
- `A.2.2.9.2.2.2.1.1.2` renumbered (UUID stable: `a007505e…7588`)
- `A.2.2.9.2.2.2.1.1` renumbered (UUID stable: `ea3fd0be…10b5`)
- `A.2.2.9.2.2.2.1.2` renumbered (UUID stable: `befbf1d8…c96b`)
- `A.2.2.9.2.2.2.1` renumbered (UUID stable: `b68f9009…39a5`)
- `A.2.2.9.2.2.2.2` renumbered (UUID stable: `163b998a…7604`)
- `A.2.2.9.2.2.2.3` renumbered (UUID stable: `5e673229…d9c1`)
- `A.2.2.9.2.2.2.4.1` renumbered (UUID stable: `74f88b57…2e5c`)
- `A.2.2.9.2.2.2.4.2` renumbered (UUID stable: `35c38264…1066`)
- `A.2.2.9.2.2.2.4` renumbered (UUID stable: `9a9b56f4…cb60`)
- `A.2.2.9.2.2.2` renumbered (UUID stable: `4ad2a180…cf52`)
- `A.2.2.9.2.2.3.1.1.1.1` renumbered (UUID stable: `e06ee9c9…994a`)
- `A.2.2.9.2.2.3.1.1.1.2` renumbered (UUID stable: `def2ad89…d722`)
- `A.2.2.9.2.2.3.1.1.1` renumbered (UUID stable: `32cc16f9…1b57`)
- `A.2.2.9.2.2.3.1.1.2` renumbered (UUID stable: `85a0d037…8f60`)
- `A.2.2.9.2.2.3.1.1` renumbered (UUID stable: `2645e2f0…8498`)
- `A.2.2.9.2.2.3.1.2` renumbered (UUID stable: `179cb7a5…c575`)
- `A.2.2.9.2.2.3.1.3` renumbered (UUID stable: `b91d0eb6…af09`)
- `A.2.2.9.2.2.3.1.4.1.1` renumbered (UUID stable: `a227491c…ea7f`)
- `A.2.2.9.2.2.3.1.4.1` renumbered (UUID stable: `991aaf4f…ec0d`)
- `A.2.2.9.2.2.3.1.4.2` renumbered (UUID stable: `d86e5f9f…bc13`)
- `A.2.2.9.2.2.3.1.4` renumbered (UUID stable: `c0e07df6…a639`)
- `A.2.2.9.2.2.3.1` renumbered (UUID stable: `a14cea92…c1f7`)
- `A.2.2.9.2.2.3.2.1.1.1` renumbered (UUID stable: `ff9674e1…539e`)
- `A.2.2.9.2.2.3.2.1.1.2` renumbered (UUID stable: `4290c4b4…b755`)
- `A.2.2.9.2.2.3.2.1.1` renumbered (UUID stable: `cb905fcc…ad7e`)
- `A.2.2.9.2.2.3.2.1.2` renumbered (UUID stable: `921d945d…8045`)
- `A.2.2.9.2.2.3.2.1` renumbered (UUID stable: `ef37ff82…39cb`)
- `A.2.2.9.2.2.3.2.2` renumbered (UUID stable: `0eba9704…f162`)
- `A.2.2.9.2.2.3.2.3` renumbered (UUID stable: `1eafc42a…b317`)
- `A.2.2.9.2.2.3.2.4.1` renumbered (UUID stable: `689a6ce6…4e6b`)
- `A.2.2.9.2.2.3.2.4.2.1` renumbered (UUID stable: `ddcfe438…3823`)
- `A.2.2.9.2.2.3.2.4.2.2` renumbered (UUID stable: `09ddd2c5…9299`)
- `A.2.2.9.2.2.3.2.4.2` renumbered (UUID stable: `22166d2b…a905`)
- `A.2.2.9.2.2.3.2.4` renumbered (UUID stable: `0bce1c09…0584`)
- `A.2.2.9.2.2.3.2` renumbered (UUID stable: `38c54d2b…89a2`)
- `A.2.2.9.2.2.3.3.1.1.1` renumbered (UUID stable: `42848ad7…c46c`)
- `A.2.2.9.2.2.3.3.1.1.2` renumbered (UUID stable: `98b5465e…6410`)
- `A.2.2.9.2.2.3.3.1.1` renumbered (UUID stable: `428d6e85…7ac0`)
- `A.2.2.9.2.2.3.3.1.2` renumbered (UUID stable: `a616c3f6…01e7`)
- `A.2.2.9.2.2.3.3.1` renumbered (UUID stable: `cc3d967c…791d`)
- `A.2.2.9.2.2.3.3.2` renumbered (UUID stable: `c860168e…e0cb`)
- `A.2.2.9.2.2.3.3.3` renumbered (UUID stable: `01214a59…a517`)
- `A.2.2.9.2.2.3.3.4.1` renumbered (UUID stable: `7e4e6528…4f28`)
- `A.2.2.9.2.2.3.3.4.2.1` renumbered (UUID stable: `e7fc7c2e…4e8e`)
- `A.2.2.9.2.2.3.3.4.2` renumbered (UUID stable: `f654be61…b277`)
- `A.2.2.9.2.2.3.3.4` renumbered (UUID stable: `bea2c790…5d26`)
- `A.2.2.9.2.2.3.3` renumbered (UUID stable: `6a8b5e8b…3ebb`)
- `A.2.2.9.2.2.3.4.1.1.1` renumbered (UUID stable: `c3b16255…9203`)
- `A.2.2.9.2.2.3.4.1.1.2` renumbered (UUID stable: `555a08a4…1644`)
- `A.2.2.9.2.2.3.4.1.1` renumbered (UUID stable: `9fa7d744…1bb6`)
- `A.2.2.9.2.2.3.4.1.2` renumbered (UUID stable: `f19c7277…a6a2`)
- `A.2.2.9.2.2.3.4.1` renumbered (UUID stable: `53016a06…f771`)
- `A.2.2.9.2.2.3.4.2` renumbered (UUID stable: `1b0c0956…526c`)
- `A.2.2.9.2.2.3.4.3` renumbered (UUID stable: `7f991abf…d97a`)
- `A.2.2.9.2.2.3.4.4.1` renumbered (UUID stable: `d7e64cf2…3059`)
- `A.2.2.9.2.2.3.4.4.2` renumbered (UUID stable: `d5cce836…76cc`)
- `A.2.2.9.2.2.3.4.4` renumbered (UUID stable: `c7436489…ee99`)
- `A.2.2.9.2.2.3.4` renumbered (UUID stable: `2d1d83ea…3f62`)
- `A.2.2.9.2.2.3.5.1.1.1` renumbered (UUID stable: `c6ad2b62…3e38`)
- `A.2.2.9.2.2.3.5.1.1.2` renumbered (UUID stable: `bac65a98…e4e2`)
- `A.2.2.9.2.2.3.5.1.1` renumbered (UUID stable: `c5db0c30…ca06`)
- `A.2.2.9.2.2.3.5.1.2` renumbered (UUID stable: `bfdafaa4…c569`)
- `A.2.2.9.2.2.3.5.1` renumbered (UUID stable: `e5c0a813…b29f`)
- `A.2.2.9.2.2.3.5.2` renumbered (UUID stable: `185d7f3b…ceab`)
- `A.2.2.9.2.2.3.5.3` renumbered (UUID stable: `d247fec5…8d64`)
- `A.2.2.9.2.2.3.5.4.1` renumbered (UUID stable: `43a3722c…d365`)
- `A.2.2.9.2.2.3.5.4.2` renumbered (UUID stable: `adfb66a3…187c`)
- `A.2.2.9.2.2.3.5.4` renumbered (UUID stable: `bae40b55…7671`)
- `A.2.2.9.2.2.3.5` renumbered (UUID stable: `24fa76f6…c2ac`)
- `A.2.2.9.2.2.3.6.1.1.1` renumbered (UUID stable: `95379a19…ab85`)
- `A.2.2.9.2.2.3.6.1.1.2` renumbered (UUID stable: `97e2c2b5…bd39`)
- `A.2.2.9.2.2.3.6.1.1` renumbered (UUID stable: `7ff087ca…22bc`)
- `A.2.2.9.2.2.3.6.1.2` renumbered (UUID stable: `1c0ce5c0…87f6`)
- `A.2.2.9.2.2.3.6.1` renumbered (UUID stable: `59306024…ff8e`)
- `A.2.2.9.2.2.3.6.2` renumbered (UUID stable: `48863e96…4098`)
- `A.2.2.9.2.2.3.6.3` renumbered (UUID stable: `51ca2399…0d13`)
- `A.2.2.9.2.2.3.6.4.1.1` renumbered (UUID stable: `847092ba…c480`)
- `A.2.2.9.2.2.3.6.4.1.2` renumbered (UUID stable: `1b03bc85…c379`)
- `A.2.2.9.2.2.3.6.4.1` renumbered (UUID stable: `221cde4c…5646`)
- `A.2.2.9.2.2.3.6.4.2.1` renumbered (UUID stable: `f4323202…9dce`)
- `A.2.2.9.2.2.3.6.4.2` renumbered (UUID stable: `1ba7ea74…746b`)
- `A.2.2.9.2.2.3.6.4` renumbered (UUID stable: `bd74388f…5806`)
- `A.2.2.9.2.2.3.6` renumbered (UUID stable: `182ca3dc…125b`)
- `A.2.2.9.2.2.3` renumbered (UUID stable: `a1dc075e…a2fa`)
- `A.2.2.9.2.2.4.1.1.1.1.1` renumbered (UUID stable: `56e6b01b…cb70`)
- `A.2.2.9.2.2.4.1.1.1.1.2` renumbered (UUID stable: `fa1e98b5…e35a`)
- `A.2.2.9.2.2.4.1.1.1.1` renumbered (UUID stable: `52fc6ecc…0f22`)
- `A.2.2.9.2.2.4.1.1.1.2` renumbered (UUID stable: `f8991663…8ee8`)
- `A.2.2.9.2.2.4.1.1.1` renumbered (UUID stable: `0930f2b1…b0cb`)
- `A.2.2.9.2.2.4.1.1.2` renumbered (UUID stable: `fa744d67…3d4d`)
- `A.2.2.9.2.2.4.1.1.3` renumbered (UUID stable: `4c84f0a6…dfcc`)
- `A.2.2.9.2.2.4.1.1.4.1` renumbered (UUID stable: `273db3f1…2bbd`)
- `A.2.2.9.2.2.4.1.1.4.2` renumbered (UUID stable: `b785cb0c…6977`)
- `A.2.2.9.2.2.4.1.1.4` renumbered (UUID stable: `08dd7788…c69f`)
- `A.2.2.9.2.2.4.1.1` renumbered (UUID stable: `780719e8…83df`)
- `A.2.2.9.2.2.4.1.2.1.1.1` renumbered (UUID stable: `9c5455f3…779c`)
- `A.2.2.9.2.2.4.1.2.1.1.2` renumbered (UUID stable: `358d4696…d3bb`)
- `A.2.2.9.2.2.4.1.2.1.1` renumbered (UUID stable: `fd914a13…d1fa`)
- `A.2.2.9.2.2.4.1.2.1.2` renumbered (UUID stable: `5cae5183…2fe6`)
- `A.2.2.9.2.2.4.1.2.1` renumbered (UUID stable: `c12533a4…b95b`)
- `A.2.2.9.2.2.4.1.2.2` renumbered (UUID stable: `f894a7d2…b535`)
- `A.2.2.9.2.2.4.1.2.3` renumbered (UUID stable: `862aff47…9e83`)
- `A.2.2.9.2.2.4.1.2.4.1` renumbered (UUID stable: `7e7e516a…b48d`)
- `A.2.2.9.2.2.4.1.2.4.2` renumbered (UUID stable: `f1e0fb16…2979`)
- `A.2.2.9.2.2.4.1.2.4` renumbered (UUID stable: `baa296a6…a9bc`)
- `A.2.2.9.2.2.4.1.2` renumbered (UUID stable: `16474cb5…cc2b`)
- `A.2.2.9.2.2.4.1.3.1.1.1` renumbered (UUID stable: `44fb9520…a765`)
- `A.2.2.9.2.2.4.1.3.1.1.2` renumbered (UUID stable: `30152570…00f4`)
- `A.2.2.9.2.2.4.1.3.1.1` renumbered (UUID stable: `7ba12eff…f982`)
- `A.2.2.9.2.2.4.1.3.1.2` renumbered (UUID stable: `8f3b3d8b…d9b2`)
- `A.2.2.9.2.2.4.1.3.1` renumbered (UUID stable: `0f8e3d69…9fb0`)
- `A.2.2.9.2.2.4.1.3.2` renumbered (UUID stable: `841497f9…8d4a`)
- `A.2.2.9.2.2.4.1.3.3` renumbered (UUID stable: `ebbfa305…bb2f`)
- `A.2.2.9.2.2.4.1.3.4.1.1` renumbered (UUID stable: `0f50e796…0307`)
- `A.2.2.9.2.2.4.1.3.4.1` renumbered (UUID stable: `1f50ce0e…c017`)
- `A.2.2.9.2.2.4.1.3.4.2` renumbered (UUID stable: `43aedc35…ea0b`)
- `A.2.2.9.2.2.4.1.3.4` renumbered (UUID stable: `5a0f038c…77a3`)
- `A.2.2.9.2.2.4.1.3` renumbered (UUID stable: `d9c13a1a…0717`)
- `A.2.2.9.2.2.4.1.4.1.1.1` renumbered (UUID stable: `fa1aab6f…ce29`)
- `A.2.2.9.2.2.4.1.4.1.1.2` renumbered (UUID stable: `ee6adeb0…0074`)
- `A.2.2.9.2.2.4.1.4.1.1` renumbered (UUID stable: `dea4f41d…ab7a`)
- `A.2.2.9.2.2.4.1.4.1.2` renumbered (UUID stable: `10cb9c97…aded`)
- `A.2.2.9.2.2.4.1.4.1` renumbered (UUID stable: `6dac32e6…68ca`)
- `A.2.2.9.2.2.4.1.4.2` renumbered (UUID stable: `9cb825c8…4d26`)
- `A.2.2.9.2.2.4.1.4.3` renumbered (UUID stable: `f54de74a…9a0d`)
- `A.2.2.9.2.2.4.1.4.4.1.1` renumbered (UUID stable: `0ab76a83…0970`)
- `A.2.2.9.2.2.4.1.4.4.1` renumbered (UUID stable: `9478c3d6…45e1`)
- `A.2.2.9.2.2.4.1.4.4.2` renumbered (UUID stable: `39aba7ed…b218`)
- `A.2.2.9.2.2.4.1.4.4` renumbered (UUID stable: `8d00d8df…9e2b`)
- `A.2.2.9.2.2.4.1.4` renumbered (UUID stable: `c40a0708…9455`)
- `A.2.2.9.2.2.4.1` renumbered (UUID stable: `04864587…85a4`)
- `A.2.2.9.2.2.4.2` renumbered (UUID stable: `9cdac621…c27d`)
- `A.2.2.9.2.2.4.3` renumbered (UUID stable: `0bbeab5f…7a0c`)
- `A.2.2.9.2.2.4` renumbered (UUID stable: `805381e5…31ba`)
- `A.2.2.9.2.2` renumbered (UUID stable: `eecfa6ad…484b`)
- `A.2.2.9.3.1.1` renumbered (UUID stable: `219459b3…6dbb`)
- `A.2.2.9.3.1.2.1.0.6.1` renumbered (UUID stable: `f2ecf6a4…f82e`)
- `A.2.2.9.3.1.2.1` renumbered (UUID stable: `65fc0b79…1069`)
- `A.2.2.9.3.1.2` renumbered (UUID stable: `d6d16076…486c`)
- `A.2.2.9.3.1.3.1` renumbered (UUID stable: `0c7b0644…15e4`)
- `A.2.2.9.3.1.3` renumbered (UUID stable: `f0d5ab5e…e604`)
- `A.2.2.9.3.1.4.1` renumbered (UUID stable: `15e14f25…03c5`)
- `A.2.2.9.3.1.4` renumbered (UUID stable: `04edac33…7771`)
- `A.2.2.9.3.1` renumbered (UUID stable: `4aab68fd…22fa`)
- `5` → `6` across 27 docs.
- `9` → `10` across 65 docs.
- `makerdao` → `sky/scope` across 3 docs.
- `10` → `11` across 8 docs.
- `8.1.2.1` → `4` across 6 docs.
- `8` → `9` across 335 docs.
- `6` → `4` across 13 docs.
- `8` → `4` across 16 docs.
- `1.2.1.4` → `3` across 16 docs.
- `Executor Accord` → `Agent Creation` across 9 docs.
- `4` → `5` across 19 docs.
- `Root Edit` → `Prime Transformation` across 9 docs.
- `7` → `8` across 12 docs.
- `Allocation System` → `Distribution Reward` across 4 docs.
- `2` → `1` across 10 docs.
- `3` → `2` across 6 docs.
- `5` → `3` across 6 docs.
- `7` → `5` across 4 docs.
- `6` → `7` across 1 doc.

### Context
Unifies reward recipient and sharing across Sky Primitive reward mechanisms — all payments route to the Prime Agent managing the Integrator relationship, with sharing bilaterally negotiated — which drives the large structural renumbering of the Support Scope primitive tree (most additions/deletions are relocations within the reorg, not net-new mechanisms). Also rebrands Immunefi bug-bounty URLs (makerdao → sky).

---

## PR #251 — Atlas Edit Proposal — 2026-05-25
**Merged:** 2026-05-29 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core A.2.2.5.2.3.1.1 deleted: Publicly Held Definition** (UUID `d6265f88…5718`)
- **Core A.2.8.2.2.2.1.5 deleted: Minimum Float** (UUID `3918317d…a6b5`)
- **Limitations On Usage Of Root Edit Primitive Prior To Independent Governance** (`A.2.2.5.2.3.1`): `457b` → `4842`; `8958` → `9767`

### Housekeeping
- `A.2.10.1.5.3` (Approval Process): `Support` → `Core`
- `A.2.11.1.1.2.1` (Assets In Scope): `Support Facilitator` → `Protocol Security Workstream Lead`
- `A.2.11.1.1.2.2` (Severity Classification): `Support Facilitator` → `Protocol Security Workstream Lead`
- `A.2.8.2.2.2.4.5.2.1` (Grove Foundation Grant Authorization: Q2 2026): added `Multisig`
- `A.2.8.2.2.2.4.5` (Subsequent Allocation Mechanism): `Tokens Being Publicly Held` → `Independent Governance`
- `A.2.9.1.1.1.1` (Resilience Fund Budget): `Support` → `Core`
- `A.2.9.1.1.1.2.1` (Resilience Fund Technical Committee Selection And Compensation): `Support` → `Core`
- `A.2.9.1.1.1.4.2.2.1` (Resilience Fund Claim Approval Payout Claim): `Support` → `Core`
- `Support Facilitators` → `Core Facilitator` across 12 docs.
- `Support` → `Core` across 4 docs.

### Context
Part of the protocol-wide Support/Stability Facilitator → Core Facilitator consolidation running across this edit. The deleted "Publicly Held Definition" and "Minimum Float" docs are superseded by the new Independent Governance definition (A.0.1.1.54), which the subsequent-allocation mechanism now keys off.

---

## PR #246 — Atlas Edit Proposal — 2026-05-18
**Merged:** 2026-05-21 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- `A.2.2.8.3.1.2.1.0.6.1` (List of Active Pioneer Primes): `Launch Agent 6` → `Osero`
- `A.2.8.2.6.1.1.2` (Osero Details): `Launch Agent 6` → `Osero`
- `A.2.8.2.6.1.1` (Parties To The Accord): `Launch Agent 6` → `Osero`
- `A.2.8.2.6.2.1.1` (Total Token Supply): `AGENT6` → `OSERO`
- `A.2.8.2.6.2.1.2.1` (Osero Prime Treasury): `Launch Agent 6` → `Osero`
- `A.2.8.2.6.2.1.2.2` (Sky Retained Tokens And Reward Pools): `AGENT6` → `OSERO`
- `A.2.8.2.6.2.2.1` (Osero Initial Allocation): `Launch Agent 6` → `Osero`
- `A.2.8.2.6.2.2.2.1` (Transfer Of Genesis Capital Allocation To Osero Foundation): `Launch Agent 6` → `Osero`
- `A.2.8.2.6.2.2.2.2` (Transfer Of Genesis Capital Allocation To Osero SubProxy): `Launch Agent 6` → `Osero`
- `A.2.8.2.6.2.2.2` (Initial Allocation Distribution): `Launch Agent 6` → `Osero`
- `A.2.8.2.6` (Ecosystem Accord 6: Sky And Osero): `Launch Agent 6` → `Osero`
- `A.2.8.2.7` (Ecosystem Accord 7: Sky And Skybase): `and` → `And`
- `Launch Agent 6` → `Osero` across 9 docs.
- `AGENT6` → `OSERO` across 3 docs.

### Context
Public-name reveal for Launch Agent 6 (now Osero); Ecosystem Accord 6 retitled and all party, treasury, and Pioneer Prime references updated. Ratified by Poll #1633 (10-0, non-voters: axislegati, excel, opex).

---

## PR #242 — Atlas Edit Proposal — 2026-05-11
**Merged:** 2026-05-15 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: Agent Termination Process** (`A.2.2.5.2.2.2.8.1`, UUID `82f9f4b9…3b75`): The Agent Termination Process, as specified in `A.1.14.5`, deviates from the general Artifact Edit Process and follows the special voting process specified in the documents.
  - **Voting Period** (`A.2.2.5.2.2.2.8.1.1`): The Root Edit Primitive must specify a voting period of at least 14 days.
  - **Quorum Requirement** (`A.2.2.5.2.2.2.8.1.2`): The Root Edit Primitive must specify a minimum quorum of at least 20% of outstanding tokens.
  - **Approval Threshold** (`A.2.2.5.2.2.2.8.1.3`): The Root Edit Primitive must specify a supermajority approval threshold where at least two-thirds (2/3) of votes cast are in favor.
  - **Required Notice** (`A.2.2.5.2.2.2.8.1.4`): The Root Edit Primitive must require the Operational Facilitator to issue advance notice of the Agent's proposed termination and the subsequent Agent vote in the Sky Forum.
  - **Compliance Deadline For Existing Prime Agents** (`A.2.2.5.2.2.2.8.1.5`): Existing Prime Agents whose Root Edit Primitive does not already incorporate the requirements specified in `A.2.2.5.2.2.2.8.1` must update their Agent Artifact to include the.
- **New: Short Term SKY Staking Rewards Rate** (`A.2.3.1.4.1`, UUID `de233df4…dd3c`): Pending activation of the USDS Staking Rewards specified in `A.2.3.1.2.4`, no Step 4 Capital is allocated to SKY Staking Rewards.
- **Included In An Executive Vote** (`A.2.10.1.5.3.0.3.1`): `10` → `11`
- **Emergency Communication Readiness Requirement** (`A.2.11.1.3.2.1.1.6.3`): `8` → `9`
- **Core GovOps Validates Executor Accord Primitive Inputs** (`A.2.2.1.1.13`): `13` → `14`
- **Short Term Suspension of “Founder Access”** (`A.2.2.1.1.3.2.1`): `10` → `11`; `11` → `12`
- **Prohibition On Deactivating Executor Accord And Root Edit Primitives** (`A.2.2.1.2.4.2.1.2`): `13` → `14`
- **Changing Primitive Instance Status** (`A.2.2.1.3.3`): `13` → `14`
- **Agent Inputs** (`A.2.2.5.2.1.1.1`): `13` → `14`
- **Limitations On Usage Of Root Edit Primitive Prior To Tokens Being Publicly Held** (`A.2.2.5.2.3.1`): `10` → `11`; `11` → `12`
- **Atlas Edit Proposal Process For Prime Agents** (`A.2.2.5.2.3.2`): `10` → `11`
- **Instance Setup Deployments** (`A.2.2.9.1.1.2.3`): `9` → `10`
- **Operationalization Of Allocation Instances** (`A.2.2.9.1.1.3.1`): `13` → `14`

### Housekeeping
- `A.2.11.1.3.2.2.1.1.1` (Signer Rotation Requirement): `Core GovOps` → `the Protocol Security Workstream Lead`
- `A.2.11.1.3.2.2.1.1.2` (Signer Composition Documentation Requirement): `Core GovOps` → `the Protocol Security Workstream Lead`
- `A.2.11.1.3.2.2.1.1.3` (Threshold Preservation Requirement): `Core GovOps` → `the Protocol Security Workstream Lead`
- `A.2.8.2.5.2.2.2` (Use Of Genesis Capital): `spell` → `Spell`
- `A.2.9.1.1.1.4.1.6` (Resilience Fund Approval Process And Verifiability): `spell` → `Spell`
- `9` → `10` across 1 doc.
- `spell` → `Spell` across 2 docs.
- `8` → `9` across 1 doc.
- `10` → `11` across 4 docs.
- `11` → `12` across 2 docs.
- `13` → `14` across 5 docs.
- `Core GovOps` → `the Protocol Security Workstream Lead` across 3 docs.

### Context
Three substantive support-scope additions from the May 11 weekly cycle (Poll #1632): a special-voting Agent Termination Process all Prime Agents must incorporate into their Root Edit Primitive by Sep 1, 2026 (14-day vote, 20% quorum, 2/3 approval); restoration of the Short Term SKY Staking Rewards rate at 50% of Step 2 Capital (A.2.3.1.4.1); and rerouting signer-rotation notifications and threshold-reduction approvals from Core GovOps to the Protocol Security Workstream Lead.

---

## PR #237 — Atlas Edit Proposal — 2026-05-04
**Merged:** 2026-05-08 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: Ecosystem Accord 10 — Sky and Grove** (`A.2.8.2.10`, UUID `0cb00b28…dc97`): formalizes ongoing compensation to Grove for the Chronicle Point Reward Instance — the mainnet `StakingRewards` contract at the Chainlog `REWARDS_USDS_01` key, into which USDS is deposited to accrue Chronicle Points.
  - **Compensation formula**: `USDS_Deposited × 20% × Base_Rate` (Base Rate per `A.3.1.2.1`, UUID `228f9955…00b9`); accrues continuously, sub-period proration when USDS deposited or Base Rate changes
  - **Settlement**: monthly via the Monthly Settlement Cycle, `Σ(USDS_Deposited × 0.20 × Base_Rate / 365 × Sub-Period_Days)`
  - **Duration**: indefinite, retroactive commencement 2025-07-24; modifiable only via Atlas Edit
  - **Retroactive compensation**: 2025-07-24 → 2026-03-31, settled in the April 2026 MSC
  - **Parties**: Sky (= Sky Core) and Grove (= Grove Prime Agent + Grove Foundation)

### Housekeeping
- Removed broken `A.5.5.1.1` cross-references from Legacy Accounts (`A.2.3.1.2.2.2.1.6.1`) and the two Spark Liquidity Bootstrapping transfer records (`A.2.8.2.2.2.7.4.1`, `A.2.8.2.2.2.7.4.2`) — cleanup paired with the deletion of Article `A.5.5` (see `A.5--accessibility/changelog.md`).

### Context
First non-foundational Ecosystem Accord added since the Atlas onboarding wave; ratified by Poll #1631 (10-0, non-voters: excel, opex, tango). Pegs Grove's compensation directly to Sky's monetary policy lever — the Base Rate — so payouts scale automatically with USDS deposits in the Chronicle Point Reward Instance and with future SSR/Base Rate adjustments. The retroactive 8-month window (Jul 2025 – Mar 2026) means the April 2026 MSC will carry a one-time catch-up payment in addition to the recurring monthly accrual.

---

## PR #227 — Atlas Edit Proposal — 2026-04-27
**Merged:** 2026-04-30 | **Type:** Weekly edit (Atlas Axis — Poll #1630)

### Material Changes
- **TMF Step 1 restructured** (`A.2.3.1.2.2`, UUID `324e9d22…`): "Security and Stability Maintenance" → "Security and Maintenance"; allocation expanded from **10% to 20%** of Net Revenue, now split as:
  - 10% → **Fortification Foundation Allocation** (`A.2.3.1.2.2.1`, new): legal defense, resilience, unquantifiable risk, protocol development; interim: may flow to Sky Frontier Foundation
  - 10% → **Core Council Allocation** (`A.2.3.1.2.2.2`, new): unified allocation for Core Executors (active + retired), Aligned Delegates, Governance Accessibility Rewards, Sky Frontier Foundation grants; discretionary split via Core Council Buffer and AD Buffer
- **TMF Step 2 replaced** with **Aggregate Backstop Capital** (`A.2.3.1.2.3`, UUID `2b28d464…`): replaces HASR buffer + Stability Capital Retention formula. Dynamic ABC retention:
  - ABC < Turbo-Fill Floor (150M): retain 50% of Step 2 Capital
  - ABC between Turbo-Fill Floor and Target (1.5% of USDS supply): retain 50% × (1 − ABC/Target)
  - ABC ≥ Target: 0% retained; all flows to Step 3
- **TMF Step 3 replaced** with **Smart Burn Engine** (`A.2.3.1.2.4`, UUID `5ce73730…`): Step 3 Capital allocated as 45% SKY buyback→stakers, 45% USDS staking rewards, 10% SKY buyback→burned
- **TMF Step 4 simplified** to **Staking Rewards** (`A.2.3.1.2.5`, UUID `bb163691…`): distributes USDS and SKY staking rewards produced in Step 3
- **Transitionary framework retired** (`A.2.3.1.4` deleted): entire Stage 0/1/2 Step 4 allocation structure removed; HASR/SASR activity-tier buffers deleted; SCR/Stability Capital Buffer formula deleted; ISRC sourcing updated to flow from Aggregate Backstop Capital (100% above Target ABC + 1/3 up to Target ABC)
- **Authorized Forum Accounts Requirements** (`A.2.7.1.1.1.1`, UUID `a76f81b5…`): new section requiring governance-capacity forum accounts to register entity handle and authorized representatives; unregistered accounts may be disregarded for governance purposes. Initial registry: 16 entities (Pattern, Redline, BA Labs, Spark, Obex, Grove, Soter Labs, Amatsu, Dewiz, Atlas Axis, Ozone, Endgame Edge, Keel, Sidestream, JanSky, Rune). See `A.2.7.1.1.1.1--forum-accounts/changelog.md` for the canonical baseline and future registry mutations (Active Data, edited via Direct Edit between weekly cycles).
- **Grove Foundation Grant Authorization Q2 2026** (`A.2.8.2.2.2.4.5.2.1`, UUID `85f7d545…`): **800,000 USDS/month** from Grove's Prime Treasury for 3 months (Q2 2026). Recipient: Grove Foundation at `0xE3EC4CC359E68c9dCE15Bf667b1aD37Df54a5a42`

### Housekeeping
- ISRC sourcing section renamed: `A.2.3.1.3` "Sourcing Of Internal Senior Risk Capital From Surplus Buffers" → "Sourcing Of Internal Senior Risk Capital"; definition updated to cite ABC as source
- Core Governance Reward Primitive: funding source clarified as Core Council Allocation; retroactive effective date May 19, 2025; accrued undisbursed amounts funded from Core Council Buffer
- Spark Foundation grant authorizations reorganized into `A.2.8.2.2.2.4.5.1.x` nested hierarchy; Grove Foundation grants added at `A.2.8.2.2.2.4.5.2`
- Cross-references throughout updated from old transitionary paths (`A.2.3.1.4.1.x`, `A.2.3.1.4.2`) to new permanent TMF step paths (`A.2.3.1.2.2.x`, `A.2.3.1.2.4`, `A.2.3.1.2.5`)

### Context
The largest TMF restructuring since the framework launched. The old transitionary framework (Stage 0/1/2 for Step 4 allocation, activity-tier staking buffers, SCR formula) is retired and replaced with a permanent architecture. Key shifts: (1) Step 1 explicitly allocates 10% to the Fortification Foundation, formalizing a legal/security reserve; (2) ABC growth is baked into Step 2 rather than being a separate governance action; (3) staking rewards (USDS and SKY) integrate directly into TMF Steps 3–4 rather than running as parallel vesting streams. USDS supply ~$10.5B at merge.

---

## PR #224 — Atlas Edit Proposal — 2026-04-20
**Merged:** 2026-04-24 | **Type:** Weekly edit (Atlas Axis — Poll #1629)

### Material Changes
- **Multisig Security Enforcement Framework** (`A.2.11.1.3`): new comprehensive section governing multisig setup, ongoing management, incident reporting, and compliance across Sky Core and Prime Agent infrastructure, effective May 20, 2026. Key requirements: smart contract control multisigs should target 7/9 supermajority where feasible; high-value asset multisigs have explicit minimum thresholds; periodic review, incident reporting obligations, and noncompliance enforcement; Multisig Registry (`A.2.11.1.3.4`) with Active Data Controller designation
- **Ecosystem Upkeep Fee Primitive** replaces split Distribution Requirement / Market Cap Fee structure: all Prime Agents now pay a uniform **50 bps/year** of market cap in USDS (previously 0.30% Market Cap Fee or 0.25% annual token buyback/distribution); Ecosystem Accord special upkeep logic removed; Distribution Requirement Primitive deleted, Market Cap Fee renamed to Ecosystem Upkeep Fee
- **Loss Absorption Sequence** reordered: Genesis Capital Backstop now applied **before** SKY Backstop (previously SKY came first); Genesis Capital Backstop trigger conditions revised accordingly
- **Pioneer Incentive Pool split removed**: Pioneer Prime retains **100%** of Pioneer Incentive Pool (previously 80% mandated for third-party USDS adoption incentives, 20% retained)
- **Prime Agent Data Production Responsibilities** clarified: Prime Agents explicitly responsible for data production and Risk Capital inputs

### Housekeeping
- Agent creation process updated: "Founder Must Globally Activate Distribution Requirement And/Or Market Cap Fee Primitive" step removed; Ecosystem Upkeep Fee Primitive now required; prohibition on deactivating both primitives simplified to single prohibition on deactivating Ecosystem Upkeep Fee Primitive.

### Context
The most consequential governance-fee change since agents launched: uniform 50 bps replaces agent-choice between 30 bps Market Cap Fee and 25 bps token distribution. The Genesis Capital Backstop priority change is material for loss-absorption ordering. The Pioneer Incentive Pool change directly affects how Launch Agent 6 can deploy Plasma incentive funds. Poll #1629 passed (non-voters: axislegati, brendan-navigator, excel, opex).

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

## PR #208 — Atlas Edit Proposal — 2026-03-23
**Merged:** 2026-03-27 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Spark Foundation Grant Authorization: Q2 2026** (`A.2.8.2.2.2.5.5.3` — new): Sky Governance authorises 1,100,000 USDS/month to the Spark Foundation from the SubDAO Proxy for Q2 2026 (3 months), plus 100,000 USDS/month to the Spark Asset Foundation for Q2 2026. Forum: https://forum.skyeco.com/t/march-26-2026-proposed-changes-to-spark-for-upcoming-spell/27770

### Housekeeping
- Multiple forum links across A.2 updated from `forum.sky.money` → `forum.skyeco.com` (including Ecosystem Accord dispute reference at `A.2.8.1.2`; Spark Foundation Q1 2026 grant at `A.2.8.2.2.2.5.5.2`; Grove RWA Conduit at `A.6.1.1.2.3.2.2`).

---

## PR #200 — 2026-03-16 Weekly Edit Proposal
**Merged:** 2026-03-20 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Keel Genesis Capital Allocation** (`A.2.8.2.3.2.5`): new — **10,000,000 USDS** to be transferred in Mar 26, 2026 Executive Vote; SubProxy address at `A.6.1.1.3.2.1.1.3.1.1.2`.
- **Keel Tokenomics** (`A.2.8.2.3.2.4`): new placeholder — "will be specified in a future iteration."
- **Launch Agent 6 (Osero) Genesis Capital Transfer** (`A.2.8.2.6.2.2.2.2`): "future Executive Vote, contingent on future agreement" → Mar 26, 2026 Executive Vote; SubProxy address added: `0x24fdcd3bFA5C2553e05B2f9AD0365EBC296278D3`.
- **Ecosystem Accord 8: Sky And Amatsu** (`A.2.8.2.8`): new accord record. Genesis Capital Allocation: **25,000,000 USDS**, Mar 26, 2026 Executive Vote; SubProxy address TBD via Technical Scope Forum Post. Indefinite duration, commencing 2026-03-19.
- **Ecosystem Accord 9: Sky And Ozone** (`A.2.8.2.9`): new accord record. Genesis Capital Allocation: **25,000,000 USDS**, Mar 26, 2026 Executive Vote; SubProxy address TBD via Technical Scope Forum Post. Indefinite duration, commencing 2026-03-19.

### Context
Sets up the Mar 26, 2026 Executive Vote framework for four Genesis Capital transfers: Keel (10M USDS), Launch Agent 6/Osero (10M USDS), Amatsu (25M USDS), and Ozone (25M USDS). Ecosystem Accords 8 and 9 formalize Amatsu and Ozone as Operational Executor Agents.

---

## PR #187 — 2026-02-23 Atlas Edit Weekly Cycle Proposal
**Merged:** 2026-03-05 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Distribution Reward** (`A.2.2.8.1.2.1.4.3.1`): "Amatsu calculates" → "Denna Labs calculates" (same as PR #180 — confirms Denna Labs is the new calculator).
- **SKY Buybacks allocation** (`A.2.3.1.4.2.1`): 300,000 USDS/day → **37,600 USDS/day** of Step 4 Capital.
- **Safe Harbor agreement address** (`A.2.11.1.2.1`, `A.2.11.1.2.2.2`): `0x9E5Cf4a9C806fE1F4392788b21342a442E14Cc20` → `0xf17bB418B4EC251f300Aa3517Cb37349f17697A1`.
- **Safe Harbor protocol name** (`A.2.11.1.2.2.3.5`): "Sky Ecosystem" → "Sky."
- **RRC Dashboard/API** (`A.2.2.9.1.1.3.2.1.1`): renamed "Dashboard And API" → "Dashboard"; Blockanalitica URL removed; URL updated to `https://info.sky.money/required-risk-capital`.

### Housekeeping
- Link-text fixes across A.2.2.9, A.2.2.10; whitespace and markdown list normalization.

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

## PR #180 — Feb 9 edit
**Merged:** 2026-02-12 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Amatsu Distribution Reward** (`A.2.2.8.1.2.1.4.3.1`): "Amatsu calculates the Distribution Reward" → "Denna Labs calculates the Distribution Reward."
- **Core Governance Reward recipients** (`A.2.2.10.1.2.1`): Skybase entry reformatted with bold name (no substantive change).
- **Grove Token Generation Event** added: first date SKY Staking users can earn GROVE Token Rewards; cross-referenced to `A.4.4.1`.
- **Token Launch Penalty Settlement** (`A.2.8.2.2.2.8.1.2`): new section added — penalty paid at last Capital Transfer to a Genesis Agent.
- **Ecosystem Accord 7** (`A.2.8.2.7.x`): minor whitespace/punctuation corrections.
- **Safe Harbor chains parameter** (`A.2.11.1.2.2.3.3`): chain list replaced by reference to subdocuments.
- **A.2.3.1.4.1.1.1.6.3 → .6.4** renumbering (section header shift, UUID preserved).

### Housekeeping
- Trailing double-space removal across A.2.2.10 subsections; minor link-text fixes.

---

## PR #172 — Jan 26 Edit
**Merged:** 2026-01-29 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Monthly Settlement Cycle — Independent Calculation** (`A.2.4.1.2.1.2.2`): Core Council Risk Advisor calculation must now also include amounts for Core Council and Aligned Delegates Buffers per `A.2.3.1.4.1`.
- **Monthly Settlement Cycle — Final Calculation** (`A.2.4.1.2.1.3`): Same addition — Final Calculation must include final amounts for CC/AD Buffers.
- **Launch Agent 6 Prime Treasury** (`A.2.8.2.6.2.1.2.1`): 777,777,778 → **677,777,778 AGENT6** to Prime Treasury; 100M AGENT6 earmarked for incentives.
- **Sky Retained Tokens (Launch Agent 6)** (`A.2.8.2.6.2.1.2.2`): 222,222,222 → **322,222,222 AGENT6** retained by Sky.
- **Launch Agent 6 Initial Allocation** (`A.2.8.2.6.2.2.1`): 10,000,000 → **10,500,000 USDS**.
- **Transfer of Genesis Capital — LA6 Foundation** (`A.2.8.2.6.2.2.2.1`, renamed + new UUID `4fd99f26…`): Records transfer of 500,000 USDS from Core Council Buffer to Launch Agent 6 Foundation (`0xfDD0…3CC58`).
- **Transfer of Genesis Capital — LA6 SubProxy** (`A.2.8.2.6.2.2.2.2`, new): New sub-doc added.
- **Transfer of Genesis Capital — USDS Demand Multisig** (`A.2.8.2.7.2.2.2.2`, new): 5,000,000 USDS from Surplus Buffer to USDS Demand Subsidies Multisig to be included in January 29, 2026 Executive Vote; no prior Governance Poll required.

### Context
Ecosystem Accord 6 (Osero) cross-referenced — see Osero changelog. The LA6 AGENT6 reallocation (100M to incentives) comes with a proportional increase in Sky's retained share.

---

## PR #156 — January 12 edit
**Merged:** 2026-01-19 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **"Accessibility Reward" renamed to "Distribution Reward"** (`A.2.9.2.2.2.3`, `A.2.3.8.1.2.1.6.1.0.6.1`, `A.2.3.8.2.2.1.4.1`): global rename of the reward type across all references.
- **Grove Token Reward Distribution Schedule** (`A.2.9.2.2.2.1.2.2.1`): Fixed annual schedule table removed; replaced with "distributed over time as determined by Sky Governance."
- **SPK Token Reward Distribution Schedule** (`A.2.9.2.2.2.1.2.2.2`): Fixed table retained for USDS-user tranche; text updated to note all other SPK reserved for future rewards at governance discretion.
- **Subsequent Allocation Mechanism** (`A.2.9.2.2.2.5.5`): Condition "before SPK/GROVE decentralized enough" removed; now grants are subject to the Root Edit Primitive limitations at `A.2.3.5.2.3.1`.
- **Spark Foundation Grant Authorization: October 2025** (`A.2.9.2.2.2.5.5.1`): Renamed (new UUID `12425328…`); framing updated to historical.
- **Spark Foundation Grant Authorization: December 2025** (`A.2.9.2.2.2.5.5.2`, new): 1,100,000 USDS/month Q1 2026 from SubDAO Proxy + 150,000 USDS one-time for Spark Asset Foundation Q1 2026 expenses; Sky Governance consent recorded.

### Context
The removal of the fixed GROVE distribution schedule and relaxation of the subsequent-grant trigger condition are significant — governance no longer commits to a multi-year token emission table for GROVE.

---

## PR #143 — 2025-12-15 Edit
**Merged:** 2026-01-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core Council Buffer multisig** (`A.2.4.1.4.1.1.1.2–.3`):
  - Signing requirement: **4/6 → 5/6**
  - Signers revised: CF (×2) + GovOps (**×3**) + Soter Labs (×1) — Amatsu removed vs. Dec 8 edit
- **Keel Senior Risk Capital** (`A.2.9.2.3.2.3`): 7.5 million USDS short-term Senior Risk Capital for Keel (credited to TRC, not transferred)
- **Ecosystem Accord 6: Sky and Launch Agent 6** (`A.2.9.2.6`) — accord terms added: AGENT6 total supply 1B, LA6 Prime Treasury 777.8M, Sky retained 222.2M; Initial Allocation 10M USDS to LA6 SubProxy (contingent on future agreement); duration indefinite from 2025-12-18

---

## PR #141 — Dec 8 edit
**Merged:** 2025-12-11 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Core Council Buffer multisig** (`A.2.4.1.4.1.1.1`):
  - Signing requirement: **3/4 → 4/6**
  - Signers expanded from CF (×2) + GovOps (×2) to CF (×2) + GovOps (×2) + Operational GovOps Amatsu (×1) + Operational GovOps Soter Labs (×1)
  - Modification rule updated: exactly 6 signers required (was: minimum 4, equal split)
  - New docs added: "Consolidation Of Funds Into Core Council Buffer" (`A.2.4.1.4.1.1.1.6`) requiring Legacy Accounts (Distribution Reward Controller, Integration Boost Wallets, Liquidity Bootstrapping Budget) to be moved into the Core Council Buffer
- **November/December 2025 settlement** (`A.2.5.1.2.1.6.4`): Jan 2026 settlement covers two months; Spark calculations separated — only Spark uses standard resolution process, all other amounts treated as Agreed Amounts from Initial Calculation
- **Keel Senior Risk Capital** (`A.2.9.2.3.2.3`): 7.5 million USDS short-term Senior Risk Capital provisioned for Keel (credited to TRC, not transferred)
- **Ecosystem Accord 6: Sky and Launch Agent 6** (`A.2.9.2.6`) — new accord added:
  - Duration: indefinite from 2025-12-18
  - AGENT6 total supply: **1,000,000,000** — LA6 Prime Treasury: 777,777,778; Sky retained: 222,222,222
  - Initial USDS allocation: **10,000,000 USDS** to LA6 SubProxy (transfer contingent on future agreement on terms)

### Context
Core Council Buffer expansion reflects addition of Operational GovOps executors (Amatsu, Soter Labs) as signers. Ecosystem Accord 6 formalizes Launch Agent 6 (Osero) joining the Sky ecosystem; see Osero changelog for the full artifact addition.

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

## PR #115 — Atlas Edit Weekly Proposal 2025-11-17
**Merged:** 2025-11-20 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Distribution Reward Primitive** (A.2.4): "Accessibility Reward" terminology replaced with "Distribution Reward" across multiple docs (Reward Payment formula, Pioneer Prime Benefits, Integration Boost process flow, Distribution Rewards section); Pioneer Prime Benefits now references Distribution Reward for tagging purposes
- **Boosted Distribution Reward**: 0.3% rate clarified as commencing January 2026
- **Monthly Settlement Cycle** (A.2.6) restructured:
  - New step: "Forum Post By Core GovOps" must be created by end of each month (replaces "Initial Calculation by Operational Executor Agent" as first step)
  - Initial Calculation deadline extended: 5 → **7 calendar days** post month-end
  - Independent Calculation (Core Council Risk Advisor): 5 days after IC posting → **7 calendar days** post month-end (combined with IC)
  - "Resolution Of Differences By Core GovOps Atlas Axis" → **"Final Calculation By Core GovOps"** (new consolidated step; Core GovOps has 12 calendar days from month-end)
  - Interim scope: "September 2025" section → **"July/August 2025"** (initial cycle); "October 2025" → **"September 2025"** content; new "November/December 2025" section: no December cycle, January 2026 covers Nov–Dec combined
  - Revenue Sharing for Sky Direct Exposures: simplified — Prime Agents not required to pay ACL Borrow Rate for Sky Direct Exposure funds; all yield flows exclusively to Sky

### Context
The Monthly Settlement Cycle restructure consolidates the calculation workflow under Core GovOps, introduces a forum post anchor step, and shifts the baseline timeline to 7+12 days from month-end. Also corrects the interim-cycle naming that was referencing future months by name.

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

## PR #103 — 2025-11-02 Weekly Cycle Edit Proposal
**Merged:** 2025-11-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **"Accessibility Reward" → "Distribution Reward" global rename** across A.2.4 and related sections:
  - Section title: "Accessibility Reward Primitive" → "Distribution Reward Primitive"
  - Purpose, Allowed Instances, Multi-Instance Coordinator, Global Specification, Base Elements, Integrator Program docs all updated
  - Compliance With Local Laws condition precedent renamed
  - All cross-references to "Accessibility Reward Code", "Accessibility Reward Rate", "Accessibility Reward Fee" updated
  - Pioneer Prime Benefits and Pioneer Incentive Pool references updated
  - Distribution Reward reimbursement amounts Active Data cross-references updated
  - Governance/Treasury allocation step descriptions updated (0.5% allocated to Integrators; 0.5% to Prime Agents managing Integrator rewards — terminology alignment)
  - Stage 1 settlement calculation: "Accessibility Reward" → "Distribution Reward" references
  - SkyLink settlement cycle text updated
- **A.2.10** restructured: "Accessibility Reward" → "Distribution Reward" section renamed; "Accessibility Reward Rate" → "Distribution Reward Rate"; split specification (Frontend Portion 50% / Prime Portion 50%) subsections deleted from A.2.10 and consolidated into the rate doc; 2025 Bonus and Bonus Limitation docs updated
- **Ecosystem Entity Grants** (A.2.14 → A.2.15): section restructured from a single Executive Vote authorization doc into discrete historical grant records:
  - Sky Frontier Foundation August 2025 grant recorded: 50M USDS, 1,977,443,914 SKY, 28,829,858.44 UNI-V2 LP, 35.41 DAI, 46,362.27 ENS, 1,467.08 stkAAVE, 643.73 COMP, 60 AAVE, 0.0296 WETH (`0xca51…A0`, tx `0x9dff…3f`)
  - Fortification Foundation August 2025 grant recorded: 10M USDS, 200M SKY (`0x4834…C6`, same tx)
  - Section number renumbered A.2.14 → A.2.15

### Context
PR 103 is the primary rename PR completing the "Accessibility Reward" → "Distribution Reward" terminology transition across the Core Atlas. The Ecosystem Entity Grants restructuring converts the section from a forward-looking authorization to an historical record.

---

## PR #96 — October 27 edit
**Merged:** 2025-10-31 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Sky Direct Exposures** (A.2.4) renamed from "Direct Sky Exposures"; governance authority shifted from Atlas Edit Proposal process to Core Facilitator direct designation via Sky Forum posts; list converted to Active Data (Responsible Party: Core Facilitator, Direct Edit update process)
- **Current Sky Direct Exposures** Active Data record added:
  - Treasury Bills — BUIDL, JTRSY, USTB on Ethereum Mainnet by Grove
  - CLOs — JAAA on Ethereum Mainnet by Grove
- **JAAA Direct Exposure Through Grove** entry deleted (replaced by the new Active Data list)
- **Revenue Sharing for Sky Direct Exposures**: previous text about ACL Borrow Rate exception replaced — Prime Agents not required to pay ACL Borrow Rate on Sky Direct Exposure funds; all yield exclusively due to Sky
- **Treasury Management Short-Term Measures** (A.2.5) substantially expanded:
  - Allocation changed: Net revenue now allocated through modified steps (not manually via Executive Votes)
  - **Step 1 Capital**: 21% allocated: 20% → Core Council Buffer (3/4 multisig at `0x210C…4364`, CF + Core GovOps signers); 1% → Aligned Delegates Buffer (3/4 multisig at `0x37FC…a3A3`, CF + Core GovOps signers)
  - **Step 4 Capital** (remaining 79% of Step 1): 300,000 USDS/day → SKY buybacks; remainder → Surplus Buffer
  - **Implementation**: retroactive to Sep 1, 2025; next Executive Vote must include transfers of 3,876,387 USDS to Core Council Buffer and 193,820 USDS to Aligned Delegates Buffer for Sep 2025
- **Monthly Settlement Cycle** (A.2.6): Stage 2 timing updated (see governance entry); "Resolution Of Differences By Core GovOps Atlas Axis" → "Core GovOps" throughout; "Accessibility Reward" reference in Stage 1 calc clarified as "Distribution Reward"; Integration Boost Wallet cross-reference fix (near-term → near-term)
- **Distribution Reward Primitive** (A.2.4): multiple "an Distribution Reward" → "a Distribution Reward" copy fixes; "Accessibility Reward" → "Distribution Reward" sweep across Pioneer Prime Benefits, Integration Boost process flow, Distribution Rewards section, Reward Payment formula

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
