from __future__ import annotations

import warnings


CURATION_EXTRA = "chartcoach[curation]"


def missing_curation_dependency(name: str | None) -> ModuleNotFoundError:
    package = name or "curation dependency"
    return ModuleNotFoundError(
        f"{package} requires the optional `{CURATION_EXTRA}` dependencies.",
        name=name,
    )


def require_umap() -> None:
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ImportWarning)
            import umap  # noqa: F401
    except ModuleNotFoundError as exc:
        raise missing_curation_dependency(exc.name) from exc


__all__ = [
    "CURATION_EXTRA",
    "missing_curation_dependency",
    "require_umap",
]
