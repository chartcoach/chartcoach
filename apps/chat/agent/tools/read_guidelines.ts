import { defineTool } from "eve/tools";
import { z } from "zod";
import { readGuidelines } from "../../lib/retrieval/read";
import { sessionSelection } from "../selection-context";

export default defineTool({
  description:
    "Read up to three guideline entries with their advice, exceptions, sources, and citation links.",
  inputSchema: z.object({ ids: z.array(z.string().min(1)).min(1).max(3) }),
  async execute({ ids }, ctx) {
    return readGuidelines(ids, {
      selection: sessionSelection(ctx.session),
      signal: ctx.abortSignal,
    });
  },
});
