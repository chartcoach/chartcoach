from .clients import create_chroma_client
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .chroma import CacheMode, ChromaIndex, ChromaIndexPaths
    from .guidelines import GuidelineSearchHit, GuidelineSearchResult, search_guidelines

__all__ = [
    "CacheMode",
    "GuidelineSearchHit",
    "GuidelineSearchResult",
    "ChromaIndex",
    "ChromaIndexPaths",
    "create_chroma_client",
    "search_guidelines",
]

_LAZY_EXPORTS = {
    "CacheMode": (".chroma", "CacheMode"),
    "ChromaIndex": (".chroma", "ChromaIndex"),
    "ChromaIndexPaths": (".chroma", "ChromaIndexPaths"),
    "GuidelineSearchHit": (".guidelines", "GuidelineSearchHit"),
    "GuidelineSearchResult": (".guidelines", "GuidelineSearchResult"),
    "search_guidelines": (".guidelines", "search_guidelines"),
}


def __getattr__(name: str) -> object:
    if name not in _LAZY_EXPORTS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib import import_module

    module_name, attr_name = _LAZY_EXPORTS[name]
    value = getattr(import_module(module_name, __name__), attr_name)
    globals()[name] = value
    return value
