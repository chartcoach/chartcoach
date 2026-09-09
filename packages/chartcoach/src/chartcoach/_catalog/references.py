from __future__ import annotations

import dataclasses as dc
import re
from collections.abc import Mapping, Sequence
from types import MappingProxyType
from typing import TYPE_CHECKING, cast

import polars as pl
import polars_refkit
import refkit
from typing_extensions import TypedDict

from .._constants import DEFAULT_GUIDELINE_URL_TEMPLATE
from ._polars import explode_frame
from .errors import CatalogValidationError
from .schemas import (
    GUIDELINE_REFERENCES_SCHEMA,
    GUIDELINE_SOURCES_SCHEMA,
    REFERENCES_SCHEMA,
)

if TYPE_CHECKING:
    from .model import Catalog

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
class ReferenceTables:
    references: pl.DataFrame
    guideline_references: pl.DataFrame
    citations: Mapping[str, str]


class CitationSource(TypedDict):
    """One formatted source attached to a guideline citation."""

    reference_id: str
    source_type: str | None
    authors_text: str | None
    year: str | None
    source_title: str | None
    journal: str | None
    booktitle: str | None
    publisher: str | None
    doi: str | None
    url: str | None
    citation: str


class CitationRecord(TypedDict):
    """One public guideline citation and its source citations."""

    id: str
    title: str
    url: str
    guideline_citation: str
    sources: list[CitationSource]


def parse_bibtex(bibtex_content: str) -> list[str]:
    """Return self-contained BibTeX entries from a bibliography."""

    document = _parse_document(bibtex_content)
    source = bibtex_content.encode("utf-8")
    context = [
        source[block["span"][0] : block["span"][1]].decode("utf-8")
        for block in document.blocks
        if block["kind"] in {"string", "preamble"}
    ]
    return [
        "\n".join([*context, source[entry.span[0] : entry.span[1]].decode("utf-8")])
        for entry in document.entries.occurrences()
    ]


def parse_bibtex_reference(bibtex_str: str) -> refkit.types.ResolvedBibEntry:
    """Resolve the source fields of one BibTeX reference."""

    document = _parse_document(bibtex_str)
    try:
        entries = document.resolve()
    except refkit.ParseError as exc:
        raise CatalogValidationError(
            "Invalid BibTeX reference.", details={"diagnostics": exc.diagnostics}
        ) from exc
    if not entries:
        preview = bibtex_str.strip().replace("\n", " ")[:80]
        raise ValueError(f"No BibTeX entry parsed from input: {preview!r}.")
    if len(entries) != 1:
        raise ValueError(f"Expected one BibTeX entry, found {len(entries)}.")
    return entries[0]


def _parse_document(source: str) -> refkit.BibDocument:
    document = refkit.BibDocument.parse(source)
    if document.failed_blocks:
        raise CatalogValidationError(
            "Invalid BibTeX bibliography.",
            details={"failed_blocks": document.failed_blocks},
        )
    return document


