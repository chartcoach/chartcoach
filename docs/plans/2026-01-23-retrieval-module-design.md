# Retrieval Module Design (Draft)

## Goal
Define a small, stable API for guideline retrieval that makes it easy to experiment with multiple strategies (semantic, lexical, hybrid, rules-based), driven by the scenario schema in `evals/scenarios/spec.yaml`.

## Inputs (from `evals/scenarios/spec.yaml`)
- `query`: user request (text)
- `designer_intent`: context/intent (text)
- `lang`: language code
- `chart`: optional artifact (uri, mime, bytes)

## Design Constraint: Mixed Context Without Overengineering
We want to support realistic contexts (chart + dataset + notes + constraints) without introducing a heavy “pipeline framework”.

### Option A (recommended): Typed `ContextItem` union
Model request context as a list of small, typed items (text/image/table/file). Strategies can ignore items they don’t support. This keeps the core API stable while still allowing richer inputs.

### Option B: Unstructured `context: dict[str, Any]`
Very flexible but quickly becomes unclear and hard to type-check. Fine for prototyping, but tends to metastasize into ad-hoc conventions.

### Option C: Mandatory analyzer pipeline
Powerful, but likely overkill right now. Better as an optional layer that produces additional `TextContextItem`s (captions, dataset summaries, inferred labels) for strategies to consume.

## DSPy Integration (strategies as `dspy.Module`)
If you want to minimize bespoke “retrieval framework” boilerplate and benefit from
DSPy’s tracing + LLM utilities, the simplest path is:

### Recommendation: DSPy-first strategies, minimal shared types
- Every strategy is a `dspy.Module` with `forward(request) -> RetrievalResult`.
- Deterministic strategies are still fine as modules (they just don’t call LLMs).
- We still define a small, stable set of Pydantic/dataclass models for:
  - `RetrievalRequest` (incl. mixed `ContextItem`s)
  - `RetrievalResult` (hits + evidence + traces)

This keeps the shared “contract” tiny while avoiding a custom plugin system or
tracing implementation.

### Dependency note
If you want to keep the core library lightweight, make DSPy an optional extra
(e.g., `chartcoach[retrieval]`). If the project is DSPy-first end-to-end, you
can make it a core dependency and simplify packaging.

## Open Decisions
1. Should chart artifacts be first-class in the core retrieval request type, or handled by upstream analyzers that produce text/labels?
2. What should the core retrieval output contain (IDs only vs IDs + matched sections + debug rationale)?

## Decision: Output Shape = C (IDs + Evidence + Debug)
For evaluation and iteration, retrieval must return:
- the ranked guideline IDs (+ aggregate score)
- evidence describing what matched (section role + snippet + match score)
- structured debug traces per strategy (inputs used, intermediate candidates, filters, timings)

## Proposed Public API (high level)
- `RetrievalRequest` (dataclass): query, lang, context items, constraints (k, roles, label filters)
- `RetrievalHit` (dataclass): guideline_id, score, evidence[], guideline preview fields, debug summary
- `RetrievalResult` (dataclass): hits[], traces[]
- `RetrievalStrategy` (Protocol): `retrieve(request, resources) -> RetrievalResult` (or `hits, trace`)
- `Retriever` (class): runs one strategy or composes multiple strategies (fusion) and merges traces

### Suggested Minimal Type Set
- `ContextItem` union (text/image/table/file) with `kind` + `role`
- `RetrievalConstraints`: `k`, `roles`, `labels_any`, `labels_all`
- `Evidence`: `{guideline_id, role, snippet, score, source}` where `source` can reference catalog text units (`{id, role}`)
- `StrategyTrace`: `{strategy, used_context_roles, params, timings_ms, notes, artifacts}`

## Composability Model (strategies as building blocks)
To keep it simple, composition can just be *modules calling other modules* (no
separate abstraction layer). Provide a few tiny “combinator modules”:

### Sequential composition (narrowing / staging)
`Chain([s1, s2, ...])` (a `dspy.Module`)
- Runs `s1` to produce an initial ranking.
- Passes a *constraint* forward (e.g., `allowed_ids = top_m(s1)`), then runs `s2` within that candidate set.
- Returns the final stage hits (or an explicit fusion of stages), while retaining all stage traces.

