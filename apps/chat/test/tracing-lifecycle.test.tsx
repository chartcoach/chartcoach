import { SpanStatusCode, trace } from "@opentelemetry/api";
import {
  BasicTracerProvider,
  InMemorySpanExporter,
  type ReadableSpan,
} from "@opentelemetry/sdk-trace-base";
import type { InstrumentationAttemptScope } from "eve/instrumentation";
import type {
  AgentActionTraceState,
  AgentSessionTraceState,
  AgentTraceStateStore,
  AgentTurnTraceState,
} from "../node_modules/eve/dist/src/tracing/agent-trace-state.js";
import { MockLanguageModelV4 } from "ai/test";
import { APICallError, generateText } from "ai";
import { traceCompaction } from "../agent/compaction-telemetry";
import { expect, it, vi } from "vite-plus/test";
import { LangfuseProcessor } from "../agent/telemetry";
import { contentInstrumentation } from "../agent/trace-payloads";

// SAFETY: Exercise the pinned native lifecycle and dispatcher that order Eve's
// spans before the application's full-content instrumentation callbacks.
const { createAgentOtelInstrumentation } = (await import(
  new URL("./tracing/agent-otel-provider.js", import.meta.resolve("eve")).href
)) as typeof import("../node_modules/eve/dist/src/tracing/agent-otel-provider.js");

// SAFETY: This URL loads the dispatcher from the package that supplies its declared types.
const { createInstrumentationHooks } = (await import(
  new URL("./instrumentation/lifecycle.js", import.meta.resolve("eve")).href
)) as typeof import("../node_modules/eve/dist/src/instrumentation/lifecycle.js");

// SAFETY: Native span IDs and the tracer use the generator from the same pinned package.
const { AgentSpanIdGenerator } = (await import(
  new URL("./tracing/agent-span-id-generator.js", import.meta.resolve("eve")).href
)) as typeof import("../node_modules/eve/dist/src/tracing/agent-span-id-generator.js");

// SAFETY: Exercise the installed harness entry that parks manual compaction without opening a turn.
const { createToolLoopHarness } = (await import(
  new URL("./harness/tool-loop.js", import.meta.resolve("eve")).href
)) as typeof import("../node_modules/eve/dist/src/harness/tool-loop.js");

// SAFETY: The installed runtime supplies the production compaction telemetry options and event adapter.
const { bindInstrumentationRuntime } = (await import(
  new URL("./instrumentation/runtime.js", import.meta.resolve("eve")).href
)) as typeof import("../node_modules/eve/dist/src/instrumentation/runtime.js");

// SAFETY: Use the context implementation read by that same pinned runtime.
const { ContextContainer } = (await import(
  new URL("./context/container.js", import.meta.resolve("eve")).href
)) as typeof import("../node_modules/eve/dist/src/context/container.js");

// SAFETY: This context key defines the private production capture policy used by the gateway.
const { ConversationContextKey } = (await import(
  new URL("./shared/conversation-context.js", import.meta.resolve("eve")).href
)) as typeof import("../node_modules/eve/dist/src/shared/conversation-context.js");

class MemoryTraceState implements AgentTraceStateStore {
  private readonly sessions = new Map<string, AgentSessionTraceState>();
  private readonly turns = new Map<string, AgentTurnTraceState>();
  private readonly actions = new Map<string, AgentActionTraceState>();
  private readonly anchors = new Map<string, AgentActionTraceState>();

  getSession(sessionId: string) {
    return this.sessions.get(sessionId);
  }

  setSession(sessionId: string, state: AgentSessionTraceState) {
    this.sessions.set(sessionId, state);
  }

  deleteSession(sessionId: string) {
    this.sessions.delete(sessionId);
  }

  getTurn(sessionId: string, turnId: string) {
    return this.turns.get(JSON.stringify([sessionId, turnId]));
  }

  setTurn(sessionId: string, turnId: string, state: AgentTurnTraceState) {
    this.turns.set(JSON.stringify([sessionId, turnId]), state);
  }

