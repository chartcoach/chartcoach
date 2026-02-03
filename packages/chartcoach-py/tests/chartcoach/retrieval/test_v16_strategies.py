from __future__ import annotations

from typing import cast

import numpy as np
import polars as pl
import pytest

import dspy

from chartcoach.catalog import Catalog
from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.embedding import GuidelineAbstractTextSource
from chartcoach.index import VectorIndex
from chartcoach.retrieval.strategy.pipelines.ann_dense import AnnDenseStrategy
from chartcoach.retrieval.strategy.pipelines.decompose_parallel import (
    DecomposeParallelStrategy,
)
from chartcoach.retrieval.strategy.pipelines.focus import (
    FocusConfig,
    fallback_roles_for_focus,
    focus_config_from_env,
    primary_roles_for_focus,
)
from chartcoach.retrieval.strategy.pipelines.guideline_status import (
    StatusScorerConfig,
    filter_guidelines_by_status,
)
from chartcoach.retrieval.strategy.pipelines.label_first_abstract import (
    LabelFirstAbstractStrategy,
)
from chartcoach.retrieval.strategy.pipelines.label_gated_ann import (
    LabelGatedAnnStrategy,
)
from chartcoach.retrieval.strategy.pipelines.label_hints import (
    match_catalog_ids_by_label_hints,
)
from chartcoach.retrieval.strategy.pipelines.neighborhood_explorer import (
    NeighborhoodExplorerStrategy,
)
from chartcoach.retrieval.strategy.pipelines.role_aware_sections import (
    RoleAwareSectionsStrategy,
)
from chartcoach.retrieval.strategy.pipelines.searcher import GuidelineSearcher
from chartcoach.retrieval.strategy.types import ImageItem, RetrievalRequest, TextItem
from chartcoach.retrieval.strategy.vector_index import (
    CatalogVectorIndex,
    EmbeddingConfig,
)


class _FakeLanceIndex:
    backend = "lance"

    def __init__(self) -> None:
        self._dense_by_role: dict[str, pl.DataFrame] = {}
        self._hybrid_by_query: dict[str, pl.DataFrame] = {}

    def set_dense(self, *, role: str, df: pl.DataFrame) -> None:
        self._dense_by_role[role] = df

    def set_hybrid(self, *, query: str, df: pl.DataFrame) -> None:
        self._hybrid_by_query[query] = df

    def search(self, _query: np.ndarray, *, k: int = 10, roles=None, ids=None):  # noqa: ANN001
        df = self._dense_by_role.get("default", pl.DataFrame()).head(k)
        if roles:
            # Simple behavior to exercise role-fallback: require advice to return rows.
            role_set = set(roles)
            if len(role_set) > 1 and "advice" not in role_set:
                df = pl.DataFrame({"id": [], "role": [], "score": []})
        if ids:
            df = df.filter(pl.col("id").is_in(sorted(ids)))
        return df.head(k)

    def search_fts(self, query: str, *, k: int = 10, roles=None, ids=None):  # noqa: ANN001
        _ = (roles, ids)
        return self._hybrid_by_query.get(query, pl.DataFrame()).head(k)

    def search_hybrid(  # noqa: PLR0913
        self,
        *,
        query_text: str,
        query_vector: np.ndarray,  # noqa: ARG002
        reranker=None,  # noqa: ANN001
        k: int = 10,
        roles=None,  # noqa: ANN001
        ids=None,  # noqa: ANN001
        fts_columns=None,  # noqa: ANN001
    ):
        _ = (reranker, fts_columns)
        df = self._hybrid_by_query.get(query_text, pl.DataFrame()).head(k)
        if roles:
            role_set = set(roles)
            if len(role_set) > 1 and "advice" not in role_set:
                df = pl.DataFrame({"id": [], "role": [], "score": []})
        if ids:
            df = df.filter(pl.col("id").is_in(sorted(ids)))
        return df.head(k)


