export * from "./index.js";

export { loadCatalogFromParquetUrl } from "./catalog/load-parquet-browser.js";

/**
 * Convenience wrapper for browser environments where you already have the bytes
 * (e.g., `await (await fetch(url)).arrayBuffer()` or a `Uint8Array`).
 */
export {
	loadCatalogFromParquet as loadCatalogFromParquetBytes,
} from "./catalog/load-parquet-core.js";
