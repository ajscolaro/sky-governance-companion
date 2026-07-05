# Aligned Delegate Roster — Change History

Atlas path: `A.1.5.1.5` — List of Recognized Aligned Delegates (Core), with
the Active Data table at `A.1.5.1.5.0.6.1`. Mutates whenever an AD is
formally recognized, derecognized, or has identifying data updated (e.g.
contract migrations).

Roster changes have historically arrived as Flow 1 (weekly Atlas Edit
Proposals); going forward, equivalent registry-only updates may also arrive
as Flow 3 (Active Data Direct Edit) at the Core Facilitator's discretion.

Framework PRs that touched the AD roster as part of larger structural
changes (e.g. PR #186 renumbering `A.1.5.1.4` → `A.1.5.1.5` to make room for
the Probationary Period) remain in the parent `../changelog.md`.

---

## PR #257 — Derecognize Kuzmich, add new breaches
**Merged:** 2026-06-11 | **Type:** Active Data update (Designated Controller)

### Material Changes
- **Registry row added** in Current Aligned Delegates (`A.1.6.1.5.0.6.1`): | Delegate Name | EA Address | Delegation Contract | Forum Post |

### Context
Kuzmich is removed from the Current Aligned Delegates roster (derecognized; see the matching Derecognized-list entry in `../changelog.md`). The diff also reformats the roster table to the compact style, so the captured "row" is the header line.

---

## PR #194 — add Brendan Navigator
**Merged:** 2026-03-09 | **Type:** Active Data update (Core Facilitator)

### Material Changes
- **Current Aligned Delegates** (`A.1.5.1.5` Active Data table): Brendan Navigator added as a new recognized AD.
  - Hot wallet: `0xecDD304bB96cC7A6d745D9534Ce4d12f2A134058` (verifySig/303125)
  - Cold wallet: `0x8a8D131502bb4868A0777bEf604547A8316a8f11` (verifySig/303124)
  - Forum submission: https://forum.sky.money/t/brendan-navigator-ad-recognition-submission/27748
  - Existing entries OPEX and AxisLegati reformatted (column-width alignment only; addresses and sigs unchanged).

---

## PR #173 — derecognize Sky Staking
**Merged:** 2026-01-27 | **Type:** Active Data update (Core Facilitator)

### Material Changes
- **AD derecognized**: Sky Staking — removed from the Recognized Aligned Delegates table and added to the Derecognized Alignment Conservers registry (`A.1.4.10.2.0.6.1`) dated 2026-01-27, reason **misalignment**. Forum: https://forum.sky.money/t/ad-derecognition-due-to-misalignment-2026-01-27/27655

### Context
Sky Staking was recognized as an AD in PR #6 (2025-06-16) and derecognized here ~7 months later. Unlike the 2023–2024 derecognitions (operational-security breaches / failure to migrate), this one is logged as a misalignment derecognition.

---

## PR #169 — Add OPEX
**Merged:** 2026-01-21 | **Type:** Active Data update (Core Facilitator)

### Material Changes
- **New AD recognized**: OPEX — recognition address `0xE3dc949720Da42c5c842D06974BCB7B03F4f604f`, vote contract `0x16A5a76904140e01F31C7e7ABD9fB81988469bA4`, forum: https://forum.sky.money/t/opex-ad-recognition-submission/27630

### Context
Standalone single-AD addition to the Recognized Aligned Delegates Active Data table. OPEX appears as an active AD in later governance records (e.g. listed among non-voters in Poll #1633, PR #246).

---

## PR #25 — New AD added - Kuzmich
**Merged:** 2025-07-07 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New AD recognized**: Kuzmich — recognition address `0x2847540606a790E5083d0D63470fAb01344c8e92`, vote contract `0x2C89024c13A80bC1B662A3dB990524652C15221C`, forum: https://forum.sky.money/t/ad-recognition-submission/26743

---

## PR #6 — Update Multiple ADs
**Merged:** 2025-06-16 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **8 ADs updated to v3 voting contracts**: Bonapublica, PBG, WBC, BLUE, Cloaky, AegisD, Excel, Tango — new contract addresses and verification signatures recorded in the AD Active Data table.
- **New AD recognized**: Sky Staking (recognition address `0x05c73AE49fF0ec654496bF4008d73274a919cB5C`).

---

## PR #14 — Derecognize ADs that failed to migrate
**Merged:** 2025-06-13 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **12 ADs derecognized** from the AD roster: JAG, Penguin Soldier, Vision, Nimsen, Ikagai, Byteron, Shanah, Pipkin, JuliaChang, StoneWill, Rocky, Jiaozi — all removed for failure to migrate to v3 contracts (context: PR #6 updated v3 addresses for the remaining active ADs).

---

## PR #3 — New AD added: Max Staking Yield
**Merged:** 2025-06-03 | **Type:** Weekly edit (Atlas Axis)

### Material Changes
- **New AD recognized**: Max Staking Yield (recognition address `0x9746bDaB7ab2609247332324400cc1fbE887095C`, forum: max-staking-yield-ad-recognition-submission/26462).

---
