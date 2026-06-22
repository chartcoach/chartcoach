from __future__ import annotations

import shutil
from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING, Iterable

from .entries import CatalogEntry
from .markdown import parse_guideline
from .manifest import CatalogManifest
from .references import parse_bibtex

if TYPE_CHECKING:
    from .collection import Catalog


def load_catalog_entry(path: Path) -> CatalogEntry:
    """Load a single catalog entry from a folder on disk."""
    guideline_md_path = path / "guideline.md"
    if not guideline_md_path.exists():
        raise FileNotFoundError(
            f"No guideline.md file found in catalog entry directory: {path}"
        )

    guideline = parse_guideline(guideline_md_path.read_text())

    references: list[str] = []
    if guideline.bibliography is not None:
        bib_path = path / guideline.bibliography
        references = parse_bibtex(bib_path.read_text())

    return CatalogEntry(guideline=guideline, references=tuple(references))


def load_catalog(folder_path: PathLike[str]) -> Catalog:
    """Load all catalog entries from a folder."""
    from .collection import Catalog

    root = Path(folder_path)
    manifest = CatalogManifest.from_path(root / "MANIFEST.md")
    entries_root = root / "entries"
    if not entries_root.exists():
        raise FileNotFoundError(f"No entries directory found in catalog folder: {root}")
    entries: list[CatalogEntry] = []

    for entry_path in sorted(entries_root.iterdir()):
        if not entry_path.is_dir():
            continue
        entries.append(load_catalog_entry(entry_path))

    return Catalog.from_entries(entries, manifest=manifest)


def write_catalog_entries(
    entries: Iterable[CatalogEntry],
    root: PathLike[str],
    *,
    manifest: CatalogManifest,
) -> None:
    """Write catalog entries back to the folder layout."""
    folder_path = Path(root)
    folder_path.mkdir(parents=True, exist_ok=True)
    manifest.write(folder_path / "MANIFEST.md")
    entries_root = folder_path / "entries"
    if entries_root.exists():
        shutil.rmtree(entries_root)
    entries_root.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        entry_folder = entries_root / entry.guideline.id
        entry_folder.mkdir(parents=True, exist_ok=True)

        guideline_md_path = entry_folder / "guideline.md"
        guideline_md_path.write_text(entry.guideline.to_markdown())

        if entry.guideline.bibliography is None:
            continue

        bib_path = entry_folder / entry.guideline.bibliography
        bib_path.parent.mkdir(parents=True, exist_ok=True)
        bib_path.write_text("\n".join(entry.references))
