from __future__ import annotations

import click

from ._catalog.index import register_index_commands
from ._catalog.lifecycle import register_lifecycle_commands
from ._catalog.navigation import register_navigation_commands
from ._catalog.release_curation import register_release_commands
from .common import CONTEXT_SETTINGS


@click.group(
    "catalog",
    context_settings=CONTEXT_SETTINGS,
    invoke_without_command=True,
    no_args_is_help=False,
    help="Inspect, search, build, and publish catalogs.",
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
register_release_commands(catalog_command)

__all__ = ["catalog_command"]
