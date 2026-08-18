import { defineConfig, defineDocs } from "fumadocs-mdx/config";
import { metaSchema, pageSchema } from "fumadocs-core/source/schema";
import type { LLMsOptions } from "fumadocs-core/mdx-plugins/remark-llms";
import { remarkMarimo } from "@marimo-team/mdx-marimo/remark";

const llmsOptions: LLMsOptions = {
  mdxAsPlaceholder: [
    "Callout",
    "CatalogNotebookRuntime",
    "PythonNotebookRuntime",
    "marimo-mdx-island",
  ],
};

export const docs = defineDocs({
  dir: "content/docs",
  docs: {
    schema: pageSchema,
    postprocess: {
      includeProcessedMarkdown: llmsOptions,
    },
  },
  meta: {
    schema: metaSchema,
  },
});

export default defineConfig({
  mdxOptions: {
    rehypeCodeOptions: {
      themes: {
        light: "github-light-high-contrast",
        dark: "github-dark-high-contrast",
      },
    },
    remarkPlugins: [
      [
        remarkMarimo,
        {
          compiler: {
            uvCommand: "uv",
          },
        },
      ],
    ],
  },
});
