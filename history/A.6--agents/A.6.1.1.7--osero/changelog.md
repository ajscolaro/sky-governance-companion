# Osero — Change History

Atlas path: `A.6.1.1.7` (357 docs) — formerly known as Launch Agent 6; public-name reveal landed in PR #246 (2026-05-21).

---

## PR #277 — Atlas Edit Proposal — 2026-07-13
**Merged:** 2026-07-16 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: Maximum Exposure** (`A.6.1.1.7.2.6.1.3.1.1.1.2.5.2`, UUID `7baff09a…fe4d`): The Maximum Exposure for this Instance is 5,000,000 USDS.
- **New: Capital Ratio Requirement** (`A.6.1.1.7.2.6.1.3.1.1.1.2.5.3`, UUID `771b1a44…a11f`): The Capital Ratio Requirement for this Instance, as specified in `A.3.2.1.1.1`, is 100%.

### Housekeeping
- `A.6.1.1.7.2.6.2.1.2` (Active Instances Directory): removed `Junior`
- `A.6.1.1.7.2.6.2.1.3` (Completed Instances Directory): removed `Junior`
- `A.6.1.1.7.2.6.2.1.4` (In Progress Invocations Directory): removed `Junior`
- `A.6.1.1.7.2.6.2.1.5.1.1` (Failed Invocations): removed `Junior`
- `A.6.1.1.7.2.6.2.1.5.1.2` (Suspended Instances): removed `Junior`
- `A.6.1.1.7.2.6.2.1.5.1` (Archived Invocations/Instances): removed `Junior`
- `A.6.1.1.7.2.6.2.1` (Primitive Hub Document): removed `Junior`
- `A.6.1.1.7.2.6.2.2` (Active Instances): removed `Junior`
- `A.6.1.1.7.2.6.2.3` (Completed Instances): removed `Junior`
- `A.6.1.1.7.2.6.2.4` (In Progress Invocations): removed `Junior`
- `A.6.1.1.7.2.6.2` (Risk Capital Rental Primitive): removed `Junior`

### Context
Sets an Osero instance's Maximum Exposure to 5M USDS with a 100% Capital Ratio Requirement, alongside the ecosystem-wide "Junior" risk-capital terminology cleanup.

---

## PR #273 — Atlas Edit Proposal — 2026-07-06
**Merged:** 2026-07-10 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New: Ethereum Mainnet** (`A.6.1.1.7.2.6.1.1.2.1`, UUID `4c7bab4f…5ddf`): The documents herein contain a Directory of all Instances on the Ethereum Mainnet of the Allocation System Primitive with Instance status of `Active`.
  - **SparkLend** (`A.6.1.1.7.2.6.1.1.2.1.1`): The Ethereum Mainnet Instances of the SparkLend Protocol with `Active` Status are stored herein.
  - **Ethereum Mainnet - SparkLend USDS Instance Configuration Document Location** (`A.6.1.1.7.2.6.1.1.2.1.1.1`): This Instance's associated Instance Configuration Document is located at `A.6.1.1.7.2.6.1.3.1.1.1`.
