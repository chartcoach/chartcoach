import {
  Citation,
  CitationGroup,
  Document,
  Library,
  Style,
  tidyBibtex,
  type Entry,
  type RenderedNode,
} from "refkit-js";
import sanitizeHtml from "sanitize-html";

function escapeHtml(value: string): string {
  return value.replace(
    /[&<>"']/g,
    (character) =>
      ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;",
      })[character]!,
  );
}

function citeId(key: string): string {
  return `ref-${key}`;
}

function nodeText(node: RenderedNode): string {
  if (node.kind === "Element") return node.children.map(nodeText).join("");

  if (node.kind === "Markup") return node.value;

  if (node.kind === "Transparent") return "";

  return node.text;
}

function inlineHtml(node: RenderedNode, hover: Map<string, string>): string {
  if (node.kind === "Element") {
    const html = node.children.map((child) => inlineHtml(child, hover)).join("");

    if (node.meta?.kind !== "Entry") return html;
    const key = node.meta.key;

    return `<a class="citation" href="#${encodeURIComponent(citeId(key))}" data-citekey="${escapeHtml(key)}" title="${escapeHtml(hover.get(key) ?? key)}">${html}</a>`;
  }

  let html = escapeHtml(nodeText(node));

  if (node.kind === "Text" || node.kind === "Link") {
    const format = node.formatting;

    if (format.fontStyle === "Italic") html = `<i>${html}</i>`;

    if (format.fontWeight === "Bold") html = `<b>${html}</b>`;

    if (format.textDecoration === "Underline") html = `<u>${html}</u>`;

    if (format.verticalAlign === "Sup") html = `<sup>${html}</sup>`;

    if (format.verticalAlign === "Sub") html = `<sub>${html}</sub>`;
  }

  return html;
}

export function renderGuidelineCitations(bodies: readonly string[], references: readonly string[]) {
  // Parse each reference in its own macro scope before sharing citation state.
  const entries = new Map<string, Entry>();

  for (const source of references) {
    const parsed = Library.parseBibtex(tidyBibtex(source).bibtex, { recovery: "report" });

    for (const entry of parsed) {
      if (!entries.has(entry.key)) entries.set(entry.key, entry);
    }
  }

  const library = Library.fromRecords(entries.values());

  const citedKeys = new Set<string>();
  const groups: { keys: string[]; id: string }[] = [];
  const citations: Citation[] = [];
  const pattern = /\[([^\]]*?@[^\]]+?)\]/g;

  for (const body of bodies) {
    for (const match of body.matchAll(pattern)) {
      const keys = Array.from(match[1].matchAll(/@([^\s;,\]]+)/g), (key) => key[1]);
      const id = String(groups.length);
      groups.push({ keys, id });

      for (const key of keys) citedKeys.add(key);
      const valid = keys.filter((key) => library.has(key));

      if (valid.length) citations.push(new Citation(id, new CitationGroup(valid)));
    }
  }

  const rendered = new Document(library, Style.load("apa"), { locale: "en-US" }).render(citations);
  const hover = new Map<string, string>();

  for (const entry of rendered.bibliography.tree) {
    if (entry.kind === "bibliography-entry") {
      hover.set(entry.key, entry.content.map(nodeText).join("").replace(/\s+/g, " ").trim());
    }
  }

  let groupIndex = 0;

  const renderedBodies = bodies.map((body) =>
    body.replace(pattern, () => {
      const { keys, id } = groups[groupIndex++];
      const citation = rendered.citations[id];

      const html =
        citation?.tree
          .map((node) => (node.kind === "bibliography-entry" ? "" : inlineHtml(node, hover)))
          .join("") ?? "";

      const missing = keys
        .filter((key) => !library.has(key))
        .map(
          (key) =>
            `<span class="citation citation--missing" title="Missing reference: ${escapeHtml(key)}">@${escapeHtml(key)}</span>`,
        );

      return [html, ...missing].filter(Boolean).join(" ");
    }),
  );

  const bibliographyHtml = citations.length
    ? sanitizeHtml(rendered.bibliography.html, {
        allowedTags: ["a", "div", "span", "p", "br", "i", "b", "em", "strong", "u", "sup", "sub"],
        allowedAttributes: {
          a: ["href", "rel", "target"],
          div: ["id", "class", "data-citekey"],
          span: ["class"],
        },
        allowedSchemes: ["http", "https", "mailto"],
        allowProtocolRelative: false,
        transformTags: {
          div(tagName, attributes) {
            const key = attributes["data-key"];

            return {
              tagName,
              attribs: key ? { ...attributes, id: citeId(key), "data-citekey": key } : attributes,
            };
          },
          a: sanitizeHtml.simpleTransform("a", { target: "_blank", rel: "noreferrer" }),
        },
      })
    : undefined;

  return { bodies: renderedBodies, citedKeys: Array.from(citedKeys), bibliographyHtml };
}
