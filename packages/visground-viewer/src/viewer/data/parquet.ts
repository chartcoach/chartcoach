import { asyncBufferFromUrl, parquetReadObjects } from "hyparquet";
import { compressors } from "hyparquet-compressors";
import type {
  CandidateGuidelineDetail,
  CandidateImageMeta,
  CandidateRecord,
  CandidateScore,
  CandidateScoreRun,
  ScoreBreakdownDimension,
  ViewerRuntimeConfig,
} from "../contract/types";

export type ViewerArtifactRowWire = {
  visgen_id: string;
  vis_id: string;
  query: string;
  search_text: string;
  overall_score: number | null;
  candidate_json: string;
} & Record<string, unknown>;

export type ViewerArtifactRow = {
  visgen_id: string;
  vis_id: string;
  query: string;
  search_text: string;
  overall_score: number | null;
  dimension_values: Record<string, string | null>;
  candidate: CandidateRecord;
};

type ParquetSource = Awaited<ReturnType<typeof asyncBufferFromUrl>>;

export type ParquetLoaderDependencies = {
  openUrlBuffer: typeof asyncBufferFromUrl;
  readObjects: typeof parquetReadObjects;
};

export type ViewerArtifactLoadOptions = {
  runtimeConfig: ViewerRuntimeConfig;
  resolveImageUrl?: (url: string | null) => string | null;
  dependencies?: Partial<ParquetLoaderDependencies>;
};

const defaultParquetLoaderDependencies: ParquetLoaderDependencies = {
  openUrlBuffer: asyncBufferFromUrl,
  readObjects: parquetReadObjects,
};

class ViewerArtifactValidationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "ViewerArtifactValidationError";
  }
}

