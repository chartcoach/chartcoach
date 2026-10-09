from __future__ import annotations

from pathlib import Path

import click


def load_env_file(
    ctx: click.Context, parameter: click.Parameter, value: Path | None
) -> None:
    """Load only the selected file or .env in the working directory, before options."""
    if ctx.resilient_parsing:
        return
    path = value if value is not None else Path.cwd() / ".env"
    if value is None and not path.exists():
        return
    if not path.is_file():
        raise click.BadParameter(
            "Environment file must be a readable file.", param=parameter
        )
    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError as exc:
        raise click.ClickException(
            "Install chartcoach[mcp] to load environment files."
        ) from exc
    try:
        load_dotenv(path, override=False, encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise click.BadParameter(
            "Environment file must be readable UTF-8.", param=parameter
        ) from exc
