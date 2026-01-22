// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import sitemap from "@astrojs/sitemap";
import { fileURLToPath } from "node:url";

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

// https://astro.build/config
const siteUrl = resolveSiteUrl();

export default defineConfig({
  site: siteUrl,
  vite: {
    resolve: {
      alias: {
        "@chartcoach/site": fileURLToPath(new URL("./src", import.meta.url)),
      },
    },
  },
  integrations: [
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
    ...(siteUrl ? [sitemap()] : []),
  ],
});
