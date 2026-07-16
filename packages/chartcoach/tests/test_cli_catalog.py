from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

from click.testing import CliRunner
from obstore.store import MemoryStore
import pytest

from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.curation.release_builder import (
    EmbeddingProfile,
    build_catalog_release,
)
from chartcoach.catalog.curation.release_publisher import (
    publish_catalog_release,
    select_catalog_release,
)
from chartcoach.cli.main import main as chartcoach_cli
from catalog_testkit import deterministic_embedding

_PROFILE = "test/deterministic"
_EMBEDDING = "chartcoach-cli-catalog-test"


def test_catalog_overview_reports_local_content_identity(
    runner: CliRunner,
    sample_catalog_path: Path,
) -> None:
    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "overview",
            "--source",
            str(sample_catalog_path),
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0, result.output
    overview = json.loads(result.stdout)
    assert overview["source"] == str(sample_catalog_path)
    assert overview["release_digest"] is None
    assert len(overview["content_digest"]) == 64
    assert {row["name"] for row in overview["tables"]} == {
        "guidelines",
        "sections",
        "guideline_labels",
    }


def test_catalog_overview_preserves_the_resolved_release_digest(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import chartcoach.catalog.curation.cache as cache_api

    digest = "a" * 64
    bundle = sample_catalog.write_bundle(tmp_path / "bundle")
    release = SimpleNamespace(digest=digest)
    monkeypatch.setattr(
        cache_api,
        "download_catalog_bundle",
        lambda: (release, bundle),
    )

    result = runner.invoke(
        chartcoach_cli,
        ["catalog", "overview", "--format", "json"],
    )

    assert result.exit_code == 0, result.output
    overview = json.loads(result.stdout)
    assert overview["source"] == "catalog.json"
    assert overview["release_digest"] == digest


@pytest.mark.curation
def test_catalog_cache_pull_prefetches_one_profile(
    runner: CliRunner,
    sample_catalog: Catalog,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source = _published_release(sample_catalog, tmp_path)
    cache_root = tmp_path / "cache"
    import chartcoach.catalog.curation.cache as cache_api

    monkeypatch.setattr(cache_api, "artifact_store", lambda: source)
    monkeypatch.setattr(cache_api, "cache_root", lambda: cache_root)

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "cache",
            "pull",
            "--profile",
            _PROFILE,
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0, result.output
    row = json.loads(result.stdout)[0]
    assert len(row["digest"]) == 64
    assert Path(row["catalog_path"]).is_dir()
    assert (Path(row["index_path"]) / "documents.lance").is_dir()


def _published_release(catalog: Catalog, tmp_path: Path) -> MemoryStore:
    root = tmp_path / "release"
    built = build_catalog_release(
        catalog,
        root=root,
        profiles={
            _PROFILE: EmbeddingProfile(
                embedding=deterministic_embedding(_EMBEDDING),
                umap={"n_neighbors": 3},
            )
        },
    )
    source = MemoryStore()
    publish_catalog_release(source, root)
    select_catalog_release(source, built.digest)
    return source
