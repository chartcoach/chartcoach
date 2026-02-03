from __future__ import annotations

import json
from pathlib import Path

from chartcoach.retrieval.service.artifact_schema import generate_artifacts_json_schema
from chartcoach.retrieval.service.eval_artifacts_schema import (
    EvalArtifactsIndexArtifact,
    EvalScenarioBundleArtifact,
)


def _repo_root() -> Path:
    cwd = Path.cwd().resolve()
    for candidate in [cwd, *cwd.parents]:
        if (candidate / "packages").exists() and (candidate / "apps").exists():
            return candidate
    raise RuntimeError("Could not locate repo root from cwd.")


def test_artifact_schema_json_is_up_to_date() -> None:
    repo_root = _repo_root()
    schema_path = repo_root / "docs" / "artifacts" / "schema-v1.json"
    loaded = json.loads(schema_path.read_text(encoding="utf-8"))
    assert loaded == generate_artifacts_json_schema()


def test_eval_ui_fixture_artifacts_validate_against_pydantic_models() -> None:
    repo_root = _repo_root()
    fixtures_root = (
        repo_root / "apps" / "eval-ui" / "fixtures" / "eval-artifacts" / "v1"
    )

    index_path = fixtures_root / "index.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    EvalArtifactsIndexArtifact.model_validate(index)

    bundles_dir = fixtures_root / "bundles"
    bundle_paths = sorted(p for p in bundles_dir.glob("*.json") if p.is_file())
    assert bundle_paths, "Expected at least one eval artifacts bundle fixture."
    bundle = json.loads(bundle_paths[0].read_text(encoding="utf-8"))
    EvalScenarioBundleArtifact.model_validate(bundle)
