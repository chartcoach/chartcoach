from pathlib import Path

import pytest

from chartcoach.catalog import Catalog
from chartcoach.catalog.storage import load_catalog_entry
from chartcoach.guideline import parse_bibtex


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
    (entry_dir / "guideline.md").write_text(GUIDELINE_MD)
    (entry_dir / "references.bib").write_text(BIBTEX)
    return entry_dir


def test_catalog_loads_folder_entries_and_tables(tmp_path: Path) -> None:
    write_catalog_entry(tmp_path)
    (tmp_path / "__templates__").mkdir()

    catalog = Catalog.from_disk(tmp_path)

    assert len(catalog) == 1
    assert catalog[0].id == "direct-labels"
    assert catalog.guidelines_df.select("id").to_series().to_list() == ["direct-labels"]
    assert catalog.sections_df.select("role").to_series().to_list() == ["advice"]
    assert catalog.guideline_labels_df.select("label").to_series().to_list() == [
        "chart:line",
        "goal:comparison",
    ]


def test_catalog_write_folders_roundtrips_entries(tmp_path: Path) -> None:
    write_catalog_entry(tmp_path / "source")
    catalog = Catalog.from_disk(tmp_path / "source")

    catalog.write_folders(tmp_path / "written")
    reloaded = Catalog.from_disk(tmp_path / "written")

    assert [entry.model_dump() for entry in reloaded] == [
        entry.model_dump() for entry in catalog
    ]


def test_load_catalog_entry_requires_guideline_file(tmp_path: Path) -> None:
    empty_entry = tmp_path / "empty"
    empty_entry.mkdir()

    with pytest.raises(FileNotFoundError, match="No guideline.md file found"):
        load_catalog_entry(empty_entry)


def test_parse_bibtex_ignores_percent_comments() -> None:
    assert parse_bibtex(BIBTEX) == [BIBTEX.split("\n", 1)[1].strip()]
