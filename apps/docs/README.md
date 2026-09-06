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

## Maintain live examples

| Concern                                             | File                                        |
| --------------------------------------------------- | ------------------------------------------- |
| Cell source, Python dependencies, and browser setup | The MDX page containing the example         |
| Build-time marimo compilation                       | `apps/docs/source.config.ts`                |
| Browser activation and JavaScript SDK registration  | `apps/docs/components/notebook-runtime.tsx` |
| MDX component registration                          | `apps/docs/components/mdx.tsx`              |

During a build, `python marimo` fences execute and place their initial output
in the static page. In the browser, Pyodide activates those cells so readers
can interact with them. The notebook runtime registers the workspace
`@chartcoach/catalog` module before the JavaScript live cell connects.

Keep dependency pins and browser setup beside the cell that uses them. After a
live-example change, inspect the static output, activated output, interaction,
and navigation between notebook pages.

## Validate

```bash
pnpm --dir apps/docs check
pnpm --dir apps/docs typecheck
pnpm --dir apps/docs test
pnpm --dir apps/docs build
```

Inspect visible changes at desktop and narrow widths. Run `make check` before
handoff. Live-example builds need network access to the pinned Python package
and catalog files on `files.peter.gy`.

## Machine-readable routes

The static export includes:

- `/llms.txt` for the page index
- `/llms-full.txt` for all page Markdown in one file
- `/llms.mdx/docs/<path>/content.md` for one page

Their route handlers live under `apps/docs/app`. Changes that also touch
`@chartcoach/catalog` or `@chartcoach/brand` must preserve the dependency rules
documented in [Web apps](../../development_docs/architecture/web-delivery.md).
