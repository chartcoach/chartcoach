from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import Catalog
from chartcoach._catalog.curation.release_publisher import (
    _publish_release,
    _select_release,
)
from chartcoach._catalog.paths import paths
from chartcoach._catalog.releases import CatalogRelease
from chartcoach.curation import (
    EmbeddingProfile,
    build_release,
    publish_release,
    select_release,
)
from obstore.store import MemoryStore

pytestmark = pytest.mark.curation


def test_public_facade_publishes_and_selects_a_file_destination(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    release = build_release(sample_catalog, root)
    destination = (tmp_path / "objects").as_uri()

    published = publish_release(root, destination)
    selected = select_release(release.digest, destination)

    assert published == selected == release
    assert (
        CatalogRelease.from_mapping(
            json.loads((tmp_path / "objects" / paths.selected()).read_text())
        )
        == release
    )


def test_publish_and_select_release_by_digest_in_memory_store(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    release = build_release(sample_catalog, root)
    store = MemoryStore()

    published = _publish_release(store, root)
    selected = _select_release(store, release.digest)

    assert published == release
    assert selected == release
    assert (
        CatalogRelease.from_mapping(json.loads(_read_bytes(store, paths.selected())))
        == release
    )


def test_publish_repairs_an_uncommitted_artifact(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    release = build_release(sample_catalog, root)
    store = MemoryStore()
    artifact_path = "entries.parquet"
    object_path = paths.release(release.digest).artifact(artifact_path)
    store.put(object_path, b"partial")

    _publish_release(store, root)

    assert _read_bytes(store, object_path) == (root / artifact_path).read_bytes()


def test_publish_is_idempotent_after_release_commit(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    build_release(sample_catalog, root)
    store = MemoryStore()

    first = _publish_release(store, root)
    second = _publish_release(store, root)

    assert second == first


def test_publish_relocates_the_self_contained_lancedb_profile(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    profile = "minilm-normalized"
    release = build_release(
        sample_catalog,
        root,
        profiles={
            profile: EmbeddingProfile(
                deterministic_embedding("published-index-profile")
            )
        },
    )
    store = MemoryStore()

    _publish_release(store, root)

    release_paths = paths.release(release.digest)
    for filename in ("profile.json", "index.tar.gz"):
        artifact = f"profiles/{profile}/{filename}"
        assert (
            _read_bytes(store, release_paths.artifact(artifact))
            == (root / artifact).read_bytes()
        )


def test_select_keeps_the_current_release_when_digest_is_missing(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    release = build_release(sample_catalog, root)
    store = MemoryStore()
    _publish_release(store, root)
    _select_release(store, release.digest)
    current = _read_bytes(store, paths.selected())

    with pytest.raises(FileNotFoundError):
        _select_release(store, "0" * 64)

    assert _read_bytes(store, paths.selected()) == current


@pytest.mark.parametrize("damage", ["missing", "corrupt"])
def test_committed_publish_rejects_damaged_artifacts_without_repair(
    sample_catalog: Catalog, tmp_path: Path, damage: str
) -> None:
    root = tmp_path / "release"
    release = build_release(sample_catalog, root)
    store = MemoryStore()
    _publish_release(store, root)
    key = paths.release(release.digest).artifact("entries.parquet")
    if damage == "missing":
        store.delete(key)
    else:
        store.put(key, b"corrupt")

    with pytest.raises((FileNotFoundError, ValueError)):
        _publish_release(store, root)

    if damage == "missing":
        with pytest.raises(FileNotFoundError):
            _read_bytes(store, key)
    else:
        assert _read_bytes(store, key) == b"corrupt"


def test_select_keeps_current_selection_when_candidate_artifacts_are_corrupt(
    sample_catalog: Catalog, tmp_path: Path
) -> None:
    root = tmp_path / "release"
    release = build_release(sample_catalog, root)
    store = MemoryStore()
    _publish_release(store, root)
    _select_release(store, release.digest)
    current = _read_bytes(store, paths.selected())
    candidate_root = tmp_path / "candidate"
    candidate = build_release(
        Catalog.from_guidelines([], manifest=sample_catalog.manifest), candidate_root
    )
    _publish_release(store, candidate_root)
    store.put(paths.release(candidate.digest).artifact("entries.parquet"), b"corrupt")

    with pytest.raises(ValueError, match="byte count"):
        _select_release(store, candidate.digest)

    assert _read_bytes(store, paths.selected()) == current


def _read_bytes(store: Any, path: str) -> bytes:
    return bytes(store.get(path).buffer())
