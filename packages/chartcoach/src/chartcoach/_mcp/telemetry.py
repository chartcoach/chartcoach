"""Tool-call telemetry: span attributes, one log record per call, and Langfuse export.

`ToolTelemetry` runs inside the MCP SDK's OpenTelemetry middleware, so the
current span is the SDK's `tools/call <name>` span. It adds attributes to that
span. Catalog tools stay free of tracing code, and the attributes reach any
OpenTelemetry exporter the process configures.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import time
import uuid
from collections.abc import Mapping
from importlib.metadata import version
from typing import TYPE_CHECKING, Any

from mcp.server.context import CallNext, HandlerResult, ServerRequestContext
from opentelemetry import baggage, propagate, trace
from opentelemetry.trace import format_trace_id

from chartcoach._catalog import Catalog
from chartcoach._catalog.identity import catalog_identity

from .settings import ENVIRONMENT_FIELDS

if TYPE_CHECKING:
    from langfuse import Langfuse

logger = logging.getLogger("chartcoach.mcp")

# Matches the chat app, which types its search, SQL, and read tools as retrievers.
RETRIEVER_TOOLS = frozenset({"search", "sql", "read"})
METADATA = "langfuse.observation.metadata"


class ToolTelemetry:
    """Annotate each `tools/call` span and log the call's outcome."""

    def __init__(self, catalog: Catalog) -> None:
        identity = catalog_identity(catalog)
        release = identity["release_digest"]
        self.attributes: dict[str, Any] = {
            "langfuse.trace.tags": ("chartcoach", "mcp"),
            "langfuse.version": version("chartcoach"),
            f"{METADATA}.catalogId": release
            or hashlib.sha256(
                (identity["entries_digest"] + identity["manifest_digest"]).encode()
            ).hexdigest(),
        }
        if release:
            self.attributes[f"{METADATA}.catalogReleaseId"] = release
        # A stdio process serves one client connection for its whole lifetime.
        # Claude Code passes its session ID to the stdio servers it spawns.
        host = os.environ.get("CLAUDE_CODE_SESSION_ID")
        self.process = (
            (host, "CLAUDE_CODE_SESSION_ID") if host else (uuid.uuid4().hex, "process")
        )

    async def __call__(
        self, ctx: ServerRequestContext[Any, Any], call_next: CallNext
    ) -> HandlerResult:
        if ctx.method != "tools/call":
            return await call_next(ctx)
        name = (ctx.params or {}).get("name")
        span = trace.get_current_span()
        if span.is_recording():
            span.set_attributes(self.call_attributes(ctx))
        started = time.perf_counter()
        outcome = "exception"
        try:
            result = await call_next(ctx)
            outcome = _outcome(result)
            if span.is_recording():
                span.set_attributes(_result_attributes(result, outcome))
            return result
        except BaseException as exc:
            outcome = type(exc).__name__
            raise
        finally:
            context = span.get_span_context()
            logger.info(
                "tool=%s outcome=%s duration_ms=%.1f trace_id=%s",
                name,
                outcome,
                (time.perf_counter() - started) * 1000,
                format_trace_id(context.trace_id) if context.is_valid else "-",
            )

    def call_attributes(self, ctx: ServerRequestContext[Any, Any]) -> dict[str, Any]:
        params = ctx.params or {}
        meta = ctx.meta or {}
        headers = getattr(ctx.request, "headers", None) or {}
        propagated = _baggage(meta)
        attributes = dict(self.attributes)
        if "arguments" in params:
            attributes["gen_ai.tool.call.arguments"] = _json(params["arguments"])
        if params.get("name") in RETRIEVER_TOOLS:
            attributes["langfuse.observation.type"] = "retriever"

        # Prefer the caller's Langfuse baggage, then the host's conversation,
        # then the narrowest MCP connection.
        session = None
        if _identifier(propagated.get("langfuse_session_id")):
            session = (propagated["langfuse_session_id"], "baggage")
        elif _identifier(meta.get("openai/session")):
            session = (meta["openai/session"], "openai/session")
        elif ctx.request is None:
            session = self.process
        elif headers.get("mcp-session-id"):
            # Stateful HTTP clients present this ID to resume their session.
            digest = hashlib.sha256(headers["mcp-session-id"].encode()).hexdigest()
            session = (digest[:32], "Mcp-Session-Id")
        if session is not None:
            attributes["gen_ai.conversation.id"] = session[0]
            attributes[f"{METADATA}.sessionSource"] = session[1]
        for user in (propagated.get("langfuse_user_id"), meta.get("openai/subject")):
            if _identifier(user):
                attributes["user.id"] = user
                break

        client = ctx.session.client_params
        if client is not None:
            attributes[f"{METADATA}.client"] = client.client_info.name
            attributes[f"{METADATA}.clientVersion"] = client.client_info.version
        if headers.get("user-agent"):
            attributes[f"{METADATA}.userAgent"] = headers["user-agent"]
        return attributes


def start_langfuse() -> Langfuse:
    """Export tool spans to the Langfuse project named by the `LANGFUSE_*` variables."""
    missing = [
        name
        for name in ("LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY")
        if not os.environ.get(name)
    ]
    if missing:
        raise ValueError(
            f"{ENVIRONMENT_FIELDS['tracing']} requires {' and '.join(missing)}."
        )
    try:
        from langfuse import Langfuse
    except ModuleNotFoundError as exc:
        if exc.name is None or not exc.name.startswith("langfuse"):
            raise
        raise ValueError(
            f"{ENVIRONMENT_FIELDS['tracing']} requires chartcoach[tracing]. "
            "Install chartcoach[mcp,tracing]."
        ) from None
    # The client reads the remaining LANGFUSE_* settings. It registers its span
    # processor on the global tracer provider that the MCP SDK records into.
    return Langfuse()


def _outcome(result: HandlerResult) -> str:
    if not isinstance(result, Mapping) or result.get("isError") is not True:
        return "ok"
    structured = result.get("structuredContent")
    error = structured.get("error") if isinstance(structured, Mapping) else None
    code = error.get("code") if isinstance(error, Mapping) else None
    return code if isinstance(code, str) else "tool_error"


def _result_attributes(result: HandlerResult, outcome: str) -> dict[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    structured = result.get("structuredContent")
    text = "\n".join(
        item["text"]
        for item in result.get("content") or ()
        if isinstance(item, Mapping) and isinstance(item.get("text"), str)
    )
    attributes: dict[str, Any] = {
        "gen_ai.tool.call.result": text if structured is None else _json(structured)
    }
    if outcome != "ok":
        error = structured.get("error") if isinstance(structured, Mapping) else None
        message = error.get("message") if isinstance(error, Mapping) else text
        attributes[f"{METADATA}.errorCode"] = outcome
        # The SDK sets the span's ERROR status without a description.
        attributes["langfuse.observation.status_message"] = str(message or outcome)
    return attributes


def _baggage(meta: Mapping[str, Any]) -> Mapping[str, object]:
    # The SDK parents its span on the `_meta` trace context but attaches only
    # the span, so the carrier's baggage is read from `_meta` directly.
    try:
        return baggage.get_all(propagate.extract(meta)) if meta else {}
    except (ValueError, TypeError):
        return {}


def _identifier(value: object) -> bool:
    return isinstance(value, str) and 0 < len(value) <= 200


def _json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), default=str)
