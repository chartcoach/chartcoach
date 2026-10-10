import { defineEval } from "eve/evals";
import { assertGrounding } from "./assert-grounding";

export default defineEval({
  async test(t) {
    for (const method of ["vector", "keyword", "hybrid"] as const) {
      const session = await t.session();
      const prompt = `Use ${method} search for legend labels. I have six colored lines with a separate legend. Read a relevant guideline and give one grounded recommendation.`;
      const turn = await session.send(prompt);
      turn.calledTool("search_guidelines", { input: { method }, output: { method } });
      assertGrounding(t, turn, prompt);
    }
  },
});
