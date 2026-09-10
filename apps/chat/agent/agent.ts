import { createOpenAI } from "@ai-sdk/openai";
import { defineAgent, defineDynamic } from "eve";
import { env } from "../lib/env";
import { Effect } from "effect";
import { runApp } from "../lib/app/runtime";
import { resolveConnection } from "../lib/app/connections";
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
          return { model: openai.chat(env.OPENAI_MODEL), modelContextWindowTokens: 128_000 };
        }
        const { owner, connectionId } = selection.data;
        return runApp(
          Effect.gen(function* () {
            const { connection, key } = yield* resolveConnection(owner, connectionId);
            return {
              model: connection.managed
                ? openai.chat(env.OPENAI_MODEL)
                : languageModel(connection, key),
              modelContextWindowTokens: connection.contextWindow,
            };
          }).pipe(
            Effect.withSpan("chat.resolve_model", {
              attributes: { "langfuse.session.id": ctx.session.id },
            }),
            Effect.annotateSpans({
              "langfuse.session.id": ctx.session.id,
              "session.id": ctx.session.id,
              "user.id": owner,
            }),
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
