# chartcoach Agent Guide

chartcoach is a visualization design guideline catalog monorepo with public web apps, Python and
JavaScript readers, a CLI, and catalog curation tools.

## Responsibility

- Treat catalog schemas, release records, public APIs, CLI output, and site copy
  as user-facing contracts.
- Keep one catalog wire shape across Python, JavaScript, fixtures, and web apps.
- Keep the base Python package compatible with Pyodide. Put LanceDB, Obstore,
  UMAP, MCP, and other native or service integrations behind package extras.
- Route curation storage through Obspec protocols and Obstore implementations.
- Preserve immutable digest-addressed releases and the single `catalog.json`
  selection record.
- Prefer direct changes over aliases, compatibility layers, generated models,
  and speculative abstractions.
- Read the nearest README, package manifest, and behavior tests before editing a
  package.

## Ownership

- `apps/site`: Astro public site, Guideline Catalog browser, and site build integrations.
- `apps/docs`: Next.js and Fumadocs product documentation.
- `packages/brand`: reviewed web assets, font imports, and CSS tokens.
- `packages/catalog`: browser-safe release and catalog readers.
- `packages/chartcoach`: Python API, CLI, MCP server, and curation code.
- `fixtures/catalog-release`: release contract shared by readers and the site.

## Commands

Install both workspaces from the repository root:

```sh
pnpm install
uv sync --locked --package chartcoach --all-groups --all-extras
```

Run the complete JavaScript and web gate from the repository root:

```sh
pnpm ready
```

Use the Make gates for Python changes:

```sh
make format lint typecheck test build
```

`pnpm dev` starts both web apps. Package-native commands remain available for a
focused build, test, typecheck, or dev server.

## Change Rules

- Update both readers and the shared fixture when the catalog wire shape changes.
- Update lockfiles with dependency changes.
- Keep shared web assets and styles in `packages/brand` and import them through
  package exports.
- Validate through the boundary changed by the patch. Run `pnpm ready` for a
  cross-workspace JavaScript change and all Python Make gates for a Python
  package change.
- Report any skipped gate with its command, failure, and remaining risk.

## Development Contracts

- [Architecture and ownership](development_docs/architecture.md)
- [Development workflow](development_docs/development.md)
- [Releases and catalog data](development_docs/releases-and-data.md)
