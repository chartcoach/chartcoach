import type { RefObject } from "react";

export type AnywidgetModelLike = {
  get(name: string): unknown;
  set(name: string, value: unknown): void;
  save_changes(): void;
  on(name: string, callback: (...args: unknown[]) => void): void;
  off(name: string, callback: (...args: unknown[]) => void): void;
  send?(content: unknown): void;
};

export type ViewerSelection = {
  vis_id: string;
  request_chart: string | null;
  objective: string;
  overview_variant: string;
  dimension_filters: Record<string, string | null>;
};

export type CatalogEntry = {
  vis_id: string;
  nl_query: string;
  request_chart: string | null;
};

export type ViewerOption = {
  value: string | null;
  label: string;
};

export type ViewerVariantOption = {
  value: string;
  label: string;
};

export type ViewerFilterControl = {
  id: string;
  label: string;
  options: ViewerOption[];
  value: string | null;
};

export type ViewerToolbarPill = {
  id: "objective" | "compare";
  label: string;
};

export type MatrixAxes = {
  group_label: string | null;
  row_label: string;
  column_label: string;
};

export type CandidateImageMeta = {
  width: number | null;
  height: number | null;
  aspect_ratio: number | null;
  aspect_kind: "standard" | "landscape" | "portrait" | string;
  is_extreme_aspect: boolean;
};

export type ScoreBreakdownDimension = "overall" | "faithfulness" | "expressiveness" | "aesthetics";

export type CandidateScore = {
  id: string;
  label: string;
  dimension: ScoreBreakdownDimension;
  score: number | null;
};

export type CandidateRecord = {
  visgen_id: string;
  error?: string | null;
  image_url?: string | null;
  image_meta?: CandidateImageMeta | null;
  guideline_count: number;
  overall_score?: number | null;
  score_breakdown: CandidateScore[];
};

export type AssetPayload = {
  visgen_id: string;
  variant: "hover" | "detail";
  image_url: string | null;
  image_meta: CandidateImageMeta | null;
  error?: string | null;
};

export type AssetPayloads = {
  assets: AssetPayload[];
};

export type MatrixAxisValue = {
  value: string | null;
  label: string;
};

export type MatrixCell = {
  cell_key: string;
  candidate: CandidateRecord | null;
  missing?: boolean;
  placeholder_reason?: string | null;
  group_value?: string | null;
  group_label?: string | null;
  row_value: string | null;
  row_label: string;
  column_value: string | null;
  column_label: string;
};

export type MatrixRow = MatrixAxisValue & {
  cells: MatrixCell[];
};

export type MatrixGroup = MatrixAxisValue & {
  columns: MatrixAxisValue[];
  rows: MatrixRow[];
};

export type GroupedMatrixPayload = {
  kind: "grouped";
  groups: MatrixGroup[];
};

export type FlatMatrixPayload = {
  kind: "flat";
  columns: MatrixAxisValue[];
  rows: MatrixRow[];
};

export type MatrixPayload = GroupedMatrixPayload | FlatMatrixPayload;

export type ViewerUiSchema = {
  toolbar?: {
    pills: ViewerToolbarPill[];
  };
  scope_filters: ViewerFilterControl[];
  variant_controls?: {
    label: string;
    value: string;
    options: ViewerVariantOption[];
  };
  matrix_axes: MatrixAxes;
};

export type OverviewPayload = {
  nl_query: string;
  matrix: MatrixPayload;
  ui_schema: ViewerUiSchema;
};

export type ViewerStatePayload = {
  catalog: CatalogEntry[];
  overview: OverviewPayload | null;
  error: string | null;
};

export type ViewerHoverState = {
  cell: MatrixCell;
  anchor: HTMLElement;
};

export type ViewerAssetsState = Record<string, Partial<Record<"hover" | "detail", AssetPayload>>>;
export type ViewerBusyState = "initial" | "case" | "update" | null;

export type ViewerState = {
  catalog: CatalogEntry[];
  selection: ViewerSelection;
  overview: OverviewPayload | null;
  searchTerm: string;
  busy: ViewerBusyState;
  error: string | null;
  hover: ViewerHoverState | null;
  inspectCellKey: string | null;
  activePopoverId: "case" | "objective" | "compare" | null;
  popoverAnchor: HTMLElement | null;
  assets: ViewerAssetsState;
};

export type ViewerRefs = {
  rootRef: RefObject<HTMLDivElement | null>;
  hoverCardRef: RefObject<HTMLDivElement | null>;
  popoverRef: RefObject<HTMLDivElement | null>;
};

export type ViewerActions = {
  stepCase(delta: number): void;
  jumpToCase(visId: string): void;
  changeScopeFilter(filterId: string, value: string | null): void;
  changeOverviewVariant(value: string): void;
  togglePopover(popoverId: "case" | "objective" | "compare", anchor: HTMLElement): void;
  closePopover(): void;
  openInspect(cellKey: string): void;
  closeInspect(): void;
  showHover(cell: MatrixCell, anchor: HTMLElement): void;
  scheduleHoverHide(): void;
  cancelHoverHide(): void;
  hideHover(immediate?: boolean): void;
  updateSearchTerm(value: string): void;
};

export type ViewerController = {
  state: ViewerState;
  refs: ViewerRefs;
  actions: ViewerActions;
};
