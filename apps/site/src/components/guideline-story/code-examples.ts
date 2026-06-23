import type { CodeLine, CodeToken, TokenKind } from "./types";
import { guidelineRoleSections } from "./role-sections";

export const markdownLines: readonly CodeLine[] = [
  line(t("---", "comment")),
  line(t("id", "key"), t(": "), t("direct-labels", "string")),
  line(t("title", "key"), t(": "), t("Use direct labels", "string")),
  line(t("labels", "key"), t(":")),
  line(t("  - "), t("chart:bar", "string")),
  line(t("  - "), t("task:compare", "string")),
  line(t("  - "), t("quality:readability", "string")),
  line(t("---", "comment")),
  line(),
  ...guidelineRoleSections.flatMap((section, index) => [
    line(t(`## ${section.title} `), t(`<!-- role: ${section.role} -->`, "comment")),
    line(t(section.text)),
    ...(index < guidelineRoleSections.length - 1 ? [line()] : []),
  ]),
];

export const jsonLines: readonly CodeLine[] = [
  line(t("{", "punctuation")),
  line(t('  "id"', "key"), t(": "), t('"direct-labels"', "string"), t(",", "punctuation")),
  line(t('  "title"', "key"), t(": "), t('"Use direct labels"', "string"), t(",", "punctuation")),
  line(t('  "labels"', "key"), t(": "), t("[", "punctuation")),
  line(t("    "), t('"chart:bar"', "string"), t(",", "punctuation")),
  line(t("    "), t('"task:compare"', "string"), t(",", "punctuation")),
  line(t("    "), t('"quality:readability"', "string")),
  line(t("  ", "plain"), t("]", "punctuation"), t(",", "punctuation")),
  line(t('  "sections"', "key"), t(": "), t("[", "punctuation")),
  ...guidelineRoleSections.flatMap((section, index) => jsonSectionLines(section, index)),
  line(t("  ", "plain"), t("]", "punctuation"), t(",", "punctuation")),
  line(t('  "references"', "key"), t(": "), t("[", "punctuation")),
  line(t("    "), t('"muth_text_in_data_visualizations_2022"', "string")),
  line(t("  "), t("]", "punctuation")),
  line(t("}", "punctuation")),
];

export const typescriptLines: readonly CodeLine[] = [
  line(
    t("import", "keyword"),
    t(" { "),
    t("DEFAULT_CATALOG"),
    t(", "),
    t("loadCatalog", "function"),
    t(" } "),
    t("from", "keyword"),
    t(" "),
    t('"@chartcoach/catalog"', "string"),
  ),
  line(),
  line(t("const", "keyword"), t(" { entriesUrl, manifestUrl } = "), t("DEFAULT_CATALOG")),
  line(
    t("const", "keyword"),
    t(" entries = "),
    t("await", "keyword"),
    t(" "),
    t("("),
    t("await", "keyword"),
    t(" "),
    t("fetch", "function"),
    t("(entriesUrl))."),
    t("arrayBuffer", "function"),
    t("()"),
  ),
  line(
    t("const", "keyword"),
    t(" manifestText = "),
    t("await", "keyword"),
    t(" "),
    t("("),
    t("await", "keyword"),
    t(" "),
    t("fetch", "function"),
    t("(manifestUrl))."),
    t("text", "function"),
    t("()"),
  ),
  line(
    t("const", "keyword"),
    t(" catalog = "),
    t("await", "keyword"),
    t(" "),
    t("loadCatalog", "function"),
    t("({ entries, manifestText })"),
  ),
  line(
    t("const", "keyword"),
    t(" entry = catalog."),
    t("require", "function"),
    t("("),
    t('"direct-labels"', "string"),
    t(")"),
  ),
  line(),
  line(t("const", "keyword"), t(" summary = "), t("{", "punctuation")),
  line(t("  title: entry.title,")),
  line(t("  labels: entry.labels,")),
  line(t("  references: entry.references,")),
  line(t("}", "punctuation")),
];

export const pythonLines: readonly CodeLine[] = [
  line(
    t("from", "keyword"),
    t(" chartcoach "),
    t("import", "keyword"),
    t(" "),
    t("Catalog", "type"),
  ),
  line(),
  line(t("catalog"), t(" = "), t("Catalog", "type"), t("."), t("open", "function"), t("()")),
  line(
    t("entry"),
    t(" = catalog."),
    t("entry", "function"),
    t("("),
    t('"direct-labels"', "string"),
    t(")"),
  ),
  line(),
  line(t("summary"), t(" = {")),
  line(t("    "), t('"title"', "string"), t(": entry["), t('"title"', "string"), t("],")),
  line(t("    "), t('"labels"', "string"), t(": entry["), t('"labels"', "string"), t("],")),
  line(t("    "), t('"references"', "string"), t(": entry["), t('"references"', "string"), t("],")),
  line(t("}")),
];

export const shellLines: readonly CodeLine[] = [
  line(t("chartcoach", "function"), t(" catalog read "), t("direct-labels", "string")),
  line(
    t("chartcoach", "function"),
    t(" catalog find "),
    t('"legend lookup in bar chart"', "string"),
  ),
  line(t("chartcoach", "function"), t(" catalog cite "), t("direct-labels", "string")),
];

function t(text: string, kind?: TokenKind): CodeToken {
  return { text, kind };
}

function line(...tokens: CodeToken[]): CodeLine {
  return tokens;
}

function jsonSectionLines(
  section: (typeof guidelineRoleSections)[number],
  index: number,
): CodeLine[] {
  const text = jsonSectionText(section.role);

  return [
    line(
      t("    "),
      t("{", "punctuation"),
      t(" "),
      t('"role"', "key"),
      t(": "),
      t(`"${section.role}"`, "string"),
      t(",", "punctuation"),
      t(" "),
      t('"text"', "key"),
      t(": "),
      t(`"${text}"`, "string"),
      t(" "),
      t("}", "punctuation"),
      ...(index < guidelineRoleSections.length - 1 ? [t(",", "punctuation")] : []),
    ),
  ];
}

function jsonSectionText(role: (typeof guidelineRoleSections)[number]["role"]): string {
  switch (role) {
    case "advice":
      return "Place labels beside values.";
    case "reason":
      return "Reduce legend lookup work.";
    case "context":
      return "Use with small bar sets.";
    case "exceptions":
      return "Keep legends when labels crowd.";
    case "costs":
      return "Uses plot space.";
    case "mistakes":
      return "Do not label dense marks.";
    case "check":
      return "Can values be read directly?";
    case "fix":
      return "Move labels beside marks.";
  }
}
