import { asyncBufferFromFile } from "hyparquet";

import { loadCatalogFromParquet } from "./load-parquet-core.js";

export async function loadCatalogFromParquetFile(parquetPath: string) {
  const file = await asyncBufferFromFile(parquetPath);
  return loadCatalogFromParquet(file);
}
