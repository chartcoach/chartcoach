# chartcoach

The `chartcoach` Python package opens a Guideline Catalog from local files or a
published release. It provides the stored guideline records plus Polars and
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
record = catalog.entry("directly-label-series-instead-of-using-a-color-key")
print(record["title"])
```

Expected output:

```text
Directly label colored series instead of relying on a color key
```

This call downloads the catalog files over HTTPS, verifies their recorded byte
counts and SHA-256 hashes, and caches the verified files.

## Choose a catalog source

`open_catalog(source)` accepts:

| Source                     | Behavior                                            |
| -------------------------- | --------------------------------------------------- |
| Authored folder            | Reads `MANIFEST.md` and `entries/<id>/guideline.md` |
| Compiled bundle            | Reads `MANIFEST.md` and `entries.parquet`           |
| Local release directory    | Reads its `release.json` and verifies listed files  |
| `catalog.json` path or URL | Follows the currently selected release              |
| `release.json` path or URL | Keeps one release digest across calls               |
| Omitted                    | Opens the official selected catalog                 |

Install `chartcoach[cloud]` for S3, GCS, or Azure sources.

## Query tables

`catalog.to_frame()` returns the six stored fields for each guideline.
`catalog.guidelines()`, `sections()`, `guideline_labels()`, `references()`,
`guideline_references()`, and `guideline_sources()` return query-ready Polars
dataframes. `catalog.duckdb()` registers those six query tables in an in-memory
DuckDB connection.

## Search an index

Install `chartcoach[index]` to open a named LanceDB index stored with a catalog
release. The following template requires a release that publishes the named
profile:

```python
from chartcoach import open_index

table = open_index(
    "https://catalog.example.com/catalog/releases/<digest>/release.json",
    profile="sentence-transformers/all-MiniLM-L6-v2",
)
```

`open_index` returns the release's `documents` table. A missing profile raises
`CatalogError` and lists the available names.

## Use chartcoach from a notebook agent

[marimo](https://docs.marimo.io/) code mode discovers `chartcoach.agent` when
chartcoach is installed in the notebook's Python environment. The module
exposes the same catalog operations used by the CLI and MCP server, plus the
version-matched [Agent Plugin](https://peter-gy.github.io/agent-plugins/)
resources:

```python
import chartcoach.agent as cc

help(cc)
tools = cc.Tools.open()
catalog = tools.catalog
candidates = cc.query_entries(
    catalog,
    contains="direct labels",
    limit=5,
    include_body=False,
)
core = cc.agent_skill()
print(core.source)
```

`cc.agent_plugin()` returns an `agent_plugins.Plugin` object.
`cc.agent_skills()` returns its `agent_plugins.Skill` objects in chartcoach
workflow order. Use `cc.agent_plugin().skill(name)` for direct lookup,
`skill.file(path)` for a checked packaged resource, and
`cc.skill_description(skill)` when presenting a discovery list.

The Agent Plugin also exposes the packaged MCP stdio entry through
`cc.agent_plugin().mcp`. Install `chartcoach[mcp]` in the agent client's Python
environment before it starts that server.

## Documentation

| Page                                                       | Details                                                       |
| ---------------------------------------------------------- | ------------------------------------------------------------- |
| [Python](https://docs.chartcoach.dev/python)               | Source types, table methods, DuckDB queries, and `open_index` |
| [Catalog CLI](https://docs.chartcoach.dev/cli)             | Terminal commands, JSON output, and exit codes                |
| [MCP server](https://docs.chartcoach.dev/mcp)              | SQL and search tools for MCP clients                          |
| [Curate and publish](https://docs.chartcoach.dev/curation) | Authoring, build, publication, and public selection           |

chartcoach is licensed under [Apache-2.0](LICENSE).
