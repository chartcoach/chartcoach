import { toMarkdown } from "@chartcoach/catalog";

import type { LlmPageSource, LlmPageSourceContext } from "../integrations/llms";
import { serializeGuidelineMarkdown } from "../lib/guideline-markdown";
import { loadSiteCatalog } from "./catalog-source";

export async function chartcoachLlmPages({ root }: LlmPageSourceContext): Promise<LlmPageSource[]> {
  const catalog = await loadSiteCatalog(root);
  const guidelines = Array.from(catalog).sort((a, b) => a.title.localeCompare(b.title));
  const guidelinePages = guidelines.map((guideline): LlmPageSource => {
    const referencesBib = guideline.references.length > 0 ? guideline.references.join("\n\n") : "";

    return {
      pathname: `/guidelines/${guideline.id}/`,
      title: guideline.title,
      description: guideline.description,
      markdown: serializeGuidelineMarkdown(toMarkdown(guideline), referencesBib),
      markdownPathname: `/guidelines/${guideline.id}.md`,
      writeMarkdown: false,
    };
  });

  return [...sitePages(guidelines.length), ...guidelinePages];
}

function sitePages(guidelineCount: number): LlmPageSource[] {
  return [
    {
      pathname: "/",
      title: "chartcoach",
      description:
        "chartcoach helps chart agents review charts with guidance they can inspect and cite.",
      markdownPathname: "/index.md",
      markdown: [
        "# chartcoach",
        "",
        "chartcoach gives agents citable visualization guidance. Use it to review charts, recommend encodings, evaluate trade-offs, and explain which guidance supports each recommendation.",
        "",
        "## Resources",
        "",
        "- [Browse the Guideline Catalog](/guidelines/)",
        "- [Read docs](https://docs.chartcoach.dev)",
        "- [Catalog repository](https://github.com/chartcoach/catalog)",
        "- [Agent skills](https://github.com/chartcoach/skills)",
        "",
        "## What the catalog provides",
        "",
        "- Human-readable guideline Markdown",
        "- Guidance available through the Python API, TypeScript API, and CLI",
        "- Section roles for advice, reason, context, exceptions, costs, mistakes, checks, and fixes",
        "- Source references for grounded responses",
        "- Search-ready guidance for embeddings, clustering, and coverage analysis",
      ].join("\n"),
    },
    {
      pathname: "/guidelines/",
      title: "Guideline Catalog",
      description: `Browse ${guidelineCount.toLocaleString()} chartcoach guideline pages for chart guidance, source links, and machine-readable Markdown and JSON.`,
      markdownPathname: "/guidelines.md",
      markdown: [
        "# Guideline Catalog",
        "",
        `The Guideline Catalog contains ${guidelineCount.toLocaleString()} visualization guideline entries.`,
        "",
        "Each guideline has a public page for reading, a Markdown route for agents, and a JSON route for apps that need the same guidance and source links.",
        "",
        "Use `/guidelines/{id}.md` for the Markdown representation and `/guidelines/{id}.json` for the structured representation.",
      ].join("\n"),
    },
  ];
}
