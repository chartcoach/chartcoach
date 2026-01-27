import type { Loader } from "astro/loaders";
import path from "node:path";
import { fileURLToPath } from "node:url";

import Cite from "citation-js";
import sanitizeHtml from "sanitize-html";

import { loadCatalogFromFolder } from "@chartcoach/catalog/node";

type RenderedCitations = {
  body: string;
  citedKeys: string[];
  bibliographyHtml?: string;
};

type ReferenceInfo = {
  key: string;
  bibtex: string;
  csl?: unknown[];
  inlineHtml?: string;
  hoverText?: string;
};

function citeId(key: string): string {
  return `ref-${key.replace(/[^A-Za-z0-9:_-]/g, "_")}`;
}

function stripOuterParens(text: string): string {
  const trimmed = text.trim();
  if (trimmed.startsWith("(") && trimmed.endsWith(")")) return trimmed.slice(1, -1);
  return trimmed;
}

function bibtexKeyFromEntry(entry: string): string | null {
  const match = /^@\w+\s*\{\s*([^,\s]+)\s*,/m.exec(entry);
  return match?.[1]?.trim() || null;
}

function linkifyHtml(html: string): string {
  // Conservative linkification for DOI/URL strings produced by citation-js.
  return html.replace(
    /(https?:\/\/[^\s<>"']+[^\s<>"'.)\],;:])/g,
    (url) => `<a href="${url}" rel="noreferrer" target="_blank">${url}</a>`,
  );
}

function escapeHtmlAttribute(value: string): string {
  return value
    .replace(/&/g, "&amp;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

const SANITIZE_CITATION_HTML_OPTIONS: sanitizeHtml.IOptions = {
  allowedTags: [
    "a",
    "div",
    "span",
    "p",
    "ul",
    "ol",
    "li",
    "br",
    "i",
    "b",
    "em",
    "strong",
    "sup",
    "sub",
  ],
  allowedAttributes: {
    a: ["href", "rel", "target", "title", "class", "data-citekey"],
    div: ["id", "class", "data-csl-entry-id"],
    span: ["class", "title", "data-citekey"],
    "*": ["class", "id", "title", "data-csl-entry-id", "data-citekey"],
  },
  allowedSchemes: ["http", "https", "mailto"],
  allowProtocolRelative: false,
};

function sanitizeCitationHtml(html: string): string {
  return sanitizeHtml(html, SANITIZE_CITATION_HTML_OPTIONS);
}

function renderCitationsInMarkdown(body: string, references: string[]): RenderedCitations {
  const referencesByKey = new Map<string, ReferenceInfo>();
  for (const entry of references) {
    const key = bibtexKeyFromEntry(entry);
    if (!key) continue;

    const info: ReferenceInfo = { key, bibtex: entry };
    try {
      const cite = new Cite(entry);
      info.csl = cite.data;
    } catch {
      // Keep BibTeX for display, but skip CSL parsing for rendering.
    }

    referencesByKey.set(key, info);
  }

  const citedKeys = new Set<string>();

  const processed = body.replace(/\[([^\]]*?@[^\]]+?)\]/g, (match, inside) => {
    const keys: string[] = [];
    const citeKeyPattern = /@([^\s;,\]]+)/g;
    let matchResult: RegExpExecArray | null;
    while ((matchResult = citeKeyPattern.exec(inside)) !== null) {
      const key = matchResult[1];
      if (key) keys.push(key);
    }
    if (keys.length === 0) return match;

    const parts = keys.map((key) => {
      citedKeys.add(key);

      const ref = referencesByKey.get(key);
      if (!ref) {
        return `<span class="citation citation--missing" title="Missing reference: ${key}">@${key}</span>`;
      }

      if (!ref.csl?.length) {
        return `<span class="citation citation--missing" title="Invalid reference entry: ${key}">@${key}</span>`;
      }

      ref.inlineHtml ??= stripOuterParens(
        new Cite(ref.csl).format("citation", {
          format: "html",
          template: "apa",
          lang: "en-US",
        }),
      );
      ref.inlineHtml = sanitizeCitationHtml(ref.inlineHtml);

      ref.hoverText ??= (() => {
        try {
          const text = new Cite(ref.csl).format("bibliography", {
            format: "text",
            template: "apa",
            lang: "en-US",
          });
          return text.replace(/\s+/g, " ").trim();
        } catch {
          return undefined;
        }
      })();

      const titleAttr = ref.hoverText ? ` title="${escapeHtmlAttribute(ref.hoverText)}"` : "";

      return `<a class="citation" href="#${citeId(key)}" data-citekey="${key}"${titleAttr}>${ref.inlineHtml}</a>`;
    });

    return `(${parts.join("; ")})`;
  });

  let bibliographyHtml: string | undefined;
  if (citedKeys.size > 0) {
    const citedCsl = Array.from(citedKeys)
      .map((key) => referencesByKey.get(key)?.csl ?? [])
      .flat()
      .filter(Boolean);

    if (citedCsl.length > 0) {
      try {
        bibliographyHtml = new Cite(citedCsl).format("bibliography", {
          format: "html",
          template: "apa",
          lang: "en-US",
        });
        bibliographyHtml = bibliographyHtml.replace(
          /<div data-csl-entry-id="([^"]+)"/g,
          (_m, id: string) => `<div id="${citeId(id)}" data-csl-entry-id="${id}"`,
        );
        bibliographyHtml = sanitizeCitationHtml(linkifyHtml(bibliographyHtml));
      } catch {
        // If bibliography formatting fails, fall back to no bibliography.
      }
    }
  }

  return {
    body: processed,
    citedKeys: Array.from(citedKeys),
    bibliographyHtml,
  };
}

export function guidelinesLoader({
  base = "../../guidelines",
}: {
  base?: string;
} = {}): Loader {
  return {
    name: "chartcoach-guidelines-loader",
    async load(context) {
      const projectRoot = fileURLToPath(context.config.root);
      const guidelinesRoot = path.resolve(projectRoot, base);

      context.watcher?.add(guidelinesRoot);

      const catalog = await loadCatalogFromFolder(guidelinesRoot);
      context.store.clear();

      for (const entry of catalog.entries) {
        const id = entry.guideline.id;
        const referencesBib =
          entry.references.length > 0 ? entry.references.join("\n\n") : undefined;

        const { body, citedKeys, bibliographyHtml } = renderCitationsInMarkdown(
          entry.guideline.body,
          entry.references,
        );

        const sourcePath = path.resolve(projectRoot, base, id, "guideline.md");
        const filePath = path.relative(projectRoot, sourcePath);

        const data = await context.parseData({
          id,
          data: {
            id: entry.guideline.id,
            title: entry.guideline.title,
            description: entry.guideline.description || undefined,
            labels: entry.guideline.labels,
            bibliography: entry.guideline.bibliography,
            referencesBib,
            citations: citedKeys,
            bibliographyHtml,
          },
          filePath: sourcePath,
        });

        const rendered = await context.renderMarkdown(body);
        const digest = context.generateDigest(`${body}\n\n${referencesBib ?? ""}`);

        context.store.set({
          id,
          data,
          body,
          rendered,
          digest,
          filePath,
          assetImports: rendered.metadata?.imagePaths,
        });
      }
    },
  };
}
