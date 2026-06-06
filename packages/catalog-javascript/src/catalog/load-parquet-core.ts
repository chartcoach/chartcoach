import { parquetReadObjects } from "hyparquet";
import { compressors } from "hyparquet-compressors";
import { Catalog, type CatalogOptions, type Guideline } from "./model";
import type { CatalogManifest } from "./manifest";
import { requireGuidelineFromWire } from "./wire";

export type AsyncBuffer = {
  byteLength: number;
  slice(start: number, end?: number): ArrayBuffer | Promise<ArrayBuffer>;
};

export type ParquetBytes = ArrayBuffer | ArrayBufferView;
export type CatalogLoadOptions = CatalogOptions & {
  manifest?: CatalogManifest;
};

function normalizeParquetBytes(bytes: ParquetBytes): ArrayBuffer {
  if (bytes instanceof ArrayBuffer) return bytes;

  // TypedArray/DataView may be a view into a larger ArrayBuffer (or SharedArrayBuffer).
  // Copy to a standalone ArrayBuffer covering exactly the view range.
  const u8 = new Uint8Array(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  return u8.slice().buffer;
}

export async function loadCatalog(
  file: AsyncBuffer | ParquetBytes,
  options: CatalogLoadOptions = {},
): Promise<Catalog> {
  const normalizedFile =
    file instanceof ArrayBuffer || ArrayBuffer.isView(file)
      ? normalizeParquetBytes(file as ParquetBytes)
      : file;

  const rows = (await parquetReadObjects({
    file: normalizedFile,
    compressors,
  })) as Array<Record<string, unknown>>;

  const guidelines: Guideline[] = rows.map((row, index) =>
    requireGuidelineFromWire(row, `parquet row ${index}`),
  );

  return new Catalog(guidelines, options);
}
