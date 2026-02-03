from __future__ import annotations

from typing import TYPE_CHECKING

from chartcoach.env import load_env
from chartcoach.retrieval.strategy.optional import require_dspy

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


def _normalize_model(model: str) -> str:
    model = (model or "").strip()
    if not model:
        raise ValueError("Missing model name.")

    # DSPy 3.x relies on provider-prefixed model names (e.g. `openai/gpt-4o-mini`).
    if "/" not in model and not model.startswith("ft:"):
        return f"openai/{model}"
    return model


def create_openai_compatible_lm(
    *,
    model: str,
    timeout_seconds: float,
    num_retries: int,
) -> dspy.LM:
    openai = load_env().openai.require()
    return dspy.LM(
        model=_normalize_model(model),
        api_base=openai.api_base,
        api_key=openai.api_key,
        num_retries=max(0, int(num_retries)),
        timeout=max(1.0, float(timeout_seconds)),
    )


def create_lm(*, model: str, timeout_seconds: float, num_retries: int) -> dspy.LM:
    return create_openai_compatible_lm(
        model=model, timeout_seconds=timeout_seconds, num_retries=num_retries
    )
