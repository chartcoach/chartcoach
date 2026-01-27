from __future__ import annotations

import json

import pytest

from obstore.store import MemoryStore

from chartcoach.catalog import Catalog, CatalogEntry, Guideline
from chartcoach.retrieval.service.eval_artifacts import (
    ScenarioChart,
    ScenarioSpec,
    build_bundle_digest,
    build_retrieval_request,
    build_scenario_bundle,
    compute_digest,
    delete_paths,
    entry_score,
    list_paths,
    load_scenarios,
    now_iso,
    read_json,
    write_json,
)
from chartcoach.retrieval.strategy.base import RetrievalStrategy, StrategyInfo
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse


def test_now_iso_is_isoish() -> None:
    value = now_iso()
    assert value.endswith("+00:00")
    assert "T" in value


def test_load_scenarios_parses_yaml(tmp_path) -> None:
    path = tmp_path / "spec.yaml"
    path.write_text(
        """
scenarios:
  - id: s1
    title: Scenario 1
    lang: en
    chart:
      uri: https://example.invalid/chart.png
      mime: image/png
    query: Retrieve guidelines.
    designer_intent: Improve the chart.
""".lstrip(),
        encoding="utf-8",
    )

    scenarios = load_scenarios(path)
    assert [s.id for s in scenarios] == ["s1"]
    assert scenarios[0].chart is not None
    assert scenarios[0].chart.uri.startswith("https://")


def test_build_retrieval_request_requires_designer_intent() -> None:
    scenario = ScenarioSpec(
        id="s1",
        title="Scenario 1",
        lang="en",
        chart=ScenarioChart(uri="https://example.invalid/chart.png", mime="image/png"),
        query="Retrieve guidelines.",
        designer_intent="   ",
    )
    with pytest.raises(ValueError, match="designer_intent"):
        build_retrieval_request(scenario, k=None)


def test_build_retrieval_request_shapes_context() -> None:
    scenario = ScenarioSpec(
        id="s1",
        title="Scenario 1",
        lang="en",
        chart=ScenarioChart(uri="https://example.invalid/chart.png", mime="image/png"),
        query="Retrieve guidelines.",
        designer_intent="Improve the chart.",
    )
    request = build_retrieval_request(scenario, k=5)
    assert request.k == 5
    assert any(i.role == "chart" for i in request.context)
    assert any(i.role == "situation" for i in request.context)
    assert any(i.role == "chart_spec" for i in request.context)


def test_compute_digest_is_stable() -> None:
    assert compute_digest({"a": 1, "b": 2}) == compute_digest({"b": 2, "a": 1})


def test_bundle_digest_changes_with_inputs() -> None:
    scenario = ScenarioSpec(
        id="s1",
        title="Scenario 1",
        lang="en",
        chart=ScenarioChart(uri="https://example.invalid/chart.png", mime="image/png"),
        query="Retrieve guidelines.",
        designer_intent="Improve the chart.",
    )
    d1 = build_bundle_digest(
        scenario=scenario,
        catalog_uri="file:///tmp/catalog.parquet",
        strategy_ids=["a"],
        k=None,
    )
    d2 = build_bundle_digest(
        scenario=scenario,
        catalog_uri="file:///tmp/catalog.parquet",
        strategy_ids=["a"],
        k=10,
    )
    assert d1 != d2


def test_entry_score_monotone() -> None:
    scores = [entry_score(i, 5) for i in range(5)]
    assert scores[0] > scores[1] > scores[2]
    assert scores[-1] >= 0.01


def test_read_write_list_delete_json_roundtrip() -> None:
    store = MemoryStore()
    write_json(store, "index.json", {"ok": True})
    assert read_json(store, "index.json") == {"ok": True}
    assert read_json(store, "missing.json") is None

    write_json(store, "nested/a.json", {"a": 1})
    paths = list_paths(store, prefix="nested/")
    assert paths == ["nested/a.json"]

    delete_paths(store, paths)
    assert read_json(store, "nested/a.json") is None


def test_read_json_requires_object() -> None:
    import obstore

    store = MemoryStore()
    obstore.put(store, "arr.json", b"[]")
    with pytest.raises(ValueError, match="Expected JSON object"):
        read_json(store, "arr.json")


def test_build_scenario_bundle_runs_strategies() -> None:
    class DummyStrategy(RetrievalStrategy):
        id = "dummy@v0"

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
            entry = CatalogEntry(
                guideline=Guideline(
                    id="g1",
                    title="T",
                    description="D",
                    labels=[],
                    body="B",
                ),
                references=[],
            )
            return RetrievalResponse(
                catalog=Catalog(entries=[entry]),
                meta={"k": request.k},
            )

    scenario = ScenarioSpec(
        id="s1",
        title="Scenario 1",
        lang="en",
        chart=ScenarioChart(uri="https://example.invalid/chart.png", mime="image/png"),
        query="Retrieve guidelines.",
        designer_intent="Improve the chart.",
    )
    bundle = build_scenario_bundle(
        scenario=scenario,
        catalog_uri="file:///tmp/catalog.parquet",
        strategies=[
            (
                StrategyInfo(id="dummy@v0", name="DummyStrategy", description=""),
                DummyStrategy(Catalog(entries=[])),
            )
        ],
        k=3,
    )
    assert bundle.schema_version == 1
    assert bundle.scenario.id == scenario.id
    assert bundle.strategies[0].strategy_id == "dummy@v0"
    assert bundle.strategies[0].meta["k"] == 3
    assert bundle.strategies[0].guidelines[0].rank == 1
    assert bundle.strategies[0].guidelines[0].entry.guideline.id == "g1"

    # bundle is JSON-serializable
    json.dumps(bundle.model_dump(mode="json"))


def test_build_scenario_bundle_records_strategy_errors() -> None:
    class FailingStrategy(RetrievalStrategy):
        id = "failing@v0"

        def _forward(self, request: RetrievalRequest) -> RetrievalResponse:  # noqa: ARG002
            raise ValueError("boom")

    scenario = ScenarioSpec(
        id="s1",
        title="Scenario 1",
        lang="en",
        chart=ScenarioChart(uri="https://example.invalid/chart.png", mime="image/png"),
        query="Retrieve guidelines.",
        designer_intent="Improve the chart.",
    )
    bundle = build_scenario_bundle(
        scenario=scenario,
        catalog_uri="file:///tmp/catalog.parquet",
        strategies=[
            (
                StrategyInfo(id="failing@v0", name="FailingStrategy", description=""),
                FailingStrategy(Catalog(entries=[])),
            )
        ],
        k=3,
    )
    assert bundle.strategies[0].strategy_id == "failing@v0"
    assert "boom" in str(bundle.strategies[0].meta.get("error"))
    assert bundle.strategies[0].guidelines == []
