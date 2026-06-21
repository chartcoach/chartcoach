import type { Loader } from "astro/loaders";

import Cite from "citation-js";
import sanitizeHtml from "sanitize-html";

import { toMarkdown } from "@chartcoach/catalog";

import {
  catalogSourceRecordPath,
  catalogSourceWatchFiles,
  loadSiteCatalog,
  resolveCatalogSource,
  resolveSiteCatalogSource,
} from "../config/catalog-source";
import { createGuidelineRecord } from "../lib/guideline-record";
import { createGuidelineSearchModel } from "../lib/guideline-search-model";

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
  // Link DOI/URL tokens without absorbing trailing citation punctuation.
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

function buildReferencesByKey(references: string[]): Map<string, ReferenceInfo> {
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

  return referencesByKey;
}

function renderBibliographyHtml(
  citedKeys: Iterable<string>,
  referencesByKey: Map<string, ReferenceInfo>,
): string | undefined {
  const citedCsl = Array.from(citedKeys)
    .map((key) => referencesByKey.get(key)?.csl ?? [])
    .flat()
    .filter(Boolean);

  if (citedCsl.length === 0) return undefined;

  try {
    let bibliographyHtml = new Cite(citedCsl).format("bibliography", {
      format: "html",
      template: "apa",
      lang: "en-US",
    });
    bibliographyHtml = bibliographyHtml.replace(
      /<div data-csl-entry-id="([^"]+)"/g,
      (_m, id: string) => `<div id="${citeId(id)}" data-csl-entry-id="${id}"`,
    );
    return sanitizeCitationHtml(linkifyHtml(bibliographyHtml));
  } catch {
    return undefined;
  }
}

function renderCitationsInMarkdown(
  body: string,
  referencesByKey: Map<string, ReferenceInfo>,
): RenderedCitations {
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
      const escapedKey = escapeHtmlAttribute(key);
      if (!ref) {
        return `<span class="citation citation--missing" title="Missing reference: ${escapedKey}">@${escapedKey}</span>`;
      }

      if (!ref.csl?.length) {
        return `<span class="citation citation--missing" title="Invalid reference entry: ${escapedKey}">@${escapedKey}</span>`;
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

      return `<a class="citation" href="#${citeId(key)}" data-citekey="${escapedKey}"${titleAttr}>${ref.inlineHtml}</a>`;
    });

    return `(${parts.join("; ")})`;
  });

  return {
    body: processed,
    citedKeys: Array.from(citedKeys),
    bibliographyHtml: renderBibliographyHtml(citedKeys, referencesByKey),
  };
}

export function guidelinesLoader({
  source,
}: {
  source?: string;
} = {}): Loader {
  return {
    name: "chartcoach-guidelines-loader",
    async load(context) {
      const catalogSource = source
        ? resolveCatalogSource(source, context.config.root)
        : resolveSiteCatalogSource(context.config.root);
      const watchedFiles = catalogSourceWatchFiles(context.config.root, source);
      if (watchedFiles.length > 0) context.watcher?.add(watchedFiles);

      const catalog = await loadSiteCatalog(context.config.root, source);
      const guidelines = Array.from(catalog);
      context.store.clear();

      const storeEntries = await Promise.all(
        guidelines.map(async (guideline) => {
          const id = guideline.id;
          const references = [...guideline.references];
          const record = createGuidelineRecord(guideline);
          const referencesBib = references.length > 0 ? references.join("\n\n") : undefined;
          const referencesByKey = buildReferencesByKey(references);

          const renderedBody = renderCitationsInMarkdown(guideline.body, referencesByKey);
          const citedKeys = new Set(renderedBody.citedKeys);
          const sectionInputs = guideline.sections.map((section) => {
            const renderedSection = renderCitationsInMarkdown(section.content, referencesByKey);
            for (const key of renderedSection.citedKeys) citedKeys.add(key);

            return {
              role: section.role,
              title: section.title,
              body: renderedSection.body,
            };
          });
          const sectionMarkdown = await Promise.all(
            sectionInputs.map((section) => context.renderMarkdown(section.body)),
          );
          const sections = sectionInputs.map((section, index) => ({
            role: section.role,
            title: section.title,
            html: sectionMarkdown[index]?.html ?? "",
          }));
          const bibliographyHtml = renderBibliographyHtml(citedKeys, referencesByKey);

          const [data, rendered] = await Promise.all([
            context.parseData({
              id,
              data: {
                id: guideline.id,
                title: guideline.title,
                description: guideline.description || undefined,
                labels: [...guideline.labels],
                markdown: toMarkdown(guideline),
                record,
                search: createGuidelineSearchModel(guideline),
                sections,
                bibliography: guideline.bibliography,
                referencesBib,
                citations: Array.from(citedKeys),
                bibliographyHtml,
              },
            }),
            context.renderMarkdown(renderedBody.body),
          ]);
          const digest = context.generateDigest(`${renderedBody.body}\n\n${referencesBib ?? ""}`);
          const filePath = catalogSourceRecordPath(context.config.root, catalogSource, id);

          return {
            id,
            data,
            body: renderedBody.body,
            rendered,
            digest,
            filePath,
            assetImports: rendered.metadata?.imagePaths,
          };
        }),
      );

      for (const entry of storeEntries) {
        context.store.set(entry);
      }
    },
  };
}
