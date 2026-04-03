# Chart Coach site (Astro + Starlight)

This app is the public-facing browser for the Chart Coach guideline catalog.

## Develop

From the repo root:

```bash
pnpm --filter site dev
```

## Validate

```bash
pnpm --filter site astro check
pnpm --filter site build
```

## Sitemap

This site uses `@astrojs/sitemap`.

- If `SITE_URL` is unset, builds fall back to `http://localhost:4321/`.
- For deployments, set `SITE_URL` so canonical URLs and the sitemap point at the real domain.

```bash
SITE_URL="https://example.com" pnpm --filter site build
```

For local dev, you can also define `SITE_URL` in the repo-root `.env` (see `.env.example`).

When building the Docker image, pass the same value as a build arg:

```bash
docker build --build-arg SITE_URL="https://example.com" -f apps/site/Dockerfile .
```

## Agentation review mode

ChartCoach’s site can mount the Agentation toolbar for desktop design review.

### Default behavior

- local development: enabled automatically
- preview / other non-dev builds: disabled unless `PUBLIC_ENABLE_AGENTATION=true`
- unsupported mobile / coarse-pointer viewports: hidden

### Optional environment variables

- `PUBLIC_ENABLE_AGENTATION=true` — allow the toolbar outside local dev
- `PUBLIC_AGENTATION_ENDPOINT=http://localhost:4747` — connect the toolbar to an external Agentation / MCP HTTP endpoint

### Example preview flow

```bash
PUBLIC_ENABLE_AGENTATION=true \
PUBLIC_AGENTATION_ENDPOINT=http://localhost:4747 \
pnpm --filter site build

PUBLIC_ENABLE_AGENTATION=true \
PUBLIC_AGENTATION_ENDPOINT=http://localhost:4747 \
pnpm --filter site preview
```

### Notes

- Phase 1 is local-first; if no endpoint is configured, Agentation falls back to local copy/localStorage behavior.
- The integration is intended for internal review. See Agentation licensing before redistributing it as part of a product.