  updateTurn(
    sessionId: string,
    turnId: string,
    update: (state: AgentTurnTraceState) => AgentTurnTraceState,
  ) {
    const current = this.getTurn(sessionId, turnId);

    if (current) this.setTurn(sessionId, turnId, update(current));
  }

  deleteTurn(sessionId: string, turnId: string) {
    this.turns.delete(JSON.stringify([sessionId, turnId]));
  }

  getAction(key: string) {
    return this.actions.get(key);
  }

  setAction(key: string, state: AgentActionTraceState) {
    this.actions.set(key, state);
  }

  deleteAction(key: string) {
    this.actions.delete(key);
  }

  deleteActions(sessionId: string, turnId?: string) {
    for (const [key, state] of this.actions)
      if (state.sessionId === sessionId && (turnId === undefined || state.turnId === turnId))
        this.actions.delete(key);
  }

  findAction(sessionId: string, callId: string) {
    return [...this.actions.values()].find(
      (state) => state.sessionId === sessionId && state.callId === callId,
    );
  }

  setActionAnchor(key: string, state: AgentActionTraceState) {
    this.anchors.set(key, state);
  }

  findActionAnchor(sessionId: string, turnId: string, callId: string) {
    return [...this.anchors.values()].find(
      (state) =>
        state.sessionId === sessionId && state.turnId === turnId && state.callId === callId,
    );
  }

  deleteActionAnchors(sessionId: string) {
    for (const [key, state] of this.anchors)
      if (state.sessionId === sessionId) this.anchors.delete(key);
  }
}

function setup(competeOnEnd?: (span: ReadableSpan) => boolean) {
  const exporter = new InMemorySpanExporter();

  const processor = new LangfuseProcessor({
    exporter,
    publicKey: "pk-test",
    secretKey: "sk-test",
    mediaUploadEnabled: false,
  });

  const competingFlushes: Promise<void>[] = [];
  const idGenerator = new AgentSpanIdGenerator();

  const provider = new BasicTracerProvider({
    idGenerator,
    spanProcessors: [
      processor,
      {
        onStart() {},
        onEnd(span) {
          if (competeOnEnd?.(span))
            // Another session's step flush can run between Eve's serial native
            // handler and the parallel full-content handler for this session.
            queueMicrotask(() => competingFlushes.push(provider.forceFlush()));
        },
        async forceFlush() {},
        async shutdown() {},
      },
    ],
  });

  const native = createAgentOtelInstrumentation({
    environment: "production",
    frameworkVersion: "0.74.0",
    idGenerator,
    recordInputs: true,
    recordOutputs: true,
    stateStore: new MemoryTraceState(),
    tracer: provider.getTracer("eve.agent"),
    tracePolicy: () => ({ emit: true, recordInputs: true, recordOutputs: true }),
  });

  const content = contentInstrumentation(processor.payloads);

  const hooks = createInstrumentationHooks({
    serialBefore: [{ ...native.hook, name: "native" }],
    parallel: [{ ...content, name: "content" }],
  }).forTrace!({
    agentName: "chartcoach",
    audience: "private",
    environment: "production",
    channel: { kind: "channel:eve" },
    principalType: "user",
  });

  const sessionId = "lifecycle-session";

  async function start(turnId = "turn-one", sequence = 0) {
    if (sequence === 0)
      await hooks.publish({
        type: "session.started",
        idempotencyKey: `session:${sessionId}`,
        agentName: "chartcoach",
        channelAudience: "private",
        channelKind: "channel:eve",
        rootSessionId: sessionId,
        sessionId,
        traceSessionId: sessionId,
      });
    await hooks.publish({
      type: "turn.started",
      idempotencyKey: `turn:${sessionId}:${turnId}`,
      sessionId,
      turnId,
      rootSessionId: sessionId,
      traceSessionId: sessionId,
      sequence,
    });
  }

  async function call(attemptIndex = 0, turnId = "turn-one") {
    const scope: InstrumentationAttemptScope = {
      sessionId,
      turnId,
      attemptId: `${sessionId}:${turnId}:0:${attemptIndex}`,
      attemptIndex,
      stepIndex: 0,
      channelAudience: "private",
      functionId: "chartcoach",
    };

    const idempotencyKey = `model:${scope.attemptId}`;
    await hooks.publish({
      type: "step.attempt.started",
      idempotencyKey: scope.attemptId,
      scope,
      operation: { modelId: "test-model", operationId: "generateText", provider: "test" },
    });
    await hooks.publish({
      type: "model.call.started",
      idempotencyKey,
      scope,
      model: { modelId: "test-model", provider: "test" },
      input: {
        instructions: "Review the chart.",
        messages: [{ role: "user", content: "Question" }],
      },
    });

    return {
      scope,
      async complete(text: string) {
        await hooks.publish({
          type: "model.call.completed",
          idempotencyKey,
          scope,
          finishReason: "stop",
          usage: { inputTokens: 12, outputTokens: 8 },
          content: [{ type: "text", text }],
        });
        await hooks.publish({
          type: "step.attempt.completed",
          idempotencyKey: scope.attemptId,
          scope,
        });
      },
      async fail(error: Error) {
        await hooks.publish({ type: "model.call.failed", idempotencyKey, scope, error });
        await hooks.publish({
          type: "step.attempt.failed",
          idempotencyKey: scope.attemptId,
          scope,
          error,
        });
      },
    };
  }

  async function settle(
    outcome: "completed" | "failed" | "cancelled" = "completed",
    turnId = "turn-one",
    error = new Error("The turn failed."),
  ) {
    const identity = { idempotencyKey: `turn:${sessionId}:${turnId}`, sessionId, turnId };

    if (outcome === "failed") await hooks.publish({ type: "turn.failed", ...identity, error });
    else
      await hooks.publish({
        type: outcome === "cancelled" ? "turn.cancelled" : "turn.completed",
        ...identity,
      });
    await hooks.publish({
      type: "session.waiting",
      idempotencyKey: `session:${sessionId}`,
      sessionId,
      turnId,
    });
    await Promise.all(competingFlushes);
    await provider.forceFlush();
  }

  return { provider, processor, hooks, exporter, competingFlushes, start, call, settle };
}

