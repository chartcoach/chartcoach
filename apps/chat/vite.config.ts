import { defineConfig } from "vite-plus";
import stylex from "@stylexjs/unplugin/rollup";

export default defineConfig({
  plugins: [stylex({ devMode: "css-only", useCSSLayers: true })],
  pack: {
    entry: ["cli/index.ts"],
    outDir: ".output/cli",
    format: ["esm"],
    platform: "node",
    target: "node24",
    dts: false,
    deps: {
      // Preserve the package subpath resolution used by existing builds.
      resolveDepSubpath: true,
      alwaysBundle: ["@commander-js/extra-typings"],
      onlyBundle: ["@commander-js/extra-typings"],
    },
  },
  test: {
    include: ["test/**/*.test.tsx"],
    environment: "node",
    env: { CHARTCOACH_CATALOG: new URL("../../fixtures/catalog-release/", import.meta.url).href },
  },
});
