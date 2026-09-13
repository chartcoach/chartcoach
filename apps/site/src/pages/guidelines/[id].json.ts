import type { APIRoute } from "astro";
import type { CollectionEntry } from "astro:content";
import { getCollection } from "astro:content";

import { serializeGuidelineRecord } from "@/lib/guideline-record";

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
  return new Response(serializeGuidelineRecord(guideline.data.record), {
    headers: {
      "Content-Type": "application/json; charset=utf-8",
    },
  });
};
