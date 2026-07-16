# Architecture and ownership

chartcoach keeps one Guideline Catalog contract across authored data, compiled
artifacts, Python and JavaScript readers, and the two web apps.

## Data flow

```text
authored folder
  -> MANIFEST.md + entries.parquet
  -> immutable release + optional embedding profiles
  -> catalog.json selection
  -> Python, JavaScript, site, docs, CLI, MCP, and agent consumers
```

An authored folder contains `MANIFEST.md` and `entries/<id>/guideline.md` files.
Compilation preserves the manifest and writes the six-field catalog wire shape
to `entries.parquet`. The readers derive Markdown bodies and queryable tables
from those rows.

## Workspace ownership

| Path                       | Owns                                                                          |
| -------------------------- | ----------------------------------------------------------------------------- |
| `apps/site`                | Astro pages, catalog browser, LLM output, search index, and Open Graph images |
| `apps/docs`                | Next.js and Fumadocs product documentation                                    |
| `packages/brand`           | Reviewed brand assets, font imports, and CSS tokens                           |
| `packages/catalog`         | Browser-safe release validation, Parquet loading, and catalog models          |
| `packages/chartcoach`      | Python catalog model, Polars and DuckDB tables, CLI, MCP, and curation        |
| `fixtures/catalog-release` | Release artifacts shared by JavaScript, site, and Python contract tests       |

The package owning a behavior also owns its focused tests. Cross-language wire
tests read the same fixture.

## Python dependency boundary

The base `chartcoach` package loads authored folders and compiled bundles with
Pyodide-compatible dependencies. Optional extras own integration boundaries:

| Extra      | Boundary                                                                                      |
| ---------- | --------------------------------------------------------------------------------------------- |
| `index`    | Open native LanceDB indexes                                                                   |
| `mcp`      | Run the MCP server                                                                            |
| `curation` | Build embedding profiles, project vectors, cache releases, and publish through object storage |

Curation accepts LanceDB embedding functions from the caller. Each profile
keeps its own vector space, UMAP projection, neighbor graph, and native LanceDB
archive.

Obspec defines the storage operations used by curation. Obstore supplies local,
HTTP, and S3-compatible stores. Cache and publication code use the same object
key contract from `chartcoach.paths`.

## Cross-workspace changes

| Change                           | Update together                                                                |
| -------------------------------- | ------------------------------------------------------------------------------ |
| Catalog row or manifest shape    | Python reader, JavaScript reader, shared fixture, site consumers, product docs |
| Release envelope or object keys  | Python release model, JavaScript release reader, `chartcoach.paths`, fixture   |
| Embedding profile artifact shape | Curation builder, validator, cache, analysis documentation                     |
| Brand asset or token             | `packages/brand` and its site or docs consumer                                 |
| Dependency                       | Owning manifest and matching lockfile                                          |

Use [Development workflow](development.md) for the commands that verify each
boundary.
