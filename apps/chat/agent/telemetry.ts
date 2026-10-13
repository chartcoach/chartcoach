import {
  isDefaultExportSpan,
  LangfuseSpanProcessor,
  type LangfuseSpanProcessorParams,
} from "@langfuse/otel";
import { SpanKind, type Attributes, type Context, type SpanContext } from "@opentelemetry/api";
import type { ReadableSpan, Span } from "@opentelemetry/sdk-trace-base";
import { randomBytes } from "node:crypto";
import { z } from "zod";
import { TracePayloads, turnKey } from "./trace-payloads";
import { modelTraceSchema } from "./model-trace-state";

const metadataTraceSchema = modelTraceSchema.partial().extend({
  catalogId: z.string().optional(),
  guidelineCount: z.number().optional(),
  catalogReleaseId: z.string().optional(),
  catalogPredicate: z.string().optional(),
  catalogSelectionId: z.string().optional(),
  modelConnectionId: z.string().optional(),
});

function exportSpan(span: ReadableSpan): boolean {
  const scope = span.instrumentationScope.name;

  if (["chartcoach.app", "workflow", "@vercel/otel/fetch"].includes(scope)) return false;

  return scope === "eve.agent" || scope === "chartcoach.compaction" || isDefaultExportSpan(span);
}

export class LangfuseProcessor extends LangfuseSpanProcessor {
  readonly payloads = new TracePayloads();
  private readonly contexts = new Map<string, Attributes>();
  private readonly anchors = new Map<string, SpanContext>();
  private readonly finishedTurns = new Map<string, { sessionId: string; turnId: string }>();
  private readonly pending: ReadableSpan[] = [];

  constructor(options: LangfuseSpanProcessorParams = {}) {
    super({ ...options, shouldExportSpan: ({ otelSpan }) => exportSpan(otelSpan) });
  }

  override onStart(span: Span, parentContext: Context): void {
    if (!exportSpan(span)) {
      super.onStart(span, parentContext);

      return;
    }

    const attributes = span.attributes;
    const runId = z.string().safeParse(attributes["agent.run.id"]);
    const turnId = z.string().safeParse(attributes["agent.turn.id"]);

    if (
      span.instrumentationScope.name === "eve.agent" &&
      span.name === "agent.step" &&
      runId.success &&
      turnId.success &&
      span.parentSpanContext
    )
      this.anchors.set(turnKey(runId.data, turnId.data), span.parentSpanContext);
    const context: Attributes = { ...this.contexts.get(span.spanContext().traceId) };

    for (const key of ["agent.run.id", "agent.turn.id", "agent.step.index", "agent.step.attempt"]) {
      if (attributes[key] !== undefined) context[key] = attributes[key];
    }

    const sessionId = z
      .string()
      .safeParse(
        attributes["gen_ai.conversation.id"] ??
          attributes["agent.session.id"] ??
          attributes["langfuse.session.id"],
      );

    if (sessionId.success) context["session.id"] = sessionId.data;

    const userId = z
      .string()
      .safeParse(
        attributes["ai.settings.context.userId"] ??
          attributes["agent.principal.current.id"] ??
          attributes["agent.principal.initiator.id"],
      );

    if (userId.success) context["user.id"] = userId.data;

    const metadata = metadataTraceSchema.safeParse(
      Object.fromEntries(
        Object.keys(metadataTraceSchema.shape)
          .map((key) => [key, attributes[`ai.settings.context.${key}`]])
          .filter(([, value]) => value !== undefined),
      ),
    );

    if (metadata.success) {
      // A newly resolved connection replaces every model field, including an
      // optional endpoint that the preceding connection may have supplied.
      if (metadata.data.modelConnectionId !== undefined)
        for (const key of Object.keys(modelTraceSchema.shape))
          delete context[`langfuse.observation.metadata.${key}`];

      for (const [key, value] of Object.entries(metadata.data))
        context[`langfuse.observation.metadata.${key}`] = value;
    }

    context["langfuse.trace.name"] = "chartcoach response";
    context["langfuse.trace.tags"] = ["chartcoach", "chat"];
    span.setAttributes(context);

    if (span.instrumentationScope.name !== "chartcoach.compaction") {
      this.contexts.delete(span.spanContext().traceId);
      this.contexts.set(span.spanContext().traceId, context);

      if (this.contexts.size > 1024) {
        const first = this.contexts.keys().next().value;

        if (first !== undefined) this.contexts.delete(first);
      }
    }

    super.onStart(span, parentContext);
  }

