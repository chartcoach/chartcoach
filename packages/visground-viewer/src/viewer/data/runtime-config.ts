export type ViewerDimensionSpec = {
  id: string;
  label: string;
  nullLabel?: string;
  noneValueMode?: "null" | "all";
  aliases?: Record<string, string>;
  order?: Record<string, number>;
};

export const viewerDimensions = [
  {
    id: "objective",
    label: "Objective",
    aliases: { select: "Select", refine: "Refine" },
    order: { select: 0, refine: 1 },
  },
  {
    id: "request_chart",
    label: "Chart type",
    nullLabel: "All chart types",
    noneValueMode: "all",
  },
  {
    id: "audience",
    label: "Audience",
    nullLabel: "No audience",
    aliases: { novice: "Novice", casual: "Casual", expert: "Expert" },
  },
  {
    id: "grammar",
    label: "Grammar",
    aliases: { altair: "Altair", matplotlib: "Matplotlib", plotly: "Plotly" },
  },
  {
    id: "grounding_mode",
    label: "Grounding",
    aliases: { none: "Ungrounded", hybrid: "Grounded", structured: "Structured" },
    order: { none: 0, hybrid: 1, structured: 2 },
  },
  {
    id: "model",
    label: "Model",
    aliases: {
      "gpt-5.3-codex": "GPT-5.3 Codex",
      "claude-sonnet-4.6": "Claude 4.6",
      "gemini-3.1-pro-preview": "Gemini 3.1",
      "gpt-5.4": "GPT-5.4",
    },
  },
] as const satisfies readonly ViewerDimensionSpec[];

export const viewerFilterDimensions = ["objective", "request_chart", "audience"] as const;
export const viewerAxisDimensions = ["model", "grounding_mode", "grammar"] as const;

export const viewerDefaultSelection = {
  filters: {
    objective: "select",
    request_chart: null,
    audience: null,
  },
  layout: {
    row_dimension: "model",
    column_dimension: "grounding_mode",
    group_dimension: "grammar",
  },
} as const;
