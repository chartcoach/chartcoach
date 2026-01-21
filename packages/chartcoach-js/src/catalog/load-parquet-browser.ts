import { asyncBufferFromUrl } from "hyparquet";

import { loadCatalogFromParquet, type AsyncBuffer } from "./load-parquet-core.js";

export async function loadCatalogFromParquetUrl(
	url: string,
	requestInit?: RequestInit,
) {
	const file = (await asyncBufferFromUrl({
		url,
		requestInit,
	})) as AsyncBuffer;

	return loadCatalogFromParquet(file);
}
