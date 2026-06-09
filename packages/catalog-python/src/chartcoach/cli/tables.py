from __future__ import annotations

from collections.abc import Sequence

import click
import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.catalog.relations import (
    TABLE_SPECS,
    catalog_table_names,
    catalog_table_rows,
    catalog_table_schema,
)
from chartcoach.tools import ToolError, format_error

from .common import (
    CONTEXT_SETTINGS,
    ROW_FORMATS,
    source_option,
    emit_rows,
    load_catalog,
)


@click.group(
    "tables",
    context_settings=CONTEXT_SETTINGS,
    help="Inspect structured catalog tables.",
)
def tables_command() -> None:
    """Inspect structured catalog tables."""


@tables_command.command("list", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option(
    "--row-counts",
    is_flag=True,
    help="Materialize each table enough to include row counts.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def list_command(ctx: click.Context, row_counts: bool, output_format: str) -> None:
    """List queryable catalog tables."""

    emit_rows(
        list_tables(load_catalog(ctx), include_row_counts=row_counts),
        output_format=output_format,
    )


@tables_command.command("schema", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option(
    "--table",
    "table_names",
    multiple=True,
    help="Only include this table. Can be passed more than once.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def schema_command(
    ctx: click.Context,
    table_names: tuple[str, ...],
    output_format: str,
) -> None:
    """List columns for SQL-visible catalog tables."""

    try:
        rows = describe_tables(tables=table_names)
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    except click.ClickException:
        raise
    except Exception as exc:
        raise click.ClickException(
            format_error(
                str(exc),
                ["Run tables list first to inspect available table names."],
            )
        ) from exc
    emit_rows(rows, output_format=output_format)


@tables_command.command("values", context_settings=CONTEXT_SETTINGS)
@source_option
@click.argument("table")
@click.argument("column")
@click.option(
    "--explode",
    is_flag=True,
    help="Count each item in a list-valued column separately.",
)
@click.option("--contains", help="Case-insensitive substring filter over values.")
@click.option(
    "--limit",
    type=click.IntRange(min=1),
    default=50,
    show_default=True,
    help="Maximum values to print.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="table",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def values_command(
    ctx: click.Context,
    table: str,
    column: str,
    explode: bool,
    contains: str | None,
    limit: int,
    output_format: str,
) -> None:
    """Count distinct values in a catalog table column."""

    catalog = load_catalog(ctx)
    try:
        rows = count_values(
            catalog,
            table,
            column,
            explode=explode,
            contains=contains,
            limit=limit + 1,
        )
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    except click.ClickException:
        raise
    except Exception as exc:
        raise click.ClickException(
            format_error(
                str(exc),
                ["Run tables schema first to inspect available columns."],
            )
        ) from exc
    visible_rows = rows[:limit]
    emit_rows(visible_rows, output_format=output_format)
    if len(rows) > limit:
        click.echo(
            f"Returned {limit} values. Increase --limit to inspect more.",
            err=True,
        )


def list_tables(
    catalog: Catalog,
    *,
    include_row_counts: bool = False,
) -> list[dict[str, object]]:
    """List SQL-visible catalog tables."""

    if include_row_counts:
        return catalog_table_rows(catalog)
    return [
        {"name": spec.name, "columns": len(spec.schema), "rows": None}
        for spec in TABLE_SPECS.values()
    ]


def describe_tables(tables: Sequence[str] = ()) -> list[dict[str, object]]:
    """List columns for SQL-visible catalog tables."""

    try:
        return catalog_table_schema(tables)
    except KeyError as exc:
        raise unknown_table_error([str(exc).strip("'")]) from exc


def count_values(
    catalog: Catalog,
    table: str,
    column: str,
    *,
    explode: bool = False,
    contains: str | None = None,
    limit: int = 50,
) -> list[dict[str, object]]:
    """Count distinct values in a catalog table column."""

    frame = require_table(catalog, table)
    require_column(table, frame, column)
    dtype = frame.schema[column]
    if _is_list_dtype(dtype) and not explode:
        raise ToolError(
            f"Column {table}.{column} is list-valued.",
            hints=["Pass --explode to count each list item separately."],
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
            pl.lit(table).alias("table"),
            pl.lit(column).alias("column"),
        )
        .select("table", "column", "value", "rows")
        .to_dicts()
    )


def require_table(catalog: Catalog, table: str) -> pl.DataFrame:
    if table not in catalog_table_names():
        raise unknown_table_error([table])
    return catalog.table(table)


def require_column(table: str, frame: pl.DataFrame, column: str) -> None:
    if column not in frame.columns:
        columns = ", ".join(frame.columns)
        raise ToolError(
            f"Unknown column for table {table}: {column}",
            hints=[
                f"Available columns on {table}: {columns}",
                f"Use one of the available columns on {table}.",
            ],
        )


def unknown_table_error(tables: Sequence[str]) -> ToolError:
    available = ", ".join(catalog_table_names())
    return ToolError(
        f"Unknown table(s): {', '.join(tables)}",
        hints=[
            f"Available tables: {available}",
            "Use one of the available table names.",
        ],
    )


def _is_list_dtype(dtype: object) -> bool:
    return isinstance(dtype, pl.DataType) and dtype.base_type() == pl.List


__all__ = ["tables_command"]
