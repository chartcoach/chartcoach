import type starlight from "@astrojs/starlight";

type StarlightConfig = Parameters<typeof starlight>[0];

export const sidebar = [
  {
    label: "Start",
    items: [
      { label: "Overview", slug: "index" },
      { label: "Catalog structure", slug: "catalog" },
      { label: "Labels and filters", slug: "labels" },
    ],
  },
  {
    label: "API Reference",
    items: [
      { label: "Overview", slug: "api" },
      { label: "Catalog records", slug: "api/catalog-records" },
      { label: "Python API", slug: "api/python" },
      { label: "JavaScript API", slug: "api/javascript" },
      { label: "Browser loading", slug: "api/browser" },
      { label: "CLI", slug: "api/cli" },
      { label: "MCP", slug: "api/mcp" },
    ],
  },
] satisfies StarlightConfig["sidebar"];
