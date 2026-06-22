from __future__ import annotations

import click

from chartcoach.tools import format_error, mcp_tool_specs

from chartcoach.constants import (
    INDEX_ENV,
    LANCE_DOCUMENT_TABLE,
    SOURCE_ENV,
)

from .common import ROW_FORMATS, emit_rows

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}
TRANSPORT_CHOICES = ("stdio", "sse", "streamable-http")
LOG_LEVEL_CHOICES = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
MCP_INDEX_EXTRA_HINTS = (
    "For one-off runs, use `uvx --from 'chartcoach[mcp,index]@latest' chartcoach ...`.",
    "From a checkout, use `uv run --package chartcoach --extra mcp --extra index chartcoach ...`.",
)


def _is_missing_optional_dependency(exc: ModuleNotFoundError) -> bool:
    return _has_missing_module(exc, ("mcp",))


def _is_missing_search_dependency(exc: ModuleNotFoundError) -> bool:
    return _has_missing_module(exc, ("lancedb",))


def _has_missing_module(exc: ModuleNotFoundError, module_names: tuple[str, ...]) -> bool:
    current: BaseException | None = exc
    while current is not None:
        if isinstance(current, ModuleNotFoundError):
            name = current.name
            if name is not None and any(
                name == module or name.startswith(f"{module}.")
                for module in module_names
            ):
                return True
        current = current.__cause__
    return False


@click.group(
    "mcp",
    context_settings=CONTEXT_SETTINGS,
    help="Start and configure chartcoach MCP servers.",
)
def mcp_command() -> None:
    """Start and configure chartcoach MCP servers."""


@mcp_command.command(
    "tools",
    context_settings=CONTEXT_SETTINGS,
    short_help="Print MCP tool contracts.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(ROW_FORMATS),
    default="json",
    show_default=True,
    help="Output format.",
)
def tools_command(output_format: str) -> None:
    """Print MCP tool names, arguments, registration conditions, and return shapes."""

    emit_rows(mcp_tool_specs(), output_format=output_format)


@mcp_command.command(
    "serve",
    context_settings=CONTEXT_SETTINGS,
    short_help="Start the chartcoach MCP server.",
)
@click.option(
    "--source",
    "source_path",
    envvar=SOURCE_ENV,
    metavar="PATH_OR_URL",
    help=(
        "Catalog bundle, entries parquet file, authored folder, or metadata URL. "
        f"Defaults to ${SOURCE_ENV}, then the package-pinned Default Catalog release."
    ),
)
@click.option(
    "--index",
    "index_path",
    envvar=INDEX_ENV,
    metavar="PATH_OR_URI",
    help=(
        "LanceDB database path or URI for search tools. "
        f"Defaults to ${INDEX_ENV} when set."
    ),
)
@click.option(
    "--table",
    "table_name",
    default=LANCE_DOCUMENT_TABLE,
    show_default=True,
    help="LanceDB table name for search tools.",
)
@click.option(
    "--transport",
    type=click.Choice(TRANSPORT_CHOICES, case_sensitive=False),
    help="MCP transport. Defaults to CHARTCOACH_MCP_TRANSPORT or stdio.",
)
@click.option(
    "--host",
    help="Host for sse and streamable-http transports. Defaults to CHARTCOACH_MCP_HOST or 127.0.0.1.",
)
@click.option(
    "--port",
    type=click.IntRange(1, 65535),
    help="Port for sse and streamable-http transports. Defaults to CHARTCOACH_MCP_PORT or 8000.",
)
@click.option(
    "--log-level",
    type=click.Choice(LOG_LEVEL_CHOICES, case_sensitive=False),
    help="Logging level. Defaults to CHARTCOACH_MCP_LOG_LEVEL or INFO.",
)
def serve_command(
    source_path: str | None,
    index_path: str | None,
    table_name: str,
    transport: str | None,
    host: str | None,
    port: int | None,
    log_level: str | None,
) -> None:
    """Start the chartcoach MCP server."""

    try:
        _run_server(
            index_path=index_path,
            table_name=table_name,
            source_path=source_path,
            transport=transport,
            host=host,
            port=port,
            log_level=log_level,
        )
    except ModuleNotFoundError as exc:  # pragma: no cover - depends on install extras
        if _is_missing_optional_dependency(exc):
            raise click.ClickException(
                "The `chartcoach mcp serve` command requires the optional MCP dependencies. Install `chartcoach[mcp]` to use it."
            ) from exc
        if _is_missing_search_dependency(exc):
            raise click.ClickException(
                format_error(
                    "Indexed MCP search requires the optional LanceDB dependencies.",
                    MCP_INDEX_EXTRA_HINTS,
                )
            ) from exc
        raise
    except ValueError as exc:
        raise click.ClickException(str(exc)) from exc


def _run_server(
    *,
    index_path: str | None,
    table_name: str,
    source_path: str | None,
    transport: str | None,
    host: str | None,
    port: int | None,
    log_level: str | None,
) -> None:
    from chartcoach import mcp

    config = mcp.configure(
        index=index_path,
        table=table_name,
        source=source_path,
        transport=transport.lower() if transport is not None else None,
        host=host,
        port=port,
        log_level=log_level.upper() if log_level is not None else None,
    )
    mcp.main(
        settings=config.settings,
        runtime=config.runtime,
    )


__all__ = ["mcp_command", "serve_command", "tools_command"]
