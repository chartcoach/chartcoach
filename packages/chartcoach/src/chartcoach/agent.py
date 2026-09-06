"""Use ChartCoach from notebook agents."""

from __future__ import annotations

import sys
from textwrap import indent
from types import ModuleType

import agent_plugins

from .catalog import open_catalog, open_index
from .catalog.introspection import describe_tables, list_tables
from .catalog.query import query_entries
from .catalog.read import retrieve_entry_records
from .catalog.references import citation_records
from .catalog.summary import catalog_overview, list_labels, list_roles
from .skills import (
    agent_plugin,
    agent_skill,
    agent_skills,
    skill_description,
    skill_markdown,
)
from .tools import Tools


def _catalog_help(summary: str) -> str:
    return (
        f"{summary}\n\n"
        + """\

Open a catalog, find candidate guidelines, then read and cite the selected
records with the same operations used by the command-line interface:

    import chartcoach.agent as cc
    from pprint import pprint

    source = None  # Pass a local bundle or release path for offline work.
    tools = cc.Tools.open(source)
    catalog = tools.catalog
    candidates = cc.query_entries(
        catalog,
        contains="direct labels",
        limit=5,
        include_body=False,
    ).select("id", "title", "description", "labels").to_dicts()
    if not candidates:
        raise LookupError("No guidelines matched. Inspect cc.list_labels(catalog).")

    guideline_id = candidates[0]["id"]
    records = cc.retrieve_entry_records(
        catalog,
        ids=[guideline_id],
        source_detail="full",
    )
    citations = cc.citation_records(
        catalog,
        ids=[guideline_id],
    )
    overview = cc.catalog_overview(
        catalog,
        source=str(source or "official selected catalog"),
    )
    labels = cc.list_labels(catalog)
    roles = cc.list_roles(catalog)
    tables = cc.list_tables(catalog, include_row_counts=True)
    schema = cc.describe_tables()
    sql_result = tools.sql(
        "SELECT id, title FROM guidelines LIMIT 5"
    )
    result = {
        "candidates": candidates,
        "records": records,
        "citations": citations,
        "overview": overview,
        "labels": labels,
        "roles": roles,
        "tables": tables,
        "schema": schema,
        "sql": sql_result,
    }
    pprint(result)

For indexed search, open the catalog and its release-backed table together:

    indexed = cc.Tools.open(source, profile="<profile>")
    hits = indexed.search("direct labels", mode="fts")

The `rank` field gives result order. The numeric `score` is relevance for
full-text and hybrid search, and distance for vector search.
"""
    )


def _module_help(summary: str) -> str:
    catalog_help = _catalog_help(summary)
    try:
        plugin = agent_plugin()
        described = tuple(
            (skill, skill_description(skill)) for skill in agent_skills(plugin)
        )
        tree = indent(plugin.tree(max_depth=3, max_files=50), "    ")
        paths = "\n".join(
            f"    {skill.path.name:<12} {description}\n"
            f"                 {skill.file('SKILL.md')}"
            for skill, description in described
        )
    except agent_plugins.AgentPluginError as error:
        return f"""{catalog_help}

The installed Agent Plugin could not be resolved: {error}
"""

    return f"""{catalog_help}

The installed Agent Plugin carries instructions that match this chartcoach
version:

{tree}

Read `core` first, then select the workflow for the current task:

{paths}

Read the core instructions:

    core = cc.agent_skill()
    print(core.source)

Inspect every packaged resource when the task needs more context:

    resources = cc.agent_plugin()
    skills = cc.agent_skills(resources)
    descriptions = [
        (skill.path.name, cc.skill_description(skill))
        for skill in skills
    ]
    print(cc.skill_markdown(core, full=True))

Inspect the portable MCP server configuration:

    mcp = resources.mcp
    if mcp is not None:
        print(mcp.servers)
        print(mcp.issues)

Browse the published documentation map at:

    https://docs.chartcoach.dev/llms.txt
"""


__all__ = [
    "Tools",
    "agent_plugin",
    "agent_skill",
    "agent_skills",
    "catalog_overview",
    "citation_records",
    "describe_tables",
    "list_labels",
    "list_roles",
    "list_tables",
    "open_catalog",
    "open_index",
    "query_entries",
    "retrieve_entry_records",
    "skill_description",
    "skill_markdown",
]


class _AgentModule(ModuleType):
    @property
    def __doc__(self) -> str | None:  # pyrefly: ignore [bad-override]
        summary = self.__dict__.get("__doc__")
        return _module_help(summary) if isinstance(summary, str) else None

    @__doc__.setter
    def __doc__(self, value: str | None) -> None:
        self.__dict__["__doc__"] = value


sys.modules[__name__].__class__ = _AgentModule
