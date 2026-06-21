import { llms } from "fumadocs-core/source";

import { source } from "@/lib/source";

export const revalidate = false;

export function GET() {
  const body = llms(source)
    .index()
    .replace(/^# Docs\b/, "# chartcoach docs")
    .replace(/\n- \*\*Separator\*\*\n/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trimEnd();

  return new Response(`${body}\n`, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
    },
  });
}
