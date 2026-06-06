from __future__ import annotations

from pathlib import Path

import click

from chartcoach.constants import INDEX_DIR_ENV, SOURCE_ENV

from .common import CONTEXT_SETTINGS

PROMPT_TARGETS = {
    "codex": "Codex",
    "claude": "Claude Code",
    "opencode": "Opencode",
}
GUIDANCE_MODES = ("create", "feedback", "explore", "debug")
DEFAULT_SKILL = "chartcoach/catalog"
DEFAULT_PUBLIC_SITE_URL = "https://chartcoach.github.io"


@click.command("prompt", context_settings=CONTEXT_SETTINGS)
@click.option("--codex", is_flag=True, help="Print a startup prompt for Codex.")
@click.option("--claude", is_flag=True, help="Print a startup prompt for Claude Code.")
@click.option("--opencode", is_flag=True, help="Print a startup prompt for Opencode.")
@click.option(
    "--task",
    help="User task to include in the startup prompt.",
)
@click.option(
    "--source",
    "source_path",
    envvar=SOURCE_ENV,
    type=click.Path(path_type=Path),
    help=f"Catalog bundle, parquet file, or authored folder. Defaults to ${SOURCE_ENV} when set.",
)
@click.option(
    "--index-dir",
    envvar=INDEX_DIR_ENV,
    type=click.Path(file_okay=False, path_type=Path),
    help=f"Semantic index directory. Defaults to ${INDEX_DIR_ENV} when set.",
)
@click.option(
    "--guidance-mode",
    type=click.Choice(GUIDANCE_MODES),
    default="explore",
    show_default=True,
    help="Design-reasoning mode for the prompt.",
)
@click.option(
    "--skill",
    default=DEFAULT_SKILL,
    show_default=True,
    help="Installed ChartCoach skill name referenced by the prompt.",
)
@click.option(
    "--public-site-url",
    default=DEFAULT_PUBLIC_SITE_URL,
    show_default=True,
    help="Base URL used when asking the agent to cite guideline public links.",
)
def prompt_command(
    codex: bool,
    claude: bool,
    opencode: bool,
    task: str | None,
    source_path: Path | None,
    index_dir: Path | None,
    guidance_mode: str,
    skill: str,
    public_site_url: str,
) -> None:
    """Print an agent startup prompt for ChartCoach."""

    target = _resolve_target(codex=codex, claude=claude, opencode=opencode)
    click.echo(
        build_agent_prompt(
            target=target,
            task=task,
            source_path=source_path,
            index_dir=index_dir,
            guidance_mode=guidance_mode,
            skill=skill,
            public_site_url=public_site_url,
        )
    )


def build_agent_prompt(
    *,
    target: str,
    task: str | None = None,
    source_path: Path | None = None,
    index_dir: Path | None = None,
    guidance_mode: str = "explore",
    skill: str = DEFAULT_SKILL,
    public_site_url: str = DEFAULT_PUBLIC_SITE_URL,
) -> str:
    """Return a ChartCoach startup prompt for one agent runtime."""

    agent_name = PROMPT_TARGETS[target]
    normalized_site_url = public_site_url.rstrip("/")
    lines = [
        "Use ChartCoach for evidence-backed visualization design reasoning.",
        "",
        f"Target agent: {agent_name}.",
        f"Installed skill: `{skill}`.",
        f"Guidance mode: `{guidance_mode}`.",
    ]
    if source_path is not None:
        lines.append(f"Catalog source: `{source_path}`.")
    else:
        lines.append(
            f"Catalog source: use the user's provided path or `${SOURCE_ENV}` when available."
        )
    if index_dir is not None:
        lines.append(f"Semantic index directory: `{index_dir}`.")
    else:
        lines.append(
            f"Semantic index directory: use `${INDEX_DIR_ENV}` when available."
        )
    if task:
        lines.extend(["", "User task:", task.strip()])

    lines.extend(
        [
            "",
            "Work contract:",
            f"- Use the installed `{skill}` skill for workflow mechanics.",
            "- Read `MANIFEST.md` for this catalog instance's section-role and label-family semantics.",
            "- Start with manifest prose, table schema, label discovery, and guideline summaries.",
            "- Use role-specific section reads before full guideline bodies when the needed roles are clear.",
            "- Treat the semantic index as optional. If it is missing or fails catalog-digest validation, continue with progressive disclosure over catalog rows.",
            "- When retrieved guidelines constrain or justify the answer, include a Guideline Use Report with guideline ids and public links.",
            f"- Use public links shaped as `{normalized_site_url}/guidelines/<guideline-id>/`.",
        ]
    )
    return "\n".join(lines)


def _resolve_target(*, codex: bool, claude: bool, opencode: bool) -> str:
    selected = [
        name
        for name, enabled in {
            "codex": codex,
            "claude": claude,
            "opencode": opencode,
        }.items()
        if enabled
    ]
    if len(selected) != 1:
        raise click.ClickException(
            "Pass exactly one agent flag: --codex, --claude, or --opencode."
        )
    return selected[0]


__all__ = ["build_agent_prompt", "prompt_command"]
