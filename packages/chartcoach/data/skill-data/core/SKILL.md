---
name: core
description: Choose a chartcoach catalog, find guideline records, read them in full, and format their citations.
---

# chartcoach Core

Use the Guideline Catalog to find possible matches, read each selected record,
and keep its source citation with the final answer.

## Choose the catalog

Set one source for the whole task:

```sh
export CHARTCOACH_SOURCE=./authored-catalog
# or: export CHARTCOACH_SOURCE=./dist/catalog
# or: export CHARTCOACH_SOURCE=https://files.peter.gy/catalog/chartcoach/catalog/releases/<digest>/release.json

chartcoach catalog overview
```

An authored folder contains `MANIFEST.md` and `entries/<id>/guideline.md`. A
compiled bundle contains `MANIFEST.md` and `entries.parquet`. A remote source
names `catalog.json` or `release.json`.

`--source` overrides `CHARTCOACH_SOURCE` for one command. When both are absent,
commands open the official selected catalog. Prefer an exact `release.json`
URL when the answer must keep one catalog digest.

## Inspect labels and sections

Each catalog defines its own section roles and label families in
`MANIFEST.md`. Inspect the current values before using them as exact filters:

```sh
chartcoach catalog overview --format json
chartcoach catalog roles --format json
chartcoach catalog labels --format json
```

## Find records

`catalog list` filters IDs, titles, descriptions, and labels:

```sh
chartcoach catalog list --contains "axis labels" --format json
chartcoach catalog list --label <exact-label> --format json
chartcoach catalog list --label-prefix <prefix> --format json
```

Repeated `--label` values all have to match. If a filter returns no rows,
broaden `--contains`, remove one label, or shorten the prefix.

`catalog sql` handles relationships between guideline, section, label, and
source tables:

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

SQL accepts one read-only `SELECT`.

## Read and cite each selection

`list`, `sql`, and `find` return possible matches. Read the full record before
using it, then format its link and references:

```sh
chartcoach catalog read <guideline-id> \
  --source-detail minimal \
  --format markdown

chartcoach catalog cite <guideline-id> --format markdown
```

Discard a record when its chart family, reader task, audience, data type, or
interaction state differs from the current case.

## Search an indexed release

`catalog find` needs `chartcoach[index]` and a release that includes the named
profile. A profile is a search index stored with that release.

```sh
chartcoach catalog find \
  --profile <profile> \
  --mode fts \
  --where "role = 'section.<manifest-role>'" \
  --limit 10 \
  --format compact \
  "<query>"
```

Use `--mode vector` or `--mode hybrid` with one `--vector VALUE` per embedding
dimension. The calling application creates that query vector. Copy guideline
IDs exactly from the result and check them with `catalog read`.

## Install optional features

| Task                                        | Package selector       |
| ------------------------------------------- | ---------------------- |
| Local and HTTP catalogs, Polars, and DuckDB | `chartcoach`           |
| S3, GCS, and Azure catalogs                 | `chartcoach[cloud]`    |
| LanceDB search indexes                      | `chartcoach[index]`    |
| MCP server                                  | `chartcoach[mcp]`      |
| Build, publish, and select releases         | `chartcoach[curation]` |

For a one-off inspection of the official catalog, override any exported
source:

```sh
CHARTCOACH_SOURCE= uvx chartcoach@latest catalog overview
```

## Output formats

Tabular commands support `table` and `json`. `read`, `cite`, and `manifest`
support `markdown` and `json`. `find` also supports `compact`.

Use the same guideline ID in search results, full reads, citations, notes, and
the final answer.
