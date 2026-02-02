from __future__ import annotations

import os
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


def _float_env(name: str, default: float) -> float:
    raw = (os.environ.get(name) or "").strip()
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        return default


def _int_env(name: str, default: int) -> int:
    raw = (os.environ.get(name) or "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


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


def create_strategy_lm() -> dspy.LM:
    # LiteLLM defaults can be too aggressive for local gateways and tool-using
    # programs. Keep this configurable and conservative by default.
    model = os.environ.get("CHARTCOACH_STRATEGY_LM_MODEL") or "gpt-5.1"
    timeout = _float_env("CHARTCOACH_LM_TIMEOUT_SECONDS", 120.0)
    retries = _int_env("CHARTCOACH_LM_NUM_RETRIES", 6)
    return create_openai_compatible_lm(
        model=model, timeout_seconds=timeout, num_retries=retries
    )


def create_strategy_vlm() -> dspy.LM:
    # Use the same OpenAI-compatible endpoint and credentials as the primary LM,
    # but allow separate (often longer) timeouts for vision requests.
    model = os.environ.get("CHARTCOACH_STRATEGY_VLM_MODEL") or "gpt-5.2"
    timeout = _float_env(
        "CHARTCOACH_VLM_TIMEOUT_SECONDS",
        _float_env("CHARTCOACH_LM_TIMEOUT_SECONDS", 120.0),
    )
    retries = _int_env(
        "CHARTCOACH_VLM_NUM_RETRIES",
        _int_env("CHARTCOACH_LM_NUM_RETRIES", 6),
    )
    return create_openai_compatible_lm(
        model=model, timeout_seconds=timeout, num_retries=retries
    )


def create_guideline_status_lm() -> dspy.LM:
    """LM used for lightweight guideline status classification/filtering."""

    model = (
        os.environ.get("CHARTCOACH_GUIDELINE_STATUS_LM_MODEL")
        or os.environ.get("CHARTCOACH_STRATEGY_LM_MODEL")
        or "gpt-5.1"
    )
    timeout = _float_env(
        "CHARTCOACH_GUIDELINE_STATUS_TIMEOUT_SECONDS",
        _float_env("CHARTCOACH_LM_TIMEOUT_SECONDS", 120.0),
    )
    retries = _int_env(
        "CHARTCOACH_GUIDELINE_STATUS_NUM_RETRIES",
        _int_env("CHARTCOACH_LM_NUM_RETRIES", 6),
    )
    return create_openai_compatible_lm(
        model=model, timeout_seconds=timeout, num_retries=retries
    )
