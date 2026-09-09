import { defineTool } from "eve/tools";
import { z } from "zod";
import { queryCatalog } from "../../lib/retrieval/sql";
import { sessionSelection } from "../selection-context";

export default defineTool({
  description:
    "Run one read-only DuckDB SELECT against catalog tables for filtering, joins, counts, and source analysis. Call describe_catalog for columns and vocabulary. Return id or guideline_id to retrieve guideline cards, then read selected guidelines before giving advice. SQL rows are bounded to 50 rows and 64 KiB with a 5-second deadline. BIGINT and DECIMAL values are strings.",
  inputSchema: z.object({
    sql: z.string().min(1).max(8_000),
    limit: z.number().int().min(1).max(50).default(20),
  }),
  async execute({ sql, limit }, ctx) {
    return queryCatalog(sql, {
      selection: sessionSelection(ctx.session),
      signal: ctx.abortSignal,
      limit,
    });
  },
});
