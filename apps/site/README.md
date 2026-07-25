# @chartcoach/site

Astro public site for the chartcoach Guideline Catalog browser and public
guideline pages. The published public site is
[chartcoach.dev](https://chartcoach.dev/).

Run it locally:

```bash
pnpm --dir apps/site dev
```

The dev script runs through portless at `https://chartcoach.localhost`.
Run `pnpm --dir apps/site dev:app` to start Astro directly.

Run focused checks and a build from the repository root:

```bash
pnpm --dir apps/site check
pnpm --dir apps/site test
pnpm --dir apps/site typecheck
pnpm --dir apps/site build
```

Typechecks and builds use the shared catalog release fixture by default. Set
`CHARTCOACH_SITE_CATALOG_SOURCE` to build against an exact HTTP release
descriptor.

Run `pnpm ready` for the complete JavaScript workspace gate.

## License

Apache-2.0. See [LICENSE](../../LICENSE).
