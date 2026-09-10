import * as stylex from "@stylexjs/stylex";
import { colors, media } from "./tokens.stylex";

const spread = stylex.keyframes({
  "0%, 8%, 95%, 100%": { transform: "rotate(0deg)" },
  "24%, 84%": { transform: "rotate(var(--tile-spread))" },
});

const orbit = stylex.keyframes({
  "0%, 23%": { transform: "rotate(0deg)" },
  "69%, 100%": { transform: "rotate(360deg)" },
});

const angles = [140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 0, 20, 40];

const styles = stylex.create({
  root: {
    display: "inline-block",
    width: 24,
    height: 24,
    flexShrink: 0,
  },
  motion: {
    transformOrigin: "50px 50px",
    animationDuration: "5.6s",
    animationTimingFunction: "cubic-bezier(0.65, 0, 0.35, 1)",
    animationIterationCount: "infinite",
  },
  spread: (index: number) => ({
    "--tile-spread": `${(index - 6.5) * (360 / 14 - 20)}deg`,
    animationName: { default: spread, [media.reducedMotion]: "none" },
  }),
  orbit: (index: number) => ({
    animationName: { default: orbit, [media.reducedMotion]: "none" },
    animationDelay: `${index * 0.056}s`,
  }),
  tile: { fill: colors.foreground },
  accent: { fill: colors.accent },
});

export function LoadingMark() {
  return (
    <svg {...stylex.props(styles.root)} viewBox="0 0 100 100" aria-hidden="true" focusable="false">
      {angles.map((angle, index) => (
        <g key={angle} transform={`rotate(${angle} 50 50)`}>
          <g {...stylex.props(styles.motion, styles.spread(index))}>
            <g {...stylex.props(styles.motion, styles.orbit(index))}>
              <rect
                {...stylex.props(styles.tile, angle <= 40 && styles.accent)}
                x="47.9"
                y="5"
                width="4.2"
                height="13"
                rx="2.1"
              />
            </g>
          </g>
        </g>
      ))}
    </svg>
  );
}
