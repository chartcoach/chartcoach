import { parquetReadObjects } from "hyparquet";
import { compressors } from "hyparquet-compressors";
import { Catalog, type CatalogEntry } from "./model.js";
import { requireCatalogEntryFromWire } from "./wire.js";

export type AsyncBuffer = {
  byteLength: number;
  slice(start: number, end?: number): ArrayBuffer | Promise<ArrayBuffer>;
};

export type ParquetBytes = ArrayBuffer | ArrayBufferView;

function normalizeParquetBytes(bytes: ParquetBytes): ArrayBuffer {
  if (bytes instanceof ArrayBuffer) return bytes;

  // TypedArray/DataView may be a view into a larger ArrayBuffer (or SharedArrayBuffer).
  // Copy to a standalone ArrayBuffer covering exactly the view range.
  const u8 = new Uint8Array(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  return u8.slice().buffer;
}

export async function loadCatalogFromParquet(file: AsyncBuffer | ParquetBytes): Promise<Catalog> {
  const normalizedFile =
    file instanceof ArrayBuffer || ArrayBuffer.isView(file)
      ? normalizeParquetBytes(file as ParquetBytes)
      : file;

  const rows = (await parquetReadObjects({
    file: normalizedFile,
    compressors,
  })) as Array<Record<string, unknown>>;

  const entries: CatalogEntry[] = rows.map((row, index) =>
    requireCatalogEntryFromWire(row, `parquet row ${index}`),
  );

  return new Catalog(entries);
}
