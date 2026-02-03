# Paper Assets (Strategy Matrix, Tables, Figures)

This repo keeps **paper-facing analysis** separate from retrieval strategy implementations:

- Strategies must be scenario-agnostic and must not encode benchmark-coupled heuristics.
- Paper/report tooling is allowed to reference strategy IDs and artifact versions, because it is
  *analysis over outputs*, not algorithm logic.

## Controlled Comparison Set (Main Table)

For the main paper narrative, prefer a small set of **representatives** (families), then use
targeted ablations:

- Dense: `ann-dense@v1`
- Lexical: `bm25-prf@v1`
- Hybrid baseline: `hybrid-rrf@v1`
- Sparse baseline: `sparse-splade@v1`
- Dense+sparse: `dense-sparse-rrf@v1`
- Structure-aware: `multirepr-rrf@v1` (and optionally `role-aware-sections@v1`)
- Best LLM query modeling: `facet-fusion-hybrid@v1` (and/or `hyde-hybrid@v1`)
- Set selection: `hybrid-rrf-setselect-facility@v1` (and/or label coverage)
- Agentic upper-bound: `agentic-hybrid@v1`

Everything else is "supplementary" unless it answers a specific research question.

Manifest examples:
- Main: `docs/manifests/paper-main-v20.yaml`
- Ablation (no vision): `docs/manifests/paper-ablation-no-vision-v20.yaml`
- Ablation (focus=all): `docs/manifests/paper-ablation-focus-all-v20.yaml`

## Taxonomy Source of Truth

Paper scripts use a lightweight taxonomy file:

- `docs/retrieval/strategy_taxonomy.yaml`

This is intentionally **not** used by strategy code.

## Generating Tables/Figures

The retrieval CLI includes analysis commands (`analyze-stability`, `analyze-counterfactual`,
`analyze-pool`, `analyze-negatives`). Paper asset generation wraps these and emits
reproducible, merge-friendly outputs (CSV + Markdown):

```bash
uv run chartcoach-retrieval paper-assets \
  --run nogit/eval-artifacts/v18 \
  --run nogit/eval-artifacts/v19 \
  --out nogit/strat-eval/paper-assets \
  --taxonomy docs/retrieval/strategy_taxonomy.yaml
```

Optional: render plots (PNG). Install the optional deps group and pass `--plots`:

```bash
uv sync --group paper
uv run chartcoach-retrieval paper-assets \
  --run nogit/eval-artifacts/v18 \
  --run nogit/eval-artifacts/v19 \
  --out nogit/strat-eval/paper-assets \
  --plots
```
