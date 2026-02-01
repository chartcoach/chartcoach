import { defineConfig } from "vite";
import { devtools } from "@tanstack/devtools-vite";
import { tanstackStart } from "@tanstack/react-start/plugin/vite";
import viteReact from "@vitejs/plugin-react";
import viteTsConfigPaths from "vite-tsconfig-paths";
import { fileURLToPath, URL } from "url";
import { existsSync } from "node:fs";
import { join } from "node:path";

import tailwindcss from "@tailwindcss/vite";
import { nitro } from "nitro/vite";

const monorepoRoot = fileURLToPath(new URL("../..", import.meta.url));

const repoEnvPath = join(monorepoRoot, ".env");
const loadEnvFile = (process as NodeJS.Process & { loadEnvFile?: (path?: string) => void })
  .loadEnvFile;
if (typeof loadEnvFile === "function" && existsSync(repoEnvPath)) loadEnvFile(repoEnvPath);

export default defineConfig({
  envDir: monorepoRoot,
  build: {
    rollupOptions: {
      onwarn(warning, warn) {
        // Some deps ship `"use client"` directives for React Server Components.
        // Rollup can't preserve these in our bundling targets and warns noisily.
        if (
          warning.code === "MODULE_LEVEL_DIRECTIVE" &&
          typeof warning.message === "string" &&
          warning.message.includes('"use client"')
        ) {
          return;
        }
        warn(warning);
      },
    },
  },
  server: {
    fs: {
      allow: [monorepoRoot],
    },
  },
  resolve: {
    alias: {
      "@chartcoach/eval-ui": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  plugins: [
    devtools(),
    nitro({
      rollupConfig: {
        onwarn(warning, warn) {
          // Nitro's internal Rollup build is chatty about `"use client"` directives
          // shipped by some deps (React Server Components). Ignore those warnings
          // while keeping the rest of the build output actionable.
          const code = warning.code ?? "";
          if (
            code === "MODULE_LEVEL_DIRECTIVE" &&
            typeof warning.message === "string" &&
            warning.message.includes('"use client"')
          ) {
            return;
          }

          // Match Nitro defaults (avoids regressing noise levels).
          if (code === "EVAL") return;
          if (code === "CIRCULAR_DEPENDENCY") return;
          if (code === "THIS_IS_UNDEFINED") return;
          if (code === "EMPTY_BUNDLE") return;

          warn(warning);
        },
      },
    }),
    // enables path aliases
    viteTsConfigPaths({ projects: ["./tsconfig.json"] }),
    tailwindcss(),
    tanstackStart(),
    viteReact(),
  ],
});
