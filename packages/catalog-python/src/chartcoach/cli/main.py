from __future__ import annotations

import click

from .catalog import catalog_command
from .mcp import mcp_command

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(
    context_settings=CONTEXT_SETTINGS,
    help=(
        "ChartCoach command-line interface.\n\n"
        "Use `chartcoach catalog --help` to inspect and retrieve guidelines. "
        "Use `chartcoach mcp --help` to start the MCP server."
    ),
)
def main() -> None:
    """ChartCoach command-line interface."""


main.add_command(catalog_command)
main.add_command(mcp_command)

__all__ = ["main"]
