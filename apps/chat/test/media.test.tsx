import { createHash } from "node:crypto";
import { ROOT_CONTEXT, trace } from "@opentelemetry/api";
import {
  BasicTracerProvider,
  InMemorySpanExporter,
  SimpleSpanProcessor,
} from "@opentelemetry/sdk-trace-base";
import type {
  InstrumentationModelCallStartedEvent,
  ProviderDefinition,
  JsonValue,
} from "eve/instrumentation";
import { afterEach, expect, it, vi } from "vite-plus/test";
import { LangfuseProcessor } from "../agent/telemetry";
import { traceMessages } from "../agent/trace-content";
import { contentInstrumentation, TracePayloads } from "../agent/trace-payloads";

const png = Buffer.from(
  "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9ZlS8AAAAASUVORK5CYII=",
  "base64",
);

afterEach(() => vi.unstubAllGlobals());

function modelCall(
  data: Uint8Array | ArrayBuffer | string = png,
  sessionId = "review-one",
  turnId = "turn-one",
): InstrumentationModelCallStartedEvent {
  return {
    type: "model.call.started",
    idempotencyKey: `${sessionId}:${turnId}:model`,
    model: { modelId: "test-model", provider: "test" },
    scope: {
      sessionId,
      turnId,
      attemptId: `${sessionId}:${turnId}:0:0`,
      attemptIndex: 0,
      stepIndex: 0,
    },
    input: {
      instructions: "Review with grounded guidance.",
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Review this chart." },
            { type: "file", data, mediaType: "image/png" },
          ],
        },
      ],
    },
  };
}

function setup(mediaUploadEnabled = false) {
  const exporter = new InMemorySpanExporter();
  const original = new InMemorySpanExporter();

  const processor = new LangfuseProcessor({
    exporter,
    publicKey: "pk-lf-test",
    secretKey: "sk-lf-test",
    baseUrl: "https://langfuse.test",
    mediaUploadEnabled,
  });

  const provider = new BasicTracerProvider({
    spanProcessors: [processor, new SimpleSpanProcessor(original)],
  });

  return {
    exporter,
    original,
    processor,
    provider,
    content: contentInstrumentation(processor.payloads),
  };
}

function nativeCall(test: ReturnType<typeof setup>, event = modelCall(), parent = ROOT_CONTEXT) {
  const tracer = test.provider.getTracer("eve.agent");

  const step = tracer.startSpan(
    "agent.step",
    {
      attributes: {
        "agent.run.id": event.scope.sessionId,
        "gen_ai.conversation.id": event.scope.sessionId,
        "agent.turn.id": event.scope.turnId,
        "agent.step.index": event.scope.stepIndex,
        "agent.step.attempt": event.scope.attemptIndex,
      },
    },
    parent,
  );

  const model = tracer.startSpan(
    "chat test-model",
    { attributes: { "gen_ai.operation.name": "chat", "gen_ai.request.model": "test-model" } },
    trace.setSpan(ROOT_CONTEXT, step),
  );

  test.content.events["model.call.started"](event);
  model.setAttribute("gen_ai.usage.input_tokens", 20);
  model.end();
  test.content.events["model.call.completed"]({
    type: "model.call.completed",
    idempotencyKey: event.idempotencyKey,
    scope: event.scope,
    finishReason: "stop",
    usage: { inputTokens: 20, outputTokens: 5 },
    content: [
      { type: "reasoning", text: "Check the labels." },
      { type: "text", text: "Use direct labels." },
    ],
  });
  step.end();

  return { step, model };
}

it("explicitly captures hosted private-channel content for the Langfuse destination", () => {
  const destination: ProviderDefinition = contentInstrumentation(new TracePayloads());
  expect(
    destination.tracePolicy?.({
      audience: "private",
      environment: "production",
      agentName: "chartcoach",
      channel: { kind: "channel:eve" },
      principalType: "user",
    }),
  ).toEqual({ emit: true, recordInputs: true, recordOutputs: true });
});

