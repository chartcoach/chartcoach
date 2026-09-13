import { defineAgent, defineDynamic } from "eve";

import { Effect } from "effect";
import { runApp } from "../lib/app/runtime";
import { resolveConnection } from "../lib/app/connections";
import { modelMetadata } from "../lib/app/model-metadata";
import { languageModel } from "../lib/app/providers";
import { modelSelectionSchema } from "../shared/preferences";

export default defineAgent({
  model: defineDynamic({
    events: {
      "step.started": async (_event, ctx) => {
        const attributes = ctx.session.auth.current?.attributes;

        const selection = modelSelectionSchema.safeParse({
          owner: attributes?.["chartcoach.owner"],
          threadId: attributes?.["chartcoach.thread"],
          connectionId: attributes?.["chartcoach.connection"],
        });

        if (!selection.success && attributes?.["chartcoach.thread"] !== undefined)
          throw new Error("Choose an available model connection before continuing.");

        const spanAttributes = {
          "langfuse.session.id": ctx.session.id,
          "session.id": ctx.session.id,
        };

        if (selection.success) Object.assign(spanAttributes, { "user.id": selection.data.owner });

        return runApp(
          Effect.gen(function* () {
            const resolved = selection.success
              ? yield* resolveConnection(selection.data.owner, selection.data.connectionId)
              : yield* resolveConnection("direct", "server");

            const connection = resolved.connection;

            const metadata = modelMetadata(connection, connection.baseURL);

            yield* Effect.annotateCurrentSpan(
              "langfuse.observation.metadata",
              JSON.stringify(metadata),
            );

            return {
              model: languageModel(connection, resolved.key),
              modelContextWindowTokens: connection.contextWindow,
            };
          }).pipe(
            Effect.withSpan("chat.resolve_model", {
              attributes: { "langfuse.session.id": ctx.session.id },
            }),
            Effect.annotateSpans(spanAttributes),
          ),
        );
      },
    },
  }),
  defaultTools: false,
  experimental: { instrumentationProviders: true },
  build: {
    externalDependencies: [
      "@chartcoach/catalog",
      "@lancedb/lancedb",
      "@huggingface/transformers",
      "@duckdb/node-api",
      "@effect/sql-sqlite-node",
    ],
  },
});
