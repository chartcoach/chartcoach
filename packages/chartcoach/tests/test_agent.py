from __future__ import annotations

import pydoc
from collections.abc import Sequence
from importlib.metadata import distribution
from pathlib import Path
from typing import cast

import agent_plugins
import chartcoach.agent as chartcoach_agent
import pytest
from chartcoach import skills as skill_service
from chartcoach.catalog.collection import Catalog
from chartcoach.catalog.entries import Guideline, Section
from chartcoach.catalog.errors import CatalogLookupError, CatalogValidationError
from chartcoach.catalog.introspection import describe_tables, list_tables
from chartcoach.catalog.query import query_entries
from chartcoach.catalog.read import SourceDetail, retrieve_entry_records
from chartcoach.catalog.references import citation_records
from chartcoach.catalog.summary import catalog_overview, list_labels, list_roles
from chartcoach.tools import Tools

_PROJECT = Path(__file__).parents[1]
_FIXTURE_RELEASE = _PROJECT.parents[1] / "fixtures" / "catalog-release"
_SKILL_NAMES = ("core", "discuss", "visfeedback", "visrec", "contribute")
_PLUGIN_FILES = {
    "mcp.json",
    "plugin.json",
    *{f"skills/{name}/SKILL.md" for name in _SKILL_NAMES},
}


def _capability_entry_points():
    return [
        entry_point
        for entry_point in distribution("chartcoach").entry_points
        if entry_point.group == "marimo.agent.capability"
    ]


def test_project_plugin_carries_the_selected_chartcoach_files() -> None:
    plugin = agent_plugins.Plugin.from_project(_PROJECT)

    assert plugin.path == _PROJECT.parents[1]
    assert {
        path.relative_to(plugin.path).as_posix() for path in plugin.files
    } == _PLUGIN_FILES


def test_marimo_code_mode_discovers_the_chartcoach_agent_module() -> None:
    capabilities = _capability_entry_points()

    assert [(entry.name, entry.value) for entry in capabilities] == [
        ("chartcoach", "chartcoach.agent")
    ]
    assert capabilities[0].load() is chartcoach_agent


def test_agent_module_exposes_resolvable_portable_mcp_server(
    tmp_path: Path,
) -> None:
    plugin = chartcoach_agent.agent_plugin()
    mcp = plugin.mcp

    assert mcp is not None
    assert mcp.issues == ()
    assert mcp.servers == {
        "chartcoach": agent_plugins.StdioServer(
            command="chartcoach",
            args=("mcp",),
        )
    }
    launch = mcp.resolve_stdio("chartcoach", data_dir=tmp_path)
    assert launch.command == "chartcoach"
    assert launch.args == ("mcp",)
    assert launch.cwd == plugin.path
    assert launch.env["PLUGIN_ROOT"] == str(plugin.path)
    assert launch.env["PLUGIN_DATA"] == str(tmp_path)


def test_agent_module_uses_shared_skill_and_catalog_operations() -> None:
    assert chartcoach_agent.agent_plugin is skill_service.agent_plugin
    assert chartcoach_agent.agent_skill is skill_service.agent_skill
    assert chartcoach_agent.agent_skills is skill_service.agent_skills
    assert chartcoach_agent.query_entries is query_entries
    assert chartcoach_agent.retrieve_entry_records is retrieve_entry_records
    assert chartcoach_agent.citation_records is citation_records
    assert chartcoach_agent.catalog_overview is catalog_overview
    assert chartcoach_agent.list_labels is list_labels
    assert chartcoach_agent.list_roles is list_roles
    assert chartcoach_agent.list_tables is list_tables
    assert chartcoach_agent.describe_tables is describe_tables
    assert chartcoach_agent.Tools is Tools


