import { CatalogError } from "./errors";

export const DEFAULT_CATALOG_ARTIFACT_BASE_URL = "https://artifacts.chartcoach.dev";
export const DEFAULT_CATALOG_DIGEST =
  "7cfd43ee820be252b8ae9058c4c36109a9c8415c6b3a5ff8a9127117b4a10c19";
export const DEFAULT_CATALOG_VERSION = "0.0.0";
export const DEFAULT_CATALOG_METADATA_URL = new URL(
  "metadata.json",
  `${DEFAULT_CATALOG_ARTIFACT_BASE_URL}/`,
).toString();

export type ArtifactKind = "manifest" | "entries" | "lancedb-index";

export type ArtifactDescriptor = {
  kind: ArtifactKind;
  path: string;
  digest: string;
  bytes: number;
  format?: string;
  rows?: number;
  [key: string]: unknown;
};

export type CatalogReleaseMetadata = {
  version: string;
  digest: string;
  artifacts: ArtifactDescriptor[];
};

export type CatalogReleasePointer = {
  kind: "chartcoach-release-pointer";
  target: string;
  version?: string;
  digest?: string;
};

export type ResolvedCatalogReleaseMetadata = {
  metadata: CatalogReleaseMetadata;
  metadataUrl: string;
};

export function parseCatalogReleaseMetadata(value: unknown): CatalogReleaseMetadata {
  if (!isRecord(value)) {
    throw new CatalogError("Catalog release metadata must be an object.");
  }
  const artifacts = value.artifacts;
  if (!Array.isArray(artifacts)) {
    throw new CatalogError("Catalog release metadata artifacts must be a list.");
  }
  const metadata = {
    version: requiredString(value, "version"),
    digest: requiredString(value, "digest"),
    artifacts: artifacts.map(parseArtifactDescriptor),
  };
  artifact(metadata, "manifest");
  artifact(metadata, "entries");
  return metadata;
}

export async function fetchCatalogReleaseMetadata(
  metadataUrl: string | URL = DEFAULT_CATALOG_METADATA_URL,
  request?: RequestInit,
): Promise<CatalogReleaseMetadata> {
  return (await fetchCatalogRelease(metadataUrl, request)).metadata;
}

export async function fetchCatalogRelease(
  metadataUrl: string | URL = DEFAULT_CATALOG_METADATA_URL,
  request?: RequestInit,
): Promise<ResolvedCatalogReleaseMetadata> {
  return fetchCatalogReleaseFrom(metadataUrl.toString(), request, 0);
}

async function fetchCatalogReleaseFrom(
  metadataUrl: string,
  request: RequestInit | undefined,
  depth: number,
): Promise<ResolvedCatalogReleaseMetadata> {
  if (depth > 5) {
    throw new CatalogError("Catalog metadata pointer chain is too deep.");
  }
  const response = await fetch(metadataUrl.toString(), request);
  if (!response.ok) {
    throw new CatalogError(`Failed to load catalog metadata: ${response.status}`);
  }
  const value = await response.json();
  if (isCatalogReleasePointer(value)) {
    return fetchCatalogReleaseFrom(resolvePointerUrl(metadataUrl, value.target), request, depth + 1);
  }
  return {
    metadata: parseCatalogReleaseMetadata(value),
    metadataUrl,
  };
}

export function artifactUrl(
  metadataUrl: string | URL,
  descriptor: ArtifactDescriptor,
): string {
  return new URL(descriptor.path, metadataUrl).toString();
}

export function artifact(
  metadata: CatalogReleaseMetadata,
  kind: ArtifactKind,
): ArtifactDescriptor {
  const descriptor = metadata.artifacts.find((item) => item.kind === kind);
  if (!descriptor) {
    throw new CatalogError(`Catalog release metadata is missing a ${kind} artifact.`);
  }
  return descriptor;
}

function parseArtifactDescriptor(value: unknown): ArtifactDescriptor {
  if (!isRecord(value)) {
    throw new CatalogError("Catalog artifact descriptor must be an object.");
  }
  const kind = value.kind;
  if (kind !== "manifest" && kind !== "entries" && kind !== "lancedb-index") {
    throw new CatalogError(`Unsupported catalog artifact kind: ${String(kind)}`);
  }
  const path = requiredString(value, "path");
  validateRelativePath(path);
  const descriptor: ArtifactDescriptor = {
    kind,
    path,
    digest: requiredString(value, "digest"),
    bytes: requiredInteger(value, "bytes"),
  };
  if (typeof value.format === "string") descriptor.format = value.format;
  if (typeof value.rows === "number" && Number.isInteger(value.rows)) {
    descriptor.rows = value.rows;
  }
  for (const [key, rawValue] of Object.entries(value)) {
    if (!["kind", "path", "digest", "bytes", "format", "rows"].includes(key)) {
      descriptor[key] = rawValue;
    }
  }
  return descriptor;
}

function validateRelativePath(path: string): void {
  if (path.startsWith("/") || path.split("/").includes("..")) {
    throw new CatalogError(`Catalog artifact path must be relative: ${path}`);
  }
}

function resolvePointerUrl(metadataUrl: string, target: string): string {
  try {
    const parsed = new URL(target);
    if (parsed.protocol !== "http:" && parsed.protocol !== "https:") {
      throw new CatalogError(`Unsupported catalog release pointer URL: ${target}`);
    }
    return parsed.toString();
  } catch (error) {
    if (error instanceof CatalogError) throw error;
  }
  if (target.startsWith("/")) {
    validateRelativePath(target.slice(1));
    return new URL(target, metadataUrl).toString();
  }
  validateRelativePath(target);
  return new URL(target, metadataUrl).toString();
}

function isCatalogReleasePointer(value: unknown): value is CatalogReleasePointer {
  return isRecord(value) && value.kind === "chartcoach-release-pointer" && typeof value.target === "string";
}

function requiredString(value: Record<string, unknown>, key: string): string {
  const raw = value[key];
  if (typeof raw !== "string" || raw.length === 0) {
    throw new CatalogError(`Catalog release metadata ${key} must be a string.`);
  }
  return raw;
}

function requiredInteger(value: Record<string, unknown>, key: string): number {
  const raw = value[key];
  if (typeof raw !== "number" || !Number.isInteger(raw) || raw < 0) {
    throw new CatalogError(`Catalog release metadata ${key} must be a non-negative integer.`);
  }
  return raw;
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return Boolean(value && typeof value === "object" && !Array.isArray(value));
}