function productionInstrumentation(test: ReturnType<typeof setup>) {
  const ctx = new ContextContainer();
  ctx.set(ConversationContextKey, {
    audience: "private",
    channel: { kind: "channel:eve" },
    environment: "production",
    principalType: "user",
  });

  return bindInstrumentationRuntime(
    {
      hooks: test.hooks,
      ownsAgentSpans: true,
      otelSettings: {
        recordInputs: true,
        recordOutputs: true,
        traceChannelRequests: false,
        tracePolicy: () => true,
      },
      forceFlush: () => test.provider.forceFlush(),
      shutdown: () => test.provider.shutdown(),
      runInContext: (_operation, execute) => execute(),
    },
    ctx,
    { agentName: "chartcoach", rootSessionId: "lifecycle-session", sessionId: "lifecycle-session" },
  )!.prepareExecution();
}

function maintenanceSession(): Parameters<ReturnType<typeof createToolLoopHarness>>[0] {
  return {
    agent: { system: "Review the chart.", tools: [], modelReference: { id: "test-model" } },
    compaction: { threshold: 1000, recentWindowSize: 1 },
    continuationToken: "test-continuation",
    sessionId: "lifecycle-session",
    history: [
      { role: "user", kind: "user", content: "History ".repeat(2000) },
      { role: "user", kind: "user", content: "r".repeat(2000) },
    ],
    state: {
      "eve.harness.sessionProjection": {
        started: true,
        nextSequence: 1,
        turns: {},
        authorizations: {},
        calls: {},
        candidates: {},
        inputs: {},
        tasks: {},
      },
    },
  };
}

const maintenanceAttributes = {
  "agent.run.id": "lifecycle-session",
  "agent.turn.id": "turn_1",
  "agent.step.index": 0,
  "gen_ai.conversation.id": "lifecycle-session",
};

