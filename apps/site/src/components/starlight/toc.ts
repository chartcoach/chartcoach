type TocItem = {
  slug: string;
  text: string;
  depth: number;
  children: TocItem[];
};

export function removeOverviewTocItem(items: TocItem[]): TocItem[] {
  return items
    .filter((item) => item.slug !== "_top")
    .map((item) => ({
      ...item,
      children: removeOverviewTocItem(item.children ?? []),
    }));
}
