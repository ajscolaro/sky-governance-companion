# Pattern — Change History

Atlas path: `A.6.1.1.6` (353 docs)

---

## PR #222 — Atlas Edit Proposal — 2026-04-13
**Merged:** 2026-04-16 | **Type:** Weekly edit (Atlas Axis — Poll 1628) | **+1232/-32 lines**

### Material Changes

- **New: Pattern Liquidity Layer entire documentation tree added** (`A.6.1.1.6.2.6.1`, massive scaffold): full Pattern Liquidity Layer artifact — ALM contract addresses, rate limits, Relayer/Freezer Multisigs, role hierarchy, Controller function specs, and first Active Instance (Maple). Governance inherited from the Sky Liquidity Layer pattern, operated by **Pattern Dev Co.** (development company providing services to Pattern)
  - **Allocator Contracts (Ethereum Mainnet):** ALLOCATOR_BUFFER `0x823459b5…F1ef` (preexisting), **ALLOCATOR_ORACLE** `0xc7B91C40…40dB7`, **ALLOCATOR_REGISTRY** `0xCdCFA953…bB3B`, **ALLOCATOR_ROLES** `0x9A865A71…E803`, ALLOCATOR_VAULT (ALLOCATOR-PATTERN-A) `0xbd34fc6A…3B0E` (preexisting)
  - **ALM Contracts (Ethereum Mainnet):** ALM_CONTROLLER (MainnetController) **`0x8739a869…62b1`** v1.6.0; ALM_PROXY **`0xbA43325E…169F`**; ALM_RATE_LIMITS **`0xa77f69f9…EA204`**
  - **Relayer Multisig** `0xd00665Df…737B`, **2/3** signing, controlled by **Operational GovOps Soter Labs**; three signers all Soter Labs-controlled
  - **Freezer Multisig** `0xe728D67b…18bB`, **2/5** signing, composition: **3 Soter Labs + 1 Redline Facilitation Group + 1 Pattern**. Modification requires Atlas Edit Proposal (with exceptions for self-reported key loss or voluntary removal)
  - **USDS Mint Maximum (Pattern Liquidity Layer):** `maxAmount` **100M USDS** / `slope` **50M USDS/day**
  - **USDS For USDC Swap Maximum:** `maxAmount` **100M USDS** / `slope` **50M USDS/day**
  - **USDS Burn Maximum:** TBD (future iteration)
  - **Total Risk Capital operator:** Pattern Dev Co. operates the Pattern Liquidity Layer and agrees to stay at or below **90% Encumbrance Ratio**
  - **Full Controller function specification:** Admin Functions (setMintRecipient, setLayerZeroRecipient, setMaxSlippage); Relayer Functions (mintUSDS, burnUSDS, transferAsset, ERC-4626 deposit/withdraw/redeem, ERC-7540 request/claim deposit/redeem, swapUSDSToDAI/swapDAIToUSDS, PSM swaps, transferTokenLayerZero); Freezer-triggered rate-limit management (Set/Trigger Decrease/Remove Compromised Relayer); Emergency Protocol (USDS Burn, USDC→USDS Swap, ERC-4626 Withdrawal, Redeem All Mainnet Positions)
- **New Pattern SLL instance: Ethereum Mainnet — Maple USDC** (`A.6.1.1.6.2.6.1.3.1.1.1`, new and first Active Instance):
  - Token: **syrupUSDC** `0x80ac24aA…46A0b`; Underlying: `0xA0b86991…06eB48` (USDC)
  - Inflow RateLimitID: `0x99a69e57…9bfe10`; Outflow RateLimitID: `0x64e6fd9d…77dc57`
  - **Deposit: `maxAmount` 100M USDC / `slope` 20M USDC/day**; Withdrawal: Unlimited
  - **RRC Framework Full Implementation Coverage: `Covered`** (unusual — most new instances launch at `Pending`)
  - Instance-specific operational extensions: `requestMapleRedemption` / `cancelMapleRedemption` relayer functions for Maple's queued-withdrawal model
- **Pattern Dev Co. introduced** (`A.6.1.1.6.2.1.1.3.1.1.5.1`, new): "Pattern Dev Co. is the development company that provides services to Pattern." Parallels the Obex/Treadstone relationship introduced in PR #186

