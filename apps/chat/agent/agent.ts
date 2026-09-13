import { createOpenAI } from "@ai-sdk/openai";
import { defineAgent, defineDynamic } from "eve";
import { env } from "../lib/env";
import { Effect } from "effect";
import { runApp } from "../lib/app/runtime";
import { managedConnection, resolveConnection } from "../lib/app/connections";
import { modelMetadata } from "../lib/app/model-metadata";
import { languageModel } from "../lib/app/providers";
import { modelSelectionSchema } from "../shared/preferences";

const openai = createOpenAI({
  baseURL: env.OPENAI_BASE,
  apiKey: env.OPENAI_API_KEY,
});

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

        if (!selection.success) {
          if (attributes?.["chartcoach.thread"] !== undefined)
            throw new Error("Choose an available model connection before continuing.");
        }

        const spanAttributes = {
          "langfuse.session.id": ctx.session.id,
          "session.id": ctx.session.id,
        };

        if (selection.success) Object.assign(spanAttributes, { "user.id": selection.data.owner });

        return runApp(
          Effect.gen(function* () {
            const resolved = selection.success
              ? yield* resolveConnection(selection.data.owner, selection.data.connectionId)
              : undefined;

            const connection = resolved?.connection ?? managedConnection();

            if (!connection)
              throw new Error("Choose an available model connection before continuing.");

            const metadata = modelMetadata(
              connection,
              connection.managed
                ? (env.OPENAI_BASE ?? "https://api.openai.com")
                : connection.baseURL,
            );

            yield* Effect.annotateCurrentSpan(
              "langfuse.observation.metadata",
              JSON.stringify(metadata),
            );

            return {
              model:
                resolved && !connection.managed
                  ? languageModel(connection, resolved.key)
                  : openai.chat(env.OPENAI_MODEL),
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
