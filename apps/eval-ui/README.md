# @chartcoach/eval-ui (Guideline Relevance Eval)

TanStack Start app for human relevance rating of retrieved visualization guidelines.

## What it does

- Loads scenarios from `evals/scenarios/spec.yaml`
- Loads guideline catalog entries from `guidelines/catalog.parquet` via `@chartcoach/catalog`
- Shows each scenario’s chart + query + designer intent
- Shows per-strategy guideline sets (retrieval backends are out of scope; current strategies are dummy)
- Persists Likert (1-5) relevance ratings locally in the browser via TanStack DB (localStorage)
- Supports offline use by caching scenarios + scenario bundles locally (RxDB)
- Allows syncing ratings to S3 and pulling the latest export from S3 (device-scoped)

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

## Docker (Self-host)

Build from the monorepo root (important for pnpm workspaces):

```bash
docker build -f apps/eval-ui/Dockerfile -t chartcoach-eval-ui .
```

Run:

```bash
docker run --rm -p 3000:3000 \
  -e NITRO_HOST=0.0.0.0 -e NITRO_PORT=3000 \
  -e S3_REGION=us-east-1 \
  -e S3_ACCESS_KEY_ID=... -e S3_SECRET_ACCESS_KEY=... \
  -e S3_BUCKET=... \
  -e S3_ENDPOINT=https://... \
  -e S3_PREFIX=chartcoach \
  -e S3_FORCE_PATH_STYLE=false \
  chartcoach-eval-ui
```

If `S3_*` variables are not set, automatic rating uploads are disabled (local persistence still works).

## Storage

### Ratings

Ratings are stored locally via RxDB (localStorage) under the database name `chartcoach-eval-ui` (keys managed by RxDB).
Use the “Clear ratings” button in the header to reset. Older builds used `chartcoach/eval-ui/relevance-ratings/v1` and will migrate once.

## Guideline Links

Set `VITE_GUIDELINE_DETAIL_URL_TEMPLATE` to link each guideline card to your guideline browser.
Use `{id}` as the placeholder, e.g. `https://example.com/guidelines/{id}`.

In development, if unset, eval-ui uses `http://localhost:4321/guidelines/{id}/` (Astro default dev URL).

### Offline cache

Scenarios and scenario bundles are cached under:

- `chartcoach/eval-ui/cache/scenarios/v1`
- `chartcoach/eval-ui/cache/scenario-bundle/v1:{scenarioId}`

## Devtools

TanStack devtools are enabled in development builds only. They are not loaded in production builds.
