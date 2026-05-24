import type starlight from "@astrojs/starlight";

type StarlightUserConfig = Parameters<typeof starlight>[0];
type StarlightSidebar = NonNullable<StarlightUserConfig["sidebar"]>;
type StarlightSidebarGroup = Extract<StarlightSidebar[number], { items: any[] }>;

type SiteNavigationEntry = {
  id: "overview" | "guidelines" | "catalog" | "labels" | "api";
  href: string;
  headerLabel: string;
  sidebar?: {
    group: "Start" | "Catalog" | "API Reference";
    label: string;
  };
};

export const siteNavigation = [
  {
    id: "overview",
    href: "/",
    headerLabel: "Overview",
    sidebar: {
      group: "Start",
      label: "Overview",
    },
  },
  {
    id: "guidelines",
    href: "/guidelines/",
    headerLabel: "Guidelines",
    sidebar: {
      group: "Catalog",
      label: "Guidelines",
    },
  },
  {
    id: "catalog",
    href: "/catalog/",
    headerLabel: "Catalog",
    sidebar: {
      group: "Start",
      label: "Catalog structure",
    },
  },
  {
    id: "labels",
    href: "/labels/",
    headerLabel: "Labels",
    sidebar: {
      group: "Start",
      label: "Labels & filters",
    },
  },
  {
    id: "api",
    href: "/api/",
    headerLabel: "API",
    sidebar: {
      group: "API Reference",
      label: "Overview",
    },
  },
] as const satisfies readonly SiteNavigationEntry[];

export const headerNavigation = siteNavigation.map(({ id, href, headerLabel }) => ({
  id,
  href,
  label: headerLabel,
}));

export const siteSocialLinks = [
  {
    icon: "github",
    label: "GitHub",
    href: "https://github.com/peter-gy/chartcoach",
  },
] satisfies NonNullable<StarlightUserConfig["social"]>;

const sidebarGroupOrder = ["Start", "Catalog", "API Reference"] as const;

const apiReferenceSidebarItems = [
  { label: "Catalog records", link: "/api/catalog-records/" },
  { label: "Python", link: "/api/python/" },
  { label: "JavaScript & TypeScript", link: "/api/javascript/" },
  { label: "Browser loading", link: "/api/browser/" },
  { label: "CLI", link: "/api/cli/" },
  { label: "MCP", link: "/api/mcp/" },
  { label: "Artifacts", link: "/api/artifacts/" },
] satisfies StarlightSidebarGroup["items"];

export const sidebarNavigation = sidebarGroupOrder.reduce<StarlightSidebar>((groups, group) => {
  let items: StarlightSidebarGroup["items"] = siteNavigation
    .filter((entry) => entry.sidebar?.group === group)
    .map((entry) => ({
      label: entry.sidebar!.label,
      link: entry.href,
    }));

  if (group === "API Reference") {
    items = [...items, ...apiReferenceSidebarItems];
  }

  if (items.length === 0) return groups;

  groups.push({
    label: group,
    items,
  } satisfies StarlightSidebarGroup);

  return groups;
}, []);
