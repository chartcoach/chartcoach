# @chartcoach/eval-ui (Guideline Relevance Eval)

TanStack Start app for human relevance rating of retrieved visualization guidelines.

## What it does
- Loads scenarios from `evals/scenarios/spec.yaml`
- Loads guideline catalog entries from `guidelines/catalog.parquet` via `@chartcoach/catalog`
- Shows each scenario’s chart + query + designer intent
- Shows per-strategy guideline sets (retrieval backends are out of scope; current strategies are dummy)
- Persists Likert (1–5) relevance ratings locally in the browser via TanStack DB (localStorage)
- Supports offline use by caching scenarios + scenario bundles in localStorage
- Allows exporting saved ratings for downstream evaluation pipelines

## Run

```bash
# from the monorepo root
pnpm install
pnpm dev:eval

# or, from apps/eval-ui
pnpm dev
```

## Build

```bash
# from the monorepo root
pnpm build:eval

# or, from apps/eval-ui
pnpm build
```

## QA

```bash
# from the monorepo root
pnpm lint:js
pnpm test:eval
```

## Storage

### Ratings
Ratings are stored in localStorage under `chartcoach/eval-ui/relevance-ratings/v1`.
Use the “Clear ratings” button in the header to reset.

### Offline cache
Scenarios and scenario bundles are cached under:
- `chartcoach/eval-ui/cache/scenarios/v1`
- `chartcoach/eval-ui/cache/scenario-bundle/v1:{scenarioId}`

## Devtools
TanStack devtools are enabled in development builds only. They are not loaded in production builds.
