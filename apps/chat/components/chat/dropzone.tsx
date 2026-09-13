import { ImagePlus } from "lucide-react";
import type { ReactNode } from "react";
import { useFileDrop } from "../../chat/use-file-drop";
import * as stylex from "@stylexjs/stylex";
import { colors } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

const styles = stylex.create({
  shell: { height: "100dvh", minHeight: 320, display: "flex", flexDirection: "column" },
  overlay: {
    position: "fixed",
    inset: 12,
    zIndex: 20,
    pointerEvents: "none",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    gap: 12,
    padding: 24,
    borderWidth: 2,
    borderStyle: "dashed",
    borderColor: colors.accent,
    borderRadius: 8,
    backgroundColor: `color-mix(in srgb, ${colors.background} 96%, transparent)`,
    textAlign: "center",
  },
  icon: { color: colors.accent },
  description: {
    margin: 0,
    maxWidth: 400,
    color: colors.muted,
    fontSize: 14,
    lineHeight: 1.5,
    textWrap: "balance",
  },
  title: { color: colors.foreground, fontSize: 24, fontWeight: 500, letterSpacing: "-0.025em" },
});

export function Dropzone({
  children,
  disabled,
  hasAttachment,
  onFiles,
}: {
  children: ReactNode;
  disabled: boolean;
  hasAttachment: boolean;
  onFiles: (files: File[]) => void;
}) {
  const active = useFileDrop(disabled, onFiles);

  return (
    <div {...stylex.props(styles.shell)}>
      {children}
      {active ? (
        <div {...stylex.props(styles.overlay)} role="status">
          <ImagePlus {...stylex.props(ui.icon, styles.icon)} size={32} aria-hidden="true" />
          <p {...stylex.props(styles.description, styles.title)}>
            {disabled
              ? "Chart upload is busy"
              : hasAttachment
                ? "Drop to replace your chart"
                : "Drop your chart anywhere"}
          </p>
          <p {...stylex.props(styles.description)}>
            {disabled
              ? "Wait for the current task to finish, then drop your chart again."
              : "One PNG, JPEG, or WebP image · Up to 3 MiB"}
          </p>
        </div>
      ) : null}
    </div>
  );
}
