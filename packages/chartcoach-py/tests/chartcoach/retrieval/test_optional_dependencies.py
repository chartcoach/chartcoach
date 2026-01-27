from __future__ import annotations

import builtins
import types

import pytest


def test_strategy_package_exports_dspy_symbols_when_installed() -> None:
    import chartcoach.retrieval.strategy as strategy

    assert hasattr(strategy, "RetrievalStrategy")


def test_require_dspy_returns_module() -> None:
    from chartcoach.retrieval.strategy.optional import require_dspy

    module = require_dspy()
    assert isinstance(module, types.ModuleType)
    assert module.__name__ == "dspy"


def test_require_dspy_raises_helpful_error_when_missing(monkeypatch) -> None:
    from chartcoach.retrieval.strategy import optional

    original_import = builtins.__import__

    def fake_import(name: str, globals=None, locals=None, fromlist=(), level=0):  # noqa: ANN001
        if name == "dspy":
            raise ModuleNotFoundError("No module named 'dspy'", name="dspy")
        return original_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, "__import__", fake_import)

    with pytest.raises(RuntimeError, match=r"chartcoach\[retrieval\]"):
        optional.require_dspy()


def test_require_dspy_reraises_import_error_for_subdependency(monkeypatch) -> None:
    from chartcoach.retrieval.strategy import optional

    original_import = builtins.__import__

    def fake_import(name: str, globals=None, locals=None, fromlist=(), level=0):  # noqa: ANN001
        if name == "dspy":
            raise ModuleNotFoundError("No module named 'some_dep'", name="some_dep")
        return original_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, "__import__", fake_import)

    with pytest.raises(ModuleNotFoundError, match=r"some_dep"):
        optional.require_dspy()
