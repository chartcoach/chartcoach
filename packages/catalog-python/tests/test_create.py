from __future__ import annotations

import pytest

import chartcoach as cc
from chartcoach.create import create


def test_create_requires_explicit_catalog(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CHARTCOACH_CATALOG_PATH", raising=False)

    with pytest.raises(ValueError, match="create\\(catalog=\\.\\.\\.\\)"):
        create()


def test_create_is_available_from_package_root() -> None:
    assert cc.create is create
