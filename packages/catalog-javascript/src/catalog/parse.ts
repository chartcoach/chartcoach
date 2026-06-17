import { parse as parseYaml } from "yaml";
import { CatalogError } from "./errors";
import { normalizeLabel } from "./labels";
import type { Guideline, GuidelineSection } from "./model";

const UNASSIGNED_SECTION_ROLE = "__unassigned__";
export type GuidelineSource = Omit<Guideline, "references">;

export function parseSectionBlocks(body: string): GuidelineSection[] {
  const headingPattern = /^##\s+(.+?)\s*<!--\s*role:\s*(.*?)\s*-->\s*$/;

  const sections: GuidelineSection[] = [];
  const lines = body.split("\n");

  let currentSection: { role: string; title: string } | null = null;
  let currentContentLines: string[] = [];

  function flushDangling() {
    const content = currentContentLines.join("\n").trim();
    if (!content) return;
    sections.push({ role: UNASSIGNED_SECTION_ROLE, title: "", content });
    currentContentLines = [];
  }

  function flushSection() {
    if (!currentSection) return;
    const content = currentContentLines.join("\n").trim();
    sections.push({ ...currentSection, content });
    currentSection = null;
    currentContentLines = [];
  }

  for (const line of lines) {
    const match = headingPattern.exec(line);
    if (match) {
      if (currentSection) {
        flushSection();
      } else {
        flushDangling();
      }
      const role = match[2]!.trim();
      if (!role) {
        throw new CatalogError("Invalid guideline section: role must not be empty.");
      }
      currentSection = { title: match[1]!.trim(), role };
      continue;
    }
    currentContentLines.push(line);
  }

  if (currentSection) flushSection();
  else flushDangling();

  return sections;
}

export function parseMarkdownDocument(markdown: string): {
  frontmatter: Record<string, unknown>;
  body: string;
} {
  if (!markdown.startsWith("---")) return { frontmatter: {}, body: markdown };

  const parts = markdown.split("---", 3);
  if (parts.length < 3) return { frontmatter: {}, body: markdown };

  const frontmatterStr = parts[1]?.trim() ?? "";
  const body = (parts[2] ?? "").trim();

  const frontmatter = (parseYaml(frontmatterStr) as Record<string, unknown> | null) ?? {};
  return { frontmatter, body };
}

export function parseGuidelineMarkdown(markdown: string): GuidelineSource {
  const { frontmatter, body } = parseMarkdownDocument(markdown);

  const id = frontmatter.id;
  const title = frontmatter.title;
  const bibliography = frontmatter.bibliography;
  const description = frontmatter.description;
  const labels = frontmatter.labels;

  if (typeof id !== "string" || id.length === 0) {
    throw new CatalogError("Invalid guideline frontmatter: `id` must be a non-empty string.");
  }
  if (typeof title !== "string" || title.length === 0) {
    throw new CatalogError("Invalid guideline frontmatter: `title` must be a non-empty string.");
  }

  const sections = parseSectionBlocks(body);

  return {
    id,
    title,
    bibliography: typeof bibliography === "string" ? bibliography : undefined,
    description: typeof description === "string" ? description : "",
    labels: Array.isArray(labels)
      ? labels.map((label) => normalizeLabel(label, "guideline label"))
      : [],
    body,
    sections,
  };
}

export function parseBibliographyEntries(bibtexContent: string): string[] {
  const commentFree = bibtexContent
    .split("\n")
    .filter((line) => !line.trimStart().startsWith("%"))
    .join("\n");

  return commentFree
    .split(/(?=@)/g)
    .map((entry) => entry.trim())
    .filter((entry) => entry.length > 0);
}
