import path from "node:path";
import { defineConfig } from "vite";
import anywidget from "@anywidget/vite";

export default defineConfig({
  plugins: [anywidget()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "../../packages/visground-viewer/src"),
    },
  },
  define: {
    "process.env.NODE_ENV": JSON.stringify("production"),
  },
  build: {
    outDir: "./src/visground/viewer/_static/anywidget",
    target: "esnext",
    copyPublicDir: false,
    lib: {
      entry: {
        index: "./js/anywidget.ts",
      },
      formats: ["es"],
      fileName: (_format, entryName) => `${entryName}.js`,
    },
    rollupOptions: {
      output: {
        inlineDynamicImports: true,
      },
    },
  },
});
