import { ROOT_CONTEXT, trace } from "@opentelemetry/api";
import {
  BasicTracerProvider,
  InMemorySpanExporter,
  SimpleSpanProcessor,
} from "@opentelemetry/sdk-trace-base";
import { z } from "zod";
import { expect, it } from "vite-plus/test";
import { LangfuseProcessor } from "../agent/telemetry";
import { traceContext } from "../agent/trace-context";
import type { InstrumentationRuntimeContextInput } from "eve/instrumentation";
import { modelMetadata } from "../lib/app/model-metadata";
import { resolvedModelTrace } from "../agent/model-trace-state";

// SAFETY: The pinned Eve container exercises the same named state and ALS
// boundary used by separately bundled model and instrumentation declarations.
const { ContextContainer, contextStorage } = (await import(
  new URL("./context/container.js", import.meta.resolve("eve")).href
)) as typeof import("../node_modules/eve/dist/src/context/container.js");

function inEveContext<A>(run: () => A): A {
  return contextStorage.run(new ContextContainer(), run);
}

function runtimeInput(sessionId: string, turnId = "turn-one", stepIndex = 0) {
  return {
    session: { id: sessionId, auth: { current: null, initiator: null } },
    channel: { kind: "channel:eve", metadata: { audience: "private" } },
    step: { index: stepIndex },
    turn: { id: turnId, sequence: 0 },
    modelInput: { instructions: undefined, messages: [] },
  } satisfies InstrumentationRuntimeContextInput;
}

function runtimeAttributes(value: Record<string, string | number | boolean | undefined>) {
  return Object.fromEntries(
    Object.entries(value)
      .filter(([, item]) => item !== undefined)
      .map(([key, item]) => [`ai.settings.context.${key}`, item]),
  );
}

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

  const processor = new LangfuseProcessor({
    exporter,
    publicKey: "pk-lf-test",
    secretKey: "sk-lf-test",
    mediaUploadEnabled: false,
  });

  const provider = new BasicTracerProvider({
    spanProcessors: [processor, new SimpleSpanProcessor(original)],
  });

  try {
    const tracer = provider.getTracer("eve.agent");

    const conversations = ["review-one", "review-two"].map((sessionId) => {
      const root = tracer.startSpan("invoke_agent chartcoach", {
        attributes: {
          "gen_ai.operation.name": "invoke_agent",
          "agent.run.id": sessionId,
          "gen_ai.conversation.id": sessionId,
          "agent.turn.id": "turn-one",
          "agent.step.index": 0,
        },
      });

      const step = tracer.startSpan(
        "agent.step",
        { attributes: { "agent.step.index": 0 } },
        trace.setSpan(ROOT_CONTEXT, root),
      );

      const model = tracer.startSpan(
        "chat test-model",
        {
          attributes: {
            "gen_ai.operation.name": "chat",
            "agent.run.id": sessionId,
            "gen_ai.conversation.id": sessionId,
            "ai.settings.context.userId": "reviewer",
            "ai.settings.context.catalogId": "catalog-digest",
            "ai.settings.context.guidelineCount": 3,
            ...runtimeAttributes(connectionMetadata(sessionId)),
          },
        },
        trace.setSpan(ROOT_CONTEXT, step),
      );

      return { root, model, step, sessionId };
    });

    for (const { root, model, step, sessionId } of conversations) {
      const tool = tracer.startSpan(
        "execute_tool read_guidelines",
        {
          attributes: { "gen_ai.operation.name": "execute_tool" },
        },
        trace.setSpan(ROOT_CONTEXT, trace.wrapSpanContext(step.spanContext())),
      );

      tool.end();
      model.setAttributes({ "gen_ai.usage.input_tokens": 20, "gen_ai.usage.output_tokens": 5 });
      model.end();
      step.end();
      root.end();
      processor.payloads.capture({
        type: "session.waiting",
        idempotencyKey: "waiting",
        sessionId: sessionId,
        turnId: "turn-one",
      });
    }

    provider.getTracer("workflow").startSpan("step.invoke").end();
    provider.getTracer("@vercel/otel/fetch").startSpan("GET catalog").end();
    provider.getTracer("chartcoach.app").startSpan("chat.resolve_model").end();
    await provider.forceFlush();
    const spans = exporter.getFinishedSpans();
    expect(spans).toHaveLength(8);

    expect(original.getFinishedSpans().some((span) => span.name === "chat test-model")).toBe(true);

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
      const model = session.find((span) => span.name === "generate-response")!;
      const tool = session.find((span) => span.name === "execute_tool read_guidelines")!;
      expect(tool.parentSpanContext?.spanId).toBe(model.parentSpanContext?.spanId);
      expect(model.attributes).toMatchObject({
        "langfuse.trace.name": "ChartCoach response",
        "user.id": "reviewer",
        "gen_ai.usage.input_tokens": 20,
        "gen_ai.usage.output_tokens": 5,
      });

      for (const [key, value] of Object.entries(connectionMetadata(sessionId))) {
        expect(model.attributes[`langfuse.observation.metadata.${key}`]).toEqual(
          z.string().safeParse(value).success ? value : JSON.stringify(value),
        );
        expect(tool.attributes[`langfuse.observation.metadata.${key}`]).toEqual(
          z.string().safeParse(value).success ? value : JSON.stringify(value),
        );
      }

      expect(model.attributes["langfuse.observation.metadata.catalogId"]).toBe("catalog-digest");
    }

    expect(new Set(spans.map((span) => span.spanContext().traceId)).size).toBe(2);
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

