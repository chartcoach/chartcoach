import { defineEval } from "eve/evals";
import { reviewSchema } from "../shared/review";
import { assertGrounding } from "./assert-grounding";

export default defineEval({
  async test(t) {
    const prompt =
      "Explore the catalog schema, then use DuckDB SQL to find a guideline whose title includes label and whose source year is 2020 or later. Read one returned guideline and explain how it can help a line chart with six series and a separate legend. Use SQL for retrieval, not semantic search.";
    const turn = await t.send(prompt, { outputSchema: reviewSchema });
    turn.calledTool("describe_catalog");
    turn.calledTool("query_catalog", { output: { method: "sql" } });
    assertGrounding(t, turn, prompt);
  },
});
