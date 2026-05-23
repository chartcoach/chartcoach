from __future__ import annotations

from collections.abc import Sequence

import polars as pl

from ..catalog.collection import Catalog, CatalogEntry
from ..catalog.relations import catalog_relations


class CatalogToolError(ValueError):
    """Actionable error raised by reusable catalog tools."""

    def __init__(self, message: str, *, hints: Sequence[str] = ()) -> None:
        super().__init__(message)
        self.message = message
        self.hints = tuple(hints)

    def __str__(self) -> str:
        return format_tool_error(self.message, self.hints)


class CatalogTools:
    """Deterministic tools for discovering and reading visualization knowledge.

    This layer is transport-agnostic. The CLI formats its returned rows for
    shells, and the MCP server exposes the same methods as tools for agents.
    """

    def __init__(self, catalog: Catalog) -> None:
        self._catalog = catalog

    @property
    def catalog(self) -> Catalog:
        """Return the source catalog."""

        return self._catalog

    def relations(self) -> list[dict[str, object]]:
        """List queryable structured relations and row counts."""

        return [
            {"name": relation_name, "rows": frame.height}
            for relation_name, frame in catalog_relations(self.catalog).items()
        ]

    def schema(
        self,
        relations: Sequence[str] = (),
    ) -> list[dict[str, object]]:
        """List columns for structured catalog relations."""

        relation_frames = catalog_relations(self.catalog)
        selected_relations = set(relations)
        unknown_relations = sorted(selected_relations - set(relation_frames))
        if unknown_relations:
            raise self._unknown_relation_error(unknown_relations)

        rows: list[dict[str, object]] = []
        for relation, frame in relation_frames.items():
            if selected_relations and relation not in selected_relations:
                continue
            for column, dtype in frame.schema.items():
                rows.append(
                    {
                        "relation": relation,
                        "column": column,
                        "type": str(dtype),
                    }
                )
        return rows

    def values(
        self,
        relation: str,
        column: str,
        *,
        explode: bool = False,
        contains: str | None = None,
        limit: int = 50,
    ) -> list[dict[str, object]]:
        """Count distinct values in any structured relation column."""

        frame = self._require_relation(relation)
        self._require_column(relation, frame, column)
        dtype = frame.schema[column]
        if _is_list_dtype(dtype) and not explode:
            raise CatalogToolError(
                f"Column {relation}.{column} is list-valued.",
                hints=[
                    "Pass explode=True to count each list item separately.",
                    f"CLI: chartcoach catalog --catalog PATH values {relation} {column} --explode --format jsonl",
                ],
            )

        value_expr = pl.col(column).explode() if explode else pl.col(column)
        values = frame.select(value_expr.alias("value")).filter(
            pl.col("value").is_not_null()
        )
        values = values.with_columns(pl.col("value").cast(pl.String).alias("value"))
        if contains:
            needle = contains.lower()
            values = values.filter(
                pl.col("value").str.to_lowercase().str.contains(needle, literal=True)
            )

        return (
            values.group_by("value")
            .len("rows")
            .sort(["rows", "value"], descending=[True, False])
            .head(limit)
            .with_columns(
                pl.lit(relation).alias("relation"),
                pl.lit(column).alias("column"),
            )
            .select("relation", "column", "value", "rows")
            .to_dicts()
        )

    def list_guidelines(
        self,
        *,
        labels: Sequence[str] = (),
        contains: str | None = None,
        limit: int = 50,
    ) -> list[dict[str, object]]:
        """List guideline ids and summaries with deterministic filters."""

        self._validate_labels(labels)
        df = self.catalog.guidelines_df.select(
            "id",
            "title",
            "description",
            "labels",
        )
        for label_value in labels:
            df = df.filter(pl.col("labels").list.contains(label_value))
        if contains:
            needle = contains.lower()
            df = df.filter(
                pl.any_horizontal(
                    pl.col("id").str.to_lowercase().str.contains(needle, literal=True),
                    pl.col("title")
                    .str.to_lowercase()
                    .str.contains(needle, literal=True),
                    pl.col("description")
                    .str.to_lowercase()
                    .str.contains(needle, literal=True),
                )
            )
        return df.head(limit).to_dicts()

    def get_guideline(self, guideline_id: str) -> dict[str, object]:
        """Return one complete guideline entry by id."""

        return self._get_entry(guideline_id).model_dump()

    def retrieve_guidelines(
        self,
        *,
        ids: Sequence[str] = (),
        labels: Sequence[str] = (),
        label_prefixes: Sequence[str] = (),
        contains: str | None = None,
        roles: Sequence[str] = (),
        limit: int = 12,
    ) -> list[dict[str, object]]:
        """Return guideline records with optional label and section filters."""

        resolved_roles = self.validate_guideline_filters(
            labels=labels,
            label_prefixes=label_prefixes,
            roles=roles,
        )
        entries = self._query_entries(
            ids=ids,
            labels=labels,
            label_prefixes=label_prefixes,
            contains=contains,
            limit=limit,
        )

        return [
            guideline_record(
                entry,
                roles=set(resolved_roles) if resolved_roles else None,
            )
            for entry in entries
        ]

    def validate_guideline_filters(
        self,
        *,
        labels: Sequence[str] = (),
        label_prefixes: Sequence[str] = (),
        roles: Sequence[str] = (),
    ) -> tuple[str, ...]:
        """Validate reusable guideline filters and return normalized roles."""

        self._validate_labels(labels)
        self._validate_label_prefixes(label_prefixes)
        resolved_roles = normalize_section_roles(roles)
        self._validate_section_roles(resolved_roles)
        return resolved_roles

    def _get_entry(self, guideline_id: str) -> CatalogEntry:
        try:
            return self.catalog.get(guideline_id)
        except KeyError as exc:
            raise self._unknown_id_error(guideline_id) from exc

    def _query_entries(
        self,
        *,
        ids: Sequence[str],
        labels: Sequence[str],
        label_prefixes: Sequence[str],
        contains: str | None,
        limit: int,
    ) -> tuple[CatalogEntry, ...]:
        entries = [self._get_entry(guideline_id) for guideline_id in ids]
        if not ids:
            entries = list(self.catalog.entries)

        for label in labels:
            entries = [entry for entry in entries if label in entry.guideline.labels]
        for prefix in label_prefixes:
            entries = [
                entry
                for entry in entries
                if any(label.startswith(prefix) for label in entry.guideline.labels)
            ]
        if contains:
            needle = contains.lower()
            entries = [
                entry for entry in entries if needle in _query_text(entry).lower()
            ]
        return tuple(entries[:limit])

    def _require_relation(self, relation: str) -> pl.DataFrame:
        relation_frames = catalog_relations(self.catalog)
        if relation not in relation_frames:
            raise self._unknown_relation_error([relation])
        return relation_frames[relation]

    def _require_column(
        self,
        relation: str,
        frame: pl.DataFrame,
        column: str,
    ) -> None:
        if column not in frame.columns:
            raise self._unknown_column_error(relation, frame, column)

    def _distinct_strings(
        self,
        *,
        relation: str,
        column: str,
        explode: bool = False,
    ) -> set[str]:
        frame = self._require_relation(relation)
        self._require_column(relation, frame, column)
        value_expr = pl.col(column).explode() if explode else pl.col(column)
        values = (
            frame.select(value_expr.alias("value"))
            .filter(pl.col("value").is_not_null())
            .with_columns(pl.col("value").cast(pl.String).alias("value"))
            .get_column("value")
            .to_list()
        )
        return {value for value in values if isinstance(value, str)}

    def _validate_labels(self, labels: Sequence[str]) -> None:
        if not labels:
            return
        available = self._distinct_strings(
            relation="guideline_labels",
            column="label",
        )
        missing = sorted(set(labels) - available)
        if missing:
            raise CatalogToolError(
                f"Unknown label(s): {', '.join(missing)}",
                hints=[
                    "Discover labels with the values tool: relation='guideline_labels', column='label'.",
                    "CLI: chartcoach catalog --catalog PATH values guideline_labels label --format jsonl | head",
                ],
            )

    def _validate_label_prefixes(self, prefixes: Sequence[str]) -> None:
        if not prefixes:
            return
        available = self._distinct_strings(
            relation="guideline_labels",
            column="label",
        )
        missing = [
            prefix
            for prefix in sorted(set(prefixes))
            if not any(label.startswith(prefix) for label in available)
        ]
        if missing:
            raise CatalogToolError(
                f"No labels match prefix(es): {', '.join(missing)}",
                hints=[
                    "Discover labels with the values tool: relation='guideline_labels', column='label'.",
                    "Use exact labels once you have found a value to keep.",
                ],
            )

    def _validate_section_roles(self, roles: Sequence[str]) -> None:
        if not roles:
            return
        available = self._distinct_strings(relation="sections", column="role")
        missing = sorted(set(roles) - available)
        if missing:
            raise CatalogToolError(
                f"Unknown section role(s): {', '.join(missing)}",
                hints=[
                    "Discover roles with the values tool: relation='sections', column='role'.",
                    "CLI: chartcoach catalog --catalog PATH values sections role --format jsonl",
                    "Use roles exactly as returned, or omit roles to include every section.",
                ],
            )

    def _unknown_relation_error(self, relations: Sequence[str]) -> CatalogToolError:
        available = ", ".join(catalog_relations(self.catalog).keys())
        return CatalogToolError(
            f"Unknown relation(s): {', '.join(relations)}",
            hints=[
                f"Available relations: {available}",
                "Run the relations tool before schema, values, or SQL.",
                "CLI: chartcoach catalog --catalog PATH relations --format jsonl",
            ],
        )

    def _unknown_column_error(
        self,
        relation: str,
        frame: pl.DataFrame,
        column: str,
    ) -> CatalogToolError:
        columns = ", ".join(frame.columns)
        return CatalogToolError(
            f"Unknown column for relation {relation}: {column}",
            hints=[
                f"Available columns on {relation}: {columns}",
                f"Run schema with relation={relation!r} before calling values or SQL.",
                f"CLI: chartcoach catalog --catalog PATH schema --relation {relation} --format jsonl",
            ],
        )

    def _unknown_id_error(self, guideline_id: str) -> CatalogToolError:
        return CatalogToolError(
            f"Unknown guideline id: {guideline_id}",
            hints=[
                "Discover ids with list_guidelines.",
                "CLI: chartcoach catalog --catalog PATH list --format jsonl | head",
                "Search by text with search_guidelines or semantic search.",
            ],
        )


