import * as stylex from "@stylexjs/stylex";
import { Streamdown, type Components } from "streamdown";
import { colors } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

const styles = stylex.create({
  markdown: { whiteSpace: "normal", display: "grid", rowGap: 12 },
  paragraph: {
    margin: 0,
    display: { default: "block", [stylex.when.ancestor(":is(li)")]: "inline" },
  },
  strong: { fontWeight: 600 },
  emphasis: { fontStyle: "italic" },
  code: {
    borderRadius: 4,
    backgroundColor: colors.background,
    paddingInline: 6,
    paddingBlock: 2,
    fontSize: 14,
    lineHeight: "20px",
  },
  list: {
    listStylePosition: "inside",
    whiteSpace: "normal",
    padding: 0,
    paddingLeft: { default: 0, [stylex.when.ancestor(":is(li)")]: 24 },
    marginTop: 0,
    marginBottom: {
      default: 0,
      ":not(:last-child)": { default: 16, [stylex.when.ancestor(":is(li)")]: 0 },
    },
    marginInline: 0,
  },
  unordered: { listStyleType: "disc" },
  ordered: { listStyleType: "decimal" },
  listItem: { paddingBlock: 4 },
  inline: { display: "inline" },
});

const recommendationElements = ["p", "strong", "em", "code", "ul", "ol", "li", "br", "a"];

const recommendationComponents = {
  p: ({ children }) => <p {...stylex.props(styles.paragraph)}>{children}</p>,
  strong: ({ children }) => <strong {...stylex.props(styles.strong)}>{children}</strong>,
  em: ({ children }) => <em {...stylex.props(styles.emphasis)}>{children}</em>,
  code: ({ children }) => <code {...stylex.props(ui.mono, styles.code)}>{children}</code>,
  ul: ({ children }) => <ul {...stylex.props(styles.list, styles.unordered)}>{children}</ul>,
  ol: ({ children, start }) => (
    <ol {...stylex.props(styles.list, styles.ordered)} start={start}>
      {children}
    </ol>
  ),
  li: ({ children }) => (
    <li {...stylex.props(stylex.defaultMarker(), styles.listItem)}>{children}</li>
  ),
  br: () => <br />,
  a: ({ children }) => <span {...stylex.props(styles.inline)}>{children}</span>,
} satisfies Components;

const linkSafety = { enabled: false };

const remend = { linkMode: "text-only" as const };

export function Recommendation({ content, streaming }: { content: string; streaming: boolean }) {
  return (
    <Streamdown
      {...stylex.props(styles.markdown)}
      mode={streaming ? "streaming" : "static"}
      isAnimating={streaming}
      allowedElements={recommendationElements}
      components={recommendationComponents}
      skipHtml
      controls={false}
      linkSafety={linkSafety}
      remend={remend}
    >
      {content}
    </Streamdown>
  );
}
