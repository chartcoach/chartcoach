import { defineTool } from "eve/tools";
import { z } from "zod";
import { describeCatalog } from "../../lib/retrieval/sql";
import { sessionSelection } from "../selection-context";

export default defineTool({
  description:
    "Inspect catalog table names, columns, row counts, section roles, label families, and index profiles before SQL queries. Join sections, guideline_labels, and guideline_sources to guidelines.id through guideline_id. Counts and source metadata describe catalog coverage, not chart-design recommendations.",
  inputSchema: z.object({}),
  async execute(_input, ctx) {
    return describeCatalog({
      selection: sessionSelection(ctx.session),
      signal: ctx.abortSignal,
    });
  },
});
