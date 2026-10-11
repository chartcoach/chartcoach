import { createHash } from "node:crypto";
import type { InstrumentationRuntimeContextInput } from "eve/instrumentation";
import { z } from "zod";
import { modelTraceSchema, resolvedModelTrace } from "./model-trace-state";
import { parseSelection } from "./selection-context";

export function traceContext({
  session,
  turn,
}: Pick<InstrumentationRuntimeContextInput, "session" | "turn">): Record<
  string,
  string | number | boolean
> {
  const principal = session.auth.initiator ?? session.auth.current;
  const value = principal?.attributes["chartcoach.selection"];
  const selection = value === undefined ? undefined : parseSelection(value);
  const context: Record<string, string | number | boolean> = {};

  const connection = z
    .string()
    .safeParse(session.auth.current?.attributes["chartcoach.connection"]);

  if (connection.success) context.modelConnectionId = connection.data;

  const resolved = resolvedModelTrace.get();

  if (resolved?.sessionId === session.id && resolved.turnId === turn.id) {
    const metadata = modelTraceSchema.safeParse(resolved.metadata);

    if (metadata.success)
      for (const [key, item] of Object.entries(metadata.data))
        if (item !== undefined) context[key] = item;
  }

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
