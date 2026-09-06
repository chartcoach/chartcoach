from __future__ import annotations

import json
from typing import Literal, cast

import click

from chartcoach.catalog.errors import CatalogError
from chartcoach.tools import ToolError, Tools

from ..common import (
    CONTEXT_SETTINGS,
    SEARCH_FORMATS,
    emit_rows,
    guideline_search_rows_to_compact_markdown,
    guideline_search_rows_to_markdown,
    index_profile_option,
    search_cli_error,
    source_option,
    source_path,
)


@click.command("find", context_settings=CONTEXT_SETTINGS)
@source_option
@index_profile_option
@click.argument("query")
@click.option(
    "--limit",
    type=click.IntRange(min=1),
    default=8,
    show_default=True,
    help="Maximum indexed documents to inspect before guideline deduplication.",
)
@click.option("--where", help="LanceDB SQL filter over indexed document columns.")
@click.option(
    "--vector",
    type=float,
    multiple=True,
    help="Caller-provided vector component. Pass once per dimension.",
)
@click.option(
    "--mode",
    type=click.Choice(("fts", "vector", "hybrid")),
    default="fts",
    show_default=True,
    help="LanceDB query mode for document retrieval.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(SEARCH_FORMATS),
    default="compact",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def find_command(
    ctx: click.Context,
    profile: str,
    query: str,
    limit: int,
    where: str | None,
    vector: tuple[float, ...],
    mode: str,
    output_format: str,
) -> None:
    """Rank entries with a LanceDB profile."""

    try:
        source = source_path(ctx)
        result = Tools.open(source, profile=profile).search(
            query,
            limit=limit,
            where=where,
            vector=vector or None,
            mode=cast(Literal["fts", "vector", "hybrid"], mode),
        )
    except ToolError as exc:
        raise click.ClickException(str(exc)) from exc
    except click.ClickException:
        raise
    except ModuleNotFoundError as exc:
        raise click.ClickException(
            search_cli_error(
                str(exc),
                missing_index_extra=True,
            )
        ) from exc
    except CatalogError as exc:
        raise click.ClickException(
            search_cli_error(exc.message, hints=exc.hints)
        ) from exc
    except Exception as exc:
        raise click.ClickException(search_cli_error(str(exc))) from exc

    if output_format == "json":
        click.echo(json.dumps(result, indent=2, ensure_ascii=False, default=str))
        return

    rows = cast(list[dict[str, object]], result["rows"])
    if output_format == "markdown":
        click.echo(
            guideline_search_rows_to_markdown(rows).rstrip() or "No entries matched."
        )
    elif output_format == "compact":
        click.echo(
            guideline_search_rows_to_compact_markdown(rows).rstrip()
            or "No entries matched."
        )
    else:
        emit_rows(
            rows,
            output_format=output_format,
            empty_message="No entries matched.",
        )


def register_index_commands(group: click.Group) -> None:
    group.add_command(find_command)


__all__ = ["register_index_commands"]
