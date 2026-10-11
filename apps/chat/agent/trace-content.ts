import { z } from "zod";
import type { JsonValue, InstrumentationToolCallFailedEvent } from "eve/instrumentation";
import { maxChartBytes } from "../shared/attachment";

const imageDataSchema = z.union([z.instanceof(Uint8Array), z.instanceof(ArrayBuffer), z.string()]);

const call = {
  toolName: z.string(),
  toolCallId: z.string().optional(),
  callId: z.string().optional(),
};

const partSchema = z.discriminatedUnion("type", [
  z.object({ type: z.literal("text"), text: z.string() }),
  z.object({ type: z.literal("reasoning"), text: z.string() }),
  z.object({ type: z.literal("file"), data: imageDataSchema, mediaType: z.string() }),
  z.object({
    type: z.literal("image"),
    image: imageDataSchema,
    mediaType: z.string().default("image/png"),
  }),
  z.object({ type: z.literal("tool-call"), ...call, input: z.json() }),
  z.object({ type: z.literal("tool-result"), ...call, output: z.json() }),
  z.object({ type: z.literal("tool-error"), ...call, error: z.unknown() }),
]);

const messageSchema = z.object({
  role: z.string(),
  content: z.union([z.string(), z.array(z.unknown())]),
});

const errorSchema = z.union([
  z.string(),
  z.object({ message: z.string(), name: z.string().optional(), code: z.string().optional() }),
]);

const toolOutputSchema = z.discriminatedUnion("type", [
  z.object({ type: z.literal("text"), value: z.string() }),
  z.object({ type: z.literal("json"), value: z.json() }),
  z.object({ type: z.literal("error-text"), value: z.string() }),
  z.object({ type: z.literal("error-json"), value: z.json() }),
]);

type ImageData = z.infer<typeof imageDataSchema>;

type TraceError = InstrumentationToolCallFailedEvent["error"];

export type TraceMessage = {
  role: string;
  content: JsonValue;
  reasoning_content?: string;
  tool_calls?: JsonValue[];
  tool_call_id?: string;
  name?: string;
};

// Project content, never SDK request objects, headers, or provider credentials.
export function traceMessages(messages: readonly unknown[]): TraceMessage[] {
  return messages.flatMap<TraceMessage>((message) => {
    const parsed = messageSchema.safeParse(message);

    if (!parsed.success) return [];
    const { role, content } = parsed.data;
    const text = z.string().safeParse(content);

    if (text.success) return [{ role, content: text.data }];
    const values = z.array(z.unknown()).parse(content);
    const parts: JsonValue[] = [];
    const calls: JsonValue[] = [];
    const results: TraceMessage[] = [];
    const reasoning: string[] = [];

    for (const value of values) {
      const part = partSchema.safeParse(value);

      if (!part.success) continue;
      const p = part.data;

      switch (p.type) {
        case "text":
          parts.push({ type: "text", text: p.text });
          break;
        case "reasoning":
          reasoning.push(p.text);
          break;
        case "file":
        case "image": {
          const url = imageDataUri(p.type === "file" ? p.data : p.image, p.mediaType);

          if (url) parts.push({ type: "image_url", image_url: { url } });
          break;
        }

        case "tool-call": {
          const id = z.string().safeParse(p.toolCallId ?? p.callId);

          if (id.success)
            calls.push({
              id: id.data,
              type: "function",
              function: { name: p.toolName, arguments: JSON.stringify(p.input) },
            });
          break;
        }

        case "tool-result":
        case "tool-error": {
          const id = z.string().safeParse(p.toolCallId ?? p.callId);

          if (!id.success) break;

          const wrapped =
            p.type === "tool-result" ? toolOutputSchema.safeParse(p.output) : undefined;

          const output =
            p.type === "tool-error"
              ? errorContent(p.error)
              : wrapped?.success
                ? wrapped.data.value
                : p.output;

          results.push({
            role: "tool",
            tool_call_id: id.data,
            name: p.toolName,
            content: JSON.stringify(output),
          });
          break;
        }
      }
    }

    if (role === "tool") return results;
    const output: TraceMessage = { role, content: parts };

    if (reasoning.length) output.reasoning_content = reasoning.join("\n");

    if (calls.length) output.tool_calls = calls;

    return [output, ...results];
  });
}

export function errorContent(value: TraceError): JsonValue {
  if (value instanceof Error) return { name: value.name, message: value.message };

  return errorSchema.safeParse(value).data ?? { message: "The operation failed." };
}

function imageDataUri(data: ImageData, mediaType: string): string | undefined {
  if (!["image/png", "image/jpeg", "image/webp"].includes(mediaType)) return;

  if (data instanceof Uint8Array || data instanceof ArrayBuffer) {
    if (data.byteLength === 0 || data.byteLength > maxChartBytes) return;

    return `data:${mediaType};base64,${Buffer.from(data instanceof ArrayBuffer ? new Uint8Array(data) : data).toString("base64")}`;
  }

  const prefix = `data:${mediaType};base64,`;
  const base64 = data.startsWith(prefix) ? data.slice(prefix.length) : data;

  if (
    !base64.length ||
    base64.length > Math.ceil(maxChartBytes / 3) * 4 ||
    base64.length % 4 !== 0 ||
    !/^[A-Za-z0-9+/]*={0,2}$/.test(base64)
  )
    return;
  const bytes = Buffer.from(base64, "base64");

  return bytes.byteLength > 0 && bytes.byteLength <= maxChartBytes ? prefix + base64 : undefined;
}
