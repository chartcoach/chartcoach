from __future__ import annotations

import hashlib
import json
from pathlib import Path

import polars as pl
import pytest
from catalog_testkit import deterministic_embedding
from chartcoach import Catalog, CatalogManifest, Guideline, Section, open_catalog
from chartcoach.cli.main import main as chartcoach_cli
from chartcoach.curation import (
    EmbeddingProfile,
    IndexProfile,
    build_release,
    validate_release,
    write_bundle,
)
from click.testing import CliRunner

_CONTRACT = (
    Path(__file__).parents[3] / "fixtures" / "catalog-contract" / "operations.json"
)
_SOURCE_URL = "https://www.datawrapper.de/blog/colorblindness-part2"
_DOCUMENT_TEXT = (
    "Read the original source [@muth_colorblindness_2020].\n\nSources\n\n"
    "- muth_colorblindness_2020: Lisa Charlotte Muth. 2020. "
    "What to consider when visualizing data for colorblind readers. "
    "https://www.datawrapper.de/blog/colorblindness-part2"
)


@pytest.fixture
def source_catalog(sample_manifest: CatalogManifest) -> Catalog:
    reference = json.loads(_CONTRACT.read_text(encoding="utf-8"))["bibliography_urls"][
        0
    ]["reference"]
    return Catalog.from_guidelines(
        [
            Guideline(
                id="source-locator",
                title="Inspect the source",
                description="Follow a reference to its original publication.",
                sections=(
                    Section(
                        role="advice",
                        title="Advice",
                        content="Read the original source [@muth_colorblindness_2020].",
                    ),
                ),
                references=(reference,),
            )
        ],
        manifest=sample_manifest,
    )


def test_cli_citation_includes_the_publication_locator(
    source_catalog: Catalog, runner: CliRunner, tmp_path: Path
) -> None:
    source = write_bundle(source_catalog, tmp_path / "catalog")

    result = runner.invoke(
        chartcoach_cli,
        [
            "catalog",
            "cite",
            "source-locator",
            "--source",
            str(source),
            "--format",
            "json",
        ],
    )

    assert result.exit_code == 0, result.output
    citation = json.loads(result.output)["records"][0]["sources"][0]
    assert citation["url"] == _SOURCE_URL
    assert citation["citation"] == (
        "Muth, L. C. (2020,). "
        "What to consider when visualizing data for colorblind readers. "
        "https://www.datawrapper.de/blog/colorblindness-part2"
    )


def test_document_content_hash_includes_its_source_locator(
    source_catalog: Catalog,
) -> None:
    document = (
        source_catalog.documents()
        .filter(pl.col("id") == "source-locator---role---advice")
        .row(0, named=True)
    )

    assert document["text"] == _DOCUMENT_TEXT
    assert (
        document["content_hash"] == hashlib.sha256(_DOCUMENT_TEXT.encode()).hexdigest()
    )


@pytest.mark.curation
def test_built_profile_retains_source_locators_in_its_documents(
    source_catalog: Catalog, tmp_path: Path
) -> None:
    root = tmp_path / "release"
    release = build_release(
        source_catalog,
        root,
        profiles={
            "sources": EmbeddingProfile(
                deterministic_embedding("source-locator-build"),
                export_documents=True,
            )
        },
    )

    assert validate_release(root) == release
    catalog = open_catalog(root)
    documents = pl.read_parquet(catalog.artifact("profiles/sources/documents.parquet"))
    document = documents.filter(pl.col("role") == "section.advice").row(0, named=True)
    assert document["text"] == _DOCUMENT_TEXT
    assert (
        document["content_hash"] == hashlib.sha256(_DOCUMENT_TEXT.encode()).hexdigest()
    )
    assert documents.select(catalog.documents().columns).equals(catalog.documents())


@pytest.mark.curation
def test_native_index_requires_the_catalogs_complete_source_context(
    source_catalog: Catalog, tmp_path: Path
) -> None:
    import lancedb
    from lancedb.embeddings import EmbeddingFunctionConfig

    incomplete_text = _DOCUMENT_TEXT.removesuffix(f". {_SOURCE_URL}")
    documents = source_catalog.documents().with_columns(
        text=pl.when(pl.col("role") == "section.advice")
        .then(pl.lit(incomplete_text))
        .otherwise(pl.col("text")),
        content_hash=pl.when(pl.col("role") == "section.advice")
        .then(pl.lit(hashlib.sha256(incomplete_text.encode()).hexdigest()))
        .otherwise(pl.col("content_hash")),
    )
    connection = lancedb.connect(tmp_path / "native")
    table = connection.create_table(
        "documents",
        data=documents.to_arrow(),
        embedding_functions=[
            EmbeddingFunctionConfig(
                source_column="text",
                vector_column="vector",
                function=deterministic_embedding("source-context-validation"),
            )
        ],
    )

    with pytest.raises(
        ValueError, match="document rows do not match the catalog derivation"
    ):
        build_release(
            source_catalog,
            tmp_path / "release",
            profiles={"sources": IndexProfile(table)},
        )
