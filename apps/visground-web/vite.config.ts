import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

const __dirname = dirname(fileURLToPath(import.meta.url));
const monorepoRoot = resolve(__dirname, "../..");
const appSourceRoot = resolve(__dirname, "./src");

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    conditions: ["source", "module", "browser", "development|production"],
    alias: {
      "@": appSourceRoot,
    },
  },
  server: {
    host: "127.0.0.1",
    port: 4174,
    strictPort: true,
    fs: {
      allow: [monorepoRoot],
    },
  },
  preview: {
    host: "127.0.0.1",
    port: 4174,
    strictPort: true,
  },
});