const summaryResult = (text: string) => ({
  content: [{ type: "text" as const, text }],
  finishReason: { unified: "stop" as const, raw: "stop" },
  usage: {
    inputTokens: { total: 40, noCache: 30, cacheRead: 10, cacheWrite: undefined },
    outputTokens: { total: 8, text: 8, reasoning: undefined },
  },
  warnings: [],
});

const content = (span: ReadableSpan, direction: "input" | "output") =>
  JSON.parse(String(span.attributes[`langfuse.observation.${direction}`]));

it("preserves full native completion and the delayed turn root through competing session flushes", async () => {
  const test = setup((span) =>
    ["chat", "invoke_agent"].includes(String(span.attributes["gen_ai.operation.name"])),
  );

  const text = "long-output ".repeat(4000);

  try {
    await test.start();
    const call = await test.call();
    await call.complete(text);
    await test.settle();
    expect(test.competingFlushes).toHaveLength(2);
    const spans = test.exporter.getFinishedSpans();
    expect(spans).toHaveLength(3);
    const generation = spans.find((span) => span.name === "generate-response")!;
    const step = spans.find((span) => span.name === "agent.step")!;
    const root = spans.find((span) => span.name === "respond-to-user")!;
    expect(generation.attributes["gen_ai.output.messages"]).toBeUndefined();
    expect(content(generation, "output")[0].content).toEqual([{ type: "text", text }]);
    expect(content(root, "output")).toEqual(content(generation, "output"));
    expect(content(root, "input")).toEqual([{ role: "user", content: "Question" }]);
    expect(generation.parentSpanContext?.spanId).toBe(step.spanContext().spanId);
    expect(step.parentSpanContext?.spanId).toBe(root.spanContext().spanId);
    expect(new Set(spans.map((span) => span.spanContext().traceId)).size).toBe(1);
    expect(spans.filter((span) => span.attributes["langfuse.internal.is_app_root"])).toEqual([
      root,
    ]);
  } finally {
    await test.provider.shutdown();
  }
});

it("keeps failed attempts and the successful retry attached to one native turn", async () => {
  const test = setup();

  try {
    await test.start();
    await (await test.call()).fail(new Error("Provider retry required."));
    await test.provider.forceFlush();
    await (await test.call(1)).complete("Retry succeeded.");
    await test.settle();
    const spans = test.exporter.getFinishedSpans();
    const generations = spans.filter((span) => span.name === "generate-response");
    expect(generations).toHaveLength(2);
    expect(generations.map((span) => span.attributes["agent.step.attempt"])).toEqual([0, 1]);
    expect(generations[0]!.status.code).toBe(SpanStatusCode.ERROR);
    expect(content(generations[0]!, "output")).toEqual({
      name: "Error",
      message: "Provider retry required.",
    });
    const root = spans.find((span) => span.name === "respond-to-user")!;
    expect(content(root, "output")).toEqual(content(generations[1]!, "output"));
    expect(spans.filter((span) => span.attributes["langfuse.internal.is_app_root"])).toEqual([
      root,
    ]);
    const count = spans.length;
    await test.provider.forceFlush();
    expect(test.exporter.getFinishedSpans()).toHaveLength(count);
  } finally {
    await test.provider.shutdown();
  }
});

for (const outcome of ["failed", "cancelled"] as const)
  it(`settles a ${outcome} native turn and retains the session for a follow-up`, async () => {
    const test = setup();

    try {
      await test.start();
      const error = new Error("Interrupted model call.");
      await (await test.call()).fail(error);
      await test.settle(outcome, "turn-one", error);

      const firstRoot = test.exporter
        .getFinishedSpans()
        .find((span) => span.name === "respond-to-user")!;

      expect(firstRoot.attributes["agent.turn.outcome"]).toBe(outcome);
      expect(firstRoot.status.code === SpanStatusCode.ERROR).toBe(outcome === "failed");
      await test.start("turn-two", 1);
      await (await test.call(0, "turn-two")).complete("Follow-up succeeded.");
      await test.settle("completed", "turn-two");

      const roots = test.exporter
        .getFinishedSpans()
        .filter((span) => span.name === "respond-to-user");

      expect(roots).toHaveLength(2);
      expect(roots[0]!.attributes["session.id"]).toBe(roots[1]!.attributes["session.id"]);
      expect(roots[0]!.spanContext().traceId).not.toBe(roots[1]!.spanContext().traceId);
      expect(content(roots[1]!, "output")[0].content).toEqual([
        { type: "text", text: "Follow-up succeeded." },
      ]);
    } finally {
      await test.provider.shutdown();
    }
  });

