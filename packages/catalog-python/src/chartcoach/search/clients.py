from __future__ import annotations

import logging
import pathlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from chromadb.api import ClientAPI
else:
    ClientAPI = object

logger = logging.getLogger(__name__)


def _missing_search_extra_error() -> ModuleNotFoundError:
    return ModuleNotFoundError(
        "Chroma-backed search requires the optional `chartcoach[search]` dependencies."
    )


def create_chroma_client(
    path: str | pathlib.Path,
) -> ClientAPI:
    """Create a persistent Chroma client at the given path."""
    try:
        import chromadb
    except ModuleNotFoundError as exc:
        raise _missing_search_extra_error() from exc

    chroma_path = pathlib.Path(path)
    logger.debug("Opening Chroma persistent client at %s", chroma_path)
    return chromadb.PersistentClient(chroma_path)


__all__ = ["create_chroma_client"]
