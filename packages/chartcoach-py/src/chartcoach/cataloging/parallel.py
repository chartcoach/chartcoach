from __future__ import annotations

import json
from collections.abc import Callable, Iterable
from typing import ParamSpec, TypeVar

import diskcache
from joblib import Parallel, delayed
from tenacity import retry, stop_after_attempt, wait_fixed
from tqdm.auto import tqdm


T = TypeVar("T")
R = TypeVar("R")
P = ParamSpec("P")


def parallel_map(
    fn: Callable[[T], R],
    inputs: Iterable[T],
    *,
    n_jobs: int = -1,
    backend: str = "threading",
    desc: str | None = None,
    cache_dir: str | None = ".cache",
    cache_key_provider: Callable[[T], str] | None = None,
) -> list[R]:
    inputs_list = list(inputs)
    cache = diskcache.Cache(cache_dir) if cache_dir else None

    with tqdm(total=len(inputs_list), desc=desc) as pbar:

        @retry(wait=wait_fixed(1), stop=stop_after_attempt(3), reraise=True)
        def _wrapper(inp: T) -> R:
            cache_key: str | None = None
            if cache is not None:
                cache_key = (
                    json.dumps(inp, sort_keys=True, default=str)
                    if cache_key_provider is None
                    else cache_key_provider(inp)
                )
                cached = cache.get(cache_key)
                if cached is not None:
                    pbar.update(1)
                    return cached

            result = fn(inp)

            if cache is not None and cache_key is not None:
                cache.set(cache_key, result)

            pbar.update(1)
            return result

        return list(
            Parallel(n_jobs=n_jobs, backend=backend, return_as="generator")(
                delayed(_wrapper)(inp) for inp in inputs_list
            )
        )


def param_collapsed(fn: Callable[P, R]) -> Callable[[dict], R]:
    def wrapped(item: dict) -> R:
        return fn(**item)

    return wrapped