function hasOwn<K extends PropertyKey>(value: object, key: K): value is Record<K, unknown> {
  return Object.prototype.hasOwnProperty.call(value, key);
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function ensureString(value: unknown, field: string, options?: { allowEmpty?: boolean }): string {
  if (typeof value !== "string" || (!options?.allowEmpty && value.length === 0)) {
    throw new Error(`${field} must be ${options?.allowEmpty ? "a string" : "a non-empty string"}.`);
  }
  return value;
}

function ensureOptionalString(value: unknown, field: string): string | null | undefined {
  if (value === undefined) {
    return undefined;
  }
  if (value === null) {
    return null;
  }
  return ensureString(value, field, { allowEmpty: true });
}

function ensureNumberOrNull(value: unknown, field: string): number | null {
  if (value === null || value === undefined) {
    return null;
  }
  if (typeof value !== "number" || !Number.isFinite(value)) {
    throw new Error(`${field} must be a finite number or null.`);
  }
  return value;
}

function ensureBoolean(value: unknown, field: string): boolean {
  if (typeof value !== "boolean") {
    throw new Error(`${field} must be a boolean.`);
  }
  return value;
}

function ensureStringArray(value: unknown, field: string): string[] {
  if (!Array.isArray(value)) {
    throw new Error(`${field} must be an array.`);
  }
  return value.map((entry, index) =>
    ensureString(entry, `${field}[${index}]`, { allowEmpty: true }),
  );
}

function parseDimensionValue(value: unknown, field: string): string | null {
  if (typeof value === "string" || value === null) {
    return value;
  }
  throw new Error(`${field} must be a string or null.`);
}

function parseDimensionValues(value: unknown, field: string): Record<string, string | null> {
  if (!isRecord(value)) {
    throw new Error(`${field} must be an object.`);
  }
  return Object.fromEntries(
    Object.entries(value).map(([key, entry]) => [
      key,
      parseDimensionValue(entry, `${field}.${key}`),
    ]),
  );
}

const scoreBreakdownDimensions = new Set<ScoreBreakdownDimension>([
  "overall",
  "faithfulness",
  "expressiveness",
  "aesthetics",
]);

function parseScoreDimension(value: unknown, field: string): ScoreBreakdownDimension {
  const dimension = ensureString(value, field) as ScoreBreakdownDimension;
  if (!scoreBreakdownDimensions.has(dimension)) {
    throw new Error(`${field} must be a known score dimension.`);
  }
  return dimension;
}

function parseScoreRun(value: unknown, field: string): CandidateScoreRun {
  if (!isRecord(value)) {
    throw new Error(`${field} must be an object.`);
  }
  return {
    run_id: ensureString(value.run_id, `${field}.run_id`, { allowEmpty: true }),
    label: ensureString(value.label, `${field}.label`, { allowEmpty: true }),
    score: ensureNumberOrNull(value.score, `${field}.score`),
    reasoning: ensureOptionalString(value.reasoning, `${field}.reasoning`) ?? null,
  };
}

function parseScore(value: unknown, field: string): CandidateScore {
  if (!isRecord(value)) {
    throw new Error(`${field} must be an object.`);
  }
  if (!Array.isArray(value.runs)) {
    throw new Error(`${field}.runs must be an array.`);
  }
  return {
    id: ensureString(value.id, `${field}.id`),
    label: ensureString(value.label, `${field}.label`),
    dimension: parseScoreDimension(value.dimension, `${field}.dimension`),
    score: ensureNumberOrNull(value.score, `${field}.score`),
    reasoning: ensureOptionalString(value.reasoning, `${field}.reasoning`) ?? null,
    runs: value.runs.map((entry, index) => parseScoreRun(entry, `${field}.runs[${index}]`)),
  };
}

function parseGuidelineDetail(value: unknown, field: string): CandidateGuidelineDetail {
  if (!isRecord(value)) {
    throw new Error(`${field} must be an object.`);
  }
  return {
    id: ensureString(value.id, `${field}.id`),
    title: ensureString(value.title, `${field}.title`, { allowEmpty: true }),
    url: ensureOptionalString(value.url, `${field}.url`) ?? null,
    description: ensureString(value.description, `${field}.description`, { allowEmpty: true }),
    sources: ensureStringArray(value.sources, `${field}.sources`),
  };
}

function parseImageMeta(value: unknown, field: string): CandidateImageMeta | null {
  if (value === undefined || value === null) {
    return null;
  }
  if (!isRecord(value)) {
    throw new Error(`${field} must be an object or null.`);
  }
  return {
    width: ensureNumberOrNull(value.width, `${field}.width`),
    height: ensureNumberOrNull(value.height, `${field}.height`),
    aspect_ratio: ensureNumberOrNull(value.aspect_ratio, `${field}.aspect_ratio`),
    aspect_kind: ensureString(value.aspect_kind, `${field}.aspect_kind`),
    is_extreme_aspect: ensureBoolean(value.is_extreme_aspect, `${field}.is_extreme_aspect`),
  };
}

function parseCandidateRecord(value: unknown, field: string): CandidateRecord {
  if (!isRecord(value)) {
    throw new Error(`${field} must be an object.`);
  }
  if (!Array.isArray(value.guideline_details)) {
    throw new Error(`${field}.guideline_details must be an array.`);
  }
  if (!Array.isArray(value.score_breakdown)) {
    throw new Error(`${field}.score_breakdown must be an array.`);
  }
  const guidelineCount = value.guideline_count;
  if (
    typeof guidelineCount !== "number" ||
    !Number.isInteger(guidelineCount) ||
    guidelineCount < 0
  ) {
    throw new Error(`${field}.guideline_count must be a non-negative integer.`);
  }
  return {
    visgen_id: ensureString(value.visgen_id, `${field}.visgen_id`),
    dimension_values: parseDimensionValues(value.dimension_values, `${field}.dimension_values`),
    error: ensureOptionalString(value.error, `${field}.error`) ?? null,
    image_url: ensureOptionalString(value.image_url, `${field}.image_url`) ?? null,
    image_meta: parseImageMeta(value.image_meta, `${field}.image_meta`),
    guideline_count: guidelineCount,
    guideline_details: value.guideline_details.map((entry, index) =>
      parseGuidelineDetail(entry, `${field}.guideline_details[${index}]`),
    ),
    overall_score:
      value.overall_score === undefined
        ? undefined
        : ensureNumberOrNull(value.overall_score, `${field}.overall_score`),
    score_breakdown: value.score_breakdown.map((entry, index) =>
      parseScore(entry, `${field}.score_breakdown[${index}]`),
    ),
  };
}

function parseCandidateJson(value: unknown, field: string): CandidateRecord {
  const source = ensureString(value, field);
  try {
    return parseCandidateRecord(JSON.parse(source), field);
  } catch (error) {
    if (error instanceof SyntaxError) {
      throw new Error(`${field} must be valid JSON.`);
    }
    throw error;
  }
}

function parseViewerArtifactRowWire(value: unknown, index: number): ViewerArtifactRowWire {
  const field = `rows[${index}]`;
  if (!isRecord(value)) {
    throw new Error(`${field} must be an object.`);
  }
  return {
    ...value,
    visgen_id: ensureString(value.visgen_id, `${field}.visgen_id`),
    vis_id: ensureString(value.vis_id, `${field}.vis_id`),
    query: ensureString(value.query, `${field}.query`, { allowEmpty: true }),
    search_text: ensureString(value.search_text, `${field}.search_text`, { allowEmpty: true }),
    overall_score: ensureNumberOrNull(value.overall_score, `${field}.overall_score`),
    candidate_json: ensureString(value.candidate_json, `${field}.candidate_json`),
  };
}

export function parseViewerArtifactRows(value: unknown): ViewerArtifactRowWire[] {
  if (!Array.isArray(value)) {
    throw new ViewerArtifactValidationError("Parquet artifact must contain row objects.");
  }
  return value.map((row, index) => {
    try {
      return parseViewerArtifactRowWire(row, index);
    } catch (error) {
      if (error instanceof ViewerArtifactValidationError) {
        throw error;
      }
      throw new ViewerArtifactValidationError(
        error instanceof Error ? error.message : String(error),
      );
    }
  });
}

async function readParquetObjects(
  file: ParquetSource,
  dependencies: ParquetLoaderDependencies,
): Promise<ViewerArtifactRowWire[]> {
  const rows = await dependencies.readObjects({
    file,
    compressors,
  });
  return parseViewerArtifactRows(rows);
}

function normalizeDimensionValues(
  row: ViewerArtifactRowWire,
  runtimeConfig: ViewerRuntimeConfig,
): Record<string, string | null> {
  const rowId = String(row.visgen_id);
  const values: Record<string, string | null> = {};

  for (const dimension of runtimeConfig.dimensions) {
    if (!hasOwn(row, dimension.id)) {
      throw new Error(
        `Viewer artifact row ${rowId} is missing configured dimension '${dimension.id}'.`,
      );
    }

    values[dimension.id] = parseDimensionValue(row[dimension.id], `row.${dimension.id}`);
  }

  return values;
}

function normalizeScoreBreakdown(
  candidate: CandidateRecord,
  rowOverallScore: number | null,
  rowId: string,
): CandidateScore[] {
  let hasOverallScore = false;
  return candidate.score_breakdown.map((score) => {
    if (score.id !== "overall") {
      return score;
    }
    if (hasOverallScore) {
      throw new Error(
        `Viewer artifact row ${rowId} has duplicate overall score_breakdown entries.`,
      );
    }
    hasOverallScore = true;
    if (score.score !== rowOverallScore) {
      throw new Error(
        `Viewer artifact row ${rowId} has conflicting score_breakdown overall score.`,
      );
    }
    return {
      ...score,
      score: rowOverallScore,
    };
  });
}

function normalizeArtifactRow(
  row: ViewerArtifactRowWire,
  options: ViewerArtifactLoadOptions,
): ViewerArtifactRow {
  const rowId = String(row.visgen_id);
  const candidate = parseCandidateJson(row.candidate_json, `candidate_json for row ${rowId}`);
  if (candidate.visgen_id !== rowId) {
    throw new Error(
      `Viewer artifact row ${rowId} has conflicting candidate_json.visgen_id '${candidate.visgen_id}'.`,
    );
  }
  const rowOverallScore =
    row.overall_score === null || row.overall_score === undefined ? null : row.overall_score;
  if (candidate.overall_score !== undefined && candidate.overall_score !== rowOverallScore) {
    throw new Error(`Viewer artifact row ${rowId} has conflicting overall_score values.`);
  }
  const nextImageUrl = options?.resolveImageUrl?.(candidate.image_url ?? null);
  const dimensionValues = normalizeDimensionValues(row, options.runtimeConfig);
  const scoreBreakdown = normalizeScoreBreakdown(candidate, rowOverallScore, rowId);
  const normalizedCandidate =
    nextImageUrl === undefined
      ? candidate
      : {
          ...candidate,
          image_url: nextImageUrl,
        };

  return {
    visgen_id: rowId,
    vis_id: String(row.vis_id),
    query: String(row.query ?? ""),
    search_text: String(row.search_text ?? ""),
    overall_score: rowOverallScore,
    dimension_values: dimensionValues,
    candidate: {
      ...normalizedCandidate,
      overall_score: rowOverallScore,
      score_breakdown: scoreBreakdown,
      dimension_values: dimensionValues,
    },
  };
}

export function normalizeViewerArtifactRows(
  rows: ViewerArtifactRowWire[],
  options: ViewerArtifactLoadOptions,
): ViewerArtifactRow[] {
  return rows.map((row) => normalizeArtifactRow(row, options));
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

  const file = await resolvedDependencies.openUrlBuffer({
    url,
    requestInit,
  });
  return await readParquetObjects(file, resolvedDependencies);
}

export async function loadViewerArtifactFromParquetUrl(
  url: string,
  requestInit: RequestInit | undefined,
  options: ViewerArtifactLoadOptions,
): Promise<ViewerArtifactRow[]> {
  const rows = await loadViewerArtifactRowsFromParquetUrl(url, requestInit, options.dependencies);

  return normalizeViewerArtifactRows(rows, options);
}
