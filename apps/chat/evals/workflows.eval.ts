import { defineEval } from "eve/evals";
import { satisfies } from "eve/evals/expect";
import type { Answer } from "../shared/answer";
import { assertGrounding } from "./assert-grounding";

export default defineEval({
  async test(t) {
    for (const scenario of [
      {
        workflow: "discuss",
        prompt:
          "Compare direct labels and legends for a static line chart with three series. When is each appropriate? Explain the tradeoff using the catalog.",
      },
      {
        workflow: "visrec",
        prompt:
          "I have monthly revenue for four product lines over two years. Readers need to compare trends in a printed management report. Recommend a chart and encoding choices grounded in the catalog.",
      },
    ] as const) {
      const turn = await (await t.session()).send(scenario.prompt);
      const answer = assertGrounding(t, turn, scenario.prompt);
      t.check(
        answer,
        satisfies<Answer>(
          (value) =>
            value.workflow === scenario.workflow &&
            value.points.every((point) => point.assessment === null),
          "selects the requested workflow and explains a design decision",
        ),
      );
    }
  },
});
