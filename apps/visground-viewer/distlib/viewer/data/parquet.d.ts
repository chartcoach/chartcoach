import type { CandidateRecord } from "../contract/types";
export type ViewerArtifactRowWire = {
  visgen_id: string;
  vis_id: string;
  query: string;
  search_text: string;
  objective: string | null;
  request_chart: string | null;
  audience: string | null;
  grammar: string | null;
  grounding_mode: string | null;
  model: string | null;
  overall_score: number | null;
  candidate_json: string;
};
export type ViewerArtifactRow = Omit<ViewerArtifactRowWire, "candidate_json"> & {
  candidate: CandidateRecord;
};
export declare function loadViewerArtifactFromParquetUrl(
  url: string,
  requestInit?: RequestInit,
  options?: {
    resolveImageUrl?: (url: string | null) => string | null;
  },
): Promise<ViewerArtifactRow[]>;
//# sourceMappingURL=parquet.d.ts.map
