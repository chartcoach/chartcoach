import { createHash } from "node:crypto";
import { BasicTracerProvider, InMemorySpanExporter } from "@opentelemetry/sdk-trace-base";
import type { DataContent } from "ai";
import type { InstrumentationModelCallStartedEvent } from "eve/instrumentation";
import { afterEach, expect, it, vi } from "vite-plus/test";
import { mediaInstrumentation } from "../agent/media";
import { LangfuseProcessor } from "../agent/telemetry";

const png = Buffer.from(
  "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9ZlS8AAAAASUVORK5CYII=",
  "base64",
);

afterEach(() => vi.unstubAllGlobals());

function modelCall(
  data: DataContent = png,
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

  const provider = new BasicTracerProvider({
    spanProcessors: [
      new LangfuseProcessor({
        exporter,
        publicKey: "pk-lf-test",
        secretKey: "sk-lf-test",
        baseUrl: "https://langfuse.test",
        mediaUploadEnabled,
      }),
    ],
  });

  return {
    exporter,
    provider,
    media: mediaInstrumentation(provider.getTracer("chartcoach.media")),
  };
}

it("uploads image bytes through Langfuse and exports the session-linked media reference", async () => {
  const requests: Request[] = [];
  const mediaId = createHash("sha256").update(png).digest("base64url").slice(0, 22);
  let uploaded: Uint8Array | undefined;
  vi.stubGlobal("fetch", async (input: RequestInfo | URL, init?: RequestInit) => {
    const request = new Request(input, init);
    requests.push(request.clone());
    const url = new URL(request.url);

    if (url.href === "https://langfuse.test/api/public/media" && request.method === "POST") {
      return Response.json({ mediaId, uploadUrl: "https://uploads.test/chart.png" });
    }

    if (url.href === "https://uploads.test/chart.png" && request.method === "PUT") {
      uploaded = new Uint8Array(await request.arrayBuffer());

      return new Response(null, { status: 200 });
    }

    if (
      url.href === `https://langfuse.test/api/public/media/${mediaId}` &&
      request.method === "PATCH"
    ) {
      return Response.json({});
    }

    throw new Error(`Unexpected media request: ${request.method} ${url.href}`);
  });
  const { exporter, provider, media } = setup(true);

  try {
    media.events["model.call.started"](modelCall());
    await provider.forceFlush();
    expect(uploaded).toEqual(new Uint8Array(png));
    const upload = await requests[0]!.json();
    expect(upload).toMatchObject({ contentLength: png.byteLength, contentType: "image/png" });
    const spans = exporter.getFinishedSpans();
    expect(spans).toHaveLength(1);
    const span = spans[0]!;
    expect(span.name).toBe("Chart image");
    expect(span.attributes["session.id"]).toBe("review-one");
    expect(span.parentSpanContext).toBeUndefined();
    const image = JSON.parse(String(span.attributes["langfuse.observation.input"])).image;
    expect(image).toMatch(/^@@@langfuseMedia:type=image\/png\|id=.+\|source=base64_data_uri@@@$/);
    expect(JSON.parse(String(span.attributes["langfuse.observation.metadata"]))).toMatchObject({
      turnId: "turn-one",
      bytes: png.byteLength,
      sha256: createHash("sha256").update(png).digest("hex"),
    });
  } finally {
    media.shutdown();
    await provider.shutdown();
  }
});

it("deduplicates retries within a turn and separates parallel sessions and follow-ups", async () => {
  const { exporter, provider, media } = setup();

  try {
    const first = modelCall();
    media.events["model.call.started"](first);
    media.events["model.call.started"](modelCall(png, "review-two"));
    media.events["model.call.started"]({
      ...first,
      scope: { ...first.scope, attemptIndex: 1 },
    });
    media.events["model.call.started"](modelCall(png, "review-one", "turn-two"));
    await provider.forceFlush();
    expect(exporter.getFinishedSpans().map((span) => span.attributes["session.id"])).toEqual([
      "review-one",
      "review-two",
      "review-one",
    ]);
  } finally {
    media.shutdown();
    await provider.shutdown();
  }
});

it("keeps the full allowed image and skips oversized or policy-filtered input", async () => {
  const { exporter, provider, media } = setup();

  try {
    const maximum = Buffer.alloc(3 * 1024 * 1024, 7);
    media.events["model.call.started"](modelCall(maximum));
    media.events["model.call.started"](modelCall(Buffer.alloc(3 * 1024 * 1024 + 1), "too-large"));
    media.events["model.call.started"](modelCall("A".repeat(4 * 1024 * 1024 + 4), "large-base64"));
    media.events["model.call.started"]({ ...modelCall(png, "private"), input: undefined });
    media.events["model.call.started"](modelCall("https://images.test/chart.png", "remote"));
    await provider.forceFlush();
    const spans = exporter.getFinishedSpans();
    expect(spans).toHaveLength(1);
    const image = JSON.parse(String(spans[0]!.attributes["langfuse.observation.input"])).image;
    expect(
      Buffer.from(image.slice("data:image/png;base64,".length), "base64").equals(maximum),
    ).toBe(true);
  } finally {
    media.shutdown();
    await provider.shutdown();
  }
});
