# ChartCoach agent guide

ChartCoach is a visualization guidance monorepo. It contains the public site,
product documentation, browser and Python catalog readers, CLI and MCP
interfaces, and catalog curation tools.

Read the nearest package README and behavior tests before editing a package.
Use the root commands to verify changes across package boundaries.

## Command contract

Run commands from the repository root.

| Purpose                | Command                                                           | Expected result                |
| ---------------------- | ----------------------------------------------------------------- | ------------------------------ |
| Install JavaScript     | `pnpm install --frozen-lockfile`                                  | Lockfile installs unchanged    |
| Install Python         | `uv sync --locked --package chartcoach --all-groups --all-extras` | Environment matches `uv.lock`  |
| Check format and lint  | `pnpm check`                                                      | Vite+ reports no issues        |
| Typecheck web packages | `pnpm typecheck`                                                  | TypeScript and app checks pass |
| Test web packages      | `pnpm test`                                                       | Package tests pass             |
| Build web packages     | `pnpm build`                                                      | Package builds complete        |
| Check JavaScript       | `pnpm ready`                                                      | All JavaScript gates pass      |
| Check Python           | `make python-check`                                               | All Python gates pass          |
| Check the repository   | `make check`                                                      | Every handoff gate passes      |
| Start both web apps    | `pnpm dev`                                                        | Portless starts both apps      |

Use `pnpm --dir <path> <script>` for a focused package loop. Use
`uv run --locked --package chartcoach ...` for a focused Python command.
Run `make check` before handoff.

When a dependency manifest changes, run `pnpm install` or `uv lock` as
appropriate and include the matching lockfile update.

## Workspace ownership

| Path                       | Responsibility                                                               |
| -------------------------- | ---------------------------------------------------------------------------- |
| `apps/site`                | Astro public site, catalog browser, search, LLM pages, and Open Graph images |
| `apps/docs`                | Next.js and Fumadocs product documentation                                   |
| `packages/brand`           | Reviewed assets, font imports, and CSS tokens                                |
| `packages/catalog`         | Browser-safe catalog loading, release validation, and catalog models         |
| `packages/chartcoach`      | Python API, CLI, MCP server, runtime index access, and curation              |
| `fixtures/catalog-release` | Wire fixture shared by readers, tests, and the site build                    |

The root `package.json` and `vite.config.ts` own JavaScript orchestration and
shared policy. Each package manifest owns its dependencies, focused scripts,
tests, and build configuration. The root `pyproject.toml` defines a virtual uv
workspace. Publishable Python metadata lives in
`packages/chartcoach/pyproject.toml`.

## Dependency direction

The web package graph is:

```text
apps/site  -> packages/catalog
          -> packages/brand

apps/docs  -> packages/brand
```

`packages/catalog` is a browser-safe leaf. Keep it independent from the apps,
brand assets, and Node built-ins. Vite+ enforces this boundary.

Use package names for cross-package TypeScript imports. Keep app
implementations private to their app. Add shared behavior to a package when it
has a stable contract and more than one real consumer.

## Python boundaries

`open_catalog(source)` and `open_index(source, profile=...)` are the public
read paths. Sources are local paths, `file://` URIs, or HTTP and HTTPS
descriptor URLs. Capability extras add cloud sources, native indexes, MCP, and
curation.

`catalog/runtime.py` owns source resolution, downloads, integrity checks,
caching, and safe extraction. Runtime modules may import release models.
Curation modules own building, validation, publication, and selection. Keep
runtime imports independent from curation.

Package publication and catalog promotion have separate identities and
workflows. Package tags publish PyPI and npm artifacts. Catalog promotion
selects an already published immutable catalog release.

## Core invariants

- Keep one catalog wire shape across Python, JavaScript, the shared fixture,
  and both web apps.
- Treat catalog schemas, release records, public APIs, CLI output, and site
  copy as user-facing contracts.
- Keep digest-addressed catalog releases immutable.
- Route every `catalog.json` selection write through the curation selection
  service.
- Keep the base Python package compatible with Pyodide.
- Keep optional integrations behind capability extras.
- Use the shared release fixture for contract tests and local static builds.
  Catalog deployment supplies the exact remote release URL.

Update both readers and the fixture when the catalog row or release envelope
changes. Test through the nearest public API, command, generated artifact, or
runtime boundary.

## Generated paths

Build tools own these paths:

- `apps/docs/.next/`
- `apps/docs/.source/`
- `apps/docs/out/`
- `apps/site/.astro/`
- `apps/site/dist/`
- `packages/catalog/dist/`
- `dist/`

Change source files and run the owning build. Update `pnpm-lock.yaml` and
`uv.lock` through their package managers.

## Development contracts

- [Architecture and ownership](development_docs/architecture.md)
- [Development workflow](development_docs/development.md)
- [Releases and catalog data](development_docs/releases-and-data.md)
