from __future__ import annotations

import json
from typing import Literal, cast

import click

from chartcoach.tools import ToolError, Tools

from ..common import (
    CONTEXT_SETTINGS,
    SEARCH_FORMATS,
    catalog_release_digest,
    emit_rows,
    guideline_search_rows_to_compact_markdown,
    guideline_search_rows_to_markdown,
    index_profile_option,
    load_catalog,
    require_index,
    required_index_option,
    search_cli_error,
    source_option,
)


@click.command("find", context_settings=CONTEXT_SETTINGS)
@source_option
@required_index_option
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
    index_path: str | None,
    profile: str | None,
    query: str,
    limit: int,
    where: str | None,
    vector: tuple[float, ...],
    mode: str,
    output_format: str,
) -> None:
    """Rank entries with a LanceDB profile."""

    catalog = load_catalog(ctx)
    resolved_index = index_path or (
        catalog_release_digest(ctx) if profile is not None else None
    )
    try:
        table = require_index(resolved_index, profile=profile)
        result = Tools(
            catalog,
            table=table,
            index_path=resolved_index,
            release_digest=catalog_release_digest(ctx),
        ).search(
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
