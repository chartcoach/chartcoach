import {
  isDefaultExportSpan,
  LangfuseSpanProcessor,
  type LangfuseSpanProcessorParams,
} from "@langfuse/otel";
import type { Context } from "@opentelemetry/api";
import type { ReadableSpan, Span } from "@opentelemetry/sdk-trace-base";
import type {
  InstrumentationRuntimeContext,
  InstrumentationRuntimeContextInput,
} from "eve/instrumentation";
import { z } from "zod";
import { parseSelection } from "./selection-context";
import { createHash } from "node:crypto";

const modelTraceSchema = z.object({
  modelConnectionId: z.string(),
  modelConnectionName: z.string(),
  modelProvider: z.string(),
  modelName: z.string(),
  modelEndpointOrigin: z.string().optional(),
  modelContextWindow: z.number(),
  modelManaged: z.boolean(),
});

export const catalogTraceSchema = z.object({
  catalogId: z.string().optional(),
  guidelineCount: z.number().optional(),
  catalogReleaseId: z.string().optional(),
  catalogPredicate: z.string().optional(),
  catalogSelectionId: z.string().optional(),
  modelConnectionId: z.string().optional(),
});

const encodedTraceMetadata = z
  .string()
  .transform((value, context) => {
    try {
      return JSON.parse(value);
    } catch {
      context.addIssue({ code: "custom", message: "Invalid trace metadata." });

      return z.NEVER;
    }
  })
  .pipe(catalogTraceSchema.extend(modelTraceSchema.partial().shape));

export class LangfuseProcessor extends LangfuseSpanProcessor {
  private readonly contexts = new Map<string, Record<string, string>>();

  constructor(options: LangfuseSpanProcessorParams = {}) {
    super({
      ...options,
      shouldExportSpan: ({ otelSpan }) =>
        isDefaultExportSpan(otelSpan) ||
        ["eve.agent", "eve", "gen_ai", "chartcoach.app"].includes(
          otelSpan.instrumentationScope.name,
        ),
    });
  }

  override onStart(span: Span, parentContext: Context): void {
    const attributes = span.attributes;

    const sessionId = z
      .string()
      .safeParse(
        attributes["agent.session.id"] ??
          attributes["langfuse.session.id"] ??
          attributes["gen_ai.conversation.id"] ??
          attributes["ai.settings.context.eve.session.id"],
      );

    const traceId = span.spanContext().traceId;
    const context = { ...this.contexts.get(traceId) };

    if (sessionId.success) context["session.id"] = sessionId.data;
    const userId = z.string().safeParse(attributes["ai.settings.context.userId"]);

    if (userId.success) context["user.id"] = userId.data;

    const metadata = catalogTraceSchema.safeParse(
      Object.fromEntries(
        Object.keys(catalogTraceSchema.shape)
          .map((key) => [key, attributes[`ai.settings.context.${key}`]])
          .filter(([, value]) => value !== undefined),
      ),
    );

    // Eve resolves models on a separate trace before opening the generation span.
    const resolvedModel = encodedTraceMetadata.safeParse(
      this.contexts.get(`model:${context["session.id"]}`)?.["langfuse.trace.metadata"],
    );

    if (resolvedModel.success || (metadata.success && metadata.data.catalogId)) {
      const previous = encodedTraceMetadata.safeParse(context["langfuse.trace.metadata"]);
      context["langfuse.trace.metadata"] = JSON.stringify({
        ...previous.data,
        ...resolvedModel.data,
        ...metadata.data,
      });
    }

    // Eve reconstructs non-recording parent contexts across durable steps.
    // Keep a bounded identity cache for tool spans that carry just the trace ID.
    if (Object.keys(context).length) {
      this.remember(traceId, context);
    }

    span.setAttributes(context);

    if (attributes["langfuse.trace.name"] === undefined) {
      span.setAttribute("langfuse.trace.name", "ChartCoach conversation");
    }

    super.onStart(span, parentContext);
  }

