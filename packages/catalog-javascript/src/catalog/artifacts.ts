import { CatalogError } from "./errors";

export const DEFAULT_CATALOG_ARTIFACT_BASE_URL = "https://artifacts.chartcoach.dev";
export const DEFAULT_CATALOG_DIGEST =
  "7cfd43ee820be252b8ae9058c4c36109a9c8415c6b3a5ff8a9127117b4a10c19";
export const DEFAULT_CATALOG_VERSION = "0.0.0";
export const DEFAULT_CATALOG_RELEASE_ROOT_URL = new URL(
  `catalog/releases/${DEFAULT_CATALOG_VERSION}/${DEFAULT_CATALOG_DIGEST}/`,
  `${DEFAULT_CATALOG_ARTIFACT_BASE_URL}/`,
).toString();
export const DEFAULT_CATALOG_METADATA_URL = new URL(
  "metadata.json",
  DEFAULT_CATALOG_RELEASE_ROOT_URL,
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
  const url = metadataUrl.toString();
  const response = await fetch(url, request);
  if (!response.ok) {
    throw new CatalogError(`Failed to load catalog metadata: ${response.status}`);
  }
  const value = await response.json();
  return {
    metadata: parseCatalogReleaseMetadata(value),
    metadataUrl: url,
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