def build_reference_tables(catalog_df: pl.DataFrame) -> ReferenceTables:
    """Build source records and cached APA citations for distinct references."""

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
            citations=MappingProxyType({}),
        )

    bibtex_to_id: dict[str, str] = {}
    reference_rows: list[dict[str, object]] = []
    references_by_id: dict[str, refkit.types.ResolvedBibEntry] = {}
    for bibtex in exploded.select("bibtex").unique().get_column("bibtex").to_list():
        if not isinstance(bibtex, str):
            continue
        reference = parse_bibtex_reference(bibtex)
        parsed = reference["fields"]
        reference_id = reference["key"]
        bibtex_to_id[bibtex] = reference_id
        previous = references_by_id.get(reference_id)
        if previous is not None:
            if previous != reference:
                raise CatalogValidationError(
                    f"Conflicting BibTeX definitions for reference id: {reference_id}.",
                    details={"reference_id": reference_id},
                )
            continue
        references_by_id[reference_id] = reference

        authors_text = _string_or_none(parsed.get("author"))
        reference_rows.append(
            {
                "id": reference_id,
                "source_type": reference["entry_type"],
                "authors": _split_authors(authors_text),
                "authors_text": authors_text,
                "year": _string_or_none(parsed.get("year")),
                "title": _string_or_none(parsed.get("title")),
                "journal": _string_or_none(parsed.get("journal")),
                "booktitle": _string_or_none(parsed.get("booktitle")),
                "publisher": _string_or_none(parsed.get("publisher")),
                "url": _reference_url(parsed),
                "doi": _string_or_none(parsed.get("doi")),
                "bibtex": bibtex,
            }
        )
    edge_rows = [
        {"guideline_id": str(guideline_id), "reference_id": bibtex_to_id[bibtex]}
        for guideline_id, bibtex in exploded.iter_rows()
        if isinstance(bibtex, str) and bibtex in bibtex_to_id
    ]

    references = pl.DataFrame(reference_rows, schema=REFERENCES_SCHEMA).sort("id")
    rendered = references.select(
        "id",
        "doi",
        "url",
        polars_refkit.full_bibliography(
            polars_refkit.tidy_bibtex(pl.col("bibtex")),
            style="apa",
            locale="en-US",
            recovery="report",
        ).alias("citation"),
    )
    citations = {}
    for reference_id, doi, url, citation in rendered.iter_rows():
        if citation is None:
            raise CatalogValidationError(
                f"Could not render BibTeX reference: {reference_id}.",
                details={"reference_id": reference_id},
            )
        doi_url = (
            "https://doi.org/"
            + doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
            if doi
            else None
        )
        # CSL styles can omit a publication URL when a DOI is present.
        for locator in (doi_url, url):
            if locator and locator not in citation:
                citation = f"{citation} {locator}"
        citations[reference_id] = citation

    return ReferenceTables(
        references=references,
        guideline_references=(
            pl.DataFrame(edge_rows, schema=GUIDELINE_REFERENCES_SCHEMA)
            .unique()
            .sort("guideline_id", "reference_id")
        ),
        citations=MappingProxyType(citations),
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
) -> list[CitationRecord]:
    """Return public guideline links and source citations for guideline entry IDs.

    Each result contains `id`, `title`, `url`, `guideline_citation`, and a
    `sources` list. The default URL template targets the public catalog site.
    """

    from .query import validate_ids

    validate_ids(catalog, ids)
    validate_url_template(url_template)
    if not ids:
        return []

    order = pl.DataFrame({"id": list(ids), "_catalog_order": range(len(ids))})
    guideline_rows = (
        order.join(
            catalog.table("guidelines").select("id", "title"),
            on="id",
            how="inner",
        )
        .sort("_catalog_order")
        .drop("_catalog_order")
        .to_dicts()
    )
    sources_by_guideline: dict[str, list[CitationSource]] = {
        str(guideline_id): [] for guideline_id in ids
    }
    source_frame = catalog.table("guideline_sources").filter(
        pl.col("guideline_id").is_in(ids)
    )
    if not source_frame.is_empty():
        citations = catalog._reference_tables().citations
        for row in source_frame.sort("guideline_id", "reference_id").to_dicts():
            guideline_id = str(row["guideline_id"])
            sources_by_guideline.setdefault(guideline_id, []).append(
                citation_source_from_row(row, citations[str(row["reference_id"])])
            )

    records: list[CitationRecord] = []
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


def citation_source_from_row(
    row: Mapping[str, object], citation: str
) -> CitationSource:
    source = {
        column: row.get(column) for column in CITATION_SOURCE_COLUMNS if column in row
    }
    source["citation"] = citation
    return cast(CitationSource, source)


def guideline_citation(title: str, guideline_id: str, url: str) -> str:
    return f"[{title}]({url}) (`{guideline_id}`)"


def validate_url_template(url_template: str) -> None:
    if "{id}" not in url_template:
        raise CatalogValidationError(
            "Guideline URL template must include `{id}`.",
            hints=(f"Use a template such as `{DEFAULT_GUIDELINE_URL_TEMPLATE}`.",),
        )


def _string_or_none(value: object) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _reference_url(entry: Mapping[str, object]) -> str | None:
    explicit = _string_or_none(entry.get("url"))
    value = explicit or _string_or_none(entry.get("howpublished"))
    if value is None:
        return None
    wrapped = re.fullmatch(r"\\url\{([^{}]*)\}", value)
    candidate = wrapped.group(1) if wrapped else value
    if re.fullmatch(r"https?://[^\s{}\\/?#]+[^\s{}\\]*", candidate, re.IGNORECASE):
        return candidate
    return explicit


def _split_authors(authors_text: str | None) -> list[str]:
    if authors_text is None:
        return []
    return [part.strip() for part in authors_text.split(" and ") if part.strip()]


__all__ = [
    "DEFAULT_GUIDELINE_URL_TEMPLATE",
    "CitationRecord",
    "CitationSource",
    "ReferenceTables",
    "build_guideline_sources_df",
    "build_reference_tables",
    "citation_records",
    "citation_source_from_row",
    "guideline_citation",
    "parse_bibtex",
    "parse_bibtex_reference",
]
