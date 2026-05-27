from __future__ import annotations

import dataclasses as dc
from collections.abc import Mapping
from functools import cache
from types import MappingProxyType
from typing import Any

import bibtexparser


@dc.dataclass(frozen=True, slots=True)
class ParsedBibtexEntry:
    """One parsed BibTeX entry plus its serialized BibTeX."""

    entry: Mapping[str, Any]
    bibtex: str

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
    )


def _dump_bibtex_entry(entry: dict[str, Any]) -> str:
    database = bibtexparser.bibdatabase.BibDatabase()
    database.entries = [entry]
    return bibtexparser.dumps(database).strip()
