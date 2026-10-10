import { createHash } from "node:crypto";
import { ROOT_CONTEXT, trace, type Tracer } from "@opentelemetry/api";
import { defineInstrumentation, type ProviderDefinition } from "eve/instrumentation";
import { z } from "zod";
import { maxChartBytes } from "../shared/attachment";
import { catalogTraceSchema } from "./telemetry";

const imageDataSchema = z.union([z.instanceof(Uint8Array), z.instanceof(ArrayBuffer), z.string()]);

type ImageData = z.infer<typeof imageDataSchema>;

const imageSchema = z.object({
  type: z.literal("file"),
  mediaType: z.enum(["image/png", "image/jpeg", "image/webp"]),
  data: imageDataSchema,
});

const messageSchema = z.object({ role: z.literal("user"), content: z.array(z.unknown()) });

export function mediaInstrumentation(tracer?: Tracer) {
  const observed = new Map<string, string>();

  const release = ({ sessionId }: { sessionId: string }) => {
    observed.delete(sessionId);
  };

  const definition = {
    tracePolicy: () => true,
    events: {
      "model.call.started"(event) {
        if (!event.input || observed.get(event.scope.sessionId) === event.scope.turnId) return;

        for (const message of [...event.input.messages].reverse()) {
          const parsed = messageSchema.safeParse(message);

          if (!parsed.success) continue;

          for (const part of [...parsed.data.content].reverse()) {
            const image = imageSchema.safeParse(part);

            if (!image.success) continue;
            const bytes = imageBytes(image.data.data, image.data.mediaType);

            if (!bytes) return;
            const digest = createHash("sha256").update(bytes).digest("hex");

            const span = (tracer ?? trace.getTracer("chartcoach.media")).startSpan(
              "Chart image",
              {
                attributes: {
                  "chartcoach.media": true,
                  "langfuse.trace.name": "Chart image",
                  "gen_ai.conversation.id": event.scope.sessionId,
                  "langfuse.observation.type": "span",
                  "langfuse.observation.input": JSON.stringify({
                    image: `data:${image.data.mediaType};base64,${bytes.toString("base64")}`,
                  }),
                  "langfuse.observation.metadata": JSON.stringify({
                    turnId: event.scope.turnId,
                    stepIndex: event.scope.stepIndex,
                    attemptIndex: event.scope.attemptIndex,
                    mediaType: image.data.mediaType,
                    bytes: bytes.byteLength,
                    sha256: digest,
                  }),
                },
              },
              ROOT_CONTEXT,
            );

            const userId = z.string().safeParse(event.runtimeContext?.userId);

            if (userId.success) span.setAttribute("user.id", userId.data);
            const catalog = catalogTraceSchema.safeParse(event.runtimeContext);

            if (catalog.success)
              span.setAttribute("langfuse.trace.metadata", JSON.stringify(catalog.data));
            span.end();
            // Waiting sessions and retries in this process reuse the turn's observation.
            observed.delete(event.scope.sessionId);
            observed.set(event.scope.sessionId, event.scope.turnId);

            if (observed.size > 1024) {
              const oldest = observed.keys().next().value;

              if (oldest !== undefined) observed.delete(oldest);
            }

            return;
          }
        }
      },
      "session.completed": release,
      "session.failed": release,
    },
    shutdown() {
      observed.clear();
    },
  } satisfies ProviderDefinition;

  return { ...defineInstrumentation(definition), ...definition };
}

function imageBytes(data: ImageData, mediaType: string): Buffer | undefined {
  if (data instanceof Uint8Array || data instanceof ArrayBuffer) {
    if (data.byteLength === 0 || data.byteLength > maxChartBytes) return;

    return Buffer.from(data instanceof ArrayBuffer ? new Uint8Array(data) : data);
  }

  const prefix = `data:${mediaType};base64,`;
  const base64 = data.startsWith(prefix) ? data.slice(prefix.length) : data;

  if (
    base64.length === 0 ||
    base64.length > Math.ceil(maxChartBytes / 3) * 4 ||
    base64.length % 4 !== 0 ||
    !/^[A-Za-z0-9+/]*={0,2}$/.test(base64)
  )
    return;
  const bytes = Buffer.from(base64, "base64");

  return bytes.byteLength > 0 && bytes.byteLength <= maxChartBytes ? bytes : undefined;
}
