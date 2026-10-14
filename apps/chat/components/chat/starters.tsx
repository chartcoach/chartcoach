import { SuggestionPrimitive, ThreadPrimitive } from "@assistant-ui/react";
import * as stylex from "@stylexjs/stylex";
import { ChartColumn, ChartLine, Table, type LucideIcon } from "lucide-react";
import type { Ref } from "react";
import { starters } from "../../shared/starters";
import { colors, media, motion } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

const icons = {
  "/examples/bicycle-trips.png": ChartColumn,
  "/examples/support-requests.png": ChartLine,
  "/examples/visits-brief.png": Table,
} satisfies Record<(typeof starters)[number]["image"], LucideIcon>;

export function Starters({
  ref,
  disabled,
  pending,
  onExample,
}: {
  ref?: Ref<HTMLElement>;
  disabled: boolean;
  /** The example image being prepared for sending. */
  pending?: string;
  onExample: (image: string, prompt: string) => Promise<void>;
}) {
  return (
    <section ref={ref} aria-label="Try an example" {...stylex.props(styles.root)}>
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
  const Icon = icons[starter.image];

  return (
    <SuggestionPrimitive.Trigger
      {...stylex.props(ui.focus, styles.chip, pending && styles.pending)}
      disabled={disabled}
      aria-busy={pending}
      title={starter.description}
      onClick={(event) => {
        event.preventDefault();
        void onExample(starter.image, starter.prompt);
      }}
    >
      <Icon {...stylex.props(styles.icon)} size={16} aria-hidden="true" />
      <SuggestionPrimitive.Title />
    </SuggestionPrimitive.Trigger>
  );
}

const styles = stylex.create({
  root: {
    display: "flex",
    flexWrap: { default: "wrap", [media.compact]: "nowrap" },
    justifyContent: "safe center",
    gap: 8,
    width: "min(100%, 720px)",
    marginInline: "auto",
    paddingTop: { default: 16, [media.compact]: 0 },
    paddingBottom: { default: 0, [media.compact]: 4 },
    paddingInline: { default: 24, [media.mobile]: 12 },
    overflowX: { default: "visible", [media.compact]: "auto" },
    scrollbarWidth: "none",
    flexShrink: 0,
  },
  chip: {
    display: "inline-flex",
    alignItems: "center",
    gap: 8,
    flexShrink: 0,
    minHeight: 36,
    paddingBlock: 0,
    paddingInline: 12,
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: colors.border,
    borderRadius: 10,
    backgroundColor: {
      default: "transparent",
      ":hover:enabled": { default: null, [media.hover]: colors.surface },
    },
    color: {
      default: colors.muted,
      ":hover:enabled": { default: null, [media.hover]: colors.foreground },
    },
    fontSize: 14,
    whiteSpace: "nowrap",
    cursor: { default: "pointer", ":disabled": "default" },
    touchAction: "manipulation",
    userSelect: "none",
    WebkitTapHighlightColor: "transparent",
    transform: { default: "scale(1)", ":active:enabled": "scale(0.97)" },
    transitionProperty: "transform, background-color, color",
    transitionDuration: { default: motion.control, [media.reducedMotion]: "0ms" },
    transitionTimingFunction: `${motion.easeOut}, ease, ease`,
  },
  pending: { transform: "scale(0.97)", color: colors.foreground },
  icon: { flexShrink: 0 },
});
