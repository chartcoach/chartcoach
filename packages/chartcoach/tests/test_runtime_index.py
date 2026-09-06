from __future__ import annotations

from pathlib import Path
import shutil

import pytest

from chartcoach import CatalogError, open_index
from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.curation import EmbeddingProfile, build_release
from chartcoach.catalog.documents import document_rows
from catalog_testkit import deterministic_embedding


pytestmark = [pytest.mark.curation, pytest.mark.search]
_PROFILE = "test/deterministic"
_EMBEDDING = "chartcoach-runtime-index-test"


def test_open_index_extracts_and_reuses_a_release_profile(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_root = tmp_path / "release"
    release = build_release(
        sample_catalog,
        release_root,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding(_EMBEDDING),
                umap={"n_neighbors": 3},
            )
        },
    )
    cache = tmp_path / "cache"
    monkeypatch.setattr("chartcoach.catalog.runtime._cache_root", lambda: cache)

    first = open_index(release_root, profile=_PROFILE)
    artifact = release.artifact(f"profiles/{_PROFILE}/index.tar.gz")
    extracted = cache / "indexes" / artifact.sha256
    second = open_index(release_root / "release.json", profile=_PROFILE)

    assert (
        first.count_rows()
        == second.count_rows()
        == document_rows(sample_catalog).height
    )
    assert (extracted / "documents.lance").is_dir()
    assert (extracted / ".complete").read_text() == artifact.sha256


def test_open_index_repairs_an_incomplete_extraction(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_root = tmp_path / "release"
    release = build_release(
        sample_catalog,
        release_root,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding(_EMBEDDING),
                umap={"n_neighbors": 3},
            )
        },
    )
    cache = tmp_path / "cache"
    monkeypatch.setattr("chartcoach.catalog.runtime._cache_root", lambda: cache)
    open_index(release_root, profile=_PROFILE)
    artifact = release.artifact(f"profiles/{_PROFILE}/index.tar.gz")
    extracted = cache / "indexes" / artifact.sha256
    shutil.rmtree(extracted / "documents.lance")

    repaired = open_index(release_root, profile=_PROFILE)

    assert repaired.count_rows() == document_rows(sample_catalog).height
    assert (extracted / "documents.lance").is_dir()


def test_open_index_lists_available_profiles(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release_root = tmp_path / "release"
    build_release(sample_catalog, release_root)

    with pytest.raises(CatalogError, match="Available profiles: none"):
        open_index(release_root, profile="missing")


def test_open_index_rejects_a_symlinked_artifact_parent(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release_root = tmp_path / "release"
    build_release(
        sample_catalog,
        release_root,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding(_EMBEDDING),
                umap={"n_neighbors": 3},
            )
        },
    )
    profile_root = release_root / "profiles" / "test"
    outside = tmp_path / "outside"
    profile_root.rename(outside)
    profile_root.symlink_to(outside, target_is_directory=True)

    with pytest.raises(CatalogError, match="Catalog artifact is missing"):
        open_index(release_root, profile=_PROFILE)