- **New: Allocator Oracle Contract** (`A.6.1.1.7.2.6.1.2.1.1.1.1.1.3`, UUID `eafb8f6f…c9b3`): The address of the ALLOCATOR_ORACLE contract is: `0xc7B91C401C02B73CBdF424dFaaa60950d5040dB7`.
- **New: Allocator Registry Contract** (`A.6.1.1.7.2.6.1.2.1.1.1.1.1.4`, UUID `e1babaf7…b488`): The address of the ALLOCATOR_REGISTRY contract is: `0xCdCFA95343DA7821fdD01dc4d0AeDA958051bB3B`.
- **New: Allocator Roles Contract** (`A.6.1.1.7.2.6.1.2.1.1.1.1.1.5`, UUID `f612bab0…6dbe`): The address of the ALLOCATOR_ROLES contract is: `0x9A865A710399cea85dbD9144b7a09C889e94E803`.
- **New: Diamond PAU Contracts** (`A.6.1.1.7.2.6.1.2.1.1.1.2`, UUID `00360509…1173`): The documents herein define the addresses of the Diamond Parallelized Allocation Unit (Diamond PAU) contracts deployed for the Osero Liquidity Layer.
  - **ALM Proxy Contract** (`A.6.1.1.7.2.6.1.2.1.1.1.2.1.1`): The address of the ALM Proxy contract is: `0x6d370e359e9cbd0Fd35Bb38fAF705D84238CB884`.
  - **Controller Contract** (`A.6.1.1.7.2.6.1.2.1.1.1.2.1.2`): The address of the Controller contract is: `0x24169Afb34fAe4D4356BC54Bd80319131e35ca38`.
  - **AccessControls Contract** (`A.6.1.1.7.2.6.1.2.1.1.1.2.1.3`): The address of the AccessControls contract is: `0x791D2a017532CfAD881c446e6bF93BbC3c0778b2`.
  - **ALM Rate Limits Contract** (`A.6.1.1.7.2.6.1.2.1.1.1.2.1.4`): The address of the ALM Rate Limits contract is: `0xE9a78f34fe497e2186f81B8c014cd93B308BC62a`.
  - **AdministeredAgent Contract** (`A.6.1.1.7.2.6.1.2.1.1.1.2.1.5`): The address of the AdministeredAgent contract is: `0x1837505D104F7a6D8b7e19452610B0A3D652EF12`.
- **New: RateLimits** (`A.6.1.1.7.2.6.1.2.1.1.2`, UUID `cec50748…0e63`): The documents herein list the rate limits for the Osero Liquidity Layer Diamond PAU.
  - **USDS Mint Maximum** (`A.6.1.1.7.2.6.1.2.1.1.2.1.1`): The maximum amount of USDS that can be minted by the Osero Diamond PAU (`LIMIT_USDS_MINT`) is specified in the document herein.
  - **USDS Burn Maximum** (`A.6.1.1.7.2.6.1.2.1.1.2.1.2`): The maximum amount of USDS that can be burned by the Osero Diamond PAU (`LIMIT_USDS_BURN`) is specified in the document herein.
- **New: On-chain Parameters** (`A.6.1.1.7.2.6.1.2.1.1.3`, UUID `5b8cc141…5002`): The documents herein list general on-chain parameters for the Osero Liquidity Layer.
  - **Allocator Vault Parameters** (`A.6.1.1.7.2.6.1.2.1.1.3.1`): The Allocator Vault parameters for ALLOCATOR-PRYSM-A are defined in `A.3.7.1.2.1.7`.
  - **Whitelisting Of ALM Proxy** (`A.6.1.1.7.2.6.1.2.1.1.3.2`): The ALM Proxy for the Osero Diamond PAU will be whitelisted on the litePSM in an upcoming spell.
