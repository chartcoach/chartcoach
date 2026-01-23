from __future__ import annotations

from pathlib import Path

import pytest

from chartcoach.catalog.load import load_catalog, load_catalog_entry_


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


def test_load_catalog_entry_errors(tmp_path: Path) -> None:
    entry_dir = tmp_path / "e"
    entry_dir.mkdir()
    with pytest.raises(FileNotFoundError):
        load_catalog_entry_(entry_dir)

    (entry_dir / "a.md").write_text("a")
    (entry_dir / "b.md").write_text("b")
    with pytest.raises(ValueError):
        load_catalog_entry_(entry_dir)


def test_load_catalog_entry_missing_bib_logs_and_nulls_bibliography(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    entry_dir = tmp_path / "e"
    entry_dir.mkdir()
    (entry_dir / "guideline.md").write_text(
        _guideline_markdown(guideline_id="g1", bibliography="references.bib")
    )

    entry = load_catalog_entry_(entry_dir)
    assert entry.guideline.bibliography is None
    assert "not found" in caplog.text.lower()


def test_load_catalog_skips_bad_entries(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    good = tmp_path / "good"
    bad = tmp_path / "bad"
    good.mkdir()
    bad.mkdir()

    (good / "guideline.md").write_text(_guideline_markdown(guideline_id="g1"))
    # bad has no markdown file

    catalog = load_catalog(tmp_path)
    assert catalog.df().select("id").to_series().to_list() == ["g1"]
    assert "error loading catalog entry" in caplog.text.lower()
