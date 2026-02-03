from __future__ import annotations

from pathlib import Path

from chartcoach.retrieval.config import load_run_config


def test_load_run_config_parses_strategy_timeout_env(monkeypatch) -> None:
    monkeypatch.setenv("CHARTCOACH_EMBEDDING_PROJECTOR", "sentence_transformers")

    monkeypatch.setenv("CHARTCOACH_STRATEGY_TIMEOUT_SECONDS", "-1")
    assert load_run_config().strategy_timeout_seconds is None

    monkeypatch.setenv("CHARTCOACH_STRATEGY_TIMEOUT_SECONDS", "0.1")
    assert load_run_config().strategy_timeout_seconds == 1.0


def test_load_run_config_applies_yaml_overrides(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("CHARTCOACH_EMBEDDING_PROJECTOR", "sentence_transformers")

    cfg_path = tmp_path / "run.yaml"
    cfg_path.write_text(
        """
focus:
  mode: violations
chart_vision:
  enabled: true
lms:
  strategy:
    model: gpt-5.1
""".lstrip(),
        encoding="utf-8",
    )

    cfg = load_run_config(cfg_path)
    assert cfg.focus.mode == "violations"
    assert cfg.chart_vision.enabled is True
    assert cfg.lms.strategy.model == "gpt-5.1"


def test_run_config_public_dict_does_not_expose_embedding_secrets(monkeypatch) -> None:
    monkeypatch.setenv("CHARTCOACH_EMBEDDING_PROJECTOR", "litellm")
    monkeypatch.setenv("OPENAI_BASE_URL", "http://example.invalid/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "x")

    cfg = load_run_config()
    embedding_args = cfg.public_dict()["embedding"]["args"]
    assert "api_key" not in embedding_args
    assert "api_base" not in embedding_args
    assert embedding_args.get("normalize_embeddings") is True
