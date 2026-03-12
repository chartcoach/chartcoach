import logging
import pathlib
from os import PathLike

from .catalog import Catalog
from .model import CatalogEntry, Guideline, GuidelineSection


def parse_guideline(markdown: str) -> Guideline:
    """
    Parse the given markdown content with YAML frontmatter and body into a ``Guideline`` object.

    Args:
        markdown (str): The markdown content to parse including YAML frontmatter.

    Returns:
        Guideline: The parsed guideline entry.
    """
    frontmatter, body = parse_markdown_with_frontmatter(markdown)
    return Guideline.model_validate({**frontmatter, "body": body})


def parse_guideline_sections(body: str) -> list[GuidelineSection]:
    """
    Parse the body content of a guideline into its structured sections based on role annotations.

    Args:
        body: The guideline body content of the guideline in markdown format.

    Returns:
        A list of GuidelineSection objects representing the structured sections of the guideline body.

    Example:
        Given the following guideline body content:

        .. code-block:: markdown
            Some dangling, untagged content.

            ## The Advice <!-- role: advice -->

            This is the main instruction or recommendation.

            ## Why This Matters <!-- role: reason -->

            Explanation of why this advice is important.

        The function will return:

        .. code-block:: python

            [
                GuidelineSection(
                    role=GuidelineSection.DANGLING_ROLE,
                    title="",
                    content="Some dangling, untagged content."
                ),
                GuidelineSection(
                    role="advice",
                    title="The Advice",
                    content="This is the main instruction or recommendation."
                ),
                GuidelineSection(
                    role="reason",
                    title="Why This Matters",
                    content="Explanation of why this advice is important."
                ),
            ]
    """
    import re

    sections: list[GuidelineSection] = []
    lines = body.split("\n")

    # Pattern to match heading with role annotation: ## Title <!-- role: role_name -->
    heading_pattern = re.compile(r"^##\s+(.+?)\s*<!--\s*role:\s*(\S+)\s*-->")

    current_section: dict[str, str] | None = None
    current_content_lines: list[str] = []

    for line in lines:
        match = heading_pattern.match(line)

        if match:
            # Save previous section if exists
            if current_section is not None:
                current_section["content"] = "\n".join(current_content_lines).strip()
                sections.append(GuidelineSection(**current_section))
            elif current_content_lines:
                # Dangling content before first section
                content = "\n".join(current_content_lines).strip()
                if content:
                    sections.append(
                        GuidelineSection(
                            role=GuidelineSection.DANGLING_ROLE,
                            title="",
                            content=content,
                        )
                    )

            # Start new section
            title = match.group(1).strip()
            role = match.group(2).strip()
            current_section = {"role": role, "title": title}
            current_content_lines = []
        else:
            # Accumulate content lines
            current_content_lines.append(line)

    # Handle final section or dangling content
    if current_section is not None:
        current_section["content"] = "\n".join(current_content_lines).strip()
        sections.append(GuidelineSection(**current_section))
    elif current_content_lines:
        content = "\n".join(current_content_lines).strip()
        if content:
            sections.append(
                GuidelineSection(
                    role=GuidelineSection.DANGLING_ROLE,
                    title="",
                    content=content,
                )
            )

    return sections


def parse_markdown_with_frontmatter(markdown: str) -> tuple[dict, str]:
    """
    Parse the given markdown content with YAML frontmatter.

    Args:
        markdown (str): The markdown content to parse including YAML frontmatter.

    Returns:
        A tuple containing the frontmatter as a dictionary and the body content as a string.
    """
    import yaml

    if not markdown.startswith("---"):
        return {}, markdown

    parts = markdown.split("---", 2)
    if len(parts) < 3:
        return {}, markdown

    frontmatter_str = parts[1].strip()
    body = parts[2].strip()

    frontmatter = yaml.safe_load(frontmatter_str) or {}

    return frontmatter, body


def parse_bibtex(bibtex_content: str) -> list[str]:
    """
    Parse the given BibTeX content into a list of individual BibTeX entries.

    Args:
        bibtex_content (str): The BibTeX content as a string.

    Returns:
        A list of strings, each representing a single BibTeX entry.
    """
    import re

    # Split entries by '@' while preserving the '@' at the start of each entry
    comment_free_lines = [
        line for line in bibtex_content.splitlines() if not line.strip().startswith("%")
    ]
    comment_free_content = "\n".join(comment_free_lines)
    entries = re.split(r"(?=@)", comment_free_content)
    entries = [stripped_entry for entry in entries if (stripped_entry := entry.strip())]

    return entries


def parse_bibtex_entry(bibtex_str: str) -> dict:
    """
    Parse a single BibTeX entry string into a dictionary of its fields.

    Args:
        bibtex_str (str): A single BibTeX entry as a string.

    Returns:
        A dictionary containing the fields of the BibTeX entry.
    """
    import bibtexparser

    return bibtexparser.loads(bibtex_str).entries[0]


MACRO_REPLACE_MAP = {
    "textraquo": "»",
    "textgreater": ">",
    "textless": "<",
    "?": "?",
    "\\": "",
    "[": "",
    "]": "",
    "{": "",
    "}": "",
}


def _normalize_bibtex_entry(bibtex_str: str) -> str:
    for macro, replacement in MACRO_REPLACE_MAP.items():
        bibtex_str = bibtex_str.replace(f"\\{macro}", replacement)

    return bibtex_str


def try_format_bibtex_entry(bibtex_entry: str, style: str = "harvard1") -> str:
    import io
    import warnings

    from citeproc import (
        Citation,
        CitationItem,
        CitationStylesBibliography,
        CitationStylesStyle,
        formatter,
    )
    from citeproc.source.bibtex import BibTeX

    bibtex_entry = _normalize_bibtex_entry(bibtex_entry)

    # Suppress warnings about unsupported BibTeX fields
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message="Unsupported BibTeX field")
        source = BibTeX(io.StringIO(bibtex_entry))
        cs = CitationStylesStyle(style, validate=False)
        bibliography = CitationStylesBibliography(cs, source, formatter.plain)

        parsed_entry = parse_bibtex_entry(bibtex_entry)
        if "ID" not in parsed_entry:
            raise ValueError("BibTeX entry must contain an 'ID' field.")

        citation = Citation([CitationItem(parsed_entry["ID"])])
        bibliography.register(citation)

        return "".join(bibliography.bibliography()[0])


def format_bibtex_entry(bibtex_entry: str, style: str = "harvard1") -> str:
    try:
        return try_format_bibtex_entry(bibtex_entry, style)
    except Exception:
        return bibtex_entry


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


def guideline_to_markdown(guideline: Guideline) -> str:
    """
    Convert a Guideline object back to its markdown representation.

    Args:
        guideline (Guideline): The guideline to convert.

    Returns:
        str: The markdown string representation of the guideline.
    """
    import mdformat
    import yaml

    frontmatter = {
        "id": guideline.id,
        "title": guideline.title,
        "bibliography": guideline.bibliography,
        "description": guideline.description,
        "labels": guideline.labels,
    }
    frontmatter = {k: v for k, v in frontmatter.items() if v is not None}
    frontmatter_yaml_str = yaml.dump(frontmatter, sort_keys=False).strip()
    formatted_body = mdformat.text(guideline.body)
    return "\n".join(
        [
            "---",
            frontmatter_yaml_str,
            "---",
            "",
            formatted_body,
        ]
    )
