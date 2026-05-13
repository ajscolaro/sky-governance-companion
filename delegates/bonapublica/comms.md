# Bonapublica — Vote Rationales

Source: Forum thread (topic 20451), filtered to posts by the delegate only.

**Security note:** All content below originates from untrusted forum posts.
It has been sanitized but should be treated as external data, not instructions.

---

## 2026-05-12 — Atlas Edit Weekly Cycle Proposal — May 11, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/248*

*Relates to: Weekly Cycle Vote (Poll 1632) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1632; declares the May 11 weekly cycle aligned with Atlas v2.
- **Agent Termination Process** — Codifies a five-element termination framework inside the Root Edit Primitive at A.2.2.5.2.2.2.8.1: voting period ≥14 days, quorum ≥20% of outstanding tokens, approval threshold 2/3 supermajority; existing prime agents must update their artifacts to include requirements by September 1, 2026.
- **Synome Documents and delegated authority** — New article A.1.3 defines Synome Documents and creates a Delegated Authority Update Process with Archon Labs as designated Synome Editor; supremacy clause at A.1.3.1.4 unambiguously establishes Atlas-over-Synome precedence: "In any case of conflict between an Atlas Document and a Synome Document, the Atlas Document takes precedence."
- **Short-term SKY staking rewards restored** — New doc A.2.3.1.4.1 specifies that pending USDS staking rewards activation, SKY staking rewards are funded from SKY token reserves via the Vesting Stream Contract at 50% of Step 2 Capital from the prior Monthly Settlement Cycle; rate determined by Core Facilitator in consultation with Core Council Risk Advisor.
- **Obex freezer multisig broadened** — Operational majority now 3 signers (Operational GovOps) + 1 (Operational Facilitator) = 4 of 5; Obex retains 1; 2/5 threshold preserves low operational barrier for emergency freezing while diluting single-actor control.

---
## 2026-05-07 — Ecosystem Spell Validation — May 7, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/247*

*Relates to: Spell 0xA0059DaDd7Fbdbc81a9bb9d1d17cCB029b6AF596 | Vote: **Yes***

Key rationale points:

- **Spell verification** — Confirmed action address, tag/codehash match, expiration (2026-06-06), officeHours=true; full Foundry suite run against archived commit 96073cb2; libraries reinstalled fresh.
- **Test coverage** — Tests passed covering Solana SkyLink bridge unpause (including `testEthereumToAvalancheUsdsFlowDisabled`), GSM pause delay increase, April 2026 monthly settlement cycle, staking rewards update, and agent proxy spells.
- **Foundry upgrade** — First spell validated using Foundry v1.7.0 (previously v1.5.1-stable).

---

## 2026-05-05 — Atlas Edit Weekly Cycle Proposal — May 4, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/246*

*Relates to: Weekly Cycle Vote (Poll 1631) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1631; declares the May 4 weekly cycle aligned with Atlas v2.
- **Sky-Grove Ecosystem Accord** — Lands correctly into the A.2.8.2 naming scheme; back-referenced from Grove's engagement directory at A.6.1.1.2.3.5.3; base rate UUID, chronicle point reward instance, and accrual method internal links all align with Atlas v2.
- **Sky Savings Rate query documentation** — Adds onchain query documentation bridging the SSR spec to its concrete onchain getter; no contradictions; formula `(ssr / 1e27)^31_536_000 - 1` computes effective annual yield.
- **Legacy terminology cleanup** — Removes Governance Facilitator references and retires defunct liquidity bootstrapping program; no orphaned cross-references.
- **Solidity identifier fix** — Removes stray spaces from Solidity identifiers across Keel, Obex, and Pattern rate limit management sections; "solidity identifiers cannot contain spaces so any code or audit tool consuming atlas documented function, event, and struct names would have misparsed."

---

## 2026-04-28 — Atlas Edit Weekly Cycle Proposal — April 27, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/245*

