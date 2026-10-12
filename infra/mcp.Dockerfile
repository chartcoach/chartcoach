# syntax=docker/dockerfile:1
# The chartcoach MCP server over Streamable HTTP, built from the locked workspace.
#   docker build -f infra/mcp.Dockerfile -t chartcoach-mcp .
#   docker run -p 8000:8000 -e CHARTCOACH_MCP_PUBLIC_URL=https://mcp.example.org chartcoach-mcp

FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS build
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0 \
    UV_NO_DEV=1
WORKDIR /app

# Dependencies change less often than the package, so they get their own layer.
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=.python-version,target=.python-version \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=packages/chartcoach/pyproject.toml,target=packages/chartcoach/pyproject.toml \
    uv sync --locked --package chartcoach --extra mcp --extra embedding-openai \
        --no-install-workspace

COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --package chartcoach --extra mcp --extra embedding-openai \
        --no-editable

FROM python:3.12-slim-bookworm
LABEL org.opencontainers.image.source="https://github.com/chartcoach/chartcoach" \
    org.opencontainers.image.licenses="Apache-2.0"
RUN useradd --uid 1000 --create-home chartcoach \
    && mkdir /cache \
    && chown chartcoach:chartcoach /cache
COPY --from=build --chown=chartcoach:chartcoach /app/.venv /app/.venv

# The catalog cache lives in /cache. Mount a volume there to keep verified
# releases across restarts.
ENV PATH="/app/.venv/bin:$PATH" \
    XDG_CACHE_HOME=/cache \
    CHARTCOACH_MCP_TRANSPORT=streamable-http \
    CHARTCOACH_MCP_HOST=0.0.0.0 \
    CHARTCOACH_MCP_PORT=8000
USER chartcoach
WORKDIR /home/chartcoach
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=60s \
    CMD python -c "import urllib.request, sys; sys.exit(urllib.request.urlopen('http://127.0.0.1:8000/healthz', timeout=4).status != 200)"

ENTRYPOINT ["chartcoach", "mcp"]