  override onEnd(span: ReadableSpan): void {
    const attributes = { ...span.attributes };

    if (span.name === "chat.resolve_model" && span.instrumentationScope.name === "chartcoach.app") {
      const metadata = encodedTraceMetadata
        .pipe(modelTraceSchema)
        .safeParse(attributes["langfuse.observation.metadata"]);

      if (metadata.success) {
        const traceId = span.spanContext().traceId;
        const saved = this.contexts.get(traceId) ?? {};

        const catalog = encodedTraceMetadata
          .pipe(catalogTraceSchema)
          .safeParse(saved["langfuse.trace.metadata"]);

        attributes["langfuse.trace.metadata"] = JSON.stringify({
          ...catalog.data,
          ...metadata.data,
        });
        saved["langfuse.trace.metadata"] = String(attributes["langfuse.trace.metadata"]);
        this.remember(traceId, saved);

        const session = z
          .string()
          .safeParse(attributes["langfuse.session.id"] ?? attributes["session.id"]);

        if (session.success)
          this.remember(`model:${session.data}`, {
            "session.id": session.data,
            "langfuse.trace.metadata": JSON.stringify(metadata.data),
          });
      }
    }

    if (span.instrumentationScope.name === "chartcoach.app")
      attributes["langfuse.trace.name"] = attributes["langfuse.session.id"]
        ? "ChartCoach conversation"
        : "ChartCoach workspace";

    if (attributes["gen_ai.operation.name"] === "chat") {
      for (const direction of ["input", "output"]) {
        const value = z
          .number()
          .nonnegative()
          .safeParse(attributes[`agent.usage.${direction}_tokens`]);

        if (value.success && attributes[`gen_ai.usage.${direction}_tokens`] === undefined) {
          attributes[`gen_ai.usage.${direction}_tokens`] = value.data;
        }
      }
    }

    super.onEnd({
      name: span.name,
      kind: span.kind,
      spanContext: () => span.spanContext(),
      parentSpanContext: span.parentSpanContext,
      startTime: span.startTime,
      endTime: span.endTime,
      status: span.status,
      attributes,
      links: span.links,
      events: span.events,
      duration: span.duration,
      ended: span.ended,
      resource: span.resource,
      instrumentationScope: span.instrumentationScope,
      droppedAttributesCount: span.droppedAttributesCount,
      droppedEventsCount: span.droppedEventsCount,
      droppedLinksCount: span.droppedLinksCount,
    });
  }

  releaseSession(sessionId: string): void {
    for (const [traceId, context] of this.contexts) {
      if (context["session.id"] === sessionId) this.contexts.delete(traceId);
    }
  }

  private remember(traceId: string, value: Record<string, string>): void {
    this.contexts.delete(traceId);
    this.contexts.set(traceId, value);

    if (this.contexts.size > 1024) {
      const oldest = this.contexts.keys().next().value;

      if (oldest !== undefined) this.contexts.delete(oldest);
    }
  }

  override async shutdown(): Promise<void> {
    try {
      await super.shutdown();
    } finally {
      this.contexts.clear();
    }
  }
}

export function traceContext({
  session,
}: InstrumentationRuntimeContextInput): InstrumentationRuntimeContext {
  const principal = session.auth.initiator;
  const value = principal?.attributes["chartcoach.selection"];
  const selection = value === undefined ? undefined : parseSelection(value);
  const context: Record<string, string | number> = {};

  const connection = z
    .string()
    .safeParse(session.auth.current?.attributes["chartcoach.connection"]);

  if (connection.success) context.modelConnectionId = connection.data;

  if (principal) context.userId = principal.principalId;

  if (selection) {
    context.catalogId = selection.catalogId;
    context.guidelineCount = selection.ids.length;
    context.catalogSelectionId = createHash("sha256")
      .update(
        JSON.stringify({ catalogId: selection.catalogId, ids: [...new Set(selection.ids)].sort() }),
      )
      .digest("hex");
    const release = z.string().safeParse(principal?.attributes["chartcoach.release"]);

    if (release.success) context.catalogReleaseId = release.data;
    const predicate = z.string().safeParse(principal?.attributes["chartcoach.predicate"]);

    if (predicate.success) context.catalogPredicate = predicate.data;
  }

  return context;
}
