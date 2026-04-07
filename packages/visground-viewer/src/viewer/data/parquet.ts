import { asyncBufferFromUrl, parquetReadObjects } from "hyparquet";
import { compressors } from "hyparquet-compressors";
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

async function loadParquetFile(url: string, requestInit?: RequestInit) {
  try {
    return await asyncBufferFromUrl({
      url,
      requestInit,
    });
  } catch (error) {
    const response = await fetch(url, requestInit);
    if (!response.ok) {
      throw new Error(
        `failed to load parquet artifact from ${url}: ${
          error instanceof Error ? error.message : String(error)
        }; fallback fetch failed ${response.status}`,
      );
    }
    return await response.arrayBuffer();
  }
}

export async function loadViewerArtifactFromParquetUrl(
  url: string,
  requestInit?: RequestInit,
  options?: {
    resolveImageUrl?: (url: string | null) => string | null;
  },
): Promise<ViewerArtifactRow[]> {
  const file = await loadParquetFile(url, requestInit);
  const rows = (await parquetReadObjects({
    file,
    compressors,
  })) as ViewerArtifactRowWire[];

  return rows.map((row) => ({
    ...row,
    overall_score:
      row.overall_score === null || row.overall_score === undefined
        ? null
        : Number(row.overall_score),
    candidate: (() => {
      const candidate = JSON.parse(row.candidate_json) as CandidateRecord;
      const nextImageUrl = options?.resolveImageUrl?.(candidate.image_url ?? null);
      return nextImageUrl === undefined
        ? candidate
        : {
            ...candidate,
            image_url: nextImageUrl,
          };
    })(),
  }));
}
