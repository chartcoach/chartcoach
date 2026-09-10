import { ArrowUpRight } from "lucide-react";
import Image from "next/image";
import { useState } from "react";
import type { GuidelinePreview } from "../../chat/tool-output";
import * as stylex from "@stylexjs/stylex";
import { colors, media } from "../ui/tokens.stylex";
import { ui } from "../ui/ui";

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
    borderRadius: 6,
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
  image: { width: "100%", height: "100%", objectFit: "contain", display: "block" },
  fallback: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    gap: 12,
    padding: 24,
    textAlign: "center",
    fontSize: 18,
    lineHeight: 1.4,
    color: colors.foreground,
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
  compactFooter: { display: { default: "none", [media.desktop]: "flex" } },
  arrow: { marginLeft: "auto", color: colors.accentText },
});

export function GuidelineCard({
  guideline,
  compact = false,
}: {
  guideline: GuidelinePreview;
  compact?: boolean;
}) {
  const [imageFailed, setImageFailed] = useState(false);
  return (
    <a
      {...stylex.props(ui.focus, styles.card)}
      href={guideline.url}
      target="_blank"
      rel="noopener noreferrer"
      aria-label={guideline.title}
    >
      <span {...stylex.props(styles.preview)} aria-hidden="true">
        {imageFailed ? (
          <span {...stylex.props(styles.fallback)}>
            <span>{guideline.title}</span>
          </span>
        ) : (
          <Image
            {...stylex.props(styles.image)}
            src={`${guideline.url}/og.png`}
            alt=""
            fill
            sizes="(max-width: 720px) 92vw, 440px"
            quality={90}
            onError={() => setImageFailed(true)}
          />
        )}
      </span>
      <span {...stylex.props(styles.footer, compact && styles.compactFooter)}>
        <span>Read guideline</span>
        <ArrowUpRight {...stylex.props(ui.icon, styles.arrow)} size={16} aria-hidden="true" />
      </span>
    </a>
  );
}
