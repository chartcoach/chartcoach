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
