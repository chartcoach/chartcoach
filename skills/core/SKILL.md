---
name: core
description: Open one Guideline Catalog, find guideline entries, read selected evidence, and format citations.
---

# chartcoach Core

Open one Guideline Catalog for the task. Use compact candidates to choose
records, then read and cite the selected guideline entry IDs from that same
`Catalog`. Use `visfeedback` for a rendered chart, `visrec` for a design brief,
`discuss` for a comparison, and `contribute` for a catalog issue.

## Use Python

```python
import chartcoach.agent as cc

location = None  # Pass an authored folder, bundle, deployed root, or descriptor.
catalog = cc.open_catalog(location)
description = catalog.describe()

candidates = catalog.query(
    contains="labels",
    limit=5,
).to_dicts()
selected_ids = [row["id"] for row in candidates[:3]]
records = catalog.read(ids=selected_ids, source_detail="minimal")
citations = catalog.cite(ids=selected_ids)
candidates
```

`catalog.query()` returns a Polars DataFrame with `id`, `title`, `description`,
and `labels`. Select candidates before calling `catalog.read()`. Pass
`source_detail="full"` when the task needs every parsed source field and the
entry's BibTeX references.

## Choose a query

| Need                                                           | Primitive                                                  |
| -------------------------------------------------------------- | ---------------------------------------------------------- |
| A term or short phrase in an entry's ID, title, or description | `catalog.query(contains=...)` or `catalog list --contains` |
| Exact catalog labels                                           | `labels` / `--label`, with every supplied filter required  |
| Several concepts or words in guideline text                    | Explicit full-text search (`fts`) on an available profile  |
| Section text, source fields, or compound conditions            | Native DuckDB or `catalog sql`                             |

`contains` matches one contiguous substring. It ignores case and treats
whitespace, hyphens, and underscores as equivalent separators. Search separate
concepts separately, such as `labels` and `overlap`. A list of keywords such as
`line chart labels overlap` must occur together to match.

If a query returns zero candidates, shorten the phrase, try another term, or
relax exact filters. Use full-text search when the catalog has a profile. If it
has none, query section text with SQL. An empty result describes that query,
not the catalog's coverage of the task. When matches are too broad, add a
verified label or inspect relevant sections before choosing records.

Discover what the next operation needs: `describe` for identity and profiles,
`labels` and `roles` for exact vocabulary, and `schema` for SQL columns. Reuse
that information throughout the task.

## Use the terminal

Commands open the official selected catalog by default. Set a source when the
task uses another catalog:

```sh
export CHARTCOACH_SOURCE=./authored-catalog
chartcoach catalog describe
```

`--source` overrides `CHARTCOACH_SOURCE`. When both are absent, commands open
the official selected catalog. Use an exact `release.json` location when the
task must retain one release digest.

Inspect the vocabulary or schema needed by a filter or query:

```sh
chartcoach catalog roles
chartcoach catalog labels --contains label
chartcoach catalog schema sections guideline_sources
```

Find compact candidates with filters or SQL:

```sh
chartcoach catalog list --contains "labels" --limit 5
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
chartcoach catalog read <first-id> <second-id> \
  --source-detail minimal \
  --format markdown
chartcoach catalog cite <first-id> <second-id> --format markdown
```

Discard a record when its chart family, reader task, audience, data type, or
interaction state differs from the current case.

`read` includes the selected entries' sections. Check their applicable
situations and exceptions before narrowing by role. `cite` identifies sources
attached to a guideline. Inspect a publication before attributing a specific
claim to it. Keep the observed facts, the guideline's advice, and your own
inference distinguishable in the answer.

## Search an indexed release

`catalog.describe()` lists flat profile IDs attached to a release. Choose an
available profile. Explicit full-text search loads its index while keeping
embedding providers idle:

```python
profile = "<profile-id>"
table = catalog.index(profile)
hits = table.search(
    "direct labels", query_type="fts", fts_columns="text"
).select(["id", "parent_id", "role", "_score"]).limit(10).to_list()
selected_ids = list(dict.fromkeys(hit["parent_id"] for hit in hits))
records = catalog.read(ids=selected_ids)
citations = catalog.cite(ids=selected_ids)
```

Use `query_type="vector"` or `query_type="hybrid"` after installing the profile's
`python_requirements` and registering its LanceDB embedding alias. LanceDB
reconstructs the persisted function and embeds the query text. A host sets
referenced variables before the first semantic query:

```python
from lancedb.embeddings import get_registry

get_registry().set_var("provider-key", "<secret>")
metadata = catalog.describe(profile=profile)["profile"]
hits = table.search("direct labels", query_type="vector").distance_type(
    metadata["distance_metric"]
).select(["id", "parent_id", "role", "_distance"]).limit(10).to_list()
```

For a numeric-vector query, use a vector produced by the profile's embedding
model with the reported dimensions and distance metric.

