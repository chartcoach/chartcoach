export type ViewerDimensionSpec = {
  id: string;
  label: string;
  nullLabel?: string;
  noneValueMode?: "null" | "all";
  aliases?: Record<string, string>;
  order?: Record<string, number>;
};
export declare const viewerDimensions: readonly [
  {
    readonly id: "objective";
    readonly label: "Objective";
    readonly aliases: {
      readonly select: "Select";
      readonly refine: "Refine";
    };
    readonly order: {
      readonly select: 0;
      readonly refine: 1;
    };
  },
  {
    readonly id: "request_chart";
    readonly label: "Chart type";
    readonly nullLabel: "All chart types";
    readonly noneValueMode: "all";
  },
  {
    readonly id: "audience";
    readonly label: "Audience";
    readonly nullLabel: "No audience";
    readonly aliases: {
      readonly novice: "Novice";
      readonly casual: "Casual";
      readonly expert: "Expert";
    };
  },
  {
    readonly id: "grammar";
    readonly label: "Grammar";
    readonly aliases: {
      readonly altair: "Altair";
      readonly matplotlib: "Matplotlib";
      readonly plotly: "Plotly";
    };
  },
  {
    readonly id: "grounding_mode";
    readonly label: "Grounding";
    readonly aliases: {
      readonly none: "Ungrounded";
      readonly hybrid: "Grounded";
      readonly structured: "Structured";
    };
    readonly order: {
      readonly none: 0;
      readonly hybrid: 1;
      readonly structured: 2;
    };
  },
  {
    readonly id: "model";
    readonly label: "Model";
    readonly aliases: {
      readonly "gpt-5.3-codex": "GPT-5.3 Codex";
      readonly "claude-sonnet-4.6": "Claude 4.6";
      readonly "gemini-3.1-pro-preview": "Gemini 3.1";
      readonly "gpt-5.4": "GPT-5.4";
    };
  },
];
export declare const viewerFilterDimensions: readonly ["objective", "request_chart", "audience"];
export declare const viewerAxisDimensions: readonly ["model", "grounding_mode", "grammar"];
export declare const viewerDefaultSelection: {
  readonly filters: {
    readonly objective: "select";
    readonly request_chart: null;
    readonly audience: null;
  };
  readonly layout: {
    readonly row_dimension: "model";
    readonly column_dimension: "grounding_mode";
    readonly group_dimension: "grammar";
  };
};
//# sourceMappingURL=runtime-config.d.ts.map
