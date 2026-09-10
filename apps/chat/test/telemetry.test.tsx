import { ROOT_CONTEXT, trace } from "@opentelemetry/api";
import {
  BasicTracerProvider,
  InMemorySpanExporter,
  SimpleSpanProcessor,
} from "@opentelemetry/sdk-trace-base";
import { expect, it } from "vite-plus/test";
import { LangfuseProcessor, traceContext } from "../agent/telemetry";
import type { InstrumentationRuntimeContextInput } from "eve/instrumentation";

it("exports session-scoped model and tool trees while omitting orchestration spans", async () => {
  const exporter = new InMemorySpanExporter();
  const original = new InMemorySpanExporter();
  const provider = new BasicTracerProvider({
    spanProcessors: [
      new LangfuseProcessor({
        exporter,
        publicKey: "pk-lf-test",
        secretKey: "sk-lf-test",
        mediaUploadEnabled: false,
      }),
      new SimpleSpanProcessor(original),
    ],
  });
  try {
    const tracer = provider.getTracer("eve.agent");
    const conversations = ["review-one", "review-two"].map((sessionId) => {
      const root = tracer.startSpan("agent.session", {
        attributes: { "agent.session.id": sessionId },
      });
      const model = tracer.startSpan(
        "chat test-model",
        {
          attributes: {
            "gen_ai.operation.name": "chat",
            "ai.settings.context.eve.session.id": sessionId,
            "ai.settings.context.userId": "reviewer",
            "ai.settings.context.catalogId": "catalog-digest",
            "ai.settings.context.guidelineCount": 3,
          },
        },
        trace.setSpan(ROOT_CONTEXT, root),
      );
      return { root, model };
    });
    for (const { root, model } of conversations) {
      const tool = tracer.startSpan(
        "execute_tool read_guidelines",
        {
          attributes: { "gen_ai.operation.name": "execute_tool" },
        },
        trace.setSpan(ROOT_CONTEXT, trace.wrapSpanContext(model.spanContext())),
      );
      tool.end();
      model.setAttributes({ "agent.usage.input_tokens": 20, "agent.usage.output_tokens": 5 });
      model.end();
      root.end();
    }
    provider.getTracer("workflow").startSpan("step.invoke").end();
    provider.getTracer("@vercel/otel/fetch").startSpan("GET catalog").end();
    await provider.forceFlush();
    const spans = exporter.getFinishedSpans();
    expect(spans).toHaveLength(6);
    for (const span of original.getFinishedSpans()) {
      expect(span.attributes["gen_ai.usage.input_tokens"]).toBeUndefined();
    }
    for (const sessionId of ["review-one", "review-two"]) {
      const session = spans.filter((span) => span.attributes["session.id"] === sessionId);
      expect(session).toHaveLength(3);
      expect(new Set(session.map((span) => span.spanContext().traceId)).size).toBe(1);
      const model = session.find((span) => span.name === "chat test-model")!;
      const tool = session.find((span) => span.name === "execute_tool read_guidelines")!;
      expect(tool.parentSpanContext?.spanId).toBe(model.spanContext().spanId);
      expect(model.attributes).toMatchObject({
        "langfuse.trace.name": "Chart review",
        "user.id": "reviewer",
        "gen_ai.usage.input_tokens": 20,
        "gen_ai.usage.output_tokens": 5,
      });
      expect(JSON.parse(String(model.attributes["langfuse.trace.metadata"]))).toEqual({
        catalogId: "catalog-digest",
        guidelineCount: 3,
      });
    }
    expect(new Set(spans.map((span) => span.spanContext().traceId)).size).toBe(2);
  } finally {
    await provider.shutdown();
  }
});

it("projects catalog identity and principal identity without exporting authentication attributes", () => {
  const session: InstrumentationRuntimeContextInput["session"] = {
    id: "review-one",
    auth: {
      current: null,
      initiator: {
        principalId: "reviewer",
        principalType: "user",
        authenticator: "test",
        attributes: {
          secret: "private",
          "chartcoach.selection": JSON.stringify({
            catalogId: "a".repeat(64),
            ids: ["direct-labels"],
          }),
          "chartcoach.release": "b".repeat(64),
          "chartcoach.predicate": "SELECT id FROM catalog_entries WHERE id = 'direct-labels'",
        },
      },
    },
  };
  const input: InstrumentationRuntimeContextInput = {
    session,
    channel: { kind: "channel:eve", metadata: { audience: "unknown" } },
    step: { index: 0 },
    turn: { id: "turn-one", sequence: 0 },
    modelInput: { instructions: undefined, messages: [] },
  };
  expect(traceContext(input)).toEqual({
    userId: "reviewer",
    catalogId: "a".repeat(64),
    guidelineCount: 1,
    catalogReleaseId: "b".repeat(64),
    catalogPredicate: "SELECT id FROM catalog_entries WHERE id = 'direct-labels'",
    catalogSelectionId: expect.stringMatching(/^[a-f0-9]{64}$/),
  });
  expect(
    traceContext({ ...input, session: { ...session, auth: { current: null, initiator: null } } }),
  ).toEqual({});
});
