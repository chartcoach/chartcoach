import type { CollectionEntry } from "astro:content";

export type GuidelineEntry = CollectionEntry<"guidelines">;

export const GUIDELINES_PER_PAGE = 24;

export function sortGuidelines(guidelines: GuidelineEntry[]) {
  return guidelines.toSorted((a, b) => a.data.title.localeCompare(b.data.title));
}

export function getGuidelinePageCount(totalRecords: number, pageSize = GUIDELINES_PER_PAGE) {
  return Math.max(1, Math.ceil(totalRecords / pageSize));
}

export function paginateGuidelines(
  guidelines: GuidelineEntry[],
  page: number,
  pageSize = GUIDELINES_PER_PAGE,
) {
  const start = (page - 1) * pageSize;
  return guidelines.slice(start, start + pageSize);
}

export function getGuidelinesPageHref(page: number) {
  return page === 1 ? "/guidelines/" : `/guidelines/page/${page}/`;
}
