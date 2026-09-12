export const SITE_PATHS = {
  home: "/",
  guidelines: "/guidelines/",
  indexMarkdown: "/index.md",
  guidelinesMarkdown: "/guidelines.md",
} as const;

export const GUIDELINE_ROUTE_PATTERNS = {
  json: "/guidelines/{id}.json",
  markdown: "/guidelines/{id}.md",
} as const;

export const EXTERNAL_HREFS = {
  docs: "https://docs.chartcoach.dev/",
  docsGettingStarted: "https://docs.chartcoach.dev/getting-started",
  catalogRepository: "https://github.com/chartcoach/catalog",
  skillsRepository: "https://github.com/chartcoach/skills",
  paper: "https://arxiv.org/abs/2512.20306",
  contact: "mailto:pgyarmati@ethz.ch",
} as const;

function pathSegment(value: string): string {
  return encodeURIComponent(value);
}

export function isExternalHttpHref(href: string): boolean {
  return /^https?:\/\//.test(href);
}

export function externalHrefLabel(href: string): string {
  return href.replace(/^https?:\/\//, "").replace(/\/$/, "");
}

export function normalizePathname(pathname: string): string {
  if (!pathname || pathname === SITE_PATHS.home) return SITE_PATHS.home;

  const withLeadingSlash = pathname.startsWith("/") ? pathname : `/${pathname}`;

  return withLeadingSlash.endsWith("/") ? withLeadingSlash : `${withLeadingSlash}/`;
}

export function guidelinePath(guidelineId: string): string {
  return `/guidelines/${pathSegment(guidelineId)}/`;
}

function guidelineJsonPath(guidelineId: string): string {
  return `/guidelines/${pathSegment(guidelineId)}.json`;
}

export function guidelineMarkdownPath(guidelineId: string): string {
  return `/guidelines/${pathSegment(guidelineId)}.md`;
}

export function guidelineJsonOgImagePath(guidelineId: string): string {
  return `${guidelineJsonPath(guidelineId)}.png`;
}

export function guidelineMarkdownOgImagePath(guidelineId: string): string {
  return `${guidelineMarkdownPath(guidelineId)}.png`;
}

export function guidelinesPagePath(page: number): string {
  return page <= 1 ? SITE_PATHS.guidelines : `/guidelines/page/${page}/`;
}

export function catalogGuidelineMarkdownSourceHref(guidelineId: string): string {
  return `${EXTERNAL_HREFS.catalogRepository}/blob/main/entries/${pathSegment(guidelineId)}/guideline.md`;
}

export function ogImagePathname(pagePathname: string): string {
  return `${normalizePathname(pagePathname)}og.png`.replace(/^\/\//, "/");
}

export function ogImageUrl(site: string | URL, pagePathname: string): string {
  return new URL(ogImagePathname(pagePathname).replace(/^\//, ""), site).toString();
}