### Housekeeping

- Added Maple Active Instances Directory under Pattern SLL: `A.6.1.1.6.2.6.1.1.2.1` (Ethereum Mainnet) → `.1.1` (Maple) → `.1.1.1` (Maple USDC Instance Config Location pointer)
- Allocator Vault Contract renumbered from `A.6.1.1.6.2.6.1.2.1.1.1.1.2` → `A.6.1.1.6.2.6.1.2.1.1.1.1.1.5` to make room for the new Oracle/Registry/Roles contracts; UUID preserved (`5ee30a61…3B0E`)

### Context

Pattern's Liquidity Layer goes live in this PR — analogous to the Grove Liquidity Layer structurally (shared Controller function spec, ALM architecture, 90% Encumbrance ceiling) but with Pattern-specific multisig composition (3 Soter / 1 Redline / 1 Pattern on the Freezer vs. Grove's equivalent arrangement) and a single inaugural active instance: Maple USDC via **syrupUSDC**, RRC Covered with a 100M deposit cap. The Maple redemption-queue machinery (`requestMapleRedemption` / `cancelMapleRedemption`) is specifically coded into Pattern's MainnetController, following the same pattern Spark uses for syrupUSDT (see PR #183). The Pattern Dev Co. / Pattern separation mirrors the Treadstone / Rubicon / Obex triad — this is the emerging architectural norm for Prime Agents: a non-technical "Foundation" entity (Pattern) plus a development operating company (Pattern Dev Co.) accountable for day-to-day liquidity-layer operation. Ratification Poll 1628 passed 10-0 with 3 non-voters. SKY ~$0.075, USDS supply ~$11.3B at merge.

---

## PR #176 — 2026-02-02 Edit
**Merged:** 2026-02-05 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Launch Agent 5 renamed to Pattern** throughout the Atlas: agent Artifact header (A.6.1.1.6), full Primitives scaffold, Agent Token references, Pattern Allocator Vault parameters, Root Edit / forum category references, and all LA5 cross-references.

### Context
Public-name reveal for Launch Agent 5 — last of the original pseudonymous LA1–LA5 cohort to receive its public name (Grove/Keel/Skybase/Obex already renamed). This PR also set initial Skybase SubProxy and StarGuard addresses (A.6.1.1.4) — see skybase changelog if/when processed. Rename-only backfill — the rest of this PR's content has not been processed in detail.

---

## PR #133 — 2025-12-01 AEW Proposal
**Merged:** 2025-12-04 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Pattern (formerly Launch Agent 5) full artifact onboarded** (A.6.1.1.6): the entire Pattern agent artifact was added in this PR — ~1,400 lines of new Atlas content establishing the agent's complete Sky Primitives framework:
  - **Agent Creation Primitive**: completed (one completed instance, `A.6.1.1.6.2.1.1`)
  - **Prime Transformation Primitive**: agent creation scaffold
  - **Executor Transformation Primitive**: operational executor infrastructure
  - **Agent Token Primitive**: token issuance framework (Ozone token instance with completed creation; Token SkyLink Primitive)
  - **Operational Primitives**: Executor Accord Primitive (Ozone instance), Root Edit Primitive, Light Agent Primitive
  - **Ecosystem Upkeep Primitives**: Distribution Requirement, Market Cap Fee, Upkeep Rebate
  - **Supply/Demand Side Stablecoin Primitives**: integration and pioneer chain scaffolds
  - **Core Governance Primitives**: Core Governance Reward Primitive
  - **Omni Documents** (`A.6.1.1.6.3`): Sky Forum reference, Sky Ecosystem Emergency Response, Agent-Specific Emergency Response

### Context
PR #133 is the formal onboarding of Pattern (internally referred to as "Launch Agent 5" at inception) into the Atlas — the full scope framework that was published here represents Pattern's structural blueprint at launch. The sheer volume of documents (350+ new Atlas nodes) reflects the boilerplate-heavy pattern of Prime Agent artifact scaffolding established with earlier agents. Pattern's first active token (Ozone) appears as a completed Agent Token Primitive instance.

---
