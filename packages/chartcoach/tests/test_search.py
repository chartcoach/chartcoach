from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import cast

import polars as pl
import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import Catalog, Guideline, Section
from chartcoach._catalog import CatalogManifest
from lancedb_embedding_fixture import registered_embedding

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


def test_catalog_documents_have_stable_search_identity(sample_catalog: Catalog) -> None:
    frame = sample_catalog.documents()
    row = frame.filter(frame["id"] == "direct-labels---overview").to_dicts()[0]

    assert frame.columns == [
        "row_id",
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
    catalog = _catalog_with_sections(
        sample_manifest,
        Section(role="advice", title="First", content="First advice."),
        Section(role="advice", title="Second", content="Second advice."),
    )

    rows = catalog.documents().filter(pl.col("role") == "section.advice")

    assert rows.select("id", "text").to_dicts() == [
        {"id": "repeated-role---role---advice", "text": "First advice."},
        {"id": "repeated-role---role---advice---2", "text": "Second advice."},
    ]


@pytest.mark.curation
def test_catalog_index_returns_the_release_profile_table(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    from chartcoach import open_catalog
    from chartcoach.curation import EmbeddingProfile, build_release

    path = tmp_path / "release"
    build_release(
        sample_catalog,
        path,
        profiles={
            "test-search": EmbeddingProfile(
                embedding=_test_embedding(),
            )
        },
    )
    opened = open_catalog(path).index("test-search")

    assert opened.name == "documents"
    rows = (
        opened.search("direct labels", query_type="fts", fts_columns="text")
        .limit(1)
        .to_list()
    )
    assert rows[0]["parent_id"] == "direct-labels"


@pytest.mark.curation
def test_fresh_process_search_uses_lancedb_query_embeddings(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    profile = "test-distinct"
    release = tmp_path / "release"
    from chartcoach.curation import EmbeddingProfile, build_release

    build_release(
        sample_catalog,
        release,
        profiles={profile: EmbeddingProfile(registered_embedding())},
    )
    marker = tmp_path / "query-method.txt"
    script = f"""
import lancedb_embedding_fixture
from chartcoach._catalog.search import catalog_search
from chartcoach import open_catalog
lancedb_embedding_fixture.registered_embedding()
catalog = open_catalog({str(release)!r})
for mode in ("vector", "hybrid"):
    result = catalog_search(catalog, "direct labels", profile={profile!r}, mode=mode, limit=2)
    assert result["matches"][0]["id"] == "direct-labels"
"""
    environment = {
        **os.environ,
        "PYTHONPATH": str(Path(__file__).parent),
        "CHARTCOACH_QUERY_PROCESS": "1",
        "CHARTCOACH_QUERY_MARKER": str(marker),
    }

    result = subprocess.run(
        [sys.executable, "-c", script],
        env=environment,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert marker.read_text().splitlines() == ["query", "query"]


@pytest.mark.curation
def test_fresh_process_fts_is_provider_independent(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    profile = "test-distinct"
    release = tmp_path / "release"
    from chartcoach.curation import EmbeddingProfile, build_release

    build_release(
        sample_catalog,
        release,
        profiles={profile: EmbeddingProfile(registered_embedding())},
    )
    script = f"""
from chartcoach._catalog.search import catalog_search
from chartcoach import open_catalog
catalog = open_catalog({str(release)!r})
result = catalog_search(catalog, "direct labels", profile={profile!r}, mode="fts", limit=2)
assert result["matches"][0]["id"] == "direct-labels"
"""

    result = subprocess.run(
        [sys.executable, "-c", script],
        env={**os.environ, "PYTHONPATH": ""},
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr


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
