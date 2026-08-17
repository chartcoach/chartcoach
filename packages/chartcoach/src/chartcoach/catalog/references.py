from __future__ import annotations

import dataclasses as dc
from collections.abc import Mapping, Sequence
from types import MappingProxyType
from typing import TYPE_CHECKING

import bibtexparser
import polars as pl

from ..constants import DEFAULT_GUIDELINE_URL_TEMPLATE
from ._polars import explode_frame
from .errors import CatalogValidationError
from .schemas import (
    GUIDELINE_REFERENCES_SCHEMA,
    GUIDELINE_SOURCES_SCHEMA,
    REFERENCES_SCHEMA,
)

if TYPE_CHECKING:
    from .collection import Catalog

CITATION_SOURCE_COLUMNS = (
    "reference_id",
    "source_type",
    "authors_text",
    "year",
    "source_title",
    "journal",
    "booktitle",
    "publisher",
    "doi",
    "url",
)


@dc.dataclass(frozen=True, slots=True)
class ParsedBibtexEntry:
    """One parsed BibTeX entry plus its serialized BibTeX."""

    entry: Mapping[str, object]
    bibtex: str

    @property
    def id(self) -> str:
        value = self.entry.get("ID")
        if not isinstance(value, str) or not value:
            raise ValueError("BibTeX entry must contain an 'ID' field.")
        return value


@dc.dataclass(frozen=True, slots=True)
class ReferenceTables:
    references: pl.DataFrame
    guideline_references: pl.DataFrame


def parse_bibtex(bibtex_content: str) -> list[str]:
    """Return individual BibTeX entries parsed from a `.bib` file."""

    database = bibtexparser.loads(bibtex_content)
    return [_dump_bibtex_entry(entry) for entry in database.entries]


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


def build_reference_tables(catalog_df: pl.DataFrame) -> ReferenceTables:
    """Build parsed reference tables in one BibTeX parse pass."""

    exploded = (
        explode_frame(
            catalog_df.select(
                pl.col("id").alias("guideline_id"),
                pl.col("references").alias("bibtex"),
            ),
            "bibtex",
        )
        .drop_nulls("bibtex")
        .unique()
    )
    if exploded.is_empty():
        return ReferenceTables(
            references=pl.DataFrame(schema=REFERENCES_SCHEMA),
            guideline_references=pl.DataFrame(schema=GUIDELINE_REFERENCES_SCHEMA),
        )

    bibtex_to_id: dict[str, str] = {}
    reference_rows: list[dict[str, object]] = []
    seen_reference_ids: set[str] = set()
    for bibtex in exploded.select("bibtex").unique().get_column("bibtex").to_list():
        if not isinstance(bibtex, str):
            continue
        reference = parse_bibtex_reference(bibtex)
        parsed = reference.entry
        reference_id = reference.id
        bibtex_to_id[bibtex] = reference_id
        if reference_id in seen_reference_ids:
            continue
        seen_reference_ids.add(reference_id)

        authors_text = _string_or_none(parsed.get("author"))
        reference_rows.append(
            {
                "id": reference_id,
                "source_type": _entry_type_or_none(parsed.get("ENTRYTYPE")),
                "authors": _split_authors(authors_text),
                "authors_text": authors_text,
                "year": _string_or_none(parsed.get("year")),
                "title": _string_or_none(parsed.get("title")),
                "journal": _string_or_none(parsed.get("journal")),
                "booktitle": _string_or_none(parsed.get("booktitle")),
                "publisher": _string_or_none(parsed.get("publisher")),
                "url": _string_or_none(parsed.get("url")),
                "doi": _string_or_none(parsed.get("doi")),
                "bibtex": bibtex,
            }
        )
    edge_rows = [
        {"guideline_id": str(guideline_id), "reference_id": bibtex_to_id[bibtex]}
        for guideline_id, bibtex in exploded.iter_rows()
        if isinstance(bibtex, str) and bibtex in bibtex_to_id
    ]

    return ReferenceTables(
        references=(
            pl.DataFrame(reference_rows, schema=REFERENCES_SCHEMA)
            .unique("id")
            .sort("id")
        ),
        guideline_references=(
            pl.DataFrame(edge_rows, schema=GUIDELINE_REFERENCES_SCHEMA)
            .unique()
            .sort("guideline_id", "reference_id")
        ),
    )


def build_guideline_sources_df(
    guideline_references_df: pl.DataFrame,
    references_df: pl.DataFrame,
) -> pl.DataFrame:
    """Build a dataframe of guideline-to-source rows for SQL joins."""

    if guideline_references_df.is_empty() or references_df.is_empty():
        return pl.DataFrame(schema=GUIDELINE_SOURCES_SCHEMA)
    sources = references_df.rename(
        {
            "id": "reference_id",
            "title": "source_title",
        }
    )
    return (
        guideline_references_df.join(sources, on="reference_id", how="left")
        .select(list(GUIDELINE_SOURCES_SCHEMA))
        .cast(pl.Schema(GUIDELINE_SOURCES_SCHEMA))
        .sort("guideline_id", "reference_id")
    )