def _make_vector_index(
    *, catalog: Catalog, fake: _FakeLanceIndex
) -> CatalogVectorIndex:
    embedded = pl.DataFrame(
        {
            "id": ["g1", "g2", "g3"],
            "role": ["advice", "advice", "advice"],
            "content": ["a", "b", "c"],
            "embedding": [[1.0, 0.0], [1.0, 0.0], [0.0, 1.0]],
        }
    )
    return CatalogVectorIndex(
        catalog=catalog,
        sources=tuple(),
        config=EmbeddingConfig(model="fake"),
        embedded_text_df=embedded,
        index=cast(VectorIndex, fake),
    )


@pytest.fixture()
def catalog() -> Catalog:
    return Catalog(
        entries=[
            CatalogEntry(
                guideline=Guideline(
                    id="g1",
                    title="Use accessible colors",
                    description="Ensure color choices are accessible.",
                    labels=["topic:color", "audience:general"],
                    body=(
                        "## Advice <!-- role: advice -->\nUse colorblind-safe palettes.\n\n"
                        "## Context <!-- role: context -->\nAccessibility matters.\n\n"
                        "## Exceptions <!-- role: exceptions -->\nSome cases allow nonstandard colors.\n"
                    ),
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g2",
                    title="Label axes clearly",
                    description="Axis labels should be clear.",
                    labels=["topic:annotation"],
                    body="## Advice <!-- role: advice -->\nAdd axis titles.\n",
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=Guideline(
                    id="g3",
                    title="Add context annotations",
                    description="Add context to avoid misinterpretation.",
                    labels=["topic:annotation", "impact:credibility"],
                    body="## Advice <!-- role: advice -->\nAdd context notes.\n",
                ),
                references=[],
            ),
        ]
    )


def test_focus_env_and_role_helpers(monkeypatch) -> None:
    monkeypatch.delenv("CHARTCOACH_STRATEGY_FOCUS", raising=False)
    monkeypatch.delenv("CHARTCOACH_STRATEGY_FOCUS_ROLE_FALLBACK", raising=False)
    monkeypatch.delenv("CHARTCOACH_STRATEGY_STATUS_FILTER", raising=False)
    cfg = focus_config_from_env()
    assert cfg.mode == "all"
    assert cfg.allow_role_fallback is True
    assert cfg.use_status_filter is False

    monkeypatch.setenv("CHARTCOACH_STRATEGY_FOCUS", "violations")
    monkeypatch.setenv("CHARTCOACH_STRATEGY_FOCUS_ROLE_FALLBACK", "0")
    cfg = focus_config_from_env(default="satisfied")
    assert cfg.mode == "violations"
    assert cfg.allow_role_fallback is False
    assert cfg.use_status_filter is False

    monkeypatch.setenv("CHARTCOACH_STRATEGY_FOCUS", "not-a-mode")
    cfg = focus_config_from_env(default="satisfied")
    assert cfg.mode == "satisfied"

    monkeypatch.setenv("CHARTCOACH_STRATEGY_STATUS_FILTER", "1")
    cfg = focus_config_from_env()
    assert cfg.use_status_filter is True

    assert primary_roles_for_focus("all") is None
    assert primary_roles_for_focus("violations") == {
        "fix",
        "mistakes",
        "exceptions",
        "check",
    }
    assert primary_roles_for_focus("satisfied") == {"check", "reason", "context"}
    assert primary_roles_for_focus("other") is None  # type: ignore[arg-type]
    fallback = fallback_roles_for_focus("violations")
    assert fallback is not None
    # When role-filtered retrieval yields empty results, broaden to include
    # guideline-level fields and untagged sections for recall.
    assert {"fix", "mistakes", "exceptions", "check", "advice"} <= fallback
    assert {"title", "description", "labels", "__dangling__"} <= fallback
    assert fallback_roles_for_focus("all") is None


def test_label_matching_helpers(catalog: Catalog) -> None:
    ids, matched = match_catalog_ids_by_label_hints(
        catalog=catalog, label_hints=["topic:annotation"]
    )
    assert ids == {"g2", "g3"}
    assert "topic:annotation" in matched

    ids, matched = match_catalog_ids_by_label_hints(
        catalog=catalog, label_hints=["annotation"]
    )
    assert ids == {"g2", "g3"}
    assert matched

    ids, matched = match_catalog_ids_by_label_hints(catalog=catalog, label_hints=[])
    assert ids == set()
    assert matched == {}

    # Empty/whitespace hints normalize to nothing.
    ids, matched = match_catalog_ids_by_label_hints(catalog=catalog, label_hints=[" "])
    assert ids == set()
    assert matched == {}

    # Catalog entries with no labels are skipped safely.
    from chartcoach.catalog.model import CatalogEntry, Guideline as GuidelineModel

    no_label_catalog = Catalog(
        entries=[
            CatalogEntry(
                guideline=GuidelineModel(
                    id="g0",
                    title="No labels",
                    description="",
                    labels=[],
                    body="## Advice <!-- role: advice -->\nText.\n",
                ),
                references=[],
            )
        ]
    )
    ids, matched = match_catalog_ids_by_label_hints(
        catalog=no_label_catalog, label_hints=["topic:annotation"]
    )
    assert ids == set()
    assert matched


def test_guideline_abstract_text_source_variants(catalog: Catalog) -> None:
    src = GuidelineAbstractTextSource()
    df = src.text_df(catalog)
    assert set(df.columns) == {"id", "role", "content"}
    assert df.filter(pl.col("id") == "g1").get_column("role").to_list() == ["abstract"]

    df_no_labels = GuidelineAbstractTextSource(include_labels=False).text_df(catalog)
    assert "Labels:" not in "\n".join(df_no_labels.get_column("content").to_list())


def test_filter_guidelines_by_status_selects_focus_and_uses_chart_key(
    monkeypatch, catalog: Catalog
) -> None:
    request = RetrievalRequest(
        context=[
            TextItem(role="title", text="T"),
            TextItem(role="situation", text="S"),
            ImageItem(role="chart", uri="file:///tmp/x.png"),
        ],
        k=2,
    )

    entries = catalog.entries

    seen_chart_keys: list[str] = []

    class DummyStatusModule:
        def classify_many(self, *, chart_key: str, situation: str, entries):  # noqa: ANN001
            _ = situation
            seen_chart_keys.append(chart_key)
            # Force only g2 as violated; g1 unclear; g3 satisfied.
            out = []
            for e in entries:
                if e.id == "g2":
                    out.append({"id": e.id, "status": "violated", "confidence": 1.0})
                elif e.id == "g3":
                    out.append({"id": e.id, "status": "satisfied", "confidence": 1.0})
                else:
                    out.append({"id": e.id, "status": "unclear", "confidence": 0.0})
            return out

    cfg = StatusScorerConfig(candidate_multiplier=2, keep_unclear=True, batch_size=10)
    selected, meta = filter_guidelines_by_status(
        request=request,
        entries=entries,
        output_k=2,
        focus="violations",
        status_module=DummyStatusModule(),
        config=cfg,
    )
    assert [e.id for e in selected] == ["g2", "g1"]
    assert meta["guideline_status_used"] is True
    assert seen_chart_keys and seen_chart_keys[0].startswith("uri:")

    # Focus=all is a no-op.
    selected, meta = filter_guidelines_by_status(
        request=request,
        entries=entries,
        output_k=1,
        focus="all",
        status_module=DummyStatusModule(),
        config=cfg,
    )
    assert [e.id for e in selected] == ["g1"]
    assert meta["guideline_status_used"] is False


def test_ann_dense_strategy_applies_role_fallback_and_status_focus(
    monkeypatch, catalog: Catalog
) -> None:
    from chartcoach.retrieval.strategy.pipelines import ann_dense as mod

    fake = _FakeLanceIndex()
    fake.set_dense(
        role="default",
        df=pl.DataFrame(
            {"id": ["g1", "g2"], "role": ["advice", "advice"], "score": [2.0, 1.0]}
        ),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    class DummyStatus:
        def classify_many(self, *, chart_key: str, situation: str, entries):  # noqa: ANN001
            _ = (chart_key, situation)
            return [
                {"id": e.id, "status": ("violated" if e.id == "g2" else "unclear")}
                for e in entries
            ]

    monkeypatch.setattr(
        mod,
        "shared_status_scorer",
        lambda: ("lm", DummyStatus(), StatusScorerConfig(candidate_multiplier=2)),
    )

    strat = AnnDenseStrategy(
        catalog=catalog,
        searcher=searcher,
        default_k=1,
        focus=FocusConfig(mode="violations", allow_role_fallback=True, use_status_filter=True),
    )
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert [e.id for e in out.catalog.entries] == ["g2"]
    assert out.meta["focus"]["mode"] == "violations"
    assert out.meta["guideline_status_used"] is True


def test_ann_dense_strategy_calls_chart_vision_when_enabled(
    monkeypatch, catalog: Catalog
) -> None:
    from chartcoach.retrieval.strategy.pipelines import ann_dense as mod

    monkeypatch.setenv("CHARTCOACH_CHART_VISION_ENABLED", "1")

    fake = _FakeLanceIndex()
    fake.set_dense(
        role="default",
        df=pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]}),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    monkeypatch.setattr(mod, "create_strategy_vlm", lambda: object())

    seen = {"called": False}

    def fake_with_chart_vision(request, *, base_situation, vision):  # noqa: ANN001
        _ = (base_situation, vision)
        seen["called"] = True
        return request, {"chart_vision_used": True}

    monkeypatch.setattr(mod, "with_chart_vision", fake_with_chart_vision)

    strat = AnnDenseStrategy(catalog=catalog, searcher=searcher, default_k=1)
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert seen["called"] is True
    assert out.meta["chart_vision"]["chart_vision_used"] is True


