from __future__ import annotations

from chartcoach.catalog.model import CatalogEntry, Guideline
from chartcoach.retrieval.operators import apply_status_filter, plan_status_filter
from chartcoach.retrieval.strategy.pipelines.guideline_status import (
    StatusScorer,
    StatusScorerConfig,
)
from chartcoach.retrieval.strategy.types import RetrievalRequest, TextItem


class _FakeStatusModule:
    def classify_many(  # noqa: D401
        self, *, chart_key: str, situation: str, entries: list[CatalogEntry]
    ) -> list[dict[str, object]]:
        _ = (chart_key, situation)
        out: list[dict[str, object]] = []
        for entry in entries:
            status = "unclear"
            if entry.id == "g1":
                status = "violated"
            elif entry.id == "g2":
                status = "satisfied"
            out.append({"id": entry.id, "status": status, "confidence": 1.0})
        return out


def _entries() -> list[CatalogEntry]:
    return [
        CatalogEntry(
            guideline=Guideline(
                id="g1",
                title="A",
                description="A",
                labels=[],
                body="",
            ),
            references=[],
        ),
        CatalogEntry(
            guideline=Guideline(
                id="g2",
                title="B",
                description="B",
                labels=[],
                body="",
            ),
            references=[],
        ),
        CatalogEntry(
            guideline=Guideline(
                id="g3",
                title="C",
                description="C",
                labels=[],
                body="",
            ),
            references=[],
        ),
    ]


def test_plan_status_filter_disables_when_focus_all() -> None:
    plan = plan_status_filter(
        focus_mode="all",
        requested_k=10,
        status_scorer=None,
        status_filter_enabled=True,
    )
    assert plan.use_status_filter is False
    assert plan.candidate_k == 10


def test_plan_status_filter_uses_candidate_multiplier() -> None:
    scorer = StatusScorer(
        lm=None,  # type: ignore[arg-type]
        module=_FakeStatusModule(),  # type: ignore[arg-type]
        config=StatusScorerConfig(candidate_multiplier=4),
    )
    plan = plan_status_filter(
        focus_mode="violations",
        requested_k=10,
        status_scorer=scorer,
        status_filter_enabled=True,
    )
    assert plan.use_status_filter is True
    assert plan.candidate_k == 40


def test_apply_status_filter_prioritizes_focus_mode() -> None:
    scorer = StatusScorer(
        lm=None,  # type: ignore[arg-type]
        module=_FakeStatusModule(),  # type: ignore[arg-type]
        config=StatusScorerConfig(keep_unclear=True),
    )
    request = RetrievalRequest(
        context=[
            TextItem(role="intent", text="Designer intent."),
        ]
    )
    selected, meta = apply_status_filter(
        request=request,
        entries=_entries(),
        output_k=2,
        focus_mode="violations",
        status_scorer=scorer,
    )
    assert [e.id for e in selected] == ["g1", "g3"]
    assert meta["guideline_status_focus"] == "violations"
    assert meta["guideline_status_used"] is True
