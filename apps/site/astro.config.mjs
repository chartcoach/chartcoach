// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import sitemap from "@astrojs/sitemap";
import react from "@astrojs/react";
import { fileURLToPath } from "node:url";
import { existsSync } from "node:fs";
import { join } from "node:path";

const monorepoRoot = fileURLToPath(new URL("../..", import.meta.url));

const repoEnvPath = join(monorepoRoot, ".env");
const loadEnvFile = /** @type {undefined | ((path?: string) => void)} */ (process.loadEnvFile);
if (typeof loadEnvFile === "function" && existsSync(repoEnvPath)) loadEnvFile(repoEnvPath);

/**
 * Resolve the canonical site URL for sitemap + canonical links.
 * Prefer an explicit `SITE_URL`, but fall back to common provider env vars.
 */
function resolveSiteUrl() {
  const candidates = [
    process.env.SITE_URL,
    process.env.PUBLIC_SITE_URL,
    process.env.URL, // Netlify
    process.env.DEPLOY_PRIME_URL, // Netlify previews
    process.env.CF_PAGES_URL, // Cloudflare Pages
    process.env.VERCEL_URL ? `https://${process.env.VERCEL_URL}` : undefined, // Vercel
  ].filter((value) => typeof value === "string");

  for (const candidate of candidates) {
    try {
      return new URL(candidate).toString();
    } catch {
      // ignore invalid candidate
    }
  }

  return undefined;
}

/**
 * @param {string} siteUrl
 * @param {"env" | "default"} source
 * @returns {import("astro").AstroIntegration}
 */
function siteUrlLogger(siteUrl, source) {
  return /** @type {import("astro").AstroIntegration} */ ({
    name: "chartcoach:site-url",
    hooks: {
      /** @param {import("astro").HookParameters<"astro:config:setup">} options */
      "astro:config:setup": (options) => {
        const { logger } = options;
        logger.info(`site url resolved (${siteUrl}) [${source}]`);
      },
    },
  });
}

// https://astro.build/config
const envSiteUrl = resolveSiteUrl();
const siteUrl = envSiteUrl ?? "http://localhost:4321/";
const siteUrlSource = envSiteUrl ? "env" : "default";

export default defineConfig({
  site: siteUrl,
  vite: {
    envDir: monorepoRoot,
    server: {
      fs: {
        allow: [monorepoRoot],
      },
    },
    resolve: {
      alias: {
        "@chartcoach/site": fileURLToPath(new URL("./src", import.meta.url)),
      },
    },
  },
  integrations: [
    siteUrlLogger(siteUrl, siteUrlSource),
    react(),
    starlight({
      title: "Chart Coach",
      customCss: ["./src/styles/custom.css"],
      social: [{ icon: "github", label: "GitHub", href: "http://github.com/peter-gy/chartcoach" }],
      components: {
        TableOfContents: "./src/components/starlight/TableOfContents.astro",
        MobileTableOfContents: "./src/components/starlight/MobileTableOfContents.astro",
      },
      sidebar: [
        {
          label: "Start",
          items: [
            { label: "Overview", link: "/" },
            { label: "Catalog structure", link: "/catalog/" },
            { label: "Labels & filters", link: "/labels/" },
            { label: "About", link: "/about/" },
          ],
        },
        {
          label: "Catalog",
          items: [{ label: "Guidelines", link: "/guidelines/" }],
        },
      ],
    }),
    sitemap(),
  ],
});
