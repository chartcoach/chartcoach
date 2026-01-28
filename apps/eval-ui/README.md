# @chartcoach/eval-ui (Guideline Relevance Eval)

TanStack Start app for human relevance rating of retrieved visualization guidelines.

## What it does

- Loads **precomputed eval artifacts** (scenarios + per-strategy guideline bundles) from an artifacts root:
  - `file://...` (local folder)
  - `https://...` (hosted JSON)
  - `s3://...` (S3 / S3-compatible)
- Shows each scenario’s chart + query + designer intent
- Shows per-strategy guideline sets from the artifact bundles
- Persists Likert (1-5) relevance ratings locally in the browser via RxDB (localStorage)
- Allows syncing ratings to S3 and pulling the latest export from S3 (device-scoped; optional)

## Run

```bash
# from the monorepo root
pnpm install
pnpm dev:eval

# or, from apps/eval-ui
pnpm dev
```

### Env vars

For local dev, you can define env vars in the repo-root `.env` (see `.env.example`).
In CI/Docker, prefer passing env vars via the environment (don’t bake a `.env` into images).

### Artifacts configuration

By default (no env vars), eval-ui reads **fixture artifacts** shipped in-repo so `pnpm dev:eval` works without S3.

To point eval-ui at your own artifacts, set `EVAL_ARTIFACTS_URL` (directory root containing `index.json` and `bundles/*.json`):

```bash
# local folder
EVAL_ARTIFACTS_URL="file:///absolute/path/to/eval-artifacts/v1/" pnpm dev:eval

# hosted JSON
EVAL_ARTIFACTS_URL="https://example.com/eval-artifacts/v1/" pnpm dev:eval

# S3 (requires S3_* env vars for credentials/endpoint)
EVAL_ARTIFACTS_URL="s3://my-bucket/some/prefix/eval-artifacts/v1/" pnpm dev:eval
```

To generate artifacts locally (writes `index.json` + `bundles/{scenarioId}.json`):

```bash
uv run chartcoach-retrieval run \
  --scenarios evals/scenarios/spec.yaml \
  --catalog-uri guidelines/catalog.parquet \
  --artifacts-url "file://$PWD/nogit/eval-artifacts/v1/"

EVAL_ARTIFACTS_URL="file://$PWD/nogit/eval-artifacts/v1/" pnpm dev:eval
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

## Devtools

TanStack devtools are enabled in development builds only. They are not loaded in production builds.
