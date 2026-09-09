import { ImagePlus } from "lucide-react";
import { type ReactNode, useEffect, useEffectEvent, useState } from "react";
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
  const [active, setActive] = useState(false);
  const dragOver = useEffectEvent((event: DragEvent) => {
    if (!event.dataTransfer?.types.includes("Files")) return;
    event.preventDefault();
    event.dataTransfer.dropEffect = disabled ? "none" : "copy";
  });
  const drop = useEffectEvent((event: DragEvent) => {
    if (!event.dataTransfer?.types.includes("Files")) return;
    event.preventDefault();
    onFiles(Array.from(event.dataTransfer.files));
  });

  useEffect(() => {
    const targets = new Set<EventTarget>();
    function reset() {
      targets.clear();
      setActive(false);
    }
    function enter(event: DragEvent) {
      if (!event.dataTransfer?.types.includes("Files") || !event.target) return;
      targets.add(event.target);
      setActive(true);
    }
    function leave(event: DragEvent) {
      if (event.target) targets.delete(event.target);
      if (targets.size === 0) reset();
    }
    function finish(event: DragEvent) {
      reset();
      drop(event);
    }
    function keyDown(event: KeyboardEvent) {
      if (event.key === "Escape") reset();
    }
    window.addEventListener("dragenter", enter);
    window.addEventListener("dragleave", leave);
    window.addEventListener("dragover", dragOver);
    window.addEventListener("drop", finish);
    window.addEventListener("dragend", reset);
    window.addEventListener("blur", reset);
    window.addEventListener("keydown", keyDown);
    return () => {
      window.removeEventListener("dragenter", enter);
      window.removeEventListener("dragleave", leave);
      window.removeEventListener("dragover", dragOver);
      window.removeEventListener("drop", finish);
      window.removeEventListener("dragend", reset);
      window.removeEventListener("blur", reset);
      window.removeEventListener("keydown", keyDown);
    };
  }, []);

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
