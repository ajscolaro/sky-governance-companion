# Support Scope — Change History

Atlas path: `A.2` — The Support Scope

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

## PR #133 — 2025-12-01 AEW Proposal
**Merged:** 2025-12-04 | **+1987/-171 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.2.3.1.2.1.2.6.1` - Sky Core Vault Income [Core]
- **Added** `A.2.3.1.2.1.2.6` - Other Income [Core]
- **Added** `A.2.3.1.2.1.2.6.2` - LitePSM Income [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---

## PR #186 — 2026-02-16 AEW proposal
**Merged:** 2026-02-22 | **+2119/-158 lines**

### Raw Changes (rewrite with /atlas-track)
- **Added** `A.2.11.1.2.2.3.1` - Agreement URI Parameter [Core]
- **Added** `A.2.11.1.2.2.3.2.1` - Bounty Cap USD Parameter [Core]
- **Added** `A.2.11.1.2.2.2` - Agreement Address [Core]
- **Added** `A.2.11.1.2.2.3.2` - Bounty Terms Parameters [Core]
- **Added** `A.2.11.1.2.2.3.2.2` - Bounty Percentage Parameter [Core]
- **Added** `A.2.11.1.2.2` - Execution [Core]
- **Added** `A.2.11.1.2.6` - Agreement Fact Page [Core]
- **Added** `A.2.11.1.2.2.1` - Safe Harbor Registry Contract [Core]
- **Added** `A.2.11.1.2.2.3.2.3` - Diligence Requirements Parameter [Core]
- **Added** `A.2.11.1.2.2.3.5` - Protocol Name Parameter [Core]
- **Added** `A.2.11.1.2.2.3.3.2` - Asset Recovery Addresses [Core]
- **Added** `A.2.11.1.2.4` - Frontends [Core]
- **Added** `A.2.11.1.2.2.3.2.4` - Identity Parameter [Core]
- **Added** `A.2.11.1.2.5` - Prime Responsibilities [Core]
- **Added** `A.2.11.1.2.2.3.4` - Contact Details [Core]
- **Added** `A.2.11.1.2.2.3.2.5` - Retainable Parameter [Core]
- **Added** `A.2.11.1.2.2.3.3` - Chains Parameter [Core]
- **Added** `A.2.11.1.2.2.3` - Execution Parameters [Core]
- **Added** `A.2.11.1.2.2.3.3.1` - Chain IDs [Core]
- **Added** `A.2.11.1.2` - Safe Harbor [Core]
- **Added** `A.2.11.1.2.1` - Agreement [Core]
- **Added** `A.2.11.1.2.2.3.3.3` - Accounts [Core]
- **Added** `A.2.11.1.2.3` - Maintenance [Core]

<!-- REWRITE THIS ENTRY: Read the diff and current Atlas to classify changes as
     Material (with before→after values) vs Housekeeping (one-line summaries).
     Replace this section with ### Material Changes and ### Housekeeping.
     See /atlas-track skill for the target format. -->

---
