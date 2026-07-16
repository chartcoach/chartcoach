---
name: core
description: Use this for chartcoach catalog sources, retrieval, citations, package extras, release digests, cache pull, and LanceDB search.
---

# chartcoach Core

Use the Guideline Catalog as a source-backed record system. Discover candidate
ids, read the exact records, then format citations.

## Start With The Catalog

Inspect the current vocabulary before using exact roles or labels:

```sh
chartcoach catalog overview --format json
chartcoach catalog roles --format json
chartcoach catalog labels --format json
```

The manifest defines section roles and label families for the active catalog.
Treat its values as runtime data.

## Retrieve And Verify

Use `list` for deterministic filters:

```sh
chartcoach catalog list --contains "axis labels" --format json
chartcoach catalog list --label <exact-label> --format json
chartcoach catalog list --label-prefix <prefix> --format json
```

Use repeated `--label` filters for all-of matching. Broaden `--contains`, remove
one label, or shorten a prefix when a filter returns no rows.

Read every selected record before citing it:

```sh
chartcoach catalog read <guideline-id> \
  --source-detail minimal \
  --format markdown

chartcoach catalog cite <guideline-id> --format markdown
```

`list`, `sql`, and `find` return candidates. `read` returns the exact text that
supports or rejects a candidate. `cite` formats its public link and source
references.

## Query Relationships

Inspect the schema, then run one read-only `SELECT`:

```sh
chartcoach catalog schema --tables --row-counts
chartcoach catalog schema sections guideline_sources
chartcoach catalog sql "
  select distinct g.id, g.title
  from guidelines g
  join sections s on s.guideline_id = g.id
  where s.content ilike '%uncertainty%'
  limit 20
" --format json
```

Queryable tables are `guidelines`, `sections`, `guideline_labels`,
`references`, `guideline_references`, and `guideline_sources`.

## Use Indexed Discovery

Use LanceDB when titles, descriptions, labels, and SQL text matching leave too
many candidates:

```sh
chartcoach catalog find \
  --profile <profile> \
  --mode fts \
  --where "role = 'section.<manifest-role>'" \
  --limit 10 \
  --format compact \
  "<query>"
```

Use `--mode vector` or `--mode hybrid` with one `--vector VALUE` per dimension.
The calling application owns query-vector production. Copy ids exactly from
the result and verify them with `catalog read`.

## Select A Source

Commands that read a catalog accept `--source`:

```sh
chartcoach catalog overview --source ./authored-catalog
chartcoach catalog overview --source ./dist/catalog
chartcoach catalog overview --source <64-character-release-digest>
```

An authored folder contains `MANIFEST.md` and `entries/<id>/guideline.md`. A
bundle contains `MANIFEST.md` and `entries.parquet`. A digest names an immutable
published release. The default source is `CHARTCOACH_SOURCE`, then the selected
release in `catalog.json`.

Use `chartcoach catalog cache pull --profile <profile>` to prefetch the selected
catalog and one index archive.

## Choose Dependencies

| Boundary                                                      | Package selector       |
| ------------------------------------------------------------- | ---------------------- |
| Local catalog, Polars, and DuckDB                             | `chartcoach`           |
| Local LanceDB table                                           | `chartcoach[index]`    |
| MCP server                                                    | `chartcoach[mcp]`      |
| Published storage, cache, profile build, and release curation | `chartcoach[curation]` |

For one-off published catalog work:

```sh
uvx --from 'chartcoach[curation]@latest' chartcoach catalog overview
```

## Output Contracts

Tabular commands support `table` and `json`. `read`, `cite`, and `manifest`
support `markdown` and `json`. `find` also supports `compact`.

Keep ids as the join key across discovery, exact reads, citations, notes, and
final answers.
