from __future__ import annotations

from pathlib import Path

import polars as pl
import pytest

from chartcoach import CatalogError, open_catalog
from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.entries import Guideline, Section
from chartcoach.catalog.errors import CatalogValidationError
from chartcoach.catalog.manifest import CatalogManifest, CatalogManifestError

from catalog_testkit import write_catalog_entry, write_manifest


def test_authored_folder_compiles_catalog_rows_and_relations(tmp_path: Path) -> None:
    write_manifest(tmp_path)
    write_catalog_entry(tmp_path)

    catalog = open_catalog(tmp_path)

    assert set(catalog.to_frame().columns) == {
        "id",
        "title",
        "description",
        "labels",
        "sections",
        "references",
    }
    assert catalog.entry("direct-labels")["body"] == (
        "## Advice <!-- role: advice -->\n\n"
        "Place the label close to the mark it names [@smith2024]."
    )
    assert catalog.guideline_labels().get_column("label").to_list() == [
        "chart:line",
        "goal:comparison",
    ]
    assert catalog.guideline_sources().select(
        "guideline_id",
        "reference_id",
        "source_title",
        "year",
    ).to_dicts() == [
        {
            "guideline_id": "direct-labels",
            "reference_id": "smith2024",
            "source_title": "Readable charts",
            "year": "2024",
        }
    ]


def test_authored_folder_loads_entries_in_id_order(tmp_path: Path) -> None:
    write_manifest(tmp_path)
    write_catalog_entry(tmp_path, "z-guideline")
    write_catalog_entry(tmp_path, "a-guideline")

    catalog = open_catalog(tmp_path)

    assert catalog.guidelines().get_column("id").to_list() == [
        "a-guideline",
        "z-guideline",
    ]


def test_compiled_bundle_roundtrips_manifest_and_rows(tmp_path: Path) -> None:
    write_manifest(tmp_path / "source")
    write_catalog_entry(tmp_path / "source")
    catalog = open_catalog(tmp_path / "source")

    bundle = catalog.write_bundle(tmp_path / "bundle")
    reloaded = open_catalog(bundle)

    assert reloaded.manifest.section_roles["advice"].name == "advice"
    assert reloaded.to_frame().equals(catalog.to_frame())


def test_content_digest_is_entry_order_stable(
    sample_manifest: CatalogManifest,
) -> None:
    first = Guideline(
        id="direct-labels",
        title="Use direct labels",
        description="Label marks directly when space permits.",
        labels=("chart:line",),
        sections=(
            Section(
                role="advice",
                title="Advice",
                content="Label marks directly when space permits.",
            ),
        ),
    )
    second = Guideline(
        id="full-axis-bars",
        title="Use full axes",
        description="Keep bar axes honest.",
        labels=("chart:bar",),
        sections=(
            Section(
                role="advice",
                title="Advice",
                content="Keep bar axes honest.",
            ),
        ),
    )

    assert (
        Catalog.from_guidelines(
            [first, second], manifest=sample_manifest
        ).content_digest()
        == Catalog.from_guidelines(
            [second, first], manifest=sample_manifest
        ).content_digest()
    )


def test_catalog_duckdb_exposes_guidelines_and_sections(
    sample_catalog: Catalog,
) -> None:
    connection = sample_catalog.duckdb()
    try:
        rows = connection.sql(
            """
            select g.id, s.content
            from guidelines g
            join sections s on s.guideline_id = g.id
            where list_contains(g.labels, 'chart:bar')
              and s.role = 'advice'
            """
        ).fetchall()
    finally:
        connection.close()

    assert rows == [("full-axis-bars", "Start bar value axes at zero.")]


def test_catalog_rejects_duplicate_ids(sample_manifest: CatalogManifest) -> None:
    guideline = Guideline(
        id="duplicate",
        title="Title",
        description="Description",
        sections=(Section(role="advice", title="Advice", content="Content."),),
    )

    with pytest.raises(ValueError, match="duplicate guideline ids"):
        Catalog.from_guidelines(
            [guideline, guideline],
            manifest=sample_manifest,
        )


def test_catalog_folder_requires_manifest(tmp_path: Path) -> None:
    write_catalog_entry(tmp_path)

    with pytest.raises(CatalogError, match="MANIFEST.md"):
        open_catalog(tmp_path)


def test_catalog_manifest_covers_compiled_vocabulary(tmp_path: Path) -> None:
    write_manifest(
        tmp_path,
        """# Sample Catalog

## Section Roles

### reason

Evidence behind a guideline.

## Label Families

### chart

Chart-family labels such as `chart:line`.

### goal

Task-goal labels such as `goal:comparison`.
""",
    )
    write_catalog_entry(tmp_path)

    with pytest.raises(CatalogManifestError, match="undefined section role"):
        open_catalog(tmp_path)


def test_compiled_bundle_rejects_invalid_rows(
    tmp_path: Path,
    sample_manifest: CatalogManifest,
) -> None:
    bundle = tmp_path / "bundle"
    bundle.mkdir()
    sample_manifest.write(bundle / "MANIFEST.md")
    pl.from_dicts(
        [
            {
                "id": "direct-labels",
                "title": 7,
                "description": "Label marks directly.",
                "labels": [],
                "sections": [
                    {
                        "role": "advice",
                        "title": "Advice",
                        "content": "Place labels near marks.",
                    }
                ],
                "references": [],
            }
        ]
    ).write_parquet(bundle / "entries.parquet")

    with pytest.raises(
        CatalogValidationError,
        match=(
            r"Catalog row 1 \(id='direct-labels'\) is invalid: "
            r"title must be a string\."
        ),
    ):
        open_catalog(bundle)
