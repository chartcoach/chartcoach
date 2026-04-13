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

type ParquetSource = Awaited<ReturnType<typeof asyncBufferFromUrl>> | ArrayBuffer;

type ParquetLoaderDependencies = {
  fetch: typeof fetch;
  openUrlBuffer: typeof asyncBufferFromUrl;
  readObjects: typeof parquetReadObjects;
};

const defaultParquetLoaderDependencies: ParquetLoaderDependencies = {
  fetch: globalThis.fetch.bind(globalThis),
  openUrlBuffer: asyncBufferFromUrl,
  readObjects: parquetReadObjects,
};

async function fetchParquetArrayBuffer(
  url: string,
  requestInit: RequestInit | undefined,
  dependencies: ParquetLoaderDependencies,
): Promise<ArrayBuffer> {
  const response = await dependencies.fetch(url, requestInit);
  if (!response.ok) {
    throw new Error(`fallback fetch failed ${response.status}`);
  }
  return await response.arrayBuffer();
}

async function readParquetObjects(
  file: ParquetSource,
  dependencies: ParquetLoaderDependencies,
): Promise<ViewerArtifactRowWire[]> {
  return (await dependencies.readObjects({
    file,
    compressors,
  })) as ViewerArtifactRowWire[];
}

export async function loadViewerArtifactRowsFromParquetUrl(
  url: string,
  requestInit?: RequestInit,
  dependencies: Partial<ParquetLoaderDependencies> = {},
): Promise<ViewerArtifactRowWire[]> {
  const resolvedDependencies = {
    ...defaultParquetLoaderDependencies,
    ...dependencies,
  } satisfies ParquetLoaderDependencies;

  try {
    const primaryFile = await resolvedDependencies.openUrlBuffer({
      url,
      requestInit,
    });
    return await readParquetObjects(primaryFile, resolvedDependencies);
  } catch (primaryError) {
    try {
      const bufferedFile = await fetchParquetArrayBuffer(url, requestInit, resolvedDependencies);
      return await readParquetObjects(bufferedFile, resolvedDependencies);
    } catch (fallbackError) {
      throw new Error(
        `failed to load parquet artifact from ${url}: ${primaryError instanceof Error ? primaryError.message : String(primaryError)}; ${fallbackError instanceof Error ? fallbackError.message : String(fallbackError)}`,
      );
    }
  }
}

export async function loadViewerArtifactFromParquetUrl(
  url: string,
  requestInit?: RequestInit,
  options?: {
    resolveImageUrl?: (url: string | null) => string | null;
  },
): Promise<ViewerArtifactRow[]> {
  const rows = await loadViewerArtifactRowsFromParquetUrl(url, requestInit);

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