def test_label_gated_ann_strategy_falls_back_when_gate_empty(
    monkeypatch, catalog: Catalog
) -> None:
    from chartcoach.retrieval.strategy.pipelines import label_gated_ann as mod

    fake = _FakeLanceIndex()
    # Dense results do not include g3, so gating to g3 forces a fallback.
    fake.set_dense(
        role="default",
        df=pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]}),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = LabelGatedAnnStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=1,
        focus=FocusConfig(mode="violations", allow_role_fallback=True),
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(
                canonical_query="S", label_hints=["impact:credibility"]
            )

    strat._program = DummyProgram()

    class DummyStatus:
        def classify_many(self, *, chart_key: str, situation: str, entries):  # noqa: ANN001
            _ = (chart_key, situation)
            return [{"id": e.id, "status": "violated"} for e in entries]

    monkeypatch.setattr(
        mod,
        "shared_status_scorer",
        lambda: ("lm", DummyStatus(), StatusScorerConfig(candidate_multiplier=2)),
    )

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert [e.id for e in out.catalog.entries] == ["g1"]
    assert out.meta["label_gating"]["candidate_filter_used"] is True


def test_label_strategies_clean_list_support_string_and_dedupe() -> None:
    assert LabelGatedAnnStrategy._clean_list(" topic:annotation ") == [
        "topic:annotation"
    ]
    assert LabelGatedAnnStrategy._clean_list(["a", "A", "b"]) == ["a", "b"]

    assert LabelFirstAbstractStrategy._clean_list(" topic:annotation ") == [
        "topic:annotation"
    ]
    assert LabelFirstAbstractStrategy._clean_list(["a", "A", "b"]) == ["a", "b"]


