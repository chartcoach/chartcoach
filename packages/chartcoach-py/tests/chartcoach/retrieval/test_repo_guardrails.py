from __future__ import annotations

import subprocess
from pathlib import Path

import yaml


def _repo_root() -> Path:
    cwd = Path.cwd().resolve()
    for candidate in [cwd, *cwd.parents]:
        if (candidate / "packages").exists() and (candidate / "apps").exists():
            return candidate
    raise RuntimeError("Could not locate repo root from cwd.")


def _git_tracked_paths(repo_root: Path) -> list[Path]:
    out = subprocess.check_output(
        ["git", "ls-files"],
        cwd=str(repo_root),
        text=True,
    )
    return [repo_root / line for line in out.splitlines() if line.strip()]


def _load_eval_scenario_ids(repo_root: Path) -> set[str]:
    scenarios_path = repo_root / "evals" / "scenarios" / "spec.yaml"
    if not scenarios_path.exists():
        return set()
    loaded = yaml.safe_load(scenarios_path.read_text(encoding="utf-8"))
    if not isinstance(loaded, dict):
        return set()
    scenarios = loaded.get("scenarios")
    if not isinstance(scenarios, list):
        return set()
    ids: set[str] = set()
    for scenario in scenarios:
        if not isinstance(scenario, dict):
            continue
        raw = scenario.get("id")
        if isinstance(raw, str) and raw.strip():
            ids.add(raw.strip())
    return ids


def test_no_hints_files_tracked() -> None:
    repo_root = _repo_root()
    tracked = _git_tracked_paths(repo_root)
    offenders = [
        p.as_posix()
        for p in tracked
        if p.name.startswith("hints_") and p.suffix == ".py"
    ]
    assert offenders == []


def test_strategy_code_does_not_reference_eval_specs_or_scenario_ids() -> None:
    repo_root = _repo_root()
    scenario_ids = {s for s in _load_eval_scenario_ids(repo_root) if len(s) >= 8}
    forbidden_substrings = {
        "evals/scenarios",
        "nogit/strat-eval",
    }

    roots = [
        repo_root
        / "packages"
        / "chartcoach-py"
        / "src"
        / "chartcoach"
        / "retrieval"
        / "strategy",
        repo_root
        / "packages"
        / "chartcoach-py"
        / "src"
        / "chartcoach"
        / "retrieval"
        / "operators",
    ]

    offenders: list[str] = []
    for root in roots:
        for path in root.rglob("*.py"):
            if path.name == "__init__.py":
                continue
            text = path.read_text(encoding="utf-8")
            if any(s in text for s in forbidden_substrings):
                offenders.append(path.relative_to(repo_root).as_posix())
                continue
            for scenario_id in scenario_ids:
                if scenario_id in text:
                    offenders.append(path.relative_to(repo_root).as_posix())
                    break

    assert offenders == []
