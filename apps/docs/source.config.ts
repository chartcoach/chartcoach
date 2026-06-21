import { defineConfig, defineDocs } from "fumadocs-mdx/config";
import { metaSchema, pageSchema } from "fumadocs-core/source/schema";
import type { LLMsOptions } from "fumadocs-core/mdx-plugins/remark-llms";

const llmsOptions: LLMsOptions = {
  mdxAsPlaceholder: ["Callout"],
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
  mdxOptions: {},
});
