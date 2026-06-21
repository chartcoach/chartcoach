# chartcoach Agent Guide

chartcoach is a guideline catalog, public site, docs site, and catalog-loader
monorepo. Use `pnpm` for JavaScript and `uv` for Python.

## Responsibility

Treat the catalog, public APIs, site, and docs as user-facing contracts.
Prefer small, typed, source-backed changes over broad helpers or silent
fallbacks. If a current caller does not need an alias or shim, remove it.
Before changing a module, read its nearest README, package manifest, and tests.

## Repository Map

- `apps/site`: Astro and MDX marketing site with the Guideline Catalog browser.
- `apps/docs`: Astro/Starlight technical docs site.
- `packages/brand`: shared web identity package with canonical brand assets,
  Poppins imports, CSS tokens, generated PNGs, and public asset sync checks for
  `apps/site` and `apps/docs`.
- `packages/catalog-javascript`: JS loaders, parsers, and catalog wire types.
- `packages/catalog-python`: Python catalog package and `chartcoach` CLI.

## Invariants

- Catalog entries are source data. Do not invent alternate record shapes in UI,
  loaders, or site code.
- Wire-shape changes must update the Python reader, JavaScript reader, docs, and
  site code that consumes the shape.
- Public copy should be terse and concrete. Say what the reader can inspect,
  run, or compare. Avoid stock rationale and vague filler.
- Dependency changes must include the matching lockfile changes.
- `packages/catalog-python` is the only Python package intended for PyPI.

## Commands

- Site: `pnpm --dir apps/site lint` and `pnpm --dir apps/site build`.
- Brand assets: `pnpm brand:sync` after changing canonical assets, then
  `pnpm brand:check`.
- JS packages: `pnpm --dir <package> lint`, `pnpm --dir <package> typecheck`,
  and the local build or test script.
- Python packages: `uv run ruff check .`, `uv run ty check .`,
  `uv run pyrefly check`, and targeted pytest commands such as
  `uv run pytest packages/catalog-python/tests`.
- Cross-workspace: `pnpm lint`, `pnpm typecheck`, `pnpm build`, `pnpm test`.
