from __future__ import annotations

import click

from chartcoach import __version__

from .catalog import catalog_command
from .mcp import mcp_command
from .skills import skills_command

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(
    context_settings=CONTEXT_SETTINGS,
    invoke_without_command=True,
    no_args_is_help=False,
    help="Inspect and query the ChartCoach guideline catalog.",
)
@click.version_option(__version__, prog_name="chartcoach")
@click.pass_context
def main(ctx: click.Context) -> None:
    """chartcoach command-line interface."""

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit(0)


main.add_command(catalog_command)
main.add_command(mcp_command)
main.add_command(skills_command)

__all__ = ["main"]
