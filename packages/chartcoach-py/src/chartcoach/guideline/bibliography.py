from __future__ import annotations

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


def parse_bibtex(bibtex_content: str) -> list[str]:
    """Split BibTeX content into individual entries."""
    import re

    comment_free = "\n".join(
        line for line in bibtex_content.splitlines() if not line.strip().startswith("%")
    )
    return [
        entry.strip() for entry in re.split(r"(?=@)", comment_free) if entry.strip()
    ]


def parse_bibtex_entry(bibtex_str: str) -> dict:
    """Parse a single BibTeX entry into a dictionary of fields."""
    import bibtexparser

    return bibtexparser.loads(bibtex_str).entries[0]


def _normalize_bibtex_entry(bibtex_str: str) -> str:
    normalized = bibtex_str
    for macro, replacement in MACRO_REPLACE_MAP.items():
        normalized = normalized.replace(f"\\{macro}", replacement)
    return normalized


def try_format_bibtex_entry(bibtex_entry: str, style: str = "harvard1") -> str:
    """Format a BibTeX entry with citeproc, raising on failures."""
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

    normalized_entry = _normalize_bibtex_entry(bibtex_entry)

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message="Unsupported BibTeX field")
        source = BibTeX(io.StringIO(normalized_entry))
        citation_style = CitationStylesStyle(style, validate=False)
        bibliography = CitationStylesBibliography(
            citation_style, source, formatter.plain
        )

        parsed_entry = parse_bibtex_entry(normalized_entry)
        if "ID" not in parsed_entry:
            raise ValueError("BibTeX entry must contain an 'ID' field.")

        citation = Citation([CitationItem(parsed_entry["ID"])])
        bibliography.register(citation)
        return "".join(bibliography.bibliography()[0])


def format_bibtex_entry(bibtex_entry: str, style: str = "harvard1") -> str:
    """Format a BibTeX entry, falling back to the raw string on errors."""
    try:
        return try_format_bibtex_entry(bibtex_entry, style)
    except Exception:
        return bibtex_entry
