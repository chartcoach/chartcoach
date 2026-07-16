from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from obstore.store import LocalStore, MemoryStore
import pytest

from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.curation.release_builder import build_catalog_release
from chartcoach.catalog.curation.release_publisher import (
    publish_catalog_release,
    select_catalog_release,
)
from chartcoach.catalog.paths import paths
from chartcoach.catalog.releases import CatalogRelease


pytestmark = pytest.mark.curation


@pytest.mark.parametrize("store_kind", ["memory", "local"])
def test_publish_and_select_release_by_digest(
    sample_catalog: Catalog,
    tmp_path: Path,
    store_kind: str,
) -> None:
    root = tmp_path / "release"
    release = build_catalog_release(sample_catalog, root=root)
    store = (
        MemoryStore()
        if store_kind == "memory"
        else LocalStore(tmp_path / "objects", mkdir=True)
    )

    published = publish_catalog_release(store, root)
    selected = select_catalog_release(store, release.digest)

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
    release = build_catalog_release(sample_catalog, root=root)
    store = MemoryStore()
    artifact_path = "entries.parquet"
    object_path = paths.release(release.digest).artifact(artifact_path)
    store.put(object_path, b"partial")

    publish_catalog_release(store, root)

    assert _read_bytes(store, object_path) == (root / artifact_path).read_bytes()


def test_publish_is_idempotent_after_release_commit(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    build_catalog_release(sample_catalog, root=root)
    store = MemoryStore()

    first = publish_catalog_release(store, root)
    second = publish_catalog_release(store, root)

    assert second == first


def test_select_keeps_the_current_release_when_digest_is_missing(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    root = tmp_path / "release"
    release = build_catalog_release(sample_catalog, root=root)
    store = MemoryStore()
    publish_catalog_release(store, root)
    select_catalog_release(store, release.digest)
    current = _read_bytes(store, paths.selected())

    with pytest.raises(FileNotFoundError):
        select_catalog_release(store, "0" * 64)

    assert _read_bytes(store, paths.selected()) == current


def _read_bytes(store: Any, path: str) -> bytes:
    return bytes(store.get(path).buffer())
