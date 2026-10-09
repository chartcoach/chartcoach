# chartcoach

The `chartcoach` Python package opens a Guideline Catalog from local files or a
published release. It provides guideline entries plus Polars and
DuckDB tables for sections, labels, and references.

chartcoach is alpha software. Installing the package also installs the
`chartcoach` CLI.

## Read one guideline

```bash
uv add chartcoach
```

```python
from chartcoach import open_catalog

catalog = open_catalog()
record = catalog.read(
    ids=["directly-label-series-instead-of-using-a-color-key"],
    source_detail="minimal",
)[0]
print(record["title"])
```

Expected output:

```text
Directly label colored series instead of relying on a color key
```

This call downloads the catalog files over HTTPS, verifies the byte counts and
SHA-256 hashes listed by the release, and caches the verified files.

## Choose a catalog location

`open_catalog(location)` accepts:

| Location                   | Behavior                                            |
| -------------------------- | --------------------------------------------------- |
| Authored folder            | Reads `MANIFEST.md` and `entries/<id>/guideline.md` |
| Compiled bundle            | Reads `MANIFEST.md` and `entries.parquet`           |
| Local deployed root        | Opens the release selected by its `catalog.json`    |
| Local release directory    | Reads its `release.json` and verifies listed files  |
| `catalog.json` path or URL | Follows the currently selected release              |
| `release.json` path or URL | Keeps one release digest across calls               |
| Omitted                    | Opens the official selected catalog                 |

Install `chartcoach[cloud]` for S3, GCS, or Azure locations.

## Query catalog tables

`catalog.to_frame()` returns the six stored fields for each guideline.
`catalog.table(name)` returns `guidelines`, `sections`, `guideline_labels`,
`references`, `guideline_references`, or `guideline_sources` as a query-ready
Polars dataframe. Tables are derived on first use and reused within the
`Catalog`. Each call returns an independent dataframe handle that callers can
transform or mutate while the cached tables stay unchanged.
`catalog.duckdb()` registers those six catalog tables in an in-memory DuckDB
connection owned by the caller. Reuse it for related queries and close it after
use.

## Search an index

Install `chartcoach[index]` to open a named LanceDB index stored with a catalog
release. The following template requires a release that publishes the named
profile:

```python
from chartcoach import open_catalog

catalog = open_catalog("dist/release-indexed")
table = catalog.index("minilm-normalized")
hits = (
    table.search("direct labels", query_type="fts", fts_columns="text")
    .select(["id", "parent_id", "role", "_score"])
    .limit(5)
    .to_list()
)
ids = list(dict.fromkeys(hit["parent_id"] for hit in hits))
records = catalog.read(ids=ids)
```

`catalog.index()` returns the release's LanceDB `documents` table from a
protected shared extraction. Pass a new `directory=Path(...)` for a
caller-owned writable copy. A missing profile raises `CatalogError` and lists
the available names. Profile IDs are flat lowercase release handles. Inspect
`catalog.describe(profile=...)` for the embedding binding, dimensions,
`distance_metric`, and `python_requirements`.
Explicit full-text search keeps embedding providers idle. Project the fields
needed for candidate selection, then read the parent entries' context and
exceptions before applying their advice.

## Compose verified release files

```python
entries = catalog.artifact("entries.parquet")
with catalog.duckdb() as connection:
    rows = connection.read_parquet(str(entries)).select("id, title").limit(5).fetchall()

local = catalog.cache()
offline = open_catalog(local)
```

