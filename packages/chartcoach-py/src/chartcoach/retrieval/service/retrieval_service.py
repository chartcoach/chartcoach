from __future__ import annotations

from collections.abc import Callable, Sequence
from os import PathLike

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import StrategyInfo
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.registry import StrategyRegistration
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse


class RetrievalServiceError(Exception):
    """Base error for retrieval use-cases (framework-agnostic)."""


class UnknownStrategyError(RetrievalServiceError):
    pass


class CatalogLoadError(RetrievalServiceError):
    pass


class StrategyInitError(RetrievalServiceError):
    pass


class StrategyRunError(RetrievalServiceError):
    pass


class StrategyUpstreamError(RetrievalServiceError):
    """Strategy failed due to an upstream dependency (e.g., LM provider)."""


CatalogLoader = Callable[[str | PathLike[str]], Catalog]


_CACHE_CONFIGURED = False


def configure_dspy_cache() -> None:
    """Enable DSPy disk+memory caching once per process."""
    global _CACHE_CONFIGURED
    if _CACHE_CONFIGURED:
        return

    try:
        import dspy
    except ImportError as e:  # pragma: no cover
        raise RuntimeError(
            "Install `chartcoach[retrieval]` to run retrieval strategies."
        ) from e

    dspy.configure_cache(enable_disk_cache=True, enable_memory_cache=True)
    _CACHE_CONFIGURED = True


class RetrievalService:
    def __init__(
        self,
        *,
        registrations: Sequence[StrategyRegistration],
        catalog_loader: CatalogLoader = Catalog.from_uri,
        configure_cache: Callable[[], None] = configure_dspy_cache,
    ) -> None:
        self._catalog_loader = catalog_loader
        self._configure_cache = configure_cache
        self._by_id = {
            strategy_cls.id: (strategy_cls, factory)
            for strategy_cls, factory in registrations
        }

    def list_strategies(self) -> list[StrategyInfo]:
        infos = [strategy_cls.info() for strategy_cls, _factory in self._by_id.values()]
        return sorted(infos, key=lambda s: s.id)

    def _require_registration(self, strategy_id: str) -> StrategyRegistration:
        registration = self._by_id.get(strategy_id)
        if registration is None:
            raise UnknownStrategyError(f"Unknown strategy id: {strategy_id!r}.")
        return registration

    def load_catalog(self, catalog_uri: str | PathLike[str]) -> Catalog:
        try:
            return self._catalog_loader(catalog_uri)
        except (OSError, ValueError) as e:
            raise CatalogLoadError(str(e)) from e

    def instantiate_strategy(self, strategy_id: str, *, catalog: Catalog):
        self._configure_cache()
        _strategy_cls, factory = self._require_registration(strategy_id)
        try:
            return factory(catalog=catalog)
        except RuntimeError as e:
            raise StrategyInitError(str(e)) from e

    def instantiate_strategies(
        self,
        *,
        catalog_uri: str,
        strategy_ids: Sequence[str] | None = None,
    ) -> list[tuple[StrategyInfo, RetrievalStrategy]]:
        catalog = self.load_catalog(catalog_uri)
        self._configure_cache()

        registrations = list(self._by_id.values())
        if strategy_ids:
            wanted = set(strategy_ids)
            registrations = [reg for reg in registrations if reg[0].id in wanted]
            missing = wanted - {reg[0].id for reg in registrations}
            if missing:
                raise UnknownStrategyError(f"Unknown strategy ids: {sorted(missing)}")

        strategies = [
            (strategy_cls.info(), factory(catalog=catalog))
            for strategy_cls, factory in registrations
        ]
        strategies.sort(key=lambda s: s[0].id)
        return strategies

    def run_strategy(
        self,
        strategy_id: str,
        *,
        catalog_uri: str,
        request: RetrievalRequest,
    ) -> RetrievalResponse:
        catalog = self.load_catalog(catalog_uri)
        strategy = self.instantiate_strategy(strategy_id, catalog=catalog)

        try:
            return strategy(request=request)
        except ValueError as e:
            raise StrategyRunError(str(e)) from e
        except Exception as e:  # noqa: BLE001
            raise StrategyUpstreamError(_safe_upstream_error_message(e)) from e


def _safe_upstream_error_message(exc: Exception) -> str:
    lowered = str(exc).lower()

    if "expired_key" in lowered or "expired key" in lowered:
        return (
            "Upstream model authentication failed (expired_key). Check OPENAI_API_KEY."
        )
    if "authentication" in lowered:
        return "Upstream model authentication failed. Check OPENAI_API_KEY."
    if "rate_limit" in lowered or "rate limit" in lowered:
        return "Upstream model rate limit exceeded."

    return "Upstream model request failed."
