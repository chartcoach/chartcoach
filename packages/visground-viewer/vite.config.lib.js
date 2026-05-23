import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  define: {
    "process.env.NODE_ENV": JSON.stringify("production"),
  },
  build: {
    outDir: "distlib",
    target: "esnext",
    copyPublicDir: false,
    lib: {
      entry: {
        index: "./src/index.ts",
      },
      fileName: (_format, entryName) => `${entryName}.js`,
      formats: ["es"],
    },
    rollupOptions: {
      external: ["react", "react-dom", "react-dom/client", "react/jsx-runtime"],
      output: {
        chunkFileNames: "chunk-[hash].js",
      },
    },
  },
});
