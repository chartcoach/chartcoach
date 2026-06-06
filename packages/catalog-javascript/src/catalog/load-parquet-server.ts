import { asyncBufferFromFile } from "hyparquet";

import { loadCatalog, type CatalogLoadOptions } from "./load-parquet-core";

export async function readCatalogFile(
  parquetPath: string,
  options: CatalogLoadOptions = {},
) {
  const file = await asyncBufferFromFile(parquetPath);
  return loadCatalog(file, options);
}
