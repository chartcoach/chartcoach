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
        model="gpt-4o-mini", timeout_seconds=0.25, num_retries=-5
    )
    assert isinstance(lm, DummyLM)
    assert created["model"] == "openai/gpt-4o-mini"
    assert created["api_base"] == "http://example.invalid/v1"
    assert created["api_key"] == "x"
    assert created["timeout"] == 1.0
    assert created["num_retries"] == 0


def test_create_strategy_lm_vlm_and_status_use_env(monkeypatch) -> None:
    calls: list[dict[str, object]] = []

    def fake_create_openai_compatible_lm(**kwargs):  # noqa: ANN003
        calls.append(dict(kwargs))
        return kwargs

    monkeypatch.setattr(mod, "create_openai_compatible_lm", fake_create_openai_compatible_lm)

    # Strategy LM.
    monkeypatch.setenv("CHARTCOACH_STRATEGY_LM_MODEL", "gpt-4o-mini")
    monkeypatch.setenv("CHARTCOACH_LM_TIMEOUT_SECONDS", "123.5")
    monkeypatch.setenv("CHARTCOACH_LM_NUM_RETRIES", "7")
    out = mod.create_strategy_lm()
    assert out["model"] == "gpt-4o-mini"
    assert out["timeout_seconds"] == 123.5
    assert out["num_retries"] == 7

    # Strategy VLM (falls back to LM timeout/retries when not set).
    monkeypatch.setenv("CHARTCOACH_STRATEGY_VLM_MODEL", "gpt-4.1-mini")
    monkeypatch.delenv("CHARTCOACH_VLM_TIMEOUT_SECONDS", raising=False)
    monkeypatch.delenv("CHARTCOACH_VLM_NUM_RETRIES", raising=False)
    out = mod.create_strategy_vlm()
    assert out["model"] == "gpt-4.1-mini"
    assert out["timeout_seconds"] == 123.5
    assert out["num_retries"] == 7

    # Guideline status LM (prefers dedicated env vars).
    monkeypatch.setenv("CHARTCOACH_GUIDELINE_STATUS_LM_MODEL", "gpt-4o-mini")
    monkeypatch.setenv("CHARTCOACH_GUIDELINE_STATUS_TIMEOUT_SECONDS", "9")
    monkeypatch.setenv("CHARTCOACH_GUIDELINE_STATUS_NUM_RETRIES", "2")
    out = mod.create_guideline_status_lm()
    assert out["model"] == "gpt-4o-mini"
    assert out["timeout_seconds"] == 9.0
    assert out["num_retries"] == 2

    # Invalid env values fall back to defaults.
    monkeypatch.setenv("CHARTCOACH_LM_TIMEOUT_SECONDS", "nope")
    monkeypatch.setenv("CHARTCOACH_LM_NUM_RETRIES", "nope")
    out = mod.create_strategy_lm()
    assert out["timeout_seconds"] == 120.0
    assert out["num_retries"] == 6
