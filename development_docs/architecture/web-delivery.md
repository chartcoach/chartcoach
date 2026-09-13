# Web apps

The public site, product docs, and chat are separate applications. They import
the shared brand package. The site and chat also read the catalog package.

```text
apps/site  -> @chartcoach/catalog
          -> @chartcoach/brand

apps/docs  -> @chartcoach/brand

apps/chat  -> @chartcoach/catalog/node
          -> @chartcoach/brand
```

The apps do not import each other. Vite+ rules and the tests under
`tools/architecture` enforce these paths.

## Public site

`apps/site/src/config/catalog-location.ts` chooses the catalog read by Astro.

| Context          | Catalog location                                                  |
| ---------------- | ----------------------------------------------------------------- |
| Local default    | `fixtures/catalog-release`                                        |
| Local override   | `CHARTCOACH_SITE_CATALOG`                                         |
| Cloudflare Pages | Exact HTTPS `release.json` URL containing its 64-character digest |

Cloudflare Pages fails when the variable is missing, empty, local, mutable, or
uses HTTP. This prevents a deployment from quietly building the small test
fixture or following a moving `catalog.json` selection.

Local inputs use the same descriptor-backed package loader as remote inputs.
A directory with `release.json` verifies the core files listed by that release.
A deployed root with `catalog.json` resolves `catalog/releases/<digest>/` and
retains the exact release location. A directory with `MANIFEST.md` and
`entries.parquet` is a descriptor-free bundle. A directory containing both
selection and exact release descriptors is rejected.

The loaded catalog feeds:

- guideline HTML, JSON, and Markdown pages
- the browser search index
- `llms.txt` files
- Open Graph images
- the sitemap and catalog listing

Each Astro loader or integration writes its own generated files. The build
output lives in `apps/site/dist`.

## Product docs

Task guides live under `apps/docs/content/docs/(guide)`. API and file reference
pages live under `apps/docs/content/docs/(reference)`. The nearest `meta.json`
lists pages in navigation order.

The docs app also exports `/llms.txt`, `/llms-full.txt`, and one Markdown route
per page.

Fumadocs derives navigation from `meta.json`, table-of-contents headings from
MDX, and the static search index from the same source collection. Code examples
render as highlighted, copyable blocks. Validate examples against the workspace
packages when their API or instructions change.

## Chat app

`apps/chat` publishes the `chartcoach` npm application. Next.js exports its interface as static assets. The CLI supervises an Eve worker and serves the interface and authenticated agent requests on one public origin. The browser
sends chart images and questions to Eve and receives structured reviews and tool
events. Shared schemas define filter selections and review evidence.

`runtime/schema.ts` owns the configuration schema. `runtime/environment.ts` derives
typed T3 Env validation from it, and `runtime/config.ts` applies precedence. The launcher
validates it before starting a worker, resolves the selected catalog release, and
passes one resolved configuration to the worker. `runtime/start.ts` owns the data
directory lock and the worker and gateway resources. `runtime/worker.ts` owns the
Nitro listener, storage readiness, and shutdown hooks. It reports its ready URL
over IPC. Eve's working directory
is the configured data directory, so its workflows and sandbox files persist beside
the app database and credential key.

`runtime/gateway.ts` serves static assets and forwards `/eve/` requests to the
private worker using a per-process credential. The public listener validates Host
and Origin headers. Network listeners require HTTP Basic authentication. Workflow
callbacks remain on the worker's loopback origin. The gateway replaces forwarded
headers with its configured public origin.

The pinned Eve dependency has two focused patches: preserving image bytes in
instrumentation and keeping live stream events ordered during disk catch-up.
`apps/chat/test/workflow-stream.test.mjs` exercises the latter against Eve's actual
vendored reader, including replay from a saved cursor. Keep these checks when
upgrading Eve and remove a patch only when the upstream version passes them.

The app separates rendering, browser computation, and server catalog access:

- `components/` renders the conversation, filters, and guideline previews.
- `chat/` owns browser conversation state, attachments, and filter transitions.
- `browser/` owns a DuckDB-WASM worker and Mosaic's linked query clients.
- `lib/catalog/` loads verified catalog artifacts and owns native tables and filter scopes.

`lib/retrieval/` applies the chat app's search, embedding, and bounded SQL policies
to those scopes. `agent/` binds these operations to Eve's authenticated routes and
tools. Each review uses its initiating filter selection for every retrieval path.
The public catalog package continues to own artifact verification and persistent
artifact caching.

Browser filtering loads the release's verified core files through authenticated,
digest-bound routes, then queries Parquet and canonical tables locally. Mosaic
facet clients omit their own positive filter, while the
result count and preview apply every filter. Worker assets are generated from
the installed package by `scripts/prepare-duckdb.mjs` during dev/build setup.

The count client captures a full `SELECT DISTINCT g.id` selection query. Applying
filters retains it locally. The first Eve session request sends `{ catalogId, sql }`
as gzip/base64 in `x-chartcoach-selection`. Follow-ups omit that header.
Authentication bounds the encoded header and decompressed data, validates one
read-only query, and requires known guideline IDs. The server freezes those IDs
in the initiating session's private authentication state. Scope-cache eviction
rebuilds tables from that fixed set, preserving the selection across queries.

Run `pnpm --dir apps/chat dev` for the local app and agent. Run
`pnpm --dir apps/chat eval --url "$APP_URL"` to exercise the configured model
through the browser-facing origin.

## Generated directories

| Directory               | Generated by                      |
| ----------------------- | --------------------------------- |
| `apps/site/.astro`      | Astro content and type generation |
| `apps/site/dist`        | Astro build                       |
| `apps/docs/.source`     | Fumadocs content generation       |
| `apps/docs/.next`       | Next.js build                     |
| `apps/docs/out`         | Static docs export                |
| `apps/chat/.next`       | Next.js build                     |
| `apps/chat/out`         | Static chat interface             |
| `apps/chat/dist`        | Installable npm application       |
| `apps/chat/.output`     | Eve production build              |
| `packages/catalog/dist` | JavaScript package build          |

Edit the source files, then run the package that writes the generated
directory. Do not edit generated output directly.

## Focused checks

| Change                     | Command and inspection                                       |
| -------------------------- | ------------------------------------------------------------ |
| Site catalog location      | `pnpm --dir apps/site test` and `pnpm --dir apps/site build` |
| Site output or search      | `pnpm --dir apps/site test` and inspect `apps/site/dist`     |
| Docs content or navigation | `pnpm --dir apps/docs build` plus browser links and search   |
| Shared web import          | `pnpm check:architecture`                                    |

## Chat distribution

`apps/chat/scripts/package.mjs` assembles compiled Eve code and the static UI into
`apps/chat/dist`. It excludes traced `node_modules` and resolves exact runtime
versions for the distribution manifest. The pinned Eve build tooling supplies a
sandbox plan containing its compiled template keys and skill seeds. The worker
provisions that plan through the public just-bash backend before readiness. This
keeps template state in the data directory and compiler dependencies in the build. npm installs native dependencies for the
consumer platform. The source workspace keeps the compiler, frontend dependencies,
and private brand and skill packages.

`infra/Dockerfile` builds and installs the same npm tarballs. `infra/compose.yml` persists `/data`
and `/cache`. `tools/release/verify-chat.mjs` installs both tarballs outside the
workspace and checks the CLI, authenticated browser, a streamed grounded answer,
and conversation persistence after restart.
