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
