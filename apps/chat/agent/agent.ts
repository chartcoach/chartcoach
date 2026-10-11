import { defineAgent, defineDynamic } from "eve";

import { Effect } from "effect";
import { runApp } from "../lib/app/runtime";
import { resolveConnection } from "../lib/app/connections";
import { langfuseTracingEnabled } from "../lib/env";
import { traceCompaction } from "./compaction-telemetry";
import { resolvedModelTrace } from "./model-trace-state";
import { traceContext } from "./trace-context";
import { modelMetadata } from "../lib/app/model-metadata";
import { languageModel } from "../lib/app/providers";
import { z } from "zod";
import { modelSelectionSchema } from "../shared/preferences";

export default defineAgent({
  model: defineDynamic({
    events: {
      "step.started": async (event, ctx) => {
        const attributes = ctx.session.auth.current?.attributes;

        const selection = modelSelectionSchema.safeParse({
          owner: attributes?.["chartcoach.owner"],
          threadId: attributes?.["chartcoach.thread"],
          connectionId: attributes?.["chartcoach.connection"],
        });

        if (!selection.success && attributes?.["chartcoach.thread"] !== undefined)
          throw new Error("Choose an available model connection before continuing.");

        const step = z
          .object({
            data: z.object({ turnId: z.string(), stepIndex: z.number(), sequence: z.number() }),
          })
          .parse(event).data;

        const spanAttributes = {
          "langfuse.session.id": ctx.session.id,
          "session.id": ctx.session.id,
          "agent.turn.id": step.turnId,
          "agent.step.index": step.stepIndex,
        };

        if (selection.success) Object.assign(spanAttributes, { "user.id": selection.data.owner });

        const resolvedModel = await runApp(
          Effect.gen(function* () {
            const resolved = selection.success
              ? yield* resolveConnection(selection.data.owner, selection.data.connectionId)
              : yield* resolveConnection("direct", "server");

            const connection = resolved.connection;

            const metadata = modelMetadata(connection, connection.baseURL);

            const model = languageModel(connection, resolved.key);

            return {
              model,
              metadata,
              modelContextWindowTokens: connection.contextWindow,
            };
          }).pipe(
            Effect.withSpan("chat.resolve_model", {
              attributes: { "langfuse.session.id": ctx.session.id },
            }),
            Effect.annotateSpans(spanAttributes),
          ),
        );

        if (!langfuseTracingEnabled)
          return {
            model: resolvedModel.model,
            modelContextWindowTokens: resolvedModel.modelContextWindowTokens,
          };

        resolvedModelTrace.update(() => ({
          sessionId: ctx.session.id,
          turnId: step.turnId,
          metadata: resolvedModel.metadata,
        }));

        const { userId, ...metadata } = traceContext({
          session: ctx.session,
          turn: { id: step.turnId, sequence: step.sequence },
        });

        const compactionAttributes = {
          ...spanAttributes,
          "agent.run.id": ctx.session.id,
          "gen_ai.conversation.id": ctx.session.id,
          ...Object.fromEntries(
            Object.entries({ ...metadata, ...resolvedModel.metadata })
              .filter(([, value]) => value !== undefined)
              .map(([key, value]) => [`langfuse.observation.metadata.${key}`, value]),
          ),
        };

        if (userId !== undefined) Object.assign(compactionAttributes, { "user.id": userId });

        return {
          model: traceCompaction(resolvedModel.model, compactionAttributes),
          modelContextWindowTokens: resolvedModel.modelContextWindowTokens,
        };
      },
    },
  }),
  defaultTools: false,
  build: {
    externalDependencies: [
      "@chartcoach/catalog",
      "@lancedb/lancedb",
      "@huggingface/transformers",
      "@duckdb/node-api",
    ],
  },
});
