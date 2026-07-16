import { parquetReadObjects } from "hyparquet";
import { compressors } from "hyparquet-compressors";
import { Catalog, type Guideline } from "./model";
import { parseCatalogManifest } from "./manifest";
import { requireGuidelineFromWire } from "./wire";

export type AsyncBuffer = {
  byteLength: number;
  slice(start: number, end?: number): ArrayBuffer | Promise<ArrayBuffer>;
};

export type ParquetBytes = ArrayBuffer | ArrayBufferView;
export type CatalogBytes = ParquetBytes | AsyncBuffer;
export type LoadCatalogInput = {
  entries: CatalogBytes;
  manifestText: string;
};

function normalizeParquetBytes(bytes: ParquetBytes): ArrayBuffer {
  if (bytes instanceof ArrayBuffer) return bytes;

  // TypedArray/DataView may be a view into a larger ArrayBuffer (or SharedArrayBuffer).
  // Copy to a standalone ArrayBuffer covering exactly the view range.
  const u8 = new Uint8Array(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  return u8.slice().buffer;
}

export async function loadCatalog(input: LoadCatalogInput): Promise<Catalog> {
  const manifest = parseCatalogManifest(input.manifestText);
  const normalizedFile =
    input.entries instanceof ArrayBuffer || ArrayBuffer.isView(input.entries)
      ? normalizeParquetBytes(input.entries as ParquetBytes)
      : input.entries;

  const rows = (await parquetReadObjects({
    file: normalizedFile,
    compressors,
  })) as Array<Record<string, unknown>>;

  const guidelines: Array<Omit<Guideline, "body">> = rows.map((row, index) =>
    requireGuidelineFromWire(row, `parquet row ${index}`),
  );

  return new Catalog(guidelines, manifest);
}
