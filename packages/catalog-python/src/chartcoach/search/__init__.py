from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .guidelines import GuidelineSearchHit, GuidelineSearchResult, search_guidelines
    from .lance import CacheMode, LanceIndex

__all__ = [
    "CacheMode",
    "GuidelineSearchHit",
    "GuidelineSearchResult",
    "LanceIndex",
    "search_guidelines",
]

_LAZY_EXPORTS = {
    "CacheMode": (".lance", "CacheMode"),
    "LanceIndex": (".lance", "LanceIndex"),
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
