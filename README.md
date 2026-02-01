# ChartCoach

Visualization guideline catalog + tooling for browsing, retrieval, and human evaluation.

## Repo layout

- `guidelines/`: guideline entries (Markdown + metadata) and `catalog.parquet`
- `apps/site/`: Astro/Starlight guideline browser
- `apps/eval-ui/`: TanStack Start app for rating retrieved guidelines per scenario (bucket + optional utility dimensions)
- `evals/`: evaluation scenarios (`evals/scenarios/spec.yaml`)
- `packages/chartcoach-js/` (`@chartcoach/catalog`): JS catalog loaders/utilities
- `packages/chartcoach-ui/`: shared UI components/styles
- `packages/chartcoach-py/`: Python library for working with the catalog
- `packages/examples/`: Python example workflows (cataloging/analysis/application)

## Environment variables

- Copy `.env.example` to `.env` (repo root) and fill in values.
- `apps/site` + `apps/eval-ui` load the repo-root `.env` automatically in dev/build.
- For Python, run from the repo root with `uv run --env-file .env ...`.

## Web apps (pnpm)

```bash
pnpm install
pnpm dev:site   # http://localhost:4321
pnpm dev:eval   # http://localhost:3000
```

```bash
pnpm build:site
pnpm build:eval
pnpm lint:js
pnpm test:eval
```

## Python (uv)

```bash
uv sync --all-packages --all-groups
uv run pytest
```

## Docker

```bash
docker build -f apps/eval-ui/Dockerfile -t chartcoach-eval-ui .
docker build -f apps/site/Dockerfile --build-arg SITE_URL="https://example.com" -t chartcoach-site .
```

See `apps/site/README.md` and `apps/eval-ui/README.md` for app-specific details.
