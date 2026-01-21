import logging
import pathlib
from os import PathLike

from .catalog import Catalog
from .model import CatalogEntry
from .parse import parse_bibtex, parse_guideline

logger = logging.getLogger(__name__)


def load_catalog_entry_(path: pathlib.Path) -> CatalogEntry:
    """
    Load a catalog entry from the specified directory path.

    Args:
        path (pathlib.Path): The path to the catalog entry directory.
    Returns:
        CatalogEntry: The loaded catalog entry.
    """
    md_files = list(path.glob("*.md"))

    if not md_files:
        raise FileNotFoundError(
            f"No guideline markdown file found in catalog entry directory: {path}"
        )

    if len(md_files) > 1:
        raise ValueError(
            f"Multiple markdown files found in catalog entry directory: {path}. Expected only one."
        )

    guideline_md_path = md_files[0]
    guideline_md_content = guideline_md_path.read_text()
    guideline = parse_guideline(guideline_md_content)

    # Read bibtex if present
    references_content: str | None = None
    references = []
    if guideline.bibliography is not None:
        bib_path = path / guideline.bibliography
        if bib_path.exists():
            references_content = bib_path.read_text()
            references = (
                parse_bibtex(references_content)
                if references_content is not None
                else []
            )
        else:
            logger.warning(
                f"Bibliography file specified in guideline '{guideline.id}' not found: '{bib_path}'. Setting guideline bibliography to None."
            )
            guideline.bibliography = None

    return CatalogEntry(guideline=guideline, references=references)


def load_catalog(folder_path: PathLike[str]) -> Catalog:
    """
    Load all catalog entries from the specified folder path.

    Args:
        folder_path (pathlib.Path): The path to the catalog folder.
    Returns:
        list[CatalogEntry]: A list of loaded catalog entries.
    """
    entries: list[CatalogEntry] = []

    for entry in pathlib.Path(folder_path).iterdir():
        if entry.is_dir():
            try:
                catalog_entry = load_catalog_entry_(entry)
                entries.append(catalog_entry)
            except Exception as e:
                logger.warning(f"Error loading catalog entry from {entry}: {e}")

    return Catalog(entries)