def test_agent_help_workflow_runs_against_the_release_fixture() -> None:
    tools = chartcoach_agent.Tools.open(_FIXTURE_RELEASE)
    catalog = tools.catalog
    candidates = chartcoach_agent.query_entries(
        catalog,
        contains="Direct Labels",
        limit=5,
        include_body=False,
    ).to_dicts()
    guideline_id = str(candidates[0]["id"])

    records = chartcoach_agent.retrieve_entry_records(
        catalog,
        ids=[guideline_id],
        source_detail="full",
    )
    overview = chartcoach_agent.catalog_overview(
        catalog,
        source=str(_FIXTURE_RELEASE),
    )

    assert guideline_id == "direct-labels"
    assert records[0]["id"] == guideline_id
    assert catalog.release is not None
    assert overview["release_digest"] == catalog.release.digest


def test_agent_read_contract_rejects_ambiguous_strings(
    sample_catalog: Catalog,
) -> None:
    with pytest.raises(CatalogValidationError, match="ids must be a sequence") as ids:
        chartcoach_agent.retrieve_entry_records(
            sample_catalog,
            ids="direct-labels",
        )
    with pytest.raises(CatalogValidationError, match="labels must be a sequence"):
        chartcoach_agent.query_entries(
            sample_catalog,
            labels="chart:line",
        )
    with pytest.raises(CatalogValidationError, match="ids must contain strings"):
        chartcoach_agent.retrieve_entry_records(
            sample_catalog,
            ids=cast(Sequence[str], [1]),
        )
    with pytest.raises(CatalogValidationError, match="tables must be a sequence"):
        chartcoach_agent.describe_tables("guidelines")
    with pytest.raises(CatalogValidationError, match="Unknown source detail") as detail:
        chartcoach_agent.retrieve_entry_records(
            sample_catalog,
            ids=["direct-labels"],
            source_detail=cast(SourceDetail, "everything"),
        )

    assert "Pass ids=['direct-labels']." in str(ids.value)
    assert "Choose one of: none, minimal, full." in str(detail.value)


def test_agent_read_contract_accepts_empty_ids(sample_catalog: Catalog) -> None:
    assert chartcoach_agent.retrieve_entry_records(sample_catalog, ids=[]) == []


def test_agent_label_recovery_scopes_only_known_families(
    sample_catalog: Catalog,
) -> None:
    with pytest.raises(CatalogLookupError) as unknown_family:
        chartcoach_agent.query_entries(sample_catalog, labels=["missing:value"])
    with pytest.raises(CatalogLookupError) as known_family:
        chartcoach_agent.query_entries(sample_catalog, labels=["chart:missing"])

    assert "family='missing'" not in str(unknown_family.value)
    assert "--family missing" not in str(unknown_family.value)
    assert "family='chart'" in str(known_family.value)
    assert "--family chart" in str(known_family.value)


def test_agent_text_search_preserves_unicode_case_matching(
    sample_catalog: Catalog,
) -> None:
    catalog = Catalog.from_guidelines(
        [
            Guideline(
                id="street",
                title="Straße",
                description="Street label guidance.",
                sections=(
                    Section(
                        role="advice",
                        title="Advice",
                        content="Keep the street label visible.",
                    ),
                ),
            )
        ],
        manifest=sample_catalog.manifest,
    )

    matches = chartcoach_agent.query_entries(
        catalog,
        contains="STRAẞE",
        include_body=False,
    )

    assert matches.get_column("id").to_list() == ["street"]


@pytest.mark.parametrize("contains", ["___", "---", "   "])
def test_agent_text_search_rejects_separator_only_queries(
    sample_catalog: Catalog,
    contains: str,
) -> None:
    with pytest.raises(CatalogValidationError, match="must not consist only"):
        chartcoach_agent.query_entries(sample_catalog, contains=contains)


def test_agent_module_help_teaches_code_and_resource_traversal() -> None:
    plugin = chartcoach_agent.agent_plugin()
    rendered = pydoc.render_doc(chartcoach_agent)

    assert str(plugin.path) in rendered
    assert "tools = cc.Tools.open(source)" in rendered
    assert "candidates = cc.query_entries(" in rendered
    assert "resources = cc.agent_plugin()" in rendered
    assert "mcp = resources.mcp" in rendered
    assert "print(core.source)" in rendered
    assert "print(cc.skill_markdown(core, full=True))" in rendered
    assert 'indexed = cc.Tools.open(source, profile="<profile>")' in rendered
    assert "https://docs.chartcoach.dev/llms.txt" in rendered
