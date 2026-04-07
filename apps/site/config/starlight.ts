import type starlight from "@astrojs/starlight";

import { sidebar } from "../astro.sidebar";
import { siteSocialLinks } from "./navigation";

type StarlightUserConfig = Parameters<typeof starlight>[0];
type StarlightComponents = NonNullable<StarlightUserConfig["components"]>;

const baseComponents = {
  Header: "./src/components/starlight/Header.astro",
  Hero: "./src/components/starlight/Hero.astro",
  Pagination: "./src/components/starlight/Pagination.astro",
  SiteTitle: "./src/components/starlight/SiteTitle.astro",
  TableOfContents: "./src/components/starlight/TableOfContents.astro",
  MobileTableOfContents: "./src/components/starlight/MobileTableOfContents.astro",
} satisfies StarlightComponents;

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
    title: "Structured visualization design knowledge",
    favicon: "/brand/chartcoach-favicon.svg",
    customCss: ["./src/styles/shadcn.css", "./src/styles/custom.css"],
    social: siteSocialLinks,
    components: createStarlightComponents(enableAgentationReview),
    sidebar,
  };
}
