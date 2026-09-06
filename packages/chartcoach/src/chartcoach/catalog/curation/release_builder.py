from __future__ import annotations

import json
import os
import shutil
from collections.abc import Mapping
from dataclasses import dataclass, field
from importlib.metadata import PackageNotFoundError, version
from os import PathLike
from pathlib import Path
from types import MappingProxyType
from typing import TYPE_CHECKING, TypeAlias

from ..model import Catalog
from ..profile_layout import validate_profile_id
from ..profiles import DistanceMetric, validate_requirements
from ..releases import CatalogRelease, ReleaseArtifact
from ..releases.hashing import release_digest, sha256_file
from .artifacts import build_release_artifacts

if TYPE_CHECKING:
    from lancedb.embeddings import EmbeddingFunction


@dataclass(frozen=True, slots=True)
class EmbeddingProfile:
    """Build configuration for one index profile and its optional exports."""

    embedding: EmbeddingFunction
    distance_metric: DistanceMetric = "cosine"
    python_requirements: Mapping[str, str] = field(default_factory=dict)
    umap: Mapping[str, object] | None = None
    export_documents: bool = False

    def __post_init__(self) -> None:
        if self.distance_metric not in {"cosine", "l2", "dot"}:
            raise ValueError(
                f"Unsupported profile distance metric: {self.distance_metric!r}."
            )
        requirements = validate_requirements(self.python_requirements)
        for distribution, expected in requirements.items():
            try:
                actual = version(distribution)
            except PackageNotFoundError as exc:
                raise ValueError(
                    f"Profile requirement is not installed: {distribution}=={expected}."
                ) from exc
            if actual != expected:
                raise ValueError(
                    f"Profile requirement {distribution} must be {expected}, found {actual}."
                )
        object.__setattr__(self, "python_requirements", MappingProxyType(requirements))
        if self.umap is not None:
            object.__setattr__(self, "umap", MappingProxyType(dict(self.umap)))
        if not isinstance(self.export_documents, bool):
            raise TypeError("Profile export_documents must be a boolean.")


@dataclass(frozen=True, slots=True)
class ProfileReuse:
    """A profile from a verified local release reused for derived exports."""

    release: str | PathLike[str]
    profile: str
    umap: Mapping[str, object] | None = None
    export_documents: bool = False

    def __post_init__(self) -> None:
        value = os.fspath(self.release)
        if not isinstance(value, str):
            raise TypeError("Profile reuse release must contain text.")
        object.__setattr__(self, "release", Path(value).absolute())
        object.__setattr__(
            self,
            "profile",
            validate_profile_id(self.profile),
        )
        if self.umap is not None:
            object.__setattr__(self, "umap", MappingProxyType(dict(self.umap)))
        if not isinstance(self.export_documents, bool):
            raise TypeError("Profile export_documents must be a boolean.")


ProfileBuild: TypeAlias = EmbeddingProfile | ProfileReuse

_NO_PROFILES: Mapping[str, ProfileBuild] = MappingProxyType({})


def build_release(
    catalog: Catalog,
    output: PathLike[str],
    *,
    profiles: Mapping[str, ProfileBuild] = _NO_PROFILES,
) -> CatalogRelease:
    profiles = _normalized_profiles(profiles)
    root = Path(output)
    root.parent.mkdir(parents=True, exist_ok=True)
    root.mkdir()
    try:
        manifest_path = root / "MANIFEST.md"
        entries_path = root / "entries.parquet"
        catalog.manifest.write(manifest_path)
        catalog.to_frame().write_parquet(entries_path)
        artifacts = {
            "MANIFEST.md": _artifact(manifest_path),
            "entries.parquet": _artifact(entries_path),
            **build_release_artifacts(catalog, root, profiles=profiles),
        }
        release = CatalogRelease(
            digest=release_digest(artifacts),
            artifacts=artifacts,
        )
        (root / "release.json").write_text(
            json.dumps(release.to_record(), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    except BaseException:
        shutil.rmtree(root)
        raise
    return release


def _normalized_profiles(
    profiles: Mapping[str, ProfileBuild],
) -> dict[str, ProfileBuild]:
    normalized: dict[str, ProfileBuild] = {}
    for value, profile in profiles.items():
        name = validate_profile_id(value)
        if not isinstance(profile, EmbeddingProfile | ProfileReuse):
            raise TypeError(f"Profile {name!r} has an invalid build specification.")
        normalized[name] = profile
    return normalized


def _artifact(path: Path) -> ReleaseArtifact:
    return ReleaseArtifact(
        sha256=sha256_file(path),
        bytes=path.stat().st_size,
    )


__all__ = ["EmbeddingProfile", "ProfileBuild", "ProfileReuse", "build_release"]
