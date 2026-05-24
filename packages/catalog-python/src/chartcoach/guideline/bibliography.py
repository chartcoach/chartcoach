from __future__ import annotations

import dataclasses as dc
import io
import warnings
from collections.abc import Mapping
from functools import cache
from types import MappingProxyType
from typing import Any

import bibtexparser
from citeproc import (
    Citation,
    CitationItem,
    CitationStylesBibliography,
    CitationStylesStyle,
    formatter,
)
from citeproc.source.bibtex import BibTeX

MACRO_REPLACE_MAP = {
    "textraquo": "»",
    "textgreater": ">",
    "textless": "<",
    "!": "",
    "?": "?",
    "\\": "",
    "[": "",
    "]": "",
    "{": "",
    "}": "",
}


@dc.dataclass(frozen=True, slots=True)
class ParsedBibtexEntry:
    """One parsed BibTeX entry plus the serialized BibTeX used by citeproc."""

    entry: Mapping[str, Any]
    bibtex: str
    normalized_bibtex: str

    @property
    def id(self) -> str:
        value = self.entry.get("ID")
        if not isinstance(value, str) or not value:
            raise ValueError("BibTeX entry must contain an 'ID' field.")
        return value


def parse_bibtex(bibtex_content: str) -> list[str]:
    """Return individual BibTeX entries parsed from a `.bib` file."""

    database = bibtexparser.loads(bibtex_content)
    return [_dump_bibtex_entry(entry) for entry in database.entries]


def parse_bibtex_entry(bibtex_str: str) -> dict[str, Any]:
    """Parse a single BibTeX entry into a dictionary of fields."""
    return dict(parse_bibtex_reference(bibtex_str).entry)


@cache
def parse_bibtex_reference(bibtex_str: str) -> ParsedBibtexEntry:
    """Parse one BibTeX reference and retain its normalized serialized form."""

    database = bibtexparser.loads(bibtex_str)
    if not database.entries:
        preview = bibtex_str.strip().replace("\n", " ")[:80]
        raise ValueError(f"No BibTeX entry parsed from input: {preview!r}.")
    if len(database.entries) != 1:
        raise ValueError(f"Expected one BibTeX entry, found {len(database.entries)}.")
    entry = dict(database.entries[0])
    bibtex = _dump_bibtex_entry(entry)
    return ParsedBibtexEntry(
        entry=MappingProxyType(entry),
        bibtex=bibtex,
        normalized_bibtex=_normalize_bibtex_entry(bibtex),
    )


def _normalize_bibtex_entry(bibtex_str: str) -> str:
    normalized = bibtex_str
    for macro, replacement in MACRO_REPLACE_MAP.items():
        normalized = normalized.replace(f"\\{macro}", replacement)
    return normalized


@cache
def format_bibtex_entry(bibtex_entry: str, style: str = "harvard1") -> str:
    """Format a BibTeX entry with citeproc, raising on failures."""
    return format_bibtex_reference(parse_bibtex_reference(bibtex_entry), style=style)


def format_bibtex_reference(
    parsed: ParsedBibtexEntry,
    *,
    style: str = "harvard1",
) -> str:
    """Format an already parsed BibTeX entry with citeproc."""
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message="Unsupported BibTeX field")
        source = BibTeX(io.StringIO(parsed.normalized_bibtex))
        citation_style = CitationStylesStyle(style, validate=False)
        bibliography = CitationStylesBibliography(
            citation_style, source, formatter.plain
        )

        citation = Citation([CitationItem(parsed.id)])
        bibliography.register(citation)
        return "".join(bibliography.bibliography()[0])


def _dump_bibtex_entry(entry: dict[str, Any]) -> str:
    database = bibtexparser.bibdatabase.BibDatabase()
    database.entries = [entry]
    return bibtexparser.dumps(database).strip()
