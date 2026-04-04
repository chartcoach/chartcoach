import path from "node:path";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
      "@chartcoach/ui": path.resolve(__dirname, "../ui/src"),
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