def test_label_first_abstract_strategy_falls_back_on_id_filter(
    monkeypatch, catalog: Catalog
) -> None:
    from chartcoach.retrieval.strategy.pipelines import label_first_abstract as mod

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        query="S",
        df=pl.DataFrame(
            {"id": ["g1", "g2"], "role": ["abstract", "abstract"], "score": [2.0, 1.0]}
        ),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    abstract_searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = LabelFirstAbstractStrategy(
        catalog=catalog,
        abstract_searcher=abstract_searcher,
        lm=lm,
        default_k=1,
        focus=FocusConfig(mode="violations"),
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            # Gate to g3 (not returned by fake index), forcing fallback to ids=None.
            return dspy.Prediction(
                canonical_query="S", label_hints=["impact:credibility"]
            )

    strat._program = DummyProgram()

    class DummyStatus:
        def classify_many(self, *, chart_key: str, situation: str, entries):  # noqa: ANN001
            _ = (chart_key, situation)
            return [{"id": e.id, "status": "violated"} for e in entries]

    monkeypatch.setattr(
        mod,
        "shared_status_scorer",
        lambda: ("lm", DummyStatus(), StatusScorerConfig(candidate_multiplier=2)),
    )

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert [e.id for e in out.catalog.entries] == ["g1"]
    assert out.meta["label_plan"]["candidate_filter_used"] is True


def test_label_gated_ann_strategy_retries_lm_and_uses_vision(
    monkeypatch, catalog: Catalog
) -> None:
    from chartcoach.retrieval.strategy.pipelines import label_gated_ann as mod

    monkeypatch.setenv("CHARTCOACH_CHART_VISION_ENABLED", "1")

    fake = _FakeLanceIndex()
    fake.set_dense(
        role="default",
        df=pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]}),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    monkeypatch.setattr(mod, "create_strategy_vlm", lambda: object())
    monkeypatch.setattr(
        mod,
        "with_chart_vision",
        lambda request, **_kwargs: (request, {"chart_vision_used": True}),
    )

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = LabelGatedAnnStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=1,
        focus=FocusConfig(mode="all"),
    )

    class FlakyProgram(dspy.Module):
        calls = 0

        def forward(self, **_kwargs):  # noqa: ANN003
            FlakyProgram.calls += 1
            if FlakyProgram.calls == 1:
                raise RuntimeError("boom")
            return dspy.Prediction(canonical_query="", label_hints=[])

    strat._program = FlakyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert out.meta["chart_vision"]["chart_vision_used"] is True
    assert out.meta["label_gating"]["lm_attempts"] == 2
    assert out.meta["label_gating"]["canonical_query"] == "S"