it("uploads the original image inside the generation and exports full prompts and reasoning", async () => {
  const requests: Request[] = [];
  const mediaId = createHash("sha256").update(png).digest("base64url").slice(0, 22);
  let uploaded: Uint8Array | undefined;
  vi.stubGlobal("fetch", async (input: RequestInfo | URL, init?: RequestInit) => {
    const request = new Request(input, init);
    requests.push(request.clone());

    if (request.url === "https://langfuse.test/api/public/media" && request.method === "POST")
      return Response.json({ mediaId, uploadUrl: "https://uploads.test/chart.png" });

    if (request.url === "https://uploads.test/chart.png" && request.method === "PUT") {
      uploaded = new Uint8Array(await request.arrayBuffer());

      return new Response(null, { status: 200 });
    }

    if (
      request.url === `https://langfuse.test/api/public/media/${mediaId}` &&
      request.method === "PATCH"
    )
      return Response.json({});
    throw new Error(`Unexpected media request: ${request.method} ${request.url}`);
  });
  const test = setup(true);

  try {
    const { step } = nativeCall(test);
    await test.provider.forceFlush();
    expect(uploaded).toEqual(new Uint8Array(png));

    const span = test.exporter
      .getFinishedSpans()
      .find((span) => span.name === "generate-response")!;

    expect(span.attributes["session.id"]).toBe("review-one");
    expect(span.parentSpanContext?.spanId).toBe(step.spanContext().spanId);
    const messages = JSON.parse(String(span.attributes["langfuse.observation.input"]));
    expect(messages[0]).toEqual({ role: "system", content: "Review with grounded guidance." });
    expect(messages[1].content[1].image_url.url).toMatch(
      /^@@@langfuseMedia:type=image\/png\|id=.+\|source=base64_data_uri@@@$/,
    );
    expect(JSON.parse(String(span.attributes["langfuse.observation.output"]))[0]).toMatchObject({
      reasoning_content: "Check the labels.",
      content: [{ type: "text", text: "Use direct labels." }],
    });
    expect(
      test.original.getFinishedSpans().find((span) => span.name === "chat test-model")?.attributes[
        "langfuse.observation.input"
      ],
    ).toBeUndefined();
  } finally {
    await test.provider.shutdown();
  }
});

it("retains the full permitted image and long history without leaking provider options", async () => {
  const test = setup();

  try {
    const event = modelCall(Buffer.alloc(3 * 1024 * 1024, 7));
    const text = "full context ".repeat(5000);
    nativeCall(test, {
      ...event,
      input: {
        ...event.input!,
        messages: [
          { role: "assistant", content: text, providerOptions: { apiKey: "private-key" } },
          ...event.input!.messages,
        ],
      },
    });
    await test.provider.forceFlush();

    const input = JSON.parse(
      String(
        test.exporter.getFinishedSpans().find((span) => span.name === "generate-response")!
          .attributes["langfuse.observation.input"],
      ),
    );

    expect(input[1].content).toBe(text);
    expect(JSON.stringify(input)).not.toContain("private-key");
    expect(Buffer.from(input[2].content[1].image_url.url.split(",")[1], "base64").byteLength).toBe(
      3 * 1024 * 1024,
    );
  } finally {
    await test.provider.shutdown();
  }
});

it("isolates concurrent sessions and rejects oversized or invalid image input", async () => {
  const test = setup();

  try {
    for (const [data, session] of [
      [png, "first"],
      [Buffer.alloc(3 * 1024 * 1024 + 1), "oversized"],
      ["https://images.test/chart.png", "remote"],
    ] as const)
      nativeCall(test, modelCall(data, session));
    await test.provider.forceFlush();

    const generations = test.exporter
      .getFinishedSpans()
      .filter((span) => span.name === "generate-response");

    expect(generations.map((span) => span.attributes["session.id"])).toEqual([
      "first",
      "oversized",
      "remote",
    ]);
    expect(
      generations.map(
        (span) =>
          JSON.parse(String(span.attributes["langfuse.observation.input"]))[1].content.length,
      ),
    ).toEqual([2, 1, 1]);
  } finally {
    await test.provider.shutdown();
  }
});

