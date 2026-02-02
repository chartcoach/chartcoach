from __future__ import annotations

import json
from pathlib import Path

import pytest

import chartcoach.retrieval.analysis.stability as stability
from chartcoach.retrieval.analysis.stability import compute_stability, format_stability_table


def _write_bundle(root: Path, *, scenario_id: str, strategy_id: str, guideline_ids: list[str]) -> None:
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


def test_compute_stability_pairwise_jaccard(tmp_path) -> None:
    run1 = tmp_path / "run1"
    run2 = tmp_path / "run2"

    _write_bundle(run1, scenario_id="s1", strategy_id="hybrid@v1", guideline_ids=["a", "b", "c"])
    _write_bundle(run2, scenario_id="s1", strategy_id="hybrid@v1", guideline_ids=["b", "c", "d"])

    results = compute_stability(runs=[run1, run2], k=3)
    assert len(results) == 1
    r = results[0]
    assert r.strategy_id == "hybrid@v1"
    assert r.scenarios["s1"] == 0.5  # |{b,c}| / |{a,b,c,d}|
    assert r.mean_jaccard == 0.5


def test_format_stability_table(tmp_path) -> None:
    run1 = tmp_path / "run1"
    run2 = tmp_path / "run2"
    _write_bundle(run1, scenario_id="s1", strategy_id="hybrid@v1", guideline_ids=["a"])
    _write_bundle(run2, scenario_id="s1", strategy_id="hybrid@v1", guideline_ids=["a"])

    table = format_stability_table(compute_stability(runs=[run1, run2], k=1))
    assert "| strategy | mean_jaccard |" in table
    assert "| hybrid@v1 | 1.000 |" in table


def test_pairwise_jaccard_handles_single_and_empty_sets() -> None:
    assert stability._pairwise_jaccard([set()]) == 1.0
    assert stability._pairwise_jaccard([set(), set()]) == 1.0


def test_extract_guideline_id_branches() -> None:
    assert stability._extract_guideline_id(None) is None
    assert stability._extract_guideline_id({"id": "x"}) == "x"
    assert stability._extract_guideline_id({"guideline": {"id": "y"}}) == "y"
    assert stability._extract_guideline_id({"guideline": "nope", "id": "z"}) == "z"


def test_load_run_bundle_sets_requires_bundles_dir(tmp_path) -> None:
    with pytest.raises(FileNotFoundError):
        stability.load_run_bundle_sets(artifacts_root=tmp_path / "missing", k=None)


def test_load_run_bundle_sets_skips_invalid_records(tmp_path) -> None:
    root = tmp_path / "run"
    bundles = root / "bundles"
    bundles.mkdir(parents=True)

    # scenario not dict
    (bundles / "bad1.json").write_text(json.dumps({"scenario": "nope"}), encoding="utf-8")
    # scenario missing id
    (bundles / "bad2.json").write_text(json.dumps({"scenario": {"id": ""}}), encoding="utf-8")
    # strategies not list
    (bundles / "bad3.json").write_text(
        json.dumps({"scenario": {"id": "s1", "title": "T", "lang": "en"}, "strategies": "nope"}),
        encoding="utf-8",
    )
    # strategy not dict
    (bundles / "bad4.json").write_text(
        json.dumps({"scenario": {"id": "s2", "title": "T", "lang": "en"}, "strategies": [1]}),
        encoding="utf-8",
    )
    # invalid strategy_id + invalid guidelines shapes
    (bundles / "bad5.json").write_text(
        json.dumps(
            {
                "scenario": {"id": "s3", "title": "T", "lang": "en"},
                "strategies": [
                    {"strategy_id": "", "guidelines": []},
                    {"strategy_id": "ok", "guidelines": "nope"},
                ],
            }
        ),
        encoding="utf-8",
    )
    # rows with non-dict and missing guideline ids
    (bundles / "bad6.json").write_text(
        json.dumps(
            {
                "scenario": {"id": "s4", "title": "T", "lang": "en"},
                "strategies": [
                    {
                        "strategy_id": "ok",
                        "guidelines": [
                            1,
                            {"entry": 1},
                            {"entry": {"guideline": {}}},
                            {"entry": {"id": "g1"}},
                        ],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    out = stability.load_run_bundle_sets(artifacts_root=root, k=10)
    assert out["s4"]["ok"] == ["g1"]


def test_compute_stability_requires_two_runs(tmp_path) -> None:
    with pytest.raises(ValueError, match="at least 2"):
        compute_stability(runs=[tmp_path], k=1)


def test_compute_stability_handles_no_overlap(tmp_path) -> None:
    run1 = tmp_path / "run1"
    run2 = tmp_path / "run2"
    _write_bundle(run1, scenario_id="s1", strategy_id="a", guideline_ids=["x"])
    _write_bundle(run2, scenario_id="s2", strategy_id="a", guideline_ids=["x"])
    assert compute_stability(runs=[run1, run2], k=1) == []


def test_compute_stability_handles_no_strategy_overlap(tmp_path) -> None:
    run1 = tmp_path / "run1"
    run2 = tmp_path / "run2"
    _write_bundle(run1, scenario_id="s1", strategy_id="a", guideline_ids=["x"])
    _write_bundle(run2, scenario_id="s1", strategy_id="b", guideline_ids=["x"])
    assert compute_stability(runs=[run1, run2], k=1) == []


def test_compute_stability_skips_missing_strategy_per_scenario(tmp_path) -> None:
    run1 = tmp_path / "run1"
    run2 = tmp_path / "run2"
    _write_bundle(run1, scenario_id="s1", strategy_id="a", guideline_ids=["x"])
    _write_bundle(run2, scenario_id="s1", strategy_id="a", guideline_ids=["x"])

    # Same scenario ids exist in both runs, but strategy "a" is missing for s2 in run1.
    _write_bundle(run1, scenario_id="s2", strategy_id="b", guideline_ids=["y"])
    _write_bundle(run2, scenario_id="s2", strategy_id="a", guideline_ids=["y"])

    results = compute_stability(runs=[run1, run2], k=1)
    assert len(results) == 1
    assert results[0].strategy_id == "a"
    assert results[0].scenarios == {"s1": 1.0}


def test_format_stability_table_handles_empty() -> None:
    assert "No overlapping" in format_stability_table([])
