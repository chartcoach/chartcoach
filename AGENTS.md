# ChartCoach Agent Guide

ChartCoach is a guideline catalog, public site, shared UI, and VisGround tooling
monorepo. Use `pnpm` for JavaScript and `uv` for Python.

## Responsibility

Treat the catalog, public APIs, notebooks, and docs as user-facing surfaces.
Prefer small, typed, source-backed changes over broad helpers or silent
fallbacks. If a current caller does not need an alias or shim, remove it.
Before changing a module, read its nearest README, package manifest, and tests.

## Repository Map

- `apps/site`: Astro/Starlight docs site and guideline browser.
- `apps/visground`: internal Python workbench, anywidget frontend, datasets, evaluations.
- `apps/visground-web`: standalone Vite host for a VisGround parquet export.
- `packages/catalog-javascript`: JS loaders, parsers, and catalog wire types.
- `packages/catalog-python`: Python catalog package and `chartcoach` CLI.
- `packages/ui`: shared React primitives, design tokens, brand assets.
- `packages/visground-viewer`: reusable React viewer and anywidget bridge.
- `packages/examples/*`: marimo notebooks for cataloging, analysis, application.

## Invariants

- Catalog entries are source data. Do not invent alternate record shapes in UI,
  loaders, notebooks, or evaluation code.
- Wire-shape changes must update the Python reader, JavaScript reader, docs, and
  examples that consume the shape.
- VisGround exports must keep the Python exporter, anywidget bridge, reusable
  viewer, and web host aligned.
- Generated VisGround outputs are cache-local by default. Do not reintroduce
  bulky generated artifacts under `apps/visground/data/artifacts`.
- Public copy should be terse and concrete. Say what the reader can inspect,
  run, or compare; avoid stock rationale and generic filler.
- Dependency changes must include the matching lockfile changes.
- `packages/catalog-python` is the only Python package intended for PyPI.
  `apps/visground` and `packages/examples/*` are uv projects, not distributions.

## Commands

- Site: `pnpm --dir apps/site lint` and `pnpm --dir apps/site build`.
- Viewer: `pnpm --dir packages/visground-viewer test`.
- Web host: `pnpm --dir apps/visground-web build`.
- VisGround workbench: `pnpm --dir apps/visground test`.
- JS packages: `pnpm --dir <package> lint`, `pnpm --dir <package> typecheck`,
  and the local build or test script.
- Python packages: `uv run ruff check .`, `uv run ty check .`, and targeted
  pytest commands such as `uv run pytest apps/visground/tests`.
- Cross-workspace: `pnpm lint`, `pnpm typecheck`, `pnpm build`, `pnpm test`.