*Relates to: Weekly Cycle Vote (Poll 1630) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1630; declares the April 27 weekly cycle aligned with Atlas v2.
- **TMF simplified to 4-step waterfall** — Step 1: Security & Maintenance (20%); Step 2: Aggregate Backstop Capital growth via three phases (phase 1: 50% retained until ABC reaches 150M turbo-fill floor, phase 2: graduated retention as ABC fills toward TABC=1.5% of USDS supply, phase 3: 0% retained); Step 3: SBE 45/45/10 (USDS rewards, SKY rewards, burn); Step 4: staking rewards distribution.
- **Authorized Forum Accounts registry** — Adds A.2.7.1.1.1.1 establishing a registry-of-record for governance actor forum identities with 14 entities populated; ties disclosure of representation to the Atlas.
- **GSM Pause Delay doubled** — A.1.9.3.1.2 changed from "24 hours" to "48 hours."
- **Protocol Security Workstream Lead** — Names "vamsi" as the Protocol Security Workstream Lead; creates a security role under A.1.7.1 as a sibling to the risk advisor.
- **Grove Foundation Q2 2026 grant** — 800K USDS/month from Grove's own treasury (not Sky's) to Grove Foundation; recipient address 0xE3EC4CC359E68c9dCE15Bf667b1aD37Df54a5a42.

---

## 2026-04-24 — Ecosystem Spell Validation — April 23, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/244*

*Relates to: Spell 0x06851b5235cefb29c60ef3b29eb1f661d960b125 | Vote: **Yes***

Key rationale points:

- **Spell verification** — Confirmed action address, tag/codehash match, expiration (2026-05-23 15:14 UTC), officeHours=true; full Foundry suite run against archived commit 9a59b426.
- **Test coverage** — Tests passed covering March 2026 monthly settlement cycle, staking rewards update, ALLOCATOR-BLOOM-A and ALLOCATOR-PATTERN-A DC-IAM parameters, Pattern ALM proxy whitelist, and agent proxy spells.
- **Dark spell check** — Standard constructor and execute pattern confirmed; not CREATE2 deployed; libraries reinstalled via `rm -rf ./lib && git submodule update --init --recursive`.

---

## 2026-04-22 — Atlas Edit Weekly Cycle Proposal — April 20, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/243*

*Relates to: Weekly Cycle Vote (Poll 1629) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1629; declares the April 20 weekly cycle aligned with Atlas v2.
- **Loss absorption sequence reordered** — Genesis Capital Backstop (A.3.7.1.6) now applied before SKY Backstop; SKY is now last resort after genesis agent capital is exhausted, making the policy "materially stricter on SKY holders."
- **Plasma SkyLink Bridge** — Adds A.1.9.4.1.4 section with L2GovernanceRelay at 0x5CE28f2dD353945db9AB3273A2a1dD1AB632e24b; token bridge validators LayerZero + Nethermind (2/2 quorum); governance bridge uses 4/7 DVN quorum; USDS rate limit 5M/day.
- **Ecosystem Upkeep simplification** — Removes market cap fee and distribution requirement primitives from A.2.2.6; replaces with a single 50bps of market cap/year fee paid monthly in USDS; updates all eight per-agent subtrees consistently.
- **Multisig Security Enforcement Framework** — New A.2.11.1.3 section (~70 subdocs) covering security guidelines, monitoring, registry, and noncompliance enforcement; effective 2026-05-20; high-value asset multisigs (>$1M) require >7 signers; baseline minimum 3 signers with >50% threshold.

---

## 2026-04-13 — Atlas Edit Weekly Cycle Proposal — April 13, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/242*

*Relates to: Weekly Cycle Vote (Poll 1628) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1628; declares the April 13 weekly cycle aligned with Atlas v2.
- **Grove Liquidity Layer update for April 23 spell** — Verifies USDS mint rate limits raised to 500M max/500M slope; Avalanche bridge rate limits (50M/50M ETH-to-Avax, 20M/20M Avax-to-ETH); Centrifuge JTRSY USDS vault added; Avalanche foreignController upgraded to v1.8.0.
- **Pattern Liquidity Layer documentation** — Verifies all contract addresses (mainnet controller, ALM proxy, rate limits, allocator buffer/vault, subProxy, relayer, freezer); rate limits confirmed (USDS mint 100M/50M, USDS to USDC 100M/50M, Maple LIMIT_4626_DEPOSIT 100M/20M).
- **Integrator Program transfer** — All Viridian Advisors references replaced with Operational GovOps across A.2.2.8.1.2.1 and beyond; complete and consistent.
- **RRC/CRR terminology correction** — Fixes "instance financial RRC ratio" to "instance financial CRR" and "instance administrative risk RRC" to "instance administrative RRC" across the risk framework.

---

## 2026-04-10 — Ecosystem Spell Validation — April 9, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/241*

*Relates to: Spell 0x70Da14478667C08320Ef65506063abba84B6990f | Vote: **Yes***

Key rationale points:

