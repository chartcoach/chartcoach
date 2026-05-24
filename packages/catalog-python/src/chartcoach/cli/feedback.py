from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import cast

import click

from chartcoach.tools.catalog import CatalogToolError

from .common import (
    CONTEXT_SETTINGS,
    evidence_packets_to_markdown,
    catalog_tools,
    emit_object,
    source_option,
)

FEEDBACK_FORMATS = ("markdown", "json", "jsonl")


@click.group(
    "feedback",
    context_settings=CONTEXT_SETTINGS,
    help="Prepare catalog-grounded feedback prompts for existing chart images.",
)
def feedback_command() -> None:
    """Prepare catalog-grounded feedback prompts for existing chart images."""


@feedback_command.command("prompt", context_settings=CONTEXT_SETTINGS)
@source_option
@click.option(
    "--image",
    "image_path",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    required=True,
    help="Local chart image to review.",
)
@click.option(
    "--situation",
    required=True,
    help="Chart goal, audience, outlet, reading conditions, or task.",
)
@click.option(
    "--label",
    multiple=True,
    help="Require this exact guideline label. Can be passed more than once.",
)
@click.option(
    "--label-prefix",
    multiple=True,
    help="Require at least one label with this prefix. Can be passed more than once.",
)
@click.option(
    "--contains",
    help="Case-insensitive substring filter over id, title, description, and body.",
)
@click.option(
    "--section",
    "sections",
    multiple=True,
    help="Include only these section roles. Can be passed more than once.",
)
@click.option(
    "--limit",
    type=click.IntRange(min=1),
    default=8,
    show_default=True,
    help="Maximum guideline evidence packets.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(FEEDBACK_FORMATS),
    default="markdown",
    show_default=True,
    help="Output format.",
)
@click.pass_context
def prompt_command(
    ctx: click.Context,
    image_path: Path,
    situation: str,
    label: tuple[str, ...],
    label_prefix: tuple[str, ...],
    contains: str | None,
    sections: tuple[str, ...],
    limit: int,
    output_format: str,
) -> None:
    """Return a prompt and deterministic guideline evidence for one local chart."""

    try:
        evidence = catalog_tools(ctx).retrieve_guidelines(
            labels=label,
            label_prefixes=label_prefix,
            contains=contains,
            roles=sections,
            limit=limit,
        )
    except CatalogToolError as exc:
        raise click.ClickException(str(exc)) from exc

    packet: dict[str, object] = {
        "image": str(image_path),
        "situation": situation,
        "evidence": evidence,
        "evidence_count": len(evidence),
    }
    if output_format == "markdown":
        click.echo(_feedback_prompt_to_markdown(packet).rstrip())
    elif output_format == "jsonl":
        click.echo(json.dumps(packet, ensure_ascii=False))
    else:
        emit_object(packet, output_format=output_format)


def _feedback_prompt_to_markdown(packet: dict[str, object]) -> str:
    lines = [
        "# Chart Feedback Prompt",
        "",
        f"Image: `{packet['image']}`",
        "",
        "Situation:",
        "",
        str(packet["situation"]),
        "",
        "Use the image and situation to produce grounded visualization feedback. "
        "Cite only guideline ids from the evidence below, and do not apply a "
        "guideline unless it visibly affects this chart.",
        "",
        "# Guideline Evidence",
        "",
    ]
    lines.append(
        evidence_packets_to_markdown(
            cast(Sequence[Mapping[str, object]], packet["evidence"])
        ).rstrip()
    )
    return "\n".join(lines)


__all__ = ["feedback_command", "prompt_command"]