it("attaches real Eve history compaction before the first attempt to its later native turn", async () => {
  const test = setup();
  trace.setGlobalTracerProvider(test.provider);

  // SAFETY: Invoke the compaction engine from the pinned package tested by the native lifecycle fixture.
  const { compactMessages } = (await import(
    new URL("./harness/compaction/engine.js", import.meta.resolve("eve")).href
  )) as typeof import("../node_modules/eve/dist/src/harness/compaction/engine.js");

  const model = new MockLanguageModelV4({
    doGenerate: {
      content: [{ type: "text", text: "Keep the direct-label recommendation." }],
      finishReason: { unified: "stop", raw: "stop" },
      usage: {
        inputTokens: { total: 40, noCache: 30, cacheRead: 10, cacheWrite: undefined },
        outputTokens: { total: 8, text: 8, reasoning: undefined },
      },
      warnings: [],
    },
  });

  try {
    await test.start();
    await compactMessages(
      [{ role: "user", content: "Review the labels. ".repeat(3000) }],
      traceCompaction(model, {
        "agent.run.id": "lifecycle-session",
        "agent.turn.id": "turn-one",
        "agent.step.index": 0,
        "gen_ai.conversation.id": "lifecycle-session",
      }),
      { threshold: 2048, recentWindowSize: 1 },
      undefined,
      { isEnabled: false },
      undefined,
      undefined,
      true,
    );
    await test.provider.forceFlush();
    expect(test.exporter.getFinishedSpans()).toHaveLength(0);
    await (await test.call()).complete("The full response.");
    await test.settle();
    const spans = test.exporter.getFinishedSpans();
    const summary = spans.find((span) => span.name === "compact-history")!;
    const root = spans.find((span) => span.name === "respond-to-user")!;
    const generation = spans.find((span) => span.name === "generate-response")!;
    expect(summary.parentSpanContext?.spanId).toBe(root.spanContext().spanId);
    expect(summary.spanContext().traceId).toBe(root.spanContext().traceId);
    expect(summary.attributes["langfuse.internal.is_app_root"]).toBe(false);
    expect(content(summary, "input")[0].role).toBe("system");
    expect(content(summary, "output")[0].content).toEqual([
      { type: "text", text: "Keep the direct-label recommendation." },
    ]);
    expect(content(generation, "output")[0].content).toEqual([
      { type: "text", text: "The full response." },
    ]);
    expect(spans.filter((span) => span.attributes["langfuse.internal.is_app_root"])).toEqual([
      root,
    ]);
  } finally {
    await test.provider.shutdown();
    trace.disable();
  }
});