  override onEnd(span: ReadableSpan): void {
    if (
      span.instrumentationScope.name === "eve.agent" &&
      span.attributes["gen_ai.operation.name"] === "invoke_agent"
    ) {
      const run = z.string().safeParse(span.attributes["agent.run.id"]);
      const turn = z.string().safeParse(span.attributes["agent.turn.id"]);

      if (run.success && turn.success)
        this.anchors.set(turnKey(run.data, turn.data), span.spanContext());
    }

    if (!exportSpan(span)) {
      super.onEnd(span);

      return;
    }

    // Eve ends native spans before publishing their full lifecycle payloads.
    // Drain after the event batch so its local 32 KiB cap never truncates Langfuse content.
    this.pending.push(copySpan(span));
  }

  private drain(shuttingDown = false): void {
    const spans = this.pending.splice(0);
    const maintenance = new Map<string, { anchor: SpanContext; spans: ReadableSpan[] }>();

    for (const span of spans) {
      const attributes = span.attributes;
      const key = turnKey(String(attributes["agent.run.id"]), String(attributes["agent.turn.id"]));

      if (
        span.instrumentationScope.name !== "chartcoach.compaction" ||
        this.anchors.has(key) ||
        (!shuttingDown && !this.payloads.isTurnSettled(attributes))
      )
        continue;

      let group = maintenance.get(key);

      if (!group) {
        group = {
          anchor: { ...span.spanContext(), spanId: randomBytes(8).toString("hex") },
          spans: [],
        };
        maintenance.set(key, group);
      }

      group.spans.push(span);
    }

    for (let span of spans) {
      const attributes = span.attributes;
      const compaction = span.instrumentationScope.name === "chartcoach.compaction";

      if (compaction) {
        const key = turnKey(
          String(attributes["agent.run.id"]),
          String(attributes["agent.turn.id"]),
        );

        const nativeAnchor = this.anchors.get(key);
        const group = maintenance.get(key);
        const anchor = nativeAnchor ?? group?.anchor;

        if (!anchor) {
          this.pending.push(span);
          continue;
        }

        const original = span.spanContext();
        Object.assign(attributes, { ...this.contexts.get(anchor.traceId), ...attributes });
        span = {
          ...span,
          parentSpanContext: anchor,
          spanContext: () => ({
            ...original,
            traceId: anchor.traceId,
            traceFlags: anchor.traceFlags,
          }),
        };

        if (group) {
          attributes["langfuse.trace.name"] = "chartcoach history compaction";
          attributes["langfuse.trace.tags"] = ["chartcoach", "chat", "compaction"];
        }
      }

      if (!compaction && !shuttingDown && !this.payloads.ready(attributes)) {
        this.pending.push(span);
        continue;
      }

      if (!compaction) this.payloads.enrich(attributes);
      const operation = attributes["gen_ai.operation.name"];

      if (operation === "chat") attributes["langfuse.observation.type"] = "generation";

      if (operation === "invoke_agent") attributes["langfuse.observation.type"] = "agent";

      // Eve constructs its turn root after the steps, beneath a synthetic context.
      // Override the SDK's onStart inference with the actual native topology.
      if (span.instrumentationScope.name === "eve.agent" || compaction)
        attributes["langfuse.internal.is_app_root"] = operation === "invoke_agent";

      for (const [key, value] of Object.entries(attributes))
        if (
          key.startsWith("langfuse.observation.metadata.") &&
          !z.string().safeParse(value).success
        )
          attributes[key] = JSON.stringify(value);

      if (operation === "execute_tool")
        attributes["langfuse.observation.type"] = [
          "search_guidelines",
          "read_guidelines",
          "query_catalog",
        ].includes(String(attributes["gen_ai.tool.name"]))
          ? "retriever"
          : "tool";
      let name = span.name;

      if (operation === "chat") name = compaction ? "compact-history" : "generate-response";

      if (operation === "invoke_agent") name = "respond-to-user";
      super.onEnd({ ...span, name });

      if (operation === "invoke_agent") {
        this.contexts.delete(span.spanContext().traceId);
        const sessionId = String(attributes["agent.run.id"]);
        const turnId = String(attributes["agent.turn.id"]);
        this.finishedTurns.set(turnKey(sessionId, turnId), { sessionId, turnId });
      }
    }

    // Manual compaction can generate several summaries while shrinking the
    // retained window. Group every call beneath one maintenance root when the
    // session parks; automatic compaction keeps its native turn root instead.
    for (const [key, group] of maintenance) {
      const root = maintenanceRoot(group.spans, group.anchor);
      super.onEnd(root);
      this.contexts.delete(group.anchor.traceId);
      this.finishedTurns.set(key, {
        sessionId: String(root.attributes["agent.run.id"]),
        turnId: String(root.attributes["agent.turn.id"]),
      });
    }

    for (const [key, { sessionId, turnId }] of this.finishedTurns) {
      if (
        this.pending.some(
          (span) =>
            span.attributes["agent.run.id"] === sessionId &&
            span.attributes["agent.turn.id"] === turnId,
        )
      )
        continue;
      this.payloads.release(sessionId, turnId);
      this.anchors.delete(key);
      this.finishedTurns.delete(key);
    }
  }

