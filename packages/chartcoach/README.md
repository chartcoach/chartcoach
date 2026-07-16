# chartcoach

`chartcoach` loads Guideline Catalog records, exposes them as Polars and DuckDB
tables, and opens native LanceDB indexes.

```bash
uv add chartcoach
```

```python
from chartcoach import open_catalog

catalog = open_catalog("dist/catalog")
print(catalog.guidelines().select("id", "title").head(5))
```

`open_catalog` accepts an authored folder or a compiled bundle directory. Both
contain `MANIFEST.md`. A bundle also contains `entries.parquet`.

## Public API

The top-level package exports:

- `Catalog`
- `CatalogManifest`
- `CatalogRelease`
- `open_catalog`
- `open_index`
- `resolve_release`
- `paths`

Compiled rows have six fields: `id`, `title`, `description`, `labels`,
`sections`, and `references`. `Catalog.entry(id)` and `Catalog.guidelines()`
derive Markdown bodies from the ordered sections.

## Published releases

Install the curation extra to read, cache, build, validate, and publish
digest-addressed releases through Obspec and Obstore.

```bash
uv add 'chartcoach[curation]'
```

```python
from chartcoach import open_catalog, paths, resolve_release

release = resolve_release()
catalog = open_catalog(release.digest)
release_paths = paths.release(release.digest)

print(catalog.content_digest())
print(release_paths.entries())
print(release_paths.profile("sentence-transformers/all-MiniLM-L6-v2").index())
```

`catalog.json` contains the selected release record. Passing a release digest
to `resolve_release`, `open_catalog`, or `open_index` selects an immutable
release.

## Native LanceDB queries

Install the index extra to open the fixed `documents` table.

```bash
uv add 'chartcoach[index]'
```

```python
from chartcoach import open_index

table = open_index("dist/index")

fts_rows = (
    table.search("direct labels", query_type="fts", fts_columns="text")
    .limit(8)
    .to_list()
)

query_vector = embed("direct labels")
vector_rows = (
    table.search(
        query_vector,
        query_type="vector",
        vector_column_name="vector",
    )
    .distance_type("cosine")
    .limit(8)
    .to_list()
)
```

Use LanceDB query builders directly for filters, hybrid search, rerankers, and
embedding functions. Vector and hybrid queries receive vectors from the
calling application.

## Build embedding profiles

`build_catalog_release` accepts any number of native LanceDB embedding
functions. Each profile writes one analysis Parquet file and one LanceDB
archive.

```python
from pathlib import Path

from lancedb.embeddings import get_registry

from chartcoach import open_catalog
from chartcoach.catalog.curation.release_builder import (
    EmbeddingProfile,
    build_catalog_release,
)

embedding = get_registry().get("sentence-transformers").create(
    name="all-MiniLM-L6-v2",
    device="cpu",
    normalize=True,
    trust_remote_code=False,
)

release = build_catalog_release(
    open_catalog("dist/catalog"),
    root=Path("dist/release"),
    profiles={
        "sentence-transformers/all-MiniLM-L6-v2": EmbeddingProfile(
            embedding=embedding,
        ),
    },
)

print(release.digest)
```

The profile Parquet file contains vectors, UMAP coordinates, and nearest
neighbors for analysis and Embedding Atlas. The archive contains the native
LanceDB database.

Publish the immutable release, then select its digest:

```bash
chartcoach catalog release validate dist/release
chartcoach catalog release publish dist/release --store s3://chartcoach
chartcoach catalog release select "$RELEASE_DIGEST" --store s3://chartcoach
```

Local file URLs and S3-compatible URLs use the same object-key contract.
