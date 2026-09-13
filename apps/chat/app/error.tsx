"use client";

import * as stylex from "@stylexjs/stylex";
import { ui } from "../components/ui/ui";

const styles = stylex.create({
  root: {
    minHeight: "100dvh",
    display: "grid",
    placeContent: "center",
    justifyItems: "start",
    gap: 16,
    padding: 32,
  },
  title: { fontSize: 24, fontWeight: 550, letterSpacing: "-0.025em" },
  description: { maxWidth: 440, lineHeight: 1.6 },
});

export default function ChatError({ reset }: { reset: () => void }) {
  return (
    <main {...stylex.props(styles.root)}>
      <h1 {...stylex.props(styles.title)}>The chat couldn't load</h1>
      <p {...stylex.props(styles.description)}>
        Try opening it again. Your saved conversations and model connections stay available.
      </p>
      <button
        type="button"
        {...stylex.props(ui.button, ui.outlineButton, ui.focus)}
        onClick={reset}
      >
        Try again
      </button>
    </main>
  );
}
