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

export const jsonLines: readonly CodeLine[] = JSON.stringify(
  guidelineRoleSections.map(({ role }) => ({
    role,
    title: role[0].toUpperCase() + role.slice(1),
    content: jsonSectionText(role),
  })),
  null,
  2,
)
  .split("\n")
  .map((source) => {
    const parts = source.split(/("(?:[^"\\]|\\.)*")/g);
    return parts.map((part, index) =>
      t(
        part,
        part.startsWith('"')
          ? parts[index + 1]?.trimStart().startsWith(":")
            ? "key"
            : "string"
          : "punctuation",
      ),
    );
  });

export const typescriptLines: readonly CodeLine[] = [
  line(
    t("import", "keyword"),
    t(" { "),
    t("openCatalog", "function"),
    t(" } "),
    t("from", "keyword"),
    t(" "),
    t('"@chartcoach/catalog"', "string"),
  ),
  line(),
  line(
    t("const", "keyword"),
    t(" catalog = "),
    t("await", "keyword"),
    t(" "),
    t("openCatalog", "function"),
    t("()"),
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
    t("open_catalog", "function"),
  ),
  line(),
  line(t("catalog"), t(" = "), t("open_catalog", "function"), t("()")),
  line(t("release"), t(" = catalog.release")),
  line(
    t("entry"),
    t(" = catalog."),
    t("read", "function"),
    t("(ids=["),
    t('"direct-labels"', "string"),
    t('], source_detail="full")[0]'),
  ),
  line(),
  line(t("summary"), t(" = {")),
  line(t("    "), t('"title"', "string"), t(": entry["), t('"title"', "string"), t("],")),
  line(t("    "), t('"labels"', "string"), t(": entry["), t('"labels"', "string"), t("],")),
  line(t("    "), t('"references"', "string"), t(": entry["), t('"references"', "string"), t("],")),
  line(t("}")),
];

export const shellLines: readonly CodeLine[] = [
  line(t("uv", "function"), t(" tool install "), t("chartcoach", "string")),
  line(t("chartcoach", "function"), t(" catalog read "), t("direct-labels", "string")),
  line(
    t("chartcoach", "function"),
    t(" catalog search "),
    t('"legend lookup"', "string"),
    t(" \\"),
  ),
  line(t("  --profile openai-large")),
  line(t("chartcoach", "function"), t(" catalog cite "), t("direct-labels", "string")),
];

function t(text: string, kind?: TokenKind): CodeToken {
  return { text, kind };
}

function line(...tokens: CodeToken[]): CodeLine {
  return tokens;
}

function jsonSectionText(role: (typeof guidelineRoleSections)[number]["role"]): string {
  switch (role) {
    case "advice":
      return "Label marks.";
    case "reason":
      return "Less lookup.";
    case "context":
      return "Few series.";
    case "exceptions":
      return "Crowded marks.";
    case "costs":
      return "Uses space.";
    case "mistakes":
      return "Avoid clutter.";
    case "check":
      return "Clear values?";
    case "fix":
      return "Move labels.";
  }
}
