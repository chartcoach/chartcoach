import type { EveDynamicToolPart } from "eve/react";
import { z } from "zod";
import { workflowSchema } from "../shared/workflow";

const guideline = z.object({ id: z.string(), title: z.string(), description: z.string() });

export const searchOutput = z.object({
  method: z.enum(["vector", "keyword", "hybrid"]),
  profile: z.string().optional(),
  model: z.string().optional(),
  metric: z.string().optional(),
  dimensions: z.number().optional(),
  ranking: z.string().optional(),
  matches: z.array(guideline.extend({ url: z.string() })),
});

export const describeOutput = z.object({
  tables: z.array(
    z.object({
      name: z.string(),
      rows: z.number(),
      columns: z.array(z.object({ name: z.string(), type: z.string() })),
    }),
  ),
  profiles: z.array(z.string()),
  label_families: z.array(z.object({ name: z.string(), description: z.string() })),
  section_roles: z.array(z.object({ name: z.string(), description: z.string() })),
  limits: z.object({
    default_rows: z.number(),
    max_rows: z.number(),
    max_response_bytes: z.number(),
    timeout_ms: z.number(),
  }),
});

export const sqlOutput = z.object({
  method: z.literal("sql"),
  columns: z.array(z.object({ name: z.string(), type: z.string() })),
  rows: z.array(
    z.array(z.union([z.null(), z.string(), z.json().transform((value) => JSON.stringify(value))])),
  ),
  row_count: z.number(),
  truncated: z.boolean(),
  limit: z.number(),
  matches: z.array(guideline.extend({ url: z.string() })).optional(),
});

export interface GuidelinePreview {
  id: string;
  title: string;
  url: string;
  description?: string;
}

export interface ReadGuideline extends GuidelinePreview {
  description: string;
}

export function guidelinePreview(
  id: string,
  title: string,
  href?: string,
): GuidelinePreview | undefined {
  if (!id || !title.trim() || !href) return;

  try {
    const url = new URL(href);
    const pathname = `/guidelines/${encodeURIComponent(id)}`;

    if (
      url.origin !== "https://chartcoach.dev" ||
      url.username ||
      url.password ||
      url.search ||
      url.hash ||
      (url.pathname !== pathname && url.pathname !== `${pathname}/`)
    )
      return;

    return { id, title, url: `${url.origin}${pathname}` };
  } catch {
    return;
  }
}

export const readOutput = z.object({
  guidelines: z.array(guideline),
  citations: z.array(
    z.object({
      id: z.string(),
      url: z.string(),
      sources: z.array(
        z.object({
          reference_id: z.string(),
          citation: z.string(),
          url: z.string().nullable(),
          doi: z.string().nullable().optional(),
        }),
      ),
    }),
  ),
});

const queryInput = z.object({ query: z.string() });

const searchMethodInput = z.object({ method: z.enum(["vector", "keyword", "hybrid"]) });

const readInput = z.object({ ids: z.array(z.string()) });

const sqlInput = z.object({ sql: z.string() });

const skillInput = z.object({ skill: workflowSchema });

export function parseTool(part: EveDynamicToolPart) {
  const complete = part.state === "output-available" && !part.partial;

  return {
    workflow:
      part.toolName === "load_skill" ? skillInput.safeParse(part.input).data?.skill : undefined,
    method: searchMethodInput.safeParse(part.input).data?.method,
    description:
      complete && part.toolName === "describe_catalog"
        ? describeOutput.safeParse(part.output).data
        : undefined,
    sql: part.toolName === "query_catalog" ? sqlInput.safeParse(part.input).data?.sql : undefined,
    query:
      part.toolName === "search_guidelines"
        ? queryInput.safeParse(part.input).data?.query
        : undefined,
    ids:
      part.toolName === "read_guidelines" ? readInput.safeParse(part.input).data?.ids : undefined,
    search:
      complete && part.toolName === "search_guidelines"
        ? searchOutput.safeParse(part.output).data
        : undefined,
    read:
      complete && part.toolName === "read_guidelines"
        ? readOutput.safeParse(part.output).data
        : undefined,
    sqlResult:
      complete && part.toolName === "query_catalog"
        ? sqlOutput.safeParse(part.output).data
        : undefined,
  };
}
