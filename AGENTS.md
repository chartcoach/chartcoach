# chartcoach agent guide

chartcoach publishes source-traced visualization guidance through one Guideline
Catalog contract. The repository contains the catalog readers, curation tools,
CLI, MCP server, public catalog site, and product documentation.

Read the nearest package README and behavior tests before editing a package.
Use the root commands to verify changes across package boundaries.

## Start from the product boundary

| Product decision                                      | User result                                                         | Architectural owner                                            |
| ----------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------- |
| One guideline entry record crosses every interface    | Python, JavaScript, CLI, MCP, site, and docs expose the same fields | Catalog models and the shared release fixture                  |
| Exact releases are content addressed                  | A digest resolves one verified artifact set                         | Release records, hashing, and runtime verification             |
| Public selection is independent from package releases | Catalog promotion can move after artifact validation                | Curation selection service and release workflows               |
| Runtime readers keep optional capabilities lazy       | The base package imports in Python and Pyodide                      | Python runtime composition and optional extras                 |
| Web apps consume package entry points                 | Site and docs behavior stays aligned with published SDKs            | JavaScript catalog package and app startup code                |
| References stay attached to guidance                  | People and agents can inspect the source behind a recommendation    | Guideline entry records, Markdown rendering, and public routes |

## Know where the complexity belongs

| Source of complexity                 | Contract it protects                                               |
| ------------------------------------ | ------------------------------------------------------------------ |
| Cross-language validation            | Python and JavaScript accept and reject the same wire records      |
| Local, HTTP, and cloud catalog input | One location resolves to an authored catalog, bundle, or release   |
| Integrity checks and caching         | Bytes are verified before a cached artifact becomes visible        |
| Optional index profiles              | LanceDB indexes stay tied to the release that owns their rows      |
| Immutable publication                | Artifact writes complete before `release.json` commits the release |
| Generated web outputs                | Search, LLM pages, Open Graph images, and docs reflect one catalog |

Follow the complete maps in
[Catalog files and records](development_docs/architecture/catalog-contract.md),
[Python catalog code](development_docs/architecture/runtime-and-curation.md),
and [Web apps](development_docs/architecture/web-delivery.md).

## Preserve dependency direction

The web package graph is:

```text
apps/site  -> packages/catalog
          -> packages/brand

apps/docs  -> packages/catalog
          -> packages/brand
```

`@chartcoach/catalog` is a browser-safe entry point. It imports no Node built-ins
or chartcoach workspace package. `@chartcoach/catalog/node` owns Node filesystem
loading and persistent caching. The apps consume the browser package entry point.
They do not import each other. Root lint rules and
`tools/architecture/dependencies.test.mjs` enforce this graph.

The Python read path is:

```text
public API -> runtime composition -> location and release resolution
                                  -> local, HTTP, or cloud transport
                                  -> verified artifact cache
                                  -> catalog and index loaders
```

`_catalog/runtime/` owns read orchestration. `_catalog/curation/` owns building,
validation, publication, and selection. Each depends on release models and the
small shared object-store URI helpers. They do not import each other. Optional
provider and index imports happen inside the capability that needs them.

## Keep one mutable owner

| State                            | Owner                                       |
| -------------------------------- | ------------------------------------------- |
| Public `catalog.json` selection  | `curation.select_release`                   |
| Immutable release directory      | `curation.publish_release`                  |
| Content-addressed artifact cache | `_catalog.runtime.cache`                    |
| Extracted index cache            | `_catalog.runtime.cache`                    |
| Site catalog location            | `apps/site/src/config/catalog-location.ts`  |
| Docs notebook runtime            | `apps/docs/components/notebook-runtime.tsx` |
| Docs-session JavaScript SDK      | `apps/docs/components/notebook-runtime.tsx` |
| Generated site artifacts         | The integration that writes each artifact   |

Every `catalog.json` write goes through the curation selection service.
Release artifacts are immutable after `release.json` is committed.

## Read sources of truth in order

1. `fixtures/catalog-release` for the shared release consumed by Python,
   JavaScript, site, and contract tests.
2. Python release and catalog models plus the JavaScript public package for
   executable wire behavior.
3. `_catalog/runtime/` and `_catalog/curation/` for read and write lifecycles.
4. Package manifests, Vite+ boundary rules, and architecture contract tests for
   dependency direction.
5. `development_docs/` for contributor reasoning and `apps/docs/content/docs/`
   for supported user workflows.

## Workspace ownership

| Path                       | Owns                                                                         |
| -------------------------- | ---------------------------------------------------------------------------- |
| `apps/site`                | Public catalog pages, search, LLM output, and Open Graph images              |
| `apps/docs`                | Product documentation and live Python and JavaScript examples                |
| `packages/brand`           | Reviewed assets, font imports, and CSS tokens                                |
| `packages/catalog`         | Browser-safe catalog models, release verification, and Parquet loading       |
| `packages/chartcoach`      | Python API, runtime readers, curation, CLI, MCP, Polars, DuckDB, and LanceDB |
| `fixtures/catalog-release` | Cross-language release fixture                                               |
| `tools/architecture`       | Executable workspace dependency contracts                                    |

The owning package keeps its focused tests. Cross-language tests consume the
same release fixture.

## Command contract

Run commands from the repository root.

| Task                    | Command             |
| ----------------------- | ------------------- |
| List repository targets | `make help`         |
| Install workspaces      | `make install`      |
| Check JavaScript        | `pnpm ready`        |
| Check Python            | `make python-check` |
| Build product docs      | `make docs-build`   |
| Build the public site   | `make site-build`   |
| Check the repository    | `make check`        |
| Start both web apps     | `pnpm dev`          |

Use `pnpm --dir <path> <script>` for a focused web loop. Use
`uv run --locked --package chartcoach ...` for a focused Python command. Run
`make check` before handoff.

When a dependency manifest changes, run `pnpm install` or `uv lock` and include
the matching lockfile update.

## Validate the consumer boundary

- Run the focused owner tests while working.
- Run both Python and JavaScript contract suites after a catalog row, manifest,
  release record, artifact path, or digest change.
- Build the site after changing catalog loading or generated public artifacts.
- Build and inspect the docs after changing navigation, live cells, SDK
  examples, or public contracts.
- Use browser checks for visible site and docs behavior at desktop and narrow
  widths.
- Finish with `make check`.

## Keep authored and generated files distinct

Build tools own these paths:

- `apps/docs/.next/`
- `apps/docs/.source/`
- `apps/docs/out/`
- `apps/site/.astro/`
- `apps/site/dist/`
- `packages/catalog/dist/`
- `dist/`

Change their owning source and rebuild the artifact.

## Route the task

| Task                                        | Guide                                                                          |
| ------------------------------------------- | ------------------------------------------------------------------------------ |
| General contribution                        | [Contributing](CONTRIBUTING.md)                                                |
| Catalog row, manifest, or release fields    | [Catalog files and records](development_docs/architecture/catalog-contract.md) |
| Python location, transport, cache, or index | [Python catalog code](development_docs/architecture/runtime-and-curation.md)   |
| Site, docs, or generated web output         | [Web apps](development_docs/architecture/web-delivery.md)                      |
| Package release or catalog promotion        | [Releasing packages and catalog data](development_docs/releasing.md)           |