- **New: Governance Processes** (`A.6.1.1.7.2.6.1.2.1.2`, UUID `d6410ff9…1b8f`): The documents herein describe the specific governance processes for the Osero Liquidity Layer.
  - **Osero Relayer Multisig** (`A.6.1.1.7.2.6.1.2.1.2.1.1`): The Osero Relayer Multisig is registered as an Actor on the AdministeredAgent, which holds the Allocator Role as specified in `A.2.2.10.1.1.1.3.3`, and is controlled by Osero.
  - **Address** (`A.6.1.1.7.2.6.1.2.1.2.1.1.1`): The address of the Osero Relayer Multisig on Ethereum Mainnet is `0x29c5A20A49A0D522A3714af97C517a908946b6A8`.
  - **Required Number Of Signers** (`A.6.1.1.7.2.6.1.2.1.2.1.1.2`): The Osero Relayer Multisig currently has a 2/3 signing requirement.
  - **Signers** (`A.6.1.1.7.2.6.1.2.1.2.1.1.3`): The signers of the Osero Relayer Multisig are three (3) addresses controlled by Osero.
  - **Usage Standards** (`A.6.1.1.7.2.6.1.2.1.2.1.1.4`): The signers of the Osero Relayer Multisig must use the Multisig to submit allocator operations through the AdministeredAgent in accordance with the instructions specified in the Osero Artifact.
  - **Modification** (`A.6.1.1.7.2.6.1.2.1.2.1.1.5`): Osero can change the signers of the Osero Relayer Multisig at any time, so long as there are at least two (2) signers and at least a majority of signers are required to execute transactions.
  - **Core Operator Relayer Multisig** (`A.6.1.1.7.2.6.1.2.1.2.1.2`): The Core Operator Relayer Multisig is registered as an Actor on the AdministeredAgent, which holds the Allocator Role as specified in `A.2.2.10.1.1.1.3.3`, and is controlled by Operatio.
  - **Address** (`A.6.1.1.7.2.6.1.2.1.2.1.2.1`): The address of the Core Operator Relayer Multisig on Ethereum Mainnet is `0x3dE688267Cf099307aBdd85F64D8efe03D0b2b26`.
  - **Required Number Of Signers** (`A.6.1.1.7.2.6.1.2.1.2.1.2.2`): The Core Operator Relayer Multisig currently has a 2/3 signing requirement.
  - **Signers** (`A.6.1.1.7.2.6.1.2.1.2.1.2.3`): The signers of the Core Operator Relayer Multisig are three (3) addresses controlled by Operational GovOps Soter Labs.
  - **Usage Standards** (`A.6.1.1.7.2.6.1.2.1.2.1.2.4`): The signers of the Core Operator Relayer Multisig must use the Multisig to submit allocator operations through the AdministeredAgent in accordance with the instructions specified in the Osero Artifact.
  - **Modification** (`A.6.1.1.7.2.6.1.2.1.2.1.2.5`): Soter Labs can change the signers of the Core Operator Relayer Multisig at any time, so long as there are at least two (2) signers and at least a majority of signers are required to execute transactions.
  - **Freezer Multisig** (`A.6.1.1.7.2.6.1.2.1.2.1.3`): The Freezer Multisig is registered as a Revoker on the AdministeredAgent, as specified in `A.2.2.10.1.1.1.3.5`.
  - **Address** (`A.6.1.1.7.2.6.1.2.1.2.1.3.1`): The address of the Freezer Multisig on Ethereum Mainnet is `0xF61F90907551a8A23f0f8EEE9658Fa53326de603`.
  - **Required Number Of Signers** (`A.6.1.1.7.2.6.1.2.1.2.1.3.2`): The Freezer Multisig currently has a 2/5 signing requirement.
  - **Signers** (`A.6.1.1.7.2.6.1.2.1.2.1.3.3`): The signers of the Freezer Multisig are three (3) addresses controlled by Operational GovOps Soter Labs, one (1) address controlled by Operational Facilitator Redline Facilitation Group, and one (1) address controlled by Osero.
  - **Usage Standards** (`A.6.1.1.7.2.6.1.2.1.2.1.3.4`): The signers of the Freezer Multisig should exercise their authority to remove a compromised or malicious Actor from the AdministeredAgent in the event of an emergency.
  - **Modification** (`A.6.1.1.7.2.6.1.2.1.2.1.3.5`): Modification of the signers of the Freezer Multisig must be approved through an Atlas Edit Proposal.
  - **Invoking New Instances** (`A.6.1.1.7.2.6.1.2.1.2.2`): The governance process to invoke a new Instance of the Allocation System Primitive follows the Root Edit process, see `A.6.1.1.7.2.2.2.2.1.2`.
