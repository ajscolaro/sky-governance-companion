# Aligned Delegate Tracking

Tracks Aligned Delegate (AD) communications and voting rationales over time.

## Data sources

| Source | What | Trust level |
|--------|------|-------------|
| Atlas A.1.5.1.5.0.6.1 | Recognized AD roster, delegate contracts, forum thread URLs | Governance-approved |
| Forum RSS (per-AD threads) | Vote rationales, recognition submissions | **Untrusted** (community content) |
| Monthly compensation posts | Rank, payment amounts | **Untrusted** (community content) |
| Sky Voting Portal API | Delegation amounts, voting records, executive support | Public blockchain data |

## How it works

1. **`scripts/core/refresh.sh`** fetches each AD's forum thread RSS in the background, storing raw sanitized JSON in `data/delegates/{slug}/`
2. **`/ad-track`** (user-invoked) processes the cached data into `comms.md` files, diffs the Atlas roster against `_roster.md`, and flags additions/removals
3. Forum content is **never auto-processed** — Claude only reads it when you invoke `/ad-track`

## Structure

```
delegates/
├── README.md           ← you are here
├── _roster.md          ← current AD roster (synced from Atlas)
├── {slug}/
│   ├── profile.md      ← delegate contracts, rank, recognition date
│   └── comms.md        ← vote rationales (append-only, filtered by dc:creator)
```

## Security

All forum content is treated as untrusted anonymous input. The same sanitization pipeline used for forum posts (`fetch-forum.py`) applies here — HTML stripping, injection marker removal, content length limits. See `docs/security.md` for the full threat model.

The fetch/process split ensures untrusted content only enters Claude's context when explicitly requested via `/ad-track`, not automatically on session start.