it("uses the resolved connection for actual steps zero and one without resolver index correlation", async () => {
  const exporter = new InMemorySpanExporter();

  const processor = new LangfuseProcessor({
    exporter,
    publicKey: "pk-test",
    secretKey: "sk-test",
    mediaUploadEnabled: false,
  });

  const provider = new BasicTracerProvider({
    spanProcessors: [processor],
  });

  try {
    const root = provider.getTracer("eve.agent").startSpan("agent.session", {
      attributes: {
        "agent.run.id": "changing-model",
        "gen_ai.conversation.id": "changing-model",
        "agent.turn.id": "turn-one",
        "agent.step.index": 0,
      },
    });

    inEveContext(() => {
      for (const [stepIndex, id] of ["first", "second"].entries()) {
        const metadata = {
          ...connectionMetadata(id),
          modelManaged: stepIndex === 1,
          modelEndpointOrigin: stepIndex === 0 ? "https://gateway.example" : undefined,
        };

        resolvedModelTrace.update(() => ({
          sessionId: "changing-model",
          turnId: "turn-one",
          metadata,
        }));
        const runtime = traceContext(runtimeInput("changing-model", "turn-one", stepIndex));

        const generation = provider.getTracer("eve.agent").startSpan(
          `chat ${id}`,
          {
            attributes: {
              "gen_ai.operation.name": "chat",
              "agent.run.id": "changing-model",
              "gen_ai.conversation.id": "changing-model",
              "agent.turn.id": "turn-one",
              "agent.step.index": stepIndex,
              ...runtimeAttributes(runtime),
            },
          },
          trace.setSpan(ROOT_CONTEXT, root),
        );

        generation.end();
      }
    });

    root.end();
    processor.payloads.capture({
      type: "session.waiting",
      idempotencyKey: "waiting",
      sessionId: "changing-model",
      turnId: "turn-one",
    });
    await provider.forceFlush();

    const generations = exporter
      .getFinishedSpans()
      .filter((span) => span.attributes["gen_ai.operation.name"] === "chat");

    expect(generations.map((span) => span.attributes["agent.step.index"])).toEqual([0, 1]);
    expect(
      generations.map((span) => span.attributes["langfuse.observation.metadata.modelName"]),
    ).toEqual(["model-first", "model-second"]);
    expect(
      generations.map((span) => span.attributes["langfuse.observation.metadata.modelManaged"]),
    ).toEqual(["false", "true"]);
    expect(generations[0]!.attributes["langfuse.observation.metadata.modelEndpointOrigin"]).toBe(
      "https://gateway.example",
    );
    expect(
      generations[1]!.attributes["langfuse.observation.metadata.modelEndpointOrigin"],
    ).toBeUndefined();
  } finally {
    await provider.shutdown();
  }
});

it("isolates safe resolved metadata by active session and turn", () => {
  inEveContext(() => {
    const metadata = { ...connectionMetadata("first"), apiKey: "private-key" };

    resolvedModelTrace.update(() => ({
      sessionId: "session-one",
      turnId: "turn-one",
      metadata,
    }));

    expect(traceContext(runtimeInput("session-one"))).toEqual(connectionMetadata("first"));
    expect(traceContext(runtimeInput("session-two"))).toEqual({});
    expect(traceContext(runtimeInput("session-one", "turn-two"))).toEqual({});

    inEveContext(() => {
      expect(traceContext(runtimeInput("session-one"))).toEqual({});
      resolvedModelTrace.update(() => ({
        sessionId: "session-two",
        turnId: "turn-one",
        metadata: connectionMetadata("second"),
      }));
      expect(traceContext(runtimeInput("session-two"))).toEqual(connectionMetadata("second"));
    });

    expect(traceContext(runtimeInput("session-one"))).toEqual(connectionMetadata("first"));
    expect(JSON.stringify(traceContext(runtimeInput("session-one")))).not.toContain("private-key");
  });
});

it("projects catalog identity and principal identity without exporting authentication attributes", () =>
  inEveContext(() => {
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
      traceContext({
        ...input,
        session: {
          ...session,
          auth: { current: session.auth.initiator, initiator: null },
        },
      }),
    ).toEqual(traceContext(input));
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
  }));
