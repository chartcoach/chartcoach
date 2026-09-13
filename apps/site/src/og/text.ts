const whitespacePattern = /\s+/g;

export function cleanOgText(value: string): string {
  return value.replace(whitespacePattern, " ").trim();
}

export function truncateOgText(value: string, maxLength: number): string {
  const clean = cleanOgText(value);

  if (clean.length <= maxLength) return clean;
  const sliced = clean.slice(0, Math.max(0, maxLength - 1));
  const lastSpace = sliced.lastIndexOf(" ");
  const prefix = lastSpace > maxLength * 0.65 ? sliced.slice(0, lastSpace) : sliced;

  return `${prefix.trim()}...`;
}

export function wrapOgText(value: string, maxLineLength: number, maxLines: number): string[] {
  const words = cleanOgText(value).split(" ").filter(Boolean);
  const lines: string[] = [];
  let current = "";

  for (const word of words) {
    const candidate = current ? `${current} ${word}` : word;

    if (candidate.length <= maxLineLength) {
      current = candidate;
      continue;
    }

    if (current) lines.push(current);
    current = word;

    if (lines.length === maxLines) break;
  }

  if (current && lines.length < maxLines) lines.push(current);

  if (lines.length === 0) return [""];

  const consumedWords = lines.join(" ").split(" ").filter(Boolean).length;

  if (consumedWords < words.length) {
    const last = lines[lines.length - 1] ?? "";
    lines[lines.length - 1] =
      last.length >= maxLineLength - 3
        ? `${last.slice(0, Math.max(0, maxLineLength - 3)).trim()}...`
        : `${last}...`;
  }

  return lines;
}
