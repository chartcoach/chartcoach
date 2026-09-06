import type { StoryStep } from "./types";

export const steps: readonly StoryStep[] = [
  {
    eyebrow: "Plain Markdown",
    title: "Readable by people",
    body: "A guideline is a Markdown document with a small metadata header and natural-language sections for advice, rationale, context, checks, and fixes.",
    surface: {
      intent: "Readable by people",
      form: "Markdown document",
      detail: "advice, context, checks",
    },
    artifact: "markdown",
  },
  {
    eyebrow: "References",
    title: "Traceable to sources",
    body: "Guidelines cite papers, standards, and practitioner material, so feedback can name where its recommendation came from.",
    surface: {
      intent: "Traceable to sources",
      form: "References",
      detail: "papers and practice",
    },
    artifact: "references",
  },
  {
    eyebrow: "Section Roles",
    title: "Structured for machines",
    body: "Agents can ask for the advice, rationale, context, exceptions, costs, mistakes, checks, and fixes separately.",
    surface: {
      intent: "Structured for machines",
      form: "Role-annotated sections",
      detail: "granular structure",
    },
    artifact: "structured",
  },
  {
    eyebrow: "Semantic Index",
    title: "Searchable by meaning",
    body: "The Guideline Catalog supports semantic search across guideline sections, so agents can retrieve the relevant passage for a chart task.",
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
    body: "People and apps can open the same guidance through public pages, Markdown, JSON, Python, TypeScript, and the CLI.",
    surface: {
      intent: "Portable across tools",
      form: "Open formats",
      detail: "Markdown, JSON, APIs",
    },
    artifact: "access",
  },
  {
    eyebrow: "Agent skills",
    title: "Agent-ready",
    body: "Agent skills give agents a repeatable path from retrieval to cited answer, chart evaluation, and contribution draft.",
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
    body: "After human confirmation, agents can draft a GitHub issue for missing or contested guidance in the catalog repository.",
    surface: {
      intent: "Open to revision",
      form: "catalog repository",
      detail: "GitHub issues and review",
    },
    artifact: "improve",
  },
] as const;
