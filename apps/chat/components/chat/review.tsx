import { ChevronRight } from "lucide-react";
import { type Components, Streamdown } from "streamdown";
import { type Review as ReviewData } from "../../shared/review";
import type { GuidelinePreview, ReadGuideline } from "../../chat/tool-output";
import * as stylex from "@stylexjs/stylex";
import { colors, media, motion, disclosureScope } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

const DETAILS_ANIMATION =
  "@supports (interpolate-size: allow-keywords) and selector(::details-content)";
const styles = stylex.create({
  feedback: {
    listStyle: "none",
    padding: 0,
    marginTop: 20,
    marginBottom: 0,
    marginInline: 0,
    display: "grid",
    gap: 24,
  },
  finding: {
    paddingTop: { default: 0, ":not(:first-child)": 24 },
    borderTopWidth: { default: 0, ":not(:first-child)": 1 },
    borderTopStyle: "solid",
    borderTopColor: colors.border,
  },
  assessment: {
    display: "flex",
    alignItems: "center",
    gap: 7,
    fontSize: 13,
    fontWeight: 600,
    marginTop: 0,
    marginBottom: 8,
    marginInline: 0,
  },
  respected: { color: colors.positive },
  violated: { color: colors.accentText },
  uncertain: { color: colors.caution },
  action: { fontSize: 17, lineHeight: 1.65 },
  citations: { display: "flex", flexWrap: "wrap", rowGap: 0, columnGap: 18, marginTop: 8 },
  citation: {
    display: "inline-flex",
    alignItems: "center",
    gap: 6,
    minHeight: 44,
    fontSize: 13,
    color: { default: colors.muted, ":hover": colors.foreground },
    textDecorationLine: "underline",
    textDecorationColor: { default: colors.border, ":hover": "currentColor" },
    textUnderlineOffset: 3,
    WebkitTapHighlightColor: "transparent",
  },
  reason: {
    fontSize: 14,
    "::details-content": {
      interpolateSize: { default: null, [DETAILS_ANIMATION]: "allow-keywords" },
      blockSize: { default: null, [DETAILS_ANIMATION]: { default: 0, ":is([open])": "auto" } },
      opacity: { default: null, [DETAILS_ANIMATION]: { default: 0, ":is([open])": 1 } },
      overflow: { default: null, [DETAILS_ANIMATION]: "clip" },
      transitionProperty: {
        default: null,
        [DETAILS_ANIMATION]: "height, opacity, content-visibility",
      },
      transitionDuration: {
        default: null,
        [DETAILS_ANIMATION]: {
          default: motion.disclosure,
          [media.reducedMotion]: "0ms",
          ":has(> summary:focus-visible)": "0ms",
        },
      },
      transitionTimingFunction: {
        default: null,
        [DETAILS_ANIMATION]: `${motion.easeOut}, ${motion.easeOut}, ease`,
      },
      transitionBehavior: { default: null, [DETAILS_ANIMATION]: "normal, normal, allow-discrete" },
    },
  },
  summary: {
    display: "flex",
    alignItems: "center",
    gap: 8,
    width: "fit-content",
    minHeight: 44,
    color: colors.muted,
    fontSize: 13,
    cursor: "pointer",
    listStyle: "none",
    "::-webkit-details-marker": { display: "none" },
  },
  reasonChevron: {
    transform: {
      default: "none",
      [stylex.when.ancestor("[open]", disclosureScope)]: "rotate(90deg)",
    },
  },
  detail: {
    marginTop: 8,
    marginBottom: 0,
    marginInline: 0,
    paddingTop: 14,
    paddingInline: 16,
    paddingBottom: 2,
    borderRadius: 6,
    backgroundColor: colors.surface,
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: colors.border,
  },
  term: {
    fontSize: 12,
    fontWeight: 500,
    color: { default: colors.muted, ":last-of-type": colors.foreground },
    marginBottom: 4,
  },
  description: {
    marginTop: 0,
    marginBottom: 14,
    marginInline: 0,
    whiteSpace: "pre-wrap",
    color: colors.muted,
  },
  notice: { marginTop: 20, marginBottom: 0, marginInline: 0 },
  markdown: { whiteSpace: "normal" },
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
const assessments = {
  respected: "Working well",
  violated: "Improve",
  uncertain: "Check",
};

function Citation({
  guideline,
  supporting = false,
}: {
  guideline: GuidelinePreview;
  supporting?: boolean;
}) {
  return (
    <a
      {...stylex.props(ui.focus, styles.citation)}
      href={guideline.url}
      target="_blank"
      rel="noopener noreferrer"
      aria-label={`${supporting ? "Supporting" : "Primary"}: ${guideline.title}`}
    >
      {guideline.title}
    </a>
  );
}

function Findings({
  feedback,
  guidelines,
}: {
  feedback: ReviewData["feedback"];
  guidelines: ReadonlyMap<string, ReadGuideline>;
}) {
  return (
    <ol {...stylex.props(styles.feedback)} aria-label="Guideline-backed feedback">
      {feedback.map((item) => {
        const primary = guidelines.get(item.primary_guideline_id)!;
        return (
          <li {...stylex.props(styles.finding)} key={item.primary_guideline_id}>
            <h3 {...stylex.props(styles.assessment, styles[item.assessment])}>
              {assessments[item.assessment]}
            </h3>
            <div {...stylex.props(styles.action)}>
              <Streamdown
                {...stylex.props(styles.markdown)}
                mode="static"
                allowedElements={recommendationElements}
                components={recommendationComponents}
                skipHtml
                controls={false}
                linkSafety={{ enabled: false }}
              >
                {item.recommendation}
              </Streamdown>
            </div>
            <div {...stylex.props(styles.citations)}>
              <Citation guideline={primary} />
            </div>
            <details {...stylex.props(disclosureScope, styles.reason)}>
              <summary {...stylex.props(ui.focus, styles.summary)}>
                Why this applies
                <ChevronRight
                  {...stylex.props(ui.chevron, styles.reasonChevron)}
                  size={14}
                  aria-hidden="true"
                />
              </summary>
              <dl {...stylex.props(styles.detail)}>
                <dt {...stylex.props(styles.term)}>In your chart</dt>
                <dd {...stylex.props(styles.description)}>{item.observation}</dd>
                <dt {...stylex.props(styles.term)}>Guideline requires</dt>
                <dd {...stylex.props(styles.description)}>{primary.description}</dd>
              </dl>
              {item.supporting_guideline_ids.length ? (
                <div {...stylex.props(styles.citations)}>
                  {item.supporting_guideline_ids.map((id) => (
                    <Citation key={id} guideline={guidelines.get(id)!} supporting />
                  ))}
                </div>
              ) : null}
            </details>
          </li>
        );
      })}
    </ol>
  );
}

export function Review({
  review,
  guidelines,
}: {
  review: ReviewData | undefined;
  guidelines: ReadonlyMap<string, ReadGuideline>;
}) {
  if (!review)
    return (
      <p {...stylex.props(styles.notice)}>
        The review could not be verified against the guidelines read. Please try again.
      </p>
    );
  if (review.status === "needs_context")
    return <p {...stylex.props(styles.notice)}>{review.question}</p>;
  if (review.status === "no_match")
    return (
      <p {...stylex.props(styles.notice)}>
        I could not find an applicable guideline for this request. Share more chart context or ask
        about a specific design choice.
      </p>
    );
  if (review.status === "out_of_scope")
    return (
      <p {...stylex.props(styles.notice)}>
        I can review chart design using the Guideline Catalog. Share a chart or a visualization
        question.
      </p>
    );
  return <Findings feedback={review.feedback} guidelines={guidelines} />;
}
