# chartcoach

The `chartcoach` Python package opens a Guideline Catalog from local files or a
published release. It provides guideline entries plus Polars and
DuckDB tables for sections, labels, and references.

chartcoach is alpha software and supports Python 3.10 through 3.14. Installing
the package also installs the `chartcoach` CLI.

## Read one guideline

```bash
uv add chartcoach
```

```python
from chartcoach import open_catalog

catalog = open_catalog(
    "https://files.peter.gy/packages/python/chartcoach/0.2.0/docs-catalog/c0f6dbec3dd31b07763b46fd458733db0b8b50c5793cf9447458119287129420/release.json"
)
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
Polars dataframe. Each call returns an independent dataframe that callers can
transform or mutate while the `Catalog` keeps its stored entries unchanged.
`catalog.duckdb()` registers those six catalog tables in an in-memory DuckDB
connection.

## Search an index

Install `chartcoach[index]` to open a named LanceDB index stored with a catalog
release. The following template requires a release that publishes the named
profile:

```python
from chartcoach import open_catalog

catalog = open_catalog(
    "https://catalog.example.com/catalog/releases/<digest>/release.json",
)
table = catalog.index("minilm-normalized")
```

`catalog.index()` returns the release's LanceDB `documents` table from a
protected shared extraction. Pass a new `directory=Path(...)` for a
caller-owned writable copy. A missing profile raises `CatalogError` and lists
the available names. Profile IDs are flat lowercase release handles. Inspect
`catalog.describe(profile=...)` for the embedding binding, dimensions,
`distance_metric`, and `python_requirements`.

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
candidates = catalog.query(contains="direct labels", limit=5)
selected_ids = candidates.get_column("id").head(3).to_list()
records = catalog.read(ids=selected_ids, source_detail="minimal")
citations = catalog.cite(ids=selected_ids)
core = cc.agent_plugin().skill("core")
print(core.source)
```

`cc.agent_plugin()` returns an `agent_plugins.Plugin` object.
Use `cc.agent_plugin().skill(name)` for direct lookup and `skill.file(path)`
for a checked packaged resource.

The Agent Plugin also declares the packaged MCP stdio entry through
`cc.agent_plugin().mcp`. Install `chartcoach[mcp]` in the agent client's Python
environment before it starts that server. Agents can inspect the complete
module workflow with `help(cc)`.

[marimo](https://docs.marimo.io/) is one environment for code-mode agents. It
discovers `chartcoach.agent` through the installed `marimo.agent.capability`
entry point.

## Documentation

| Page                                                       | Details                                             |
| ---------------------------------------------------------- | --------------------------------------------------- |
| [Python](https://docs.chartcoach.dev/python)               | Catalog methods plus Polars, DuckDB, and LanceDB    |
| [Catalog CLI](https://docs.chartcoach.dev/cli)             | Terminal commands, JSON output, and exit codes      |
| [MCP server](https://docs.chartcoach.dev/mcp)              | SQL and search tools for MCP clients                |
| [Curate and publish](https://docs.chartcoach.dev/curation) | Authoring, build, publication, and public selection |

chartcoach is licensed under [Apache-2.0](LICENSE).