- **New: Total Risk Capital (TRC) Management** (`A.6.1.1.7.2.6.1.2.1.3`, UUID `80559817…9369`): The documents herein specify requirements related to Osero's Total Risk Capital (TRC) management.
  - **Stablewatch's Operation Of Osero Liquidity Layer And Agreement Regarding Encumbrance Ratio** (`A.6.1.1.7.2.6.1.2.1.3.1`): Stablewatch will operate the Osero Liquidity Layer and agrees to stay at or below a 90% Encumbrance Ratio.
  - **Stablewatch's Total Risk Capital (TRC) Management Processes** (`A.6.1.1.7.2.6.1.2.1.3.2`): As operators of the Osero Liquidity Layer, Stablewatch automatically inherits, and is subject to, the base class of operational requirements related to Total Risk Capital management defined in [A.2.2.10.1.1.3.2.1.2 - Primes' Total Risk Capi.
- **New: Osero Liquidity Layer Operational Processes** (`A.6.1.1.7.2.6.1.2.2`, UUID `5c05c2d0…2457`): The documents herein describe common operational procedures for the Osero Liquidity Layer applicable across multiple Instances.
  - **Role Hierarchies And Permissions** (`A.6.1.1.7.2.6.1.2.2.1.1`): The roles and permissions of the Diamond PAU Instance are the Liquidity Layer roles defined in `A.2.2.10.1.1.1.3`, managed by the AccessControls contract.
  - **Controller Functions** (`A.6.1.1.7.2.6.1.2.2.1.2`): The Diamond PAU Controller functions for the Osero Liquidity Layer are the shared Diamond PAU Controller functions specified in `A.2.2.10.1.1.1.5.2`.
  - **USDS Facet** (`A.6.1.1.7.2.6.1.2.2.1.2.1`): The Osero Liquidity Layer uses the USDS Facet (`A.2.2.10.1.1.1.4.2.22`) to mint and burn USDS through the allocator vault.
  - **Aave Facet** (`A.6.1.1.7.2.6.1.2.2.1.2.2`): The Osero Liquidity Layer uses the Aave Facet (`A.2.2.10.1.1.1.4.2.1`) to deposit into and withdraw from SparkLend USDS.
  - **Rate Limit Management** (`A.6.1.1.7.2.6.1.2.2.1.3`): The rate limits of the Osero Liquidity Layer are managed as specified in `A.2.2.10.1.1.1.5.3`.
  - **Instance Lifecycle Management** (`A.6.1.1.7.2.6.1.2.2.1.4`): The documents herein define processes for invoking (onboarding) new Osero Liquidity Layer Instances and offboarding existing ones.
  - **Non-Routine Protocol** (`A.6.1.1.7.2.6.1.2.2.2`): The documents herein define the process for non-routine ongoing management of the Osero Liquidity Layer and its active Instances.
  - **Remove Compromised Actor As Freezer** (`A.6.1.1.7.2.6.1.2.2.3.1`): In the event of a compromised or malicious Actor, the Freezer Multisig — registered as a Revoker on the AdministeredAgent, as specified in `A.2.2.10.1.1.1.3.5` — removes that Actor by calling.
  - **Withdraw All SparkLend Positions** (`A.6.1.1.7.2.6.1.2.2.3.2`): In the event that liquidity must be recovered from SparkLend and centralized in the Osero ALM Proxy, a Relayer Multisig, acting as an Actor, withdraws the Osero Liquidity Layer's full SparkLend USDS position through the Aave Facet, as speci.
  - **Burn USDS** (`A.6.1.1.7.2.6.1.2.2.3.3`): Once liquidity has been recovered to the Osero ALM Proxy, the recovered USDS is repaid and burned through the USDS Facet, as specified in `A.2.2.10.1.1.1.5.2.2`.
