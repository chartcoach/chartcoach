from __future__ import annotations

from pathlib import Path

from chartcoach.retrieval.config import load_run_config_from_doc
from chartcoach.retrieval.manifest import ExperimentManifest, load_manifest


def test_load_manifest_parses_run_and_config(tmp_path: Path) -> None:
    path = tmp_path / "manifest.yaml"
    path.write_text(
        """
schema_version: 1
run:
  scenarios: evals/scenarios/spec.yaml
  catalog_uri: file:///tmp/catalog.parquet
  artifacts_url: memory://
  purge: false
  strategies: ["hybrid-rrf@v1"]
  k: 16
config:
  focus:
    mode: violations
""".lstrip(),
        encoding="utf-8",
    )

    manifest = load_manifest(path)
    assert isinstance(manifest, ExperimentManifest)
    assert manifest.run.k == 16
    assert manifest.run.catalog_uri == "file:///tmp/catalog.parquet"
    assert manifest.config["focus"]["mode"] == "violations"
    public = manifest.public_dict()
    assert public["run"]["strategies"] == ["hybrid-rrf@v1"]


def test_load_run_config_from_doc_ignores_env_when_disabled(monkeypatch) -> None:
    monkeypatch.setenv("CHARTCOACH_STRATEGY_LM_MODEL", "gpt-4o-mini")
    cfg = load_run_config_from_doc({}, use_env=False)
    # Deterministic defaults: env is only used when explicitly enabled.
    assert cfg.lms.strategy.model == "gpt-5.1"


def test_load_run_config_from_doc_accepts_none_doc() -> None:
    cfg = load_run_config_from_doc(None, use_env=False)
    assert cfg.lms.strategy.model == "gpt-5.1"