This supports patterns like: `LabelFilter -> SemanticSections -> Rerank`.

### Parallel composition (fusion)
`FuseRRF([s1, s2, ...])` (a `dspy.Module`)
- Runs all strategies independently on the same request/resources.
- Combines ranked lists using reciprocal-rank fusion (or another simple fusion function).
- Merges traces; evidence is unioned and trimmed per-hit.

This supports: `SemanticSections ⊕ LexicalBM25 ⊕ LabelHeuristics`.

### Adapters
`WithConstraints(base, ...)` sets default `k/roles/labels` (handy for eval reproducibility).
`AugmentContext(augmenter, base)` appends derived `TextItem`s (e.g., dataset summary) to `request.context` before calling `base`.

## Request/Context Sketch (Option A)
```python
# Pseudocode: shape, not final names
TextItem   = { kind: "text",   role: "query"|"intent"|"note"|..., text: str, lang?: str }
ImageItem  = { kind: "image",  role: "chart"|"reference", uri?: str, mime?: str, bytes?: bytes }
TableItem  = { kind: "table",  role: "dataset", df?: pl.DataFrame, uri?: str, mime?: str }
FileItem   = { kind: "file",   role: "attachment", path?: Path, uri?: str, mime?: str, bytes?: bytes }

RetrievalRequest = {
  request_id: str,
  lang: str,
  query: str,
  context: list[ContextItem],   # contains intent/chart/dataset/etc.
  constraints: { k: int, roles?: set[str], labels_any?: set[str], labels_all?: set[str] }
}
```

## Evidence + Trace Sketch (C)
```python
Evidence = {
  "guideline_id": str,
  "role": str,               # e.g., "advice", "context", "title", "description"
  "snippet": str,            # short excerpt from the matched unit
  "score": float,            # match score at the unit level
  "source": { "id": str, "role": str },  # reference into the catalog text units
}

StrategyTrace = {
  "strategy": str,            # stable ID, e.g. "semantic_sections@v1"
  "used_context_roles": list[str],
  "params": dict[str, object],
  "timings_ms": dict[str, float],
  "notes": list[str],
  "artifacts": dict[str, object],  # e.g., top unit hits before aggregation
}

RetrievalHit = {
  "guideline_id": str,
  "score": float,             # aggregated guideline score
  "evidence": list[Evidence],
  "preview": { "title": str, "description": str, "labels": list[str] },
  "debug": dict[str, object], # strategy-specific per-hit details
}

RetrievalResult = { "hits": list[RetrievalHit], "traces": list[StrategyTrace] }
```

## Strategy Sketches
- `SemanticSectionStrategy`: embed request text, nearest-neighbor over `{id, role, embedding}`; aggregate to guideline-level.
- `LabelFilterStrategy`: hard filters by catalog labels derived from request (rule-based/LLM-based later).
- `HybridRRFStrategy`: combine ranked lists from semantic + lexical using reciprocal-rank fusion.

## Next
For now, keep retrieval intentionally minimal while other parts of the system stabilize.

## Current Implementation (as of 2026-01-23)
`chartcoach.retrieval` currently provides a single placeholder strategy:
- `HeadRetrievalStrategy`: returns `vis_df.head(k)` (ignores `query`).

### Minimal Wiring Example
```python
import polars as pl

from chartcoach.retrieval import HeadRetrievalStrategy, ImageItem, RetrievalRequest, TextItem

catalog_df = pl.DataFrame({"id": ["g1", "g2", "g3"], "title": ["A", "B", "C"]})
request = RetrievalRequest(
    context=[
        TextItem(role="query", text="Retrieve visualization guidelines relevant to this chart and intent."),
        TextItem(role="intent", text="I want to show change over time and highlight key comparisons."),
        ImageItem(role="chart", uri="file://chart.png", mime="image/png"),
    ],
    k=2,
)
response = HeadRetrievalStrategy()(request=request, catalog_df=catalog_df)
print(response.result_df)
```
