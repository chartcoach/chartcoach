---
name: core
description: Open one Guideline Catalog, find guideline entries, read selected evidence, and format citations.
---

# chartcoach Core

Open one Guideline Catalog for the task. Use compact candidates to choose
records, then read and cite the selected guideline entry IDs from that same
`Catalog`.

## Use Python

```python
import chartcoach.agent as cc

location = None  # Pass an authored folder, bundle, deployed root, or descriptor.
catalog = cc.open_catalog(location)
description = catalog.describe()

candidates = catalog.query(
    contains="direct labels",
    limit=5,
).to_dicts()
if not candidates:
    raise LookupError("No guideline entries matched. Inspect catalog.describe().")

selected_ids = [row["id"] for row in candidates[:3]]
records = catalog.read(ids=selected_ids, source_detail="minimal")
citations = catalog.cite(ids=selected_ids)
result = {
    "description": description,
    "candidates": candidates,
    "records": records,
    "citations": citations,
}
result
```

`catalog.query()` returns a Polars DataFrame with `id`, `title`, `description`,
and `labels`. Select candidates before calling `catalog.read()`. Pass
`source_detail="full"` when the task needs every parsed source field and the
entry's BibTeX references.

## Use the terminal

Set one catalog source for the task:

```sh
export CHARTCOACH_SOURCE=./authored-catalog
# or: export CHARTCOACH_SOURCE=./dist/catalog
# or: export CHARTCOACH_SOURCE=/srv/catalogs/chartcoach
# or: export CHARTCOACH_SOURCE=https://files.peter.gy/catalog/chartcoach/catalog/releases/<digest>/release.json

chartcoach catalog describe
```

`--source` overrides `CHARTCOACH_SOURCE`. When both are absent, commands open
the official selected catalog. Use an exact `release.json` location when the
task must retain one release digest.

Inspect vocabulary and catalog tables before applying exact filters:

```sh
chartcoach catalog describe
chartcoach catalog roles
chartcoach catalog labels
chartcoach catalog schema --tables --row-counts
chartcoach catalog schema sections guideline_sources
```

Find compact candidates with filters or SQL:

```sh
chartcoach catalog list --contains "axis labels" --limit 5
chartcoach catalog list --label <exact-label> --limit 5
chartcoach catalog sql "
  select distinct g.id, g.title
  from guidelines g
  join sections s on s.guideline_id = g.id
  where s.content ilike '%uncertainty%'
  limit 20
"
```

Read and cite selected guideline entry IDs:

```sh
chartcoach catalog read <guideline-entry-id> \
  --source-detail minimal \
  --format markdown
chartcoach catalog cite <guideline-entry-id> --format markdown
```

Discard a record when its chart family, reader task, audience, data type, or
interaction state differs from the current case.

## Search an indexed release

`catalog.describe()` lists flat profile IDs attached to a release. Explicit
full-text search loads the profile index while keeping embedding
providers idle:

```python
result = catalog.search(
    "direct labels",
    profile="<profile-id>",
    mode="fts",
    limit=10,
)
matches = result["matches"]
```

Use `mode="vector"` or `mode="hybrid"` after installing the profile's
`python_requirements` and registering its LanceDB embedding alias. LanceDB
reconstructs the persisted function and embeds the query text. A host sets
referenced variables before the first semantic query:

```python
from lancedb.embeddings import get_registry

get_registry().set_var("provider-key", "<secret>")
result = catalog.search(
    "direct labels",
    profile="<profile-id>",
    mode="vector",
)
matches = result["matches"]
```

Use the LanceDB table for numeric vectors, custom selection, reranking, and
index tuning:

```python
table = catalog.index("<profile-id>")
rows = table.search(
    [0.1, 0.2, 0.3],
    query_type="vector",
    vector_column_name="vector",
).limit(5).to_list()
```

The terminal search returns JSON by default:

```sh
chartcoach catalog search \
  --profile <profile-id> \
  --mode fts \
  --where "role = 'section.<manifest-role>'" \
  --limit 10 \
  "<query>"
```

`limit` counts search document hits before guideline deduplication. Read the
selected guideline entry to obtain complete evidence. Search previews expose
at most 360 characters and report `excerpt_truncated`.

## Install capability tiers

| Task                                          | Package selector         |
| --------------------------------------------- | ------------------------ |
| Local and HTTP catalogs, Polars, and DuckDB   | `chartcoach`             |
| S3, GCS, and Azure catalogs                   | `chartcoach[cloud]`      |
| LanceDB tables and indexed search             | `chartcoach[index]`      |
| Model Context Protocol server                 | `chartcoach[mcp]`        |
| Build, validate, publish, and select releases | `chartcoach[curation]`   |
| UMAP projection during profile production     | `chartcoach[projection]` |

Use the same guideline entry ID in candidates, complete reads, citations,
notes, and the final answer.
