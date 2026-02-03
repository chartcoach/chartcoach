from __future__ import annotations

import json
from pathlib import Path

import pytest

from chartcoach.retrieval.analysis.counterfactual import (
    compute_counterfactual_sensitivity,
    format_counterfactual_table,
    load_counterfactual_groups,
)
from chartcoach.retrieval.analysis.pooling import (
    compute_pool_coverage,
    format_pool_table,
)


def _write_bundle(
    root: Path, *, scenario_id: str, strategy_id: str, guideline_ids: list[str]
) -> None:
    bundles = root / "bundles"
    bundles.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "scenario": {"id": scenario_id, "title": "T", "lang": "en"},
        "strategies": [
            {
                "strategy_id": strategy_id,
                "strategy_name": "S",
                "meta": {},
                "guidelines": [
                    {
                        "rank": i + 1,
                        "score": 1.0,
                        "entry": {"guideline": {"id": gid}, "references": []},
                    }
                    for i, gid in enumerate(guideline_ids)
                ],
            }
        ],
    }
    (bundles / f"{scenario_id}.json").write_text(json.dumps(payload), encoding="utf-8")


def test_load_counterfactual_groups_requires_index(tmp_path) -> None:
    with pytest.raises(FileNotFoundError):
        load_counterfactual_groups(artifacts_root=tmp_path)


def test_counterfactual_sensitivity_computes_group_overlap(tmp_path) -> None:
    run = tmp_path / "run"
    run.mkdir(parents=True)
    (run / "index.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "generated_at": "now",
                "strategies": [],
                "scenarios": [
                    {
                        "id": "s1",
                        "title": "T",
                        "lang": "en",
                        "counterfactual_group_id": "g",
                    },
                    {
                        "id": "s2",
                        "title": "T",
                        "lang": "en",
                        "counterfactual_group_id": "g",
                    },
                ],
            }
        ),
        encoding="utf-8",
    )

    _write_bundle(run, scenario_id="s1", strategy_id="a@v1", guideline_ids=["x", "y"])
    _write_bundle(run, scenario_id="s2", strategy_id="a@v1", guideline_ids=["y", "z"])

    results = compute_counterfactual_sensitivity(artifacts_root=run, k=2)
    assert len(results) == 1
    assert results[0].strategy_id == "a@v1"
    assert results[0].groups["g"] == 1 / 3
    assert abs(results[0].mean_jaccard - (1 / 3)) <= 1e-9

    table = format_counterfactual_table(results)
    assert "| strategy | mean_overlap" in table


def test_pool_coverage_reports_union_size(tmp_path) -> None:
    run = tmp_path / "run"
    _write_bundle(run, scenario_id="s1", strategy_id="a@v1", guideline_ids=["x"])
    # Add a second strategy into same bundle file by writing a second bundle for scenario s1.
    bundles = run / "bundles"
    payload = json.loads((bundles / "s1.json").read_text(encoding="utf-8"))
    payload["strategies"].append(
        {
            "strategy_id": "b@v1",
            "strategy_name": "S",
            "meta": {},
            "guidelines": [
                {
                    "rank": 1,
                    "score": 1.0,
                    "entry": {"guideline": {"id": "y"}, "references": []},
                }
            ],
        }
    )
    (bundles / "s1.json").write_text(json.dumps(payload), encoding="utf-8")

    results = compute_pool_coverage(artifacts_root=run, k=1)
    assert results[0].scenario_id == "s1"
    assert results[0].strategies == 2
    assert results[0].unique_guidelines == 2
    assert "pool_size" in format_pool_table(results)
