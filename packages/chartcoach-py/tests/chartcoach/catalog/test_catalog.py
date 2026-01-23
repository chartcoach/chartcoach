from __future__ import annotations

from pathlib import Path

import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.catalog.parse import parse_guideline


def _guideline_markdown(
    *,
    guideline_id: str = "g1",
    title: str = "Use direct labels",
    description: str = "Short description.",
    bibliography: str | None = None,
    labels: list[str] | None = None,
    body: str = "## The Advice <!-- role: advice -->\n\nDo the thing.",
) -> str:
    labels = labels or ["chart:bar", "goal:comparison"]
    bibliography_line = (
        "" if bibliography is None else f"bibliography: {bibliography}\n"
    )
    labels_yaml = "\n".join([f"  - {label}" for label in labels])
    return (
        "---\n"
        f"id: {guideline_id}\n"
        f"title: {title}\n"
        f"{bibliography_line}"
        f"description: {description}\n"
        "labels:\n"
        f"{labels_yaml}\n"
        "---\n\n"
        f"{body}\n"
    )


def test_catalog_df_is_cached_and_clone_safe() -> None:
    entry = CatalogEntry(
        guideline=Guideline(
            id="g1",
            title="T",
            description="D",
            bibliography=None,
            labels=["a:b"],
            body="## The Advice <!-- role: advice -->\n\nX",
        ),
        references=[],
    )
    catalog = Catalog([entry])
    df1 = catalog.df()
    df2 = catalog.df()
    assert df1 is not df2
    assert df1.to_dicts() == df2.to_dicts()


def test_catalog_sections_and_labels_df() -> None:
    entry = CatalogEntry(
        guideline=Guideline(
            id="g1",
            title="T",
            description="D",
            bibliography=None,
            labels=["chart:bar", "goal:comparison"],
            body="## The Advice <!-- role: advice -->\n\nX",
        ),
        references=[],
    )
    catalog = Catalog([entry])
    sections_df = catalog.sections_df()
    assert sections_df.select("role").to_series().to_list() == ["advice"]

    labels_df = catalog.labels_df()
    assert labels_df.to_dicts() == [
        {"category": "chart", "subcategory": "bar"},
        {"category": "goal", "subcategory": "comparison"},
    ]


def test_catalog_to_disk_and_load_roundtrip(tmp_path: Path) -> None:
    entry_with_bib = CatalogEntry(
        guideline=parse_guideline(
            _guideline_markdown(guideline_id="withbib", bibliography="references.bib")
        ),
        references=["@article{a, title={A}}"],
    )
    entry_without_bib = CatalogEntry(
        guideline=parse_guideline(
            _guideline_markdown(guideline_id="nobib", bibliography=None)
        ),
        references=[],
    )
    catalog = Catalog([entry_with_bib, entry_without_bib])
    catalog.write_folders(tmp_path)

    loaded = Catalog.from_disk(tmp_path)
    assert loaded.df().select("id").to_series().to_list() == ["nobib", "withbib"]


def test_catalog_from_df_and_merge() -> None:
    entry1 = CatalogEntry(
        guideline=parse_guideline(_guideline_markdown(guideline_id="a")),
        references=[],
    )
    entry2 = CatalogEntry(
        guideline=parse_guideline(_guideline_markdown(guideline_id="b")),
        references=[],
    )
    c1 = Catalog([entry1])
    c2 = Catalog([entry2])
    merged = c1 + c2
    assert len(merged) == 2
    assert merged[0].id in {"a", "b"}

    roundtripped = Catalog.from_df(merged.df())
    assert sorted([e.id for e in roundtripped]) == ["a", "b"]

    assert pl.concat([c1.df(), c2.df()], how="vertical").height == 2
