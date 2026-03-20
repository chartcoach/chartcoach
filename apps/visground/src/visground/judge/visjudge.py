from __future__ import annotations

import base64
import json
import weakref
from collections.abc import Sequence
from io import BytesIO
from os import PathLike
from pathlib import Path
from typing import TypedDict, cast

import httpx
import platformdirs
from diskcache import Cache
from PIL import Image


class VisJudgeRequest(TypedDict):
    """Input for one VisJudge call."""

    image: Image.Image
    prompt: str


class _RunResponse(TypedDict):
    result: str


class _RunManyResponse(TypedDict):
    results: list[str]


def _default_cache_dir() -> Path:
    return Path(platformdirs.user_cache_dir("visground")) / "visjudge"


def _close_resources(client: httpx.Client, cache: Cache) -> None:
    cache.close()
    client.close()


class VisJudgeClient:
    """Thin client for the VisJudge HTTP API."""

    def __init__(
        self,
        base_url: str = "http://localhost:8000",
        timeout: float | httpx.Timeout = 120.0,
        cache_dir: str | PathLike[str] | None = None,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)
        self._cache = Cache(cache_dir or _default_cache_dir())
        self._base_url = str(self._client.base_url)
        self._finalizer = weakref.finalize(
            self,
            _close_resources,
            self._client,
            self._cache,
        )

    def run(self, request: VisJudgeRequest) -> str:
        """Run VisJudge on one input."""
        payload = self._dump(request)
        key = self._cache_key(payload)
        if (result := self._cache_get(key)) is not None:
            return result

        response = self._client.post("run", json=payload)
        response.raise_for_status()
        result = self._load_one(self._json(response))
        self._cache_put(key, result)
        return result

    def run_many(self, requests: Sequence[VisJudgeRequest]) -> list[str]:
        """Run VisJudge on many inputs."""
        items = list(requests)
        if not items:
            raise ValueError("requests must not be empty.")

        payloads = [self._dump(request) for request in items]
        keys = [self._cache_key(payload) for payload in payloads]
        results = [self._cache_get(key) for key in keys]
        miss_indices = [index for index, result in enumerate(results) if result is None]

        if miss_indices:
            response = self._client.post(
                "run-many",
                json={"inputs": [payloads[index] for index in miss_indices]},
            )
            response.raise_for_status()
            fresh_results = self._load_many(self._json(response))
            if len(fresh_results) != len(miss_indices):
                raise ValueError(
                    "VisJudge returned the wrong number of /run-many results."
                )

            for index, result in zip(miss_indices, fresh_results):
                self._cache_put(keys[index], result)
                results[index] = result

        output: list[str] = []
        for result in results:
            if result is None:
                raise ValueError("VisJudge did not produce a result for every input.")
            output.append(result)
        return output

    def _encode(self, image: Image.Image) -> str:
        buf = BytesIO()
        image.save(buf, format="PNG")
        return base64.b64encode(buf.getvalue()).decode("ascii")

    def _dump(self, request: VisJudgeRequest) -> dict[str, str]:
        return {
            "image_base64": self._encode(request["image"]),
            "prompt": request["prompt"],
        }

    def _cache_get(self, key: str) -> str | None:
        value = self._cache.get(key)
        return value if isinstance(value, str) else None

    def _cache_put(self, key: str, value: str) -> None:
        self._cache.set(key, value)

    def _cache_key(self, payload: dict[str, str]) -> str:
        return json.dumps(
            {
                "ns": "visjudge.v1",
                "base_url": self._base_url,
                "request": payload,
            },
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        )

    def _json(self, response: httpx.Response) -> object:
        try:
            return response.json()
        except ValueError as exc:
            raise ValueError("VisJudge returned invalid JSON.") from exc

    def _load_one(self, data: object) -> str:
        if not isinstance(data, dict) or set(data) != {"result"}:
            raise ValueError("VisJudge returned an invalid /run response.")

        result = cast(_RunResponse, data)["result"]
        if not isinstance(result, str):
            raise ValueError("VisJudge returned an invalid /run response.")
        return result

    def _load_many(self, data: object) -> list[str]:
        if not isinstance(data, dict) or set(data) != {"results"}:
            raise ValueError("VisJudge returned an invalid /run-many response.")

        results = cast(_RunManyResponse, data)["results"]
        if not isinstance(results, list) or not all(
            isinstance(result, str) for result in results
        ):
            raise ValueError("VisJudge returned an invalid /run-many response.")
        return results


__all__ = ["VisJudgeClient", "VisJudgeRequest"]
