# Eval Artifacts

ChartCoach produces eval artifacts that are loaded by `apps/eval-ui` and used for human ratings.

## Artifact Files

An artifacts root contains:

- `index.json`
  - scenario list (inputs)
  - strategy list (what was run)
  - run-level metadata (`meta.config`, `meta.catalog_digest`, etc.)
- `bundles/<scenarioId>.json`
  - per-scenario results for each strategy
  - evidence snippets (when available) per returned guideline

## Schema Source of Truth

The canonical schema lives in Python pydantic models under:

- `packages/chartcoach-py/src/chartcoach/retrieval/service/eval_artifacts_schema.py`

The generated JSON Schema is committed at:

- `docs/artifacts/schema-v1.json`

To regenerate the JSON Schema:

```bash
uv run python -m chartcoach.retrieval.service.artifact_schema --out docs/artifacts/schema-v1.json
```

Drift checks:

- Python tests assert `docs/artifacts/schema-v1.json` matches the generated pydantic schema.
- Python tests validate the eval-ui fixture artifacts against the pydantic models.
- Eval-ui tests parse the fixture artifacts using the server-side zod schemas.

## Evidence Snippets

Each returned guideline may include an `evidence` array with short snippets indicating what text drove retrieval (role + snippet text + optional score).

These are intended for:

- more reliable human evaluation (raters see why something was retrieved),
- downstream grounding (feedback systems can cite specific guideline sections).

