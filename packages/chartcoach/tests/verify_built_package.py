from __future__ import annotations

import configparser
import json
import os
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from importlib.metadata import version
from pathlib import Path

_REPOSITORY = Path(__file__).parents[3]
_VERSION = version("chartcoach")
_DISTRIBUTION = f"chartcoach-{_VERSION}"
_WHEEL = _REPOSITORY / "dist" / f"{_DISTRIBUTION}-py3-none-any.whl"
_SDIST = _REPOSITORY / "dist" / f"{_DISTRIBUTION}.tar.gz"
_FIXTURE_RELEASE = _REPOSITORY / "fixtures" / "catalog-release"
_SKILL_NAMES = ("core", "discuss", "visfeedback", "visrec", "contribute")
_PLUGIN_FILES = tuple(
    sorted(
        (
            "mcp.json",
            "plugin.json",
            *(f"skills/{name}/SKILL.md" for name in _SKILL_NAMES),
        )
    )
)


def main() -> None:
    _verify_wheel()
    _verify_sdist()
    _verify_installed_wheel()
    print(f"Verified {_WHEEL.name} and {_SDIST.name}")


def _verify_wheel() -> None:
    plugin_root = f"{_DISTRIBUTION}.agent-plugin"
    metadata_root = f"{_DISTRIBUTION}.dist-info"
    with zipfile.ZipFile(_WHEEL) as archive:
        names = set(archive.namelist())
        plugin_files = {
            name.removeprefix(f"{plugin_root}/")
            for name in names
            if name.startswith(f"{plugin_root}/") and not name.endswith("/")
        }
        assert plugin_files == set(_PLUGIN_FILES)
        assert "chartcoach/agent.py" in names
        assert "chartcoach/curation.py" in names

        marker = json.loads(
            archive.read(f"{metadata_root}/agent_plugins.json").decode("utf-8")
        )
        assert marker == {"root": plugin_root, "files": list(_PLUGIN_FILES)}

        entry_points = configparser.ConfigParser()
        entry_points.read_string(
            archive.read(f"{metadata_root}/entry_points.txt").decode("utf-8")
        )
        assert dict(entry_points["marimo.agent.capability"]) == {
            "chartcoach": "chartcoach.agent"
        }


def _verify_sdist() -> None:
    plugin_root = f"{_DISTRIBUTION}/.agent-plugin"
    with tarfile.open(_SDIST, mode="r:gz") as archive:
        names = {member.name for member in archive.getmembers() if member.isfile()}
    plugin_files = {
        name.removeprefix(f"{plugin_root}/")
        for name in names
        if name.startswith(f"{plugin_root}/")
    }
    assert plugin_files == set(_PLUGIN_FILES)
    assert f"{_DISTRIBUTION}/src/chartcoach/agent.py" in names
    assert f"{_DISTRIBUTION}/src/chartcoach/curation.py" in names


def _verify_installed_wheel() -> None:
    with tempfile.TemporaryDirectory(prefix="chartcoach-package-") as directory:
        root = Path(directory)
        environment = root / "venv"
        uv = os.environ.get("UV", "uv")
        subprocess.run(
            [uv, "venv", str(environment), "--python", sys.executable],
            check=True,
            cwd=root,
        )
        python = environment / (
            "Scripts/python.exe" if os.name == "nt" else "bin/python"
        )
        subprocess.run(
            [
                uv,
                "pip",
                "install",
                "--python",
                str(python),
                str(_WHEEL),
            ],
            check=True,
            cwd=root,
        )
        smoke_environment = os.environ.copy()
        smoke_environment.pop("CHARTCOACH_SKILLS_DIR", None)
        smoke_environment.pop("PYTHONPATH", None)
        smoke_environment["CHARTCOACH_EXPECTED_PLUGIN_FILES"] = json.dumps(
            _PLUGIN_FILES
        )
        smoke_environment["CHARTCOACH_EXPECTED_SKILL_NAMES"] = json.dumps(_SKILL_NAMES)
        smoke_environment["CHARTCOACH_FIXTURE_RELEASE"] = str(_FIXTURE_RELEASE)
        subprocess.run(
            [python, "-I", "-c", _INSTALLED_SMOKE],
            check=True,
            cwd=root,
            env=smoke_environment,
        )


