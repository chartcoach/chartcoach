import { SuggestionPrimitive, ThreadPrimitive } from "@assistant-ui/react";
import * as stylex from "@stylexjs/stylex";
import { starters } from "../../shared/starters";
import { colors, media, motion } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

export function Starters({
  disabled,
  pending,
  onExample,
}: {
  disabled: boolean;
  /** The example image being prepared for sending. */
  pending?: string;
  onExample: (image: string, prompt: string) => Promise<void>;
}) {
  return (
    <section aria-label="Try an example" {...stylex.props(styles.root)}>
      <p {...stylex.props(styles.heading)}>Try an example</p>
      <div {...stylex.props(styles.list)}>
        <ThreadPrimitive.Suggestions>
          {({ suggestion }) => {
            const starter = starters.find((item) => item.prompt === suggestion.prompt);

            return starter ? (
              <Starter
                starter={starter}
                disabled={disabled}
                pending={starter.image === pending}
                onExample={onExample}
              />
            ) : null;
          }}
        </ThreadPrimitive.Suggestions>
      </div>
    </section>
  );
}

function Starter({
  starter,
  disabled,
  pending,
  onExample,
}: {
  starter: (typeof starters)[number];
  disabled: boolean;
  pending: boolean;
  onExample: (image: string, prompt: string) => Promise<void>;
}) {
  return (
    <SuggestionPrimitive.Trigger
      {...stylex.props(ui.focus, styles.card, pending && styles.pending)}
      disabled={disabled}
      aria-busy={pending}
      onClick={(event) => {
        event.preventDefault();
        void onExample(starter.image, starter.prompt);
      }}
    >
      <img src={starter.image} alt="" width={960} height={560} {...stylex.props(styles.image)} />
      <span {...stylex.props(styles.text)}>
        <SuggestionPrimitive.Title {...stylex.props(styles.title)} />
        <span {...stylex.props(styles.description)}>{starter.description}</span>
      </span>
    </SuggestionPrimitive.Trigger>
  );
}

const styles = stylex.create({
  root: { marginTop: { default: 40, [media.mobile]: 32 } },
  heading: { marginTop: 0, marginBottom: 12, color: colors.muted, fontSize: 12 },
  list: {
    display: "grid",
    gridTemplateColumns: {
      default: "repeat(3, minmax(0, 1fr))",
      [media.mobile]: "minmax(0, 1fr)",
    },
    gap: 12,
    padding: 2,
  },
  card: {
    display: "flex",
    flexDirection: { default: "column", [media.mobile]: "row" },
    alignItems: { default: "stretch", [media.mobile]: "center" },
    padding: 0,
    textAlign: "left",
    minWidth: 0,
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: {
      default: colors.border,
      ":hover:enabled": { default: null, [media.hover]: colors.muted },
    },
    borderRadius: 10,
    backgroundColor: {
      default: colors.background,
      ":hover:enabled": { default: null, [media.hover]: colors.navigation },
    },
    cursor: { default: "pointer", ":disabled": "default" },
    touchAction: "manipulation",
    userSelect: "none",
    WebkitTapHighlightColor: "transparent",
    transform: { default: "scale(1)", ":active:enabled": "scale(0.98)" },
    transitionProperty: "transform, background-color, border-color",
    transitionDuration: { default: motion.control, [media.reducedMotion]: "0ms" },
    transitionTimingFunction: `${motion.easeOut}, ease, ease`,
    overflow: "hidden",
    color: colors.foreground,
  },
  pending: { transform: "scale(0.98)", borderColor: colors.muted },
  image: {
    display: "block",
    width: { default: "100%", [media.mobile]: 88 },
    height: { default: "auto", [media.mobile]: 68 },
    flexShrink: 0,
    aspectRatio: "12 / 7",
    objectFit: "contain",
    backgroundColor: "#fafafa",
  },
  text: { display: "grid", gap: 4, padding: 12, minWidth: 0 },
  title: { fontSize: 14, fontWeight: 500, lineHeight: 1.4 },
  description: { fontSize: 12, color: colors.muted, lineHeight: 1.5 },
});