- **New: Ethereum Mainnet Instances** (`A.6.1.1.7.2.6.1.3.1`, UUID `3ebb2e50…d3b6`): The Ethereum Mainnet Instances of the Osero Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.
  - **SparkLend** (`A.6.1.1.7.2.6.1.3.1.1`): The Ethereum Mainnet Instances of the SparkLend Protocol with `Active` Status are stored herein.
  - **RRC Framework Full Implementation Coverage** (`A.6.1.1.7.2.6.1.3.1.1.1.1`): **`Covered`**.
  - **Network** (`A.6.1.1.7.2.6.1.3.1.1.1.2.1.1`): Ethereum Mainnet.
  - **Target Protocol** (`A.6.1.1.7.2.6.1.3.1.1.1.2.1.2`): SparkLend.
  - **Asset Supplied By Osero Liquidity Layer** (`A.6.1.1.7.2.6.1.3.1.1.1.2.1.3`): USDS.
  - **Token** (`A.6.1.1.7.2.6.1.3.1.1.1.2.1.4`): spUSDS.
  - **Token Address** (`A.6.1.1.7.2.6.1.3.1.1.1.2.2.1`): `0xC02aB1A5eaA8d1B114EF786D9bde108cD4364359`.
  - **Underlying Asset Address** (`A.6.1.1.7.2.6.1.3.1.1.1.2.2.2`): `0xdC035D45d973E3EC169d2276DDab16f1e407384F`.
  - **Inflow RateLimitID** (`A.6.1.1.7.2.6.1.3.1.1.1.2.3.1`): The inflow RateLimitID is: `0x5534da2f28b3dd200cb0042c0876cd6e2beca93d3232c366ec077018c82da73d`.
  - **Outflow RateLimitID** (`A.6.1.1.7.2.6.1.3.1.1.1.2.3.2`): The outflow RateLimitID is: `0xf9ac1455c7ba8e0bacb7a3eca4a2cf412eda3cbc0f6aa1b071d73b37d49925d8`.
  - **Deposit Rate Limits** (`A.6.1.1.7.2.6.1.3.1.1.1.2.4.1`): The deposit rate limits are.
  - **Withdrawal Rate Limits** (`A.6.1.1.7.2.6.1.3.1.1.1.2.4.2`): The withdrawal rate limits are.
  - **Max Slippage** (`A.6.1.1.7.2.6.1.3.1.1.1.2.5.1`): The `maxSlippage` for this Instance is 0.01%.
  - **Instance-specific Operational Processes** (`A.6.1.1.7.2.6.1.3.1.1.1.3`): The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Osero Liquidity Layer processes.

### Housekeeping
- `A.6.1.1.7.2.6.1` (Allocation System Primitive): removed `Instances of the`
- `A.6.1.1.7.2.6.1.3.1.1.1.2.3` renumbered (UUID stable: `7955432c…981a`)
- `A.6.1.1.7.2.6.1.3.1.1.1.2.4` renumbered (UUID stable: `d0d163d7…2d9f`)

### Context
Records Osero's full Liquidity Layer deployment on Ethereum Mainnet — Diamond PAU contracts (ALM Proxy, Controller, AccessControls, Rate Limits, AdministeredAgent), Relayer/Core Operator/Freezer multisigs, and an initial SparkLend USDS (spUSDS) instance operated by Stablewatch at a ≤90% Encumbrance Ratio — built on the shared Diamond PAU framework added to A.2 in this same edit. First substantive on-chain footprint for the agent formerly known as Launch Agent 6.

---

