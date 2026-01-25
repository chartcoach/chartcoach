# Design: Eval UI ↔ Retrieval Server Integration (2026-01-25)

## Goal
Replace `apps/eval-ui` dummy retrieval plumbing with real calls to the ChartCoach retrieval server:
- `GET /v1/strategies` to enumerate available retrieval strategies
- `POST /v1/strategies/{strategy_id}` to run a strategy for a given scenario

Add eval-ui–side caching so repeated runs reuse prior results (persisted to S3 when configured) and allow easy cache invalidation/deletion.

## Non-goals
- Redesign the eval UI itself (tabs/cards/rating UX stays as-is).
- Add new retrieval strategies (only wire what the server reports).
- Add chart downloading/proxying in eval-ui (the retrieval server is responsible for reading chart URIs and catalog URIs it is given).

## Python Retrieval Server API

### Strategy listing
Keep:
- `GET /v1/strategies -> list[StrategyInfo]`

The server is configured with a set of **strategy factories** (no pre-instantiated strategies). The listing endpoint uses `RetrievalStrategy.info()` from the class to avoid boilerplate.

### Strategy execution
Change `POST /v1/strategies/{strategy_id}` request body to include:
- `catalog_uri`: string (supports local path, `file://`, `http(s)://`, and `s3://`)
- `request`: `RetrievalRequest` (existing shared Pydantic model)

On each request:
1. Load the `Catalog` from `catalog_uri` (parquet expected for non-folder URIs).
2. Instantiate the requested strategy using its factory: `factory(catalog=Catalog)`.
3. Run the strategy with the provided `RetrievalRequest`.

Optional server-side caching: cache loaded catalogs by `catalog_uri` in-memory (small LRU) to avoid re-reading parquet repeatedly.

## Eval UI Integration

### TS client (server-side)
Create a lean `apps/eval-ui` TypeScript client that:
- Calls `GET {baseUrl}/v1/strategies`
- Calls `POST {baseUrl}/v1/strategies/{id}` with `{ catalog_uri, request }`

`baseUrl` is configured via server env (defaults to `http://127.0.0.1:8000`).

### Scenario → RetrievalRequest mapping
Build a `RetrievalRequest` from a scenario spec:
- `ImageItem` for `scenario.chart` (`uri`, `mime`)
- `TextItem` role `situation` from `scenario.designer_intent`
- `TextItem` role `chart_spec` default `"{}"`
- (Optional) include `TextItem` role `query` from `scenario.query` for future strategies

### Result mapping
The retrieval server returns `RetrievalResponse.catalog` as serialized `CatalogEntry[]`.
Eval UI maps those entries into `@chartcoach/catalog`-compatible `CatalogEntry` values by re-indexing sections from `guideline.body` (same logic as parquet loader).

### Caching and S3 persistence
Eval UI caches per `(scenarioId, strategyId, catalogUri, requestDigest)`:
1. In-memory cache (fast, per process) to avoid duplicate work within a single dev session.
2. S3 cache (persistent) when S3 env is configured.

S3 key layout:
`{S3_PREFIX?}retrieval-results/{cacheVersion}/{scenarioId}/{strategyId}/{digest}.json`

Cache invalidation:
- Bump `cacheVersion` (env) to invalidate without deleting old objects.
- Provide a server function to delete cached objects by prefix (optional, for true “destroy cache”).

### Parallel strategy execution
When building a scenario bundle:
- Fetch `GET /v1/strategies`
- Run each strategy in parallel with a configurable concurrency limit.
- Use cached results whenever present; only run the retrieval server when missing.

## Testing plan
- Python: unit tests for `catalog_from_uri` (local + `file://` + a local `http://` server) and for the new `POST` request model wiring.
- Eval UI: vitest tests for:
  - TS client request/response parsing (mock `fetch`)
  - Cache keying + “cache hit avoids network” behavior (mock AWS SDK + fetch)
- End-to-end smoke:
  - Start retrieval server + eval UI, open a scenario, verify strategies populate and guidelines render.

