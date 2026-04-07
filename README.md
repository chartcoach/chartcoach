# ChartCoach

Monorepo for the guideline catalog, docs, shared UI, and VisGround tooling.

## Modules

- `apps/site` — Astro/Starlight docs site and guideline browser.
- `apps/visground` — Python + anywidget tooling for building VisGround datasets, running evaluations, and exporting viewer artifacts.
- `apps/visground-web` — Standalone web host for the VisGround viewer.
- `packages/catalog-javascript` — JavaScript loaders, parsers, and wire types for the guideline catalog.
- `packages/catalog-python` — Python catalog library and CLI.
- `packages/ui` — Shared React UI primitives, design tokens, and brand assets.
- `packages/visground-viewer` — Reusable React viewer for VisGround parquet artifacts.
- `packages/examples/guideline-analysis-example` — Notebook example for structural analysis over the catalog.
- `packages/examples/guideline-application-example` — Notebook example for grounded visualization feedback.
- `packages/examples/guideline-cataloging-example` — Notebook example for turning source material into catalog entries.
