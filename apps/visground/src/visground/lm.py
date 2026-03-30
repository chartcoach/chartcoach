import logging
import os
from collections.abc import Callable, Iterable
from typing import Any, TypedDict

import dspy
from langfuse import get_client, observe, propagate_attributes
from langfuse._client.constants import ObservationTypeLiteralNoEvent
from openinference.instrumentation.dspy import DSPyInstrumentor

logger = logging.getLogger(__name__)


class ObserveKwargs(TypedDict, total=False):
    name: str | None
    as_type: ObservationTypeLiteralNoEvent | None
    capture_input: bool | None
    capture_output: bool | None
    transform_to_string: Callable[[Iterable[Any]], str] | None


class PropagateAttributesKwargs(TypedDict, total=False):
    user_id: str | None
    session_id: str | None
    metadata: dict[str, str] | None
    version: str | None
    tags: list[str] | None
    trace_name: str | None
    as_baggage: bool


DSPyInstrumentor().instrument()


def lm_cliproxy(model: str) -> dspy.LM:
    return dspy.LM(
        f"openai/{model}",
        api_base="http://localhost:8317/v1",
        api_key="sk-",
    )


def lm_openrouter(model: str) -> dspy.LM:
    return dspy.LM(
        f"openai/{model}",
        api_base="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
    )


dspy.configure_cache(
    enable_disk_cache=True,
    enable_memory_cache=True,
    disk_size_limit_bytes=16 * 1024 * 1024 * 1024,
)

langfuse = get_client()

if not langfuse.auth_check():
    logger.warning(
        "Langfuse client authentication failed; check Langfuse credentials and host."
    )


def make_observed_dspy_module(
    module: dspy.Module,
    observe_kwargs: ObserveKwargs | None = None,
    attributes: PropagateAttributesKwargs | None = None,
    classname: str = "ObservedModule",
) -> dspy.Module:
    if not classname:
        raise ValueError("classname must be a non-empty string.")

    observe_config: ObserveKwargs = {} if observe_kwargs is None else observe_kwargs
    attribute_config: PropagateAttributesKwargs = (
        {} if attributes is None else attributes
    )

    @observe(**observe_config)
    def forward(self, *args, **kwargs) -> dspy.Prediction:
        with propagate_attributes(**attribute_config):
            return module(*args, **kwargs)

    observed_module_type = type(classname, (dspy.Module,), {"forward": forward})
    return observed_module_type()
