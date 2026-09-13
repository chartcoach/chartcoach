from __future__ import annotations

import math
from pathlib import Path
from typing import TYPE_CHECKING, Literal, cast

import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import Catalog, open_catalog

if TYPE_CHECKING:
    from lancedb.query import LanceHybridQueryBuilder, LanceVectorQueryBuilder

pytestmark = [pytest.mark.curation, pytest.mark.search]


@pytest.fixture(scope="module")
def indexed_catalog(tmp_path_factory: pytest.TempPathFactory) -> Catalog:
    from chartcoach.curation import EmbeddingProfile, build_release

    source = Path(__file__).parents[3] / "fixtures" / "catalog-release"
    destination = tmp_path_factory.mktemp("agent-search") / "release"
    build_release(
        open_catalog(source),
        destination,
        profiles={
            "example": EmbeddingProfile(
                deterministic_embedding(
                    "chartcoach-agent-example",
                    lambda text, _index: (
                        float("direct" in text.lower()),
                        float("label" in text.lower()),
                        1.0,
                        1.0,
                    ),
                )
            )
        },
    )
    return open_catalog(destination)


@pytest.mark.parametrize(
    ("mode", "score"),
    [("fts", "_score"), ("vector", "_distance"), ("hybrid", "_relevance_score")],
)
def test_projected_native_hits_keep_scores_and_readable_parent_guidelines(
    indexed_catalog: Catalog, mode: Literal["fts", "vector", "hybrid"], score: str
) -> None:
    catalog = indexed_catalog
    table = catalog.index("example")
    query = table.search("direct labels", query_type=mode, fts_columns="text")
    if mode != "fts":
        metadata = catalog.describe(profile="example")["profile"]
        assert metadata is not None
        query = cast(
            "LanceVectorQueryBuilder | LanceHybridQueryBuilder", query
        ).distance_type(metadata["distance_metric"])
    columns = ["id", "parent_id", "role"]
    if mode != "hybrid":
        columns.append(score)
    hits = query.select(columns).limit(5).to_list()
    ids = list(dict.fromkeys(hit["parent_id"] for hit in hits))
    records = catalog.read(ids=ids)
    citations = catalog.cite(ids=ids)

    assert 1 <= len(hits) <= 5
    assert all(set(hit) == {"id", "parent_id", "role", score} for hit in hits)
    assert all(math.isfinite(hit[score]) for hit in hits)
    assert [record["id"] for record in records] == ids
    assert [citation["id"] for citation in citations] == ids
    assert all(record["sections"] for record in records)
    assert all(citation["sources"] for citation in citations)
