import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import starlight from "@astrojs/starlight";

import {
  createDocsUrlLogger,
  docsViteConfig,
  getDocsRuntimeConfig,
  loadRepoEnvFile,
} from "./src/config/site";
import { sidebar } from "./src/config/sidebar";

loadRepoEnvFile();

const { docsUrl, docsUrlSource, editLinkBaseUrl, repositoryUrl } = getDocsRuntimeConfig();
const editLink = editLinkBaseUrl ? { baseUrl: editLinkBaseUrl } : undefined;
const social = repositoryUrl
  ? [
      {
        icon: "github" as const,
        label: "GitHub",
        href: repositoryUrl,
      },
    ]
  : undefined;

export default defineConfig({
  site: docsUrl,
  vite: docsViteConfig,
  integrations: [
    createDocsUrlLogger(docsUrl, docsUrlSource),
    starlight({
      title: "ChartCoach Docs",
      description: "Technical reference for ChartCoach catalog packages, agent skills, and MCP tools.",
      customCss: ["./src/styles/docs.css"],
      editLink,
      social,
      sidebar,
    }),
    sitemap(),
  ],
});