  override async forceFlush(): Promise<void> {
    this.drain();
    await super.forceFlush();
  }

  override async shutdown(): Promise<void> {
    this.drain(true);

    try {
      await super.shutdown();
    } finally {
      this.contexts.clear();
      this.anchors.clear();
      this.finishedTurns.clear();
      this.payloads.clear();
    }
  }
}

function maintenanceRoot(spans: ReadableSpan[], anchor: SpanContext): ReadableSpan {
  const first = spans[0]!;
  const last = spans.at(-1)!;

  const duration: [number, number] = [
    last.endTime[0] - first.startTime[0],
    last.endTime[1] - first.startTime[1],
  ];

  if (duration[1] < 0) {
    duration[0] -= 1;
    duration[1] += 1_000_000_000;
  }

  const attributes: Attributes = {
    ...first.attributes,
    "gen_ai.operation.name": "invoke_agent",
    "langfuse.observation.type": "agent",
    "langfuse.internal.is_app_root": true,
    "langfuse.observation.output": last.attributes["langfuse.observation.output"],
  };

  // Generations own their provider usage and cost. A maintenance root only
  // groups those calls and must not count the same tokens a second time.
  for (const key of Object.keys(attributes))
    if (
      key.startsWith("gen_ai.usage.") ||
      key.startsWith("ai.usage.") ||
      key.startsWith("gen_ai.request.") ||
      key.startsWith("gen_ai.response.") ||
      key === "gen_ai.provider.name"
    )
      delete attributes[key];

  return {
    ...first,
    name: "compact-session",
    kind: SpanKind.INTERNAL,
    parentSpanContext: undefined,
    spanContext: () => anchor,
    attributes,
    endTime: last.endTime,
    duration,
    status: last.status,
    links: [],
    events: [],
  };
}

function copySpan(span: ReadableSpan): ReadableSpan {
  return {
    name: span.name,
    kind: span.kind,
    spanContext: () => span.spanContext(),
    parentSpanContext: span.parentSpanContext,
    startTime: span.startTime,
    endTime: span.endTime,
    status: span.status,
    attributes: { ...span.attributes },
    links: span.links,
    events: span.events,
    duration: span.duration,
    ended: span.ended,
    resource: span.resource,
    instrumentationScope: span.instrumentationScope,
    droppedAttributesCount: span.droppedAttributesCount,
    droppedEventsCount: span.droppedEventsCount,
    droppedLinksCount: span.droppedLinksCount,
  };
}
