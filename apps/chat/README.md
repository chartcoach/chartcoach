# ChartCoach chat

Review a chart, recommend a design, or discuss a visualization choice with
guideline-backed advice and visual citations. [Next.js](https://nextjs.org/) hosts the interface,
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

Open **Model settings** in the composer to add an Anthropic, OpenAI, Gemini, or
OpenAI-compatible connection. Enter your key, load the provider's model list or
enter a model ID, then choose **Save and use**. Choose a model that supports
images and tool calls. Set its published context limit under **Context window**.

Eve and Next.js load `.env.local`. These optional settings provide a shared
server connection to an OpenAI-compatible endpoint:

```dotenv
OPENAI_BASE=http://localhost:8317/v1
OPENAI_API_KEY=sk-
OPENAI_MODEL=gpt-5.6-luna
```

The supplied settings expect that local endpoint to be running. Replace the
model and credentials for another provider. These settings stay on the server.
Your question, uploaded image, and retrieved guidance go to the configured LLM.
Query embeddings are computed locally.

Server code reads typed settings from [`lib/env.ts`](lib/env.ts).
[t3-env](https://env.t3.gg/docs/nextjs) validates them during Next.js startup/build
and Eve loading. Empty optional values become unset. Invalid settings report
their names, keeping credential values out of validation errors.
Builds and catalog operations work with provider credentials unset. Add a
connection in Model settings or configure `OPENAI_API_KEY` before making model
calls. Restart both servers after changing `.env.local`.

## Manage model connections

The model control names the selected model. Saved connections can be selected,
edited, or removed. Removing a connection keeps its conversations readable.
Choose another connection to continue them. Changing providers or endpoints
requires entering the key again.

Removing a connection asks for confirmation before deleting its saved key.
Form validation focuses the field that needs attention. Changing providers or
credentials cancels outstanding model discovery.

[AI SDK](https://ai-sdk.dev/docs/introduction) adapters handle each provider's
request format. Eve resolves the provider inside its model-step lifecycle, so
durable execution records contain connection IDs rather than credentials.
Keys pass through this server to the selected provider. Use HTTPS for browser
access and hosted APIs. Local HTTP endpoints can be used for development.

Provider keys are encrypted with AES-256-GCM and bound to their owner. A signed,
HttpOnly cookie combines with the authenticated caller to scope connections and
history. Keep the cookie to retain access from that browser. The server operator
can access stored credentials, so use a server you trust and restrict provider-key
permissions and spending limits. Keys stay out of chat content and trace metadata.

Custom endpoints must match an allowed origin. `OPENAI_BASE` adds its origin
automatically. Add other trusted origins as a comma-separated list:

```dotenv
CHAT_MODEL_ORIGINS=https://api.example.com,https://models.example.com
```

The model form still needs the complete base URL, including a path such as `/v1`.
Redirects are rejected. The allowlist protects the server from arbitrary outbound
requests, so add origins you control or trust.

## Reopen a conversation

Use the left sidebar to start a chat or search previous conversations. Search and
collapse controls sit beside the wordmark. Collapsing keeps a narrow rail with the
brand mark, New chat, and Search. Select the mark to expand it again.
On smaller screens the sidebar opens as a drawer.
Each conversation's options menu offers rename, archive, or restore.
Reopening restores the chart images, guideline citations, and
saved guideline selection. Eve replays its persisted session events and follows
an in-flight response after a page reload. A changed catalog requires a new
guideline selection before continuing with its records.

[Effect](https://effect.website/docs/v3/runtime/) owns the app's scoped services,
typed failures, request timeouts, and tracing. Its SQLite client supplies
transactions, migrations, a prepared-statement cache, and write-ahead logging.
SQLite stores connection settings, conversation metadata, guideline selections,
and uploaded image previews. Eve owns the transcript and agent state.

`CHAT_DATA_DIR` overrides the platform-specific application-data directory for
`chartcoach-chat`. It contains `chat.sqlite` and the owner-readable
`credentials.key`. Preserve both together, plus Eve's `.eve/.workflow-data`
directory and sandbox storage, across server restarts. Use a SQLite-consistent
backup or stop the app before copying its database and key. Keep this data on a
private persistent volume. Deleting the key makes saved provider keys unreadable.

## Trace reviews

[Langfuse](https://langfuse.com/integrations/frameworks/eve) records the agent's
model calls, tools, timing, token usage, and cost. Set these server-side values in
`.env.local`, then restart the app:

```dotenv
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
LANGFUSE_BASE_URL=https://cloud.langfuse.com
```

Use your project's region or self-hosted URL. When `.env.local` exists in the app
directory, it supplies the complete Langfuse connection and takes precedence over
inherited credentials. Omitted local keys disable tracing, and a partial local pair
fails validation. Deployments with no local file use their server environment.

Find **ChartCoach conversation** in Langfuse. Each conversation keeps its Eve session ID and
trace identity across follow-ups, with separate turn, model, and tool branches.
Model observations include token totals and cached-token usage. Langfuse calculates
cost when it recognizes the model. Observations include the authenticated principal
when available, catalog identity, and selected guideline count. Authentication
attributes and the selected ID list stay out of telemetry metadata.

The initiating session captures catalog provenance for its model, tool, and image
observations:

| Field                 | Meaning                                                            |
| --------------------- | ------------------------------------------------------------------ |
| `catalogId`           | Catalog content identity                                           |
| `catalogReleaseId`    | Immutable release digest, when opened from a release               |
| `catalogPredicate`    | Full SQL selection submitted by the browser                        |
| `catalogSelectionId`  | SHA-256 of the catalog identity and sorted, resolved guideline IDs |
| `guidelineCount`      | Number of guidelines available to the agent                        |
| `modelConnectionId`   | Saved model connection selected for the current request            |
| `modelConnectionName` | Display name of the resolved connection                            |
| `modelProvider`       | Anthropic, OpenAI, Google, or OpenAI-compatible adapter            |
| `modelName`           | Model ID selected for the model step                               |
| `modelEndpointOrigin` | API scheme, host, and port                                         |
| `modelContextWindow`  | Configured context limit in tokens                                 |
| `modelManaged`        | Whether the connection uses the server's configured credentials    |

Model resolution records these fields for each step. Generation and tool traces
inherit the resolved model metadata alongside catalog provenance. API keys,
authorization headers, and endpoint paths, query strings, and credentials are
excluded from this metadata.

Direct clients that choose the full catalog record its full-table selection.
Retrieval continues against the frozen guideline IDs, with the original SQL kept
for inspection. Follow-ups retain the initiating release and selection.

Eve owns the OpenTelemetry pipeline through its experimental
`instrumentationProviders` setting in `agent/agent.ts` and the declarations under
`agent/instrumentation/`. It flushes buffered observations after execution steps,
including cancellation, and shuts down the exporter with the server. The exporter
keeps agent/model/tool spans and filters workflow and HTTP plumbing.

Content follows Eve's channel-audience policy. Local development captures prompts,
tool arguments/results, and responses. Hosted unknown/private channels export
metadata rather than conversation content. Treat the Langfuse project as a
destination for conversation data when content capture is enabled.

Each turn that uses a chart also records a **Chart image** observation in the same
Langfuse session. Langfuse uploads the original image, up to the app's 3 MiB limit,
and places a media reference in that observation. The image has its own trace with
turn metadata. Native model/tool traces keep Eve's 32 KiB content-attribute cap.
Retries within a running process reuse the turn's image observation. A server
restart can produce another observation, while Langfuse reuses the content-addressed media.

`LANGFUSE_TRACING_ENVIRONMENT` overrides the Vercel or Node environment label.
`LANGFUSE_RELEASE` identifies a deployment. Credentials remain server-side.

## Choose how to work

Ask for feedback, a chart recommendation, or an explanation of a design choice.
The agent chooses the workflow from your request. **Review**, **Recommend**, or
**Discuss** appears beside ChartCoach when its skill is loaded for that response.
Follow-up questions can activate a different workflow with the same guideline selection.

The three starter cards provide illustrative chart images and a data brief.
Choosing one attaches its image and fills an editable prompt. Review the draft,
then send it through the regular composer.

The agent always receives the canonical [core skill](../../skills/core/SKILL.md).
It uses Eve's native `load_skill` tool to load [visfeedback](../../skills/visfeedback/SKILL.md),
[visrec](../../skills/visrec/SKILL.md), or [discuss](../../skills/discuss/SKILL.md)
for the current request. These files own the retrieval, applicability, and
evidence policies. `agent/instructions.ts` binds them to the app's tools and
structured answer format.

The private `@chartcoach/skills` workspace package exposes the canonical files
to Eve's compiler. Builds embed the instructions and verify them against their
source files before checking relocated server startup.

Discussion and design recommendations explain the question or brief alongside
their citations. Chart reviews additionally classify each point as **Working well**,
**Improve**, or **Check**. Every recommendation must cite guidelines read in the
conversation.

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

The guideline panel shows search matches as they arrive and marks entries when read.
Primary guidelines appear as [Open Graph](https://ogp.me/) image cards in answer order.
Desktop places them in a collapsible card beside the conversation. On narrow screens,
open **Guidelines** above the conversation to inspect them in a bottom sheet.
Supporting and explored entries stay expandable, with catalog descriptions and links.
You can ask follow-up questions about the same
image, stop a response, or start a new chat.

Expand **Activity**, then a skill, search, or read action, to inspect its purpose,
search method, matched guidelines, and sources. The display groups tool calls
through assistant-ui's `MessagePrimitive.GroupedParts`. Vector-search details include
the embedding model and index profile.

The progress summary follows broad phases while individual calls remain available
in Activity. Labels crossfade in a stable row. Reduced-motion preferences make
these updates immediate.

Each new turn anchors to its question. Scroll to read the feedback or inspect
earlier messages.

The answer streams through Eve's authored `present_answer` tool. The interface
shows growing draft points once their citation IDs match successful reads.
The tool checks the complete answer against durable read history before accepting
it. Invalid references or structure produce actionable errors for the agent to
repair and resubmit. Accepted answers remain visible while the turn finishes.
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

## Choose your agent's guidelines

Open **Guidelines** in the sidebar to choose the guidelines your agent can use for feedback.
The settings occupy the main workspace. **Back to chat** returns to your conversation
and draft. Changes take effect when you choose **Use these guidelines**.
Drag the year-range handles or enter exact years. Include or exclude
authors and select source types. Blank fields keep the full range.

[Mosaic](https://uwdata.github.io/mosaic/) coordinates the linked views using
DuckDB-WASM in a browser worker. Facet counts reflect the other filters, so you
can compare alternatives before applying a selection. Scroll **Matching guidelines**
to explore the selection. The list fetches rows in batches, prefetches the next batch,
and virtualizes rendered rows. Hover or focus a title for its visual preview, or open
its link to read the guideline. Browsing preserves the full selection and facet counts.
Query results commit as non-urgent updates, keeping range and author controls responsive.

The first opening fetches verified Parquet and manifest bytes over authenticated
HTTPS and loads DuckDB's worker and WASM assets from this app. DuckDB also loads
its version-matched JSON extension from its configured extension repository.
Catalog exploration requires a browser with WebAssembly exception handling.
Draft filtering runs on your device. Leaving and reopening Guidelines reuses the
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
The CSS entrypoints contain browser resets, the shared brand palette, and native
view-transition selectors.

Components render state and dispatch commands. Hooks own request lifecycles and
interaction state. Root lint rules keep transport and server imports out of
`components/`.

| Responsibility                                                  | Owner                                                                                                                                       |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Eve and assistant-ui runtime composition                        | [use-chat-runtime.ts](chat/use-chat-runtime.ts)                                                                                             |
| Thread preparation, identity headers, and persistence           | [use-thread-session.ts](chat/use-thread-session.ts)                                                                                         |
| Transcript and evidence projection                              | [use-conversation.ts](chat/use-conversation.ts)                                                                                             |
| Model connection mutations and form lifecycle                   | [use-model-settings.ts](chat/use-model-settings.ts), [use-connection-form.ts](chat/use-connection-form.ts)                                  |
| File-drop listeners, source sheet, and virtual-list interaction | [use-file-drop.ts](chat/use-file-drop.ts), [use-evidence-panel.ts](chat/use-evidence-panel.ts), [use-match-list.ts](chat/use-match-list.ts) |

React Activity preserves the conversation and Guidelines views. The Eve stream
and browser catalog owner sit outside the hidden presentation subtrees, so switching
views preserves the chart, draft, scroll position, and loaded DuckDB worker.
Workspace navigation uses a short, type-scoped view transition. Streaming and
background catalog queries retain their own update lifecycle. Reduced-motion
preferences disable the transition animation.

[Recommendation](components/chat/recommendation.tsx) owns Streamdown's element
allowlist, inert authored links, streaming state, and StyleX typography. Provider
icons import their individual SVG components. The connection editor loads on demand.

Next.js uses StyleX's Babel and PostCSS plugins to compile styles and serve the
stylesheet. Tests use its bundler plugin to exercise compiled components.
The [chat runtime](chat/use-chat-runtime.ts) sends text and image parts through
Eve and consumes its native action stream. [present_answer](agent/tools/present_answer.ts)
validates the [shared answer contract](shared/answer.ts) against successful
guideline reads stored in Eve's durable session state. The client projects its
streamed input with the AI SDK's partial JSON parser and uses the accepted tool
result as the completed answer.

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
