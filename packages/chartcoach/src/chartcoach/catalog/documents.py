from __future__ import annotations

import hashlib
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

import polars as pl

from ._polars import explode_frame

if TYPE_CHECKING:
    from .model import Catalog

DOCUMENTS_VERSION = 1


def build_document_rows(
    guidelines_df: pl.DataFrame,
    references_df: pl.DataFrame,
) -> pl.DataFrame:
    """Build the flat document rows stored in catalog search indexes."""

    rows = (
        pl.concat(
            [
                _build_toplevel_docs_df(guidelines_df),
                _build_section_docs_df(guidelines_df, references_df),
            ],
            how="vertical",
        )
        .filter(pl.col("text").str.strip_chars() != "")
        .sort("id")
    )
    _validate_unique_document_ids(rows)

    return rows.with_columns(
        pl.col("text")
        .map_elements(_content_hash, return_dtype=pl.String)
        .alias("content_hash")
    ).select(
        "id",
        "parent_id",
        "role",
        "labels",
        "content_hash",
        "text",
    )


def document_rows(catalog: Catalog) -> pl.DataFrame:
    """Return the flat document rows for one catalog."""

    return build_document_rows(
        catalog.table("guidelines"),
        catalog.table("references"),
    )


def _content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _build_toplevel_docs_df(guidelines_df: pl.DataFrame) -> pl.DataFrame:
    return (
        guidelines_df.select(
            "id",
            overview=pl.concat_str(["title", "description"], separator="\n\n"),
            document=pl.concat_str(["title", "description", "body"], separator="\n\n"),
            labels="labels",
        )
        .unpivot(
            index=["id", "labels"],
            variable_name="role",
            value_name="text",
        )
        .select(
            id=pl.concat_str(["id", "role"], separator="---"),
            parent_id="id",
            role="role",
            labels="labels",
            text="text",
        )
    )


def _build_section_docs_df(
    guidelines_df: pl.DataFrame,
    references_df: pl.DataFrame,
) -> pl.DataFrame:
    reference_map = _build_reference_map(references_df)

    return (
        explode_frame(
            guidelines_df.select("id", "sections", "labels"),
            "sections",
        )
        .drop_nulls("sections")
        .unnest("sections")
        .with_columns(_role_occurrence=pl.col("role").cum_count().over(["id", "role"]))
        .select(
            id=pl.when(pl.col("_role_occurrence") == 1)
            .then(pl.concat_str(["id", pl.lit("role"), "role"], separator="---"))
            .otherwise(
                pl.concat_str(
                    [
                        "id",
                        pl.lit("role"),
                        "role",
                        pl.col("_role_occurrence").cast(pl.String),
                    ],
                    separator="---",
                )
            ),
            parent_id="id",
            role=pl.concat_str([pl.lit("section"), "role"], separator="."),
            labels="labels",
            text="content",
        )
        .with_columns(
            reference_context=pl.col("text")
            .str.extract_all(r"@[\w\.-]+")
            .list.eval(pl.element().str.replace_all(r"^@", ""))
            .map_elements(
                lambda citekeys: _format_reference_context(citekeys, reference_map),
                return_dtype=pl.String,
            )
        )
        .with_columns(
            text=pl.when(pl.col("text").str.contains("[@", literal=True))
            .then(
                pl.concat_str(
                    ["text", pl.lit("\nSources\n"), "reference_context"],
                    separator="\n",
                )
            )
            .otherwise("text")
        )
        .drop("reference_context")
    )


def _build_reference_map(references_df: pl.DataFrame) -> dict[str, str]:
    if references_df.is_empty():
        return {}
    return {
        str(row["id"]): _reference_context_from_row(row)
        for row in references_df.select(
            "id",
            "authors_text",
            "year",
            "title",
            "journal",
            "booktitle",
            "publisher",
            "doi",
            "url",
        ).iter_rows(named=True)
        if row.get("id") is not None
    }


def _format_reference_context(
    citekeys: Sequence[str] | pl.Series | None,
    reference_map: Mapping[str, str],
) -> str:
    values = citekeys.to_list() if isinstance(citekeys, pl.Series) else citekeys
    if not values:
        return ""

    lines = [
        f"- {citekey}: {reference_map[citekey]}"
        for citekey in sorted(set(values))
        if citekey in reference_map
    ]
    return "\n".join(lines)


def _reference_context_from_row(row: Mapping[str, object]) -> str:
    parts = [
        _text_or_none(row.get("authors_text")),
        _text_or_none(row.get("year")),
        _text_or_none(row.get("title")),
        _first_text(row, ("journal", "booktitle", "publisher")),
        _reference_locator(row),
    ]
    return ". ".join(part for part in parts if part)


def _first_text(row: Mapping[str, object], keys: Sequence[str]) -> str | None:
    for key in keys:
        value = _text_or_none(row.get(key))
        if value:
            return value
    return None


def _reference_locator(row: Mapping[str, object]) -> str | None:
    doi = _text_or_none(row.get("doi"))
    if doi:
        return f"DOI {doi}"
    return _text_or_none(row.get("url"))


def _text_or_none(value: object) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _validate_unique_document_ids(frame: pl.DataFrame) -> None:
    duplicate_ids = (
        frame.filter(pl.col("id").is_duplicated())
        .get_column("id")
        .unique()
        .sort()
        .to_list()
    )
    if duplicate_ids:
        raise ValueError(
            "Catalog documents contain duplicate document ids: "
            + ", ".join(duplicate_ids)
        )


__all__ = ["DOCUMENTS_VERSION", "build_document_rows", "document_rows"]
