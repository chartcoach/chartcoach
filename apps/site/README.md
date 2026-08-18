# @chartcoach/site

The Astro app reads a Guideline Catalog and builds public guideline pages,
search data, machine-readable Markdown and JSON, Open Graph images, and a
sitemap. The deployed catalog browser is
[chartcoach.dev](https://chartcoach.dev/).

## Run locally

Run these commands from the repository root:

```bash
make install
pnpm --dir apps/site dev
```

Open `https://chartcoach.localhost` and confirm the fixture-backed catalog
browser renders. The dev command uses portless. Run
`pnpm --dir apps/site dev:app` to start Astro directly.

## Choose the catalog

`CHARTCOACH_SITE_CATALOG_SOURCE` selects the catalog used during development,
typechecking, and builds:

| Context          | Accepted value                                                       |
| ---------------- | -------------------------------------------------------------------- |
| Unset            | Repository fixture at `fixtures/catalog-release`                     |
| Local override   | Compiled bundle directory, `catalog.json` URL, or `release.json` URL |
| Cloudflare Pages | HTTPS URL ending in `/<64-hex-digest>/release.json`                  |

Override paths can be absolute or relative to `apps/site`.

Remote builds verify the release digest and the byte count and SHA-256 hash of
`MANIFEST.md` and `entries.parquet`. Cloudflare Pages rejects missing values,
local paths, HTTP URLs, `catalog.json`, and release URLs without a digest in
the path.

## Validate and build

| Command                          | Purpose                                                 |
| -------------------------------- | ------------------------------------------------------- |
| `pnpm --dir apps/site check`     | Check formatting, lint rules, and TypeScript types      |
| `pnpm --dir apps/site test`      | Run source, search, LLM, and Open Graph tests           |
| `pnpm --dir apps/site typecheck` | Check Astro and TypeScript against the selected catalog |
| `pnpm --dir apps/site build`     | Write the static site to `apps/site/dist`               |
| `pnpm ready`                     | Check every JavaScript workspace package                |

Run `make check` before handoff.

## License

Licensed under [Apache-2.0](../../LICENSE).
