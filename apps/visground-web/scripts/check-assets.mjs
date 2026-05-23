import { access, readFile } from "node:fs/promises";
import { constants } from "node:fs";
import { join } from "node:path";
import { parquetReadObjects } from "hyparquet";
import { compressors } from "hyparquet-compressors";
import {
  normalizeViewerArtifactRows,
  parseViewerArtifactRows,
} from "../../../packages/visground-viewer/src/viewer/data/parquet.ts";
import { parseViewerRuntimeConfig } from "../../../packages/visground-viewer/src/viewer/data/runtime-config.ts";

const requiredAssets = ["public/data/viewer.parquet", "public/data/viewer.config.json"];

for (const asset of requiredAssets) {
  await access(join(import.meta.dirname, "..", asset), constants.R_OK);
}

const config = JSON.parse(
  await readFile(join(import.meta.dirname, "..", "public/data/viewer.config.json"), "utf8"),
);
const runtimeConfig = parseViewerRuntimeConfig(config);
const parquetBytes = await readFile(join(import.meta.dirname, "..", "public/data/viewer.parquet"));
const parquetRows = await parquetReadObjects({
  file: parquetBytes.buffer.slice(
    parquetBytes.byteOffset,
    parquetBytes.byteOffset + parquetBytes.byteLength,
  ),
  compressors,
});

if (!Array.isArray(config.dimensions) || config.dimensions.length === 0) {
  throw new Error("viewer.config.json must declare dimensions.");
}
if (!parquetRows.length) {
  throw new Error("viewer.parquet must contain at least one row.");
}

normalizeViewerArtifactRows(parseViewerArtifactRows(parquetRows), { runtimeConfig });
