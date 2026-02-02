# chartcoach (Python)

Python library for working with the ChartCoach guideline catalog, plus SOTA retrieval tooling (LanceDB + DSPy) and eval-artifact generation.

## Quickstart (monorepo)

From the repo root:

```bash
uv sync --all-packages --all-groups
```

## Retrieval strategies (SOTA suite)

Strategies live in `packages/chartcoach-py/src/chartcoach/retrieval/strategy/pipelines/` and are backed by a hybrid-capable index (dense + FTS + hybrid).

- `bm25-prf@v1` (`Bm25PrfStrategy`): FTS/BM25 with pseudo-relevance feedback (PRF) query expansion.
- `dense-mmr@v1` (`DenseMmrStrategy`): dense bi-encoder retrieval with guideline-level aggregation + MMR for diversity.
- `hybrid-rrf@v1` (`HybridRrfStrategy`): hybrid dense+lexical retrieval with RRF fusion.
- `query-fusion-hybrid@v1` (`QueryFusionHybridStrategy`): DSPy multi-query generation + hybrid retrieval + RRF fusion + optional cross-encoder rerank.
- `hyde-hybrid@v1` (`HydeHybridStrategy`): DSPy HyDE pseudo-document + lexical/dense fusion + optional cross-encoder rerank.
- `agentic-hybrid@v1` (`AgenticHybridStrategy`): DSPy ReAct agent using hybrid/dense/FTS tools + full guideline reads, with robust fallback fill-to-k.

## Generate eval artifacts (for eval-ui)

This writes `index.json` and `bundles/{scenarioId}.json` suitable for `apps/eval-ui`.

```bash
mkdir -p nogit/eval-artifacts/v1

uv run --env-file .env chartcoach-retrieval run \
  --scenarios evals/scenarios/spec.yaml \
  --catalog-uri guidelines/catalog.parquet \
  --artifacts-url "file://$PWD/nogit/eval-artifacts/v1/" \
  --purge \
  -k 10
```

Then point eval-ui at the generated folder:

```bash
EVAL_ARTIFACTS_URL="file://$PWD/nogit/eval-artifacts/v1/" pnpm dev:eval
```

## Configuration knobs (advanced)

### LLM (DSPy strategies)

All DSPy-backed strategies read OpenAI-compatible settings from `.env`:

- `OPENAI_BASE_URL`
- `OPENAI_API_KEY`

Optional strategy controls:

- `CHARTCOACH_STRATEGY_LM_MODEL` (default: `gpt-5.1`)
- `CHARTCOACH_LM_TIMEOUT_SECONDS` (default: `120`)
- `CHARTCOACH_LM_NUM_RETRIES` (default: `6`)

Vision (optional request enrichment):

- `CHARTCOACH_CHART_VISION_ENABLED` (default: `false`)
- `CHARTCOACH_STRATEGY_VLM_MODEL` (default: `gpt-5.2`)
- `CHARTCOACH_VLM_TIMEOUT_SECONDS` (default: `CHARTCOACH_LM_TIMEOUT_SECONDS`)
- `CHARTCOACH_VLM_NUM_RETRIES` (default: `CHARTCOACH_LM_NUM_RETRIES`)
- `CHARTCOACH_CHART_VISION_MAX_TEXT_CHARS` (default: `1400`)

Violation-aware post-filtering (optional):

- `CHARTCOACH_GUIDELINE_STATUS_MODE` = `all|violations|satisfied` (default: `all`)
- `CHARTCOACH_GUIDELINE_STATUS_CANDIDATE_MULTIPLIER` (default: `4`)
- `CHARTCOACH_GUIDELINE_STATUS_KEEP_UNCLEAR` (default: `true`)

### Embeddings / indexing

- `CHARTCOACH_EMBEDDING_MODEL` (default: `BAAI/bge-small-en-v1.5`)
- `CHARTCOACH_EMBEDDING_PROJECTOR` (`sentence_transformers` or `litellm`; default: `sentence_transformers`)

Query-fusion tuning:

- `CHARTCOACH_FUSION_N_QUERIES` (default: `4`)
- `CHARTCOACH_FUSION_RRF_K` (default: `60`)
- `CHARTCOACH_FUSION_CROSS_ENCODER_MODEL` (default: `cross-encoder/ms-marco-TinyBERT-L-6`)
- `CHARTCOACH_FUSION_XENC_CANDIDATES` (default: `80`)