def test_label_first_abstract_strategy_retries_lm_and_uses_vision(
    monkeypatch, catalog: Catalog
) -> None:
    from chartcoach.retrieval.strategy.pipelines import label_first_abstract as mod

    monkeypatch.setenv("CHARTCOACH_CHART_VISION_ENABLED", "1")

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        query="S",
        df=pl.DataFrame({"id": ["g1"], "role": ["abstract"], "score": [2.0]}),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    abstract_searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    monkeypatch.setattr(mod, "create_strategy_vlm", lambda: object())
    monkeypatch.setattr(
        mod,
        "with_chart_vision",
        lambda request, **_kwargs: (request, {"chart_vision_used": True}),
    )

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = LabelFirstAbstractStrategy(
        catalog=catalog,
        abstract_searcher=abstract_searcher,
        lm=lm,
        default_k=1,
        focus=FocusConfig(mode="all"),
    )

    class FlakyProgram(dspy.Module):
        calls = 0

        def forward(self, **_kwargs):  # noqa: ANN003
            FlakyProgram.calls += 1
            if FlakyProgram.calls == 1:
                raise RuntimeError("boom")
            return dspy.Prediction(canonical_query="", label_hints=[])

    strat._program = FlakyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert out.meta["chart_vision"]["chart_vision_used"] is True
    assert out.meta["label_plan"]["lm_attempts"] == 2
    assert out.meta["label_plan"]["canonical_query"] == "S"