`catalog.release.artifacts` lists available files, including optional document
and projection Parquet exports. `artifact(path)` verifies and caches the file
before returning a local path. `cache()` materializes every release file into
a directory that opens offline. Remote artifacts and digest-addressed
descriptors use the per-user [platformdirs](https://platformdirs.readthedocs.io/)
cache. Selected catalogs refresh `catalog.json` on each open.

For S3, pass your descriptor URI and the storage client's options to
`open_catalog(location, storage_options=...)` with `chartcoach[cloud]` installed.
See [Open and cache catalogs](https://docs.chartcoach.dev/catalogs).
Use native DuckDB connections and LanceDB tables for SQL, filtering, reranking,
batch search, and exports. Index `parent_id` values identify guideline entries.

## Use chartcoach from a code-mode agent

chartcoach follows the open
[Agent Plugins specification](https://agent-plugins.org/). The installed Python
distribution carries its version-matched Agent Skills and Model Context
Protocol server configuration. A code-mode agent can inspect those components
and call the chartcoach Python API directly:

```python
import chartcoach.agent as cc

help(cc)
catalog = cc.open_catalog()
candidates = catalog.query(contains="labels", limit=5)
selected_ids = candidates.get_column("id").head(3).to_list()
records = catalog.read(ids=selected_ids, source_detail="minimal")
citations = catalog.cite(ids=selected_ids)
core = cc.agent_plugin().skill("core")
print(core.source)
```

`cc.agent_plugin()` returns an `agent_plugins.Plugin` object.
Use `cc.agent_plugin().skill(name)` for direct lookup and `skill.file(path)`
for a checked packaged resource.

`contains` matches a contiguous phrase in the ID, title, or description.
The `core` skill teaches query recovery, index and SQL selection, and compact
results. Load the matching workflow skill for chart review, recommendation,
discussion, or contribution.

The Agent Plugin also declares the packaged MCP stdio entry through
`cc.agent_plugin().mcp`. Install `chartcoach[mcp]` in the agent client's Python
environment before it starts that server. Agents can inspect the complete
module workflow with `help(cc)`.

[marimo](https://docs.marimo.io/) is one environment for code-mode agents. It
discovers `chartcoach.agent` through the installed `marimo.agent.capability`
entry point.

## Compose or deploy MCP

```bash
uvx --from "chartcoach[mcp]" chartcoach mcp
```

The CLI loads `.env` in its working directory, or the file selected by
`--env-file`. Options override process environment; process environment overrides
dotenv. For HTTP hosting set `CHARTCOACH_MCP_TRANSPORT=streamable-http`,
`CHARTCOACH_MCP_HOST=0.0.0.0`, and
`CHARTCOACH_MCP_PUBLIC_URL=https://mcp.chartcoach.dev`. Set
`CHARTCOACH_MCP_TOKEN` for bearer authentication. The MCP endpoint defaults to
`/mcp`, with unauthenticated readiness at `/healthz`.
See [.env.example](.env.example) for deployment settings.

`chartcoach.mcp` exports `MCPConfig`, `load_config`, `register_tools`,
`create_server`, `create_app`, and `run`. Bind your own `Catalog`, extend an SDK
server, or mount the ASGI app with its lifespan. The Python factories do not
load dotenv or mutate the process environment.

Select a release-owned profile with `CHARTCOACH_INDEX_PROFILE`. Its `$var:name`
credentials resolve from environment variables or a private
`CHARTCOACH_EMBEDDING_VARS` JSON file. Each server retains its own lazy native
embedding function; FTS stays independent of providers. Install
`chartcoach[mcp,embedding-openai]` for the native
`chartcoach.embeddings.OpenAICompatibleEmbeddings` adapter, which accepts
arbitrary model IDs and explicit dimensions for OpenRouter or another
OpenAI-compatible endpoint. Build a new release profile when changing the model,
dimensions, or endpoint; runtime credentials cannot change stored vector identity.
The [MCP guide](https://docs.chartcoach.dev/mcp) covers composition and hosting.
The [model connection guide](https://docs.chartcoach.dev/model-connections) owns the
shared provider-neutral environment settings and profile-build example.
`CHARTCOACH_EMBEDDING_API_KEY` is separate from the chat text credential;
`CHARTCOACH_EMBEDDING_API_KEY_ENV` selects another credential variable.

## Documentation

| Page                                                       | Details                                             |
| ---------------------------------------------------------- | --------------------------------------------------- |
| [Python](https://docs.chartcoach.dev/python)               | Catalog methods plus Polars, DuckDB, and LanceDB    |
| [Catalog CLI](https://docs.chartcoach.dev/cli)             | Terminal commands, JSON output, and exit codes      |
| [MCP server](https://docs.chartcoach.dev/mcp)              | SQL and search tools for MCP clients                |
| [Curate and publish](https://docs.chartcoach.dev/curation) | Authoring, build, publication, and public selection |

chartcoach is licensed under [Apache-2.0](LICENSE).
