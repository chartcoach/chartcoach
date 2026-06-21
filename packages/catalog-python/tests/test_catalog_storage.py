from __future__ import annotations

from pathlib import Path

import polars as pl
import pytest

from chartcoach.catalog import (
    Catalog,
    CatalogManifestError,
    Guideline,
    Section as GuidelineSection,
)
from chartcoach.catalog.remote import read_release_metadata
from chartcoach.catalog.storage import load_catalog_entry

from catalog_testkit import write_catalog_entry, write_manifest


def test_catalog_loads_folder_entries_and_tables(tmp_path: Path) -> None:
    write_manifest(tmp_path)
    write_catalog_entry(tmp_path)

    catalog = Catalog.from_folder(tmp_path)

    assert len(catalog) == 1
    assert catalog.entry("direct-labels")["id"] == "direct-labels"
    assert catalog.guidelines().select("id").to_series().to_list() == ["direct-labels"]
    assert catalog.sections().select("role").to_series().to_list() == ["advice"]
    assert catalog.guideline_labels().select("label").to_series().to_list() == [
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


def test_catalog_folder_queries_are_deterministically_ordered(tmp_path: Path) -> None:
    write_manifest(tmp_path)
    write_catalog_entry(tmp_path, "z-guideline")
    write_catalog_entry(tmp_path, "a-guideline")

    catalog = Catalog.from_folder(tmp_path)

    assert catalog.guidelines().get_column("id").to_list() == [
        "a-guideline",
        "z-guideline",
    ]


def test_catalog_write_folder_roundtrips_entries(tmp_path: Path) -> None:
    write_manifest(tmp_path / "source")
    write_catalog_entry(tmp_path / "source")
    catalog = Catalog.from_folder(tmp_path / "source")

    catalog.write_folder(tmp_path / "written")
    reloaded = Catalog.from_folder(tmp_path / "written")

    assert reloaded.to_frame().to_dicts() == catalog.to_frame().to_dicts()


def test_catalog_write_folder_replaces_existing_entries(tmp_path: Path) -> None:
    write_manifest(tmp_path / "source")
    write_catalog_entry(tmp_path / "source")
    catalog = Catalog.from_folder(tmp_path / "source")
    output = tmp_path / "written"
    stale_entry = write_catalog_entry(output, "stale-guideline")
    (stale_entry / "notes.md").write_text("local draft")

    catalog.write_folder(output)

    assert not stale_entry.exists()
    assert Catalog.from_folder(output).guidelines().get_column("id").to_list() == [
        "direct-labels"
    ]


def test_catalog_digest_is_entry_order_stable() -> None:
    first = Guideline(
        id="direct-labels",
        title="Use direct labels",
        description="Label marks directly when space permits.",
        body="Label marks directly when space permits.",
        labels=("chart:line",),
    )
    second = Guideline(
        id="full-axis-bars",
        title="Use full axes",
        description="Keep bar axes honest.",
        body="Keep bar axes honest.",
        labels=("chart:bar",),
    )

    assert (
        Catalog.from_entries([first, second]).digest()
        == Catalog.from_entries([second, first]).digest()
    )


def test_catalog_from_entries_accepts_public_guideline_records() -> None:
    catalog = Catalog.from_entries(
        [
            Guideline(
                id="direct-labels",
                title="Use direct labels",
                description="Label marks directly when space permits.",
                body="## Advice <!-- role: advice -->\n\nPlace labels near marks.",
                labels=("chart:line",),
                sections=(
                    GuidelineSection(
                        role="advice",
                        title="Advice",
                        content="Place labels near marks.",
                    ),
                ),
            ),
            {
                "id": "full-axis-bars",
                "title": "Use full value axes for bars",
                "description": "Keep bar axes on the honest baseline.",
                "body": "## Advice <!-- role: advice -->\n\nStart axes at zero.",
                "labels": ["chart:bar"],
                "sections": [
                    {
                        "role": "advice",
                        "title": "Advice",
                        "content": "Start axes at zero.",
                    }
                ],
                "references": ["smith2024"],
            },
        ]
    )

    assert catalog.guidelines().select("id").to_series().to_list() == [
        "direct-labels",
        "full-axis-bars",
    ]
    assert catalog.entry("full-axis-bars")["references"] == ["smith2024"]


def test_catalog_select_empty_returns_empty_catalog() -> None:
    entry = Guideline(
        id="direct-labels",
        title="Use direct labels",
        description="Label marks directly when space permits.",
        body="Label marks directly when space permits.",
        labels=("chart:line",),
    )
    catalog = Catalog.from_entries([entry])

    selected = catalog.select([])

    assert len(selected) == 0
    assert selected.to_frame().schema == catalog.to_frame().schema


def test_catalog_sections_handles_guidelines_without_sections() -> None:
    catalog = Catalog.from_frame(
        pl.from_dicts(
            [
                {
                    "id": "plain-guideline",
                    "guideline": {
                        "id": "plain-guideline",
                        "title": "Plain guideline",
                        "bibliography": None,
                        "description": "Description.",
                        "labels": [],
                        "body": "No section headings here.",
                        "sections": [],
                    },
                    "references": [],
                }
            ]
        )
    )

    assert catalog.sections().is_empty()


def test_load_catalog_entry_requires_guideline_file(tmp_path: Path) -> None:
    empty_entry = tmp_path / "empty"
    empty_entry.mkdir()

    with pytest.raises(FileNotFoundError, match="No guideline.md file found"):
        load_catalog_entry(empty_entry)


def test_catalog_write_parquet_roundtrips(tmp_path: Path) -> None:
    write_manifest(tmp_path / "source")
    write_catalog_entry(tmp_path / "source")
    catalog = Catalog.from_folder(tmp_path / "source")

    parquet_path = tmp_path / "entries.parquet"
    catalog.write_parquet(parquet_path)

    reloaded = Catalog.from_parquet(parquet_path)
    assert reloaded.to_frame().to_dicts() == catalog.to_frame().to_dicts()


def test_catalog_write_bundle_includes_release_metadata(tmp_path: Path) -> None:
    write_manifest(tmp_path / "source")
    write_catalog_entry(tmp_path / "source")
    catalog = Catalog.from_folder(tmp_path / "source")

    catalog.write_bundle(tmp_path / "bundle")

    metadata = read_release_metadata(tmp_path / "bundle")
    assert metadata.version == "0.1.3"
    assert metadata.digest == catalog.digest()
    assert metadata.artifact("manifest").path == "MANIFEST.md"
    assert metadata.artifact("entries").path == "entries.parquet"
    assert metadata.artifact("entries").rows == 1


def test_catalog_duckdb_returns_native_queryable_connection(
    sample_catalog: Catalog,
) -> None:
    conn = sample_catalog.duckdb()
    try:
        rows = conn.sql(
            """
            select g.id, g.title, s.content
            from guidelines g
            join sections s on s.guideline_id = g.id
            where list_contains(g.labels, 'chart:bar')
              and s.role = 'advice'
            """
        ).pl()
    finally:
        conn.close()

    assert rows.to_dicts() == [
        {
            "id": "full-axis-bars",
            "title": "Use full value axes for bars",
            "content": "Start bar value axes at zero.",
        }
    ]


def test_catalog_write_duckdb_method_writes_database_file(
    sample_catalog: Catalog,
    tmp_path: Path,
) -> None:
    import duckdb

    path = sample_catalog.write_duckdb(tmp_path / "catalog.duckdb")

    conn = duckdb.connect(path, read_only=True)
    try:
        row = conn.sql("select count(*) from guidelines").fetchone()
    finally:
        conn.close()
    assert row == (2,)


def test_catalog_rejects_duplicate_ids() -> None:
    guideline = Guideline(
        id="duplicate",
        title="Title",
        description="Description",
        body="Body",
    )
    with pytest.raises(ValueError, match="duplicate guideline ids"):
        Catalog.from_entries([guideline, guideline])


def test_catalog_rejects_mismatched_row_id() -> None:
    with pytest.raises(ValueError, match="does not match guideline id"):
        Catalog.from_entries(
            [
                {
                    "id": "row-id",
                    "guideline": {
                        "id": "guideline-id",
                        "title": "Title",
                        "description": "Description",
                        "body": "Body",
                        "labels": [],
                        "sections": [],
                    },
                    "references": [],
                }
            ]
        )


def test_catalog_folder_requires_manifest(tmp_path: Path) -> None:
    write_catalog_entry(tmp_path)

    with pytest.raises(FileNotFoundError, match="MANIFEST.md"):
        Catalog.from_folder(tmp_path)


def test_catalog_manifest_rejects_undefined_section_roles(tmp_path: Path) -> None:
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
        Catalog.from_folder(tmp_path)


def test_catalog_manifest_rejects_undefined_label_families(tmp_path: Path) -> None:
    write_manifest(
        tmp_path,
        """# Sample Catalog

## Section Roles

### advice

Actionable guidance for applying the guideline.

## Label Families

### chart

Chart-family labels such as `chart:line`.
""",
    )
    write_catalog_entry(tmp_path)

    with pytest.raises(CatalogManifestError, match="undefined label family"):
        Catalog.from_folder(tmp_path)


def test_catalog_bundle_loads_manifest_and_parquet(tmp_path: Path) -> None:
    write_manifest(tmp_path / "source")
    write_catalog_entry(tmp_path / "source")
    catalog = Catalog.from_folder(tmp_path / "source")

    catalog.write_bundle(tmp_path / "bundle")
    reloaded = Catalog.from_bundle(tmp_path / "bundle")

    assert list(reloaded.require_manifest().section_roles) == ["advice"]
    assert reloaded.to_frame().to_dicts() == catalog.to_frame().to_dicts()


def test_catalog_open_loads_folder_bundle_and_parquet(tmp_path: Path) -> None:
    write_manifest(tmp_path / "source")
    write_catalog_entry(tmp_path / "source")

    folder_catalog = Catalog.open(tmp_path / "source")
    folder_catalog.write_bundle(tmp_path / "bundle")
    parquet_path = tmp_path / "entries.parquet"
    folder_catalog.write_parquet(parquet_path)

    assert Catalog.open(tmp_path / "source").guidelines().height == 1
    assert Catalog.open(tmp_path / "bundle").require_manifest()
    assert Catalog.open(parquet_path).guidelines().height == 1


def test_catalog_from_frame_rejects_mismatched_guideline_id() -> None:
    frame = pl.from_dicts(
        [
            {
                "id": "row-id",
                "guideline": {
                    "id": "guideline-id",
                    "title": "Title",
                    "bibliography": None,
                    "description": "Description",
                    "labels": [],
                    "body": "Body",
                    "sections": [],
                },
                "references": [],
            }
        ]
    )

    with pytest.raises(ValueError, match="row id must match guideline id"):
        Catalog.from_frame(frame)


def test_guideline_from_mapping_derives_sections_from_body() -> None:
    guideline = Guideline.from_mapping(
        {
            "id": "guideline-id",
            "title": "Title",
            "description": "Description",
            "body": "## Advice <!-- role: advice -->\n\nBody",
            "labels": [],
        }
    )

    assert [(section.role, section.content) for section in guideline.sections] == [
        ("advice", "Body")
    ]


def test_empty_label_catalog_frames_are_typed() -> None:
    catalog = Catalog.from_entries(
        [
            Guideline(
                id="unlabeled",
                title="Title",
                description="Description",
                body="Body",
            )
        ]
    )

    assert catalog.labels().schema["family"].is_(pl.String)
    assert catalog.labels().schema["category"].is_(pl.String)
    assert catalog.labels().schema["modifier"].is_(pl.String)
    assert catalog.guideline_labels().schema["label"].is_(pl.String)
    assert catalog.labels().is_empty()
    assert catalog.guideline_labels().is_empty()