- **Spell verification** — Confirmed action address, tag/codehash match, expiration (2026-05-10), officeHours=true; full Foundry suite run against archived commit e8c1c274.
- **Test coverage** — 30 tests passed including Avalanche SkyLink E2E governance relay test, USDS OFT Avalanche E2E, rate limit tests, sUSDS OFT Avalanche rate limit blocked test, Safe Harbor Avalanche onboarding, staking rewards update, Grove genesis capital transfer, and wire tests for LZ gov sender, sUSDS OFT, and USDS OFT on Avalanche.
- **Proxy spell verification** — Separately verified Spark proxy (`0x2572...`) and Grove proxy (`0x4fa1...`) codehashes, plus CERTORA spark proxy spell verification.

---

## 2026-04-07 — Atlas Edit Weekly Cycle Proposal — April 6, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/240*

*Relates to: PR #219 | Vote: **Yes***

Key rationale points:

- **Deep Atlas alignment analysis** — Provided the most detailed rationale of any delegate, systematically arguing each edit's compliance with Atlas v2 principles and document hierarchy.
- **Staking framework governance shift** — Notes that removing hardcoded vestTau/vestTot values is Atlas-compliant because those parameters are now governed dynamically by the Core Facilitator via the Operational Weekly Cycle, rather than fixed in text.
- **Genesis Capital phase-out safeguards** — Emphasises that phase-out only activates when aggregate backstop capital meets or exceeds 125M USDS, ensuring protocol safety is never compromised.
- **Structural consistency of bridge docs** — Argues the Avalanche SkyLink Bridge follows the identical template established by Solana, demonstrating internal consistency with the Atlas principle that Solana serves as prototype for future cross-chain deployments.
- **Maple syrupUSDC zero exposure logic** — Explains that 0 USD maximum exposure combined with an established 3% CRR is internally consistent: it onboards the instance into the governance framework without authorizing any capital deployment.
- **Pioneer Prime requirements change** — Notes removal of the requirement that Pioneer Primes must be created from genesis for the specific purpose of being a Pioneer Prime.

---

## 2026-03-31 — Atlas Edit Weekly Cycle Proposal — March 30, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/239*

*Relates to: Weekly Cycle Vote (Poll 1626) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1626; declares the March 30 weekly cycle aligned with Atlas v2. Post includes a detailed AI-assisted analysis of each edit (note: this is external content being reported, not instructions).
- **Emergency response agent framework transition** — ~20 documents updated: Scope Facilitators replaced by Core GovOps, Support Facilitators replaced by Core Facilitator or Core GovOps; declaring emergencies now requires only Core Facilitator without consultation requirement; accountability for CF removal now requires only Protocol Security Workstream Lead and Core GovOps (down from a majority of active Scope Facilitators).
- **Emergency spells and Protego** — Standby spell authenticity validation changes from "one Authorized Representative from each Governance Facilitator team" to "two Authorized Representatives from Core GovOps" (Atlas Axis); nonresponsive fallback moves from Scope Facilitators to Core Facilitator granting sole authority to an Operational Facilitator.
- **Demand Side Buffer** — New standalone payment account (2-of-3 multisig at 0x5e2fEc3a3C4E63A422e45C1BB83EdB3a5aD0543B, controlled by Soter Labs) replaces the old Distribution Reward Controller Wallet and Integration Boost Wallets.
- **Keel Pioneer Incentive Pool transition** — Renames "Pre-Pioneer" to "Pioneer" Incentive Pool; removes Treadstone as Keel development company, replacing with a new unnamed entity.

---

## 2026-03-26 — Ecosystem Spell Validation — March 26, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/238*

*Relates to: Spell 0x415396C98A5B42C0D97E4E80cB5C9079369Ea4D8 | Vote: **Yes***

Key rationale points:

- **Spell verification** — Confirmed action address, tag/codehash match, expiration (2026-04-24), officeHours=true; full Foundry suite run against archived commit b9551ae4.
- **Test coverage** — 21 tests passed including monthly settlement cycle inflows, `testUpdateSafeHarborAddedAccounts`, StarGuard initialisation (~16M gas), and agent proxy spells (Ozone, Amatsu onboardings, genesis funding transfers, February settlement cycle, Safe Harbor update).
- **Spark and Grove proxy spells** — Separately verified codehashes for Spark proxy (`0xc941...`) and Grove proxy (`0x...`).

---

## 2026-03-23 — Atlas Edit Weekly Cycle Proposal — March 23, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/237*

