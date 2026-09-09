import * as stylex from "@stylexjs/stylex";
import { colors, media } from "./tokens.stylex";

const flutter = stylex.keyframes({
  "0%": { transform: "rotate(0deg) scale(1)" },
  "12%": { transform: "rotate(90deg) scale(0.72)" },
  "24%, 100%": { transform: "rotate(180deg) scale(1)" },
});

const angles = [140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 0, 20, 40];

const styles = stylex.create({
  root: {
    display: "inline-block",
    width: 24,
    height: 24,
    flexShrink: 0,
  },
  tile: (index: number) => ({
    fill: colors.foreground,
    transformBox: "fill-box",
    transformOrigin: "center",
    animationName: { default: flutter, [media.reducedMotion]: "none" },
    animationDuration: "2.6s",
    animationTimingFunction: "cubic-bezier(0.65, 0, 0.35, 1)",
    animationIterationCount: "infinite",
    animationDelay: `${index * 0.11}s`,
  }),
  accent: { fill: colors.accent },
});

export function LoadingMark() {
  return (
    <svg {...stylex.props(styles.root)} viewBox="0 0 100 100" aria-hidden="true" focusable="false">
      {angles.map((angle, index) => (
        <g key={angle} transform={`rotate(${angle} 50 50)`}>
          <rect
            {...stylex.props(styles.tile(index), angle <= 40 && styles.accent)}
            x="47.9"
            y="5"
            width="4.2"
            height="13"
            rx="2.1"
          />
        </g>
      ))}
    </svg>
  );
}
