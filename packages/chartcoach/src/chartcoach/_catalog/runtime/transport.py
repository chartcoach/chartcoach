from __future__ import annotations

from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any, Literal, cast
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen

from .._object_store import obstore_uri
from ..errors import CatalogError, CatalogOperationError, CatalogValidationError
from .location import uri_name, uri_parent

_READ_CHUNK_BYTES = 1024 * 1024


def read_local_bytes(path: Path, limit: int) -> bytes:
    try:
        size = path.stat().st_size
        if size > limit:
            raise CatalogError("Catalog JSON exceeds the 1 MiB limit.")
        with path.open("rb") as source:
            data = source.read(limit + 1)
    except OSError as exc:
        raise CatalogOperationError(
            f"Could not read catalog location: {path}",
            details={"operation": "read_local"},
            hints=["Check that the catalog file exists and is readable."],
        ) from exc
    if len(data) > limit:
        raise CatalogError("Catalog JSON exceeds the 1 MiB limit.")
    return data


def read_remote_bytes(
    uri: str,
    *,
    transport: Literal["http", "cloud"],
    storage_options: Mapping[str, object],
    limit: int,
    no_cache: bool = False,
) -> bytes:
    data = bytearray()
    for chunk in remote_chunks(
        uri,
        transport=transport,
        storage_options=storage_options,
        no_cache=no_cache,
    ):
        view = memoryview(chunk)
        if len(data) + view.nbytes > limit:
            raise CatalogError("Catalog JSON exceeds the 1 MiB limit.")
        data.extend(view)
    return bytes(data)


def remote_chunks(
    uri: str,
    *,
    transport: Literal["http", "cloud"],
    storage_options: Mapping[str, object],
    no_cache: bool = False,
) -> Iterable[bytes | bytearray | memoryview]:
    if transport == "cloud":
        yield from _cloud_chunks(uri, storage_options)
        return

    headers, timeout = _http_options(storage_options)
    if no_cache:
        headers["Cache-Control"] = "no-cache"
    try:
        request = Request(uri, headers=headers)
        with urlopen(request, timeout=timeout) as response:
            while chunk := response.read(_READ_CHUNK_BYTES):
                yield chunk
    except ValueError as exc:
        raise CatalogValidationError(
            "Could not construct the catalog HTTP request.",
            hints=["Check the catalog URL and HTTP storage options."],
        ) from exc
    except OSError as exc:
        raise CatalogOperationError(
            f"Failed to load catalog resource over HTTP: {_display_http_uri(uri)}",
            details={"operation": "read_http"},
            hints=[
                "Pass a local catalog or release path as `location` for offline work.",
                "The CLI accepts `--source PATH` or `CHARTCOACH_SOURCE=PATH`.",
            ],
        ) from exc


def _display_http_uri(uri: str) -> str:
    parsed = urlsplit(uri)
    netloc = parsed.netloc.rsplit("@", 1)[-1]
    return urlunsplit((parsed.scheme, netloc, parsed.path, "", ""))


def _cloud_chunks(
    uri: str,
    storage_options: Mapping[str, object],
) -> Iterable[bytes | bytearray | memoryview]:
    try:
        from obstore.store import from_url
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "Cloud catalog locations require the optional `chartcoach[cloud]` "
            "dependencies.",
            name=exc.name,
        ) from exc

    try:
        store_factory = cast(Any, from_url)
        store = store_factory(
            obstore_uri(uri_parent(uri)),
            **dict(storage_options),
        )
    except (TypeError, ValueError) as exc:
        raise CatalogValidationError(
            "Could not configure the catalog cloud storage client.",
            hints=["Check the catalog URI and storage client options."],
        ) from exc
    except Exception as exc:
        raise CatalogOperationError(
            "Could not open catalog cloud storage.",
            details={"operation": "open_cloud"},
            hints=[
                "Check the storage client's configuration and access to the bucket."
            ],
        ) from exc
    try:
        yield from store.get(uri_name(uri))
    except Exception as exc:
        raise CatalogOperationError(
            "Failed to load catalog resource from cloud storage.",
            details={"operation": "read_cloud"},
            hints=[
                "Check that the catalog object exists and the storage client can read it."
            ],
        ) from exc


def _http_options(
    storage_options: Mapping[str, object],
) -> tuple[dict[str, str], float]:
    options = dict(storage_options)
    unsupported = set(options) - {"headers", "timeout"}
    if unsupported:
        names = ", ".join(sorted(unsupported))
        raise CatalogError(f"Unsupported HTTP storage options: {names}.")

    raw_headers = options.get("headers", {})
    if not isinstance(raw_headers, Mapping) or not all(
        isinstance(key, str) and isinstance(value, str)
        for key, value in raw_headers.items()
    ):
        raise CatalogError("HTTP storage option headers must map strings to strings.")
    raw_timeout = options.get("timeout", 900.0)
    if isinstance(raw_timeout, bool) or not isinstance(raw_timeout, int | float):
        raise CatalogError("HTTP storage option timeout must be a positive number.")
    timeout = float(raw_timeout)
    if timeout <= 0:
        raise CatalogError("HTTP storage option timeout must be a positive number.")
    headers = {"User-Agent": "chartcoach"}
    headers.update(
        {cast(str, key): cast(str, value) for key, value in raw_headers.items()}
    )
    return headers, timeout


__all__ = ["read_local_bytes", "read_remote_bytes", "remote_chunks"]
