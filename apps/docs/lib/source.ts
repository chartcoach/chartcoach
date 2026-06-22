import { docs } from "collections/server";
import { renderPlaceholder } from "fumadocs-core/mdx-plugins/remark-llms.runtime";
import { loader } from "fumadocs-core/source";

import { docsContentRoute, docsOrigin, docsRoute, gitConfig } from "@/lib/shared";

export const source = loader({
  baseUrl: docsRoute,
  source: docs.toFumadocsSource(),
  plugins: [],
});

type DocsPage = (typeof source)["$inferPage"];

export function getPageMarkdownUrl(page: DocsPage) {
  const segments = [...page.slugs, "content.md"];

  return {
    segments,
    url: `${docsContentRoute}/${segments.join("/")}`,
  };
}

function getPageSourceUrl(page: DocsPage) {
  return `https://github.com/${gitConfig.user}/${gitConfig.repo}/blob/${gitConfig.branch}/apps/docs/content/docs/${page.path}`;
}

export async function getLLMText(page: DocsPage) {
  const processed = await renderPlaceholder(await page.data.getText("processed"), {
    Callout({ attributes, children }) {
      const title = typeof attributes.title === "string" ? attributes.title : "Note";
      const lines = children.trim().split("\n");
      const content = lines.map((line) => `> ${line}`.trimEnd()).join("\n");

      return `> **${title}**
${content}`;
    },
  });
  const description = page.data.description ? `${page.data.description}\n\n` : "";

  return `# ${page.data.title}

URL: ${docsOrigin}${page.url}
Source: ${getPageSourceUrl(page)}
Markdown: ${docsOrigin}${getPageMarkdownUrl(page).url}

${description}${processed}`;
}
