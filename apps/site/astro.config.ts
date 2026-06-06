import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";

import {
  createSiteUrlLogger,
  getSiteRuntimeConfig,
  loadRepoEnvFile,
  siteViteConfig,
} from "./src/config/site";

loadRepoEnvFile();

const { siteUrl, siteUrlSource } = getSiteRuntimeConfig();

export default defineConfig({
  site: siteUrl,
  vite: siteViteConfig,
  integrations: [createSiteUrlLogger(siteUrl, siteUrlSource), mdx(), sitemap()],
});
