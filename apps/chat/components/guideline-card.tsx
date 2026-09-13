import { localGuidelineURL } from "../shared/guideline-page";
import { ArrowUpRight } from "lucide-react";
import type { GuidelinePreview } from "../chat/tool-output";
import * as stylex from "@stylexjs/stylex";
import { colors } from "./ui/tokens.stylex";
import { ui } from "./ui/ui";

const styles = stylex.create({
  card: {
    display: "grid",
    gridTemplateColumns: "minmax(0, 1fr)",
    color: "inherit",
    textDecoration: "none",
    borderWidth: 1,
    borderStyle: "solid",
    borderColor: {
      default: colors.border,
      ":hover": { default: null, "@media (hover: hover)": colors.accent },
    },
    borderRadius: 10,
    overflow: "hidden",
    backgroundColor: colors.surface,
    WebkitTapHighlightColor: "transparent",
  },
  preview: {
    position: "relative",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    alignSelf: "start",
    aspectRatio: "1200 / 630",
    backgroundColor: colors.background,
    color: colors.muted,
  },
  fallback: {
    position: "absolute",
    inset: 0,
    overflow: "hidden",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    gap: 12,
    padding: 24,
    textAlign: "center",
    fontSize: 18,
    lineHeight: 1.4,
    color: colors.foreground,
  },
  image: {
    position: "relative",
    display: "block",
    width: "100%",
    height: "auto",
    backgroundColor: colors.background,
  },
  footer: {
    display: "flex",
    alignItems: "center",
    gap: 10,
    paddingBlock: 10,
    paddingInline: 14,
    lineHeight: 1.45,
    fontSize: 12,
    color: colors.muted,
  },
  arrow: { marginLeft: "auto", color: colors.accentText },
});

export function GuidelineCard({ guideline }: { guideline: GuidelinePreview }) {
  return (
    <a
      {...stylex.props(ui.focus, styles.card)}
      href={localGuidelineURL(guideline.id)}
      target="_blank"
      rel="noopener noreferrer"
      aria-label={guideline.title}
    >
      <span {...stylex.props(styles.preview)} aria-hidden="true">
        <span {...stylex.props(styles.fallback)}>
          <span>{guideline.title}</span>
        </span>
        <img
          key={guideline.id}
          {...stylex.props(styles.image)}
          src={`https://chartcoach.dev/guidelines/${encodeURIComponent(guideline.id)}/og.png`}
          alt=""
          width={1200}
          height={630}
          loading="lazy"
          decoding="async"
          referrerPolicy="no-referrer"
          onError={(event) => {
            event.currentTarget.style.display = "none";
          }}
        />
      </span>
      <span {...stylex.props(styles.footer)}>
        <span>Read guideline</span>
        <ArrowUpRight {...stylex.props(ui.icon, styles.arrow)} size={16} aria-hidden="true" />
      </span>
    </a>
  );
}
