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
    entry: ["src/index.ts"],
    format: ["esm"],
    platform: "neutral",
    target: "es2022",
  },
  test: {
    environment: "node",
    include: ["test/**/*.test.ts"],
  },
});
