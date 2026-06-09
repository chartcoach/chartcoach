---
name: core
description: Load this before using ChartCoach. Explains default catalog access, progressive catalog navigation, output formats, CLI-served skills, optional LanceDB discovery, and the CLI primitives agents should combine.
---

# ChartCoach Core

ChartCoach exposes a versioned Guideline Catalog and CLI primitives for inspecting and retrieving visualization guidance. Start with the base CLI and progressive disclosure. Use LanceDB only when overview, labels, roles, list, query, read, schema, values, and SQL commands are not enough.

## Command Surface

All examples use `chartcoach` as the CLI command. If the command is not available, use the top-level `$chartcoach` access guidance first.

Base catalog commands:

```sh
chartcoach catalog overview
chartcoach catalog manifest
chartcoach catalog labels
chartcoach catalog roles
chartcoach catalog list
chartcoach catalog query
chartcoach catalog read
chartcoach catalog schema
chartcoach catalog values
chartcoach catalog sql
```

Optional indexed discovery requires `chartcoach[index]`:

```sh
chartcoach catalog find
chartcoach catalog index create
chartcoach catalog index info
```

Use `chartcoach mcp serve` only when a human wants to start a server interface.

Use `chartcoach skills list`, `chartcoach skills get <name>`, and `chartcoach skills path [name]` for CLI-served skills bundled with the installed package. The top-level `chartcoach` skill is installed separately by the agent skill system and is not served by `chartcoach skills get`.

## Catalog Artifacts

Omit `--source` to use the package-pinned default catalog release from `https://artifacts.chartcoach.dev`. The CLI resolves the release metadata, downloads `MANIFEST.md` and `entries.parquet` on first use, and caches them in the user's platform cache directory. The local cache mirrors the release layout: `catalog/releases/<version>/<digest>/`.

Set `CHARTCOACH_SOURCE` or pass `--source` only when the user provides a custom catalog locator. Accepted sources include a catalog bundle directory, an `entries.parquet` file, an authored folder, or a release metadata URL.

Release metadata is the artifact inventory for one catalog release. It has `version`, `digest`, and `artifacts`. The default release includes `MANIFEST.md`, `entries.parquet`, and derived LanceDB artifacts. Base commands download only the manifest and entries artifacts. Indexed commands download LanceDB artifacts only when the default index is needed.

LanceDB artifacts identify their table, catalog version, catalog digest, embedding registry, embedding model, and embedding options so query-time code can use LanceDB's native embedding function metadata.

The manifest defines section roles, label families, table contracts, and supported vocabulary for the current catalog. Treat labels and section roles as catalog-defined data, not global constants.

## Progressive Navigation

Start by learning the live catalog shape:

```sh
chartcoach catalog overview --format json
chartcoach catalog manifest --format markdown
chartcoach catalog labels --format jsonl
chartcoach catalog roles --format jsonl
```

Use `catalog query` for deterministic candidate sets without an index:

```sh
chartcoach catalog list --contains "axis" --format jsonl
chartcoach catalog query --contains "axis" --format jsonl
chartcoach catalog query --label <exact-label> --format jsonl
chartcoach catalog query --any-label <exact-label> --any-label <another-label> --format jsonl
chartcoach catalog query --label-prefix <family-or-prefix> --section-contains "<text>" --format jsonl
```

Guideline ids are exact. Copy ids from `catalog list`, `catalog query`, or `catalog find --format compact`. Do not derive ids from titles or snippets.

If a JSONL query returns no rows, do not treat that as proof the catalog has no relevant guidance. Inspect labels with `catalog labels --contains TEXT`, relax one predicate, try `--section-contains` or `--body-contains` with a broader term, or switch to `catalog sql` for explicit boolean grouping.

## Reading Guideline Sections

Use `catalog read` for exact ids and selected section roles:

```sh
chartcoach catalog read <guideline-id> --format markdown
chartcoach catalog read <guideline-id> --section <role-from-manifest> --source-detail minimal --format jsonl
```