Project the fields you need before converting hits to Python objects. Include
`_score` for full-text results and `_distance` for vector results. For hybrid
queries, select stored fields such as `id`, `parent_id`, and `role`.
LanceDB adds `_relevance_score` after reranking. Higher relevance and lower
distance rank first. These values rank retrieval results within a query, mode,
and profile. They do not establish applicability or confidence in a
recommendation.

Index rows contain `row_id`, `id`, `parent_id`, `role`, `labels`,
`content_hash`, `text`, and `vector`. `id` identifies a search document.
`parent_id` is the guideline entry ID accepted by `catalog.read` and
`catalog.cite`. Roles include `overview`, `document`, and
`section.<manifest-role>`. Multiple documents can belong to the same entry.
Use LanceDB's filtering, batch search, reranking, and result conversion on the
returned table. The default table is a protected shared extraction. Pass a
new `directory=Path(...)` to `catalog.index` for a writable copy.

## Compose catalog artifacts and SQL

`catalog.describe()["tables"]` lists the six DuckDB tables with schemas and
row counts. `guideline_id` joins section, label, and source rows to
`guidelines.id`. `guideline_references.reference_id` joins to `references.id`.
Use the native connection for joins, aggregation, parameters, and exports:

```python
with catalog.duckdb() as connection:
    rows = connection.execute(
        "select guideline_id, source_title from guideline_sources where year = ?",
        ["2024"],
    ).fetchall()
```

For a release, `catalog.release.artifacts` lists every available artifact with
its byte count and SHA-256 hash. `catalog.artifact(path)` returns a verified
local file and downloads missing remote bytes into the platform cache:

```python
entries = catalog.artifact("entries.parquet")
with catalog.duckdb() as connection:
    rows = connection.read_parquet(str(entries)).select("id, title").limit(5).fetchall()
```

Profiles may include `profiles/<profile-id>/documents.parquet` and
`profiles/<profile-id>/projection.parquet`. Inspect the release inventory
before requesting them. Documents include vectors and text. Projection rows
include `row_id`, `id`, `parent_id`, `role`, `projection_x`, `projection_y`,
and `neighbors` with parallel `ids` and `distances` arrays.

Open S3 descriptors with `cc.open_catalog("s3://bucket/catalog.json",
storage_options={"region": "eu-central-1"})` after installing
`chartcoach[cloud]`. Credentials use the object-store client's normal
configuration. Exact digest-addressed releases reuse verified descriptors
and artifacts across processes. Selected catalogs refresh `catalog.json`.
`local = catalog.cache()` downloads every artifact of the selected release
and returns a directory that `cc.open_catalog(local)` opens offline.

The terminal search returns JSON by default:

```sh
chartcoach catalog search \
  --profile <profile-id> \
  --mode fts \
  --where "role = 'section.<manifest-role>'" \
  --limit 10 \
  "<query>"
```

`limit` counts search document hits before guideline deduplication. Inspect
`documents_considered`, `match_count`, and `documents_truncated` separately.
When many hits share one parent, an additional `role = 'overview'` search can
broaden candidates. Section searches can recover evidence absent from an
overview. Deduplicate native hits by `parent_id`, preserving rank, then read
the selected entries for complete evidence. CLI and MCP previews expose at
most 360 characters and report `excerpt_truncated`.

For curation, `catalog.documents()` supplies the canonical `row_id`, `id`,
`parent_id`, `role`, `labels`, `content_hash`, and `text` rows to native
LanceDB ingestion. `IndexProfile(table, configure=...)` in `chartcoach.curation`
packages completed vectors. Its callback configures native indexes on the
release table. Use `ProfileReuse` for an existing release archive whose
indexed documents match the target catalog.

## Use TypeScript

Node applications open local bundles or remote descriptors through the Node
entry point, which persists verified artifacts in the platform cache:

```ts
import { openCatalog, artifactPath } from "@chartcoach/catalog/node";

const catalog = await openCatalog("./dist/release");
const entries = await artifactPath(catalog, "entries.parquet");
const candidates = catalog.query({ contains: "labels", limit: 5 });
const ids = candidates.map((candidate) => candidate.id);
const records = catalog.read({ ids });
const citations = catalog.cite({ ids });
```

Pass `entries` as a bound parameter to DuckDB's `read_parquet` table function.
The six stored columns are `id`, `title`, `description`, `labels`, `sections`,
and `references`. Unnest `sections` to inspect its `role`, `title`, and
`content` fields. `references` contains BibTeX strings. `catalog.read` and
`catalog.cite` provide parsed sources and formatted citations.

Browser applications import `openCatalog` from `@chartcoach/catalog` and call
`await catalog.artifact("entries.parquet")` for verified bytes. Use those bytes
with the existing browser data engine. A custom `fetch` connects a caller-owned
S3 client to either loader. Inspect the JavaScript reference for the streaming
AWS SDK adapter and cancellation contract.

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
