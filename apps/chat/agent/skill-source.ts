import { parse } from "yaml";
import { z } from "zod";

const metadataSchema = z.object({ description: z.string().trim().min(1) });

export function parseSkill(text: string) {
  const parts = /^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/.exec(text);

  if (!parts) throw new Error("Skills need YAML frontmatter and Markdown instructions.");
  const metadata = metadataSchema.parse(parse(parts[1]));

  return { description: metadata.description, markdown: parts[2].trim() };
}
