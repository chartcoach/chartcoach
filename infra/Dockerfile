FROM node:24-bookworm-slim AS build
WORKDIR /build
RUN npm install --global pnpm@12.3.4
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
COPY patches ./patches
COPY apps/chat/package.json ./apps/chat/package.json
COPY apps/docs/package.json ./apps/docs/package.json
COPY apps/site/package.json ./apps/site/package.json
COPY packages/catalog/package.json ./packages/catalog/package.json
COPY packages/brand/package.json ./packages/brand/package.json
COPY skills/package.json ./skills/package.json
COPY tools/release/package.json ./tools/release/package.json
RUN --mount=type=cache,target=/pnpm/store pnpm install --frozen-lockfile --store-dir=/pnpm/store
COPY . .
RUN pnpm --dir apps/chat build \
    && mkdir /packages \
    && npm pack ./packages/catalog --ignore-scripts --pack-destination /packages \
    && npm pack ./apps/chat/dist --ignore-scripts --pack-destination /packages

FROM scratch AS packages
COPY --from=build /packages /

FROM node:24-bookworm-slim AS runtime
LABEL org.opencontainers.image.source="https://github.com/chartcoach/chartcoach" \
    org.opencontainers.image.licenses="Apache-2.0"
ENV NODE_ENV=production \
    ONNXRUNTIME_NODE_INSTALL=skip \
    CHARTCOACH_DATA_DIR=/data \
    CHARTCOACH_CACHE_DIR=/cache
WORKDIR /opt/chartcoach
COPY --from=packages / /packages
RUN --mount=type=cache,target=/root/.npm npm install --ignore-scripts=false --omit=dev /packages/*.tgz \
    && rm -rf /packages \
    && mkdir /data /cache \
    && chown node:node /data /cache
USER node
EXPOSE 4273
HEALTHCHECK --interval=30s --timeout=5s --start-period=90s \
    CMD node -e "fetch('http://127.0.0.1:4273/healthz').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))"
ENTRYPOINT ["node", "/opt/chartcoach/node_modules/chartcoach/cli/index.mjs", "chat", "--no-open"]
CMD ["--host", "0.0.0.0"]
