# Python catalog code

One `Catalog` owns its Python guideline entries, manifest, and resolved release.
Runtime code resolves locations and injects exact-release profile loaders.
Curation code builds, validates, publishes, and selects releases.

```text
public open_catalog
  -> catalog/runtime
     -> Catalog + exact release loaders

Catalog
  -> query, read, cite, describe, SQL
  -> direct Polars and DuckDB objects
  -> injected LanceDB index loader

catalog/curation
  -> catalog and release contracts
  -> profile production and validation
  -> publication and selection
```

`catalog/runtime` and `catalog/curation` do not import each other. Both use the
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

| Method     | Owner                                     |
| ---------- | ----------------------------------------- |
| `query`    | `catalog/query.py`                        |
| `read`     | `catalog/read.py`                         |
| `cite`     | `catalog/references.py`                   |
| `describe` | `catalog/description.py`                  |
| `table`    | `catalog/relations.py` and table builders |
| `duckdb`   | `chartcoach/duckdb.py`                    |
| `sql`      | `catalog/sql.py`                          |
| `search`   | `catalog/search.py`                       |
| `index`    | Injected runtime loader                   |

The CLI and MCP adapters parse and bound transport input, call these methods,
and render their results. `chartcoach.agent` exports `Catalog`, `CatalogError`,
`open_catalog`, and the packaged Agent Plugin locator.

## Verified artifact cache

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
`Catalog.search` keeps its LanceDB table private and can use an internal cache
on those platforms.

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

Vector and hybrid convenience search validates the registered LanceDB class,
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
| `index`      | LanceDB `0.38.0` tables and index search               |
| `mcp`        | Model Context Protocol transport                       |
| `curation`   | Profile builds, validation, publication, and selection |
| `projection` | UMAP projection during profile production              |

The base package includes DuckDB `1.5.5`, Polars, and `typing-extensions`.
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

`ProfileReuse.release` names a local exact release. The reuse path checks its
profile against the target catalog, copies the original index archive, and
derives requested exports from stored vectors. Projection rebuilds retain the
embedding bytes and binding while the embedding provider stays unconstructed.
Publication validation requires the registered alias and exact declared
provider versions.

`validate_release` combines semantic catalog validation with descriptor and
byte verification. It first compares the LanceDB table with canonical catalog
documents and `profile.json`. It then checks an optional document export
against the index rows and checks projection identity, coordinates, and
neighbors in `projection.parquet`.

Publication uploads artifacts first and commits `release.json` last. Selection
copies one already published descriptor to `catalog.json`.

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
