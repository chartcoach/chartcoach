from __future__ import annotations

from chartcoach.utils.text import fence, string_hash, unfence


def test_fence_unfence_roundtrip() -> None:
    original = "hello\nworld"
    fenced = fence(original, lang="txt")
    assert "```txt" in fenced
    assert unfence(fenced) == [original]


def test_string_hash_is_stable_and_hex() -> None:
    h1 = string_hash("abc")
    h2 = string_hash("abc")
    assert h1 == h2
    assert len(h1) == 64
    int(h1, 16)
