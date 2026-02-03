from __future__ import annotations

import json
from pathlib import Path

import pytest

from chartcoach.retrieval.analysis.negatives import (
    compute_negative_hit_rates,
    format_negative_hit_table,
    load_negative_guideline_ids,
)


def _write_bundle(
    root: Path, *, scenario_id: str, strategies: dict[str, list[str]]
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
            for strategy_id, guideline_ids in strategies.items()
        ],
    }
    (bundles / f"{scenario_id}.json").write_text(json.dumps(payload), encoding="utf-8")


def test_load_negative_guideline_ids_requires_index(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_negative_guideline_ids(artifacts_root=tmp_path)


def test_negative_hit_rates_compute_fraction_and_any_hit(tmp_path: Path) -> None:
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
                        "negative_guideline_ids": ["bad"],
                    },
                    {"id": "s2", "title": "T", "lang": "en"},
                ],
            }
        ),
        encoding="utf-8",
    )

    _write_bundle(
        run, scenario_id="s1", strategies={"a@v1": ["bad", "ok"], "b@v1": ["ok", "ok2"]}
    )
    _write_bundle(run, scenario_id="s2", strategies={"a@v1": ["ok"], "b@v1": ["ok2"]})

    results = compute_negative_hit_rates(artifacts_root=run, k=2)
    assert [r.strategy_id for r in results] == ["b@v1", "a@v1"]

    by_id = {r.strategy_id: r for r in results}
    assert by_id["b@v1"].mean_negative_fraction == 0.0
    assert by_id["b@v1"].any_negative_fraction == 0.0
    assert by_id["a@v1"].scenarios["s1"] == 0.5
    assert by_id["a@v1"].mean_negative_fraction == 0.5
    assert by_id["a@v1"].any_negative_fraction == 1.0

    table = format_negative_hit_table(results)
    assert "| strategy | mean_negative_frac" in table
