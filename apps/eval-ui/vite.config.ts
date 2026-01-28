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
    nitro(),
    // enables path aliases
    viteTsConfigPaths({ projects: ["./tsconfig.json"] }),
    tailwindcss(),
    tanstackStart(),
    viteReact(),
  ],
});
