import { defineEval } from "eve/evals";
import { satisfies } from "eve/evals/expect";
import { reviewSchema, type Review } from "../shared/review";
import { assertGrounding } from "./assert-grounding";

export default defineEval({
  async test(t) {
    const cases = [
      {
        assessment: "respected",
        prompt:
          "My bar chart is for comparing individual absolute magnitudes. It shows three positive values using bars aligned to one clearly labeled zero baseline. Assess this baseline choice using the catalog and give one finding.",
      },
      {
        assessment: "violated",
        prompt:
          "My bar chart must communicate absolute magnitudes at a glance. It compares values 91, 93, and 95, but its value axis starts at 90, so displayed bar lengths are 1, 3, and 5. Assess this baseline choice using the catalog and give one finding.",
      },
    ] as const;
    for (const scenario of cases) {
      const turn = await t.newSession().send(scenario.prompt, { outputSchema: reviewSchema });
      const review = assertGrounding(t, turn, scenario.prompt);
      t.check(
        review.feedback,
        satisfies<Review["feedback"]>(
          (items) => items.length === 1 && items[0].assessment === scenario.assessment,
          `classifies the baseline as ${scenario.assessment}`,
        ),
      );
    }
    const uncertain = await t
      .newSession()
      .send(
        "The screenshot of my bar chart is cropped so the axis baseline and scale labels are not visible. I do not know their values. Can you determine whether it violates the zero-baseline guideline?",
        { outputSchema: reviewSchema },
      );
    uncertain.succeeded();
    uncertain.noFailedActions();
    uncertain.outputMatches(reviewSchema);
    const review = reviewSchema.parse(uncertain.data);
    t.check(
      review,
      satisfies<Review>(
        (value) =>
          value.status === "needs_context" ||
          (value.status === "feedback" &&
            value.feedback.length > 0 &&
            value.feedback.every((item) => item.assessment === "uncertain")),
        "does not infer a violation from missing evidence",
      ),
    );
  },
});
