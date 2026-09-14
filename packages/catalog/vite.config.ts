import { fileURLToPath } from "node:url";

import { defineConfig } from "vite-plus";

export default defineConfig({
  resolve: {
    alias: [
      {
        find: /^@chartcoach\/catalog$/,
        replacement: fileURLToPath(new URL("./src/index.ts", import.meta.url)),
      },
    ],
  },
  pack: {
    dts: true,
    entry: [
      "src/index.ts",
      "src/node.ts",
      "src/node/paths.ts",
      "src/duckdb.ts",
      "src/duckdb-wasm.ts",
    ],
    format: ["esm"],
    platform: "neutral",
    deps: { neverBundle: [/^node:/] },
    target: "es2022",
  },
  test: {
    environment: "node",
    include: ["test/**/*.test.ts"],
  },
  run: {
    tasks: {
      test: {
        command: "vp test",
        // Python source changes invalidate the cross-language contract check.
        input: [
          { auto: true },
          { pattern: "packages/chartcoach/src/**", base: "workspace" },
          { pattern: "packages/chartcoach/tests/catalog_tables_contract.py", base: "workspace" },
          { pattern: "packages/chartcoach/pyproject.toml", base: "workspace" },
          { pattern: "fixtures/catalog-contract/**", base: "workspace" },
          { pattern: "uv.lock", base: "workspace" },
        ],
      },
    },
  },
});
