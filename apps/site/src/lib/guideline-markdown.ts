export function serializeGuidelineMarkdown(markdown: string, referencesBib?: string): string {
  const references = referencesBib?.trim() ?? "";

  return `${markdown.trimEnd()}\n\n---\n\n\`\`\`bibtex\n${references}\n\`\`\`\n`;
}
