from __future__ import annotations

from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING

from .entries import Guideline
from .manifest import CatalogManifest
from .markdown import (
    _guideline_from_source,
    _pop_bibliography,
    parse_markdown_with_frontmatter,
)
from .references import parse_bibtex

if TYPE_CHECKING:
    from .collection import Catalog


def load_catalog_entry(path: Path) -> Guideline:
    """Load one guideline and its bibliography from an authored entry folder."""

    guideline_path = path / "guideline.md"
    if not guideline_path.exists():
        raise FileNotFoundError(
            f"No guideline.md file found in catalog entry directory: {path}"
        )

    metadata, body = parse_markdown_with_frontmatter(
        guideline_path.read_text(encoding="utf-8")
    )
    bibliography = _pop_bibliography(metadata)
    references: list[str] = []
    if bibliography is not None:
        references = parse_bibtex((path / bibliography).read_text(encoding="utf-8"))
    return _guideline_from_source(metadata, body, references)


def load_catalog(folder_path: PathLike[str]) -> Catalog:
    """Load an authored catalog folder."""

    from .collection import Catalog

    root = Path(folder_path)
    manifest = CatalogManifest.from_path(root / "MANIFEST.md")
    entries_root = root / "entries"
    if not entries_root.exists():
        raise FileNotFoundError(f"No entries directory found in catalog folder: {root}")
    guidelines = [
        load_catalog_entry(entry_path)
        for entry_path in sorted(entries_root.iterdir())
        if entry_path.is_dir()
    ]
    return Catalog.from_guidelines(guidelines, manifest=manifest)
