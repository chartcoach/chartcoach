import * as React from "react";

import { ChartCoachMarimekkoMark } from "./chartcoach-marimekko-mark";
import type { ChartCoachMarkMode, ChartCoachTheme } from "../lib/chartcoach-marimekko";

type ChartCoachMarimekkoCanvasProps = {
  className?: string;
  style?: React.CSSProperties;
  theme?: ChartCoachTheme;
  mode?: Extract<ChartCoachMarkMode, "static" | "hero-loop">;
  title?: string;
  idPrefix?: string;
};

function ChartCoachMarimekkoCanvas({
  className,
  style,
  theme = "auto",
  mode = "hero-loop",
  title = "Structured visualization design knowledge",
  idPrefix = "cc-marimekko-canvas",
}: ChartCoachMarimekkoCanvasProps) {
  return (
    <div
      aria-hidden={title ? undefined : true}
      className={className}
      style={{
        position: "relative",
        display: "grid",
        placeItems: "center",
        width: "100%",
        aspectRatio: "1.24 / 1",
        overflow: "hidden",
        padding: "clamp(0.85rem, 2.4vw, 1.35rem)",
        borderRadius: "var(--cc-radius-panel, 1rem)",
        background:
          "var(--cc-marimekko-canvas-bg, linear-gradient(180deg, var(--cc-shell-surface), var(--ccui-panel)))",
        boxShadow: "none",
        ...style,
      }}
    >
      <div
        aria-hidden="true"
        style={{
          position: "absolute",
          inset: 0,
          zIndex: 0,
          opacity: 0.18,
          backgroundImage:
            "linear-gradient(to right, transparent, color-mix(in srgb, var(--cc-brand) 12%, transparent) 50%, transparent), repeating-linear-gradient(to right, transparent 0 4.8rem, color-mix(in srgb, var(--cc-mark-faint) 70%, transparent) 4.8rem 4.86rem), repeating-linear-gradient(to bottom, transparent 0 4.8rem, color-mix(in srgb, var(--cc-mark-faint) 70%, transparent) 4.8rem 4.86rem)",
          pointerEvents: "none",
        }}
      />
      <div
        style={{
          position: "relative",
          zIndex: 1,
          width: "100%",
          display: "grid",
          placeItems: "center",
        }}
      >
        <ChartCoachMarimekkoMark
          idPrefix={idPrefix}
          mode={mode}
          theme={theme}
          title={title}
          style={{ width: "min(74%, 28rem)", maxWidth: "100%" }}
        />
      </div>
    </div>
  );
}

export { ChartCoachMarimekkoCanvas };
export type { ChartCoachMarimekkoCanvasProps };
