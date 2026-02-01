from __future__ import annotations

from chartcoach.retrieval.strategy.id_extraction import extract_guideline_ids


def test_extract_guideline_ids_accepts_single_dict_payload() -> None:
    known = {"g1"}
    out = extract_guideline_ids(known_ids=known, raw_used={"id": "g1"})
    assert out == ["g1"]
