import path from "node:path";
import { defineConfig } from "vite";
import anywidget from "@anywidget/vite";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig(({ command }) => {
  const isBuild = command === "build";

  return {
    plugins: [anywidget(), tailwindcss()],
    publicDir: path.resolve(__dirname, "../visground-viewer/public"),
    resolve: {
      conditions: ["chartcoach-source", "module", "browser", "development|production"],
    },
    server: {
      host: "127.0.0.1",
      port: 5173,
      strictPort: true,
    },
    define: isBuild
      ? {
          "process.env.NODE_ENV": JSON.stringify("production"),
        }
      : undefined,
    build: {
      outDir: "./src/visground/viewer/_static/anywidget",
      target: "esnext",
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
  };
});
