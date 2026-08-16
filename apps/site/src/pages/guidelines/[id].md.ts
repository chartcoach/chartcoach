import type { APIRoute } from "astro";
import type { CollectionEntry } from "astro:content";
import { getCollection } from "astro:content";

import { serializeGuidelineMarkdown } from "@/lib/guideline-markdown";

type Props = {
  guideline: CollectionEntry<"guidelines">;
};

export const prerender = true;

export async function getStaticPaths() {
  const guidelines = await getCollection("guidelines");
  return guidelines.map((guideline) => ({
    params: { id: guideline.id },
    props: { guideline },
  }));
}

export const GET: APIRoute<Props> = ({ props: { guideline } }) => {
  return new Response(
    serializeGuidelineMarkdown(guideline.data.markdown, guideline.data.referencesBib),
    {
      headers: {
        "Content-Type": "text/markdown; charset=utf-8",
      },
    },
  );
};
