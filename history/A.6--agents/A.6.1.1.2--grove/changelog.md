# Grove (GLL) — Change History

Atlas path: `A.6.1.1.2` (1489 docs)

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

## PR #110 — Nov 10 edit
**Merged:** 2025-11-13 | **Type:** Weekly edit

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

## PR #133 — 2025-12-01 AEW Proposal
**Merged:** 2025-12-04 | **+1987/-171 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.2.2` - Deposit Address (Mainnet) [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.1.4` - Token [Core]
- **Added** `A.6.1.1.2.2.6.1.1.2.1.9` - Galaxy [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2` - Parameters [Core]
- **Added** `A.6.1.1.2.3.6.5` - Authorization With Respect To FalconX [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.1` - Instance Identifiers [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.1.2` - Target Protocol [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.1.3` - Asset Supplied By Grove Liquidity Layer [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1` - Ethereum Mainnet - Agora AUSD Instance Configuration Document [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.1` - RRC Framework Full Implementation Coverage [Core]
- **Added** `A.6.1.1.2.2.6.1.2.1.1.1.1.2.4` - Circle CCTP v2 Base To Mainnet [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.5` - Off-chain Operational Parameters [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.3` - Rate Limit IDs [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.4.1` - Deposit Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11` - Agora [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.1` - RRC Framework Full Implementation Coverage [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.2` - Contract Addresses [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.2` - Contract Addresses [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.4` - Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.1.2.1.11` - Agora [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2` - Ethereum Mainnet - Monad Morpho Grove x Steakhouse High Yield Vault AUSD Instance Configuration Document [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1` - Ethereum Mainnet - Ripple RLUSD Instance Configuration Document [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.3` - Rate Limit IDs [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.4.1` - Deposit Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.1.3` - Asset Supplied By Grove Liquidity Layer [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.3` - Instance-specific Operational Processes [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.2` - Contract Addresses [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.1.2` - Target Protocol [Core]
- **Added** `A.6.1.1.2.2.6.1.2.1.1.1.1.2` - Base [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.1` - RRC Framework Full Implementation Coverage [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.1` - Instance Identifiers [Core]
- **Added** `A.6.1.1.2.2.6.1.1.2.1.10` - Ripple [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.3` - Instance-specific Operational Processes [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.3` - Rate Limit IDs [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.2.3` - Underlying Asset Address [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.2` - Contract Addresses [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.2.2` - Underlying Asset Address [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2` - Parameters [Core]
- **Added** `A.6.1.1.2.2.6.1.2.1.1.1.1.2.2` - Grove Receiver [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.3` - Instance-specific Operational Processes [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.4` - Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.1` - Instance Identifiers [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.4` - Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.3.1` - Inflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.2.1.1.1.1.2.3` - Circle CCTP v2 Mainnet To Base [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.4.1` - Deposit Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1` - Ethereum Mainnet - Galaxy Arch CLOs Instance Configuration Document [Core]
- **Added** `A.6.1.1.2.2.6.1.1.2.1.12` - Uniswap [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.3` - Instance-specific Operational Processes [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.2.1` - Token Address (Monad) [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.1` - RRC Framework Full Implementation Coverage [Core]
- **Added** `A.6.1.1.2.2.6.1.1.2.1.10.1` - Ethereum Mainnet - Ripple RLUSD Instance Configuration Document Location [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.3.2` - Outflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.2.2` - Underlying Asset Address [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.1.4` - Token [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.5` - Off-chain Operational Parameters [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.1.1` - Network [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.1.2` - Target Protocol [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.3` - Rate Limit IDs [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.4.1` - Deposit Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.3` - Instance-specific Operational Processes [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.1.2` - Target Protocol [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.4.2` - Withdrawal Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.2.2` - Underlying Asset Address [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.2.1` - Token Address (Avalanche) [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.3.2` - Outflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.3.1` - Inflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.4.2` - Withdrawal Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.2` - Contract Addresses [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.1.4` - Token [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10` - Ripple [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.1.1` - Network [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.1.1` - Network [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.4.2` - Withdrawal Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.1.4` - Token [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.2.1` - Token Address [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.1.3` - Asset Supplied By Grove Liquidity Layer [Core]
- **Added** `A.6.1.1.2.2.6.1.2.1.1.1.1.2.1` - Grove Executor [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.5` - Off-chain Operational Parameters [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.1.3` - Asset Supplied By Grove Liquidity Layer [Core]
- **Added** `A.6.1.1.2.2.6.1.1.2.1.9.1` - Ethereum Mainnet - Galaxy Arch CLOs Instance Configuration Document Location [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.5` - Off-chain Operational Parameters [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.2.1` - Token Address [Core]
- **Added** `A.6.1.1.2.2.6.1.1.2.1.7.2` - Ethereum Mainnet - Monad Morpho Grove x Steakhouse High Yield Vault AUSD Instance Configuration Document Location [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.1` - Instance Identifiers [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.3.2` - Outflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.1.1` - Network [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.4.2` - Withdrawal Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1` - Ethereum Mainnet - Monad Uniswap AUSD/USDC Instance Configuration Document [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.3.1` - Inflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.3` - Rate Limit IDs [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.4.2` - Withdrawal Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.3.2` - Outflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.4` - Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.4` - Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.1.1` - Network [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2` - Parameters [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.1.4` - Token [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.3.2` - Outflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.3.1` - Inflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.1.2.1.12.1` - Ethereum Mainnet - Monad Uniswap AUSD/USDC Instance Configuration Document Location [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9` - Galaxy [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12` - Uniswap [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.3.1` - Inflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.1.2.1.11.1` - Ethereum Mainnet - Agora AUSD Instance Configuration Document Location [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.1.2.5` - Off-chain Operational Parameters [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2` - Parameters [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.1.3` - Asset Supplied By Grove Liquidity Layer [Core]
- **Added** `A.6.1.1.2.2.6.1.2.1.1.1.1.1` - Ethereum Mainnet [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.4.1` - Deposit Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2.2.2` - Underlying Asset Address [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.7.2.2.2.1` - Token Address (Monad) [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.2` - Parameters [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.11.1.1` - RRC Framework Full Implementation Coverage [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.10.1.2.1` - Instance Identifiers [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.12.1.2.1.2` - Target Protocol [Core]
- **Modified** `A.6.1.1.2.2.6.1.1.2.1.8` - Securitize [Core]
- **Modified** `A.6.1.1.2.2.6.1.2.1.1.1.1.1.2` - Allocator Oracle Contract [Core]
- **Modified** `A.6.1.1.2.2.6.1.2.1.1.1.1.1.1` - Allocator Buffer Contract [Core]
- **Modified** `A.6.1.1.2.2.6.1.2.1.1.1.1.1.5` - Allocator Vault (Bloom-A) Contract [Core]
- **Modified** `A.6.1.1.2.2.6.1.3.1.8` - Securitize [Core]
- **Modified** `A.6.1.1.2.2.6.1.2.1.1.1.1.1.4` - Allocator Roles Contract [Core]
- **Modified** `A.6.1.1.2.2.6.1.2.1.1.1.1.1.3` - Allocator Registry Contract [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #186 — 2026-02-16 AEW proposal
**Merged:** 2026-02-22 | **+2119/-158 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.1` - Instance Identifiers [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.1.1` - Network [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.5.1` - Interim Deployment [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.4.1` - Deposit Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.1.1` - Network [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.5.1.2` - Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.4.1` - Deposit Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2` - Ethereum Mainnet - Galaxy Warehouse Instance Configuration Document [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.4` - Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.3.1` - Inflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.3.2` - Outflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.1.2.3.1.2` - Base - Steakhouse Prime Instant USDC Morpho Vault V2 Instance Configuration Document Location [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.2` - Contract Addresses [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.1.2` - Target Protocol [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.2.2` - Underlying Asset Address [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.1.3` - Asset Supplied By Grove Liquidity Layer [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.4.3` - Max Exchange Rate [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.1.4` - Token [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.2.1` - Deposit Address (Mainnet) [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.5` - Off-chain Operational Parameters [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.3` - Instance-specific Operational Processes [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.1` - RRC Framework Full Implementation Coverage [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.4` - Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.2.2` - Underlying Asset Address [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2` - Parameters [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.3.1` - Inflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.1` - Instance Identifiers [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.5.1.1` - Maximum Allocation [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.1` - RRC Framework Full Implementation Coverage [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.5` - Off-chain Operational Parameters [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.2` - Contract Addresses [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.3` - Rate Limit IDs [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.3` - Instance-specific Operational Processes [Core]
- **Added** `A.6.1.1.2.2.6.1.1.2.1.9.2` - Ethereum Mainnet - Galaxy Warehouse Instance Configuration Document Location [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.4.2` - Withdrawal Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.3.2` - Outflow RateLimitID [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.4.2` - Withdrawal Rate Limits [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.1.2` - Target Protocol [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.3` - Rate Limit IDs [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2` - Parameters [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2` - Base - Steakhouse Prime Instant USDC Morpho Vault V2 Instance Configuration Document [Core]
- **Added** `A.6.1.1.2.2.6.1.3.1.9.2.2.1.3` - Asset Supplied By Grove Liquidity Layer [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.2.1` - Token Address [Core]
- **Added** `A.6.1.1.2.2.6.1.3.3.2.2.1.4` - Token [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---
