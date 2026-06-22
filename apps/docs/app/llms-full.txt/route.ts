import { getLLMText, source } from "@/lib/source";

export const revalidate = false;

export async function GET() {
  const sortedPages = source.getPages().toSorted((a, b) => a.url.localeCompare(b.url));
  const pages = await Promise.all(sortedPages.map(getLLMText));

  return new Response(pages.join("\n\n"), {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
    },
  });
}
