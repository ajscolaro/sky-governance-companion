---
name: atlas-navigate
description: >
  Search and read Sky Atlas documents locally. Find documents by name, path prefix,
  type, or UUID, then read individual document.md files without loading the entire corpus.
argument-hint: "<search term, document number, or UUID>"
allowed-tools: Bash, Read, Grep, Glob
---

# Atlas Navigate

You are helping explore the Sky Atlas governance document using the local clone and parsed index.

## Setup check

If `data/index.json` doesn't exist, run setup first:
```bash
bash scripts/core/setup.sh
```

If the Atlas may be stale (hasn't been refreshed recently), re-sync:
```bash
bash scripts/core/atlas-sync.sh
```

## Searching for documents

Use `scripts/atlas/search-index.sh` to query the index:

```bash
# By name keyword (case-insensitive)
bash scripts/atlas/search-index.sh "exposure"

# By path prefix (everything under an entity)
bash scripts/atlas/search-index.sh --prefix "A.6.1.1.2" --limit 30

# By document type
bash scripts/atlas/search-index.sh --type "Active Data" --limit 20

# By UUID (partial match OK)
bash scripts/atlas/search-index.sh --uuid "fad68392"

# Combined filters
bash scripts/atlas/search-index.sh --prefix "A.6.1.1.1" --name "rate" --limit 20
```

Output is tab-separated: `number  name  [type]  lines X-Y`

### Search fallback strategy

**Never retry the exact same query twice.** Atlas document names are often shorter than expected (e.g. the agent is called "Pattern", not "Pattern Agent"). If a search returns no results:

1. **Break multi-word queries into single keywords** — try each word separately to find candidate documents
2. **Try the most distinctive word only** — e.g. "Pattern Agent" → try "Pattern", then "Agent" if needed
3. **Use `--prefix` if you suspect a path** — e.g. `--prefix A.6.1.1` to list all agents
4. **Fall back to jq** for flexible matching across fields

If none of the above return results, report that clearly rather than looping.

## Reading document content

Use `scripts/atlas/read-section.sh` to read a document or subtree by number/UUID:

```bash
# Single document by number
bash scripts/atlas/read-section.sh A.6.1.1.2

# Single document by UUID
bash scripts/atlas/read-section.sh fad68392-c852-4102-81fd-2a4037be38f9

# Subtree (document + all children)
bash scripts/atlas/read-section.sh A.6.1.1.2 --subtree

# Subtree with depth limit (recommended for large subtrees)
bash scripts/atlas/read-section.sh A.6.1.1.2 --subtree --depth 2
```

**Important:** Large subtrees (Spark, Grove) have thousands of documents. Always use `--depth` to limit output, then drill deeper into specific areas.

### Continuous-prose reading

`read-section.sh --subtree` concatenates raw `document.md` files (frontmatter and all), which is fine for grep but rough for human reading. For an end-to-end continuous-prose view of an Atlas area — proper `# A.X.Y - Name` heading lines, NRs inserted at their target docs, no per-doc frontmatter — use:

```bash
python3 scripts/atlas/compose-subtree.py A.6.1.1.2
# -> tmp/compose/A.6.1.1.2.md
```

Use this when you want to read an unfamiliar area top-to-bottom, or share a slice with someone used to the legacy single-file Atlas format. For PR review, use `/atlas-analyze` instead — per-doc diffs are the natural unit after atomization.

## Complex queries via jq

For queries the scripts don't cover, query `data/index.json` directly:

```bash
# Count documents by type under a prefix
jq '[.[] | select(.number | startswith("A.6.1.1.2"))] | group_by(.type) | map({type: .[0].type, count: length})' data/index.json

# Find all Active Data Controller docs under Spark
jq '.[] | select(.number | startswith("A.6.1.1.1")) | select(.type == "Active Data Controller") | "\(.number) - \(.name)"' data/index.json

# Find a document's full ancestor path
jq '.[] | select(.number == "A.6.1.1.2.2.6.1.3.1.13") | .ancestors' data/index.json
```

Index entry fields: `uuid`, `number`, `name`, `type`, `depth`, `heading_level`, `path`, `body_length`, `body_hash`, `lead_sentence`, `is_scaffold`, `is_active_data`, `parent_uuid`, `ancestors`.

## Reading raw document files

The Atlas is atomized — each document lives in its own `document.md` file with YAML frontmatter. The index's `path` field points directly at the file:

```bash
# Resolve a number/UUID to its file path, then Read it
jq -r '.[] | select(.number == "A.6.1.1.2") | .path' data/index.json
# -> .atlas-repo/content/A/6/1/1/2/document.md
```

`read-section.sh` does this lookup for you. Use raw Read only when you need to see the YAML frontmatter or process the file's exact bytes.

## Atlas format reference

Each `document.md` has YAML frontmatter (`id`, `docNo`, `name`, `type`, `depth`, `childType`, plus `targets` for NRs) followed by the document body. Key points:

- Document types: Scope > Article > Section > Core, plus Annotation, Action Tenet, Active Data Controller, Active Data, Scenario, Needed Research
- UUIDs (`id` in frontmatter) are permanent; document numbers (`docNo`) shift when content is inserted/removed
- The document number encodes true depth; when composed back to single-file form, heading levels cap at h6
- Internal cross-references link by UUID: `[A.1.2.3 - Name](uuid-here)`
- Needed Research docs live under `content/NR/` and attach to their target documents via the `targets` frontmatter list

## Complementary skills

This skill reads the current Atlas. For history, governance, and market context, see "Cross-domain questions" in CLAUDE.md:
- `/atlas-analyze` — what changed in a specific PR affecting this document
- `/governance-data` — polls and spells that authorized changes to this area
- `/messari-market-data` — market context around governance events
- `/forum-search` — community discussion about this area of the Atlas
