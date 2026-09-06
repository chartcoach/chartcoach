# chartcoach

`chartcoach` loads Guideline Catalog records into Polars and DuckDB tables. The
same source contract opens local catalogs, selected releases, exact releases,
and release-backed LanceDB profiles.

```bash
uv add chartcoach
```

```python
from chartcoach import open_catalog

catalog = open_catalog()
print(catalog.guidelines().select("id", "title").head(5))
```

## Catalog sources

`open_catalog(source)` accepts:

- an authored folder with `MANIFEST.md` and `entries/`
- a bundle with `MANIFEST.md` and `entries.parquet`
- a release directory with `release.json`
- a local `catalog.json` or `release.json`
- an HTTP or HTTPS descriptor URI
- a `file://` URI
- an S3, GCS, or Azure descriptor URI with `chartcoach[cloud]`

`source=None` opens
`https://artifacts.chartcoach.dev/catalog.json`. Remote sources name
`catalog.json` or `release.json` directly.

```python
catalog = open_catalog(
    "https://artifacts.chartcoach.dev/catalog/releases/<digest>/release.json"
)

if catalog.release is not None:
    print(catalog.release.digest)
```

Cloud provider settings travel through `storage_options`:

```python
catalog = open_catalog(
    "s3://research-artifacts/chartcoach/catalog.json",
    storage_options={"region": "eu-central-1"},
)
```

The top-level package exports `Catalog`, `CatalogError`, `CatalogManifest`,
`CatalogRelease`, `open_catalog`, `open_index`, and `__version__`.

## Native LanceDB queries

Install the index extra and select a profile from the same release source.

```bash
uv add 'chartcoach[index]'
```

```python
from chartcoach import open_index

table = open_index(
    "https://artifacts.chartcoach.dev/catalog.json",
    profile="sentence-transformers/all-MiniLM-L6-v2",
)

rows = (
    table.search("direct labels", query_type="fts", fts_columns="text")
    .limit(8)
    .to_list()
)
```

Use LanceDB directly to open a standalone database.

## Build and publish releases

The curation extra exposes one facade:

```python
from lancedb.embeddings import get_registry

from chartcoach import open_catalog
from chartcoach.catalog.curation import EmbeddingProfile, build_release

embedding = get_registry().get("sentence-transformers").create(
    name="all-MiniLM-L6-v2",
    device="cpu",
    normalize=True,
    trust_remote_code=False,
)

release = build_release(
    open_catalog("dist/catalog"),
    "dist/release",
    profiles={
        "sentence-transformers/all-MiniLM-L6-v2": EmbeddingProfile(
            embedding=embedding,
        ),
    },
)

print(release.digest)
```

Validate and publish the immutable release:

```bash
chartcoach catalog release validate dist/release
chartcoach catalog release publish dist/release --store s3://chartcoach
```

Public selection has its own lifecycle:

```bash
chartcoach catalog release select "$RELEASE_DIGEST" --store s3://chartcoach
```

The selected record lives at `catalog.json`. Immutable releases live under
`catalog/releases/<digest>/`.

## License

Apache-2.0. See [LICENSE](LICENSE).
