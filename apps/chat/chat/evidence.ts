import type { EveMessage } from "eve/react";
import { reviewSchema, validateReview, type Review as ReviewData } from "../shared/review";
import {
  guidelinePreview,
  parseTool,
  type GuidelinePreview,
  type ReadGuideline,
} from "./tool-output";

export interface ConversationOptions {
  stoppedTurnIds?: ReadonlySet<string>;
  failedTurnIds?: ReadonlySet<string>;
  interrupted?: boolean;
}
export interface MessageView {
  message: EveMessage;
  guidelines: ReadonlyMap<string, ReadGuideline>;
  review?: ReviewData;
  complete: boolean;
  stopped: boolean;
  failed: boolean;
}
export interface EvidenceItem {
  guideline: GuidelinePreview;
  stage: "matched" | "read" | "primary" | "supporting";
}

export function deriveConversation(
  messages: readonly EveMessage[],
  options: ConversationOptions = {},
) {
  const lastAssistant = messages.findLast((message) => message.role === "assistant");
  const guidelines = new Map<string, ReadGuideline>();
  const retrieved = new Map<string, GuidelinePreview>();
  const promotions = new Map<string, "primary" | "supporting">();
  const views: MessageView[] = [];
  for (const message of messages) {
    const { role, parts, metadata } = message;
    if (role === "user") {
      retrieved.clear();
      promotions.clear();
    }
    if (role === "assistant") {
      for (const part of parts) {
        if (part.type !== "dynamic-tool" || part.state !== "output-available" || part.partial)
          continue;
        const parsed = parseTool(part);
        if (part.toolName === "search_guidelines" || part.toolName === "query_catalog") {
          const output = parsed.search ?? parsed.sqlResult;
          for (const match of output?.matches ?? []) {
            const preview = guidelinePreview(match.id, match.title, match.url);
            if (preview) retrieved.set(preview.id, preview);
          }
        }
        if (part.toolName !== "read_guidelines") continue;
        const read = parsed.read;
        for (const guideline of read?.guidelines ?? []) {
          const citation = read?.citations.find((item) => item.id === guideline.id);
          const preview = guidelinePreview(guideline.id, guideline.title, citation?.url);
          if (!preview) continue;
          guidelines.set(preview.id, { ...preview, description: guideline.description });
          retrieved.set(preview.id, preview);
        }
      }
    }
    const turnId = metadata?.turnId;
    const stopped = Boolean(turnId && options.stoppedTurnIds?.has(turnId));
    const failed =
      metadata?.status === "failed" ||
      Boolean(
        metadata?.status !== "complete" &&
        ((turnId && options.failedTurnIds?.has(turnId)) ||
          (options.interrupted && message === lastAssistant)),
      );
    const complete = role === "assistant" && metadata?.status === "complete" && !stopped && !failed;
    const review = complete
      ? validateReview(reviewSchema.safeParse(metadata?.result).data, new Set(guidelines.keys()))
      : undefined;
    if (complete) {
      promotions.clear();
      if (review?.status === "feedback") {
        for (const finding of review.feedback) {
          promotions.set(finding.primary_guideline_id, "primary");
          for (const id of finding.supporting_guideline_ids) promotions.set(id, "supporting");
        }
        for (const id of promotions.keys()) retrieved.set(id, guidelines.get(id)!);
      }
    }
    views.push({ message, guidelines: new Map(guidelines), review, complete, stopped, failed });
  }
  const evidence: EvidenceItem[] = Array.from(
    new Set([...promotions.keys(), ...retrieved.keys()]),
    (id) => ({
      guideline: retrieved.get(id)!,
      stage: promotions.get(id) ?? (guidelines.has(id) ? "read" : "matched"),
    }),
  );
  return { messages: views, evidence };
}
