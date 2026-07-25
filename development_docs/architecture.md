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

## Dependency direction

```text
apps/site  -> packages/catalog
          -> packages/brand

apps/docs  -> packages/brand
```

`packages/catalog` is a browser-safe leaf. It stays independent from the apps,
brand assets, and Node built-ins. The root Vite+ policy enforces this boundary.
Cross-package TypeScript imports use package names.

The root `package.json` and `vite.config.ts` own JavaScript orchestration and
shared policy. Package manifests own dependencies, focused scripts, tests, and
build configuration. Shared external versions live in the pnpm catalog.

The root `pyproject.toml` defines the uv workspace and development tools.
Publishable Python metadata and build configuration live in
`packages/chartcoach/pyproject.toml`.

## Python runtime boundary

`open_catalog(source)` and `open_index(source, profile=...)` classify a local
path or descriptor URI before filesystem handling. Both functions resolve the
same release envelope. A selected `catalog.json` points to immutable artifacts
under `catalog/releases/<digest>/`. An exact `release.json` resolves artifacts
beside that descriptor.

`catalog/runtime.py` owns source normalization, HTTP reads, integrity checks,
content-addressed caching, and safe index extraction. Runtime code can import
release models. It cannot import curation.

Optional extras own capability boundaries:

| Extra      | Boundary                                                                |
| ---------- | ----------------------------------------------------------------------- |
| `cloud`    | Read S3, GCS, and Azure descriptor URIs through Obstore                 |
| `index`    | Open release-backed native LanceDB profiles                             |
| `mcp`      | Run the MCP server                                                      |
| `curation` | Build profiles, validate releases, publish objects, and select releases |

Curation accepts LanceDB embedding functions from the caller. Each profile
keeps its own vector space, UMAP projection, neighbor graph, and native LanceDB
archive.

Obspec defines the internal write operations used by curation. Obstore supplies
the concrete cloud and local adapters at the curation boundary. Public
consumers pass paths or descriptor URIs.

## Lifecycle boundary

Package tags publish the Python and npm packages after package CI. Catalog
promotion starts from an already published immutable release. The promotion
workflow verifies an exact release URL, builds the site from that URL, updates
`catalog.json`, and deploys the prepared site. A failed deployment restores the
previous selection.

## Cross-workspace changes

| Change                           | Update together                                                                |
| -------------------------------- | ------------------------------------------------------------------------------ |
| Catalog row or manifest shape    | Python reader, JavaScript reader, shared fixture, site consumers, product docs |
| Release envelope or object keys  | Python release model, JavaScript release reader, curation services, fixture    |
| Embedding profile artifact shape | Curation builder, validator, runtime index loader, analysis documentation      |
| Brand asset or token             | `packages/brand` and its site or docs consumer                                 |
| Dependency                       | Owning manifest and matching lockfile                                          |

Use [Development workflow](development.md) for the commands that verify each
boundary.
