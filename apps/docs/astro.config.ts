import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import starlight from "@astrojs/starlight";

import {
  createDocsUrlLogger,
  docsViteConfig,
  getDocsRuntimeConfig,
  loadRepoEnvFile,
} from "./src/config/site";

loadRepoEnvFile();

const { docsUrl, docsUrlSource } = getDocsRuntimeConfig();

export default defineConfig({
  site: docsUrl,
  vite: docsViteConfig,
  integrations: [
    createDocsUrlLogger(docsUrl, docsUrlSource),
    starlight({
      title: "ChartCoach Docs",
      description: "Documentation scaffold for ChartCoach.",
      pagefind: false,
    }),
    sitemap(),
  ],
});
