# syntax=docker/dockerfile:1.7

FROM node:24-slim AS build

WORKDIR /repo

# Used by `@astrojs/sitemap` and Astro canonical URLs.
ARG SITE_URL
ENV SITE_URL=$SITE_URL

# pnpm via Corepack (respects `packageManager` in root package.json)
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

# 1) Copy only workspace manifests first for optimal layer caching
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
COPY apps/site/package.json apps/site/package.json
COPY packages/chartcoach-js/package.json packages/chartcoach-js/package.json
COPY packages/chartcoach-js/tsconfig*.json packages/chartcoach-js/

# 2) Prefetch deps into pnpm store (BuildKit cache speeds up rebuilds)
RUN --mount=type=cache,id=pnpm-store,target=/pnpm/store \
    pnpm fetch --filter site...

# 3) Copy sources needed for the build
COPY apps/site apps/site
COPY packages/chartcoach-js packages/chartcoach-js
COPY guidelines guidelines

# 4) Install from the prefetched store (no network needed here)
RUN --mount=type=cache,id=pnpm-store,target=/pnpm/store \
    pnpm install --frozen-lockfile --offline --filter site...

# 5) Build workspace deps + site
RUN pnpm -r --filter site... build


FROM nginxinc/nginx-unprivileged:1.27-alpine AS runtime

COPY --from=build /repo/apps/site/dist /usr/share/nginx/html

EXPOSE 8080
