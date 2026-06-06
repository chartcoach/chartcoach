import path from "node:path";
import { fileURLToPath } from "node:url";
import { defineConfig } from "vitest/config";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export default defineConfig({
  resolve: {
    alias: [
      {
        find: /^@chartcoach\/catalog\/server$/,
        replacement: path.resolve(__dirname, "src/server.ts"),
      },
      {
        find: /^@chartcoach\/catalog\/browser$/,
        replacement: path.resolve(__dirname, "src/browser.ts"),
      },
      {
        find: /^@chartcoach\/catalog$/,
        replacement: path.resolve(__dirname, "src/index.ts"),
      },
    ],
  },
  test: {
    environment: "node",
    include: ["test/**/*.test.ts"],
  },
});
