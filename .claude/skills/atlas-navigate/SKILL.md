---
name: atlas-navigate
description: >
  Search and read Sky Atlas documents locally. Find documents by name, path prefix,
  type, or UUID, then read their content without loading the full 3MB file.
argument-hint: "<search term, document number, or UUID>"
allowed-tools: Bash, Read, Grep, Glob
---

# Atlas Navigate

You are helping explore the Sky Atlas governance document using the local clone and parsed index.

## Setup check

If `data/index.json` doesn't exist, run setup first:
```bash
bash scripts/setup.sh
```

If the Atlas may be stale (hasn't been refreshed recently), refresh:
```bash
bash scripts/refresh.sh
```

## Searching for documents

Use `scripts/search-index.sh` to query the index:

```bash
# By name keyword (case-insensitive)
bash scripts/search-index.sh "exposure"

# By path prefix (everything under an entity)
bash scripts/search-index.sh --prefix "A.6.1.1.2" --limit 30

# By document type
bash scripts/search-index.sh --type "Active Data" --limit 20

# By UUID (partial match OK)
bash scripts/search-index.sh --uuid "fad68392"

# Combined filters
bash scripts/search-index.sh --prefix "A.6.1.1.1" --name "rate" --limit 20
```

Output is tab-separated: `number  name  [type]  lines X-Y`

## Reading document content

Use `scripts/read-section.sh` to extract content by line range:

```bash
# Single document by number
bash scripts/read-section.sh A.6.1.1.2

# Single document by UUID
bash scripts/read-section.sh fad68392-c852-4102-81fd-2a4037be38f9

# Subtree (document + all children)
bash scripts/read-section.sh A.6.1.1.2 --subtree

# Subtree with depth limit (recommended for large subtrees)
bash scripts/read-section.sh A.6.1.1.2 --subtree --depth 2
```

**Important:** Large subtrees (Spark, Grove) have thousands of documents. Always use `--depth` to limit output, then drill deeper into specific areas.

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

Index entry fields: `uuid`, `number`, `name`, `type`, `depth`, `heading_level`, `line_start`, `line_end`, `ancestors`, `parent_uuid`.

## Reading the raw Atlas file

When you need more context than the index provides, read the Atlas file directly:

```bash
# The file path
.atlas-repo/Sky Atlas/Sky Atlas.md

# Use Read tool with line offsets from the index for targeted access
# (avoids loading the full 3MB file)
```

## Atlas format reference

The full format spec is at `.atlas-repo/ATLAS_MARKDOWN_SYNTAX.md`. Key points:

- Every document starts with: `{#...} {Number} - {Name} [{Type}]  <!-- UUID: {uuid} -->`
- Document types: Scope > Article > Section > Core, plus Annotation, Action Tenet, Active Data Controller, Active Data, Scenario, Needed Research
- UUIDs are permanent; document numbers can shift when content is inserted/removed
- Heading levels cap at h6; the document number encodes the true depth
- Internal cross-references link by UUID: `[A.1.2.3 - Name](uuid-here)`