There is no special evidence command. To assemble citation-ready evidence, combine these primitives:

1. `catalog roles` or `catalog manifest` to learn valid section roles.
2. `catalog query`, `catalog list`, `catalog sql`, or `catalog find` to identify exact ids.
3. `catalog read <id> --section <role-from-manifest> --source-detail minimal` to retrieve the catalog sections and source metadata you need.

Do not assume any section role exists. Read the manifest and use the current catalog's role names.

## Tables And SQL

Use table primitives when you need exact schema, valid values, counts, or joins:

```sh
chartcoach catalog schema --tables --row-counts
chartcoach catalog schema
chartcoach catalog values roles
chartcoach catalog values labels --contains axis
chartcoach catalog sql "select id, title from guidelines limit 5" --format jsonl
```

Use SQL when exact filtering or joins are clearer than keyword matching. Keep queries read-only.

## Indexed Discovery

`chartcoach catalog find` ranks entries with an existing LanceDB index. With the default catalog source and `chartcoach[index]` installed, it can resolve and cache the package-pinned default index when `--index` is omitted. With a custom source, pass `--index` or set `CHARTCOACH_INDEX`.

`chartcoach catalog index create` creates a LanceDB table from catalog document rows. `--index` accepts a local LanceDB database path or any URI that LanceDB can open, such as an object-store URI configured in the runtime environment.

Use LanceDB after progressive disclosure is insufficient.

For the package-pinned default catalog, read-only search can resolve the default index artifact:

```sh
chartcoach catalog find --mode fts --format compact "direct labels line chart exact lookup"
```

A full-text index works without embeddings:

```sh
chartcoach catalog index create --index ./chartcoach-index
chartcoach catalog find --index ./chartcoach-index --mode fts --format compact "direct labels line chart exact lookup"
```

Vector and hybrid search require a LanceDB embedding function. Use LanceDB-native embedding aliases and options:

```sh
chartcoach catalog index create --index ./chartcoach-index --embedding sentence-transformers --embedding-option name=all-MiniLM-L6-v2
chartcoach catalog index create --index ./chartcoach-index --embedding openai --embedding-var OPENAI_API_KEY=$OPENAI_API_KEY --embedding-option model=text-embedding-3-small
chartcoach catalog find --index ./chartcoach-index --mode hybrid --format compact "direct labels line chart exact lookup"
```

Embedding options are passed to LanceDB's embedding function `create()` call. Embedding variables are registered with LanceDB before the embedding function is created. Do not invent a ChartCoach embedding model layer.

Published catalog releases can include two LanceDB index artifacts:

| Format | Use |
| --- | --- |
| `tar+gzip` | Download and cache a local copy of the index. |
| `lancedb` | Connect directly with `lancedb.connect("<artifact-uri>")` when the object-store environment is configured. |

Search output reports indexed document roles. Values such as `overview`, `document`, or `section.<role>` explain where the match came from in the index. `catalog read --section` accepts manifest section roles, not the indexed `section.` prefix.

## Output Formats

- Use `jsonl` for agent parsing and shell pipelines.
- Use `json` when one command returns structured metadata.
- Use `table` for quick human scanning with aligned plain-text columns.
- Use `markdown` for full guideline reading.
- Use `compact` for indexed citation triage from `catalog find`.
- Use `csv` only when the shape is flat enough for tabular tools.

## Agent Rules

- Use manifest, labels, roles, and values commands to learn valid vocabulary.
- Prefer base CLI progressive disclosure before LanceDB search.
- Copy exact ids from CLI output before reading records.
- Retrieve cited sections with `catalog read <id> --section <role-from-manifest>`.
- Use `catalog values --contains TEXT` when the visible value list is too broad.
- Keep searches task-specific: chart family, data type, visual encoding, reader task, failure mode, and interaction state.
- Reject adjacent hits when the top result is scoped to a different chart family, reader task, or data type. Search again with sharper observed terms.
- If search against a custom catalog fails with a missing `--index`, build a local full-text index and retry with `--mode fts`.
