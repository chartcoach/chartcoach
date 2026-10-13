import Image from "next/image";
import Link from "next/link";
import { ArrowRight, BookOpen } from "lucide-react";
import * as stylex from "@stylexjs/stylex";
import logo from "@chartcoach/brand/assets/brand/chartcoach-horizontal.svg";
import logoWhite from "@chartcoach/brand/assets/brand/chartcoach-horizontal-white.svg";
import { colors, media } from "./ui/tokens.stylex";
import { ui } from "./ui/ui";

const digits = [
  ["10010", "10010", "10010", "11111", "00010", "00010", "00010"],
  ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
  ["10010", "10010", "10010", "11111", "00010", "00010", "00010"],
];

export function NotFoundPage() {
  return (
    <div {...stylex.props(styles.page)}>
      <header {...stylex.props(styles.header)}>
        <Link href="/" aria-label="ChartCoach home" {...stylex.props(styles.brand, ui.focus)}>
          <Image
            src={logo}
            alt=""
            width={144}
            height={36}
            unoptimized
            {...stylex.props(styles.logoLight)}
          />
          <Image
            src={logoWhite}
            alt=""
            width={144}
            height={36}
            unoptimized
            {...stylex.props(styles.logoDark)}
          />
        </Link>
      </header>
      <main {...stylex.props(styles.main)}>
        <svg
          viewBox="0 0 440 300"
          fill="none"
          aria-hidden="true"
          focusable="false"
          {...stylex.props(styles.chart)}
        >
          <g {...stylex.props(styles.grid)}>
            {[64, 104, 144, 184, 224, 264].map((y) => (
              <path key={y} d={`M24 ${y}H416`} />
            ))}
            {[56, 96, 136, 176, 216, 256, 296, 336, 376, 416].map((x) => (
              <path key={x} d={`M${x} 24V264`} />
            ))}
          </g>
          <path d="M24 24V264H416" {...stylex.props(styles.axis)} />
          <g {...stylex.props(styles.points)}>
            {digits.flatMap((rows, digit) =>
              rows.flatMap((row, y) =>
                Array.from(row).map((value, x) =>
                  value === "1" ? (
                    <circle
                      key={`${digit}:${x}:${y}`}
                      cx={56 + digit * 132 + x * 22}
                      cy={68 + y * 22}
                      r={6}
                    />
                  ) : null,
                ),
              ),
            )}
          </g>
          <circle cx="232" cy="134" r="18" {...stylex.props(styles.halo)} />
          <circle cx="232" cy="134" r="7" {...stylex.props(styles.missingPoint)} />
          <path d="M227 134H237M232 129V139" {...stylex.props(styles.cross)} />
        </svg>
        <div {...stylex.props(styles.content)}>
          <p {...stylex.props(styles.eyebrow)}>404 / Page not found</p>
          <h1 {...stylex.props(styles.title)}>We couldn’t find that page.</h1>
          <p {...stylex.props(styles.description)}>
            The link may have changed, or the address may be incomplete. Your next chart starts
            here.
          </p>
          <nav aria-label="Page recovery" {...stylex.props(styles.actions)}>
            <Link href="/" {...stylex.props(ui.button, ui.focus, styles.primary)}>
              Back to chat <ArrowRight size={18} aria-hidden="true" />
            </Link>
            <Link href="/guidelines" {...stylex.props(ui.button, ui.focus, styles.secondary)}>
              <BookOpen size={18} aria-hidden="true" /> Browse guidelines
            </Link>
          </nav>
        </div>
      </main>
      <footer {...stylex.props(styles.footer)}>Visualization guidance, grounded in sources.</footer>
    </div>
  );
}

const styles = stylex.create({
  page: {
    minHeight: "100svh",
    display: "flex",
    flexDirection: "column",
    paddingTop: "max(24px, env(safe-area-inset-top))",
    paddingBottom: "max(24px, env(safe-area-inset-bottom))",
    paddingLeft: "max(clamp(20px, 5vw, 80px), env(safe-area-inset-left))",
    paddingRight: "max(clamp(20px, 5vw, 80px), env(safe-area-inset-right))",
  },
  header: { width: "100%", maxWidth: 1280, marginInline: "auto" },
  brand: { display: "inline-flex", minHeight: 44, alignItems: "center", borderRadius: 4 },
  logoLight: { width: 144, height: 36, display: { default: "block", [media.dark]: "none" } },
  logoDark: { width: 144, height: 36, display: { default: "none", [media.dark]: "block" } },
  main: {
    flexGrow: 1,
    display: "grid",
    gridTemplateColumns: {
      default: "1fr",
      "@media (min-width: 1100px), (min-width: 600px) and (max-height: 620px)": "1fr 1fr",
    },
    alignContent: "center",
    alignItems: "center",
    gap: {
      default: 28,
      "@media (min-width: 1100px), (min-width: 600px) and (max-height: 620px)":
        "clamp(24px, 6vw, 96px)",
    },
    maxWidth: {
      default: 480,
      "@media (min-width: 1100px), (min-width: 600px) and (max-height: 620px)": 1080,
    },
    width: "100%",
    marginInline: "auto",
    paddingBlock: { default: 64, [media.mobile]: 40, [media.short]: 16 },
  },
  chart: { width: "100%", height: "auto", overflow: "visible" },
  grid: { stroke: colors.border, strokeWidth: 1, opacity: 0.6 },
  axis: { stroke: colors.muted, strokeWidth: 1, opacity: 0.45 },
  points: { fill: colors.muted, opacity: 0.7 },
  halo: { fill: "color-mix(in srgb, var(--brand-crimson) 8%, transparent)" },
  missingPoint: { stroke: colors.accent, strokeWidth: 1.5 },
  cross: { stroke: colors.accent, strokeWidth: 1.5 },
  content: { minWidth: 0 },
  eyebrow: {
    color: colors.accentText,
    fontSize: 12,
    fontWeight: 600,
    letterSpacing: "0.08em",
    textTransform: "uppercase",
  },
  title: {
    marginTop: { default: 16, [media.short]: 12 },
    fontSize: { default: "clamp(32px, 4vw, 48px)", [media.short]: 28 },
    fontWeight: 550,
    lineHeight: 1.12,
    letterSpacing: "-0.045em",
    textWrap: "balance",
  },
  description: {
    color: colors.muted,
    fontSize: { default: 16, [media.short]: 14 },
    lineHeight: { default: 1.7, [media.short]: 1.5 },
    marginTop: { default: 20, [media.short]: 12 },
    maxWidth: 380,
  },
  actions: {
    display: "flex",
    flexWrap: "wrap",
    gap: { default: 12, [media.short]: 8 },
    marginTop: { default: 28, [media.short]: 16 },
  },
  primary: {
    backgroundColor: colors.foreground,
    color: colors.background,
    paddingInline: 18,
    gap: 18,
    fontWeight: 550,
  },
  secondary: { color: colors.muted, paddingInline: 12 },
  footer: {
    color: colors.muted,
    fontSize: 12,
    width: "100%",
    maxWidth: 1280,
    marginInline: "auto",
  },
});
