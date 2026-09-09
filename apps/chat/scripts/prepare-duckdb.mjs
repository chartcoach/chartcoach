import { copyFile, mkdir } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const distribution = dirname(fileURLToPath(import.meta.resolve("@duckdb/duckdb-wasm")));
const target = fileURLToPath(new URL("../public/duckdb/", import.meta.url));
await mkdir(target, { recursive: true });
for (const name of ["duckdb-eh.wasm", "duckdb-browser-eh.worker.js"]) {
  await copyFile(join(distribution, name), join(target, name));
}
