import { defineConfig } from "astro/config";
import react from "@astrojs/react";
import sitemap from "@astrojs/sitemap";

import {
  createSiteUrlLogger,
  getSiteRuntimeConfig,
  loadRepoEnvFile,
  siteViteConfig,
} from "./src/config/site";
import { oramaSearch } from "./src/integrations/orama-search";

loadRepoEnvFile();

const { siteUrl, siteUrlSource } = getSiteRuntimeConfig();

export default defineConfig({
  site: siteUrl,
  vite: siteViteConfig,
  integrations: [
    react(),
    createSiteUrlLogger(siteUrl, siteUrlSource),
    sitemap(),
    oramaSearch({
      guidelines: {
        language: "english",
        pathMatcher: /^\/?guidelines\/(?!page\/)[^/]+\/?$/,
      },
    }),
  ],
});
