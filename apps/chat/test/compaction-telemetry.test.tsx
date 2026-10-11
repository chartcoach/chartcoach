import { AsyncLocalStorage } from "node:async_hooks";
import {
  ROOT_CONTEXT,
  SpanStatusCode,
  context,
  trace,
  type Context,
  type ContextManager,
} from "@opentelemetry/api";
import {
  BasicTracerProvider,
  InMemorySpanExporter,
  SimpleSpanProcessor,
} from "@opentelemetry/sdk-trace-base";
import { generateText, type wrapLanguageModel } from "ai";
import { afterEach, beforeEach, expect, it, vi } from "vite-plus/test";
import { traceCompaction } from "../agent/compaction-telemetry";

type Model = ReturnType<typeof wrapLanguageModel>;

type Result = Awaited<ReturnType<Model["doGenerate"]>>;

let exporter: InMemorySpanExporter;

let provider: BasicTracerProvider;

beforeEach(() => {
  exporter = new InMemorySpanExporter();
  provider = new BasicTracerProvider({ spanProcessors: [new SimpleSpanProcessor(exporter)] });
  trace.setGlobalTracerProvider(provider);

  const storage = new AsyncLocalStorage<Context>();

  const manager: ContextManager = {
    active: () => storage.getStore() ?? ROOT_CONTEXT,
    with: (value, callback, thisArg, ...args) =>
      storage.run(value, () => callback.call(thisArg, ...args)),
    bind: (_value, target) => target,
    enable() {
      return this;
    },
    disable() {
      storage.disable();

      return this;
    },
  };

  context.setGlobalContextManager(manager);
});

afterEach(async () => {
  await provider.shutdown();
  trace.disable();
  context.disable();
});

function fixture(result: Result) {
  const stream = new ReadableStream({ start: (controller) => controller.close() });

  const model: Model = {
    specificationVersion: "v4",
    provider: "test.chat",
    modelId: "compaction-model",
    supportedUrls: {},
    doGenerate: vi.fn(async () => result),
    doStream: vi.fn(async () => ({ stream })),
  };

  return { model, stream };
}

function response(text = "Summary"): Result {
  return {
    content: [
      { type: "reasoning", text: "Retain the relevant chart observations." },
      { type: "text", text },
    ],
    finishReason: { unified: "stop", raw: "stop" },
    usage: {
      inputTokens: { total: 25, noCache: 18, cacheRead: 5, cacheWrite: 2 },
      outputTokens: { total: 7, text: 4, reasoning: 3 },
    },
    warnings: [],
    request: { body: "private-request-body" },
    response: { headers: { authorization: "private-response-header" }, body: "private-body" },
    providerMetadata: { private: { apiKey: "private-provider-metadata" } },
  };
}

it("captures private compaction IO and usage once while keeping its provided native parent", async () => {
  const summary = "Complete summary. ".repeat(2400);
  const system = "Keep all necessary context. ".repeat(1600);
  const { model } = fixture(response(summary));
  const root = provider.getTracer("eve.agent").startSpan("respond-to-user");

  const wrapped = traceCompaction(model, {
    "agent.run.id": "session-one",
    "gen_ai.conversation.id": "session-one",
    "session.id": "session-one",
    "agent.turn.id": "turn-one",
    "agent.step.index": 2,
    "langfuse.observation.metadata.modelConnectionId": "personal-connection",
  });

  const image = new Uint8Array([137, 80, 78, 71]);

  const result = await context.with(trace.setSpan(ROOT_CONTEXT, root), () =>
    generateText({
      model: wrapped,
      system,
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Remember this chart." },
            { type: "file", data: image, mediaType: "image/png" },
          ],
          providerOptions: { private: { token: "private-message-options" } },
        },
      ],
      headers: { authorization: "private-auth-header" },
      providerOptions: { private: { apiKey: "private-provider-key" } },
      telemetry: {
        functionId: "eve.compaction",
        recordInputs: false,
        recordOutputs: false,
        integrations: [],
      },
    }),
  );

  root.end();
  await provider.forceFlush();

  expect(result.text).toBe(summary);

  const spans = exporter
    .getFinishedSpans()
    .filter((span) => span.instrumentationScope.name === "chartcoach.compaction");

  expect(spans).toHaveLength(1);
  const span = spans[0]!;
  expect(span.name).toBe("compact-history");
  expect(span.parentSpanContext?.spanId).toBe(root.spanContext().spanId);
  expect(span.spanContext().traceId).toBe(root.spanContext().traceId);
  expect(span.attributes).toMatchObject({
    "agent.run.id": "session-one",
    "agent.turn.id": "turn-one",
    "agent.step.index": 2,
    "gen_ai.request.model": "compaction-model",
    "langfuse.observation.type": "generation",
    "langfuse.internal.is_app_root": false,
    "gen_ai.usage.input_tokens": 25,
    "gen_ai.usage.output_tokens": 7,
    "gen_ai.usage.cache_read.input_tokens": 5,
    "gen_ai.usage.cache_write.input_tokens": 2,
    "gen_ai.usage.reasoning.output_tokens": 3,
  });
  expect(JSON.parse(String(span.attributes["langfuse.observation.input"]))).toEqual([
    { role: "system", content: system },
    {
      role: "user",
      content: [
        { type: "text", text: "Remember this chart." },
        { type: "image_url", image_url: { url: "data:image/png;base64,iVBORw==" } },
      ],
    },
  ]);
  expect(JSON.parse(String(span.attributes["langfuse.observation.output"]))).toEqual([
    {
      role: "assistant",
      content: [{ type: "text", text: summary }],
      reasoning_content: "Retain the relevant chart observations.",
    },
  ]);
  expect(JSON.stringify(span.attributes)).not.toContain("private-");
});

it("passes streaming responses through without adding a generation", async () => {
  const { model, stream } = fixture(response());

  const result = await traceCompaction(model, {}).doStream({
    prompt: [{ role: "user", content: [{ type: "text", text: "Question" }] }],
  });

  expect(result.stream).toBe(stream);
  expect(exporter.getFinishedSpans()).toHaveLength(0);
});

it("preserves a provider failure while exporting only a safe error", async () => {
  const { model } = fixture(response());

  const error = Object.assign(new Error("private-key was rejected"), {
    request: { headers: { authorization: "private-auth-header" } },
  });

  model.doGenerate = vi.fn(async () => {
    throw error;
  });

  await expect(
    traceCompaction(model, { "agent.run.id": "failed-session" }).doGenerate({
      prompt: [{ role: "user", content: [{ type: "text", text: "History" }] }],
    }),
  ).rejects.toBe(error);
  await provider.forceFlush();
  const spans = exporter.getFinishedSpans();
  expect(spans).toHaveLength(1);
  expect(spans[0]!.status).toEqual({
    code: SpanStatusCode.ERROR,
    message: "Context compaction failed.",
  });
  expect(spans[0]!.attributes["langfuse.observation.output"]).toBe(
    JSON.stringify({ message: "Context compaction failed." }),
  );
  expect(JSON.stringify(spans[0]!.attributes)).not.toContain("private-");
});
