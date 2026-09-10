import { defineTool } from "eve/tools";
import { answerSchema, answerIssues } from "../../shared/answer";
import { readGuidelineIds } from "../evidence-state";

export default defineTool({
  description:
    "Display the completed answer after validating its guideline citations. Correct any reported errors and call this tool again. After success, finish with a brief acknowledgment and no more tools.",
  inputSchema: answerSchema,
  outputSchema: answerSchema,
  execute(answer) {
    const issues = answerIssues(answer, new Set(readGuidelineIds.get()));
    if (issues.length) throw new Error(issues.join("\n"));
    return answer;
  },
  toModelOutput() {
    return {
      type: "text",
      value: "Answer displayed. Finish with a brief acknowledgment and no more tools.",
    };
  },
});
