import { parse as parseYaml } from "yaml";
import {
  DANGLING_ROLE,
  type GuidelineSection,
  type GuidelineSectionIndex,
  type ParsedGuideline,
} from "./model.js";

export function parseGuidelineSections(body: string): GuidelineSection[] {
  const headingPattern = /^##\s+(.+?)\s*<!--\s*role:\s*(\S+)\s*-->\s*$/;

  const sections: GuidelineSection[] = [];
  const lines = body.split("\n");

  let currentSection: { role: string; title: string } | null = null;
  let currentContentLines: string[] = [];

  function flushDangling() {
    const content = currentContentLines.join("\n").trim();
    if (!content) return;
    sections.push({ role: DANGLING_ROLE, title: "", content });
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
      currentSection = { title: match[1]!.trim(), role: match[2]!.trim() };
      continue;
    }
    currentContentLines.push(line);
  }

  if (currentSection) flushSection();
  else flushDangling();

  return sections;
}

export function indexGuidelineSections(sections: GuidelineSection[]): GuidelineSectionIndex {
  const byRole: Record<string, GuidelineSection[]> = {};
  for (const section of sections) {
    (byRole[section.role] ??= []).push(section);
  }
  return { byRole };
}

export function parseMarkdownWithFrontmatter(markdown: string): {
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

export function parseGuideline(markdown: string): ParsedGuideline {
  const { frontmatter, body } = parseMarkdownWithFrontmatter(markdown);

  const id = frontmatter.id;
  const title = frontmatter.title;
  const bibliography = frontmatter.bibliography;
  const description = frontmatter.description;
  const labels = frontmatter.labels;

  if (typeof id !== "string" || id.length === 0) {
    throw new Error("Invalid guideline frontmatter: `id` must be a non-empty string.");
  }
  if (typeof title !== "string" || title.length === 0) {
    throw new Error("Invalid guideline frontmatter: `title` must be a non-empty string.");
  }

  const sections = parseGuidelineSections(body);

  return {
    id,
    title,
    bibliography: typeof bibliography === "string" ? bibliography : undefined,
    description: typeof description === "string" ? description : "",
    labels: Array.isArray(labels) ? labels.filter((l): l is string => typeof l === "string") : [],
    body,
    sections,
    sectionsIndex: indexGuidelineSections(sections),
  };
}

export function parseBibtex(bibtexContent: string): string[] {
  const commentFree = bibtexContent
    .split("\n")
    .filter((line) => !line.trimStart().startsWith("%"))
    .join("\n");

  return commentFree
    .split(/(?=@)/g)
    .map((entry) => entry.trim())
    .filter((entry) => entry.length > 0);
}
