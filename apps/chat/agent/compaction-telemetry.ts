import { SpanKind, SpanStatusCode, trace, type Attributes } from "@opentelemetry/api";
import { wrapLanguageModel } from "ai";
import { traceMessages } from "./trace-content";

type Model = Parameters<typeof wrapLanguageModel>[0]["model"];

// Eve streams normal responses and calls doGenerate for context compaction.
// The resolver supplies safe identity and model metadata for this exact step.
export function traceCompaction(model: Model, attributes: Attributes) {
  return wrapLanguageModel({
    model,
    middleware: {
      specificationVersion: "v4",
      async wrapGenerate({ doGenerate, params, model: resolvedModel }) {
        return trace.getTracer("chartcoach.compaction").startActiveSpan(
          "compact-history",
          {
            kind: SpanKind.CLIENT,
            attributes: {
              ...attributes,
              "gen_ai.operation.name": "chat",
              "gen_ai.provider.name": resolvedModel.provider,
              "gen_ai.request.model": resolvedModel.modelId,
              "langfuse.observation.type": "generation",
              "langfuse.internal.is_app_root": false,
            },
          },
          async (span) => {
            try {
              span.setAttribute(
                "langfuse.observation.input",
                JSON.stringify(
                  traceMessages(
                    params.prompt.map((message) =>
                      message.role === "system"
                        ? message
                        : {
                            ...message,
                            content: message.content.map((part) =>
                              part.type === "file" && part.data.type === "data"
                                ? { ...part, data: part.data.data }
                                : part,
                            ),
                          },
                    ),
                  ),
                ),
              );
              const result = await doGenerate();
              span.setAttribute(
                "langfuse.observation.output",
                JSON.stringify(traceMessages([{ role: "assistant", content: result.content }])),
              );
              span.setAttribute("gen_ai.response.finish_reasons", [result.finishReason.unified]);

              // Eve rejects empty summaries after the model call returns. Mark
              // the observation without changing its result or failure path.
              if (!result.content.some((part) => part.type === "text" && part.text.trim().length))
                span.setStatus({
                  code: SpanStatusCode.ERROR,
                  message: "Context compaction returned an empty summary.",
                });

              const usage = result.usage;

              const counts = {
                "gen_ai.usage.input_tokens": usage.inputTokens.total,
                "gen_ai.usage.output_tokens": usage.outputTokens.total,
                "gen_ai.usage.cache_read.input_tokens": usage.inputTokens.cacheRead,
                "gen_ai.usage.cache_write.input_tokens": usage.inputTokens.cacheWrite,
                "gen_ai.usage.reasoning.output_tokens": usage.outputTokens.reasoning,
                "ai.usage.inputTokenDetails.noCacheTokens": usage.inputTokens.noCache,
                "ai.usage.outputTokenDetails.textTokens": usage.outputTokens.text,
              };

              for (const [key, value] of Object.entries(counts))
                if (value !== undefined) span.setAttribute(key, value);

              return result;
            } catch (error) {
              // Provider errors can carry request headers, bodies, and keys.
              // Preserve the thrown value for Eve without exporting that object.
              const message = "Context compaction failed.";
              span.setStatus({ code: SpanStatusCode.ERROR, message });
              span.setAttribute("langfuse.observation.output", JSON.stringify({ message }));
              throw error;
            } finally {
              span.end();
            }
          },
        );
      },
    },
  });
}
