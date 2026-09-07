import { parquetReadObjects } from "hyparquet";
import { compressors } from "hyparquet-compressors";
import {
  assertReleaseArtifactBytes,
  assertReleaseDigest,
  assertReleaseLocation,
  copyCatalogRelease,
  releaseArtifact,
  sanitizeReleaseUrl,
  type CatalogRelease,
} from "./artifacts";
import { CatalogError } from "./errors";
import type { ProfileLoader } from "./description";
import {
  Catalog,
  catalogWithRelease,
  type CatalogReleaseContext,
  type GuidelineInput,
} from "./model";
import type { JsonObject } from "./json";
import { parseCatalogManifest } from "./manifest";
import { releaseProfileNames } from "./profile-layout";
import { requireGuidelineFromWire } from "./wire";

export type AsyncBuffer = {
  byteLength: number;
  slice(start: number, end?: number): ArrayBuffer | Promise<ArrayBuffer>;
};

export type ParquetBytes = ArrayBuffer | ArrayBufferView;
export type CatalogBytes = ParquetBytes | AsyncBuffer;
export type LoadCatalogDataInput = {
  entries: CatalogBytes;
  manifestText: string;
};
export type LoadCatalogInput = {
  entries: ParquetBytes;
  manifest: ParquetBytes;
  release: CatalogRelease;
  releaseUrl: string | URL;
};

const MAX_CORE_ARTIFACT_BYTES = 64 * 1024 * 1024;

function normalizeParquetBytes(bytes: ParquetBytes): ArrayBuffer {
  if (bytes instanceof ArrayBuffer) return bytes;

  // TypedArray/DataView may be a view into a larger ArrayBuffer (or SharedArrayBuffer).
  // Copy to a standalone ArrayBuffer covering exactly the view range.
  const u8 = new Uint8Array(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  return u8.slice().buffer;
}

function isParquetBytes(bytes: CatalogBytes): bytes is ParquetBytes {
  return bytes instanceof ArrayBuffer || ArrayBuffer.isView(bytes);
}

export async function loadCatalog(input: LoadCatalogInput): Promise<Catalog> {
  return loadCatalogWithProfileLoader(input);
}

export async function loadCatalogWithProfileLoader(
  input: LoadCatalogInput,
  profileLoader?: ProfileLoader,
  artifactLoader?: CatalogReleaseContext["artifactLoader"],
): Promise<Catalog> {
  const release = copyCatalogRelease(input.release);
  await assertReleaseDigest(release);
  assertReleaseLocation(input.releaseUrl, release);
  releaseProfileNames(release);
  assertCoreArtifactSize(release, "entries.parquet", input.entries.byteLength);
  assertCoreArtifactSize(release, "MANIFEST.md", input.manifest.byteLength);
  await Promise.all([
    assertReleaseArtifactBytes(
      "entries.parquet",
      releaseArtifact(release, "entries.parquet"),
      input.entries,
    ),
    assertReleaseArtifactBytes(
      "MANIFEST.md",
      releaseArtifact(release, "MANIFEST.md"),
      input.manifest,
    ),
  ]);
  let manifestText: string;
  try {
    manifestText = new TextDecoder("utf-8", { fatal: true }).decode(
      normalizeParquetBytes(input.manifest),
    );
  } catch {
    throw new CatalogError("Catalog manifest must contain valid UTF-8.");
  }
  return parseCatalogData(
    { entries: input.entries, manifestText },
    {
      release,
      releaseUrl: sanitizeReleaseUrl(input.releaseUrl),
      profileLoader,
      artifactLoader: artifactLoader ?? suppliedArtifacts(input),
    },
  );
}

function suppliedArtifacts(input: LoadCatalogInput): CatalogReleaseContext["artifactLoader"] {
  const entries = new Uint8Array(normalizeParquetBytes(input.entries)).slice();
  const manifest = new Uint8Array(normalizeParquetBytes(input.manifest)).slice();
  return async (path, signal) => {
    signal?.throwIfAborted();
    if (path === "entries.parquet") return entries.slice();
    if (path === "MANIFEST.md") return manifest.slice();
    throw new CatalogError(`Artifact bytes were not supplied: ${path}`, {
      code: "unavailable_capability",
    });
  };
}

function assertCoreArtifactSize(
  release: CatalogRelease,
  path: "MANIFEST.md" | "entries.parquet",
  receivedBytes: number,
): void {
  const recordedBytes = releaseArtifact(release, path).bytes;
  if (recordedBytes > MAX_CORE_ARTIFACT_BYTES || receivedBytes > MAX_CORE_ARTIFACT_BYTES) {
    throw new CatalogError(`Catalog artifact exceeds size limit: ${path}`);
  }
}

export async function loadCatalogData(input: LoadCatalogDataInput): Promise<Catalog> {
  return parseCatalogData(input);
}

async function parseCatalogData(
  input: LoadCatalogDataInput,
  releaseContext?: CatalogReleaseContext,
): Promise<Catalog> {
  const manifest = parseCatalogManifest(input.manifestText);
  const normalizedFile = isParquetBytes(input.entries)
    ? normalizeParquetBytes(input.entries)
    : input.entries;

  const rows: JsonObject[] = await parquetReadObjects({
    file: normalizedFile,
    compressors,
  });

  const guidelines: GuidelineInput[] = rows.map((row, index) =>
    requireGuidelineFromWire(row, `parquet row ${index}`),
  );

  const catalog = new Catalog(guidelines, manifest);
  return releaseContext ? catalogWithRelease(catalog, releaseContext) : catalog;
}
