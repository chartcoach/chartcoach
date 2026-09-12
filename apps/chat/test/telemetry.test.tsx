import { ROOT_CONTEXT, trace } from "@opentelemetry/api";
import {
  BasicTracerProvider,
  InMemorySpanExporter,
  SimpleSpanProcessor,
} from "@opentelemetry/sdk-trace-base";
import { expect, it } from "vite-plus/test";
import { LangfuseProcessor, traceContext } from "../agent/telemetry";
import type { InstrumentationRuntimeContextInput } from "eve/instrumentation";
import { modelMetadata } from "../lib/app/model-metadata";

const connectionMetadata = (sessionId: string) =>
  modelMetadata(
    {
      id: sessionId,
      name: "Team gateway",
      provider: "compatible",
      model: `model-${sessionId}`,
      contextWindow: 64000,
      managed: false,
    },
    "https://user:password@gateway.example/private-path?api_key=private-key#fragment",
  );

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

      const resolution = provider.getTracer("chartcoach.app").startSpan(
        "chat.resolve_model",
        {
          attributes: {
            "langfuse.session.id": sessionId,
            "langfuse.observation.metadata": JSON.stringify(connectionMetadata(sessionId)),
          },
        },
        ROOT_CONTEXT,
      );

      resolution.end();

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
    expect(spans).toHaveLength(8);

    for (const span of original.getFinishedSpans()) {
      expect(span.attributes["gen_ai.usage.input_tokens"]).toBeUndefined();
    }

    for (const sessionId of ["review-one", "review-two"]) {
      const session = spans.filter((span) => span.attributes["session.id"] === sessionId);
      expect(session).toHaveLength(4);
      expect(
        new Set(
          session
            .filter((span) => span.name !== "chat.resolve_model")
            .map((span) => span.spanContext().traceId),
        ).size,
      ).toBe(1);
      const model = session.find((span) => span.name === "chat test-model")!;
      const tool = session.find((span) => span.name === "execute_tool read_guidelines")!;
      expect(tool.parentSpanContext?.spanId).toBe(model.spanContext().spanId);
      expect(model.attributes).toMatchObject({
        "langfuse.trace.name": "ChartCoach conversation",
        "user.id": "reviewer",
        "gen_ai.usage.input_tokens": 20,
        "gen_ai.usage.output_tokens": 5,
      });
      expect(JSON.parse(String(model.attributes["langfuse.trace.metadata"]))).toEqual({
        catalogId: "catalog-digest",
        guidelineCount: 3,
        ...connectionMetadata(sessionId),
      });
      expect(JSON.parse(String(tool.attributes["langfuse.trace.metadata"]))).toMatchObject(
        connectionMetadata(sessionId),
      );
    }

    expect(new Set(spans.map((span) => span.spanContext().traceId)).size).toBe(4);
  } finally {
    await provider.shutdown();
  }
});

it("projects provider configuration without credentials or endpoint paths", () => {
  const value = {
    id: "custom",
    name: "Team gateway",
    provider: "compatible" as const,
    model: "vision-model",
    contextWindow: 64000,
    managed: false,
    apiKey: "never-log-this-key",
  };

  expect(
    modelMetadata(value, "https://user:secret@gateway.example/private-token?key=secret#secret"),
  ).toEqual({
    modelConnectionId: "custom",
    modelConnectionName: "Team gateway",
    modelProvider: "compatible",
    modelName: "vision-model",
    modelContextWindow: 64000,
    modelManaged: false,
    modelEndpointOrigin: "https://gateway.example",
  });
});

it("keeps each generation's resolved model while later steps change connections", async () => {
  const exporter = new InMemorySpanExporter();

  const provider = new BasicTracerProvider({
    spanProcessors: [
      new LangfuseProcessor({
        exporter,
        publicKey: "pk-test",
        secretKey: "sk-test",
        mediaUploadEnabled: false,
      }),
    ],
  });

  try {
    const root = provider
      .getTracer("eve.agent")
      .startSpan("agent.session", { attributes: { "agent.session.id": "changing-model" } });

    for (const id of ["first", "second"]) {
      const resolution = provider.getTracer("chartcoach.app").startSpan("chat.resolve_model", {
        attributes: {
          "langfuse.session.id": "changing-model",
          "langfuse.observation.metadata": JSON.stringify(connectionMetadata(id)),
        },
      });

      resolution.end();

      const generation = provider
        .getTracer("eve.agent")
        .startSpan(
          `chat ${id}`,
          { attributes: { "gen_ai.operation.name": "chat", "agent.session.id": "changing-model" } },
          trace.setSpan(ROOT_CONTEXT, root),
        );

      generation.end();
    }

    root.end();
    await provider.forceFlush();
    expect(
      exporter
        .getFinishedSpans()
        .filter((span) => span.attributes["gen_ai.operation.name"] === "chat")
        .map((span) => JSON.parse(String(span.attributes["langfuse.trace.metadata"])).modelName),
    ).toEqual(["model-first", "model-second"]);
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
  expect(
    traceContext({
      ...input,
      session: {
        ...session,
        auth: {
          ...session.auth,
          current: {
            ...session.auth.initiator!,
            attributes: { "chartcoach.connection": "my-model" },
          },
        },
      },
    }),
  ).toMatchObject({
    modelConnectionId: "my-model",
    catalogId: "a".repeat(64),
    catalogReleaseId: "b".repeat(64),
  });
});
