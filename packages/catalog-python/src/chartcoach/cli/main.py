from __future__ import annotations

import click

from .catalog import catalog_command
from .guidelines import guidelines_command
from .index import index_command
from .mcp import mcp_command
from .prompt import prompt_command
from .skills import skills_command
from .sql import sql_command
from .tables import tables_command

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(
    context_settings=CONTEXT_SETTINGS,
    help=(
        "ChartCoach catalog CLI for AI agents.\n\n"
        "\b\n"
        "Start here (for AI agents):\n"
        "  chartcoach skills get core\n\n"
        "  CLI-served skills ship with the CLI and include workflow patterns, "
        "catalog setup, search guidance, and citation examples. Prefer them over guessing "
        "workflows from option docs alone.\n\n"
        "\b\n"
        "  skills [list]                List available CLI-served skills\n"
        "  skills get core              Catalog primitives and artifacts\n"
        "  skills get visfeedback       Visualization feedback workflow\n"
        "  skills path [name]           Print skill directory path"
    ),
)
def main() -> None:
    """ChartCoach command-line interface."""


main.add_command(catalog_command)
main.add_command(guidelines_command)
main.add_command(index_command)
main.add_command(mcp_command)
main.add_command(prompt_command)
main.add_command(skills_command)
main.add_command(sql_command)
main.add_command(tables_command)

__all__ = ["main"]
