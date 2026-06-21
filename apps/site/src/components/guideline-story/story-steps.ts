import type { StoryStep } from "./types";

export const steps: readonly StoryStep[] = [
  {
    eyebrow: "Plain Markdown",
    title: "Readable by people",
    body: "Guidelines stay in Markdown with clear titles, labels, and eight role-marked sections.",
    surface: {
      intent: "Readable by people",
      form: "Guideline records",
      detail: "plain-language roles",
    },
    artifact: "markdown",
  },
  {
    eyebrow: "Cited Sources",
    title: "Traceable to sources",
    body: "Records carry references so feedback can point back to papers, standards, and practitioner material.",
    surface: {
      intent: "Traceable to sources",
      form: "Cited references",
      detail: "papers and practice",
    },
    artifact: "source",
  },
  {
    eyebrow: "Section Roles",
    title: "Structured for machines",
    body: "Advice, reason, context, exceptions, costs, mistakes, check, and fix sections are available as fields.",
    surface: {
      intent: "Structured for machines",
      form: "Role-marked sections",
      detail: "eight section roles",
    },
    artifact: "structured",
  },
  {
    eyebrow: "Semantic Index",
    title: "Searchable by meaning",
    body: "Each role-marked section can be retrieved by labels, role, text search, or semantic similarity.",
    surface: {
      intent: "Searchable by meaning",
      form: "Semantic index",
      detail: "role-aware matches",
    },
    artifact: "embedding",
  },
  {
    eyebrow: "Open Formats",
    title: "Portable across tools",
    body: "The same role-marked record can be loaded from the site, Markdown, JSON, Python, TypeScript, and the CLI.",
    surface: {
      intent: "Portable across tools",
      form: "Open formats",
      detail: "Markdown, JSON, SDKs",
    },
    artifact: "access",
  },
  {
    eyebrow: "Agent Skill",
    title: "Agent-ready",
    body: "Skills tell agents how to retrieve records, cite them, apply them, evaluate charts, and propose contributions.",
    surface: {
      intent: "Agent-ready",
      form: "Agent skills",
      detail: "retrieve, cite, apply",
    },
    artifact: "skills",
  },
  {
    eyebrow: "Public Review",
    title: "Open to revision",
    body: "Missing or contested guidance can become a GitHub issue in the public catalog repository.",
    surface: {
      intent: "Open to revision",
      form: "Public repository",
      detail: "GitHub issues and review",
    },
    artifact: "improve",
  },
] as const;