_INSTALLED_SMOKE = """
import json
import os
from importlib.metadata import distribution
from pathlib import Path

import chartcoach.agent as cc
from chartcoach import ProfileInfo, Catalog, CatalogManifest, Guideline, Section
from chartcoach.cli.main import main
from click.testing import CliRunner

plugin = cc.agent_plugin()
assert plugin.manifest.name == "chartcoach"
expected_files = tuple(json.loads(os.environ["CHARTCOACH_EXPECTED_PLUGIN_FILES"]))
expected_skills = list(json.loads(os.environ["CHARTCOACH_EXPECTED_SKILL_NAMES"]))
assert tuple(path.relative_to(plugin.path).as_posix() for path in plugin.files) == expected_files
assert [plugin.skill(name).path.name for name in expected_skills] == expected_skills
assert plugin.mcp is not None
assert plugin.mcp.issues == ()
launch = plugin.mcp.resolve_stdio("chartcoach", data_dir=Path.cwd())
assert launch.command == "chartcoach"
assert launch.args == ("mcp",)
assert launch.cwd == plugin.path
assert launch.env["PLUGIN_ROOT"] == str(plugin.path)
assert launch.env["PLUGIN_DATA"] == str(Path.cwd().resolve())
entry_points = [
    entry
    for entry in distribution("chartcoach").entry_points
    if entry.group == "marimo.agent.capability"
]
assert [(entry.name, entry.value) for entry in entry_points] == [
    ("chartcoach", "chartcoach.agent")
]
assert entry_points[0].load() is cc
catalog = cc.open_catalog(os.environ["CHARTCOACH_FIXTURE_RELEASE"])
candidates = catalog.query(contains="direct labels", limit=5).to_dicts()
assert candidates[0]["id"] == "direct-labels"
records = catalog.read(
    ids=[candidates[0]["id"]],
    source_detail="minimal",
)
assert records[0]["id"] == "direct-labels"
citations = catalog.cite(ids=[candidates[0]["id"]])
assert citations[0]["id"] == "direct-labels"
description = catalog.describe()
assert description["release_digest"] == catalog.release.digest
with catalog.duckdb() as connection:
    assert connection.sql("select count(*) from guidelines").fetchone() == (6,)
    assert connection.read_parquet(str(catalog.artifact("entries.parquet"))).count("*").fetchone() == (6,)
constructed = Catalog.from_guidelines([
    Guideline("example", "Use labels", "Label the marks.", sections=(Section("advice", "Advice", "Use labels."),)),
], manifest=CatalogManifest.from_text(catalog.manifest.markdown))
assert constructed.read(ids=["example"])[0]["title"] == "Use labels"

runner = CliRunner()
source = os.environ["CHARTCOACH_FIXTURE_RELEASE"]
for arguments, field in [
    (["catalog", "describe", "--source", source], "release_digest"),
    (["catalog", "list", "--source", source, "--contains", "labels"], "rows"),
    (["catalog", "read", "--source", source, "direct-labels"], "records"),
    (["catalog", "cite", "--source", source, "direct-labels"], "records"),
    (["catalog", "sql", "--source", source, "select count(*) as rows from guidelines"], "rows"),
]:
    result = runner.invoke(main, arguments)
    assert result.exit_code == 0, result.output
    assert field in json.loads(result.stdout)
listed = runner.invoke(main, ["skills", "--format", "json"])
assert listed.exit_code == 0, listed.output
assert [row["name"] for row in json.loads(listed.stdout)] == expected_skills
read = runner.invoke(main, ["skills", "get", "core"])
assert read.exit_code == 0, read.output
assert "# chartcoach Core" in read.stdout
path = runner.invoke(main, ["skills", "path", "core"])
assert path.exit_code == 0, path.output
assert Path(path.stdout.strip()) == plugin.path / "skills" / "core"
"""


if __name__ == "__main__":
    main()
