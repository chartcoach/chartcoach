from __future__ import annotations

from pathlib import Path

import pytest

from chartcoach import Catalog, CatalogEntry, Guideline, Section
from chartcoach.tools.catalog import CatalogToolError, CatalogTools


def test_catalog_tools_support_progressive_discovery(sample_catalog: Catalog) -> None:
    tools = CatalogTools(sample_catalog)

    assert {"name": "guidelines", "columns": 7, "rows": None} in tools.list_tables()
    assert {
        "name": "guideline_sources",
        "columns": 14,
        "rows": None,
    } in tools.list_tables()
    assert {"name": "guidelines", "rows": 2} in tools.list_tables(
        include_row_counts=True
    )
    assert {
        "table": "sections",
        "column": "role",
        "type": "String",
    } in tools.describe_tables(tables=["sections"])


def test_catalog_tools_retrieve_and_validate_filters(sample_catalog: Catalog) -> None:
    tools = CatalogTools(sample_catalog)

    rows = tools.retrieve_guidelines(
        labels=["chart:line"],
        roles=["advice"],
    )

    assert rows[0]["id"] == "direct-labels"
    assert rows[0]["sections"] == [
        {"role": "advice", "title": "Advice", "content": "Place labels near marks."}
    ]

    with pytest.raises(CatalogToolError, match="Unknown label") as exc_info:
        tools.retrieve_guidelines(labels=["chart:missing"])
    assert "guideline_labels" in str(exc_info.value)


@pytest.mark.parametrize(
    ("method", "kwargs", "expected_ids"),
    [
        ("retrieve_guidelines", {"labels": ["chart:bar"]}, ["full-axis-bars"]),
        (
            "retrieve_guidelines",
            {"label_prefixes": ["component:lab"]},
            ["direct-labels"],
        ),
        (
            "list_guidelines",
            {"label_prefixes": ["component:lab"]},
            ["direct-labels"],
        ),
        ("retrieve_guidelines", {"contains": "zero"}, ["full-axis-bars"]),
    ],
)
def test_catalog_tools_filter_guidelines(
    sample_catalog: Catalog,
    method: str,
    kwargs: dict[str, object],
    expected_ids: list[str],
) -> None:
    tools = CatalogTools(sample_catalog)

    rows = getattr(tools, method)(**kwargs)

    assert [row["id"] for row in rows] == expected_ids


def test_catalog_tools_preserve_explicit_id_order(sample_catalog: Catalog) -> None:
    tools = CatalogTools(sample_catalog)

    ordered = tools.retrieve_guidelines(ids=["full-axis-bars", "direct-labels"])
    assert [row["id"] for row in ordered] == ["full-axis-bars", "direct-labels"]


def test_catalog_discovery_does_not_parse_unrelated_references() -> None:
    catalog = Catalog.from_entries(
        [
            CatalogEntry(
                guideline=Guideline(
                    id="bad-reference",
                    title="Title",
                    description="Description",
                    body="## Advice <!-- role: advice -->\n\nUse direct labels.",
                    labels=("chart:bar",),
                    sections=(
                        Section(
                            role="advice",
                            title="Advice",
                            content="Use direct labels.",
                        ),
                    ),
                ),
                references=("not valid bibtex",),
            )
        ]
    )
    tools = CatalogTools(catalog)

    assert tools.describe_tables(tables=["guideline_labels"])
    assert tools.count_values("guideline_labels", "label") == [
        {
            "table": "guideline_labels",
            "column": "label",
            "value": "chart:bar",
            "rows": 1,
        }
    ]


def test_catalog_tools_sql_query_returns_bounded_rows(
    sample_catalog: Catalog,
) -> None:
    result = CatalogTools(sample_catalog).sql_query(
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
    "query",
    [
        "create table x as select 1",
        "select 1; select 2",
    ],
)
def test_catalog_tools_sql_query_rejects_non_read_only_queries(
    sample_catalog: Catalog,
    query: str,
) -> None:
    with pytest.raises(CatalogToolError):
        CatalogTools(sample_catalog).sql_query(query)


def test_catalog_tools_sql_query_disables_external_file_access(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    external_csv = tmp_path / "external.csv"
    external_csv.write_text("x\n1\n")

    with pytest.raises(CatalogToolError, match="Cannot access file"):
        CatalogTools(sample_catalog).sql_query(
            f"select * from read_csv_auto({external_csv.as_posix()!r})"
        )
