from __future__ import annotations

import argparse
import configparser
import email
import json
import os
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from pathlib import Path

_REPOSITORY = Path(__file__).parents[3]
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
    parser = argparse.ArgumentParser(
        description="Verify built ChartCoach distributions."
    )
    parser.add_argument(
        "--dist-dir",
        type=Path,
        default=_REPOSITORY / "dist",
        help="Directory containing the wheel and source distribution to verify.",
    )
    parser.add_argument(
        "--minimum-dependencies",
        action="store_true",
        help="Install the lowest compatible direct dependencies and run the full tests.",
    )
    options = parser.parse_args()
    wheels = list(options.dist_dir.resolve().glob("chartcoach-*-py3-none-any.whl"))
    if len(wheels) != 1:
        parser.error("Expected exactly one ChartCoach wheel in --dist-dir")
    wheel = wheels[0]
    distribution = wheel.name.removesuffix("-py3-none-any.whl")
    sdist = wheel.with_name(f"{distribution}.tar.gz")
    distributions = {
        path
        for path in options.dist_dir.resolve().iterdir()
        if path.name.endswith((".whl", ".tar.gz"))
    }
    if distributions != {wheel, sdist}:
        parser.error(
            "Expected exactly one ChartCoach wheel and matching source distribution"
        )
    _verify_wheel(wheel, distribution)
    _verify_sdist(sdist, distribution)
    _verify_installed_wheel(wheel, minimum_dependencies=options.minimum_dependencies)
    print(f"Verified {wheel.name} and {sdist.name}")


def _verify_wheel(wheel: Path, distribution: str) -> None:
    plugin_root = f"{distribution}.agent-plugin"
    metadata_root = f"{distribution}.dist-info"
    with zipfile.ZipFile(wheel) as archive:
        names = set(archive.namelist())
        plugin_files = {
            name.removeprefix(f"{plugin_root}/")
            for name in names
            if name.startswith(f"{plugin_root}/") and not name.endswith("/")
        }
        assert plugin_files == set(_PLUGIN_FILES)
        assert "chartcoach/agent.py" in names
        assert "chartcoach/curation.py" in names
        metadata = email.message_from_bytes(archive.read(f"{metadata_root}/METADATA"))
        assert metadata["Name"] == "chartcoach"
        assert metadata["Version"] == distribution.removeprefix("chartcoach-")

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


def _verify_sdist(sdist: Path, distribution: str) -> None:
    plugin_root = f"{distribution}/.agent-plugin"
    with tarfile.open(sdist, mode="r:gz") as archive:
        names = {member.name for member in archive.getmembers() if member.isfile()}
        metadata_file = archive.extractfile(f"{distribution}/PKG-INFO")
        assert metadata_file is not None
        metadata = email.message_from_bytes(metadata_file.read())
        assert metadata["Name"] == "chartcoach"
        assert metadata["Version"] == distribution.removeprefix("chartcoach-")
    plugin_files = {
        name.removeprefix(f"{plugin_root}/")
        for name in names
        if name.startswith(f"{plugin_root}/")
    }
    assert plugin_files == set(_PLUGIN_FILES)
    assert f"{distribution}/src/chartcoach/agent.py" in names
    assert f"{distribution}/src/chartcoach/curation.py" in names


def _verify_installed_wheel(wheel: Path, *, minimum_dependencies: bool = False) -> None:
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
        requirements = []
        if minimum_dependencies:
            requirements = [
                "--resolution",
                "lowest-direct",
                "--only-binary",
                ":all:",
                "--requirements",
                str(_REPOSITORY / "packages/chartcoach/pyproject.toml"),
            ]
        install = [
            uv,
            "--directory",
            str(_REPOSITORY),
            "pip",
            "install",
            "--python",
            str(python),
            str(wheel),
            *requirements,
        ]
        subprocess.run(
            install,
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
        if minimum_dependencies:
            subprocess.run(
                [*install, "--all-extras", "pytest>=9.0.3"],
                check=True,
                cwd=root,
            )
            subprocess.run(
                [
                    python,
                    "-m",
                    "pytest",
                    str(_REPOSITORY / "packages/chartcoach/tests"),
                ],
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
