import defaultMdxComponents from "fumadocs-ui/mdx";
import type { MDXComponents } from "mdx/types";

import { CatalogNotebookRuntime, PythonNotebookRuntime } from "@/components/notebook-runtime";

export function getMDXComponents(components?: MDXComponents) {
  return {
    ...defaultMdxComponents,
    CatalogNotebookRuntime,
    PythonNotebookRuntime,
    ...components,
  } satisfies MDXComponents;
}

declare global {
  type MDXProvidedComponents = ReturnType<typeof getMDXComponents>;
}