def test_decompose_parallel_strategy_runs_parallel_and_merges(
    monkeypatch, catalog: Catalog
) -> None:
    from chartcoach.retrieval.strategy.pipelines import decompose_parallel as mod

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        query="S",
        df=pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]}),
    )
    fake.set_hybrid(
        query="facet",
        df=pl.DataFrame({"id": ["g2"], "role": ["advice"], "score": [2.0]}),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = DecomposeParallelStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=2,
        focus=FocusConfig(mode="violations", allow_role_fallback=True),
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(
                canonical_query="S",
                facet_queries=["facet"],
                label_hints=["impact:credibility"],
            )

    strat._program = DummyProgram()

    class DummyStatus:
        def classify_many(self, *, chart_key: str, situation: str, entries):  # noqa: ANN001
            _ = (chart_key, situation)
            return [{"id": e.id, "status": "violated"} for e in entries]

    monkeypatch.setattr(
        mod,
        "shared_status_scorer",
        lambda: ("lm", DummyStatus(), StatusScorerConfig(candidate_multiplier=2)),
    )

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert [e.id for e in out.catalog.entries] == ["g1", "g2"]
    assert out.meta["decomposition"]["facet_queries"] == ["facet"]


def test_decompose_parallel_strategy_retries_lm_and_uses_fallback_canonical(
    monkeypatch, catalog: Catalog
) -> None:
    from chartcoach.retrieval.strategy.pipelines import decompose_parallel as mod

    monkeypatch.setenv("CHARTCOACH_CHART_VISION_ENABLED", "1")

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        query="S",
        df=pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]}),
    )
    fake.set_hybrid(
        query="facet",
        df=pl.DataFrame({"id": ["g2"], "role": ["advice"], "score": [2.0]}),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    monkeypatch.setattr(mod, "create_strategy_vlm", lambda: object())
    monkeypatch.setattr(
        mod,
        "with_chart_vision",
        lambda request, **_kwargs: (request, {"chart_vision_used": True}),
    )

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = DecomposeParallelStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=2,
        focus=FocusConfig(mode="violations", allow_role_fallback=True),
    )

    class FlakyProgram(dspy.Module):
        calls = 0

        def forward(self, **_kwargs):  # noqa: ANN003
            FlakyProgram.calls += 1
            if FlakyProgram.calls == 1:
                raise RuntimeError("boom")
            return dspy.Prediction(
                canonical_query="",
                facet_queries="facet",
                label_hints=["topic:annotation", "topic:annotation"],
            )

    strat._program = FlakyProgram()

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert out.meta["chart_vision"]["chart_vision_used"] is True
    assert out.meta["decomposition"]["canonical_query"] == "S"
    assert out.meta["decomposition"]["lm_attempts"] == 2


def test_decompose_parallel_strategy_includes_evidence_in_hits(
    monkeypatch, catalog: Catalog
) -> None:
    fake = _FakeLanceIndex()
    fake.set_hybrid(
        query="S",
        df=pl.DataFrame(
            {
                "id": ["g1", None],
                "role": ["advice", "advice"],
                "score": [2.0, 0.1],
                "text": ["axis title is missing", "ignored"],
            }
        ),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = DecomposeParallelStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=1,
        focus=FocusConfig(mode="all", allow_role_fallback=True),
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            return dspy.Prediction(
                canonical_query="S", facet_queries=[], label_hints=[]
            )

    strat._program = DummyProgram()

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert out.meta["hits"][0]["evidence"]


def test_role_aware_sections_strategy_routes_roles_and_falls_back(
    monkeypatch, catalog: Catalog
) -> None:
    from chartcoach.retrieval.strategy.pipelines import role_aware_sections as mod

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        query="S",
        df=pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]}),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = RoleAwareSectionsStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=1,
        focus=FocusConfig(mode="violations", allow_role_fallback=True),
    )

    class DummyProgram(dspy.Module):
        def forward(self, **_kwargs):  # noqa: ANN003
            # Force a role list that makes the fake index return empty, then rely on fallback.
            return dspy.Prediction(roles=["fix", "mistakes"])

    strat._program = DummyProgram()

    class DummyStatus:
        def classify_many(self, *, chart_key: str, situation: str, entries):  # noqa: ANN001
            _ = (chart_key, situation)
            return [{"id": e.id, "status": "violated"} for e in entries]

    monkeypatch.setattr(
        mod,
        "shared_status_scorer",
        lambda: ("lm", DummyStatus(), StatusScorerConfig(candidate_multiplier=2)),
    )

    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert [e.id for e in out.catalog.entries] == ["g1"]
    assert out.meta["role_router"]["roles"] == ["fix", "mistakes"]


