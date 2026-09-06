from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
from catalog_testkit import deterministic_embedding
from chartcoach.catalog.curation import (
    EmbeddingProfile,
    build_release,
    publish_release,
    select_release,
)
from chartcoach.catalog.curation.release_publisher import (
    _publish_release,
    _select_release,
)
from chartcoach.catalog.model import Catalog
from chartcoach.catalog.paths import paths
from chartcoach.catalog.releases import CatalogRelease
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


def _read_bytes(store: Any, path: str) -> bytes:
    return bytes(store.get(path).buffer())