def citation_records(
    catalog: Catalog,
    *,
    ids: Sequence[str],
    url_template: str = DEFAULT_GUIDELINE_URL_TEMPLATE,
) -> list[dict[str, object]]:
    from .query import validate_ids

    validate_ids(catalog, ids)
    validate_url_template(url_template)
    if not ids:
        return []

    order = pl.DataFrame({"id": list(ids), "_catalog_order": range(len(ids))})
    guideline_rows = (
        order.join(catalog.guidelines().select("id", "title"), on="id", how="inner")
        .sort("_catalog_order")
        .drop("_catalog_order")
        .to_dicts()
    )
    sources_by_guideline: dict[str, list[dict[str, object]]] = {
        str(guideline_id): [] for guideline_id in ids
    }
    source_frame = catalog.guideline_sources().filter(pl.col("guideline_id").is_in(ids))
    if not source_frame.is_empty():
        for row in source_frame.sort("guideline_id", "reference_id").to_dicts():
            guideline_id = str(row["guideline_id"])
            sources_by_guideline.setdefault(guideline_id, []).append(
                citation_source_from_row(row)
            )

    records: list[dict[str, object]] = []
    for row in guideline_rows:
        guideline_id = str(row["id"])
        title = str(row["title"])
        url = url_template.replace("{id}", guideline_id)
        records.append(
            {
                "id": guideline_id,
                "title": title,
                "url": url,
                "guideline_citation": guideline_citation(title, guideline_id, url),
                "sources": sources_by_guideline.get(guideline_id, []),
            }
        )
    return records


def citation_source_from_row(row: Mapping[str, object]) -> dict[str, object]:
    source = {
        column: row.get(column) for column in CITATION_SOURCE_COLUMNS if column in row
    }
    source["citation"] = source_citation(source)
    return source


def guideline_citation(title: str, guideline_id: str, url: str) -> str:
    return f"[{title}]({url}) (`{guideline_id}`)"


def source_citation(source: Mapping[str, object]) -> str:
    authors = _clean_source_part(source.get("authors_text"))
    year = _clean_source_part(source.get("year"))
    title = _clean_source_part(source.get("source_title"))
    container = _clean_source_part(source.get("journal")) or _clean_source_part(
        source.get("booktitle")
    )
    publisher = _clean_source_part(source.get("publisher"))
    doi = _clean_source_part(source.get("doi"))
    url = _clean_source_part(source.get("url"))

    first = ""
    if authors and year:
        first = f"{authors} ({year})"
    elif authors:
        first = authors
    elif year:
        first = f"({year})"

    parts = [part for part in (first, title, container, publisher) if part]
    citation = ". ".join(part.rstrip(".") for part in parts)
    if not citation:
        citation = str(source.get("reference_id") or "Source")
    if not citation.endswith("."):
        citation += "."

    links = [_doi_url(doi) if doi else "", url or ""]
    visible_links = [link for link in links if link]
    if visible_links:
        citation = f"{citation} {' '.join(visible_links)}"
    return citation


def validate_url_template(url_template: str) -> None:
    if "{id}" not in url_template:
        raise CatalogValidationError(
            "Guideline URL template must include `{id}`.",
            hints=(f"Use a template such as `{DEFAULT_GUIDELINE_URL_TEMPLATE}`.",),
        )


def _dump_bibtex_entry(entry: Mapping[str, object]) -> str:
    database = bibtexparser.bibdatabase.BibDatabase()
    database.entries = [dict(entry)]
    return bibtexparser.dumps(database).strip()


def _string_or_none(value: object) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _split_authors(authors_text: str | None) -> list[str]:
    if authors_text is None:
        return []
    return [part.strip() for part in authors_text.split(" and ") if part.strip()]


def _entry_type_or_none(value: object) -> str | None:
    text = _string_or_none(value)
    if text is None:
        return None
    return text.lower()


def _clean_source_part(value: object) -> str:
    return str(value or "").strip()


def _doi_url(doi: str) -> str:
    normalized = doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    return f"https://doi.org/{normalized}"


__all__ = [
    "DEFAULT_GUIDELINE_URL_TEMPLATE",
    "ParsedBibtexEntry",
    "ReferenceTables",
    "build_guideline_sources_df",
    "build_reference_tables",
    "citation_records",
    "citation_source_from_row",
    "guideline_citation",
    "parse_bibtex",
    "parse_bibtex_reference",
    "source_citation",
]