def test_role_aware_sections_clean_roles_supports_string_and_dedupe() -> None:
    assert RoleAwareSectionsStrategy._clean_roles(" Advice ", max_roles=2) == ["advice"]
    assert RoleAwareSectionsStrategy._clean_roles(
        ["advice", "advice"], max_roles=2
    ) == ["advice"]


def test_role_aware_sections_strategy_retries_lm_and_uses_vision(
    monkeypatch, catalog: Catalog
) -> None:
    from chartcoach.retrieval.strategy.pipelines import role_aware_sections as mod

    monkeypatch.setenv("CHARTCOACH_CHART_VISION_ENABLED", "1")

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        query="S",
        df=pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]}),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    monkeypatch.setattr(mod, "create_strategy_vlm", lambda: object())
    monkeypatch.setattr(
        mod,
        "with_chart_vision",
        lambda request, **_kwargs: (request, {"chart_vision_used": True}),
    )

    lm = dspy.LM(model="gpt-4o-mini", api_base="http://example.invalid/v1", api_key="x")
    strat = RoleAwareSectionsStrategy(
        catalog=catalog,
        searcher=searcher,
        lm=lm,
        default_k=1,
        focus=FocusConfig(mode="all"),
    )

    class FlakyProgram(dspy.Module):
        calls = 0

        def forward(self, **_kwargs):  # noqa: ANN003
            FlakyProgram.calls += 1
            if FlakyProgram.calls == 1:
                raise RuntimeError("boom")
            return dspy.Prediction(roles="advice")

    strat._program = FlakyProgram()
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=1)
    )
    assert out.meta["chart_vision"]["chart_vision_used"] is True
    assert out.meta["role_router"]["lm_attempts"] == 2


