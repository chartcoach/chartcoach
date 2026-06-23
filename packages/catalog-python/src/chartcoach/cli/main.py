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
    help=(
        "chartcoach catalog CLI.\n\n"
        "\b\n"
        "Start here (for AI agents):\n"
        "  chartcoach skills get core\n\n"
        "\b\n"
        "Progressive Catalog Navigation:\n"
        "  catalog overview             Summarize source, counts, roles, labels\n"
        "  catalog labels               List label values and counts\n"
        "  catalog query                Filter entries without an index\n"
        "  catalog read                 Read exact entries and sections\n\n"
        "\b\n"
        "Indexed Discovery:\n"
        "  catalog find                 Rank entries with chartcoach[index]\n"
        "  catalog index create         Build a LanceDB index\n"
        "  catalog index info           Inspect a LanceDB index\n\n"
        "\b\n"
        "Catalog Lifecycle:\n"
        "  catalog build                Build a catalog bundle\n"
        "  catalog validate             Validate a catalog source\n"
        "  catalog export duckdb         Materialize DuckDB tables\n"
        "  catalog cache                Inspect and prefetch artifact cache entries\n\n"
        "\b\n"
        "MCP Server:\n"
        "  mcp tools                    Print MCP tool contracts\n"
        "  mcp serve                    Start the MCP server\n\n"
        "\b\n"
        "Agent Skills:\n"
        "  skills [list]                List CLI-served skills\n"
        "  skills get <name>            Print a CLI-served skill\n"
        "  skills path [name]           Print skill directory path"
    ),
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
