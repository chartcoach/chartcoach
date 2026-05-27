from __future__ import annotations

import click

from .artifacts import artifacts_command
from .catalog import catalog_command
from .guidelines import guidelines_command
from .index import index_command
from .mcp import mcp_command
from .sql import sql_command
from .tables import tables_command

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(
    context_settings=CONTEXT_SETTINGS,
    help=(
        "ChartCoach command-line interface.\n\n"
        "Use `chartcoach guidelines --help` to read and search guidelines. "
        "Use `chartcoach sql --help` to query catalog tables with DuckDB. "
        "Use `chartcoach tables --help` to inspect catalog tables. "
        "Use `chartcoach artifacts --help` to locate native files. "
        "Use `chartcoach mcp serve --help` to start the MCP server."
    ),
)
def main() -> None:
    """ChartCoach command-line interface."""


main.add_command(catalog_command)
main.add_command(artifacts_command)
main.add_command(guidelines_command)
main.add_command(index_command)
main.add_command(mcp_command)
main.add_command(sql_command)
main.add_command(tables_command)

__all__ = ["main"]
