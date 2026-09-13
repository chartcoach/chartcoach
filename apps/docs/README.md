# chartcoach docs

The docs app renders MDX files from `content/docs` with Next.js and Fumadocs.
A build exports the static site to `apps/docs/out` for
[docs.chartcoach.dev](https://docs.chartcoach.dev/).

## Develop

Run these commands from the repository root:

```bash
make install
pnpm --dir apps/docs dev
```

The command starts Next.js through
[Portless](https://github.com/vercel-labs/portless) and prints the local URL.
With the default proxy settings, the primary checkout uses
`https://docs.chartcoach.localhost`. A linked
[Git worktree](https://git-scm.com/docs/git-worktree) adds a subdomain derived
from its branch name, such as `https://search-ui.docs.chartcoach.localhost`, so
concurrent checkouts keep separate routes. Run `pnpm --dir apps/docs dev:app`
to start Next.js directly.

## Change the content

- Add task guides under `apps/docs/content/docs/(guide)`.
- Add API and data reference pages under
  `apps/docs/content/docs/(reference)`.
- Update the nearest `meta.json` when adding, removing, or reordering a page.
- Register MDX components in `apps/docs/components/mdx.tsx`.

Route-group directory names stay out of published URLs. For example,
`(guide)/getting-started.mdx` publishes at `/getting-started`.

## Validate

```bash
pnpm --dir apps/docs check
pnpm --dir apps/docs typecheck
pnpm --dir apps/docs build
```

Inspect visible changes at desktop and narrow widths. Run `make check` before
handoff. Run changed code examples against the workspace packages before
building. Check page links, search results, copy controls, and Markdown routes
in the static export.

## Machine-readable routes

The static export includes:

- `/llms.txt` for the page index
- `/llms-full.txt` for all page Markdown in one file
- `/llms.mdx/docs/<path>/content.md` for one page

Their route handlers live under `apps/docs/app`. Changes that also touch
`@chartcoach/catalog` or `@chartcoach/brand` must preserve the dependency rules
documented in [Web apps](../../development_docs/architecture/web-delivery.md).
