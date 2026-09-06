# Architecture

chartcoach turns authored Markdown guidelines into verified catalog files read
by Python, JavaScript, the CLI, the MCP server, the public site, and the docs.

```text
MANIFEST.md + guideline.md files
  -> MANIFEST.md + entries.parquet
  -> release.json + release files
  -> catalog.json selecting the public release
  -> Python, JavaScript, CLI, MCP, site, docs, and agents
```

The guideline record and four files are shared between these interfaces:
`MANIFEST.md`, `entries.parquet`, `release.json`, and `catalog.json`.

## Repository parts

| Path                       | Reads or writes                                                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------- |
| `packages/chartcoach`      | Python records, Polars and DuckDB tables, remote downloads, cache, release building, CLI, and MCP |
| `packages/catalog`         | Browser-safe release loading, Parquet parsing, JavaScript records, and Markdown serialization     |
| `apps/site`                | Public guideline pages, search data, LLM files, Open Graph images, and sitemap                    |
| `apps/docs`                | Guides, reference pages, and live Python and JavaScript examples                                  |
| `packages/brand`           | Shared logos, fonts, and CSS variables                                                            |
| `fixtures/catalog-release` | Small release read by both clients and local site builds                                          |

The package or app that writes a value also owns its validation. Callers use
the public package entry point instead of importing implementation files from
another workspace package.

## Dependency direction

```text
apps/site  -> packages/catalog
          -> packages/brand

apps/docs  -> packages/catalog
          -> packages/brand
```

`packages/catalog` imports no app, brand package, or Node built-in. The two
apps do not import each other. Vite+ rules check source imports, and
`tools/architecture` checks package manifests and relative paths.

The Python read and write paths meet at the catalog and release models:

```text
public API -> catalog/runtime/  -> catalog and release models
curation/ ---------------------> catalog and release models
```

`catalog/runtime/` reads sources, downloads and verifies files, and manages
caches. `catalog/curation/` builds, validates, publishes, and selects releases.
They share the small URI helpers in `catalog/_object_store.py` and do not import
each other.

## Files that change over time

| File or directory                        | What changes it              | When readers can trust it                                     |
| ---------------------------------------- | ---------------------------- | ------------------------------------------------------------- |
| `catalog.json`                           | `catalog release select`     | Its release digest is valid                                   |
| `catalog/releases/<digest>/release.json` | `catalog release publish`    | Every listed file has been uploaded                           |
| Download cache                           | Python runtime               | File size and SHA-256 match `release.json`                    |
| Extracted LanceDB cache                  | Python runtime               | The `documents` table opens and the completion marker matches |
| Generated site files                     | The owning Astro integration | The site build completes                                      |
| Static notebook output                   | The MDX notebook compiler    | The cell executes during the docs build                       |

The detailed documents divide by the files and code they describe:

- [Catalog files and records](architecture/catalog-contract.md)
- [Python catalog code](architecture/runtime-and-curation.md)
- [Web apps](architecture/web-delivery.md)
- [Releasing packages and catalog data](releasing.md)
