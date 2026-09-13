from __future__ import annotations

import json
import shutil
from pathlib import Path

import polars as pl
import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import Catalog, CatalogError, open_catalog
from chartcoach._catalog.releases import CatalogRelease
from chartcoach._catalog.search import catalog_search
from chartcoach.curation import EmbeddingProfile, build_release

pytestmark = [pytest.mark.curation, pytest.mark.search]
_PROFILE = "test-deterministic"
_EMBEDDING = "chartcoach-runtime-index-test"


def test_native_index_and_parquet_composition_from_an_offline_release(
    sample_catalog: Catalog, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "chartcoach._catalog.runtime.cache._cache_root", lambda: tmp_path / "cache"
    )
    root = tmp_path / "release"
    build_release(
        sample_catalog,
        root,
        profiles={
            _PROFILE: EmbeddingProfile(
                deterministic_embedding("chartcoach-native-composition"),
                export_documents=True,
            )
        },
    )
    cached = open_catalog(root).cache()
    shutil.rmtree(root)
    catalog = open_catalog(cached)
    table = catalog.index(_PROFILE)
    hits = (
        table.search("labels", query_type="fts", fts_columns="text").limit(10).to_list()
    )
    ids = list(dict.fromkeys(hit["parent_id"] for hit in hits))
    assert catalog.read(ids=ids)[0]["id"] == "direct-labels"
    documents = catalog.artifact(f"profiles/{_PROFILE}/documents.parquet")
    with catalog.duckdb() as connection:
        connection.read_parquet(str(documents)).create_view("documents")
        assert connection.sql(
            "select distinct g.id from guidelines g join documents d on d.parent_id = g.id order by g.id"
        ).fetchall() == [("direct-labels",), ("full-axis-bars",)]


