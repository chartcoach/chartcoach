import { CatalogError } from "./errors";

const defaultCatalogArtifactBaseUrl = "https://artifacts.chartcoach.dev";
const defaultCatalogDigest =
  "7cfd43ee820be252b8ae9058c4c36109a9c8415c6b3a5ff8a9127117b4a10c19";
const defaultCatalogVersion = "0.1.3";
const defaultCatalogReleaseRootUrl = new URL(
  `catalog/releases/${defaultCatalogVersion}/${defaultCatalogDigest}/`,
  `${defaultCatalogArtifactBaseUrl}/`,
).toString();

export const DEFAULT_CATALOG = {
  version: defaultCatalogVersion,
  digest: defaultCatalogDigest,
  releaseRootUrl: defaultCatalogReleaseRootUrl,
  metadataUrl: new URL("metadata.json", defaultCatalogReleaseRootUrl).toString(),
  entriesUrl: new URL("entries.parquet", defaultCatalogReleaseRootUrl).toString(),
  manifestUrl: new URL("MANIFEST.md", defaultCatalogReleaseRootUrl).toString(),
} as const;

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
  catalogArtifact(metadata, "manifest");
  catalogArtifact(metadata, "entries");
  return metadata;
}

export function catalogArtifactUrl(
  baseUrl: string | URL,
  descriptor: ArtifactDescriptor,
): string {
  return new URL(descriptor.path, baseUrl).toString();
}

export function catalogArtifact(
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
