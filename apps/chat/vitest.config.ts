import { defineConfig } from "vite-plus";
import stylex from "@stylexjs/unplugin/rollup";

export default defineConfig({
  plugins: [stylex({ devMode: "css-only", useCSSLayers: true })],
  test: { include: ["test/**/*.test.tsx"], environment: "node" },
});
