# Python catalog code

One `Catalog` owns its Python guideline entries, manifest, and resolved release.
Runtime code resolves locations and injects exact-release profile loaders.
Curation code builds, validates, publishes, and selects releases.

```text
public open_catalog
  -> _catalog/runtime
     -> Catalog + exact release loaders

Catalog
  -> query, read, cite, describe
  -> direct Polars and DuckDB objects
  -> injected LanceDB index loader

_catalog/curation
  -> catalog and release contracts
  -> profile production and validation
  -> publication and selection
```

`_catalog/runtime` and `_catalog/curation` do not import each other. Both use the
pure release and profile contracts.

## Runtime ownership

| Module                 | Work                                                                 |
| ---------------------- | -------------------------------------------------------------------- |
| `runtime/__init__.py`  | Resolves one location and creates the release-bound `Catalog`        |
| `runtime/location.py`  | Classifies local, HTTP, and cloud inputs                             |
| `runtime/transport.py` | Reads bounded byte streams                                           |
| `runtime/release.py`   | Resolves `catalog.json` or `release.json` once                       |
| `runtime/profiles.py`  | Loads profile metadata and LanceDB tables from that release          |
| `runtime/cache.py`     | Verifies remote files and publishes protected extraction generations |
| `profile_layout.py`    | Owns profile IDs, filenames, and release-inventory discovery         |
| `authored.py`          | Loads authored guideline folders and bibliography files              |
| `model.py`             | Owns the `Catalog` guideline entries, manifest, and operations       |
| `guidelines.py`        | Owns the `Guideline` and `Section` models                            |

`open_catalog(location)` accepts authored folders, bundles, release directories,
local deployed roots, `catalog.json`, `release.json`, and the omitted official
location. A deployed root resolves its `catalog.json` through
`catalog/releases/<digest>/`. Local release bases become absolute before the
catalog is returned. Remote loaders retain copied storage options in private
closures.

The public `Catalog(frame, manifest=...)` constructor creates an unverified
in-memory catalog. Runtime state enters through `Catalog._from_runtime` after
release resolution and byte verification. Public construction cannot attach a
release descriptor or profile loader.

## Catalog operations

`Catalog` delegates repeated domain work to focused modules:

| Method     | Owner                                      |
| ---------- | ------------------------------------------ |
| `query`    | `_catalog/query.py`                        |
| `read`     | `_catalog/read.py`                         |
| `cite`     | `_catalog/references.py`                   |
| `describe` | `_catalog/description.py`                  |
| `table`    | `_catalog/relations.py` and table builders |
| `duckdb`   | `chartcoach/duckdb.py`                     |
| `artifact` | Injected verified artifact loader          |
| `cache`    | Injected complete release materializer     |
| `index`    | Injected runtime loader                    |

Reference tables retain the authored BibTeX and resolved source fields. RefKit
renders each distinct reference with the APA style, and the catalog caches the
result for subsequent reads and citations. Polars holds the derived tables.
At 32 distinct sources, rendering uses up to eight threads within Polars'
configured thread limit. Smaller catalogs and single-thread runtimes render
sequentially. Each source keeps its own citation context.

The CLI and MCP adapters parse and bound transport input. Their SQL and search
services in `_catalog/sql.py` and `_catalog/search.py` own bounded transport
records. Native Python composition uses the returned DuckDB connection or
LanceDB table. `chartcoach.agent` exports `Catalog`, `CatalogError`,
`open_catalog`, and the packaged Agent Plugin locator.

Each `Catalog` caches its derived tables, canonical documents, and entries
digest. A per-catalog lock protects initialization, and public dataframe
methods return isolated clones. Release selection and credentials remain
with their runtime owners.

