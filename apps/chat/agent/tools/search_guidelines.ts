import { defineTool } from "eve/tools";
import { z } from "zod";
import { searchGuidelines } from "../../lib/retrieval/search";
import { sessionSelection } from "../selection-context";

export default defineTool({
  description:
    "Retrieve guidelines by meaning (vector), indexed terms (keyword/BM25), or both (hybrid/RRF). Use keyword for exact catalog terminology and hybrid when terminology and meaning both matter. Read selected IDs before recommending changes.",
  inputSchema: z.object({
    query: z.string().trim().min(1).max(500),
    method: z.enum(["vector", "keyword", "hybrid"]).default("vector"),
  }),
  async execute({ query, method }, ctx) {
    return searchGuidelines(query, method, {
      selection: sessionSelection(ctx.session),
      signal: ctx.abortSignal,
    });
  },
});
