from __future__ import annotations

import pytest
from chartcoach.catalog.releases import CatalogRelease, ReleaseArtifact
from chartcoach.catalog.releases.hashing import release_digest


def _artifacts() -> dict[str, ReleaseArtifact]:
    return {
        "MANIFEST.md": ReleaseArtifact(sha256="a" * 64, bytes=1),
        "entries.parquet": ReleaseArtifact(sha256="b" * 64, bytes=2),
        "profiles/minilm/documents.parquet": ReleaseArtifact(
            sha256="c" * 64,
            bytes=3,
        ),
        "profiles/minilm/index.tar.gz": ReleaseArtifact(
            sha256="d" * 64,
            bytes=4,
        ),
        "profiles/minilm/profile.json": ReleaseArtifact(
            sha256="e" * 64,
            bytes=5,
        ),
    }


def test_release_round_trips_a_path_keyed_artifact_envelope() -> None:
    artifacts = _artifacts()
    release = CatalogRelease(digest=release_digest(artifacts), artifacts=artifacts)

    assert CatalogRelease.from_mapping(release.to_record()) == release
    assert release.to_record()["artifacts"] == {
        path: artifact.to_record() for path, artifact in artifacts.items()
    }


def test_release_identity_is_independent_of_mapping_order() -> None:
    artifacts = _artifacts()

    assert release_digest(artifacts) == release_digest(
        dict(reversed(artifacts.items()))
    )


def test_release_requires_safe_core_paths() -> None:
    artifacts = _artifacts()
    artifacts.pop("MANIFEST.md")
    with pytest.raises(ValueError, match="MANIFEST.md"):
        CatalogRelease(digest=release_digest(artifacts), artifacts=artifacts)

    artifacts = _artifacts()
    artifacts["../outside"] = ReleaseArtifact(sha256="f" * 64, bytes=1)
    with pytest.raises(ValueError, match="portable relative path"):
        CatalogRelease(digest=release_digest(artifacts), artifacts=artifacts)
