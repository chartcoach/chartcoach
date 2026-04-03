type SocialImageHeadEntry =
  | {
      tag: "meta";
      attrs: {
        property: "og:image";
        content: string;
      };
    }
  | {
      tag: "meta";
      attrs: {
        name: "twitter:image";
        content: string;
      };
    };

export const guidelinesShareImage = "/social/chartcoach-share-guidelines.png";

export function createSocialImageHead(image: string): SocialImageHeadEntry[] {
  return [
    {
      tag: "meta",
      attrs: { property: "og:image", content: image },
    },
    {
      tag: "meta",
      attrs: { name: "twitter:image", content: image },
    },
  ];
}

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
    head: createSocialImageHead(guidelinesShareImage),
  };
}