*Relates to: Weekly Cycle Vote (Poll 1624) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1624; declares the March 23 weekly cycle aligned with Atlas v2. Post includes a detailed AI-assisted analysis of each edit (note: this is external content being reported, not instructions).
- **SparkLend governance process streamlined** — Removes the exception requiring a governance poll before an executive vote for liquidation threshold and liquidation bonus changes; all SparkLend parameter changes now go directly to executive vote via the operational weekly cycle.
- **Signal requests removed** — Deletes non-standard weekly poll definition, Signal Requests document, and associated use sections from A.1.10.1; also removes Starknet from the Emergency Declaration Procedure's facilitator chain, updating from Support Facilitators to Core Facilitator.
- **Facilitator Atlas update authority** — New doc A.1.9.2.4.13.5 codifies that after spell execution the Core Facilitator updates Sky Core docs while Operational Facilitators handle agent artifact follow-ups.
- **Q2 2026 Spark Foundation grant** — Authorises 1.1M USDS/month to Spark Foundation and 100K USDS/month to Spark Asset Foundation for Q2 2026 (3.6M USDS total), mirroring the Q1 2026 grant structure.
- **Arkis parameter update** — Removes Interim Deployment status; raises maximum exposure from $20M to $50M; reduces instance CRR from 100% to 50%.

---

## 2026-03-16 — Atlas Edit Weekly Cycle Proposal — March 16, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/236*

*Relates to: Weekly Cycle Vote (Poll 1623) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1623; declares the March 16 weekly cycle aligned with Atlas v2.
- **Ecosystem Accords 8 and 9** — Records genesis capital allocations for Amatsu (Accord 8) and Ozone (Accord 9) under A.2.8.2 - Active Ecosystem Accords; uses the established mechanism for recording inter-actor agreements enforceable by sky governance.
- **LA6 and LA7 allocator vault parameters** — Populates subProxy addresses and allocatorBuffer/vault directories in the allocation system primitive subtrees for both agents; consistent with how the Atlas structures liquidity layers and allocation system artifacts.
- **ACRDX ETH mainnet authorisation** — Straight extension of the existing pattern at A.3.2.2.1.1.1.5.3.1 - Instance Financial CRRs For Specific Assets; grounded by the sibling JTRSY/JAAA Avalanche restriction.
- **Multisig operator update** — Replaces Ozone and Amatsu as operational GovOps with Soter Labs across executor agent artifacts; good housekeeping and clean descriptive control metadata.

---

## 2026-03-12 — Ecosystem Spell Validation — March 12, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/235*

*Relates to: Spell 0x396122c087Aa23BeE53B38e14237B3C0C10DdDbc | Vote: **Yes***

Key rationale points:

- **Spell verification** — Confirmed action address, tag/codehash match, expiration (2026-04-11), officeHours=false; full Foundry suite run against archived commit 66dda238.
- **Test coverage** — 22 tests passed including `testAdoptSafeHarbor`, L2 governance relay tests for Arbitrum/Base/Optimism/Unichain, SKY buyback reduction, delayed upgrade penalty increase, and Spark proxy spell.
- **Dark spell check** — Standard execute pattern confirmed; not CREATE2 deployed.

---

## 2026-03-10 — Atlas Edit Weekly Cycle Proposal — March 9, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/234*

*Relates to: Weekly Cycle Vote (Poll 1620) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1620; declares the March 9 weekly cycle aligned with Atlas v2.
- **SKY buyback reduction** — Temporarily reduces SKY buyback share from 75% to approximately 7.5% (~37K USDS) of net profits for 3 months; keeps more profits as backstop capital while USDS supply scales to 11B; grounded by A.2.3.1.2.5.1.1 and A.2.3.1.2.5.1.2.
- **JAAA removal** — Removes JAAA from sky direct exposures active data list; notes the list type is explicitly "current" exposures, so removing a position that is no longer current is the correct maintenance action.
- **Sanctioned locations** — Adds entries to the existing full block geo list at A.5.4.1.4.1; "the cleanest housekeeping form of atlas alignment."
- **Safe Harbor address correction** — Manually verified contract `0xf17bB418B4EC251f300Aa3517Cb37349f17697A1` has a valid `getAgreementURI()` returning the correct IPFS link format; confirms the on-chain agreement reference is valid.

---

## 2026-02-27 — Ecosystem Spell Validation — February 26, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/233*

