from __future__ import annotations

from pathlib import Path

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.catalog.parse import parse_guideline
from chartcoach.catalog.serialize import catalog_to_disk, guideline_to_markdown


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


def test_guideline_to_markdown_omits_none_fields() -> None:
    guideline = Guideline(
        id="g1",
        title="T",
        description="D",
        bibliography=None,
        labels=["chart:bar"],
        body="## The Advice <!-- role: advice -->\n\nX",
    )
    md = guideline_to_markdown(guideline)
    assert "id: g1" in md
    assert "bibliography:" not in md


def test_catalog_to_disk_writes_guideline_and_references(tmp_path: Path) -> None:
    entry = CatalogEntry(
        guideline=parse_guideline(
            _guideline_markdown(guideline_id="g1", bibliography="references.bib")
        ),
        references=["@article{a, title={A}}"],
    )
    catalog = Catalog([entry])
    catalog_to_disk(catalog, tmp_path)

    guideline_path = tmp_path / "g1" / "guideline.md"
    assert guideline_path.exists()

    bib_path = tmp_path / "g1" / "references.bib"
    assert bib_path.exists()
    assert bib_path.read_text().strip().startswith("@article{a")
