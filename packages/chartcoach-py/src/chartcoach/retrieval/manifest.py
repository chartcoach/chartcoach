from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, ConfigDict, Field


MANIFEST_SCHEMA_VERSION = 1


class _ManifestBaseModel(BaseModel):
    model_config = ConfigDict(frozen=True)


class ManifestRunSpec(_ManifestBaseModel):
    scenarios: str = Field(min_length=1, default="evals/scenarios/spec.yaml")
    catalog_uri: str = Field(min_length=1)
    artifacts_url: str | None = None
    purge: bool = False
    strategies: list[str] = Field(default_factory=list)
    k: int | None = Field(default=None, ge=1)


class ExperimentManifest(_ManifestBaseModel):
    schema_version: int = Field(default=MANIFEST_SCHEMA_VERSION, frozen=True)
    run: ManifestRunSpec
    config: dict[str, Any] = Field(default_factory=dict)

    def public_dict(self) -> dict[str, Any]:
        """Return a secret-safe summary suitable for embedding in artifact metadata."""

        return {
            "schema_version": self.schema_version,
            "run": self.run.model_dump(mode="json", exclude_none=True),
            # This is a run-config override document (never includes API keys). We keep it
            # to reproduce paper runs without relying on ambient env defaults.
            "config": dict(self.config),
        }


def load_manifest(path: str | Path) -> ExperimentManifest:
    p = Path(path)
    loaded = yaml.safe_load(p.read_text(encoding="utf-8"))
    if not isinstance(loaded, dict):
        raise ValueError("Expected YAML mapping at --manifest path.")
    return ExperimentManifest.model_validate(loaded)
