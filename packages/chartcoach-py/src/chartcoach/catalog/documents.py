from __future__ import annotations

from collections.abc import Mapping, Sequence

import polars as pl


def build_docs_df(
    guidelines_df: pl.DataFrame, references_df: pl.DataFrame
) -> pl.DataFrame:
    """Build the embedding/document dataframe used by CatalogIndex."""
    import polars_hash as plh

    docs_df = pl.concat(
        [
            _build_toplevel_docs_df(guidelines_df),
            _build_section_docs_df(guidelines_df, references_df),
        ],
        how="vertical",
    ).sort("id")

    return docs_df.with_columns(
        metadata=pl.struct(
            parent_id=pl.col("metadata").struct.field("parent_id"),
            role=pl.col("metadata").struct.field("role"),
            labels=pl.col("metadata").struct.field("labels"),
            content_hash=plh.col("doc").chash.sha2_256(),
        )
    )


def _build_toplevel_docs_df(guidelines_df: pl.DataFrame) -> pl.DataFrame:
    return (
        guidelines_df.select(
            "id",
            overview=pl.concat_str(["title", "description"], separator="\n\n"),
            labels="labels",
        )
        .unpivot(
            index=["id", "labels"],
            variable_name="role",
            value_name="doc",
        )
        .select(
            id=pl.concat_str(["id", "role"], separator="---"),
            doc="doc",
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
            doc="content",
            metadata=pl.struct(
                parent_id="id",
                role=pl.concat_str([pl.lit("section"), "role"], separator="."),
                labels="labels",
            ),
        )
        .with_columns(
            reference_context=pl.col("doc")
            .str.extract_all(r"@[\w\.-]+")
            .list.eval(pl.element().str.replace_all(r"^@", ""))
            .map_elements(
                lambda citekeys: _format_reference_context(citekeys, reference_map),
                return_dtype=pl.String,
            )
        )
        .with_columns(
            doc=pl.when(pl.col("doc").str.contains("[@", literal=True))
            .then(
                pl.concat_str(
                    ["doc", pl.lit("\n**References**\n"), "reference_context"],
                    separator="\n",
                )
            )
            .otherwise("doc")
        )
        .drop("reference_context")
    )


def _build_reference_map(references_df: pl.DataFrame) -> dict[str, str]:
    return {
        ref_id: formatted
        for ref_id, formatted in references_df.select("id", "formatted").iter_rows()
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
