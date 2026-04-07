export function createGuidelinePageFrontmatter({
  title,
  description,
}: {
  title: string;
  description?: string;
}) {
  return {
    title,
    description,
    tableOfContents: false,
  };
}
