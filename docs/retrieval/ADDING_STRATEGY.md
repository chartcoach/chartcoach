# Adding a Retrieval Strategy (No Benchmark Coupling)

This repo treats retrieval strategies as research artifacts. The implementation must be:

- reusable across arbitrary scenarios (no hardcoding against `evals/scenarios/**`),
- reproducible (no env-var reads from strategies; config is injected),
- inspectable (emit typed telemetry + evidence snippets).

## Where Strategies Live

- Implementations: `packages/chartcoach-py/src/chartcoach/retrieval/strategy/pipelines/*`
- Registry: `packages/chartcoach-py/src/chartcoach/retrieval/strategy/registry.py`
- Shared operators (preferred): `packages/chartcoach-py/src/chartcoach/retrieval/operators/*`

## Required Contracts

1) **Scenario-agnostic**
- Never reference scenario ids, `evals/scenarios`, or `nogit/strat-eval`.
- Any non-trivial “intelligence” must be an explicit DSPy/VLM step.

2) **Use the runtime + config**
- Do not create global caches.
- Use `StrategyRuntime` for indices, LMs, and caches.
- Do not read environment variables inside strategies.

3) **Emit `StrategyTrace`**
- `RetrievalResponse.meta` must validate against `chartcoach.retrieval.trace.StrategyTrace`.
- Minimum: `k` and `hits` (ids, plus evidence when available).
- Set `score_kind` to describe the ranking semantics (e.g., `rrf_fusion`, `rank_normalized`).

## Minimal Skeleton

```python
from __future__ import annotations

from chartcoach.retrieval.strategy.base import RetrievalStrategy, StrategyInfo
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse
from chartcoach.retrieval.trace import StrategyTrace


class MyStrategy(RetrievalStrategy):
    id = "my-strategy@v1"

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        # 1) build query text from the canonical situation (via GuidelineSearcher)
        # 2) retrieve candidates using operators/searcher
        # 3) attach evidence + trace

        trace = StrategyTrace(k=request.k or 10, hits=[])
        return RetrievalResponse(catalog=self._catalog, meta=trace.model_dump(mode="json"))


INFO = StrategyInfo(
    id=MyStrategy.id,
    name="My Strategy",
    description="One-line description of what family it represents.",
)
```

## Tests (Signal > Coverage)

Add a small contract test that:

- instantiates the strategy with a tiny Catalog,
- calls it with a minimal request,
- asserts:
  - it returns `k` items (or fewer if catalog is smaller),
  - `StrategyTrace` validates,
  - no scenario ids are referenced (guardrails already enforce this globally).

## Guardrails

Repo guardrail tests will fail if:

- a `hints_*.py` file is tracked,
- strategy/operator code references `evals/scenarios`, `nogit/strat-eval`, or any scenario id from `evals/scenarios/spec.yaml`.

