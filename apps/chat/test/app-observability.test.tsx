import { mkdtemp, rm } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import {
  BasicTracerProvider,
  InMemorySpanExporter,
  SimpleSpanProcessor,
} from "@opentelemetry/sdk-trace-base";
import { Effect, Redacted } from "effect";
import * as OtelTracer from "@effect/opentelemetry/Tracer";
import { expect, it, vi } from "vite-plus/test";
import { createAppRuntime } from "../lib/app/runtime";
import { listProviderModels } from "../lib/app/providers";
import { saveConnection } from "../lib/app/connections";
import { LangfuseProcessor } from "../agent/telemetry";

it("exports Effect operations to the existing trace while redacting provider credentials", async () => {
  const directory = await mkdtemp(join(tmpdir(), "chartcoach-app-traces-"));
  const exported = new InMemorySpanExporter();
  const original = new InMemorySpanExporter();

  const provider = new BasicTracerProvider({
    spanProcessors: [
      new SimpleSpanProcessor(original),
      new LangfuseProcessor({
        exporter: exported,
        publicKey: "pk-test",
        secretKey: "sk-test",
        mediaUploadEnabled: false,
      }),
    ],
  });

  const tracer = provider.getTracer("chartcoach.app");
  const runtime = createAppRuntime(directory, tracer);
  const parent = tracer.startSpan("test-request");
  vi.stubGlobal("fetch", async () =>
    Response.json({
      models: [{ name: "models/vision", supportedGenerationMethods: ["generateContent"] }],
    }),
  );

  try {
    await runtime.runPromise(
      saveConnection("alice", {
        provider: "google",
        name: "Gemini",
        model: "vision",
        contextWindow: 32_000,
        apiKey: "private-provider-key",
      }).pipe(OtelTracer.withSpanContext(parent.spanContext())),
    );
    await runtime.runPromise(
      listProviderModels(
        { provider: "google", name: "Gemini", model: "vision", contextWindow: 32_000 },
        Redacted.make("private-provider-key"),
      ).pipe(
        OtelTracer.withSpanContext(parent.spanContext()),
        Effect.annotateSpans({ "langfuse.session.id": "session-test" }),
      ),
    );
    parent.end();
    await provider.forceFlush();
    const spans = original.getFinishedSpans();
    const discovery = spans.find((span) => span.name === "provider.list_models");
    expect(discovery?.parentSpanContext?.spanId).toBe(parent.spanContext().spanId);
    expect(exported.getFinishedSpans().some((span) => span.name === "provider.list_models")).toBe(
      true,
    );
    expect(spans.some((span) => span.attributes["http.request.header.x-goog-api-key"])).toBe(true);
    expect(
      JSON.stringify(spans.map((span) => ({ attributes: span.attributes, events: span.events }))),
    ).not.toContain("private-provider-key");
  } finally {
    vi.unstubAllGlobals();
    await runtime.dispose();
    await provider.shutdown();
    await rm(directory, { recursive: true, force: true });
  }
});
