from __future__ import annotations

import json
from collections.abc import Iterable
from typing import Any

import obstore
from obstore.store import ObjectStore


def read_json(store: ObjectStore, path: str) -> dict[str, Any] | None:
    try:
        result = obstore.get(store, path)
    except FileNotFoundError:
        return None

    raw = bytes(result.bytes()).decode("utf-8")
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ValueError(f"Expected JSON object at {path!r}.")
    return value


def write_json(store: ObjectStore, path: str, value: dict[str, Any]) -> None:
    data = json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")
    obstore.put(store, path, data)


def list_paths(store: ObjectStore, *, prefix: str) -> list[str]:
    items = obstore.list(store, prefix=prefix).collect()
    return [item["path"] for item in items if isinstance(item.get("path"), str)]


def delete_paths(store: ObjectStore, paths: Iterable[str]) -> None:
    normalized = [p for p in paths if p]
    if not normalized:
        return
    obstore.delete(store, normalized)
