from __future__ import annotations

import logging
from os import PathLike
from pathlib import Path
from typing import Iterable, TYPE_CHECKING

from ..guideline import parse_bibtex, parse_guideline
from .collection import CatalogEntry

if TYPE_CHECKING:
    from .collection import Catalog


logger = logging.getLogger(__name__)


def load_catalog_entry(path: Path) -> CatalogEntry:
    """Load a single catalog entry from a folder on disk."""
    md_files = list(path.glob("*.md"))

    if not md_files:
        raise FileNotFoundError(
            f"No guideline markdown file found in catalog entry directory: {path}"
        )
    if len(md_files) > 1:
        raise ValueError(
            f"Multiple markdown files found in catalog entry directory: {path}. Expected only one."
        )

    guideline = parse_guideline(md_files[0].read_text())

    references: list[str] = []
    if guideline.bibliography is not None:
        bib_path = path / guideline.bibliography
        if bib_path.exists():
            references = parse_bibtex(bib_path.read_text())
        else:
            logger.warning(
                "Bibliography file specified in guideline '%s' not found: '%s'. "
                "Setting guideline bibliography to None.",
                guideline.id,
                bib_path,
            )
            guideline.bibliography = None

    return CatalogEntry(guideline=guideline, references=references)


def load_catalog(folder_path: PathLike[str]) -> Catalog:
    """Load all catalog entries from a folder."""
    from .collection import Catalog

    entries: list[CatalogEntry] = []

    for entry_path in Path(folder_path).iterdir():
        if not entry_path.is_dir():
            continue
        try:
            entries.append(load_catalog_entry(entry_path))
        except Exception as exc:
            logger.warning("Error loading catalog entry from %s: %s", entry_path, exc)

    return Catalog(entries)


def write_catalog_entries(entries: Iterable[CatalogEntry], root: PathLike[str]) -> None:
    """Write catalog entries back to the folder layout."""
    folder_path = Path(root)
    folder_path.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        entry_folder = folder_path / entry.guideline.id
        entry_folder.mkdir(parents=True, exist_ok=True)

        guideline_md_path = entry_folder / "guideline.md"
        guideline_md_path.write_text(entry.guideline.to_markdown())

        if entry.guideline.bibliography is None:
            continue

        bib_path = entry_folder / entry.guideline.bibliography
        bib_path.parent.mkdir(parents=True, exist_ok=True)
        bib_path.write_text("\n".join(entry.references))
