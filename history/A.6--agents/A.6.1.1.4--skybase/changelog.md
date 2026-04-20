# Skybase — Change History

Atlas path: `A.6.1.1.4` (722 docs)

---

## PR #186 — 2026-02-16 AEW proposal
**Merged:** 2026-02-22 | **Type:** Weekly edit (Atlas Axis — Poll 1618) | **+2119/-158 lines**

### Material Changes

- **New instance: Curve Integration Boost** (`A.6.1.1.4.2.5.2.2.2`, new Instance Configuration Document): onboards the Curve Finance integration
  - Integration Partner: Curve; Reward Address: `0xa7843f843d29ca33ba48d9d1335b774eecc328dc`; Chain: Ethereum Mainnet
  - Cadence: **weekly**; Data Submission Responsible Actor: **Core Council Risk Advisor**
  - Data endpoint: `https://info-sky.blockanalitica.com/api/v1/incentivized-pools/`
  - Savings Rate Adjustment: per-block values for USDS in Curve vs. Sky Savings Rate
  - Inherits base routine protocol from `A.2.2.8.1.2.4.1`; no agent-specific customizations
- **New instance: Morpho Integration Boost** (`A.6.1.1.4.2.5.2.2.3`, new Instance Configuration Document): onboards the Morpho integration
  - Integration Partner: Morpho; Reward Address: `0xa7843f843d29ca33ba48d9d1335b774eecc328dc` (same as Curve)
  - Chain: Ethereum Mainnet; Cadence: **weekly**; Data Submission Responsible Actor: Core Council Risk Advisor
  - Same data endpoint as Curve; same per-block-USDS-vs-SSR adjustment strategy
  - No customizations; Integration Boost Payments Active Data list initialized empty

### Housekeeping

- Added Instance Configuration Document Location pointers at `A.6.1.1.4.2.5.2.1.2.2` (Curve) and `A.6.1.1.4.2.5.2.1.2.3` (Morpho) in the Active Instances Directory

### Context

Skybase's Integration Boost Primitive grows from a single Euler instance to three with the addition of Curve and Morpho — the two largest DeFi venues for USDS liquidity after Aave. The shared reward address across Curve and Morpho suggests a common distribution contract, and the Core Council Risk Advisor is designated Data Submission Responsible Actor for both, consistent with the role's scope established by PR #89. Operational logic is entirely inherited from the Sky Core base class, meaning rate-adjustment methodology is uniform across Skybase's Integration Boost instances. The empty Integration Boost Payments lists indicate the instances are configured but not yet paying out at merge. SKY ~$0.065, USDS supply ~$9.9B at merge.

---

## PR #167 — 2026-01-19 edit
**Merged:** 2026-01-22 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **Launch Agent 3 renamed to Skybase** throughout the Atlas: agent Artifact header (A.6.1.1.4), full Primitives scaffold, and all LA3 cross-references.
- **Skybase frontend rebranded to Sky.money** (A.6.1.1.4.2.5.1.*): "Launch Agent 3 Frontend App" → "Sky.money App"; "Launch Agent 3 Frontend Open Source Widgets" → "Sky.money Open Source Widgets" (both Instance Configuration Document and Location pointers renamed).
- **Ecosystem Accord 7: Sky and Skybase** added (A.2.8.2.7, new): formalizes Skybase's relationship with Sky; parties = Sky and Skybase; duration indefinite, commencing from 2024-09-01; substantive terms to be specified in a future iteration.
- This PR also added Ecosystem Accord 5 (Sky and Core Council Executor Agent 1) and Ecosystem Accord 6 (Sky and Launch Agent 6) — see A.2 changelog if/when processed.

### Context
Public-name reveal for Launch Agent 3, bundled with the onboarding of Skybase's dedicated Ecosystem Accord (Accord 7) and Accords 5/6 for other entities. Rename-only backfill — the rest of this PR's content and the new Accords' substantive terms have not been processed in detail.

---
