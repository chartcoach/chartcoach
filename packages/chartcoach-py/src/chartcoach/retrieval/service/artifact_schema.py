from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from chartcoach.retrieval.service.eval_artifacts_schema import (
    ARTIFACT_SCHEMA_VERSION,
    EvalArtifactsIndexArtifact,
    EvalScenarioBundleArtifact,
)


def generate_artifacts_json_schema() -> dict[str, Any]:
    """Generate the JSON Schema for eval artifacts (index + per-scenario bundles).

    This is the single source of truth for schema drift checks. The schema is
    derived directly from the pydantic models used by the artifacts builder.
    """

    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": f"ChartCoach Eval Artifacts (v{ARTIFACT_SCHEMA_VERSION})",
        "artifact_schema_version": ARTIFACT_SCHEMA_VERSION,
        "documents": {
            "index": EvalArtifactsIndexArtifact.model_json_schema(),
            "bundle": EvalScenarioBundleArtifact.model_json_schema(),
        },
    }


def write_artifacts_json_schema(path: Path) -> None:
    schema = generate_artifacts_json_schema()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(schema, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="chartcoach-artifact-schema")
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("docs/artifacts/schema-v1.json"),
        help="Output schema path (default: docs/artifacts/schema-v1.json).",
    )
    args = parser.parse_args(argv)
    write_artifacts_json_schema(args.out)


if __name__ == "__main__":  # pragma: no cover
    main()