*Relates to: Spell 0x4C56b1B1554B1230349d66F665814641A609C569 | Vote: **Yes***

Key rationale points:

- **Spell verification** — Confirmed action address, tag/codehash match, expiration (2026-03-28), officeHours=true; full Foundry suite run against archived commit 76a11c67.
- **Test coverage** — 25 tests passed including monthly settlement cycle inflows, allocator integration, StarGuard initialisation (~25M gas), new line mom ilks, vested rewards distribution, and all agent proxy spells (Pattern, Skybase, Obex, Keel, Grove, Spark).
- **Spell scope** — Launch Agent onboardings, January monthly settlement cycle and TMF, SKY staking rewards normalisation, prime agent proxy spells.

---

## 2026-02-23 — Atlas Edit Weekly Cycle Proposal — February 23, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/232*

*Relates to: Weekly Cycle Vote (Poll 1619) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1619; declares the February 23 weekly cycle aligned with Atlas v2.
- **Amatsu/Ozone to Soter Labs** — Housekeeping update; preserves Amatsu as operational executor agent while updating operational GovOps function to Soter Labs; Solana LayerZero freezer multisig 2+2 split and 2/4 threshold maintained.
- **Skybase Governance Accessibility Reward instances** — Adds instances under the canonical storage locations A.6.1.1.4.2.7.1.1.2 and A.6.1.1.4.2.7.1.2; grounded by the atlas reward code framework.
- **Safe Harbor Starknet removal** — Removes a hardcoded chain list (ETH mainnet, Arbi, BASE, Starknet) and replaces it with a general rule that authorised chains are defined in subdocs; maintains consistency with A.2.11.1.2.2.3.3.
- **GitHub/Portal alignment (PR #178)** — Atlas explicitly recognises housekeeping items as maintenance/record-keeping; this PR normalises GitHub and Notion alignment.

---

## 2026-02-17 — Atlas Edit Weekly Cycle Proposal — February 16, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/231*

*Relates to: Weekly Cycle Vote (Poll 1618) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1618; declares the February 16 weekly cycle aligned with Atlas v2.
- **AD requirements tightened** — Adds 75% voting participation threshold over 6 months, "excessive abstention" handling, and requirement for substantive explanations posted within 1 week; anchored by A.1.5.3.3.1 and A.1.5.3.3.2; notes CF conflict-of-interest recusal now routes to Core GovOps adjudication.
- **Safe Harbor agreement** — Extends the bug bounty program at A.2.11.1.1 with a time-critical fund rescue mechanism for whitehats, structured bounty terms, and fast return to protocol custody; aligns with Atlas security thesis.
- **Anchorage risk parameter update** — Lowers CRR while increasing max exposure for Anchorage Digital; "deepens the relationship with anchorage digital and signals confidence in the arrangement."
- **New Launch Agent 7 artifact** — Added using the same copy-paste pattern validated for LA4–6; no structural deviations from the LA6 pattern, anchors with A.2.2 primitives subtree.
- **Housekeeping** — Renames Amatsu GovOps role to Soter Labs; updates Obex Foundation and Development Company names; adds Integration Boost instances (Curve and Morpho) to Skybase artifact.

---

## 2026-02-12 — Ecosystem Spell Validation — February 12, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/230*

*Relates to: Spell 0x97bD98F46D0d0769745883E76c05483f9aa15Ca6 | Vote: **Yes***

Key rationale points:

- **Spell verification** — Confirmed action address, tag/codehash match, expiration (2026-03-13), officeHours=false (no office hours restriction); full Foundry suite run against archived commit 4fd1dbb4.
- **Test coverage** — 15 tests passed including ALLOCATOR-NOVA-A DC-IAM parameters, RWA001-A stability fee reduction, prime agent proxy spells, SP-BEAM tau/bud values, and splitter; suite is lightweight (only 2 non-agent actions in this spell).
- **Dark spell check** — Standard execute pattern confirmed; not CREATE2 deployed.

---

## 2026-02-09 — Atlas Edit Weekly Cycle Proposal — February 9, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/229*

*Relates to: Weekly Cycle Vote (Poll 1617) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1617; declares the February 9 weekly cycle aligned with Atlas v2.
- **Ecosystem Accord update (Spark TGE)** — Adds a new defined concept for prime TGE and introduces token launch penalty settlement; removes penalty deduction language from A.2.8.2.2.2.8.2.
- **Core Governance Reward Primitive** — Extends A.2.2.10.1 to describe how SKY pays rewards to prime agents providing secure access to core governance features; fixes the step 1 capital math by adding the missing 1% (0.5%+0.5%) already in the Atlas.
- **Housekeeping sweep** — Removes legacy ranked delegate documents, updates Skybase distribution reward instance, removes Scope Advisor mentions, updates Core GovOps references, updates active data process to include Operational Facilitator, and removes stale internal references in Needed Research docs.

---

## 2026-02-03 — Atlas Edit Weekly Cycle Proposal — February 2, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/228*

*Relates to: Weekly Cycle Vote (Poll 1616) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1616; declares the February 2 weekly cycle aligned with Atlas v2.
- **Aggregate backstop capital tightening** — Limits the backstop metric to genesis capital still held in genesis agents' subProxies, excluding operational buffers; prevents the safety net from being overstated by liquid funds.
- **Allocator vault governance** — Centralises prime allocator vault risk parameters under Endgame_Transition stability measures, tying duty to SP-BEAM and credit line controls to DC-IAM per A.3.7.1.2.
- **Pattern artifact preparation** — Renames Launch Agent 5 to Pattern and fills in technical placeholders (subProxy, StarGuard, key allocator contract addresses).
- **Grove and Skybase expansions** — Adds a new Morpho active instance to Grove; replaces Skybase future iteration placeholders with concrete on-chain parameters in the artifact parameters section.

---

## 2026-01-29 — Ecosystem Spell Validation — January 29, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/227*

*Relates to: Spell 0x4d99868F6D4d2545EbFf3a1385efE31C06d3A472 | Vote: **Yes***

Key rationale points:

- **Spell verification** — Confirmed action address, tag/codehash match, expiration (2026-02-27), officeHours=true; full Foundry suite run against archived commit 53fc086b.
- **Test coverage** — 24 tests passed covering monthly settlement cycle inflows, allocator integration, StarGuard initialisation (30M+ gas test passed), Skybase onboarding, DAO resolution for 6s Capital, pattern onboarding, and prime agent proxy spells.
- **Dark spell check** — Standard constructor and execute pattern confirmed; not CREATE2 deployed.

---

## 2026-01-27 — Atlas Edit Weekly Cycle Proposal — January 26, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/226*

*Relates to: Weekly Cycle Vote (Poll 1615) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1615; declares the January 26 weekly cycle aligned with Atlas v2.
- **JAAA sky direct exposure cap** — Adds a cap for Grove in JAAA on ETH mainnet for up to 325M USDS to the current sky direct exposures active data list at A.2.2.9.1.1.1.1.2.0.6.1.
- **CRR codification** — Moves CRR and exposure cap rules into the risk framework's exceptions and asset-specific CRR sections at A.3.2.2.1.1.1.1.3 and A.3.2.2.1.1.1.5.3.1.
- **Skybase and LA6/LA7 ecosystem accords** — Updates token allocations and genesis capital terms inside proper accord substantive terms subdocuments; adds explicit transfer subdocument for the 5M USDS demand subsidies leg per A.2.8.2.7.2.2.2.
- **Housekeeping** — Corrects Grove Agora AUSD instance rate limit parameters; renames "Launch Agent 2" to actual agent name; cleans up Grove instance config document title.

---

## 2026-01-19 — Atlas Edit Weekly Cycle Proposal — January 19, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/225*

*Relates to: Weekly Cycle Vote (Poll 1614) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1614; declares the January 19 weekly cycle aligned with Atlas v2.
- **Grove Labs transfer** — Updates tokenomics and Grove artifact operational subdocuments covering treasury custody, transfer limits, and genesis distribution flow; grounded in A.2.9.2.2.2.1 and A.6.1.1.2.2.1.4.2.1.1.4.
- **Skybase introduction** — Adds a new active ecosystem accord and defines genesis capital allocation for a new genesis agent (Skybase) using the same direct-to-exec vote pattern as other agents.
- **Legacy payment removal** — Removes an expired "prior to January 1, 2026" exception that created a dedicated funding lane being superseded by the TMF; clean deletion without altering governance powers.
- **Atlas traceability improvement** — Creates a 1-to-1 relationship between an actionTenet and its primary doc, avoiding cross-target ambiguity between AC and AD misalignment swift action rules.

---

## 2026-01-16 — Ecosystem Spell Validation — January 15, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/224*

*Relates to: Spell 0xE91C453B7e1f4DF94fb4Cb69E1F4836E62718D76 | Vote: **Yes***

Key rationale points:

- **Spell verification** — Confirmed action address, tag/codehash match, expiration (2026-02-14), officeHours=true; full Foundry suite run against archived commit.
- **Test coverage** — Tests cover GUNI V3 DAI/USDC offboardings, reward distribution vest ID updates (USDS-SKY and LSSKY-SPK), SP-BEAM tau/bud values, prime agent proxy spells, and Keel SubProxy cross-chain whitelist; all pass.
- **Dark spell check** — Standard constructor pattern confirmed; not CREATE2 deployed.

---

## 2026-01-13 — Atlas Edit Weekly Cycle Proposal — January 12, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/223*

*Relates to: Weekly Cycle Vote (Poll 1613) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1613; declares the January 12 weekly cycle aligned with Atlas v2.
- **Maple CRR update** — Updates Maple syrupUSDC to a fixed 3% CRR within the exceptions framework at A.3.2.2.1.1.1.1.3.1; a straightforward refinement of an existing asset-specific carve-out.
- **Token rewards zeroed** — Setting SKY rewards for USDS users and SPK to stakers to zero is a governance-controlled configuration change; grounded by A.4.3.2 and A.4.4.1, which confirm SKY governance determines reward levels.
- **Spark Foundation transfer authorisation** — Clarifies the approval path for proposed Spark foundation grants under A.2.9.2.2.2.5.5, noting subsequent cash grants require sky consent via an atlas modification.
- **Housekeeping** — Renames "accessibilityReward" to "distributionReward" across primitives; corrects prime_subProxy to agent_subProxy; adds secondary relayer and standardises freezer multisig requirements in Grove.

---

## 2026-01-06 — Atlas Edit Weekly Cycle Proposal — January 5, 2026

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/222*

*Relates to: Weekly Cycle Vote (Poll 1612) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1612; declares the January 5 weekly cycle aligned with Atlas v2.
- **Grove artifact registry maintenance** — Updates the Grove liquidity layer's canonical address book to reflect current deployments; consistent with previously approved Grove changes from 2025-09-25.
- **Keel Solana artifact completion** — Adds the USDC token account used by the controller PDA to custody and transact USDC on Solana; completes the Keel Solana USDC reserve registry.

---

## 2025-12-16 — Atlas Edit Weekly Cycle Proposal — December 15, 2025

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/221*

*Relates to: Weekly Cycle Vote (Poll 1611) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1611; declares the December 15 weekly cycle aligned with Atlas v2.
- **Core Council Buffer signer expansion** — Moves from 3-of-4 to 5-of-6, adding Operational GovOps Soter Labs; maintains shared control between core facilitators and GovOps.
- **Ecosystem Accord 6 (Launch Agent 6)** — Adds accord terms under A.2.9.2 - Active Ecosystem Accords, recording the LA6 agreement and its accord key details.
- **Anchorage risk requirements** — Extends the exceptions subtree at A.3.2.2.1.1.1.1.3 with a 3.5% CCR and 200M USDS max exposure for Anchorage.
- **StarGuard default-on** — Makes StarGuard the default for every SubProxy deployment; anchors with A.1.9.2.3.2.2.3.1.1.

---

## 2025-12-11 — Ecosystem Spell Validation — December 11, 2025

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/220*

*Relates to: Spell 0x0D2BDA9a446527238E802708B370DD66f375E4d1 | Vote: **Yes***

Key rationale points:

- **Spell verification methodology** — Ran full Foundry suite (26 passed, 0 failed) plus a custom pre-cast shell script that verified CCEA1 StarGuard configuration, SubProxy wards, and pre-init state; all critical checks passed.
- **CCEA1 StarGuard initialisation** — Confirmed `testStarGuardInitialization` passes; pre-init state checks verified StarGuard has no pre-plotted spell and MCD_PAUSE_PROXY is a ward.
- **Contract authenticity** — Verified not a dark spell; no assembly blocks, no delegatecall/callcode/selfdestruct, no suspicious payments; all actions match executive document.
- **Test coverage** — Tests cover USDS-SKY farm normalisation, MKR-SKY delayed upgrade penalty increase, stUSDS liquidation ratio and capped OSM, BEAM step parameters, DAO resolution, ranked delegate compensation, and prime agent proxy spells.

---

## 2025-12-08 — Atlas Edit Weekly Cycle Proposal — December 8, 2025

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/219*

*Relates to: Weekly Cycle Vote (Poll 1609) + stUSDS BEAM Parameter Update (Poll 1610) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll 1609 (weekly cycle) and Poll 1610 (stUSDS BEAM update).
- **Core Council Buffer consolidation** — Re-states the buffer's purpose and mandates consolidation from legacy accounts; consistent with A.2.4.1.4.1.1.1.
- **Risk parameter updates** — Adds Kamino/Drift exceptions under A.3.2.2.1.1.1.1.3; stUSDS liquidation parameter changes fall within Core Executor Agent mandate per A.4.4.1.3.6.1.
- **BEAM parameter governance** — Notes that A.4.4.1.3.8.3 allows all stUSDS BEAM parameters to be modified by Core Executor Agents in consultation with the Core Council Risk Advisor (BA Labs); BA Labs explicitly acts as risk advisor recommending the Poll 1610 changes.
- **Interim deployment cleanup** — Deletes the Galaxy interim deployment block (100% CRR/25M cap) from Grove and Keel artifacts; per A.1.9.2.3.2.2.2, interim guards are temporary and should be removed once validated.
- **New Launch Agent 6 artifact** — Added using the same hierarchical shell as LA4 and LA5; anchors with A.6.1.1 and primitive subdocs.

---

## 2025-12-02 — Atlas Edit Weekly Cycle Proposal — December 1, 2025

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/218*

*Relates to: Weekly Cycle Vote (Poll 1608) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1608; declares the December 1 weekly cycle aligned with Atlas v2.
- **Capital type documentation** — Formalises capital classification and target-setting; anchors with A.3.5 (Surplus Buffer) and step 0 references without changing smart burn mechanics.
- **Ranked delegate system update** — Preserves core facilitator verification, misalignment blocks, and minimum participation while enabling ranked ADs to author and trigger their own edits under core facilitator oversight.
- **TMF net revenue clarity** — Keeps step 0 as a pure accounting gate and clarifies cash-basis recognition across surplus/CC buffer/AD buffer flows; anchors with A.2.4.1.2.1.2.1.
- **Grove artifact maintenance** — Adds galaxy, Ripple RLUSD, Agora AUSD, Uniswap, and Keel Ethereum freezer signer updates; all within artifact scope and allocation system framework.

---

## 2025-11-28 — Ecosystem Spell Validation — November 27, 2025

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/217*

*Relates to: Spell 0xa57d885d8FB034455aADb8c3F3D5414c214cBe3d | Vote: **Yes***

Key rationale points:

- **Spell verification methodology** — Published full Foundry test results (26 passed, 0 failed) against the archived spell commit, confirming bytecode matches and all pre-cast checks pass.
- **Contract authenticity** — Confirmed action address 0x1464e3680F1B39a89699830d38a73ac0e88a6506 via `cast call action()(address)` and verified on-chain hash against local build.
- **Test scope** — Tests cover StarGuard launch, monthly settlement cycle inflows, SP-BEAM tau/bud values, splitter, payments, and prime agent proxy spells; all pass.
- **Dark spell check** — Confirmed standard `execute() external limited { actions(); }` constructor pattern; not deployed using CREATE2.

---

## 2025-11-25 — Atlas Edit Weekly Cycle Proposal — November 24, 2025

*Source: https://forum.skyeco.com/t/bonapublica-aligned-delegate-communication/20451/216*

*Relates to: Weekly Cycle Vote (Poll 1607) | Vote: **Yes***

Key rationale points:

- **Overall alignment** — Voted YES on Poll ID 1607; declares the November 24 weekly cycle aligned with Atlas v2.
- **CCEA1 genesis capital** — Ecosystem Accord 5 creates Core Council Executor Agent 1 with a 25M USDS genesis capital split: 20M to CCEA1 subProxy and 5M to the core council buffer with accounting rules; fits Atlas ecosystem accords and core council mandate.
- **Ranked delegate compensation** — Modernises AD tiers, removes legacy sections, aligns with the October 27 TMF edit that dedicates 1% of step 1 capital to the AD buffer and creates the AD buffer multisig.
- **Obex rename** — Update Agent Artifact is essentially a rename from Launch Agent 4 to Obex across the Atlas.
- **Subsidised borrowing date fix** — Replaces vague "trigger before end of 2025" with a fixed start date of 2026-01-01 and a 2-year borrow rate ramp per A.2.9.2.2.2.2.2.
- **StarGuard standardisation** — Removes the transition carve-out, standardising on StarGuard for Primes; matches Atlas security and resilience intent.

---

