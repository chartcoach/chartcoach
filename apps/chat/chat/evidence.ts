import type { EveMessage, EveDynamicToolPart } from "eve/react";
import {
  answerSchema,
  answerDraftSchema,
  validateAnswer,
  type Answer as AnswerData,
  type AnswerDraftValue,
} from "../shared/answer";
import type { AnswerDraft } from "./use-answer-draft";
import {
  guidelinePreview,
  parseTool,
  type GuidelinePreview,
  type ReadGuideline,
} from "./tool-output";

export interface ConversationOptions {
  draft?: AnswerDraft;
  stoppedTurnIds?: ReadonlySet<string>;
  failedTurnIds?: ReadonlySet<string>;
  interrupted?: boolean;
}
export interface MessageView {
  message: EveMessage;
  guidelines: ReadonlyMap<string, ReadGuideline>;
  answer?: AnswerData;
  drafting: boolean;
  complete: boolean;
  stopped: boolean;
  failed: boolean;
}
export interface EvidenceItem {
  guideline: GuidelinePreview;
  stage: "matched" | "read" | "primary" | "supporting";
}

function projectDraft(
  value: AnswerDraftValue,
  readIds: ReadonlySet<string>,
): AnswerData | undefined {
  if (value.status !== "answer") return;
  const points: AnswerData["points"] = [];
  for (const candidate of value.points ?? []) {
    const point = answerSchema.shape.points.element.safeParse(candidate);
    if (!point.success) break;
    const answer = {
      workflow: value.workflow,
      status: "answer" as const,
      points: [...points, point.data],
      question: null,
    };
    if (!validateAnswer(answer, readIds)) break;
    points.push(point.data);
  }
  return points.length
    ? { workflow: value.workflow, status: "answer", points, question: null }
    : undefined;
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
    const readIds = new Set(guidelines.keys());
    const presentations = parts.filter(
      (part): part is EveDynamicToolPart =>
        part.type === "dynamic-tool" && part.toolName === "present_answer",
    );
    const accepted = presentations.findLast(
      (part) => part.state === "output-available" && !part.partial,
    );
    const finalAnswer =
      accepted?.state === "output-available"
        ? validateAnswer(answerSchema.safeParse(accepted.output).data, readIds)
        : undefined;
    const pending = presentations.at(-1);
    let preview: AnswerData | undefined;
    if (!finalAnswer && !stopped && !failed && pending) {
      if (pending.state === "input-available") {
        const parsed = answerDraftSchema.safeParse(pending.input);
        if (parsed.success) preview = projectDraft(parsed.data, readIds);
      } else if (
        pending.state === "input-streaming" &&
        options.draft &&
        options.draft.toolCallId === pending.toolCallId &&
        options.draft.messageId === message.id
      )
        preview = projectDraft(options.draft.value, readIds);
    }
    const answer = finalAnswer ?? preview;
    if (answer || complete) {
      promotions.clear();
      if (answer?.status === "answer") {
        for (const finding of answer.points) {
          promotions.set(finding.primary_guideline_id, "primary");
        }
        for (const finding of answer.points) {
          for (const id of finding.supporting_guideline_ids) {
            if (promotions.get(id) !== "primary") promotions.set(id, "supporting");
          }
        }
        for (const id of promotions.keys()) retrieved.set(id, guidelines.get(id)!);
      }
    }
    views.push({
      message,
      guidelines: new Map(guidelines),
      answer,
      drafting: !!preview,
      complete,
      stopped,
      failed,
    });
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