## PR #253 — Atlas Edit Proposal — 2026-06-01
**Merged:** 2026-06-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Agent Creation Primitive** (`A.6.1.1.7.2.1.1`): `4` → `5`
- **Prime Transformation Primitive** (`A.6.1.1.7.2.1.2`): `4` → `5`
- **Executor Transformation Primitive** (`A.6.1.1.7.2.1.3`): `4` → `5`
- **Agent Token Primitive** (`A.6.1.1.7.2.1.4`): `4` → `5`
- **Genesis Primitives** (`A.6.1.1.7.2.1`): `4` → `5`
- **Executor Accord Primitive** (`A.6.1.1.7.2.2.1`): `5` → `6`
- **Root Edit Primitive** (`A.6.1.1.7.2.2.2`): `5` → `6`
- **Light Agent Primitive** (`A.6.1.1.7.2.2.3`): `5` → `6`
- **Operational Primitives** (`A.6.1.1.7.2.2`): `5` → `6`
- **Ecosystem Upkeep Fee Primitive** (`A.6.1.1.7.2.3.1`): `6` → `7`
- **Upkeep Rebate Primitive** (`A.6.1.1.7.2.3.2`): `6` → `7`
- **Ecosystem Upkeep Primitives** (`A.6.1.1.7.2.3`): `6` → `7`
- **Token SkyLink Primitive** (`A.6.1.1.7.2.4.1`): `7` → `8`
- **SkyLink Primitives** (`A.6.1.1.7.2.4`): `7` → `8`
- **Distribution Reward Primitive** (`A.6.1.1.7.2.5.1`): `8` → `9`
- **Integration Boost Primitive** (`A.6.1.1.7.2.5.2`): `8` → `9`
- **Terms** (`A.6.1.1.7.2.5.3.2.1.1.2.2`): `8` → `9`
- **Pioneer Chain Primitive** (`A.6.1.1.7.2.5.3`): `8` → `9`
- **Demand Side Stablecoin Primitives** (`A.6.1.1.7.2.5`): `8` → `9`
- **Allocation System Primitive** (`A.6.1.1.7.2.6.1`): `9` → `10`
- **Junior Risk Capital Rental Primitive** (`A.6.1.1.7.2.6.2`): `9` → `10`
- **Asset Liability Management Rental Primitive** (`A.6.1.1.7.2.6.3`): `9` → `10`
- **Supply Side Stablecoin Primitives** (`A.6.1.1.7.2.6`): `9` → `10`
- **Core Governance Reward Primitive** (`A.6.1.1.7.2.7.1`): `10` → `11`
- **Core Governance Primitives** (`A.6.1.1.7.2.7`): `10` → `11`

### Housekeeping
- `5` → `6` across 4 docs.
- `9` → `10` across 4 docs.
- `10` → `11` across 2 docs.
- `8` → `9` across 5 docs.
- `4` → `5` across 5 docs.
- `7` → `8` across 2 docs.
- `6` → `7` across 3 docs.

### Context
All changes are version-reference bumps propagated from the Support Scope (A.2) primitive-tree reorganization and the Capital Ratio Requirement rename — no Osero-specific operational change.

---