def test_neighborhood_explorer_strategy_emits_diverse_neighbors(
    monkeypatch, catalog: Catalog
) -> None:
    from chartcoach.retrieval.strategy.pipelines import neighborhood_explorer as mod

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        query="S",
        df=pl.DataFrame({"id": ["g1"], "role": ["advice"], "score": [2.0]}),
    )
    fake.set_dense(
        role="default",
        df=pl.DataFrame(
            {
                "id": ["g1", "g2", "g3"],
                "role": ["advice", "advice", "advice"],
                "score": [3.0, 2.0, 1.0],
            }
        ),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    class DummyStatus:
        def classify_many(self, *, chart_key: str, situation: str, entries):  # noqa: ANN001
            _ = (chart_key, situation)
            return [{"id": e.id, "status": "violated"} for e in entries]

    monkeypatch.setattr(
        mod,
        "shared_status_scorer",
        lambda: ("lm", DummyStatus(), StatusScorerConfig(candidate_multiplier=2)),
    )

    strat = NeighborhoodExplorerStrategy(
        catalog=catalog,
        searcher=searcher,
        default_k=2,
        focus=FocusConfig(mode="violations", allow_role_fallback=True),
    )
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert len(out.catalog.entries) == 2
    assert out.meta["exploration"]["anchor_ids"] == ["g1"]


def test_neighborhood_explorer_strategy_includes_evidence_in_hits(
    monkeypatch, catalog: Catalog
) -> None:
    fake = _FakeLanceIndex()
    fake.set_hybrid(
        query="S",
        df=pl.DataFrame(
            {
                "id": ["g1", None],
                "role": ["advice", "advice"],
                "score": [2.0, 0.1],
                "text": ["axis title missing", "ignored"],
            }
        ),
    )
    fake.set_dense(
        role="default",
        df=pl.DataFrame(
            {
                "id": ["g2"],
                "role": ["advice"],
                "score": [1.0],
                "text": ["neighbor snippet"],
            }
        ),
    )
    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    strat = NeighborhoodExplorerStrategy(
        catalog=catalog,
        searcher=searcher,
        default_k=2,
        focus=FocusConfig(mode="all", allow_role_fallback=True),
    )
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert out.meta["hits"][0]["evidence"]


def test_neighborhood_explorer_seed_role_helper_branches(catalog: Catalog) -> None:
    from chartcoach.retrieval.strategy.pipelines import neighborhood_explorer as mod

    g1 = catalog.entries[0]
    # Violations prefers exceptions when present.
    assert mod._seed_role_for_focus(g1, "violations") == "exceptions"
    # Satisfied prefers check/reason/context, falling back to advice/check.
    assert mod._seed_role_for_focus(g1, "satisfied") in {"check", "context", "advice"}
    # Default focus uses advice.
    assert mod._seed_role_for_focus(g1, "all") == "advice"

    # Empty guidelines hit the default return branches.
    empty = CatalogEntry(
        guideline=Guideline(id="gx", title="t", description="d", labels=[], body=""),
        references=[],
    )
    assert mod._seed_role_for_focus(empty, "violations") == "advice"
    assert mod._seed_role_for_focus(empty, "satisfied") == "check"


def test_neighborhood_explorer_strategy_hits_continue_branches(monkeypatch) -> None:
    from chartcoach.retrieval.strategy.pipelines import neighborhood_explorer as mod
    from chartcoach.catalog.model import CatalogEntry, Guideline as GuidelineModel

    # Build a catalog where one anchor is missing advice (to hit `continue`),
    # and one candidate is missing advice (to hit the advice-skip branch).
    catalog = Catalog(
        entries=[
            CatalogEntry(
                guideline=GuidelineModel(
                    id="g1",
                    title="T1",
                    description="D1",
                    labels=["x"],
                    body=(
                        "## Advice <!-- role: advice -->\nA1\n\n"
                        "## Context <!-- role: context -->\nC1\n\n"
                        "## Exceptions <!-- role: exceptions -->\nE1\n"
                    ),
                ),
                references=[],
            ),
            CatalogEntry(
                guideline=GuidelineModel(
                    id="g2",
                    title="T2",
                    description="D2",
                    labels=["x"],
                    body="## Context <!-- role: context -->\nC2\n",
                ),
                references=[],
            ),
        ]
    )

    monkeypatch.setenv("CHARTCOACH_CHART_VISION_ENABLED", "1")

    fake = _FakeLanceIndex()
    fake.set_hybrid(
        query="S",
        df=pl.DataFrame(
            {
                "id": ["g1", "g2"],
                "role": ["advice", "advice"],
                "score": [2.0, 1.0],
            }
        ),
    )
    # Dense calls (for context / seed roles) include a ghost id (missing entry)
    # and g2 (missing advice) to exercise skips.
    fake.set_dense(
        role="default",
        df=pl.DataFrame(
            {
                "id": ["ghost", "g2"],
                "role": ["context", "context"],
                "score": [2.0, 1.0],
            }
        ),
    )

    vector_index = _make_vector_index(catalog=catalog, fake=fake)
    monkeypatch.setattr(
        CatalogVectorIndex, "embed_query", lambda _self, _t: np.array([1.0, 0.0])
    )
    searcher = GuidelineSearcher(catalog=catalog, vector_index=vector_index)

    monkeypatch.setattr(mod, "create_strategy_vlm", lambda: object())
    monkeypatch.setattr(
        mod,
        "with_chart_vision",
        lambda request, **_kwargs: (request, {"chart_vision_used": True}),
    )
    monkeypatch.setattr(
        mod,
        "shared_status_scorer",
        lambda: ("lm", object(), StatusScorerConfig(candidate_multiplier=2)),
    )
    monkeypatch.setattr(
        mod,
        "filter_guidelines_by_status",
        lambda *, entries, output_k, **_kwargs: (
            entries[:output_k],
            {"guideline_status_used": True},
        ),
    )

    strat = NeighborhoodExplorerStrategy(
        catalog=catalog,
        searcher=searcher,
        default_k=2,
        focus=FocusConfig(mode="violations", allow_role_fallback=True),
    )
    out = strat(
        request=RetrievalRequest(context=[TextItem(role="situation", text="S")], k=2)
    )
    assert out.meta["chart_vision"]["chart_vision_used"] is True
