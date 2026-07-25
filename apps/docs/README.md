# chartcoach docs

The docs app builds the static chartcoach documentation site with Fumadocs and
Next.js. The published docs site is [docs.chartcoach.dev](https://docs.chartcoach.dev/).
Content pages render at root paths such as `/getting-started` on that domain.

Run the docs locally:

```bash
pnpm --dir apps/docs dev
```

The dev script runs through portless at `https://docs.chartcoach.localhost`.
Run `pnpm --dir apps/docs dev:app` to start Next.js directly.

Run focused checks and a build from the repository root:

```bash
pnpm --dir apps/docs check
pnpm --dir apps/docs typecheck
pnpm --dir apps/docs build
```

Run `pnpm ready` for the complete JavaScript workspace gate.

The build writes static files to `apps/docs/out`.

## Machine-readable docs routes

The docs site exports Fumadocs machine-readable routes for agents and search
tools:

- `/llms.txt`: page index generated from the Fumadocs page tree
- `/llms-full.txt`: concatenated Markdown for every docs page
- `/llms.mdx/docs/<path>/content.md`: Markdown for one docs page

Rendered docs pages include Fumadocs page actions for copying the current page
as Markdown and opening the Markdown route.