def test_catalog_index_reuses_one_protected_generation(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_root, release = _profile_release(sample_catalog, tmp_path)
    cache = tmp_path / "cache"
    monkeypatch.setattr("chartcoach._catalog.runtime.cache._cache_root", lambda: cache)

    first = open_catalog(release_root).index(_PROFILE)
    second = open_catalog(release_root / "release.json").index(_PROFILE)
    artifact = release.artifact(f"profiles/{_PROFILE}/index.tar.gz")
    root = cache / "indexes-v2" / artifact.sha256
    generations = list((root / "generations").iterdir())

    assert (
        first.count_rows() == second.count_rows() == sample_catalog.documents().height
    )
    assert len(generations) == 1
    assert generations[0].stat().st_mode & 0o222 == 0
    assert json.loads((root / "current.json").read_text())["digest"] == artifact.sha256


def test_shared_index_blocks_writes_after_deliberate_unpinning(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_root, _ = _profile_release(sample_catalog, tmp_path)
    monkeypatch.setattr(
        "chartcoach._catalog.runtime.cache._cache_root", lambda: tmp_path / "cache"
    )
    table = open_catalog(release_root).index(_PROFILE)

    table.checkout_latest()
    with pytest.raises((OSError, RuntimeError, ValueError)):
        table.delete("true")

    assert (
        open_catalog(release_root).index(_PROFILE).count_rows()
        == sample_catalog.documents().height
    )


def test_index_repair_publishes_a_new_generation(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_root, release = _profile_release(sample_catalog, tmp_path)
    cache = tmp_path / "cache"
    monkeypatch.setattr("chartcoach._catalog.runtime.cache._cache_root", lambda: cache)
    open_catalog(release_root).index(_PROFILE)
    artifact = release.artifact(f"profiles/{_PROFILE}/index.tar.gz")
    root = cache / "indexes-v2" / artifact.sha256
    first = _current_generation(root)
    _make_writable(first)
    for manifest in (first / "documents.lance").rglob("*.manifest"):
        manifest.unlink()
    _make_read_only(first)

    repaired = open_catalog(release_root).index(_PROFILE)
    second = _current_generation(root)

    assert repaired.count_rows() == sample_catalog.documents().height
    assert second != first
    assert first.exists()
    assert len(list((root / "generations").iterdir())) == 2


def test_catalog_index_lists_available_profiles(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release_root = tmp_path / "release"
    build_release(sample_catalog, release_root)

    with pytest.raises(CatalogError, match="Available profiles: none"):
        open_catalog(release_root).index("missing")


def test_catalog_index_rejects_a_symlinked_artifact_parent(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    release_root, _ = _profile_release(sample_catalog, tmp_path)
    profile_root = release_root / "profiles" / _PROFILE
    outside = tmp_path / "outside"
    profile_root.rename(outside)
    profile_root.symlink_to(outside, target_is_directory=True)

    with pytest.raises(CatalogError, match="Catalog artifact is missing"):
        open_catalog(release_root).index(_PROFILE)


def test_caller_owned_index_directory_is_writable_and_isolated(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_root, _ = _profile_release(sample_catalog, tmp_path)
    monkeypatch.setattr(
        "chartcoach._catalog.runtime.cache._cache_root", lambda: tmp_path / "cache"
    )
    catalog = open_catalog(release_root)
    directory = tmp_path / "writable-index"

    table = catalog.index(_PROFILE, directory=directory)
    table.delete("true")

    assert table.count_rows() == 0
    assert catalog.index(_PROFILE).count_rows() == sample_catalog.documents().height
    with pytest.raises(FileExistsError):
        catalog.index(_PROFILE, directory=directory)


def test_non_posix_public_index_requires_a_caller_owned_directory(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_root, _ = _profile_release(sample_catalog, tmp_path)
    cache = tmp_path / "cache"
    monkeypatch.setattr("chartcoach._catalog.runtime.cache._cache_root", lambda: cache)
    monkeypatch.setattr(
        "chartcoach._catalog.runtime.profiles.shared_index_cache_supported",
        lambda: False,
    )
    catalog = open_catalog(release_root)

    with pytest.raises(CatalogError, match="caller-owned directory") as exc_info:
        catalog.index(_PROFILE)

    assert exc_info.value.code == "unavailable_capability"
    assert catalog_search(catalog, "direct labels", profile=_PROFILE, mode="fts")[
        "matches"
    ]


def test_open_catalog_keeps_profile_loads_on_the_resolved_selection(
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    first_root, first_release = _profile_release(sample_catalog, tmp_path / "first")
    changed = Catalog(
        sample_catalog.to_frame().with_columns(
            pl.when(pl.col("id") == "direct-labels")
            .then(pl.lit("Changed title"))
            .otherwise(pl.col("title"))
            .alias("title")
        ),
        manifest=sample_catalog.manifest,
    )
    second_root, second_release = _profile_release(changed, tmp_path / "second")
    store = tmp_path / "store"
    releases = store / "catalog" / "releases"
    releases.mkdir(parents=True)
    shutil.copytree(first_root, releases / first_release.digest)
    shutil.copytree(second_root, releases / second_release.digest)
    selection = store / "catalog.json"
    selection.write_text(json.dumps(first_release.to_record()))
    monkeypatch.setattr(
        "chartcoach._catalog.runtime.cache._cache_root", lambda: tmp_path / "cache"
    )
    monkeypatch.chdir(store)
    catalog = open_catalog(".")
    selection.write_text(json.dumps(second_release.to_record()))
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    monkeypatch.chdir(elsewhere)

    assert catalog.release == first_release
    assert catalog.read(ids=["direct-labels"], source_detail="none")[0]["title"] == (
        "Use direct labels"
    )
    assert catalog.index(_PROFILE).count_rows() == sample_catalog.documents().height
    assert catalog.describe()["resolved_location"] == str(
        releases / first_release.digest / "release.json"
    )

    selected = open_catalog(selection)
    assert selected.release == second_release
    assert selected.read(ids=["direct-labels"], source_detail="none")[0]["title"] == (
        "Changed title"
    )


def _profile_release(catalog: Catalog, tmp_path: Path) -> tuple[Path, CatalogRelease]:
    root = tmp_path / "release"
    release = build_release(
        catalog,
        root,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding(_EMBEDDING),
            )
        },
    )
    return root, release


def _current_generation(root: Path) -> Path:
    current = json.loads((root / "current.json").read_text())
    return root / "generations" / current["generation"]


def _make_writable(root: Path) -> None:
    root.chmod(0o755)
    for path in root.rglob("*"):
        path.chmod(0o755 if path.is_dir() else 0o644)


def _make_read_only(root: Path) -> None:
    for path in sorted(root.rglob("*"), key=lambda item: len(item.parts), reverse=True):
        path.chmod(0o555 if path.is_dir() else 0o444)
    root.chmod(0o555)
