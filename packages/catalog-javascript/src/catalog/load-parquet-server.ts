import { asyncBufferFromFile } from "hyparquet";

import { loadCatalog, type CatalogLoadOptions } from "./load-parquet-core";
import type { Catalog } from "./model";

export async function readCatalogFile(
  parquetPath: string,
  options: CatalogLoadOptions = {},
): Promise<Catalog> {
  const file = await asyncBufferFromFile(parquetPath);
  return loadCatalog(file, options);
}
