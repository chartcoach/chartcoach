import { z } from "zod";
import { workflowSchema } from "./workflow";

export const answerSchema = z.object({
  workflow: workflowSchema,
  status: z.enum(["answer", "needs_context", "no_match", "out_of_scope"]),
  points: z
    .array(
      z.object({
        primary_guideline_id: z.string().trim().min(1),
        supporting_guideline_ids: z.array(z.string().trim().min(1)).max(2),
        assessment: z.enum(["respected", "violated", "uncertain"]).nullable(),
        context: z.string().trim().min(1).max(400),
        recommendation: z.string().trim().min(1).max(700),
      }),
    )
    .max(3),
  question: z.string().trim().min(1).max(300).nullable(),
});

export type Answer = z.infer<typeof answerSchema>;

export const answerDraftSchema = z.object({
  workflow: answerSchema.shape.workflow,
  status: answerSchema.shape.status,
  points: z.array(z.unknown()).optional(),
});
export type AnswerDraftValue = z.infer<typeof answerDraftSchema>;

export function answerIssues(answer: Answer, readIds: ReadonlySet<string>): string[] {
  const shape = answerSchema.safeParse(answer);
  if (!shape.success)
    return shape.error.issues.map((issue) => `${issue.path.join(".")}: ${issue.message}`);
  const issues: string[] = [];
  if (answer.status !== "answer") {
    if (answer.points.length) issues.push("Use an empty points array for this status.");
    if (answer.status === "needs_context" ? answer.question === null : answer.question !== null)
      issues.push("Provide a question only for needs_context, otherwise question must be null.");
    return issues;
  }
  if (!answer.points.length) issues.push("An answer requires at least one point.");
  if (answer.question !== null) issues.push("Use question:null for an answer.");
  const primary = new Set<string>();
  const unread = new Set<string>();
  for (const [index, point] of answer.points.entries()) {
    if (primary.has(point.primary_guideline_id))
      issues.push(`Merge points sharing primary guideline ${point.primary_guideline_id}.`);
    primary.add(point.primary_guideline_id);
    if (answer.workflow === "visfeedback" ? point.assessment === null : point.assessment !== null)
      issues.push(
        `Point ${index + 1}: visfeedback requires an assessment. Discuss and visrec require assessment:null.`,
      );
    if (
      new Set(point.supporting_guideline_ids).size !== point.supporting_guideline_ids.length ||
      point.supporting_guideline_ids.includes(point.primary_guideline_id)
    )
      issues.push(
        `Point ${index + 1}: supporting IDs must be distinct and differ from its primary ID.`,
      );
    for (const id of [point.primary_guideline_id, ...point.supporting_guideline_ids])
      if (!readIds.has(id)) unread.add(id);
  }
  if (unread.size)
    issues.push(
      `Read these guideline IDs before citing them: ${[...unread].join(", ")}. Use read_guidelines, or choose entries already read.`,
    );
  return issues;
}

export function validateAnswer(answer: Answer | undefined, readIds: ReadonlySet<string>) {
  return answer && answerIssues(answer, readIds).length === 0 ? answer : undefined;
}
