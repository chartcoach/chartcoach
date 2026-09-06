from __future__ import annotations

import json
from pathlib import Path
from typing import cast

import polars as pl
import pytest
from catalog_testkit import write_catalog_entry, write_manifest
from chartcoach import CatalogError, open_catalog
from chartcoach.catalog.curation import write_bundle
from chartcoach.catalog.errors import CatalogValidationError
from chartcoach.catalog.guidelines import Guideline, Section
from chartcoach.catalog.manifest import CatalogManifest, CatalogManifestError
from chartcoach.catalog.model import Catalog

_INVALID_ROWS_PATH = (
    Path(__file__).parents[3]
    / "fixtures"
    / "catalog-contract"
    / "invalid-catalog-rows.json"
)


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
    assert (
        catalog.read(ids=["direct-labels"], source_detail="none")[0]["sections"][0][
            "content"
        ]
        == "Place the label close to the mark it names [@smith2024]."
    )
    assert catalog.table("guidelines").filter(pl.col("id") == "direct-labels").item(
        0, "body"
    ) == (
        "## Advice <!-- role: advice -->\n\n"
        "Place the label close to the mark it names [@smith2024]."
    )
    assert catalog.table("guideline_labels").get_column("label").to_list() == [
        "chart:line",
        "goal:comparison",
    ]
    assert catalog.table("guideline_sources").select(
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

    assert catalog.table("guidelines").get_column("id").to_list() == [
        "a-guideline",
        "z-guideline",
    ]


def test_compiled_bundle_roundtrips_manifest_and_rows(tmp_path: Path) -> None:
    write_manifest(tmp_path / "source")
    write_catalog_entry(tmp_path / "source")
    catalog = open_catalog(tmp_path / "source")

    bundle = write_bundle(catalog, tmp_path / "bundle")
    reloaded = open_catalog(bundle)

    assert reloaded.manifest.section_roles["advice"].name == "advice"
    assert reloaded.to_frame().equals(catalog.to_frame())


def test_catalog_owns_rows_reference_tables_and_manifest(
    tmp_path: Path,
    sample_manifest: CatalogManifest,
) -> None:
    write_manifest(tmp_path)
    write_catalog_entry(tmp_path)
    catalog = open_catalog(tmp_path)
    digest = catalog.entries_digest()

    rows = catalog.to_frame()
    rows[0, "title"] = "Changed title"
    references = catalog.table("references")
    references[0, "title"] = "Changed source"
    guideline_references = catalog.table("guideline_references")
    guideline_references[0, "guideline_id"] = "changed-id"

    assert catalog.read(ids=["direct-labels"], source_detail="none")[0]["title"] == (
        "direct-labels"
    )
    assert catalog.table("references").get_column("title").to_list() == [
        "Readable charts"
    ]
    assert catalog.table("guideline_references").get_column(
        "guideline_id"
    ).to_list() == ["direct-labels"]
    assert catalog.entries_digest() == digest

    section_roles = {"advice": sample_manifest.section_roles["advice"]}
    label_families = dict(sample_manifest.label_families)
    owned_manifest = CatalogManifest(
        markdown=sample_manifest.markdown,
        section_roles=section_roles,
        label_families=label_families,
    )
    section_roles.clear()
    label_families.clear()

    assert list(owned_manifest.section_roles) == ["advice"]
    assert set(owned_manifest.label_families) == {"chart", "component", "task"}
    with pytest.raises(TypeError):
        cast(dict[str, object], owned_manifest.section_roles)["reason"] = object()


def test_entries_digest_is_entry_order_stable(
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
        ).entries_digest()
        == Catalog.from_guidelines(
            [second, first], manifest=sample_manifest
        ).entries_digest()
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

    with pytest.raises(ValueError, match="duplicate guideline entry IDs"):
        Catalog.from_guidelines(
            [guideline, guideline],
            manifest=sample_manifest,
        )


def test_python_rejects_shared_invalid_catalog_rows() -> None:
    fixture = json.loads(_INVALID_ROWS_PATH.read_text(encoding="utf-8"))

    for test_case in fixture["cases"]:
        with pytest.raises((TypeError, ValueError), match=".+"):
            Guideline.from_mapping(fixture["row"] | test_case["patch"])


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

    with pytest.raises(
        CatalogManifestError, match="undefined section role"
    ) as exc_info:
        open_catalog(tmp_path)

    assert exc_info.value.code == "invalid_input"


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
