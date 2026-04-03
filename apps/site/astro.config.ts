import { defineConfig } from "astro/config";
import react from "@astrojs/react";
import starlight from "@astrojs/starlight";
import sitemap from "@astrojs/sitemap";

import {
  createSiteUrlLogger,
  getSiteRuntimeConfig,
  loadRepoEnvFile,
  siteViteConfig,
} from "./config/site";
import { createStarlightConfig } from "./config/starlight";

loadRepoEnvFile();

const { siteUrl, siteUrlSource, enableAgentationReview } = getSiteRuntimeConfig();

export default defineConfig({
  site: siteUrl,
  vite: siteViteConfig,
  integrations: [
    createSiteUrlLogger(siteUrl, siteUrlSource),
    react(),
    starlight(createStarlightConfig({ enableAgentationReview })),
    sitemap(),
  ],
});
