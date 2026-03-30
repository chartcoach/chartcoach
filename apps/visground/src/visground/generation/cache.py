from __future__ import annotations

import json
from collections.abc import Sequence
from typing import cast

import dspy

from .models import VisGenOutput
from .signatures import ReviewVisualizationImplementation, WriteVisualizationCode

_CACHE_NAMESPACE = "visground.generation.v5"


class VisGenCache:
    def __init__(
        self,
        runtime_config: dict[str, object],
        namespace: str = _CACHE_NAMESPACE,
    ) -> None:
        self._runtime_config = runtime_config
        self._namespace = namespace

    @classmethod
    def for_runtime(
        cls,
        *,
        backend: object,
        coder_signature: type[dspy.Signature] = WriteVisualizationCode,
        review_signature: type[dspy.Signature] = ReviewVisualizationImplementation,
        reviewer_lm: dspy.LM | None = None,
        refine_rollouts: int,
        refine_threshold: float | None,
        namespace: str = _CACHE_NAMESPACE,
    ) -> VisGenCache:
        runtime_config = {
            "backend": _type_identity(type(backend)),
            "coder_signature": _type_identity(coder_signature),
            "review_signature": _type_identity(review_signature),
            "generator_lm": _lm_cache_state(dspy.settings.lm),
            "reviewer_lm": _lm_cache_state(reviewer_lm),
            "refine_rollouts": refine_rollouts,
            "refine_threshold": refine_threshold,
        }
        return cls(runtime_config=runtime_config, namespace=namespace)

    def get_many(
        self,
        examples: Sequence[dspy.Example],
    ) -> tuple[list[VisGenOutput | None], list[tuple[int, dspy.Example]]]:
        outputs: list[VisGenOutput | None] = []
        misses: list[tuple[int, dspy.Example]] = []
        for index, example in enumerate(examples):
            key = self._cache_key(example)
            value = dspy.cache.get({"key": key})
            if _is_visgen_output(value):
                outputs.append(value)
            else:
                outputs.append(None)
                misses.append((index, example))
        return outputs, misses

    def put_many(
        self,
        examples: Sequence[dspy.Example],
        outputs: Sequence[VisGenOutput],
    ) -> None:
        for example, output in zip(examples, outputs):
            dspy.cache.put({"key": self._cache_key(example)}, output)

    def _cache_key(self, example: dspy.Example) -> str:
        return json.dumps(
            {
                "ns": self._namespace,
                "runtime": self._runtime_config,
                "example": example.inputs().toDict(),
            },
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
            default=str,
        )


def _is_visgen_output(value: object) -> bool:
    if not isinstance(value, dict):
        return False
    value_dict = cast(dict[str, object], value)
    keys = {
        "id",
        "code",
        "visualization_type",
        "grounding_trace",
    }
    if not keys.issubset(value_dict):
        return False

    grounding_trace = value_dict["grounding_trace"]
    return isinstance(grounding_trace, dict) and all(
        isinstance(key, str) and isinstance(item, str)
        for key, item in grounding_trace.items()
    )


def _type_identity(obj: object) -> str:
    module = getattr(obj, "__module__", type(obj).__module__)
    qualname = getattr(obj, "__qualname__", type(obj).__qualname__)
    return f"{module}:{qualname}"


def _lm_cache_state(lm: dspy.LM | None) -> object | None:
    if lm is None:
        return None
    if hasattr(lm, "dump_state"):
        return _sanitize_for_cache(lm.dump_state())
    return _sanitize_for_cache(
        {
            "class": _type_identity(type(lm)),
            "model": getattr(lm, "model", None),
            "kwargs": getattr(lm, "kwargs", None),
        }
    )


def _sanitize_for_cache(value: object) -> object:
    if isinstance(value, dict):
        return {str(key): _sanitize_for_cache(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_sanitize_for_cache(item) for item in value]
    return value
