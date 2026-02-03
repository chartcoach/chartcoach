from __future__ import annotations

import pytest

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.retrieval.strategy.pipelines.label_hints import (
    match_catalog_ids_by_label_hints,
)


@pytest.fixture()
def catalog() -> Catalog:
    return Catalog(
        entries=[
            CatalogEntry(
                guideline=Guideline(
                    id="g1",
                    title="Use accessible colors",
                    description="Ensure color choices are accessible.",
                    labels=["topic:color", "audience:general"],
                    body="## Advice <!-- role: advice -->\nUse colorblind-safe palettes.\n",
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g2",
                    title="Label axes clearly",
                    description="Axis labels should be clear.",
                    labels=["topic:annotation"],
                    body="## Advice <!-- role: advice -->\nAdd axis titles.\n",
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g3",
                    title="Add context annotations",
                    description="Add context to avoid misinterpretation.",
                    labels=["topic:annotation", "impact:credibility"],
                    body="## Advice <!-- role: advice -->\nAdd context notes.\n",
                ),
                references=[],
            ),
        ]
    )


def test_match_catalog_ids_by_label_hints_handles_exact_and_fuzzy_matches(
    catalog: Catalog,
) -> None:
    ids, matched = match_catalog_ids_by_label_hints(
        catalog=catalog, label_hints=["topic:annotation"]
    )
    assert ids == {"g2", "g3"}
    assert "topic:annotation" in matched

    ids, matched = match_catalog_ids_by_label_hints(
        catalog=catalog, label_hints=["annotation"]
    )
    assert ids == {"g2", "g3"}
    assert matched


def test_match_catalog_ids_by_label_hints_ignores_empty_hints_and_empty_labels() -> (
    None
):
    empty = Catalog(
        entries=[
            CatalogEntry(
                guideline=Guideline(
                    id="g0",
                    title="No labels",
                    description="",
                    labels=[],
                    body="## Advice <!-- role: advice -->\nText.\n",
                ),
                references=[],
            )
        ]
    )

    ids, matched = match_catalog_ids_by_label_hints(
        catalog=empty, label_hints=["topic:annotation"]
    )
    assert ids == set()
    assert matched == {"topic:annotation": []}

    ids, matched = match_catalog_ids_by_label_hints(catalog=empty, label_hints=[" "])
    assert ids == set()
    assert matched == {}
