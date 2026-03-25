from __future__ import annotations

import base64
import json
import weakref
from collections.abc import Sequence
from io import BytesIO
from os import PathLike
from pathlib import Path
from typing import Protocol, TypedDict, cast, runtime_checkable

import dspy
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


def _close_cache(cache: Cache) -> None:
    cache.close()


def _close_resources(client: httpx.Client, cache: Cache) -> None:
    cache.close()
    client.close()


def _encode_image(image: Image.Image) -> str:
    buf = BytesIO()
    image.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("ascii")


def _dump_request(request: VisJudgeRequest) -> dict[str, str]:
    return {
        "image_base64": _encode_image(request["image"]),
        "prompt": request["prompt"],
    }


def _is_secret_config_key(key: str) -> bool:
    normalized = key.lower()
    return (
        normalized in {"api_key", "authorization"}
        or normalized.endswith("_key")
        or normalized.endswith("_token")
        or "secret" in normalized
        or "password" in normalized
        or "authorization" in normalized
    )


def _sanitize_for_cache(value: object) -> object:
    if isinstance(value, dict):
        return {
            str(key): _sanitize_for_cache(item)
            for key, item in value.items()
            if not isinstance(key, str) or not _is_secret_config_key(key)
        }
    if isinstance(value, (list, tuple)):
        return [_sanitize_for_cache(item) for item in value]
    return value


def _validate_run_many_args(
    requests: Sequence[VisJudgeRequest],
    batch_size: int,
) -> list[VisJudgeRequest]:
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1.")

    items = list(requests)
    if not items:
        raise ValueError("requests must not be empty.")
    return items


@runtime_checkable
class VisJudgeClient(Protocol):
    def run(self, request: VisJudgeRequest) -> str: ...

    def run_many(
        self,
        requests: Sequence[VisJudgeRequest],
        batch_size: int = 16,
    ) -> list[str]: ...


class VisJudgeApiClient(VisJudgeClient):
    """Thin client for the VisJudge HTTP API."""

    def __init__(
        self,
        base_url: str = "http://localhost:8000",
        timeout: float | httpx.Timeout = 600,
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
        payload = _dump_request(request)
        key = self._cache_key(payload)
        if (result := self._cache_get(key)) is not None:
            return result

        response = self._client.post("run", json=payload)
        response.raise_for_status()
        result = self._load_one(self._json(response))
        self._cache_put(key, result)
        return result

    def run_many(
        self,
        requests: Sequence[VisJudgeRequest],
        batch_size: int = 16,
    ) -> list[str]:
        """Run VisJudge on many inputs in serial batches."""
        items = _validate_run_many_args(requests, batch_size)
        results = []
        for start in range(0, len(items), batch_size):
            batch = items[start : start + batch_size]
            results.extend(self._run_many(batch))
        return results

    def _run_many(self, requests: Sequence[VisJudgeRequest]) -> list[str]:
        """Run VisJudge on many inputs."""
        items = list(requests)
        if not items:
            raise ValueError("requests must not be empty.")

        payloads = [_dump_request(request) for request in items]
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


class _VisJudgeLmSignature(dspy.Signature):
    prompt: str = dspy.InputField(desc="Instruction for judging the image")
    image: dspy.Image = dspy.InputField(desc="The visualization image to be judged")
    judgement: dict = dspy.OutputField(
        desc="Response in the exact format prescribed in the prompt"
    )


class VisJudgeLmClient(VisJudgeClient):
    def __init__(
        self,
        lm: dspy.LM,
        cache_dir: str | PathLike[str] | None = None,
    ) -> None:
        self._lm = lm
        self._cache = Cache(cache_dir or _default_cache_dir())
        self._predict = dspy.Predict(_VisJudgeLmSignature)
        self._finalizer = weakref.finalize(
            self,
            _close_cache,
            self._cache,
        )

    def run(self, request: VisJudgeRequest) -> str:
        payload = _dump_request(request)
        key = self._cache_key(payload)
        if (result := self._cache_get(key)) is not None:
            return result

        with dspy.context(lm=self._lm):
            result = self._predict(
                prompt=request["prompt"],
                image=request["image"],
            )

        normalized = self._load_result(result, index=0)
        self._cache_put(key, normalized)
        return normalized

    def run_many(
        self,
        requests: Sequence[VisJudgeRequest],
        batch_size: int = 16,
    ) -> list[str]:
        items = _validate_run_many_args(requests, batch_size)
        results = []
        for start in range(0, len(items), batch_size):
            batch = items[start : start + batch_size]
            results.extend(self._run_many(batch, start_index=start))
        return results

    def _run_many(
        self,
        requests: Sequence[VisJudgeRequest],
        *,
        start_index: int = 0,
    ) -> list[str]:
        items = list(requests)
        if not items:
            raise ValueError("requests must not be empty.")

        payloads = [_dump_request(request) for request in items]
        keys = [self._cache_key(payload) for payload in payloads]
        results = [self._cache_get(key) for key in keys]
        miss_indices = [index for index, result in enumerate(results) if result is None]

        if miss_indices:
            parallel = dspy.Parallel(
                num_threads=len(miss_indices),
                max_errors=1,
                disable_progress_bar=True,
            )
            inputs = [
                (
                    self._predict,
                    {
                        "prompt": items[index]["prompt"],
                        "image": dspy.Image.from_PIL(items[index]["image"]),
                    },
                )
                for index in miss_indices
            ]

            try:
                with dspy.context(lm=self._lm):
                    raw_results = parallel(inputs)
            except Exception as exc:
                raise RuntimeError("VisJudge LM parallel execution failed.") from exc

            if len(raw_results) != len(miss_indices):
                raise ValueError("VisJudge LM returned the wrong number of results.")

            normalized_results: list[tuple[int, str]] = []
            for index, raw_result in zip(miss_indices, raw_results):
                normalized_results.append(
                    (
                        index,
                        self._load_result(raw_result, index=start_index + index),
                    )
                )

            for index, normalized in normalized_results:
                self._cache_put(keys[index], normalized)
                results[index] = normalized

        output: list[str] = []
        for result in results:
            if result is None:
                raise ValueError(
                    "VisJudge LM did not produce a result for every input."
                )
            output.append(result)
        return output

    def _load_result(self, result: object, *, index: int) -> str:
        judgement = getattr(result, "judgement", None)
        if not isinstance(judgement, dict):
            raise ValueError(
                f"VisJudge LM returned an invalid result at index {index}."
            )
        try:
            return json.dumps(judgement)
        except TypeError as exc:
            raise ValueError(
                f"VisJudge LM returned a non-serializable result at index {index}."
            ) from exc

    def _cache_get(self, key: str) -> str | None:
        value = self._cache.get(key)
        return value if isinstance(value, str) else None

    def _cache_put(self, key: str, value: str) -> None:
        self._cache.set(key, value)

    def _cache_key(self, payload: dict[str, str]) -> str:
        return json.dumps(
            {
                "ns": "visjudge.lm.v1",
                "lm": {
                    "model": self._lm.model,
                    "model_type": self._lm.model_type,
                    "finetuning_model": self._lm.finetuning_model,
                    "use_developer_role": self._lm.use_developer_role,
                    "kwargs": _sanitize_for_cache(self._lm.kwargs),
                },
                "request": payload,
            },
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
            default=str,
        )


__all__ = [
    "VisJudgeApiClient",
    "VisJudgeClient",
    "VisJudgeLmClient",
    "VisJudgeRequest",
]
