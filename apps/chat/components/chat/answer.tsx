import { ChevronRight } from "lucide-react";
import * as Match from "effect/Match";
import { ThreadPrimitive } from "@assistant-ui/react";
import { Recommendation } from "./recommendation";
import { type Answer as AnswerData } from "../../shared/answer";
import type { GuidelinePreview, ReadGuideline } from "../../chat/tool-output";
import * as stylex from "@stylexjs/stylex";
import { colors, media, motion, disclosureScope } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

const DETAILS_ANIMATION =
  "@supports (interpolate-size: allow-keywords) and selector(::details-content)";

const styles = stylex.create({
  points: {
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
});

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
  points,
  workflow,
  streaming,
  guidelines,
}: {
  points: AnswerData["points"];
  workflow: AnswerData["workflow"];
  streaming: boolean;
  guidelines: ReadonlyMap<string, ReadGuideline>;
}) {
  const contextLabel = Match.value(workflow).pipe(
    Match.when("visfeedback", () => "In your chart"),
    Match.when("visrec", () => "Your brief"),
    Match.when("discuss", () => "Your question"),
    Match.exhaustive,
  );

  return (
    <ol {...stylex.props(styles.points)} aria-label="Guideline-backed advice" aria-busy={streaming}>
      {points.map((item) => {
        const primary = guidelines.get(item.primary_guideline_id)!;

        return (
          <li key={item.primary_guideline_id} {...stylex.props(styles.finding, ui.appear)}>
            {item.assessment ? (
              <h3 {...stylex.props(styles.assessment, styles[item.assessment])}>
                {assessments[item.assessment]}
              </h3>
            ) : null}
            <div {...stylex.props(styles.action)}>
              <Recommendation content={item.recommendation} streaming={streaming} />
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
                <dt {...stylex.props(styles.term)}>{contextLabel}</dt>
                <dd {...stylex.props(styles.description)}>{item.context}</dd>
                <dt {...stylex.props(styles.term)}>Guideline guidance</dt>
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

export function Answer({
  answer,
  guidelines,
  streaming = false,
}: {
  answer: AnswerData | undefined;
  guidelines: ReadonlyMap<string, ReadGuideline>;
  streaming?: boolean;
}) {
  if (!answer)
    return (
      <div {...stylex.props(styles.notice)}>
        <p>The answer needs another evidence check.</p>
        <ThreadPrimitive.Suggestion
          prompt="Please finish the answer, reading any missing guideline evidence and correcting the reported validation issues before presenting it."
          send
          {...stylex.props(ui.button, ui.quietButton, ui.focus)}
        >
          Try again
        </ThreadPrimitive.Suggestion>
      </div>
    );

  if (answer.status === "needs_context")
    return <p {...stylex.props(styles.notice)}>{answer.question}</p>;

  if (answer.status === "no_match")
    return (
      <p {...stylex.props(styles.notice)}>
        I could not find an applicable guideline for this request. Share more chart context or ask
        about a specific design choice.
      </p>
    );

  if (answer.status === "out_of_scope")
    return (
      <p {...stylex.props(styles.notice)}>
        I can review a chart, recommend a design, or discuss visualization choices using the
        Guideline Catalog.
      </p>
    );

  return (
    <Findings
      points={answer.points}
      workflow={answer.workflow}
      guidelines={guidelines}
      streaming={streaming}
    />
  );
}
