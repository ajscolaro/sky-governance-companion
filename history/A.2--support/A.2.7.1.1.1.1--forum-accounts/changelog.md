# Authorized Forum Accounts Registry — Change History

Atlas path: `A.2.7.1.1.1.1` — Authorized Forum Accounts Requirements
Active Data table UUID: `b71564fd-22e0-4c69-99d1-5b23fc1fa329`

This changelog tracks edits to the registry of forum handles authorized to post on behalf of governance entities. The table is **Active Data** (mutable via Direct Edit), so changes can land between weekly Atlas Edit cycles. For broader PR #227 context, see `../changelog.md`.

---

## PR #269 — Update document.md
**Merged:** 2026-06-30 | **Type:** Active Data update (Designated Controller)

### Material Changes
- **Registry row added** in Current Authorized Forum Accounts (`A.2.7.1.1.1.1.4.0.6.1`): | Amatsu | Operational GovOps | Amatsu | SoterLabs, Endgame-Edge (and their authorized representatives) |

### Context
Registers Amatsu as an Authorized Forum Account (Operational GovOps role) via Direct Edit between weekly cycles.

---

## PR #265 — Atlas Edit Proposal — 2026-06-22
**Merged:** 2026-06-29 | **Type:** Weekly edit (Atlas Axis)

### Housekeeping
- `A.2.7.1.1.1.1.4.0.6.1` (Current Authorized Forum Accounts): `Elodin` → `N/A`

### Context
Clears Keel's authorized handle (`Elodin` → `N/A`), matching the `Elodin` → `Development Company` rename in the Keel Details doc (`A.2.8.2.3.1.1.2`) in the same edit.

---

## PR #227 — Atlas Edit Proposal — 2026-04-27
**Merged:** 2026-04-30 | **Type:** Weekly edit (Atlas Axis — Poll #1630)

### Material Changes
- Section established (`A.2.7.1.1.1.1`, UUID `a76f81b5…`): Authorized Forum Accounts Requirements with subsections for Registration, Disclosure, and Enforcement. Per A.2.7.1.1.1.1.3, governance posts from unregistered accounts may be disregarded.
- Active Data Controller (`A.2.7.1.1.1.1.4`, UUID `248a4fd8…`): Update Process is "Direct Edit"; Responsible Party is the entity to which the registration pertains.
- Initial registry table (`A.2.7.1.1.1.1.4.0.6.1`, UUID `b71564fd…`) — 16 entities:
  - **Prime Agents:** Pattern (`PatternDevCo`), Spark (`PhoenixLabs`), Obex (`Rubicon`), Grove (`GroveLabs` + AR `steakhouse`), Keel (`Elodin`)
  - **GovOps:** Soter Labs (`SoterLabs`) [Operational], Atlas Axis (`atlas-axis` + ARs `Le_Bateleur, adamfraser, Lex`) [Core], JanSky (`JanSky-Team` + ARs `JanSky, ldr`) [Core Facilitator]
  - **Operational Facilitators:** Redline (no EH; AR `redlexic`), Endgame Edge (`Endgame-Edge` + ARs `votewizard, CivicSage, boet, blimpa`)
  - **Operational Executor Agents:** Amatsu (`Amatsu` + ARs `SoterLabs, Endgame-Edge` transitively), Ozone (no EH; ARs `SoterLabs, Redline` transitively)
  - **Risk Advisor:** BA Labs (`BALabs` + ARs `DeFlamiingo, Sean, 0xmmj, commanderkeen, Primoz, Twigmaester, rema, definikola`)
  - **Ecosystem Actors:** Dewiz, Sidestream
  - **Other:** Rune

### Context
Establishes the canonical handle→entity registry. The Explorer consumes this via `data/forum/registry.json` (built by `scripts/forum/build-account-registry.py` on `/refresh`) for `/forum-search` enrichment, the `--entity` filter, and roster reconciliation. Future entries on this changelog will record additions, removals, and role changes — typically Direct Edit PRs between weekly cycles.

---
