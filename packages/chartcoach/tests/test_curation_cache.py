from __future__ import annotations

from pathlib import Path
import shutil

from obstore.store import LocalStore, MemoryStore
import pytest

from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.curation.cache import (
    cache_catalog_bundle,
    cache_index_artifact,
)
from chartcoach.catalog.curation.release_builder import (
    EmbeddingProfile,
    build_catalog_release,
)
from chartcoach.catalog.curation.release_publisher import (
    publish_catalog_release,
    select_catalog_release,
)
from chartcoach.catalog.paths import paths
from chartcoach.catalog.releases import CatalogRelease
from catalog_testkit import deterministic_embedding


pytestmark = pytest.mark.curation
_PROFILE = "test/deterministic"
_EMBEDDING = "chartcoach-cache-test"


def test_core_pull_caches_the_manifest_and_entries(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    published, source = _published_release(sample_catalog, tmp_path)
    root = tmp_path / "cache"
    cache = LocalStore(root, mkdir=True)

    release, bundle = cache_catalog_bundle(source, cache, root)

    assert release == published
    assert bundle == root / paths.release(release.digest).root()
    assert (bundle / "MANIFEST.md").is_file()
    assert (bundle / "entries.parquet").is_file()


def test_completion_marker_reuses_an_exact_cached_bundle(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    published, source = _published_release(sample_catalog, tmp_path)
    root = tmp_path / "cache"
    cache = LocalStore(root, mkdir=True)
    cache_catalog_bundle(source, cache, root, reference=published.digest)

    release, bundle = cache_catalog_bundle(
        MemoryStore(),
        cache,
        root,
        reference=published.digest,
    )

    assert release == published
    assert (bundle / "entries.parquet").is_file()


def test_profile_pull_reuses_a_usable_native_index(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    published, source = _published_release(sample_catalog, tmp_path, profile=True)
    root = tmp_path / "cache"
    cache = LocalStore(root, mkdir=True)
    first = cache_index_artifact(
        source,
        cache,
        root,
        reference=published.digest,
        profile=_PROFILE,
    )

    second = cache_index_artifact(
        MemoryStore(),
        cache,
        root,
        reference=published.digest,
        profile=_PROFILE,
    )

    assert second == first
    assert (second / "documents.lance").is_dir()


def test_profile_pull_replaces_an_unusable_marked_index(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    published, source = _published_release(sample_catalog, tmp_path, profile=True)
    root = tmp_path / "cache"
    cache = LocalStore(root, mkdir=True)
    index = cache_index_artifact(
        source,
        cache,
        root,
        reference=published.digest,
        profile=_PROFILE,
    )
    shutil.rmtree(index / "documents.lance")

    repaired = cache_index_artifact(
        source,
        cache,
        root,
        reference=published.digest,
        profile=_PROFILE,
    )

    assert repaired == index
    assert (repaired / "documents.lance").is_dir()


def _published_release(
    catalog: Catalog,
    tmp_path: Path,
    *,
    profile: bool = False,
) -> tuple[CatalogRelease, MemoryStore]:
    profiles = (
        {
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding(_EMBEDDING),
                umap={"n_neighbors": 3},
            )
        }
        if profile
        else {}
    )
    root = tmp_path / ("profile-release" if profile else "core-release")
    release = build_catalog_release(
        catalog,
        root=root,
        profiles=profiles,
    )
    source = MemoryStore()
    publish_catalog_release(source, root)
    select_catalog_release(source, release.digest)
    return release, source
