from __future__ import annotations

from collections.abc import Mapping, Sequence

import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.tools import ToolError

from .navigation import validate_ids

DEFAULT_GUIDELINE_URL_TEMPLATE = "https://chartcoach.github.io/guidelines/{id}"
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


def citation_records(
    catalog: Catalog,
    *,
    ids: Sequence[str],
    url_template: str = DEFAULT_GUIDELINE_URL_TEMPLATE,
) -> list[dict[str, object]]:
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
    source = {column: row.get(column) for column in CITATION_SOURCE_COLUMNS if column in row}
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
        raise ToolError(
            "Guideline URL template must include `{id}`.",
            hints=[
                "Use a template such as `https://chartcoach.github.io/guidelines/{id}`."
            ],
        )


def _clean_source_part(value: object) -> str:
    return str(value or "").strip()


def _doi_url(doi: str) -> str:
    normalized = doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    return f"https://doi.org/{normalized}"
