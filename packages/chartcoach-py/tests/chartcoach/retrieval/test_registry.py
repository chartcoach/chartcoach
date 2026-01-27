from __future__ import annotations


def test_configure_dspy_cache_is_idempotent(monkeypatch) -> None:
    import dspy
    from chartcoach.retrieval.service import retrieval_service

    calls: list[dict[str, object]] = []
    monkeypatch.setattr(dspy, "configure_cache", lambda **kwargs: calls.append(kwargs))

    monkeypatch.setattr(retrieval_service, "_CACHE_CONFIGURED", True)
    retrieval_service.configure_dspy_cache()
    assert calls == []


def test_configure_dspy_cache_calls_once(monkeypatch) -> None:
    import dspy
    from chartcoach.retrieval.service import retrieval_service

    calls: list[dict[str, object]] = []
    monkeypatch.setattr(dspy, "configure_cache", lambda **kwargs: calls.append(kwargs))
    monkeypatch.setattr(retrieval_service, "_CACHE_CONFIGURED", False)

    retrieval_service.configure_dspy_cache()
    assert calls == [
        {"enable_disk_cache": True, "enable_memory_cache": True},
    ]
    assert retrieval_service._CACHE_CONFIGURED is True
