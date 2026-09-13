import { defineEval } from "eve/evals";
import { assertGrounding } from "./assert-grounding";

export default defineEval({
  async test(t) {
    const prompt =
      "I have a line chart with six colored series and a separate legend. How can I make it easier to read? Search the catalog, read the strongest matches, and cite their sources.";

    const turn = await t.send(prompt);
    assertGrounding(t, turn, prompt);
  },
});
