import { llms } from "fumadocs-core/source";

import { source } from "@/lib/source";

export const revalidate = false;

export async function GET() {
  const body = (await llms(source).index())
    .replace(/^# Docs\b/, "# chartcoach")
    .replace(/\n- \*\*Separator\*\*\n/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trimEnd();

  return new Response(`${body}\n`, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
    },
  });
}
