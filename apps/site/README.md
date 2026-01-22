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

This site uses `@astrojs/sitemap`. To generate a sitemap (and correct canonical URLs), set `SITE_URL` at build time:

```bash
SITE_URL="https://example.com" pnpm --filter site build
```

When building the Docker image, pass the same value as a build arg:

```bash
docker build --build-arg SITE_URL="https://example.com" -f apps/site/Dockerfile .
```
