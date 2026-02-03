# Retrieval Docs (ChartCoach)

This folder documents how ChartCoach runs retrieval strategies and produces eval artifacts that are consumed by `apps/eval-ui`.

Quick links:
- Artifact schema: `docs/artifacts/schema-v1.json` (generated from Python pydantic models)
- Paper run manifest example: `docs/manifests/paper-freeze-v20.yaml`
- How to add a strategy: `docs/retrieval/ADDING_STRATEGY.md`

## Key Concepts

- **Situation contract**: Retrieval consumes a structured request (chart + intent + typed context facets like audience/medium/constraints). Strategies must not depend on `evals/scenarios/**`.
- **Run config**: `packages/chartcoach-py/src/chartcoach/retrieval/config.py` defines a typed `RetrievalRunConfig` (defaults + optional env + optional YAML).
- **Strategy runtime**: Strategies receive a `StrategyRuntime` instance (shared indices + LMs + caches) to avoid module-level global state.
- **Eval artifacts**: `chartcoach-retrieval run` writes:
  - `index.json` (scenario list + strategy list + run metadata)
  - `bundles/<scenarioId>.json` (per-scenario strategy outputs + evidence snippets)

## Common Commands

Run a paper-style frozen experiment (manifest defines strategy list + config; store url can be overridden):

```bash
chartcoach-retrieval run \
  --manifest docs/manifests/paper-freeze-v20.yaml \
  --artifacts-url file:///tmp/chartcoach-artifacts/v1/ \
  --purge
```

Run ad-hoc (non-manifest) with env/YAML config:

```bash
chartcoach-retrieval run \
  --scenarios evals/scenarios/spec.yaml \
  --catalog-uri guidelines/catalog.parquet \
  --artifacts-url file:///tmp/chartcoach-artifacts/v1/ \
  -k 16
```

Validate drift checks:

```bash
uv run pytest
pnpm test:eval
```

