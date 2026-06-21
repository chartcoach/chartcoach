from __future__ import annotations

import click

from ._catalog.cache import register_cache_commands
from ._catalog.index import register_index_commands
from ._catalog.lifecycle import register_lifecycle_commands
from ._catalog.navigation import register_navigation_commands
from .common import CONTEXT_SETTINGS


@click.group(
    "catalog",
    context_settings=CONTEXT_SETTINGS,
    invoke_without_command=True,
    no_args_is_help=False,
    help=(
        "Inspect, query, build, and index chartcoach catalogs.\n\n"
        "\b\n"
        "Progressive Catalog Navigation:\n"
        "  overview          Summarize source, counts, roles, and label families\n"
        "  labels            List label values and counts\n"
        "  roles             List section roles and counts\n"
        "  list              List entries by id, title, description, and labels\n"
        "  query             Filter entries with composable base predicates\n"
        "  read              Read exact entries and selected sections\n"
        "  cite              Print guideline URLs and formatted source citations\n"
        "  schema            Show queryable fields and tables\n"
        "  values            Count values for a field\n"
        "  sql               Run one read-only SELECT query\n\n"
        "\b\n"
        "Indexed Discovery, requires chartcoach[index]:\n"
        "  find              Rank entries with a LanceDB index\n"
        "  index create      Build a caller-owned LanceDB index\n"
        "  index info        Inspect a LanceDB index\n\n"
        "\b\n"
        "Catalog Lifecycle:\n"
        "  build             Build a catalog bundle from authored entries\n"
        "  validate          Validate a catalog source\n"
        "  manifest          Print the catalog manifest\n"
        "  export duckdb     Materialize catalog tables into DuckDB"
        "\n"
        "  cache             Inspect, clear, and prefetch artifact cache entries"
    ),
)
@click.pass_context
def catalog_command(ctx: click.Context) -> None:
    """Catalog command group."""

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit(0)


register_navigation_commands(catalog_command)
register_index_commands(catalog_command)
register_lifecycle_commands(catalog_command)
register_cache_commands(catalog_command)

__all__ = ["catalog_command"]
