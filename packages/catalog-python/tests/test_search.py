from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

import pytest

from chartcoach import Catalog

pytestmark = pytest.mark.search


def test_reuse_only_requires_existing_cache_without_mutation(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("lancedb")

    from chartcoach.search import LanceIndex

    missing_cache_dir = tmp_path / "missing"

    with pytest.raises(FileNotFoundError, match="Cached LanceDB table"):
        LanceIndex.from_cache(
            sample_catalog,
            cache_dir=missing_cache_dir,
        )
    assert not missing_cache_dir.exists()


def test_search_documents_include_content_fingerprints(
    sample_catalog: Catalog,
) -> None:
    from chartcoach.search.documents import build_docs_df

    docs = build_docs_df(sample_catalog.guidelines(), sample_catalog.references())
    metadata_by_id = {
        str(row["id"]): row["metadata"]
        for row in docs.select("id", "metadata").to_dicts()
    }

    overview_hash = metadata_by_id["direct-labels---overview"]["content_hash"]
    document_hash = metadata_by_id["direct-labels---document"]["content_hash"]
    advice_hash = metadata_by_id["direct-labels---role---advice"]["content_hash"]

    assert isinstance(overview_hash, str)
    assert isinstance(document_hash, str)
    assert isinstance(advice_hash, str)
    assert overview_hash
    assert len({overview_hash, document_hash, advice_hash}) == 3


def test_reuse_or_create_builds_content_addressed_lancedb_table(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("lancedb")

    from chartcoach.search import LanceIndex

    cache_dir = tmp_path / "index"
    paths = LanceIndex.cache_paths(sample_catalog, cache_dir=cache_dir)
    index = LanceIndex.from_cache(
        sample_catalog,
        cache_dir=cache_dir,
        cache_mode="reuse_or_create",
    )

    assert cache_dir.exists()
    assert index.index_root == paths.index_root
    assert index.document_count() == 6
    assert index.table_name == "catalog_documents"
    assert index.table_path == paths.table_path
    assert index.table_path.exists()
    assert paths.manifest_path.exists()

    rows = index.query_documents("direct labels", limit=2)
    assert rows
    assert {row["parent_id"] for row in rows} <= {"direct-labels", "full-axis-bars"}
    assert all(row["doc"] for row in rows)


def test_reuse_only_rejects_cache_manifest_mismatch(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("lancedb")

    from chartcoach.search import LanceIndex

    cache_dir = tmp_path / "index"
    index = LanceIndex.from_cache(
        sample_catalog,
        cache_dir=cache_dir,
        cache_mode="reuse_or_create",
    )
    paths = LanceIndex.cache_paths(sample_catalog, cache_dir=cache_dir)
    assert index.index_root == paths.index_root
    manifest = json.loads(paths.manifest_path.read_text(encoding="utf-8"))
    manifest["catalog_digest"] = "wrong"
    paths.manifest_path.write_text(
        json.dumps(manifest),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="catalog_digest"):
        LanceIndex.from_cache(
            sample_catalog,
            cache_dir=cache_dir,
            cache_mode="reuse_only",
        )


def test_reuse_only_rejects_table_count_mismatch(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("lancedb")

    from chartcoach.search import LanceIndex

    cache_dir = tmp_path / "index"
    index = LanceIndex.from_cache(
        sample_catalog,
        cache_dir=cache_dir,
        cache_mode="reuse_or_create",
    )
    index.table.delete("id = 'direct-labels---overview'")

    with pytest.raises(ValueError, match="row count"):
        LanceIndex.from_cache(
            sample_catalog,
            cache_dir=cache_dir,
            cache_mode="reuse_only",
        )


def test_reuse_or_create_rebuilds_table_count_mismatch(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("lancedb")

    from chartcoach.search import LanceIndex

    cache_dir = tmp_path / "index"
    index = LanceIndex.from_cache(
        sample_catalog,
        cache_dir=cache_dir,
        cache_mode="reuse_or_create",
    )
    index.table.delete("id = 'direct-labels---overview'")

    rebuilt = LanceIndex.from_cache(
        sample_catalog,
        cache_dir=cache_dir,
        cache_mode="reuse_or_create",
    )

    assert rebuilt.document_count() == 6


def test_cached_lance_paths_are_public_without_creating_cache(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    from chartcoach.search import LanceIndex

    cache_dir = tmp_path / "index"
    paths = LanceIndex.cache_paths(sample_catalog, cache_dir=cache_dir)

    assert not cache_dir.exists()
    assert (
        paths.index_root
        == cache_dir / sample_catalog.digest() / paths.documents_version
    )
    assert paths.table_name == "catalog_documents"
    assert paths.table_path == paths.index_root / "catalog_documents.lance"
    assert paths.manifest_path == paths.index_root / "_chartcoach_index.json"


def test_query_documents_accepts_lancedb_filter(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("lancedb")

    from chartcoach.search import LanceIndex

    index = LanceIndex.from_cache(
        sample_catalog,
        cache_dir=tmp_path / "index",
        cache_mode="reuse_or_create",
    )

    rows = index.query_documents(
        "bars",
        limit=5,
        where="parent_id = 'full-axis-bars'",
    )

    assert rows
    assert {row["parent_id"] for row in rows} == {"full-axis-bars"}


def test_lance_queries_reject_empty_query_and_invalid_limits(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("lancedb")

    from chartcoach.search import LanceIndex, search_guidelines

    index = LanceIndex.from_cache(
        sample_catalog,
        cache_dir=tmp_path / "index",
        cache_mode="reuse_or_create",
    )

    with pytest.raises(ValueError, match="query must be a non-empty string"):
        index.query_documents(" ")
    with pytest.raises(ValueError, match="limit must be at least 1"):
        index.query_documents("axis", limit=0)
    with pytest.raises(ValueError, match="query_text must be a non-empty string"):
        search_guidelines(index, " ")
    with pytest.raises(ValueError, match="limit must be at least 1"):
        search_guidelines(index, "axis", limit=0)
    with pytest.raises(ValueError, match="candidate_limit must be at least 1"):
        search_guidelines(index, "axis", candidate_limit=0)


def test_search_guidelines_returns_guideline_level_hits(
    tmp_path: Path,
    sample_catalog: Catalog,
) -> None:
    pytest.importorskip("lancedb")

    from chartcoach.search import LanceIndex, search_guidelines

    index = LanceIndex.from_cache(
        sample_catalog,
        cache_dir=tmp_path / "index",
        cache_mode="reuse_or_create",
    )

    result = search_guidelines(
        index,
        "direct labels",
        limit=1,
        where="role = 'overview'",
    )

    assert result.row_count == 1
    assert result.rows[0].guideline_id == "direct-labels"
    assert result.rows[0].title == "Use direct labels"
    assert result.rows[0].document
    assert result.rows[0].score is not None
    assert result.to_dict()["rows"][0]["id"] == "direct-labels"
    assert result.to_dict()["where"] == "role = 'overview'"


def test_search_guidelines_backfills_unique_guideline_rows(
    sample_catalog: Catalog,
) -> None:
    from chartcoach.search import search_guidelines

    class FakeIndex:
        catalog = sample_catalog

        def document_count(self) -> int:
            return 100

        def query_documents(
            self,
            query: str,
            *,
            limit: int,
            where: str | None = None,
        ) -> list[dict[str, object]]:
            if where != "role = 'overview'":
                return []
            if limit < 100:
                return [
                    {
                        "id": "direct-labels---overview",
                        "parent_id": "direct-labels",
                        "role": "overview",
                        "labels": ["chart:line"],
                        "doc": "Overview text",
                        "_score": 1.3,
                    },
                    {
                        "id": "direct-labels---section.advice",
                        "parent_id": "direct-labels",
                        "role": "section.advice",
                        "labels": ["chart:line"],
                        "doc": "Advice text",
                        "_score": 0.9,
                    },
                ]
            return [
                {
                    "id": "direct-labels---overview",
                    "parent_id": "direct-labels",
                    "role": "overview",
                    "labels": ["chart:line"],
                    "doc": "Overview text",
                    "_score": 1.3,
                },
                {
                    "id": "full-axis-bars---overview",
                    "parent_id": "full-axis-bars",
                    "role": "overview",
                    "labels": ["chart:bar"],
                    "doc": "Axis text",
                    "_score": 0.8,
                },
            ]

    result = search_guidelines(
        cast(Any, FakeIndex()),
        "axis labels",
        limit=2,
        candidate_limit=100,
        where="role = 'overview'",
    )

    assert [row.guideline_id for row in result.rows] == [
        "direct-labels",
        "full-axis-bars",
    ]
    assert result.candidate_limit == 100


def test_search_guidelines_treats_candidate_limit_as_maximum(
    sample_catalog: Catalog,
) -> None:
    from chartcoach.search import search_guidelines

    class FakeIndex:
        catalog = sample_catalog

        def document_count(self) -> int:
            return 100

        def query_documents(
            self,
            query: str,
            *,
            limit: int,
            where: str | None = None,
        ) -> list[dict[str, object]]:
            rows: list[dict[str, object]] = [
                {
                    "id": "direct-labels---overview",
                    "parent_id": "direct-labels",
                    "role": "overview",
                    "labels": ["chart:line"],
                    "doc": "Overview text",
                    "_score": 1.3,
                },
                {
                    "id": "full-axis-bars---overview",
                    "parent_id": "full-axis-bars",
                    "role": "overview",
                    "labels": ["chart:bar"],
                    "doc": "Axis text",
                    "_score": 0.8,
                },
            ]
            return rows[:limit]

    result = search_guidelines(
        cast(Any, FakeIndex()),
        "axis labels",
        limit=8,
        candidate_limit=1,
    )

    assert result.row_count == 1
    assert result.rows[0].guideline_id == "direct-labels"
    assert result.candidate_limit == 1


def test_search_guidelines_rejects_malformed_index_rows(
    sample_catalog: Catalog,
) -> None:
    from chartcoach.search import search_guidelines

    class FakeIndex:
        catalog = sample_catalog

        def document_count(self) -> int:
            return 1

        def query_documents(
            self,
            query: str,
            *,
            limit: int,
            where: str | None = None,
        ) -> list[dict[str, object]]:
            return [
                {"id": "document-without-parent", "role": "overview", "doc": "Text"}
            ]

    with pytest.raises(ValueError, match="parent_id"):
        search_guidelines(cast(Any, FakeIndex()), "axis")
