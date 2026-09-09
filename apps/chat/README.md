# ChartCoach chat

Upload a chart, ask a question, and receive guideline-grounded feedback with visual
citations. [Next.js](https://nextjs.org/) hosts the interface,
[assistant-ui](https://www.assistant-ui.com/docs) supplies the chat primitives,
and [Eve](https://eve.dev/docs/guides/frontend/nextjs) runs the agent on the same
origin. [Streamdown](https://streamdown.ai/) formats the recommendations.
[StyleX](https://stylexjs.com/) compiles component styles into an atomic stylesheet.
Vector, keyword, and hybrid search use native [LanceDB](https://lancedb.github.io/lancedb/js/)
queries. [DuckDB](https://duckdb.org/docs/stable/clients/node_neo/overview) runs SQL
over the catalog. Query embeddings run on your CPU.

## Run locally

Use Node.js 24 or later on macOS or Linux. From the repository root:

```bash
pnpm install --frozen-lockfile
cp apps/chat/.env.example apps/chat/.env.local
pnpm --dir apps/chat dev
```

[Portless](https://github.com/vercel-labs/portless) prints the app's local HTTPS
URL. `withEve()` starts the agent alongside Next.js and mounts its routes on that
origin. The browser needs no separate agent URL.

Eve and Next.js load `.env.local`. Configure your OpenAI-compatible chat endpoint
and a vision-capable model it serves:

```dotenv
OPENAI_BASE=http://localhost:8317/v1
OPENAI_API_KEY=sk-
OPENAI_MODEL=gpt-5.6-luna
```

The supplied settings expect that local endpoint to be running. Replace the
model and credentials for another provider. These settings stay on the server.
Your question, uploaded image, and retrieved guidance go to the configured LLM.
Query embeddings are computed locally.

## Review a chart

Drop a PNG, JPEG, or WebP image up to 3 MiB anywhere in the app, or choose
**Add chart** to select it. Attach one chart at a time, then ask:

> What is the most important improvement supported by the guidelines?

The agent inspects the pixels, searches the catalog, reads relevant entries,
and returns up to three findings marked **Working well**, **Improve**, or **Check**.
Each leads with what to retain, change, or check.

Each finding has one primary guideline and optional supporting guidelines.
Primary guidance directly grounds the finding. Supporting guidance adds a relevant
qualification or corroboration, and must also have been read. Citation links show
the guideline titles. Expand **Why this applies** to compare the chart observation
with the authored requirement and inspect supporting citations.

The guideline panel shows search matches as they arrive, marks entries when read,
and identifies primary and supporting guidance when the review is verified.
Primary guidelines follow the order of the findings. Supporting guidance and
other explored entries are expandable. Select a title to inspect its
[Open Graph](https://ogp.me/) image preview, with one preview open at a time. The panel sits
beside the conversation on desktop. On narrow screens, expand **Guidelines** to
inspect it.
You can ask follow-up questions about the same
image, stop a response, or start a new chat.

Expand **Review activity**, then a search or read action, to inspect its query,
search method, matched guidelines, and sources. Vector-search details include
the embedding model and index profile.

Each new turn anchors to its question. Scroll to read the feedback or inspect
earlier messages.

Tool activity streams as the agent works. The completed review appears after its
structure and guideline IDs are checked against entries read in the conversation.
The agent checks applicability before assigning an assessment, asks for missing
context, reports when guidance does not apply, and
declines unrelated requests. The UI keeps a citation link visible if its preview
image cannot load. Card images load through Next.js from `chartcoach.dev`.

A new attachment replaces the selected chart and preserves your message draft.
Images stay in the draft until you send the message.

Eve stages image bytes in its local just-bash sandbox and restores them for model
calls. The 3 MiB limit keeps the image within Eve's model-visible attachment
bound. Local sessions and sandbox files persist under `.eve/`.

The first indexed search downloads the index. Vector and hybrid queries also
download about 86 MiB of model weights. Both persist in the platform's per-user
`chartcoach` cache. Later calls reuse the catalog, table, and model. SQL tables
are materialized once per loaded catalog and reused across queries.
`CATALOG_SOURCE` and `CATALOG_PROFILE` select the release and index profile.
Vector and hybrid search use its normalized `all-MiniLM-L6-v2` embeddings.

## Choose your agent's knowledge

Open **Knowledge** to choose the guidelines your agent can use for feedback.
Drag the year-range handles or enter exact years. Include or exclude
authors and select source types. Blank fields keep the full range.

[Mosaic](https://uwdata.github.io/mosaic/) coordinates the linked views using
DuckDB-WASM in a browser worker. Facet counts reflect the other filters, so you
can compare alternatives before applying a selection. Expand **Preview matching guidelines**
to inspect candidate titles.

The first opening fetches verified Parquet and manifest bytes over authenticated
HTTPS and loads DuckDB's worker and WASM assets from this app. DuckDB also loads
its version-matched JSON extension from its configured extension repository.
Catalog exploration requires a browser with WebAssembly exception handling.
Draft filtering runs on your device. Closing and reopening the panel reuses the
loaded database. Reloading the catalog or leaving the page disposes the worker.

Author, year, and source-type requirements must match the same linked source.
An excluded author disqualifies a guideline if any linked source names them.
Qualifying guidelines retain their full source context.

Choose **Use these guidelines** to start a fresh review with your chart and message draft preserved.
Applying stays local. The first message sends the catalog identity and Mosaic's
full selection SQL in a compressed header. The server executes that query before
starting the agent and retains the resolved guideline IDs in private session
state. Follow-up messages reuse that fixed scope. Search, SQL, schema inspection,
and guideline reads all use it. A selection with zero matches pauses sending
until you broaden your selection.

## Choose a search path

Ask for the method that fits your task, or let the agent choose:

| Method  | Ask                                                                               | What runs                                                        |
| ------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Vector  | “Find guidance about reducing eye travel.”                                        | Meaning-based similarity using local embeddings.                 |
| Keyword | “Use keyword search for legend labels.”                                           | BM25-ranked full-text search over indexed terms.                 |
| Hybrid  | “Use hybrid search for direct labels and series identification.”                  | Vector and keyword results combined with reciprocal rank fusion. |
| SQL     | “Inspect the schema, then find label guidance from sources published since 2020.” | Read-only DuckDB filters, joins, and aggregates.                 |

`describe_catalog` returns actual table columns, counts, label families, section
roles, and index profiles. `query_catalog` accepts one SELECT query over
`guidelines`, `sections`, `guideline_labels`, `references`, `guideline_references`,
and `guideline_sources`. For example:

```sql
SELECT DISTINCT g.id, g.title
FROM guidelines g
JOIN guideline_sources s ON s.guideline_id = g.id
WHERE try_cast(s.year AS INTEGER) >= 2020
  AND g.title ILIKE '%label%'
ORDER BY g.title
LIMIT 5
```

Include `id` or `guideline_id` to retrieve canonical guideline previews. Search and
SQL results are candidates. The agent still reads selected entries before citing them.
Expanded tool details show the method, query, ranking, SQL rows, and schema.

Agent SQL has external access and extension loading disabled, read-only transactions,
a five-second query deadline, and a 50-row maximum. SQL rows are bounded to 64 KiB.
Exact integers and decimals use strings in JSON results. For trusted scripts that
need SQL directly over Lance datasets, use DuckDB's
[Lance extension](https://duckdb.org/docs/current/core_extensions/lance) in a separate
connection with the directory from `indexPath()`. Treat extension queries as
filesystem-capable code and keep them outside the agent's restricted SQL connection.

## Follow the code

| Change                                                                | Owner                                                                       |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Routes, page metadata, and agent mounting                             | [app](app) and [next.config.ts](next.config.ts)                             |
| Conversation, composer, and guideline presentation                    | [components/chat](components/chat)                                          |
| Filter controls and shared visual primitives                          | [components/catalog](components/catalog) and [components/ui](components/ui) |
| Conversation state, uploads, and filter transitions                   | [chat](chat)                                                                |
| Browser DuckDB worker, Parquet ingestion, and Mosaic queries          | [browser](browser)                                                          |
| Browser requests for catalog metadata and counts                      | [lib/catalog-client.ts](lib/catalog-client.ts)                              |
| Verified artifacts, native tables, metadata, and cached filter scopes | [lib/catalog](lib/catalog)                                                  |
| Embedding, search, bounded SQL, and result hydration                  | [lib/retrieval](lib/retrieval)                                              |
| Authentication, prompts, and Eve tool adapters                        | [agent](agent)                                                              |
| Review and filter wire contracts                                      | [shared](shared)                                                            |

The SDK's `catalog.table()` and `catalog.describe()` define the canonical tables
and schemas. `registerCatalog()` from `@chartcoach/catalog/duckdb` installs them
in the app's caller-owned databases. Filtered databases register exact eligible
IDs, preserving their complete source context.

Catalog infrastructure is independent of Eve and React. Retrieval services apply
the chat app's result limits and query policies to a catalog scope. Eve tools
pass the initiating session's resolved selection to those services. SQL execution and
guideline-card hydration share one scope lease.

assistant-ui owns draft text, pending attachments, message context, and viewport
scrolling. Its [external-store runtime](https://www.assistant-ui.com/docs/runtimes/custom/external-store)
consumes the verified conversation derived from Eve. The `@assistant-ui/eve`
converters translate message payloads between the two libraries.

Customize primitive markup and colocated `stylex.create` styles in
`components/chat/`. `components/ui/tokens.stylex.ts` owns colors, breakpoints,
and motion values. `components/ui/ui.ts` contains shared control and focus styles.
The CSS entrypoint contains browser resets and the shared brand palette.

Next.js uses StyleX's Babel and PostCSS plugins to compile styles and serve the
stylesheet. Tests use its bundler plugin to exercise compiled components.
Keep guideline verification in `chat/evidence.ts` and the shared review contract.
The runtime's `onNew` callback requests Eve's structured output for each message.
The underlying send operation accepts text and image parts:

```ts
import { reviewSchema } from "../shared/review";

await agent.send(
  [
    { type: "text", text: prompt },
    { type: "file", data: imageDataUrl, mediaType: file.type, filename: file.name },
  ],
  { outputSchema: reviewSchema },
);
```

LanceDB searches the directory returned by `indexPath()`. Document `parent_id`
values identify entries to read and cite through the catalog API.

## Validate

With the app running, use its printed URL:

```bash
pnpm --dir apps/chat eval --url "$APP_URL"
```

This exercises the Next.js proxy and Eve's real session runtime using the
configured LLM. The evals check image observations, read-before-cite behavior,
structured feedback, and out-of-scope requests. A separate model-graded check
compares each recommendation with its cited guideline text, using the configured
LLM endpoint. Results and event
traces are stored under `.eve/evals/`.

For an agent-only check, `pnpm --dir apps/chat eval` starts an ephemeral
Eve server. Repository checks use Oxlint, formatting, TypeScript, and Eve discovery.

## Build

```bash
pnpm --dir apps/chat build
pnpm --dir apps/chat start
```

The build compiles Eve and Next.js. It also boots a relocated copy of the agent
output to verify native assets and production authentication. `nitro.config.ts`
keeps tracing inside the workspace and preserves package-relative assets.
Build on the deployment's operating system and architecture because the output
includes native binaries.

`start` runs both servers and stops the other if either exits. `PORT` selects the
Next.js port. Eve uses port 4274 by default. To change it, set
`EVE_NEXT_PRODUCTION_PORT` to the same value during both build and start so the
compiled proxy route reaches the agent.

Configure [Eve route authentication](https://eve.dev/docs/guides/auth-and-route-protection)
before exposing the production app. Its agent routes reject unauthenticated
requests by default. Keep writable persistent cache and workflow storage for a
long-running deployment.
