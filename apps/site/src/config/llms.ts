import { toMarkdown } from "@chartcoach/catalog";

import type { LlmPageSource, LlmPageSourceContext } from "../integrations/llms";
import { serializeGuidelineMarkdown } from "../lib/guideline-markdown";
import {
  EXTERNAL_HREFS,
  GUIDELINE_ROUTE_PATTERNS,
  guidelineMarkdownPath,
  guidelinePath,
  SITE_PATHS,
} from "../lib/routes";
import { loadSiteCatalog } from "./catalog-location";

export async function chartcoachLlmPages({ root }: LlmPageSourceContext): Promise<LlmPageSource[]> {
  const catalog = await loadSiteCatalog(root);
  const guidelines = Array.from(catalog).sort((a, b) => a.title.localeCompare(b.title));

  const guidelinePages = guidelines.map((guideline): LlmPageSource => {
    const referencesBib = guideline.references.length > 0 ? guideline.references.join("\n\n") : "";

    return {
      pathname: guidelinePath(guideline.id),
      title: guideline.title,
      description: guideline.description,
      markdown: serializeGuidelineMarkdown(toMarkdown(guideline), referencesBib),
      markdownPathname: guidelineMarkdownPath(guideline.id),
      writeMarkdown: false,
    };
  });

  return [...sitePages(guidelines.length), ...guidelinePages];
}

function sitePages(guidelineCount: number): LlmPageSource[] {
  return [
    {
      pathname: SITE_PATHS.home,
      title: "chartcoach",
      description:
        "chartcoach helps chart agents review charts with guidance they can inspect and cite.",
      markdownPathname: SITE_PATHS.indexMarkdown,
      markdown: [
        "# chartcoach",
        "",
        "chartcoach gives agents citable visualization guidance. Use it to review charts, recommend encodings, evaluate trade-offs, and explain which guidance supports each recommendation.",
        "",
        "## Resources",
        "",
        `- [Browse the Guideline Catalog](${SITE_PATHS.guidelines})`,
        `- [Read docs](${EXTERNAL_HREFS.docs})`,
        `- [Catalog repository](${EXTERNAL_HREFS.catalogRepository})`,
        `- [Agent skills](${EXTERNAL_HREFS.skillsRepository})`,
        "",
        "## What the catalog provides",
        "",
        "- Human-readable guideline Markdown",
        "- Guidance available through the Python API, TypeScript API, and CLI",
        "- Section roles for advice, reason, context, exceptions, costs, mistakes, checks, and fixes",
        "- References for grounded responses",
        "- Search-ready guidance for embeddings, clustering, and coverage analysis",
      ].join("\n"),
    },
    {
      pathname: SITE_PATHS.guidelines,
      title: "Guideline Catalog",
      description: `Browse ${guidelineCount.toLocaleString()} chartcoach guideline pages for chart guidance, source links, and machine-readable Markdown and JSON.`,
      markdownPathname: SITE_PATHS.guidelinesMarkdown,
      markdown: [
        "# Guideline Catalog",
        "",
        `The Guideline Catalog contains ${guidelineCount.toLocaleString()} visualization guideline entries.`,
        "",
        "Each guideline has a public page for reading, a Markdown route for agents, and a JSON route for apps that need the same guidance and source links.",
        "",
        `Use \`${GUIDELINE_ROUTE_PATTERNS.markdown}\` for the Markdown representation and \`${GUIDELINE_ROUTE_PATTERNS.json}\` for the structured representation.`,
      ].join("\n"),
    },
  ];
}
