from __future__ import annotations

from chartcoach import Catalog, CatalogEntry, Guideline
from chartcoach.tools.catalog import CatalogToolError, CatalogTools


def _catalog() -> Catalog:
    return Catalog(
        [
            CatalogEntry(
                guideline=Guideline(
                    id="direct-labels",
                    title="Use direct labels",
                    description="Label marks directly when space permits.",
                    body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                    labels=("chart:line", "component:label"),
                )
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="full-axis-bars",
                    title="Use full axes",
                    description="Keep bar axes honest.",
                    body="## Advice <!-- role: advice -->\n\nStart bar value axes at zero.",
                    labels=("chart:bar", "component:axis"),
                )
            ),
        ]
    )


def test_catalog_tools_support_progressive_discovery() -> None:
    tools = CatalogTools(_catalog())

    assert {"name": "guidelines", "rows": 2} in tools.relations()
    assert {
        "relation": "sections",
        "column": "role",
        "type": "String",
    } in tools.schema(relations=["sections"])
    assert tools.values("sections", "role") == [
        {"relation": "sections", "column": "role", "value": "advice", "rows": 2}
    ]


def test_catalog_tools_retrieve_and_validate_filters() -> None:
    tools = CatalogTools(_catalog())

    rows = tools.retrieve_guidelines(
        labels=["chart:line"],
        roles=["section.advice"],
    )

    assert rows[0]["id"] == "direct-labels"
    assert rows[0]["sections"] == [
        {"role": "advice", "title": "Advice", "content": "Place labels near marks."}
    ]

    try:
        tools.retrieve_guidelines(labels=["chart:missing"])
    except CatalogToolError as exc:
        assert "Unknown label" in str(exc)
        assert "guideline_labels" in str(exc)
    else:  # pragma: no cover
        raise AssertionError("expected CatalogToolError")


def test_catalog_tools_retrieve_filters_without_mutating_catalog_model() -> None:
    tools = CatalogTools(_catalog())

    assert [row["id"] for row in tools.retrieve_guidelines(labels=["chart:bar"])] == [
        "full-axis-bars"
    ]
    assert [
        row["id"] for row in tools.retrieve_guidelines(label_prefixes=["component:lab"])
    ] == ["direct-labels"]
    assert [row["id"] for row in tools.retrieve_guidelines(contains="zero")] == [
        "full-axis-bars"
    ]

    ordered = tools.retrieve_guidelines(ids=["full-axis-bars", "direct-labels"])
    assert [row["id"] for row in ordered] == ["full-axis-bars", "direct-labels"]
