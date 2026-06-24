import Cite from "citation-js";

import { cleanOgText, truncateOgText } from "./text";
import type { OgReferenceSummary } from "./schema";

const bibEntryPattern = /@\w+\s*\{[\s\S]*?(?=\n\s*@\w+\s*\{|$)/g;

type CslName = {
  family?: string;
  literal?: string;
};

type CslReference = {
  author?: CslName[];
  issued?: {
    "date-parts"?: (number | string)[][];
  };
  publisher?: string;
  title?: string;
  "container-title"?: string;
};

function readBibField(entry: string, field: string): string | undefined {
  const match = entry.match(
    new RegExp(`${field}\\s*=\\s*(?:\\{([\\s\\S]*?)\\}|"([\\s\\S]*?)")\\s*,?`, "i"),
  );
  return match ? cleanBibValue(match[1] ?? match[2] ?? "") : undefined;
}

function cleanBibValue(value: string): string {
  return cleanOgText(value.replace(/[{}]/g, "").replace(/\\&/g, "&"));
}

function formatAuthors(value: string | undefined): string | undefined {
  if (!value) return undefined;
  const authors = value.split(/\s+and\s+/i).map((author) => cleanOgText(author));
  if (authors.length === 0) return undefined;
  const first = authors[0];
  const family = first.includes(",") ? first.split(",")[0] : first.split(" ").at(-1);
  if (!family) return undefined;
  return authors.length > 1 ? `${family} et al.` : family;
}

function formatMeta(entry: string): string | undefined {
  const authors = formatAuthors(readBibField(entry, "author"));
  const note = readBibField(entry, "note");
  const venue =
    readBibField(entry, "journal") ??
    readBibField(entry, "booktitle") ??
    readBibField(entry, "publisher") ??
    readBibField(entry, "organization") ??
    readBibField(entry, "institution") ??
    (/\bwgbh\b/i.test(`${readBibField(entry, "howpublished") ?? ""} ${note ?? ""}`)
      ? "WGBH National Center for Accessible Media"
      : undefined);
  const year = readBibField(entry, "year");
  return [authors, venue, year].filter(Boolean).join(" · ") || undefined;
}

function formatCslAuthors(authors: CslName[] | undefined): string | undefined {
  if (!authors?.length) return undefined;
  const first = authors[0];
  const name = first?.literal ?? first?.family;
  if (!name) return undefined;
  return authors.length > 1 ? `${name} et al.` : name;
}

function formatCslMeta(reference: CslReference): string | undefined {
  const authors = formatCslAuthors(reference.author);
  const venue = reference["container-title"] ?? reference.publisher;
  const year = reference.issued?.["date-parts"]?.[0]?.[0];
  return [authors, venue, year ? String(year) : undefined].filter(Boolean).join(" · ") || undefined;
}

function summarizeWithCitationJs(bibtex: string): OgReferenceSummary[] {
  const entries = bibtex.match(bibEntryPattern) ?? [];
  try {
    return (new Cite(bibtex).data as CslReference[])
      .flatMap((reference, index) => {
        if (!reference.title) return [];
        return [
          {
            title: truncateOgText(reference.title, 132),
            meta:
              formatCslMeta(reference) ?? (entries[index] ? formatMeta(entries[index]) : undefined),
          },
        ];
      })
      .slice(0, 2);
  } catch {
    return [];
  }
}

export function summarizeGuidelineReferences(bibtex: string | undefined): OgReferenceSummary[] {
  if (!bibtex) return [];
  const citationSummaries = summarizeWithCitationJs(bibtex);
  if (citationSummaries.length > 0) return citationSummaries;

  const entries = bibtex.match(bibEntryPattern) ?? [];
  return entries
    .flatMap((entry) => {
      const title = readBibField(entry, "title");
      if (!title) return [];
      return [
        {
          title: truncateOgText(title, 132),
          meta: formatMeta(entry),
        },
      ];
    })
    .slice(0, 2);
}
