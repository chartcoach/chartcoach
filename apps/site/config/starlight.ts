import type starlight from "@astrojs/starlight";

import { sidebar } from "../astro.sidebar";
import { createSocialImageHead } from "../src/lib/site-metadata";
import { siteSocialLinks } from "./navigation";

type StarlightUserConfig = Parameters<typeof starlight>[0];
type StarlightComponents = NonNullable<StarlightUserConfig["components"]>;

const baseComponents = {
  Header: "./src/components/starlight/Header.astro",
  Pagination: "./src/components/starlight/Pagination.astro",
  TableOfContents: "./src/components/starlight/TableOfContents.astro",
  MobileTableOfContents: "./src/components/starlight/MobileTableOfContents.astro",
} satisfies StarlightComponents;

const defaultDocsShareImage = "/social/chartcoach-share-default.png";

export const docsHeadDefaults = createSocialImageHead(defaultDocsShareImage);

function createStarlightComponents(enableAgentationReview: boolean): StarlightComponents {
  if (!enableAgentationReview) return baseComponents;

  return {
    ...baseComponents,
    PageFrame: "./src/components/starlight/PageFrameAgentation.astro",
  };
}

export function createStarlightConfig({
  enableAgentationReview,
}: {
  enableAgentationReview: boolean;
}): StarlightUserConfig {
  return {
    title: "Chart Coach",
    favicon: "/brand/chartcoach-favicon.svg",
    logo: {
      src: "./src/assets/brand/chartcoach-logo-header.svg",
      alt: "Chart Coach",
      replacesTitle: true,
    },
    customCss: ["./src/styles/custom.css"],
    social: siteSocialLinks,
    head: docsHeadDefaults,
    components: createStarlightComponents(enableAgentationReview),
    sidebar,
  };
}
