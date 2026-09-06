# Python catalog code

The Python package separates reading a catalog from creating and publishing
one. Runtime code reads sources and verifies files. Curation code builds,
validates, publishes, and selects releases.

```text
open_catalog / open_index
  -> catalog/runtime/
     -> catalog and release models

catalog/curation/
  -> catalog and release models
```

The two directories do not import each other. Both can use the URI helpers in
`catalog/_object_store.py`.

## Runtime modules

| Module                 | Work                                                                    |
| ---------------------- | ----------------------------------------------------------------------- |
| `runtime/__init__.py`  | Implements `open_catalog` and `open_index`                              |
| `runtime/source.py`    | Classifies local paths, HTTP URLs, and cloud URLs                       |
| `runtime/transport.py` | Reads byte streams with size limits from local, HTTP, and cloud sources |
| `runtime/release.py`   | Parses `catalog.json` and `release.json` and resolves listed files      |
| `runtime/cache.py`     | Verifies downloaded files and extracts LanceDB indexes                  |

`open_catalog` handles these inputs:

| Input                      | Read path                            |
| -------------------------- | ------------------------------------ |
| Authored folder            | `MANIFEST.md` plus `entries/`        |
| Compiled bundle            | `MANIFEST.md` plus `entries.parquet` |
| Release directory          | Local `release.json`                 |
| `catalog.json` path or URL | Current selected digest              |
| `release.json` path or URL | One exact digest                     |
| Omitted                    | Official selected catalog            |

`open_index` accepts a release directory, `catalog.json`, or `release.json`
because the profile files must be listed by a release. An omitted source opens
the official selected catalog.

## Download and cache order

For a remote file, the runtime:

1. Reuses an existing cache file after checking its size and SHA-256 hash.
2. Streams a missing file into a uniquely named temporary file.
3. Rejects a stream that exceeds or misses the recorded byte count.
4. Rejects a SHA-256 mismatch.
5. Atomically moves the verified temporary file into the cache.
6. Removes the temporary file on every exit path.

For a LanceDB index, the runtime extracts into a temporary directory, confirms
that `documents.lance` exists, writes the completion marker, and then moves the
directory into the cache. If LanceDB cannot open a completed cache, the runtime
extracts it once more before returning the error.

## Optional dependencies

| Extra      | Enables                                                        |
| ---------- | -------------------------------------------------------------- |
| `cloud`    | S3, GCS, and Azure sources through Obstore                     |
| `index`    | LanceDB search indexes stored with a release                   |
| `mcp`      | Model Context Protocol server                                  |
| `curation` | Catalog builds, release validation, publication, and selection |

Imports for these libraries stay inside the code that needs them. The base
package therefore imports in ordinary Python and Pyodide without loading the
optional libraries.

## Curation flow

```text
authored folder
  -> compiled bundle
  -> local release.json and optional profile files
  -> published files
  -> public catalog.json selection
```

`build_release` writes a new local release directory. Validation checks the
catalog files, profile rows, archive contents, and recorded hashes.

Publication uploads the files first and writes `release.json` last. If a prior
attempt stopped before that final write, publication can upload the missing
files and finish the release. Once `release.json` exists, a repeated publish
must produce the same release record.

Selection reads the published `release.json`, verifies its digest, and writes
that record to `catalog.json`. It does not download every listed file. The
release workflow opens the exact public URL through a reader before selection
to verify `MANIFEST.md` and `entries.parquet`.

## Checks by change

| Change                   | Focused command                                                                                              |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| Source paths or URLs     | `uv run --locked --package chartcoach --all-extras pytest packages/chartcoach/tests/test_catalog_runtime.py` |
| Cache or index loading   | `uv run --locked --package chartcoach --all-extras pytest packages/chartcoach/tests/test_runtime_index.py`   |
| Release building         | `uv run --locked --package chartcoach --all-extras pytest packages/chartcoach/tests/test_release_builder.py` |
| Publication or selection | `uv run --locked --package chartcoach --all-extras pytest packages/chartcoach/tests/test_release_publish.py` |
| Import direction         | `uv run --locked --package chartcoach pytest packages/chartcoach/tests/test_architecture.py`                 |
