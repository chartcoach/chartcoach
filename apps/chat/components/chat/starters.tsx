import { SuggestionPrimitive, ThreadPrimitive, useAui } from "@assistant-ui/react";
import * as stylex from "@stylexjs/stylex";
import { starters } from "../../shared/starters";
import { colors, media } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

export function Starters({
  disabled,
  onImage,
}: {
  disabled: boolean;
  onImage: (path: string) => Promise<boolean>;
}) {
  return (
    <section aria-label="Try an example" {...stylex.props(styles.root)}>
      <p {...stylex.props(styles.heading)}>Try an example</p>
      <div {...stylex.props(styles.list)}>
        <ThreadPrimitive.Suggestions>
          {({ suggestion }) => {
            const starter = starters.find((item) => item.prompt === suggestion.prompt);

            return starter ? (
              <Starter starter={starter} disabled={disabled} onImage={onImage} />
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
  onImage,
}: {
  starter: (typeof starters)[number];
  disabled: boolean;
  onImage: (path: string) => Promise<boolean>;
}) {
  const aui = useAui();

  return (
    <SuggestionPrimitive.Trigger
      {...stylex.props(ui.focus, styles.card)}
      disabled={disabled}
      onClick={async (event) => {
        event.preventDefault();
        const prompt = aui.suggestion().getState().prompt;

        if (await onImage(starter.image)) {
          aui.composer().setText(prompt);
        }
      }}
    >
      <img src={starter.image} alt="" width={960} height={560} {...stylex.props(styles.image)} />
      <span {...stylex.props(styles.text)}>
        <SuggestionPrimitive.Title {...stylex.props(styles.title)} />
      </span>
    </SuggestionPrimitive.Trigger>
  );
}

const styles = stylex.create({
  root: { marginTop: 28 },
  heading: { marginTop: 0, marginBottom: 12, color: colors.muted, fontSize: 12 },
  list: {
    display: "grid",
    gridTemplateColumns: {
      default: "repeat(3, minmax(0, 1fr))",
      [media.mobile]: "repeat(3, 174px)",
    },
    gap: 12,
    overflowX: "auto",
    padding: 2,
    scrollbarWidth: "thin",
    scrollbarColor: `${colors.scrollThumb} transparent`,
  },
  card: {
    display: "flex",
    flexDirection: "column",
    padding: 0,
    textAlign: "left",
    minWidth: 0,
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: { default: colors.border, ":hover:enabled": colors.muted },
    borderRadius: 12,
    backgroundColor: { default: colors.background, ":hover:enabled": colors.navigation },
    cursor: "pointer",
    overflow: "hidden",
    opacity: { default: 1, ":disabled": 0.5 },
    color: colors.foreground,
  },
  image: {
    display: "block",
    width: "100%",
    height: "auto",
    aspectRatio: "12 / 7",
    objectFit: "contain",
    backgroundColor: "#fafafa",
  },
  text: { padding: 12 },
  title: { fontSize: 12, fontWeight: 500, lineHeight: 1.4 },
});
