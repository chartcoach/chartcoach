# ChartCoach

Monorepo for the guideline catalog, docs, shared UI, and VisGround tooling.

## Modules

- `apps/site` - Astro/Starlight docs site and guideline browser.
- `apps/visground` - Python package and anywidget frontend for building VisGround datasets, running evaluations, and exporting viewer artifacts.
- `apps/visground-web` - Standalone Vite host for the VisGround viewer.
- `packages/catalog-javascript` - JavaScript loaders, parsers, and wire types for the guideline catalog.
- `packages/catalog-python` - Python catalog package and `chartcoach` CLI.
- `packages/ui` - Shared React UI primitives, design tokens, and brand assets.
- `packages/visground-viewer` - Reusable React viewer for VisGround parquet exports and anywidget bridges.
- `packages/examples/*` - marimo notebooks for cataloging, analysis, and guideline application.

## Source Boundaries

- Treat catalog entries as data. Keep loaders, UI rendering, and evaluation code from inventing alternate record shapes.
- Keep public site copy short and concrete. Avoid filler about why something "matters"; say what the user can inspect or do.
- When changing a wire type, update both the Python and JavaScript readers that consume it.
- When changing generated or exported VisGround artifacts, keep the viewer, anywidget bridge, and standalone web host aligned.
- Prefer existing package-local helpers before adding new shared utilities.
- Do not keep obsolete aliases or fallback paths unless a current package imports them.

## Checks

- Site changes: `pnpm --dir apps/site lint` and `pnpm --dir apps/site build`.
- Viewer changes: `pnpm --dir packages/visground-viewer test`.
- Web host changes: `pnpm --dir apps/visground-web build`.
- JavaScript package changes: `pnpm --dir <package> lint`, `pnpm --dir <package> typecheck`, and the package build or test script.
- Python package changes: `uv run pytest apps/visground/tests` when those tests cover the touched surface.
- Cross-workspace changes: `pnpm lint`, `pnpm typecheck`, `pnpm build`, and `pnpm test`.
