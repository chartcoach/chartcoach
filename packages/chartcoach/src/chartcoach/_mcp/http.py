from __future__ import annotations

import hashlib
import hmac
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from urllib.parse import urlsplit

from mcp.server import MCPServer
from mcp.server.transport_security import TransportSecuritySettings
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.types import ASGIApp, Receive, Scope, Send

from .config import MCPConfig


class _BearerAuth:
    """Authenticate HTTP without buffering or consuming streamed request bodies."""

    def __init__(self, app: ASGIApp, *, token: str) -> None:
        self.app = app
        self.expected = hashlib.sha256(token.encode()).digest()

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        path = scope.get("path", "")
        root_path = scope.get("root_path", "")
        if root_path and path.startswith(root_path + "/"):
            path = path[len(root_path) :]
        if scope["type"] == "http" and path != "/healthz":
            headers = [
                value for name, value in scope["headers"] if name == b"authorization"
            ]
            scheme, _, credential = (
                headers[0].partition(b" ") if len(headers) == 1 else (b"", b"", b"")
            )
            if scheme.lower() != b"bearer" or not hmac.compare_digest(
                hashlib.sha256(credential.lstrip(b" ")).digest(), self.expected
            ):
                response = JSONResponse(
                    {"error": "A valid bearer token is required."},
                    status_code=401,
                    headers={
                        "WWW-Authenticate": 'Bearer realm="chartcoach"',
                        "Cache-Control": "no-store",
                    },
                )
                await response(scope, receive, send)
                return
        await self.app(scope, receive, send)


def create_app(server: MCPServer, *, config: MCPConfig | None = None) -> Starlette:
    """Compose a Streamable HTTP ASGI app with readiness and explicit origin checks.

    The returned app owns the SDK lifespan. When mounting it inside another ASGI
    app, enter its router.lifespan_context from the parent's lifespan.
    """
    settings = config or MCPConfig(transport="streamable-http")
    hosts = list(settings.allowed_hosts)
    origins = list(settings.allowed_origins)
    if settings.public_url:
        hosts.append(urlsplit(settings.public_url).netloc)
        origins.append(settings.public_url)
    security = TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=list(dict.fromkeys(hosts)),
        allowed_origins=list(dict.fromkeys(origins)),
    )
    if settings.transport == "sse":
        app = server.sse_app(host=settings.host, transport_security=security)
    else:
        app = server.streamable_http_app(
            host=settings.host,
            transport_security=security,
            streamable_http_path=settings.path,
            stateless_http=settings.stateless,
            json_response=settings.json_response,
        )

    sdk_lifespan = app.router.lifespan_context
    app.state.ready = False

    @asynccontextmanager
    async def lifespan(application: Starlette) -> AsyncGenerator[None, None]:
        async with sdk_lifespan(application):
            application.state.ready = True
            try:
                yield
            finally:
                application.state.ready = False

    async def health(request: Request) -> JSONResponse:
        ready = request.app.state.ready
        return JSONResponse(
            {"ok": ready},
            status_code=200 if ready else 503,
            headers={"Cache-Control": "no-store"},
        )

    app.router.lifespan_context = lifespan
    app.routes.append(Route("/healthz", health, methods=["GET", "HEAD"]))
    if settings.token:
        app.add_middleware(_BearerAuth, token=settings.token.get_secret_value())
    return app
