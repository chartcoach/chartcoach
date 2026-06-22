import { getSiteRuntimeConfig } from "@/config/site";

export const prerender = true;

export function GET() {
  const { isPreviewDeployment, siteUrl } = getSiteRuntimeConfig();
  const body = isPreviewDeployment
    ? "User-agent: *\nDisallow: /\n"
    : `User-agent: *\nAllow: /\nSitemap: ${new URL("/sitemap-index.xml", siteUrl).toString()}\n`;

  return new Response(body, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
    },
  });
}
