from __future__ import annotations

from pathlib import Path
from typing import cast

import polars as pl
import pytest

from chartcoach.catalog import CatalogManifest
from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.entries import Guideline, Section
from catalog_testkit import deterministic_embedding


pytestmark = pytest.mark.search
_EMBEDDING = "chartcoach-search-test"


def _embedding_vector(text: str) -> list[float]:
    lowered = text.lower()
    return [
        1.0 if "direct" in lowered else 0.0,
        1.0 if "label" in lowered else 0.0,
        1.0 if "axis" in lowered else 0.0,
        1.0 if "bar" in lowered else 0.0,
    ]


def test_document_rows_have_stable_search_identity(sample_catalog: Catalog) -> None:
    from chartcoach.catalog.documents import document_rows

    frame = document_rows(sample_catalog)
    row = frame.filter(frame["id"] == "direct-labels---overview").to_dicts()[0]

    assert frame.columns == [
        "id",
        "parent_id",
        "role",
        "labels",
        "content_hash",
        "text",
    ]
    assert row["parent_id"] == "direct-labels"
    assert row["role"] == "overview"
    assert row["text"] == (
        "Use direct labels\n\nLabel marks directly when space permits."
    )
    assert len(cast(str, row["content_hash"])) == 64


def test_repeated_section_roles_have_stable_unique_document_ids(
    sample_manifest: CatalogManifest,
) -> None:
    from chartcoach.catalog.documents import document_rows

    catalog = _catalog_with_sections(
        sample_manifest,
        Section(role="advice", title="First", content="First advice."),
        Section(role="advice", title="Second", content="Second advice."),
    )

    rows = document_rows(catalog).filter(pl.col("role") == "section.advice")

    assert rows.select("id", "text").to_dicts() == [
        {"id": "repeated-role---role---advice", "text": "First advice."},
        {"id": "repeated-role---role---advice---2", "text": "Second advice."},
    ]
    assert rows.get_column("id").n_unique() == rows.height


@pytest.mark.curation
def test_open_index_returns_the_release_profile_table(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from chartcoach import open_index
    from chartcoach.catalog.curation import EmbeddingProfile, build_release

    path = tmp_path / "release"
    build_release(
        sample_catalog,
        path,
        profiles={
            "test/search": EmbeddingProfile(
                embedding=_test_embedding(),
                umap={"n_neighbors": 3},
            )
        },
    )
    opened = open_index(path, profile="test/search")

    assert opened.name == "documents"
    rows = (
        opened.search("direct labels", query_type="fts", fts_columns="text")
        .limit(1)
        .to_list()
    )
    assert rows[0]["parent_id"] == "direct-labels"


def _catalog_with_sections(
    manifest: CatalogManifest,
    *sections: Section,
) -> Catalog:
    return Catalog.from_guidelines(
        [
            Guideline(
                id="repeated-role",
                title="Repeated role",
                description="A guideline with repeated section roles.",
                sections=sections,
            )
        ],
        manifest=manifest,
    )


def _test_embedding():
    return deterministic_embedding(
        _EMBEDDING,
        lambda text, _index: _embedding_vector(text),
    )
