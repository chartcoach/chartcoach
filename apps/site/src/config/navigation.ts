import { getSiteLinks } from "@/config/site";

type SiteNavigationEntry = {
  id: "home" | "guidelines" | "getting-started" | "docs";
  href: string;
  label: string;
  external?: boolean;
};

const coreSiteNavigation = [
  {
    id: "home",
    href: "/",
    label: "Overview",
  },
  {
    id: "guidelines",
    href: "/guidelines/",
    label: "Guidelines",
  },
  {
    id: "getting-started",
    href: "/getting-started/",
    label: "Get started",
  },
] as const satisfies readonly SiteNavigationEntry[];

export function getSiteNavigation(): readonly SiteNavigationEntry[] {
  const { docsUrl } = getSiteLinks();
  return [
    ...coreSiteNavigation,
    {
      id: "docs",
      href: docsUrl,
      label: "Docs",
      external: true,
    },
  ];
}

export function getSiteSocialLinks() {
  const { repositoryUrl } = getSiteLinks();
  return repositoryUrl
    ? [
        {
          label: "GitHub",
          href: repositoryUrl,
        },
      ]
    : [];
}
