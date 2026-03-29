import path from "node:path";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
  define: {
    "process.env.NODE_ENV": JSON.stringify("production"),
  },
  build: {
    outDir: "distlib",
    target: "esnext",
    copyPublicDir: false,
    lib: {
      entry: "./src/index.ts",
      fileName: () => "index.js",
      formats: ["es"],
    },
    rollupOptions: {
      output: {
        chunkFileNames: "chunk-[hash].js",
      },
    },
  },
});