it("groups repeated manual Eve compaction calls beneath one maintenance root before the next turn", async () => {
  const test = setup();
  trace.setGlobalTracerProvider(test.provider);

  const summary = "Keep the direct-label recommendation.";

  const model = new MockLanguageModelV4({
    doGenerate: [summaryResult("s".repeat(2500)), summaryResult(summary)],
  });

  const events: string[] = [];
  const beforeSettlement: number[] = [];
  const instrumentation = productionInstrumentation(test);

  const run = createToolLoopHarness({
    compactOnly: true,
    instrumentation,
    async handleEvent(event) {
      events.push(event.type);

      if (event.type === "compaction.completed") {
        await test.provider.forceFlush();
        beforeSettlement.push(test.exporter.getFinishedSpans().length);
      }
    },
    resolveModel: async () => traceCompaction(model, maintenanceAttributes),
    tools: new Map(),
  });

  try {
    await instrumentation.runStep(
      {
        environment: "production",
        eveVersion: "0.74.0",
        hasInput: false,
        session: { sessionId: "lifecycle-session" },
      },
      async (scope) => {
        expect(scope.telemetry()?.integrations).toEqual([]);
        expect(scope.telemetry()?.isEnabled).toBe(true);
      },
    );
    await test.start();
    await (await test.call()).complete("The preceding turn.");
    await test.settle();
    const initialCount = test.exporter.getFinishedSpans().length;
    await run(maintenanceSession());
    expect(events).toEqual(["compaction.requested", "compaction.completed", "session.waiting"]);
    expect(model.doGenerateCalls).toHaveLength(2);
    expect(beforeSettlement).toEqual([initialCount]);
    await test.provider.forceFlush();
    const spans = test.exporter.getFinishedSpans().slice(initialCount);
    const generations = spans.filter((span) => span.name === "compact-history");
    const root = spans.find((span) => span.name === "compact-session")!;
    expect(spans).toHaveLength(3);
    expect(generations).toHaveLength(2);
    expect(root.parentSpanContext).toBeUndefined();
    expect(root.attributes["langfuse.trace.name"]).toBe("chartcoach history compaction");
    expect(root.attributes["langfuse.trace.tags"]).toEqual(["chartcoach", "chat", "compaction"]);
    expect(root.attributes["session.id"]).toBe("lifecycle-session");
    expect(root.attributes["gen_ai.usage.input_tokens"]).toBeUndefined();
    expect(root.attributes["gen_ai.usage.output_tokens"]).toBeUndefined();
    expect(root.attributes["gen_ai.request.model"]).toBeUndefined();
    expect(
      test.processor.payloads.isTurnSettled({
        "agent.run.id": "lifecycle-session",
        "agent.turn.id": "turn_1",
      }),
    ).toBe(false);
    expect(content(root, "input")).toEqual(content(generations[0]!, "input"));
    expect(content(root, "output")).toEqual(content(generations[1]!, "output"));
    expect(spans.filter((span) => span.attributes["langfuse.internal.is_app_root"])).toEqual([
      root,
    ]);

    for (const generation of generations) {
      expect(generation.parentSpanContext?.spanId).toBe(root.spanContext().spanId);
      expect(generation.spanContext().traceId).toBe(root.spanContext().traceId);
      expect(generation.attributes["gen_ai.usage.input_tokens"]).toBe(40);
    }

    await test.start("turn_1", 1);
    await (await test.call(0, "turn_1")).complete("The next response.");
    await test.settle("completed", "turn_1");

    const next = test.exporter
      .getFinishedSpans()
      .findLast((span) => span.name === "respond-to-user")!;

    expect(next.spanContext().traceId).not.toBe(root.spanContext().traceId);
    expect(content(next, "output")[0].content).toEqual([
      { type: "text", text: "The next response." },
    ]);
  } finally {
    await test.provider.shutdown();
    trace.disable();
  }
});

it("keeps a retried compaction failure on its generation while the maintenance root succeeds", async () => {
  const test = setup();
  trace.setGlobalTracerProvider(test.provider);

  let attempts = 0;

  const model = new MockLanguageModelV4({
    doGenerate: async () => {
      attempts += 1;

      if (attempts === 1)
        throw new APICallError({
          message: "Provider included a private request body.",
          url: "https://model.example/v1",
          requestBodyValues: { credential: "private-provider-key" },
          statusCode: 503,
          isRetryable: true,
        });

      return summaryResult("Retry summary.");
    },
  });

  const run = createToolLoopHarness({
    compactOnly: true,
    instrumentation: productionInstrumentation(test),
    handleEvent: async () => {},
    resolveModel: async () => traceCompaction(model, maintenanceAttributes),
    tools: new Map(),
  });

  try {
    await run(maintenanceSession());
    await test.provider.forceFlush();
    const spans = test.exporter.getFinishedSpans();
    const generations = spans.filter((span) => span.name === "compact-history");
    const root = spans.find((span) => span.name === "compact-session")!;
    expect(generations).toHaveLength(2);
    expect(generations[0]!.status.code).toBe(SpanStatusCode.ERROR);
    expect(content(generations[0]!, "output")).toEqual({ message: "Context compaction failed." });
    expect(root.status.code).not.toBe(SpanStatusCode.ERROR);
    expect(content(root, "output")).toEqual(content(generations[1]!, "output"));
    expect(JSON.stringify(spans.map((span) => span.attributes))).not.toContain(
      "private-provider-key",
    );
    expect(spans.filter((span) => span.attributes["langfuse.internal.is_app_root"])).toEqual([
      root,
    ]);
  } finally {
    await test.provider.shutdown();
    trace.disable();
  }
});

