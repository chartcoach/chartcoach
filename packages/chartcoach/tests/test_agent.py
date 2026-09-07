from __future__ import annotations

import pydoc
from importlib.metadata import distribution
from pathlib import Path

import agent_plugins
import chartcoach.agent as chartcoach_agent
from chartcoach import Catalog, CatalogError, open_catalog
from chartcoach import _skills as skill_service

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
    assert {path.relative_to(plugin.path).as_posix() for path in plugin.files} == (
        _PLUGIN_FILES
    )


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
        "chartcoach": agent_plugins.StdioServer(command="chartcoach", args=("mcp",))
    }
    launch = mcp.resolve_stdio("chartcoach", data_dir=tmp_path)
    assert launch.command == "chartcoach"
    assert launch.args == ("mcp",)
    assert launch.cwd == plugin.path
    assert launch.env["PLUGIN_ROOT"] == str(plugin.path)
    assert launch.env["PLUGIN_DATA"] == str(tmp_path)


def test_agent_module_has_one_catalog_api() -> None:
    assert chartcoach_agent.__all__ == [
        "Catalog",
        "CatalogError",
        "agent_plugin",
        "open_catalog",
    ]
    assert chartcoach_agent.Catalog is Catalog
    assert chartcoach_agent.CatalogError is CatalogError
    assert chartcoach_agent.open_catalog is open_catalog
    assert chartcoach_agent.agent_plugin is skill_service.agent_plugin


def test_agent_workflow_runs_against_the_release_fixture() -> None:
    catalog = chartcoach_agent.open_catalog(_FIXTURE_RELEASE)
    candidates = catalog.query(contains="Direct Labels", limit=5).to_dicts()
    guideline_id = str(candidates[0]["id"])

    records = catalog.read(ids=[guideline_id], source_detail="minimal")
    citations = catalog.cite(ids=[guideline_id])
    description = catalog.describe()

    assert guideline_id == "direct-labels"
    assert records[0]["id"] == guideline_id
    assert citations[0]["id"] == guideline_id
    assert catalog.release is not None
    assert description["release_digest"] == catalog.release.digest


def test_agent_module_help_teaches_catalog_and_resource_discovery() -> None:
    rendered = pydoc.render_doc(chartcoach_agent)

    assert "catalog = cc.open_catalog()" in rendered
    assert "candidates = catalog.query(" in rendered
    assert "records = catalog.read(" in rendered
    assert "citations = catalog.cite(" in rendered
    assert 'core = plugin.skill("core")' in rendered