## PR #246 — Atlas Edit Proposal — 2026-05-18
**Merged:** 2026-05-21 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- `A.6.1.1.7.1` (Introduction): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.1.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.1.3.1.1.1` (Name): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.1.3.1.1.2` (SubProxy Account): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.1.3.1.1.3.1` (StarGuard Max Delay): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.1.3.1.1.3` (StarGuard Contract): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.1.3.1.1.4` (Genesis Account): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.1.3.1.1.5.1` (Osero Foundation): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.1.3.1.1.5.2` (Stablewatch): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.1` (Agent Creation Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.2.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.2.3.1.1.1` (Agent Type): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.2` (Prime Transformation Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.3.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.3` (Executor Transformation Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.4.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.4.2.1.1.1` (Token Name): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.4.2.1.1.2` (Token Symbol): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.4.2.1.1.3` (Genesis Supply): `AGENT6` → `OSERO`
- `A.6.1.1.7.2.1.4.2.1.1.4` (Token Address): `AGENT6` → `OSERO`
- `A.6.1.1.7.2.1.4.2.1.1.5` (Token Admin): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.4.2.1.1.6` (Token Emissions): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.4.2.1.2` (Operational Process Definition): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1.4` (Agent Token Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.1` (Genesis Primitives): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.1.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.1` (Executor Accord Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.2.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.2.2.1.2.1.1.1` (Short-Term Transitionary Measures): `AGENT6` → `OSERO`
- `A.6.1.1.7.2.2.2.2.1.2.1.1` (Root Edit Proposal Submission): `AGENT6` → `OSERO`
- `A.6.1.1.7.2.2.2.2.1.2.1.2` (Root Edit Expert Advisor Review): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.2.2.1.2.1.4` (Root Edit Token Holder Vote): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.2.2.1.2.1.6` (Artifact Edit Restrictions): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.2.2.1.2.1` (Routine Protocol): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.2.2.1.2.2` (Non-Routine Protocol): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.2.2.1.2.3.1` (Root Edit Voting Process In Emergency Situations): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.2.2.1.2.3` (Emergency Protocol): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.2.2.1.2` (Operational Process Definition): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.2` (Root Edit Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.3.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2.3` (Light Agent Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.2` (Operational Primitives): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.3.1.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.3.1.2.1.1.1` (Terms): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.3.1.2.1.2.1.1` (Process Definition For Upkeep Fee Payment): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.3.1` (Ecosystem Upkeep Fee Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.3.2.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.3.2.2.1.2.1.1` (Osero Holds Tokens Of Other Agents In Its SubProxy Account): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.3.2.2.1.2.1.2` (Osero Deducts Rebate From Ecosystem Upkeep Fees): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.3.2.2.1.2.1.3` (Operational GovOps Reviews Rebate): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.3.2` (Upkeep Rebate Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.3` (Ecosystem Upkeep Primitives): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.4.1.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.4.1` (Token SkyLink Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.4` (SkyLink Primitives): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.5.1.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.5.1` (Distribution Reward Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.5.2.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.5.2` (Integration Boost Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.5.3.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.5.3.2.1.1.2.1` (Address): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.5.3` (Pioneer Chain Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.5` (Demand Side Stablecoin Primitives): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.6.1.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.6.1.2.1.1.1` (Osero Liquidity Layer Addresses): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.6.1.2.1.1` (Osero Liquidity Layer Architecture): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.6.1.2.1` (General Specifications): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.6.1.2` (Multi-Instance Coordinator Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.6.1` (Allocation System Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.6.2.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.6.2` (Junior Risk Capital Rental Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.6.3.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.6.3` (Asset Liability Management Rental Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.6` (Supply Side Stablecoin Primitives): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.7.1.1` (Primitive Hub Document): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.7.1` (Core Governance Reward Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2.7` (Core Governance Primitives): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.2` (Sky Primitives): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.3.1.1` (Sky Forum): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.3.1.2` (Sky Ecosystem Emergency Response): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.3.1.3` (Agent-Specific Emergency Response): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.3.1` (Governance Information Unrelated To Root Edit Primitive): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.3.2.1` (Ecosystem Accord 6): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.3.2` (Ecosystem Accords): `Launch Agent 6` → `Osero`
- `A.6.1.1.7.3` (Omni Documents): `Launch Agent 6` → `Osero`
- `A.6.1.1.7` (Osero): `Launch Agent 6` → `Osero`
- `Launch Agent 6` → `Osero` across 85 docs.
- `AGENT6` → `OSERO` across 5 docs.

### Context
Public-name reveal: Launch Agent 6 is now Osero, with token symbol AGENT6 → OSERO. Rename ripples through the agent's entire Primitives scaffold and Ecosystem Accord 6 references; parallels the LA4 → Obex reveal in PR #121. Ratified by Poll #1633 (10-0, non-voters: axislegati, excel, opex).

---

## PR #242 — Atlas Edit Proposal — 2026-05-11
**Merged:** 2026-05-15 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Root Edit Voting Process In Emergency Situations** (`A.6.1.1.7.2.2.2.2.1.2.3.1`): `8` → `9`

### Housekeeping
- `8` → `9` across 1 doc.

---

## PR #224 — Atlas Edit Proposal — 2026-04-20
**Merged:** 2026-04-24 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Pioneer Chain Primitive on Plasma activated** (`A.6.1.1.7.2.5.3.2.1`): Launch Agent 6's Pioneer Incentive Pool address and terms established for Plasma; includes network identifier and Pioneer Incentive Pool address

### Housekeeping
- Distribution Requirement Primitive (`A.6.1.1.7.2.3.1`) renamed to "Ecosystem Upkeep Fee Primitive"; Market Cap Fee Primitive subtree (`A.6.1.1.7.2.3.2`) deleted; Upkeep Rebate references updated.

---

## PR #200 — 2026-03-16 Weekly Edit Proposal
**Merged:** 2026-03-20 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **SubProxy Account** (`A.6.1.1.7.2.1.1.3.1.1.2`): address set — `0x24fdcd3bFA5C2553e05B2f9AD0365EBC296278D3` (Ethereum Mainnet).
- **StarGuard Contract** (`A.6.1.1.7.2.1.1.3.1.1.3`): new section — address `0xBfA2D1dA838E55A74c61699e164cDFF8cF0cF0e2` (Ethereum Mainnet); prior "Genesis Account" heading removed (UUID preserved).
- Additional new sections: Pioneer Chain Primitive directories (Active/Completed/In Progress), Allocation System / Junior Risk Capital / ALM Rental Primitives directory scaffolding, Core Governance Reward Primitive — all empty placeholder directories for Osero's Liquidity Layer.
- **Ecosystem Accord 6** (`A.6.1.1.7.3.2.1`): structural fix — "Governance Information Unrelated To Root Edit Primitive" paragraph moved to correct location; Ecosystem Accord 6 cross-reference now uses UUID link.

---

## PR #187 — 2026-02-23 Atlas Edit Weekly Cycle Proposal
**Merged:** 2026-03-05 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- 510 sections (~302 additions / 302 deletions): link-text normalization sweep across Osero (`A.6.1.1.7`) Artifact — largest single agent touched. No parameter values changed.

---

## PR #172 — Jan 26 Edit
**Merged:** 2026-01-29 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Ecosystem Accord 6 cross-reference added** (`A.6.1.1.7.3.2`, new): Osero formally records agreement to Ecosystem Accord 6, located at `A.2.8.2.6`.

### Context
Ecosystem Accord 6 provisions in `A.2--support` also updated in this PR — see support changelog.

---

## PR #141 — Dec 8 edit
**Merged:** 2025-12-11 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Full Launch Agent 6 (Osero) artifact added** (`A.6.1.1.7`) — 344 new sections, 1,386 lines:
  - Genesis Primitives (Agent Creation, Prime Transformation, Executor Transformation, Agent Token) — all with Primitive Hub Documents and lifecycle directories
  - Agent Token instance active: AGENT6, total supply 1,000,000,000; allocated 777,777,778 to LA6 Prime Treasury
  - Executor Accord Primitive active instance: Ozone (Operational Executor Agent)
  - Root Edit Primitive active instance with full governance protocol (routine/non-routine/emergency, StarGuard-based)
  - Ecosystem Upkeep Primitives: Distribution Requirement, Market Cap Fee, Upkeep Rebate (all with active instances)
  - SkyLink, Demand Side Stablecoin (Distribution Reward, Integration Boost, Pioneer Chain), Supply Side Stablecoin (Allocation System, Junior Risk Capital Rental, Asset Liability Management), Core Governance Reward — all inactive
  - Omni Documents: Sky Forum category "Launch Agent 6 Prime"; emergency response protocols (to be specified later)
  - Launch Agent 6 Foundation + Development Company as parties alongside Prime Agent
  - Duration of Accord: indefinite from 2025-12-18

### Context
Osero (Launch Agent 6) is a new Sky ecosystem agent introduced in this edit alongside its Ecosystem Accord (Accord 6, recorded in A.2 support). This is the first LA6 artifact entry; Genesis Capital of 10M USDS is contingent on a future agreement.

---
