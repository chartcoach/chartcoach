from __future__ import annotations

from collections.abc import Mapping, Sequence

import polars as pl


def build_docs_df(
    guidelines_df: pl.DataFrame, references_df: pl.DataFrame
) -> pl.DataFrame:
    """Build the text records used by the search index."""
    docs_df = pl.concat(
        [
            _build_toplevel_docs_df(guidelines_df),
            _build_section_docs_df(guidelines_df, references_df),
        ],
        how="vertical",
    ).sort("id")

    return docs_df.with_columns(
        metadata=pl.struct(
            pl.col("metadata").struct.field("parent_id").alias("parent_id"),
            pl.col("metadata").struct.field("role").alias("role"),
            pl.col("metadata").struct.field("labels").alias("labels"),
            pl.when(pl.col("text").is_null())
            .then(None)
            .otherwise(pl.col("text").hash().cast(pl.String))
            .alias("content_hash"),
        )
    )


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
            text="text",
            metadata=pl.struct(
                parent_id="id",
                role="role",
                labels="labels",
            ),
        )
    )


def _build_section_docs_df(
    guidelines_df: pl.DataFrame,
    references_df: pl.DataFrame,
) -> pl.DataFrame:
    reference_map = _build_reference_map(references_df)

    return (
        guidelines_df.select("id", "sections", "labels")
        .explode("sections")
        .unnest("sections")
        .select(
            id=pl.concat_str(["id", pl.lit("role"), "role"], separator="---"),
            text="content",
            metadata=pl.struct(
                parent_id="id",
                role=pl.concat_str([pl.lit("section"), "role"], separator="."),
                labels="labels",
            ),
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


__all__ = ["build_docs_df"]