it("exports complete tool results and the displayed answer on the turn root", async () => {
  const test = setup();
  const event = modelCall();

  const answer = {
    workflow: "discuss",
    status: "answer",
    points: [
      {
        primary_guideline_id: "direct-labels",
        supporting_guideline_ids: [],
        assessment: null,
        context: "The chart labels are hard to follow.",
        recommendation: "Use direct labels.",
      },
    ],
    question: null,
  };

  const guidance = { text: "source context ".repeat(5000) };

  try {
    const root = test.provider.getTracer("eve.agent").startSpan("invoke_agent chartcoach", {
      attributes: {
        "gen_ai.operation.name": "invoke_agent",
        "agent.run.id": event.scope.sessionId,
        "gen_ai.conversation.id": event.scope.sessionId,
        "agent.turn.id": event.scope.turnId,
      },
    });

    const { step } = nativeCall(test, event, trace.setSpan(ROOT_CONTEXT, root));
    const tracer = test.provider.getTracer("eve.agent");

    for (const [name, output] of [
      ["read_guidelines", guidance],
      ["present_answer", answer],
    ] as const) {
      const callId = `call-${name}`;
      const idempotencyKey = `action-${name}`;
      test.content.events["tool.call.started"]({
        type: "tool.call.started",
        idempotencyKey,
        scope: event.scope,
        callId,
        toolName: name,
        input: name === "present_answer" ? answer : { ids: ["direct-labels"] },
      });

      const tool = tracer.startSpan(
        `execute_tool ${name}`,
        {
          attributes: {
            "gen_ai.operation.name": "execute_tool",
            "gen_ai.tool.name": name,
            "gen_ai.tool.call.id": callId,
          },
        },
        trace.setSpan(ROOT_CONTEXT, step),
      );

      tool.setAttribute("gen_ai.tool.call.result", "truncated local output");
      tool.end();
      test.content.events["tool.call.completed"]({
        type: "tool.call.completed",
        idempotencyKey,
        scope: event.scope,
        output: { type: "result", output },
      });
    }

    root.end();
    test.content.events["session.waiting"]({
      type: "session.waiting",
      idempotencyKey: "waiting",
      sessionId: event.scope.sessionId,
      turnId: event.scope.turnId,
    });
    await test.provider.forceFlush();
    const spans = test.exporter.getFinishedSpans();
    expect(
      JSON.parse(
        String(
          spans.find((span) => span.name === "execute_tool read_guidelines")!.attributes[
            "langfuse.observation.output"
          ],
        ),
      ),
    ).toEqual(guidance);
    const exportedRoot = spans.find((span) => span.name === "respond-to-user")!;
    expect(spans.find((span) => span.name === "agent.step")?.parentSpanContext?.spanId).toBe(
      exportedRoot.spanContext().spanId,
    );
    expect(new Set(spans.map((span) => span.spanContext().traceId)).size).toBe(1);
    expect(JSON.parse(String(exportedRoot.attributes["langfuse.observation.output"]))).toEqual(
      answer,
    );
    expect(
      JSON.parse(String(exportedRoot.attributes["langfuse.observation.input"]))[0].content[0].text,
    ).toBe("Review this chart.");
    expect(
      spans.find((span) => span.name === "execute_tool read_guidelines")!.attributes[
        "langfuse.observation.type"
      ],
    ).toBe("retriever");
    await test.provider.forceFlush();
    expect(test.exporter.getFinishedSpans()).toHaveLength(spans.length);
  } finally {
    await test.provider.shutdown();
  }
});

it("preserves raw result objects and explicit nulls while removing SDK wrapper options", () => {
  const result = (output: JsonValue) =>
    traceMessages([
      {
        role: "tool",
        content: [
          { type: "tool-result", toolName: "read_guidelines", toolCallId: "tool-one", output },
        ],
      },
    ])[0];

  expect(result({ value: "authored value", source: "reference" })?.content).toBe(
    JSON.stringify({ value: "authored value", source: "reference" }),
  );
  expect(
    result({ type: "json", value: null, providerOptions: { apiKey: "private-key" } })?.content,
  ).toBe("null");
  expect(
    result({
      type: "json",
      value: { text: "Full guidance." },
      providerOptions: { apiKey: "private-key" },
    })?.content,
  ).toBe(JSON.stringify({ text: "Full guidance." }));
});
