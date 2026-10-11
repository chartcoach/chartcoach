import assert from "node:assert/strict";
import { createServer } from "node:http";
import { gunzipSync } from "node:zlib";
import { z } from "zod";

const attributeValue = z.object({
  stringValue: z.string().optional(),
  intValue: z.union([z.string(), z.number()]).optional(),
  boolValue: z.boolean().optional(),
  doubleValue: z.number().optional(),
  arrayValue: z
    .object({ values: z.array(z.object({ stringValue: z.string().optional() })) })
    .optional(),
});

const spanSchema = z.object({
  traceId: z.string(),
  spanId: z.string(),
  parentSpanId: z.string().optional(),
  name: z.string(),
  attributes: z.array(z.object({ key: z.string(), value: attributeValue })),
});

const exportSchema = z.object({
  resourceSpans: z.array(
    z.object({ scopeSpans: z.array(z.object({ spans: z.array(spanSchema) })) }),
  ),
});

type TraceSpan = z.infer<typeof spanSchema>;

export async function tracingProbe(expectedImage: Buffer) {
  const spans: TraceSpan[] = [];
  const images: Buffer[] = [];

  const server = createServer(async (request, response) => {
    try {
      const chunks: Buffer[] = [];

      for await (const chunk of request) chunks.push(Buffer.from(chunk));
      const bytes = Buffer.concat(chunks);
      const body = request.headers["content-encoding"] === "gzip" ? gunzipSync(bytes) : bytes;

      if (request.url === "/api/public/otel/v1/traces") {
        const exported = exportSchema.parse(JSON.parse(body.toString()));
        spans.push(
          ...exported.resourceSpans.flatMap((resource) =>
            resource.scopeSpans.flatMap((scope) => scope.spans),
          ),
        );
        response.setHeader("content-type", "application/json");
        response.end("{}");

        return;
      }

      if (request.url === "/api/public/media" && request.method === "POST") {
        const media = z
          .object({ sha256Hash: z.string(), contentLength: z.number(), contentType: z.string() })
          .parse(JSON.parse(body.toString()));

        assert.equal(media.contentLength, expectedImage.byteLength);
        assert.equal(media.contentType, "image/png");
        const mediaId = Buffer.from(media.sha256Hash, "base64").toString("base64url").slice(0, 22);
        response.setHeader("content-type", "application/json");
        response.end(JSON.stringify({ mediaId, uploadUrl: `http://127.0.0.1:${port}/upload` }));

        return;
      }

      if (request.url === "/upload" && request.method === "PUT") {
        images.push(body);
        response.end();

        return;
      }

      if (request.url?.startsWith("/api/public/media/") && request.method === "PATCH") {
        response.setHeader("content-type", "application/json");
        response.end("{}");

        return;
      }

      response.writeHead(404);
      response.end();
    } catch (error) {
      response.writeHead(400);
      response.end(String(error));
    }
  });

  await new Promise<void>((resolve, reject) => {
    server.once("error", reject);
    server.listen(0, "127.0.0.1", resolve);
  });
  const address = server.address();
  const { port } = z.object({ port: z.number() }).parse(address);
  const remote = process.env.CHARTCOACH_TEST_LANGFUSE === "true";

  if (remote)
    assert.ok(
      process.env.LANGFUSE_PUBLIC_KEY &&
        process.env.LANGFUSE_SECRET_KEY &&
        process.env.LANGFUSE_BASE_URL,
    );

  return {
    environment: {
      CHARTCOACH_TRACING: "true",
      LANGFUSE_PUBLIC_KEY: remote ? process.env.LANGFUSE_PUBLIC_KEY! : "pk-lf-package-test",
      LANGFUSE_SECRET_KEY: remote ? process.env.LANGFUSE_SECRET_KEY! : "sk-lf-package-test",
      LANGFUSE_BASE_URL: remote ? process.env.LANGFUSE_BASE_URL! : `http://127.0.0.1:${port}`,
      LANGFUSE_TRACING_ENVIRONMENT: "integration-test",
      LANGFUSE_RELEASE: "chartcoach-tracing-review",
    },
    verify() {
      if (remote) return;

      const value = (span: TraceSpan, key: string) =>
        span.attributes.find((attribute) => attribute.key === key)?.value.stringValue;

      const roots = spans.filter((span) => span.name === "respond-to-user");
      assert.equal(
        roots.length,
        2,
        "Each browser message creates one root trace, including after restart",
      );
      assert.notEqual(roots[0]!.traceId, roots[1]!.traceId);
      assert.ok(value(roots[0]!, "session.id"));
      assert.equal(value(roots[0]!, "session.id"), value(roots[1]!, "session.id"));
      assert.ok(value(roots[0]!, "user.id"));

      for (const root of roots) {
        assert.ok(value(root, "langfuse.observation.input"));
        assert.equal(
          JSON.parse(value(root, "langfuse.observation.output")!).points[0].recommendation,
          "Use clear labels for the comparison.",
        );
        const turn = spans.filter((span) => span.traceId === root.traceId);
        const ids = new Set(turn.map((span) => span.spanId));

        for (const span of turn) {
          if (span !== root)
            assert.ok(ids.has(span.parentSpanId ?? ""), `${span.name} has an exported parent`);
          assert.equal(value(span, "session.id"), value(root, "session.id"));
        }

        for (const span of turn)
          assert.equal(
            span.attributes.find((attribute) => attribute.key === "langfuse.internal.is_app_root")
              ?.value.boolValue,
            span === root,
            `${span.name} has the expected app-root marker`,
          );
        const generations = turn.filter((span) => span.name === "generate-response");

        const tools = turn.filter(
          (span) => value(span, "gen_ai.operation.name") === "execute_tool",
        );

        assert.equal(generations.length, 3, "Each turn has three model invocations");
        assert.deepEqual(
          tools
            .map((tool) => value(tool, "gen_ai.tool.name")!)
            .sort((left, right) => left.localeCompare(right)),
          ["present_answer", "read_guidelines"],
        );
        assert.equal(turn.filter((span) => span.name === "agent.step").length, 3);

        for (const generation of generations) {
          const input = JSON.parse(value(generation, "langfuse.observation.input")!);
          assert.ok(input.some((message: { role: string }) => message.role === "system"));
          assert.ok(JSON.stringify(input).includes("@@@langfuseMedia:"));
          assert.ok(value(generation, "langfuse.observation.output"));
          assert.ok(
            generation.attributes.some(
              (attribute) => attribute.key === "gen_ai.usage.input_tokens",
            ),
          );
          assert.equal(
            value(generation, "langfuse.observation.metadata.modelName"),
            "package-test-model",
          );
          assert.ok(value(generation, "langfuse.observation.metadata.catalogId"));
        }

        for (const tool of turn.filter(
          (span) => value(span, "gen_ai.operation.name") === "execute_tool",
        )) {
          assert.ok(value(tool, "langfuse.observation.input"));
          assert.ok(value(tool, "langfuse.observation.output"));
          assert.equal(
            value(tool, "langfuse.observation.metadata.modelName"),
            "package-test-model",
          );
          assert.ok(value(tool, "langfuse.observation.metadata.catalogId"));
        }
      }

      const maintenance = spans.filter((span) => span.name === "compact-session");
      assert.equal(maintenance.length, 1, "Manual compaction creates one maintenance trace");
      const summaryRoot = maintenance[0]!;
      assert.equal(value(summaryRoot, "session.id"), value(roots[0]!, "session.id"));
      assert.equal(value(summaryRoot, "user.id"), value(roots[0]!, "user.id"));
      assert.equal(summaryRoot.parentSpanId, undefined);
      assert.ok(value(summaryRoot, "langfuse.observation.input"));
      assert.equal(
        JSON.parse(value(summaryRoot, "langfuse.observation.output")!)[0].content[0].text,
        "Retain the clear-label recommendation.",
      );
      const summaries = spans.filter((span) => span.name === "compact-history");
      assert.equal(summaries.length, 1);
      const summary = summaries[0]!;
      assert.equal(summary.parentSpanId, summaryRoot.spanId);
      assert.equal(summary.traceId, summaryRoot.traceId);
      assert.ok(value(summary, "langfuse.observation.input"));
      assert.ok(value(summary, "langfuse.observation.output"));
      assert.equal(value(summary, "langfuse.observation.metadata.modelName"), "package-test-model");
      assert.ok(value(summary, "langfuse.observation.metadata.catalogId"));
      assert.ok(
        summary.attributes.some((attribute) => attribute.key === "gen_ai.usage.input_tokens"),
      );
      assert.ok(
        !summaryRoot.attributes.some((attribute) => attribute.key.startsWith("gen_ai.usage.")),
      );
      assert.equal(spans.length, 20, "Only useful turn and compaction observations are exported");

      assert.ok(images.length);

      for (const image of images)
        assert.deepEqual(image, expectedImage, "Original uploaded chart bytes");
      assert.ok(
        spans.every(
          (span) =>
            !["sql.execute", "chat.app.request", "chat.resolve_model", "Chart image"].includes(
              span.name,
            ),
        ),
      );
      assert.ok(!JSON.stringify(spans).includes("sk-lf-package-test"));
      console.log(
        `Verified ${spans.length} rich observations in two turn traces and one maintenance trace in the same session, including chart media and restart continuity.`,
      );
    },
    async close() {
      server.closeAllConnections();
      await new Promise<void>((resolve) => server.close(() => resolve()));
    },
  };
}
