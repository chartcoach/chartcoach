from pathlib import Path

import pytest
import polars as pl

from chartcoach.catalog import Catalog, CatalogEntry
from chartcoach.catalog.storage import load_catalog_entry
from chartcoach.guideline import Guideline


GUIDELINE_MD = """---
id: direct-labels
title: Use direct labels
description: Label marks directly when space permits.
bibliography: references.bib
labels:
  - chart:line
  - goal:comparison
---

## Advice <!-- role: advice -->

Place the label close to the mark it names [@smith2024].
"""

BIBTEX = """% generated note
@article{smith2024,
  title = {Readable charts},
  author = {Smith, Ada},
  year = {2024},
  journal = {Journal of Charts}
}
"""


def write_catalog_entry(root: Path, entry_id: str = "direct-labels") -> Path:
    entry_dir = root / entry_id
    entry_dir.mkdir(parents=True)
    (entry_dir / "guideline.md").write_text(
        GUIDELINE_MD.replace("id: direct-labels", f"id: {entry_id}")
        .replace("title: Use direct labels", f"title: {entry_id}")
        .replace(
            "description: Label marks directly when space permits.",
            f"description: {entry_id} description.",
        )
    )
    (entry_dir / "references.bib").write_text(BIBTEX)
    return entry_dir


def test_catalog_loads_folder_entries_and_tables(tmp_path: Path) -> None:
    write_catalog_entry(tmp_path)
    (tmp_path / "__templates__").mkdir()

    catalog = Catalog.from_folder(tmp_path)

    assert len(catalog) == 1
    assert catalog.entry("direct-labels").id == "direct-labels"
    assert catalog.guidelines().select("id").to_series().to_list() == ["direct-labels"]
    assert catalog.sections().select("role").to_series().to_list() == ["advice"]
    assert catalog.guideline_labels().select("label").to_series().to_list() == [
        "chart:line",
        "goal:comparison",
    ]


def test_catalog_folder_queries_are_deterministically_ordered(tmp_path: Path) -> None:
    write_catalog_entry(tmp_path, "z-guideline")
    write_catalog_entry(tmp_path, "a-guideline")

    catalog = Catalog.from_folder(tmp_path)

    assert catalog.guidelines().get_column("id").to_list() == [
        "a-guideline",
        "z-guideline",
    ]


def test_catalog_write_folder_roundtrips_entries(tmp_path: Path) -> None:
    write_catalog_entry(tmp_path / "source")
    catalog = Catalog.from_folder(tmp_path / "source")

    catalog.write_folder(tmp_path / "written")
    reloaded = Catalog.from_folder(tmp_path / "written")

    assert reloaded.to_frame().to_dicts() == catalog.to_frame().to_dicts()


def test_catalog_digest_is_entry_order_stable() -> None:
    first = CatalogEntry(
        guideline=Guideline(
            id="direct-labels",
            title="Use direct labels",
            description="Label marks directly when space permits.",
            body="Label marks directly when space permits.",
            labels=("chart:line",),
        )
    )
    second = CatalogEntry(
        guideline=Guideline(
            id="full-axis-bars",
            title="Use full axes",
            description="Keep bar axes honest.",
            body="Keep bar axes honest.",
            labels=("chart:bar",),
        )
    )

    assert (
        Catalog.from_entries([first, second]).digest()
        == Catalog.from_entries([second, first]).digest()
    )


def test_catalog_select_empty_returns_empty_catalog() -> None:
    entry = CatalogEntry(
        guideline=Guideline(
            id="direct-labels",
            title="Use direct labels",
            description="Label marks directly when space permits.",
            body="Label marks directly when space permits.",
            labels=("chart:line",),
        )
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
    write_catalog_entry(tmp_path / "source")
    catalog = Catalog.from_folder(tmp_path / "source")

    parquet_path = tmp_path / "catalog.parquet"
    catalog.write_parquet(parquet_path)

    reloaded = Catalog.from_parquet(parquet_path)
    assert reloaded.to_frame().to_dicts() == catalog.to_frame().to_dicts()


def test_catalog_rejects_duplicate_ids() -> None:
    guideline = Guideline(
        id="duplicate",
        title="Title",
        description="Description",
        body="Body",
    )
    entry = CatalogEntry(guideline=guideline)

    with pytest.raises(ValueError, match="duplicate guideline ids"):
        Catalog.from_entries([entry, entry])


def test_catalog_entry_rejects_mismatched_row_id() -> None:
    with pytest.raises(ValueError, match="does not match guideline id"):
        CatalogEntry.from_mapping(
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
        )


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


def test_guideline_from_mapping_requires_serialized_sections() -> None:
    with pytest.raises(TypeError, match="sections is required"):
        Guideline.from_mapping(
            {
                "id": "guideline-id",
                "title": "Title",
                "description": "Description",
                "body": "Body",
                "labels": [],
            }
        )


def test_empty_label_catalog_frames_are_typed() -> None:
    catalog = Catalog.from_entries(
        [
            CatalogEntry(
                guideline=Guideline(
                    id="unlabeled",
                    title="Title",
                    description="Description",
                    body="Body",
                )
            )
        ]
    )

    assert catalog.labels().schema["category"].is_(pl.String)
    assert catalog.guideline_labels().schema["label"].is_(pl.String)
    assert catalog.labels().is_empty()
    assert catalog.guideline_labels().is_empty()
