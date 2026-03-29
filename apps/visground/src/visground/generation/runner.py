import json
from typing import Callable, TypedDict, cast

import dspy

from .backends import VisualizationBackend
from .models import VisualizationRequestRecord
from .signatures import WriteVisualizationCode

_VIS_GEN_OUTPUT_FIELDS = (
    "code",
    "visualization_type",
    "query_interpretation",
    "design_rationale",
    "grounding_trace",
)


class VisGenOutput(TypedDict):
    id: str
    code: str
    visualization_type: str
    query_interpretation: str
    design_rationale: list[str]
    grounding_trace: list[str]


class VisGenRunner:
    def __init__(
        self,
        backend: VisualizationBackend,
        coder_signature: type[dspy.Signature] = WriteVisualizationCode,
    ):
        self.backend = backend
        self.coder_signature = coder_signature
        self._reward_fn = _build_reward_function(backend)

    def _cache(self):
        return dspy.cache

    def _cache_put(self, cache_key: str, value: dict) -> None:
        self._cache().put({"key": cache_key}, value)

    def _cache_get(self, cache_key: str) -> dict | None:
        return self._cache().get({"key": cache_key})

    def _cache_key(self, example: dspy.Example) -> str:
        lm = dspy.settings.lm
        cache_obj = {
            "example": example.inputs().toDict(),
            "lm": lm.model,
            "output_fields": _VIS_GEN_OUTPUT_FIELDS,
        }
        return json.dumps(
            cache_obj,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        )

    def _cache_value(self, prediction: dspy.Prediction) -> dict:
        return {
            "code": prediction.code,
            "visualization_type": prediction.visualization_type,
            "query_interpretation": prediction.query_interpretation,
            "design_rationale": prediction.design_rationale,
            "grounding_trace": prediction.grounding_trace,
        }

    def generate(
        self,
        requests: list[VisualizationRequestRecord],
        num_threads: int = 20,
    ) -> list[VisGenOutput]:
        coder = dspy.ChainOfThought(self.coder_signature)
        generate_code = dspy.Refine(
            module=coder,
            N=10,
            reward_fn=self._reward_fn,
            threshold=1.0,
        )
        examples = [self.backend.build_example(req) for req in requests]
        fresh_examples = [
            example
            for example in examples
            if self._cache_get(self._cache_key(example)) is None
        ]

        inputs = [
            (
                generate_code,
                example,
            )
            for example in fresh_examples
        ]

        parallel = dspy.Parallel(num_threads=num_threads)
        results = parallel(inputs) if fresh_examples else []

        for example, result in zip(fresh_examples, results):
            self._cache_put(self._cache_key(example), self._cache_value(result))

        return [
            cast(
                VisGenOutput,
                {
                    "id": req["id"],
                    **output,
                },
            )
            for req, example in zip(requests, examples)
            if (output := self._cache_get(self._cache_key(example))) is not None
        ]


def _build_reward_function(
    backend: VisualizationBackend,
) -> Callable[[dict, dspy.Prediction], float]:
    def fn(args: dict, pred: dspy.Prediction) -> float:
        id = args["id"]
        code = pred.code
        try:
            vis = backend.materialize_visualization(id, code)
            return float(vis is not None)
        except Exception:
            return 0.0

    return fn
