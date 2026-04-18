# Other Changes — Change History

Changes that do not match any tracked entity prefix.

---

## PR #223 — remove non breaking space characters
**Merged:** 2026-04-13 | **Type:** Housekeeping

### Housekeeping
- Replaced non-breaking space characters (U+00A0) with regular spaces throughout the entire Atlas document
- Added `no-nbsps.js` markdownlint rule to lint for and prevent future NBSP characters

### Context
Pure linting/formatting pass with no content changes. Companion to PR #218 (remove whitespace in lists). No governance implications.

---

## PR #218 — remove whitespace in lists
**Merged:** 2026-04-09 | **Type:** Housekeeping

Removed blank lines between list items in multi-scope sections across A.0 (preamble), A.1 (governance), A.2 (support), A.3 (stability), and A.5 (accessibility). Pure whitespace normalization; no content changes. Companion to PR #223 (non-breaking space removal).

---

## PR #186 — 2026-02-16 AEW proposal
**Merged:** 2026-02-22 | **Type:** Weekly edit (Atlas Axis — Poll 1618) | **+2119/-158 lines**

### Housekeeping

- Deleted Needed Research entry `NR-6` — "Defining Threshold For 'Very Mild Slippery Slope' Breaches" — obsoleted by the new Graduated Response Framework in A.1.5.6.1 which replaces the prior "very mild" classification with Tier 1/Tier 2 bright lines

### Context

Cleanup of a research-track entry that no longer maps to the governance framework. See `A.1--governance` changelog for the substantive Graduated Response Framework introduction that supersedes the old "mild slippery slope" regime.

---

## PR #134 — Spark proposal - Onboard Spark Prime / Arkis
**Merged:** 2025-12-15 | **Type:** Spark proposal (new SLL instance)

Substantive changes tracked in `A.6.1.1.1--spark/changelog.md`. Unrouted: one document in `A.6.1.1.1.2.6.1.3.1.10.1.2.5.1` (Interim Deployment parameters) fell outside the indexed Atlas at time of processing.

---

## PR #133 — 2025-12-01 AEW Proposal
**Merged:** 2025-12-04 | **Type:** Weekly edit (Atlas Axis)

Unrouted changes: deleted "Needed Research" stubs (NR-11, NR-13, NR-14, NR-15, NR-16) for AD Whistleblower Bounty and Operational Security Protocols Research Track — both removed as part of the governance cleanup in this AEW. The substantive changes are tracked in the governance, support, stability, grove, keel, and pattern changelogs.

---

## PR #136 — add python script to generate UUIDs for new documents
**Merged:** 2025-12-03 | **Type:** Housekeeping

Added a Python utility (`helpers/add_uuids/add_uuids.py`, +90 lines) to auto-generate and insert UUID comments into Atlas markdown headers that lack them. Also added `.gitignore` entries for `*.bak` and `*.tmp` (backup files the script creates). No Atlas content changes.

---

## PR #129 — Always run the `validate` check to satisfy branch protection rules
**Merged:** 2025-11-27 | **Type:** Housekeeping

CI workflow fix: removed the `paths` filter from the `pull_request` trigger in `.github/workflows/validate-atlas.yml` so the `validate` check runs on all PRs (not just those touching the Atlas markdown file). No Atlas content changes.

---

## PR #24 — Update AEP-11.md
**Merged:** 2025-07-07 | **Type:** Housekeeping

`Atlas Edit Proposals/AEP-11.md` status updated: `RFC` → `Accepted`; Date Ratified: `N/A` → `2025-06-23`; Ratification Poll URL added (`https://vote.sky.money/polling/QmeHdTBV`). Metadata-only update to the AEP tracking file.

---

## PR #8 — AEP-11: Proposal - Update edit PR
**Merged:** 2025-06-05 | **Type:** Housekeeping

Updated `Atlas Edit Proposals/AEP-11.md` to correct the Pull Request reference: changed from `[79](https://github.com/makerdao/next-gen-atlas/pull/79)` to the correct URL `https://github.com/makerdao/next-gen-atlas/pull/7`. Meta-document fix only.

---
