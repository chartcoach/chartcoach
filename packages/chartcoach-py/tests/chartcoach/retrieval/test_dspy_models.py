from __future__ import annotations

import pytest

from chartcoach.retrieval.strategy import dspy_models as mod


def test_normalize_model_prefixes_openai_and_preserves_ft() -> None:
    assert mod._normalize_model("gpt-4o-mini") == "openai/gpt-4o-mini"
    assert mod._normalize_model("openai/gpt-4o-mini") == "openai/gpt-4o-mini"
    assert mod._normalize_model("ft:custom") == "ft:custom"

    with pytest.raises(ValueError, match="Missing model name"):
        mod._normalize_model("")


def test_create_openai_compatible_lm_uses_env_and_clamps(monkeypatch) -> None:
    class DummyEnv:
        def __init__(self) -> None:
            self.openai = self
            self.api_base = "http://example.invalid/v1"
            self.api_key = "x"

        def require(self) -> "DummyEnv":
            return self

    created: dict[str, object] = {}

    class DummyLM:
        def __init__(self, **kwargs):  # noqa: ANN003
            created.update(kwargs)

    monkeypatch.setattr(mod, "load_env", lambda: DummyEnv())
    monkeypatch.setattr(mod.dspy, "LM", DummyLM)

    lm = mod.create_openai_compatible_lm(
        model="gpt-4o-mini",
        timeout_seconds=0.25,
        num_retries=-5,
        temperature=0.0,
        max_tokens=None,
    )
    assert isinstance(lm, DummyLM)
    assert created["model"] == "openai/gpt-4o-mini"
    assert created["api_base"] == "http://example.invalid/v1"
    assert created["api_key"] == "x"
    assert created["timeout"] == 1.0
    assert created["num_retries"] == 0