def guideline_record(
    entry: CatalogEntry,
    *,
    roles: set[str] | None,
) -> dict[str, object]:
    """Return the transport-neutral record shape for one guideline."""

    sections = [
        section.model_dump()
        for section in entry.guideline.sections
        if roles is None or section.role in roles
    ]
    return {
        "id": entry.id,
        "title": entry.guideline.title,
        "description": entry.guideline.description,
        "labels": list(entry.guideline.labels),
        "sections": sections,
    }


def normalize_section_roles(roles: Sequence[str]) -> tuple[str, ...]:
    """Accept raw section roles or indexed-document roles such as section.advice."""

    return tuple(role.removeprefix("section.") for role in roles)


def format_tool_error(message: str, hints: Sequence[str]) -> str:
    """Render an actionable tool error for CLI and MCP transports."""

    if not hints:
        return message
    joined_hints = "\n".join(f"  - {hint}" for hint in hints)
    return f"{message}\n\nTry:\n{joined_hints}"


def sql_error_message(message: str) -> str:
    """Return a recovery-oriented SQL error message."""

    return format_tool_error(
        message,
        [
            "Inspect relations with the relations tool.",
            "Inspect columns with the schema tool.",
            "CLI: chartcoach catalog --catalog PATH schema --format jsonl",
        ],
    )


def search_error_message(message: str) -> str:
    """Return a recovery-oriented semantic-search error message."""

    return format_tool_error(
        message,
        [
            "If the Chroma cache is missing, omit reuse_only or use reuse_or_create.",
            "Discover labels with the values tool before applying label filters.",
            "Use document-level search for raw Chroma metadata filters.",
        ],
    )


def _is_list_dtype(dtype: object) -> bool:
    return str(dtype).startswith("List")


def _query_text(entry: CatalogEntry) -> str:
    return "\n".join(
        [
            entry.id,
            entry.guideline.title,
            entry.guideline.description,
            entry.guideline.body,
        ]
    )


__all__ = [
    "CatalogToolError",
    "CatalogTools",
    "format_tool_error",
    "guideline_record",
    "normalize_section_roles",
    "search_error_message",
    "sql_error_message",
]
