FROM node:22-slim AS builder

WORKDIR /app

ENV NODE_ENV=production

RUN corepack enable

COPY . .

RUN pnpm install --frozen-lockfile

# Build eval-ui and its workspace dependencies
RUN pnpm --filter @chartcoach/eval-ui... build


FROM node:22-slim AS runner

WORKDIR /app

ENV NODE_ENV=production
ENV NITRO_HOST=0.0.0.0
ENV NITRO_PORT=3000

# App runtime (Nitro output) + data files loaded by server functions
COPY --from=builder /app/apps/eval-ui/.output ./apps/eval-ui/.output
COPY --from=builder /app/apps/eval-ui/fixtures ./apps/eval-ui/fixtures
COPY --from=builder /app/evals ./evals
COPY --from=builder /app/guidelines ./guidelines

EXPOSE 3000

CMD ["node", "apps/eval-ui/.output/server/index.mjs"]
