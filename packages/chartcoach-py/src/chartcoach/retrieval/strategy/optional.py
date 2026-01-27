from __future__ import annotations

import importlib.util
from types import ModuleType


def is_dspy_available() -> bool:
    return importlib.util.find_spec("dspy") is not None


def require_dspy() -> ModuleType:
    """Import DSPy or raise a helpful error.

    DSPy is an optional dependency (install `chartcoach[retrieval]`).
    """
    try:
        import dspy
    except ModuleNotFoundError as e:
        # If DSPy itself is missing, raise a clear installation hint.
        # If a DSPy sub-dependency is missing, re-raise to preserve the root cause.
        if e.name != "dspy":
            raise
        raise RuntimeError(
            "DSPy is required for retrieval strategies. Install `chartcoach[retrieval]`."
        ) from e
    return dspy
