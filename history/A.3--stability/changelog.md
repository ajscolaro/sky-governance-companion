# Stability Scope — Change History

Atlas path: `A.3` — The Stability Scope

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

## PR #110 — Nov 10 edit
**Merged:** 2025-11-13 | **Type:** Weekly edit

### Material Changes
- **Actively Stabilizing Collateral Incentive introduced** (A.3.4, new): `Eligible ASC * (Base Rate - Treasury Bill Rate)` per block; paid monthly via Settlement Cycle. Treasury Bill Rate = 91-day US T-bill yield.
- **Resting ASC updated** (A.3.4): added "Cash Stablecoins in Uniswap (paired with USDS)"
- **Latent ASC updated** (A.3.4): "Cash Stablecoins in Uniswap" → "Cash Stablecoins in Uniswap (not paired with USDS)"
- **Agent Credit Line Borrow Rate** (A.3.2): now may vary by Prime Agent credit rating per Spell Security Registry
- **Prime Agent Credit Rating System** (A.3.2): Spell Security Incident Registry added as explicit factor

### Context
The ASC Incentive compensates Primes for the opportunity cost of maintaining liquid stablecoin buffers — the spread between the Sky Base Rate and risk-free T-bill rate. Combined with the Spell Security Registry linkage to credit ratings, this creates a dual incentive: maintain liquidity (ASC Incentive) and maintain spell quality (favorable credit rating).

---

## PR #89 — 2025-10-20 Atlas Weekly Cycle Proposal
**Merged:** 2025-10-23 | **Type:** Weekly edit

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
**Merged:** 2025-09-26 | **Type:** Weekly edit

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

## PR #133 — 2025-12-01 AEW Proposal
**Merged:** 2025-12-04 | **+1987/-171 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.3.5.3.2` - Capital Targets [Core]
- **Added** `A.3.5.3.1.2` - Aggregate Backstop Capital [Core]
- **Added** `A.3.5.3.2.2` - Capital Retention To Achieve Target Aggregate Backstop Capital [Core]
- **Added** `A.3.5.3.1.3` - Allocated Genesis Capital [Core]
- **Added** `A.3.5.3.1.1` - Aggregate Capital Buffer [Core]
- **Added** `A.3.5.3.1` - Capital Types [Core]
- **Added** `A.3.5.3` - Sky Capital [Section]
- **Added** `A.3.5.3.2.1` - Target Aggregate Backstop Capital [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---
