import { defineConfig } from "astro/config";
import react from "@astrojs/react";
import sitemap from "@astrojs/sitemap";

import {
  createSiteUrlLogger,
  getSiteRuntimeConfig,
  loadRepoEnvFile,
  siteViteConfig,
} from "./src/config/site";
import { chartcoachLlmPages } from "./src/config/llms";
import { llms } from "./src/integrations/llms";
import { oramaSearch } from "./src/integrations/orama-search";

loadRepoEnvFile();

const { siteUrl, siteUrlSource, isPreviewDeployment } = getSiteRuntimeConfig();

export default defineConfig({
  site: siteUrl,
  vite: siteViteConfig,
  integrations: [
    react(),
    createSiteUrlLogger(siteUrl, siteUrlSource),
    ...(!isPreviewDeployment ? [sitemap()] : []),
    llms({
      name: "chartcoach:llms",
      site: siteUrl,
      title: "chartcoach",
      description:
        "chartcoach turns visualization design knowledge into source-traced records for chart agents.",
      pages: chartcoachLlmPages,
    }),
    oramaSearch({
      guidelines: {
        language: "english",
        pathMatcher: /^\/?guidelines\/(?!page\/)[^/]+\/?$/,
      },
    }),
  ],
});
