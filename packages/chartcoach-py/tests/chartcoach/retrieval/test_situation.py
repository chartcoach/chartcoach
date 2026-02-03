from __future__ import annotations

import pytest

from chartcoach.retrieval.situation import (
    Situation,
    iter_context_roles,
    situation_text_parts,
)
from chartcoach.retrieval.strategy.types import ImageItem, RetrievalRequest, TextItem


def test_situation_from_request_requires_intent() -> None:
    with pytest.raises(ValueError, match="intent"):
        Situation.from_request(RetrievalRequest(context=[]))


def test_situation_from_request_accepts_legacy_situation_role() -> None:
    req = RetrievalRequest(context=[TextItem(role="situation", text="S")])
    situation = Situation.from_request(req)
    assert situation.intent == "S"


def test_situation_query_text_includes_facets_and_vision() -> None:
    req = RetrievalRequest(
        context=[
            TextItem(role="title", text="T"),
            TextItem(role="intent", text="I"),
            TextItem(role="audience", text="general news readers"),
            TextItem(role="medium", text="online"),
            TextItem(role="constraints", text="static"),
            TextItem(role="chart_vision", text="notes"),
            TextItem(role="query", text="meta"),
            TextItem(role="chart_spec", text="{}"),
            ImageItem(role="chart", uri="https://example.invalid/x.png"),
        ],
        lang="en",
    )
    situation = Situation.from_request(req)
    assert situation.title == "T"
    assert situation.intent == "I"
    assert situation.query_meta == "meta"
    assert situation.artifact.chart_spec == "{}"
    assert situation.artifact.chart_vision == "notes"
    assert situation.artifact.chart_image is not None
    assert situation.context["audience"] == "general news readers"

    text = situation.to_query_text(include_chart_vision=True)
    assert text.startswith("T")
    assert "\n\nI" in text
    assert "Context:" in text
    assert "Audience: general news readers" in text
    assert "Medium: online" in text
    assert "Constraints: static" in text
    assert "Chart image notes:" in text
    assert "notes" in text

    base = situation.to_query_text(include_chart_vision=False)
    assert "Chart image notes:" not in base


def test_situation_text_parts_wrapper() -> None:
    req = RetrievalRequest(
        context=[
            TextItem(role="intent", text="I"),
            TextItem(role="chart_vision", text="V"),
        ]
    )
    parts = situation_text_parts(req)
    assert "Chart image notes:" not in parts.base
    assert "Chart image notes:" in parts.with_chart_vision


def test_iter_context_roles_is_stable() -> None:
    roles = list(iter_context_roles())
    assert "audience" in roles
    assert "constraints" in roles
