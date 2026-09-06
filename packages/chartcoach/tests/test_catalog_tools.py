from __future__ import annotations

from pathlib import Path
from typing import cast

import pytest

from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.releases import CatalogRelease, ReleaseArtifact
from chartcoach.catalog.releases.hashing import release_digest
from chartcoach.tools import ToolError, Tools
from catalog_testkit import deterministic_embedding


def test_tools_sql_returns_bounded_rows(sample_catalog: Catalog) -> None:
    result = Tools(sample_catalog).sql(
        """
        select id, title
        from guidelines
        order by id
        """,
        limit=1,
    )

    assert result["columns"] == [
        {"name": "id", "type": "VARCHAR"},
        {"name": "title", "type": "VARCHAR"},
    ]
    assert result["rows"] == [{"id": "direct-labels", "title": "Use direct labels"}]
    assert result["row_count"] == 1
    assert result["truncated"] is True
    assert result["limit"] == 1
    assert result["content_digest"] == sample_catalog.content_digest()


def test_tools_preserve_published_release_identity(sample_catalog: Catalog) -> None:
    catalog = _released_catalog(sample_catalog)
    assert catalog.release is not None

    result = Tools(catalog).sql("select 1 as value")

    assert result["release_digest"] == catalog.release.digest


def test_tools_sql_returns_json_values(sample_catalog: Catalog) -> None:
    result = Tools(sample_catalog).sql(
        "select date '2026-07-11' as day, 1.25::decimal(4, 2) as value"
    )

    assert result["rows"] == [{"day": "2026-07-11", "value": "1.25"}]


@pytest.mark.parametrize(
    "statement",
    [
        "create table x as select 1",
        "select 1; select 2",
    ],
)
def test_tools_sql_rejects_non_read_only_queries(
    sample_catalog: Catalog,
    statement: str,
) -> None:
    with pytest.raises(ToolError):
        Tools(sample_catalog).sql(statement)


def test_tools_sql_disables_external_file_access(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    external_csv = tmp_path / "external.csv"
    external_csv.write_text("x\n1\n")

    with pytest.raises(ToolError, match="Cannot access file"):
        Tools(sample_catalog).sql(
            f"select * from read_csv_auto({external_csv.as_posix()!r})"
        )


@pytest.mark.search
def test_tools_search_uses_configured_lancedb_table(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from chartcoach.catalog.curation.lancedb_index import build_lancedb_index

    table = build_lancedb_index(
        sample_catalog,
        tmp_path / "index",
        embedding=deterministic_embedding("chartcoach-tools-test"),
    )
    result = Tools(
        sample_catalog,
        table=table,
        source=tmp_path / "release",
        profile="test/deterministic",
    ).search(
        "direct labels",
        limit=2,
        where="role = 'overview'",
        mode="fts",
    )

    rows = cast(list[dict[str, object]], result["rows"])
    assert len(rows) == 1
    row = rows[0]
    assert row["id"] == "direct-labels"
    assert row["matched_document_id"] == "direct-labels---overview"
    assert row["matched_role"] == "overview"
    assert row["labels"] == ["chart:line", "component:label", "task:lookup"]
    assert (
        row["matched_text"]
        == "Use direct labels\n\nLabel marks directly when space permits."
    )
    assert isinstance(row["score"], float)
    assert result["mode"] == "fts"
    assert result["source"] == str(tmp_path / "release")
    assert result["profile"] == "test/deterministic"


@pytest.mark.search
def test_tools_search_requires_explicit_table(sample_catalog: Catalog) -> None:
    with pytest.raises(ToolError, match="LanceDB table is required"):
        Tools(sample_catalog).search("direct labels")


def _released_catalog(catalog: Catalog) -> Catalog:
    artifacts = {
        "MANIFEST.md": ReleaseArtifact("1" * 64, 1),
        "entries.parquet": ReleaseArtifact("2" * 64, 1),
    }
    release = CatalogRelease(
        digest=release_digest(artifacts),
        artifacts=artifacts,
    )
    return Catalog(
        catalog.to_frame(),
        manifest=catalog.manifest,
        release=release,
    )
