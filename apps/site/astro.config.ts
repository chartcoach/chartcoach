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
import { guidelineSearchDocuments } from "./src/config/search";
import { llms } from "./src/integrations/llms";
import { ogImages } from "./src/integrations/og-images";
import { searchIndex } from "./src/integrations/search-index";
import { GUIDELINE_SEARCH_SCHEMA } from "./src/lib/guideline-search-model";
import OgImage from "./src/og/component";
import {
  OG_BUILD_PROPS_META,
  OG_IMAGE_HEIGHT,
  OG_IMAGE_WIDTH,
  parseOgBuildPayload,
} from "./src/og/schema";

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
        "chartcoach turns visualization design knowledge into guideline entries with source references for chart agents.",
      pages: chartcoachLlmPages,
    }),
    searchIndex({
      name: "chartcoach:search-index",
      databases: {
        guidelines: {
          language: "english",
          schema: GUIDELINE_SEARCH_SCHEMA,
          include: (pathname) => /^\/guidelines\/(?!page\/)[^/]+\/$/.test(pathname),
        },
      },
      documents: guidelineSearchDocuments,
    }),
    ogImages({
      component: OgImage,
      name: "chartcoach:og-images",
      metaName: OG_BUILD_PROPS_META,
      parsePayload: parseOgBuildPayload,
      width: OG_IMAGE_WIDTH,
      height: OG_IMAGE_HEIGHT,
    }),
  ],
});
