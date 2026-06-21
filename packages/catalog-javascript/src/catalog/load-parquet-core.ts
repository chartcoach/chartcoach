import { parquetReadObjects } from "hyparquet";
import { compressors } from "hyparquet-compressors";
import { Catalog, type Guideline } from "./model";
import { CatalogError } from "./errors";
import type { CatalogManifest } from "./manifest";
import { parseCatalogManifest } from "./manifest";
import { requireGuidelineFromWire } from "./wire";

export type AsyncBuffer = {
  byteLength: number;
  slice(start: number, end?: number): ArrayBuffer | Promise<ArrayBuffer>;
};

export type ParquetBytes = ArrayBuffer | ArrayBufferView;
export type CatalogBytes = ParquetBytes | AsyncBuffer;
export type LoadCatalogInput = CatalogBytes | {
  entries: CatalogBytes;
  manifest?: CatalogManifest;
  manifestText?: string;
};

function normalizeParquetBytes(bytes: ParquetBytes): ArrayBuffer {
  if (bytes instanceof ArrayBuffer) return bytes;

  // TypedArray/DataView may be a view into a larger ArrayBuffer (or SharedArrayBuffer).
  // Copy to a standalone ArrayBuffer covering exactly the view range.
  const u8 = new Uint8Array(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  return u8.slice().buffer;
}

export async function loadCatalog(
  input: LoadCatalogInput,
): Promise<Catalog> {
  const { entries, manifest } = resolveLoadCatalogInput(input);
  const normalizedFile =
    entries instanceof ArrayBuffer || ArrayBuffer.isView(entries)
      ? normalizeParquetBytes(entries as ParquetBytes)
      : entries;

  const rows = (await parquetReadObjects({
    file: normalizedFile,
    compressors,
  })) as Array<Record<string, unknown>>;

  const guidelines: Guideline[] = rows.map((row, index) =>
    requireGuidelineFromWire(row, `parquet row ${index}`),
  );

  return new Catalog(guidelines, { manifest });
}

function resolveLoadCatalogInput(input: LoadCatalogInput): {
  entries: CatalogBytes;
  manifest?: CatalogManifest;
} {
  if (isCatalogBytes(input)) return { entries: input };

  if (input.manifest && input.manifestText !== undefined) {
    throw new CatalogError("Pass manifest or manifestText, not both.");
  }

  return {
    entries: input.entries,
    manifest: input.manifestText === undefined
      ? input.manifest
      : parseCatalogManifest(input.manifestText),
  };
}

function isCatalogBytes(value: LoadCatalogInput): value is CatalogBytes {
  return (
    value instanceof ArrayBuffer ||
    ArrayBuffer.isView(value) ||
    (
      typeof value === "object" &&
      value !== null &&
      typeof (value as AsyncBuffer).byteLength === "number" &&
      typeof (value as AsyncBuffer).slice === "function"
    )
  );
}
