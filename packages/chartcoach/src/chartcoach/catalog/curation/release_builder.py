from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
import json
from pathlib import Path
from pathlib import PurePosixPath
import shutil
from types import MappingProxyType
from typing import TYPE_CHECKING

from ..collection import Catalog
from ..releases import CatalogRelease, ReleaseArtifact
from ..releases.hashing import release_digest, sha256_file
from .artifacts import _profile_path, build_release_artifacts

if TYPE_CHECKING:
    from lancedb.embeddings import EmbeddingFunction


@dataclass(frozen=True, slots=True)
class EmbeddingProfile:
    """A LanceDB embedding function and its UMAP projection options."""

    embedding: "EmbeddingFunction"
    umap: Mapping[str, object] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "umap", MappingProxyType(dict(self.umap)))


_NO_PROFILES: Mapping[str, EmbeddingProfile] = MappingProxyType({})


def build_catalog_release(
    catalog: Catalog,
    *,
    root: Path,
    profiles: Mapping[str, EmbeddingProfile] = _NO_PROFILES,
) -> CatalogRelease:
    profiles = _normalized_profiles(profiles)
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
    profiles: Mapping[str, EmbeddingProfile],
) -> dict[str, EmbeddingProfile]:
    normalized: dict[str, EmbeddingProfile] = {}
    names: dict[str, str] = {}
    for value, profile in profiles.items():
        name = _profile_path(value)
        folded = name.casefold()
        if previous := names.get(folded):
            raise ValueError(f"Embedding profile names collide: {previous}, {name}")
        names[folded] = name
        normalized[name] = profile
    _validate_profile_artifact_paths(normalized)
    return normalized


def _validate_profile_artifact_paths(
    profiles: Mapping[str, EmbeddingProfile],
) -> None:
    generated = sorted(
        PurePosixPath("profiles", profile, suffix)
        for profile in profiles
        for suffix in ("documents.parquet", "index.tar.gz")
    )
    for index, path in enumerate(generated):
        parts = tuple(part.casefold() for part in path.parts)
        for other in generated[index + 1 :]:
            other_parts = tuple(part.casefold() for part in other.parts)
            shorter = min(len(parts), len(other_parts))
            if parts[:shorter] == other_parts[:shorter]:
                raise ValueError(
                    f"Embedding profile artifact paths collide: {path}, {other}"
                )


def _artifact(path: Path) -> ReleaseArtifact:
    return ReleaseArtifact(
        sha256=sha256_file(path),
        bytes=path.stat().st_size,
    )


__all__ = ["EmbeddingProfile", "build_catalog_release"]
