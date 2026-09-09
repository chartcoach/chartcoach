import { z } from "zod";

export const reviewSchema = z.object({
  status: z.enum(["feedback", "needs_context", "no_match", "out_of_scope"]),
  feedback: z
    .array(
      z.object({
        primary_guideline_id: z.string().trim().min(1),
        supporting_guideline_ids: z.array(z.string().trim().min(1)).max(2),
        assessment: z.enum(["respected", "violated", "uncertain"]),
        observation: z.string().trim().min(1).max(400),
        recommendation: z.string().trim().min(1).max(700),
      }),
    )
    .max(3),
  question: z.string().trim().min(1).max(300).nullable(),
});

export type Review = z.infer<typeof reviewSchema>;

export function validateReview(review: Review | undefined, readIds: ReadonlySet<string>) {
  if (!review) return;
  if (review.status !== "feedback") {
    return review.feedback.length === 0 &&
      (review.status === "needs_context" ? review.question !== null : review.question === null)
      ? review
      : undefined;
  }
  const primary = new Set(review.feedback.map((item) => item.primary_guideline_id));
  if (
    !review.feedback.length ||
    review.question !== null ||
    primary.size !== review.feedback.length
  )
    return;
  const valid = review.feedback.every(
    (item) =>
      readIds.has(item.primary_guideline_id) &&
      new Set(item.supporting_guideline_ids).size === item.supporting_guideline_ids.length &&
      item.supporting_guideline_ids.every((id) => readIds.has(id) && !primary.has(id)),
  );
  return valid ? review : undefined;
}