`catalog.duckdb()` materializes fresh connection-owned tables through the
[Arrow C Stream interface](https://arrow.apache.org/docs/format/CStreamInterface.html),
a columnar data interchange protocol. The private stream adapter keeps this
path available with the base dependencies. Temporary registrations are released
after materialization. Mutating or closing a connection leaves the catalog and
other connections unchanged.

## Verified artifact cache

`Catalog.artifact(path)` resolves one release inventory entry to a verified
local file. `Catalog.cache()` copies every release artifact into
`releases/<digest>/` under the platform cache and writes `release.json` last.
Existing files are verified before reuse. The resulting directory opens through
`open_catalog` with the original release identity.

Remote digest-addressed descriptors are cached under `descriptors/<digest>.json`.
They are parsed and their content digest is checked on reuse. Selection files
are fetched on each open. A damaged descriptor or artifact is fetched again.

Remote artifacts are content-addressed files. A missing file is streamed to a
unique staging path, checked against its byte count and SHA-256 hash, then
published atomically.

Shared index extraction uses `indexes-v2/<archive-digest>/`:

```text
current.json
generations/
  <generation-id>/
    .complete
    documents.lance/
```

Each generation is sealed read-only before `current.json` names it. Repair
publishes another generation and retains generations that may still have open
LanceDB readers. The returned table is also checked out at its current
version. On platforms where POSIX permission bits cannot protect the path,
callers provide a new writable extraction directory explicitly.
The CLI and MCP search service keeps its LanceDB table private and can use an
internal cache on those platforms.

`catalog.index(profile, directory=...)` extracts verified bytes into that new
caller-owned directory. The returned LanceDB table is writable, and the caller
owns the directory lifetime.

## Profile loading

`catalog.describe(profile=...)` reads `profile.json`. It verifies the artifact
hash and byte count, enforces the 64 KiB limit, parses the closed schema, and
checks the entries and manifest digests.

`catalog.index(profile)` then extracts the archive and compares LanceDB schema
metadata and vector dimensions with `profile.json`. It never reads
`table.embedding_functions` during opening or FTS.

The CLI and MCP vector and hybrid search service validates the registered LanceDB class,
model fields, portable variable policy, and exact Python requirements before
passing text to LanceDB. LanceDB reconstructs the persisted function and calls
its query embedding method. FTS uses explicit `query_type="fts"` and keeps that
provider path idle.

Profile production creates the full-text index. Vector queries scan stored
vectors until a producer explicitly creates a LanceDB approximate vector index.
The index archive remains portable because it supplies one hashed byte sequence
for bounded extraction and offline copying.

Profiles use a flat lowercase ID and are discovered from `profile.json`.
`index.tar.gz` is required. `documents.parquet` is an optional portable
document/vector export. `projection.parquet` is required exactly when
`profile.json` contains projection metadata.

## Capability tiers

| Extra        | Enables                                                |
| ------------ | ------------------------------------------------------ |
| `cloud`      | S3, GCS, and Azure locations through Obstore           |
| `index`      | LanceDB tables and index search                        |
| `mcp`        | Model Context Protocol transport                       |
| `curation`   | Profile builds, validation, publication, and selection |
| `projection` | UMAP projection during profile production              |

The base package includes DuckDB, Polars, and `typing-extensions`.
Optional imports stay inside the features that use them.

## Curation flow

```text
authored folder
  -> compiled bundle
  -> release.json with optional profile artifacts
  -> immutable published release
  -> catalog.json selection
```

`build_release` writes core artifacts and optional profiles. Every profile has
`profile.json` and `index.tar.gz`. `export_documents=True` adds the portable
document/vector export. An `umap` mapping adds the separate projection export
and loads UMAP during the build.

`ProfileReuse.release` names a local exact release. The reuse path verifies the
source profile and compares its indexed rows with the target catalog, copies
the original index archive, and
derives requested exports from stored vectors. Projection rebuilds retain the
embedding bytes and binding while the embedding provider stays unconstructed.
Artifact validation checks the portable binding and stored vectors. Query-time
semantic validation checks the registered alias and declared provider versions.

`IndexProfile` accepts a native LanceDB table. It reads complete rows and
vectors into a new table to make the released data self-contained, including
when the source table uses external storage. It retains the embedding binding
and canonical document fields. `configure(table)` builds native release indexes
after materialization. All reused and precomputed profiles are prepared before
fresh embedding work begins. Canonical document comparisons use values so
equivalent Arrow string representations agree. Native ingestion emits regular
UTF-8 strings and string lists for LanceDB scalar indexes.

`validate_release` combines catalog validation with descriptor and
byte verification. It first compares the LanceDB table with canonical catalog
documents and `profile.json`. It then checks an optional document export
against the index rows and checks projection identity, coordinates, and
neighbors in `projection.parquet`. Artifact validation reads stored vectors
and portable bindings. Provider packages and credentials are required when
computing embeddings, not when validating stored artifacts.

`validate_published_release` reads fresh store bytes into a bounded temporary
directory and applies the same checks. When checking the selected release, it
also compares `catalog.json` with the immutable descriptor it names.

Publication uploads artifacts first and commits `release.json` last. Selection
validates the published candidate before copying its descriptor to
`catalog.json`. A committed publication is checked again before an idempotent
publish reports success.

Published release directories are self-contained. Runtime caches live under
the user cache, and writable index copies live in caller-selected work
directories. Immutable HTTP release files can use long-lived caching.
`catalog.json` remains revalidation-friendly. Browser deployments configure
cross-origin resource sharing for every artifact a browser reads.

## Focused checks

| Change                    | Command                                                                                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Runtime location or cache | `uv run --locked --package chartcoach --all-extras pytest packages/chartcoach/tests/test_catalog_runtime.py packages/chartcoach/tests/test_runtime_index.py`                                       |
| Profile production        | `uv run --locked --package chartcoach --all-extras pytest packages/chartcoach/tests/test_release_builder.py`                                                                                       |
| Profile validation        | `uv run --locked --package chartcoach --all-extras pytest packages/chartcoach/tests/test_release_validation.py`                                                                                    |
| Catalog operations        | `uv run --locked --package chartcoach --all-extras pytest packages/chartcoach/tests/test_catalog_operations.py`                                                                                    |
| CLI and MCP               | `uv run --locked --package chartcoach --all-extras pytest packages/chartcoach/tests/test_cli_catalog.py packages/chartcoach/tests/test_cli_search.py packages/chartcoach/tests/test_mcp_server.py` |
