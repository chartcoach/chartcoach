from .clients import create_chroma_client
from .sql import connect_catalog, register_catalog

__all__ = [
    "CacheMode",
    "ChromaIndex",
    "SearchSession",
    "SearchTools",
    "connect_catalog",
    "create_chroma_client",
    "open_search_session",
    "register_catalog",
]

_LAZY_EXPORTS = {
    "CacheMode": (".chroma", "CacheMode"),
    "ChromaIndex": (".chroma", "ChromaIndex"),
    "SearchSession": (".session", "SearchSession"),
    "SearchTools": (".tools", "SearchTools"),
    "open_search_session": (".session", "open_search_session"),
}


def __getattr__(name: str) -> object:
    if name not in _LAZY_EXPORTS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib import import_module

    module_name, attr_name = _LAZY_EXPORTS[name]
    value = getattr(import_module(module_name, __name__), attr_name)
    globals()[name] = value
    return value
