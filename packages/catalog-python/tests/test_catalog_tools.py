from __future__ import annotations

from pathlib import Path
from typing import cast

import pytest

from chartcoach import Catalog
from chartcoach.tools import ToolError, Tools


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
        {"name": "id", "type": "String"},
        {"name": "title", "type": "String"},
    ]
    assert result["rows"] == [{"id": "direct-labels", "title": "Use direct labels"}]
    assert result["row_count"] == 1
    assert result["truncated"] is True
    assert result["limit"] == 1
    assert result["catalog_digest"] == sample_catalog.digest()


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
    from chartcoach.search import index

    table = index(sample_catalog, tmp_path / "index")
    result = Tools(
        sample_catalog,
        table=table,
        index_path=tmp_path / "index",
    ).search(
        "direct labels",
        limit=2,
        where="role = 'overview'",
        mode="fts",
    )

    rows = cast(list[dict[str, object]], result["rows"])
    assert rows == [
        {
            "_score": rows[0]["_score"],
            "id": "direct-labels---overview",
            "parent_id": "direct-labels",
            "role": "overview",
            "labels": ["chart:line", "component:label", "task:lookup"],
            "content_hash": rows[0]["content_hash"],
            "text": "Use direct labels\n\nLabel marks directly when space permits.",
        }
    ]
    assert result["mode"] == "fts"
    assert result["table_name"] == "catalog_documents"


@pytest.mark.search
def test_tools_search_requires_explicit_table(sample_catalog: Catalog) -> None:
    with pytest.raises(ToolError, match="LanceDB table is required"):
        Tools(sample_catalog).search("direct labels")