it("records a failed manual compaction when Eve rejects an empty summary and parks unchanged history", async () => {
  const test = setup();
  trace.setGlobalTracerProvider(test.provider);

  const output = [
    { type: "reasoning" as const, text: "Consider the earlier recommendations." },
    { type: "text" as const, text: "" },
  ];

  const model = new MockLanguageModelV4({
    doGenerate: {
      ...summaryResult(""),
      content: output,
      finishReason: { unified: "length", raw: "length" },
    },
  });

  const events: string[] = [];

  const run = createToolLoopHarness({
    compactOnly: true,
    instrumentation: productionInstrumentation(test),
    handleEvent: async (event) => {
      events.push(event.type);
    },
    resolveModel: async () => traceCompaction(model, maintenanceAttributes),
    tools: new Map(),
  });

  try {
    const session = maintenanceSession();
    const result = await run(session);
    await test.provider.forceFlush();
    expect(events).toEqual(["compaction.requested", "session.waiting"]);
    expect(result.session.history).toEqual(session.history);
    const spans = test.exporter.getFinishedSpans();
    const generation = spans.find((span) => span.name === "compact-history")!;
    const root = spans.find((span) => span.name === "compact-session")!;
    expect(spans).toHaveLength(2);
    expect(generation.status).toEqual({
      code: SpanStatusCode.ERROR,
      message: "Context compaction returned an empty summary.",
    });
    expect(root.status).toEqual(generation.status);
    expect(content(root, "input")).toEqual(content(generation, "input"));
    expect(content(root, "input")[0].role).toBe("system");
    expect(content(generation, "output")).toEqual([
      {
        role: "assistant",
        content: [{ type: "text", text: "" }],
        reasoning_content: "Consider the earlier recommendations.",
      },
    ]);
    expect(content(root, "output")).toEqual(content(generation, "output"));
    expect(root.parentSpanContext).toBeUndefined();
    expect(generation.parentSpanContext?.spanId).toBe(root.spanContext().spanId);
    expect(spans.filter((span) => span.attributes["langfuse.internal.is_app_root"])).toEqual([
      root,
    ]);
  } finally {
    await test.provider.shutdown();
    trace.disable();
  }
});

it("exports unanchored compaction beneath a maintenance root when shutdown precedes parking", async () => {
  const test = setup();
  trace.setGlobalTracerProvider(test.provider);

  const exported: ReadableSpan[] = [];
  const exportSpans = test.exporter.export.bind(test.exporter);

  const spy = vi.spyOn(test.exporter, "export").mockImplementation((spans, done) => {
    exported.push(...spans);
    exportSpans(spans, done);
  });

  try {
    await generateText({
      model: traceCompaction(
        new MockLanguageModelV4({ doGenerate: summaryResult("Shutdown summary.") }),
        maintenanceAttributes,
      ),
      prompt: "Compact this history.",
      telemetry: { integrations: [] },
    });
    await test.provider.forceFlush();
    expect(exported).toHaveLength(0);
    await test.provider.shutdown();
    const root = exported.find((span) => span.name === "compact-session")!;
    const generation = exported.find((span) => span.name === "compact-history")!;
    expect(exported).toHaveLength(2);
    expect(root.parentSpanContext).toBeUndefined();
    expect(generation.parentSpanContext?.spanId).toBe(root.spanContext().spanId);
    expect(generation.spanContext().traceId).toBe(root.spanContext().traceId);
    expect(exported.filter((span) => span.attributes["langfuse.internal.is_app_root"])).toEqual([
      root,
    ]);
  } finally {
    await test.provider.shutdown();
    spy.mockRestore();
    trace.disable();
  }
});
