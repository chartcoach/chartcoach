# chartcoach docs

Fumadocs and Next.js static documentation for chartcoach. The published docs
site is [docs.chartcoach.dev](https://docs.chartcoach.dev/).
Content pages render at root paths such as `/getting-started` on that domain.

Run the docs locally:

```bash
pnpm --dir apps/docs dev
```

The dev script runs through portless at `https://docs.chartcoach.localhost`.
Run `pnpm --dir apps/docs dev:app` to start Next.js directly.

Run checks from the repository root:

```bash
pnpm --dir apps/docs lint
pnpm --dir apps/docs typecheck
pnpm --dir apps/docs build
```

The build writes static files to `apps/docs/out`. Serve that output with:

```bash
pnpm --dir apps/docs start
```

## LLM surfaces

The docs app exports Fumadocs machine-readable routes for agents and search
tools:

- `/llms.txt`: page index generated from the Fumadocs page tree
- `/llms-full.txt`: concatenated Markdown for every docs page
- `/llms.mdx/docs/<path>/content.md`: Markdown for one docs page

Rendered docs pages include Fumadocs page actions for copying the current page
as Markdown and opening the Markdown route.
