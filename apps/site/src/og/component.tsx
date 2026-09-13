import type { CSSProperties, ReactNode } from "react";

import {
  CHARTCOACH_WORDMARK_PATH,
  DASH_RING_ACCENT_ROTATIONS,
  DASH_RING_BASE_ROTATIONS,
} from "./brand";
import {
  OG_IMAGE_HEIGHT,
  OG_IMAGE_WIDTH,
  type OgImageProps,
  type OgReferenceSummary,
} from "./schema";
import { wrapOgText } from "./text";

const theme = {
  accent: "#e0364b",
  coral: "#f25a6d",
  dark: "#0a0a0a",
  darkBorder: "#2a2a2a",
  darkDivider: "#1f1f1f",
  darkMuted: "#7c7a76",
  darkPillText: "#c9c7c3",
  darkRoleMuted: "#3a3a3a",
  darkText: "#b4b2ae",
  darkTextStrong: "#f2f0ec",
  ink: "#111111",
  labelBorder: "#e4e4e4",
  labelMuted: "#8a8884",
  labelSeparator: "#c0beb8",
  labelSurface: "#f5f5f5",
  referenceTitle: "#1a1a1a",
  sourceHeading: "#9a9893",
  white: "#ffffff",
} as const;

// Current catalog title distribution: min 29, median 61, p90 82, max 125 chars.
const guidelineTitleBreakpoints = {
  shortest: 29,
  median: 61,
  p90: 82,
  longest: 125,
} as const;

type LabelParts = {
  namespace?: string;
  value: string;
};

function clamp(value: number, min: number, max: number): number {
  return Math.min(Math.max(value, min), max);
}

function interpolate(value: number, from: number, to: number, start: number, end: number): number {
  if (from === to) return end;
  const progress = clamp((value - from) / (to - from), 0, 1);

  return start + (end - start) * progress;
}

function guidelineTitleSize(title: string): number {
  const length = title.length;

  if (length <= guidelineTitleBreakpoints.median) {
    return Math.round(
      interpolate(
        length,
        guidelineTitleBreakpoints.shortest,
        guidelineTitleBreakpoints.median,
        58,
        51,
      ),
    );
  }

  if (length <= guidelineTitleBreakpoints.p90) {
    return Math.round(
      interpolate(length, guidelineTitleBreakpoints.median, guidelineTitleBreakpoints.p90, 51, 47),
    );
  }

  return Math.round(
    interpolate(length, guidelineTitleBreakpoints.p90, guidelineTitleBreakpoints.longest, 47, 40),
  );
}

function withAlpha(hex: string, alpha: number): string {
  const normalized = hex.replace("#", "");
  const red = Number.parseInt(normalized.slice(0, 2), 16);
  const green = Number.parseInt(normalized.slice(2, 4), 16);
  const blue = Number.parseInt(normalized.slice(4, 6), 16);

  return `rgba(${red},${green},${blue},${alpha})`;
}

function DashRing({
  accentColor,
  dashColor,
  opacity = 1,
  size,
}: {
  accentColor: string;
  dashColor: string;
  opacity?: number;
  size: number;
}) {
  const rects = [
    ...DASH_RING_ACCENT_ROTATIONS.map((rotation) => ({ fill: accentColor, rotation })),
    ...DASH_RING_BASE_ROTATIONS.map((rotation) => ({ fill: dashColor, rotation })),
  ];

  return (
    <svg height={size} style={{ display: "block", opacity }} viewBox="0 0 100 100" width={size}>
      {rects.map(({ fill, rotation }) => (
        <rect
          fill={fill}
          height={13}
          key={`${fill}-${rotation}`}
          rx={2.1}
          transform={`rotate(${rotation} 50 50)`}
          width={4.2}
          x={47.9}
          y={5}
        />
      ))}
    </svg>
  );
}

function Wordmark({ fill, width }: { fill: string; width: number }) {
  return (
    <svg
      height={(width * 749) / 5741}
      style={{ display: "block" }}
      viewBox="0 0 5741 749"
      width={width}
    >
      <g fill={fill} transform="translate(-37 740)">
        <path d={CHARTCOACH_WORDMARK_PATH} />
      </g>
    </svg>
  );
}

function BrandLockup({ tone }: { tone: "dark" | "light" }) {
  const onDark = tone === "dark";

  return (
    <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
      <DashRing
        accentColor={onDark ? theme.coral : theme.accent}
        dashColor={onDark ? theme.white : theme.ink}
        size={onDark ? 52 : 48}
      />
      <div style={{ display: "flex", marginLeft: onDark ? -6 : -5 }}>
        <Wordmark fill={onDark ? theme.white : theme.ink} width={onDark ? 210 : 190} />
      </div>
    </div>
  );
}

function Badge({ children, tone }: { children?: ReactNode; tone: "dark" | "light" }) {
  return (
    <div
      style={{
        display: "flex",
        border: `1px solid ${tone === "dark" ? theme.darkBorder : withAlpha(theme.accent, 0.4)}`,
        borderRadius: 4,
        color: tone === "dark" ? theme.darkMuted : theme.accent,
        fontFamily: "JetBrains Mono",
        fontSize: 13,
        fontWeight: 500,
        letterSpacing: "0.12em",
        lineHeight: 1,
        padding: "7px 13px",
      }}
    >
      {children}
    </div>
  );
}

function HomeHeadline({ title }: { title: string }) {
  const exactReferenceTitle = title.trim().toLowerCase() === "design knowledge agents can cite.";

  if (exactReferenceTitle) {
    return (
      <div style={{ display: "flex", flexDirection: "column" }}>
        <div style={homeHeadlineStyle}>Design knowledge</div>
        <div style={homeHeadlineStyle}>
          <span>agents can</span>
          <span style={{ color: theme.coral, marginLeft: 14 }}>cite</span>
          <span>.</span>
        </div>
      </div>
    );
  }

  const lines = wrapOgText(title, 26, 2);

  return (
    <div style={{ display: "flex", flexDirection: "column" }}>
      {lines.map((line, index) => (
        <div
          key={`${line}-${index}`}
          style={{
            display: "flex",
            color: theme.white,
            fontSize: 68,
            fontWeight: 600,
            letterSpacing: "-0.025em",
            lineHeight: 1.05,
          }}
        >
          {index === lines.length - 1 ? `${line}.` : line}
        </div>
      ))}
    </div>
  );
}

const homeHeadlineStyle: CSSProperties = {
  display: "flex",
  color: theme.white,
  fontSize: 74,
  fontWeight: 600,
  letterSpacing: "-0.025em",
  lineHeight: 1.02,
};

function HomeImage(props: OgImageProps) {
  const verbs =
    props.verbs.length > 0
      ? props.verbs
      : ["Review", "Recommend", "Discuss", "Evaluate", "Contribute"];

  return (
    <div style={frameStyle(theme.dark, theme.white)}>
      <div style={{ display: "flex", position: "absolute", right: -180, top: -25 }}>
        <DashRing accentColor={theme.coral} dashColor={theme.white} opacity={0.1} size={680} />
      </div>
      <TopRule />
      <div style={contentStyle(72)}>
        <BrandLockup tone="dark" />
        <div style={{ display: "flex", flexDirection: "column", maxWidth: 880 }}>
          <div
            style={{
              display: "flex",
              color: theme.darkMuted,
              fontFamily: "JetBrains Mono",
              fontSize: 14,
              fontWeight: 500,
              letterSpacing: "0.14em",
              lineHeight: 1,
              marginBottom: 26,
            }}
          >
            {props.eyebrow.toUpperCase()}
          </div>
          <HomeHeadline title={props.title} />
          <div
            style={{
              display: "flex",
              color: theme.darkText,
              fontSize: 25,
              fontWeight: 400,
              lineHeight: 1.45,
              marginTop: 24,
              maxWidth: 760,
            }}
          >
            {props.description}
          </div>
        </div>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <div style={{ display: "flex", gap: 10 }}>
            {verbs.map((verb) => (
              <div
                key={verb}
                style={{
                  display: "flex",
                  border: `1px solid ${theme.darkBorder}`,
                  borderRadius: 5,
                  color: theme.darkPillText,
                  fontFamily: "JetBrains Mono",
                  fontSize: 15,
                  fontWeight: 500,
                  lineHeight: 1,
                  padding: "9px 15px",
                }}
              >
                {verb}
              </div>
            ))}
          </div>
          <span
            style={{
              color: theme.darkMuted,
              fontFamily: "JetBrains Mono",
              fontSize: 16,
              fontWeight: 500,
              lineHeight: 1,
            }}
          >
            chartcoach.dev
          </span>
        </div>
      </div>
    </div>
  );
}

function CatalogImage(props: OgImageProps) {
  const roles =
    props.roles.length > 0
      ? props.roles
      : ["advice", "reason", "context", "exceptions", "costs", "mistakes", "check", "fix"];

  const stat = props.stat ?? { value: "781", label: "guidelines, openly\nauthored and reviewed" };
  const labelLines = stat.label.split(/\n/);

  return (
    <div style={frameStyle(theme.dark, theme.white)}>
      <TopRule />
      <div style={contentStyle(72)}>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <BrandLockup tone="dark" />
          <Badge tone="dark">{(props.badge ?? "Catalog").toUpperCase()}</Badge>
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <div
            style={{
              display: "flex",
              color: theme.white,
              fontSize: 64,
              fontWeight: 600,
              letterSpacing: "-0.025em",
              lineHeight: 1,
            }}
          >
            {props.title}
          </div>
          <div style={{ display: "flex", alignItems: "baseline", gap: 18, marginTop: 26 }}>
            <span
              style={{
                color: theme.coral,
                fontSize: 96,
                fontWeight: 700,
                letterSpacing: "-0.03em",
                lineHeight: 0.9,
              }}
            >
              {stat.value}
            </span>
            <div
              style={{
                display: "flex",
                flexDirection: "column",
                color: theme.darkText,
                fontSize: 25,
                fontWeight: 500,
                lineHeight: 1.18,
              }}
            >
              {labelLines.map((line) => (
                <div key={line} style={{ display: "flex" }}>
                  {line}
                </div>
              ))}
            </div>
          </div>
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <div
            style={{
              display: "flex",
              color: theme.darkMuted,
              fontFamily: "JetBrains Mono",
              fontSize: 12,
              fontWeight: 500,
              letterSpacing: "0.14em",
              lineHeight: 1,
              marginBottom: 14,
            }}
          >
            {props.eyebrow.toUpperCase()}
          </div>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              borderTop: `1px solid ${theme.darkDivider}`,
              paddingTop: 16,
            }}
          >
            {roles.map((role, index) => (
              <div
                key={role}
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 11,
                  paddingRight: 11,
                }}
              >
                <div
                  style={{
                    display: "flex",
                    width: 8,
                    height: 8,
                    borderRadius: 99,
                    backgroundColor: index === 0 ? theme.accent : theme.darkRoleMuted,
                  }}
                />
                <span
                  style={{
                    color: index === 0 ? theme.darkTextStrong : theme.labelMuted,
                    fontFamily: "JetBrains Mono",
                    fontSize: 17,
                    fontWeight: 500,
                    lineHeight: 1,
                  }}
                >
                  {role}
                </span>
                {index < roles.length - 1 && (
                  <span style={{ color: theme.darkRoleMuted, fontSize: 15, marginLeft: 11 }}>
                    /
                  </span>
                )}
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

function labelParts(label: string): LabelParts {
  const separator = label.indexOf(":");

  if (separator < 1) return { value: label };

  return {
    namespace: label.slice(0, separator),
    value: label.slice(separator + 1),
  };
}

function LabelPill({ label }: { label: string }) {
  const parts = labelParts(label);

  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        backgroundColor: theme.labelSurface,
        border: `1px solid ${theme.labelBorder}`,
        borderRadius: 6,
        color: theme.accent,
        fontFamily: "JetBrains Mono",
        fontSize: 14.5,
        fontWeight: 500,
        lineHeight: 1,
        padding: "7px 11px",
        whiteSpace: "nowrap",
      }}
    >
      {parts.namespace && <span style={{ color: theme.labelMuted }}>{parts.namespace}</span>}
      {parts.namespace && <span style={{ color: theme.labelSeparator }}>:</span>}
      <span style={{ color: theme.accent }}>{parts.value}</span>
    </div>
  );
}

function labelRows(labels: string[]): string[][] {
  const rows: string[][] = [[]];
  let currentWidth = 0;

  for (const label of labels) {
    const estimatedWidth = 28 + label.length * 8.3;

    if (rows.at(-1)?.length && currentWidth + estimatedWidth > 1040) {
      rows.push([]);
      currentWidth = 0;
    }

    rows.at(-1)?.push(label);
    currentWidth += estimatedWidth + 8;
  }

  return rows.slice(0, 2);
}

function referenceRow(reference: OgReferenceSummary, index: number) {
  const titleSize = reference.title.length > 112 ? 20 : reference.title.length > 84 ? 21 : 22;

  return (
    <div
      key={`${reference.title}-${index}`}
      style={{ display: "flex", gap: 16, alignItems: "flex-start" }}
    >
      <span
        style={{
          color: theme.accent,
          flex: "none",
          fontFamily: "JetBrains Mono",
          fontSize: 18,
          fontWeight: 600,
          lineHeight: 1.3,
          paddingTop: 1,
          width: 20,
        }}
      >
        {index + 1}
      </span>
      <div style={{ display: "flex", flexDirection: "column" }}>
        <div
          style={{
            display: "flex",
            color: theme.referenceTitle,
            fontSize: titleSize,
            fontWeight: 500,
            lineHeight: 1.24,
            width: 980,
          }}
        >
          {reference.title}
        </div>
        {reference.meta && (
          <div
            style={{
              display: "flex",
              color: theme.labelMuted,
              fontFamily: "JetBrains Mono",
              fontSize: 15,
              fontWeight: 400,
              lineHeight: 1.25,
              marginTop: 5,
            }}
          >
            {reference.meta}
          </div>
        )}
      </div>
    </div>
  );
}

function GuidelineImage(props: OgImageProps) {
  const titleSize = guidelineTitleSize(props.title);

  const badge =
    props.badge ??
    (props.kind === "guideline-json"
      ? "JSON"
      : props.kind === "guideline-md"
        ? "Markdown"
        : "Guideline");

  const rows = labelRows(props.labels);

  return (
    <div style={frameStyle(theme.white, theme.ink)}>
      <TopRule />
      <div style={contentStyle("58px 72px 56px")}>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <BrandLockup tone="light" />
          <Badge tone="light">{badge.toUpperCase()}</Badge>
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <div
            style={{
              display: "flex",
              color: theme.ink,
              fontSize: titleSize,
              fontWeight: 600,
              letterSpacing: "-0.022em",
              lineHeight: titleSize >= 52 ? 1.04 : 1.07,
              maxWidth: 1040,
            }}
          >
            {props.title}
          </div>
          <div style={{ display: "flex", flexDirection: "column", gap: 9, marginTop: 22 }}>
            {rows.map((row, rowIndex) => (
              <div key={`label-row-${rowIndex}`} style={{ display: "flex", gap: 9 }}>
                {row.map((label) => (
                  <LabelPill key={label} label={label} />
                ))}
              </div>
            ))}
          </div>
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <div
            style={{
              display: "flex",
              borderTop: `1px solid ${theme.labelBorder}`,
              color: theme.sourceHeading,
              fontFamily: "JetBrains Mono",
              fontSize: 13,
              fontWeight: 500,
              letterSpacing: "0.14em",
              lineHeight: 1,
              marginBottom: 20,
              paddingTop: 18,
            }}
          >
            SOURCES
          </div>
          <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
            {props.references.map((reference, index) => referenceRow(reference, index))}
          </div>
        </div>
      </div>
    </div>
  );
}

function TopRule() {
  return (
    <div
      style={{
        display: "flex",
        position: "absolute",
        top: 0,
        left: 0,
        width: "100%",
        height: 4,
        backgroundColor: theme.accent,
      }}
    />
  );
}

function frameStyle(backgroundColor: string, color: string): CSSProperties {
  return {
    display: "flex",
    width: OG_IMAGE_WIDTH,
    height: OG_IMAGE_HEIGHT,
    backgroundColor,
    color,
    fontFamily: "Poppins",
    overflow: "hidden",
    position: "relative",
  };
}

function contentStyle(padding: CSSProperties["padding"]): CSSProperties {
  return {
    display: "flex",
    position: "absolute",
    top: 0,
    left: 0,
    width: OG_IMAGE_WIDTH,
    height: OG_IMAGE_HEIGHT,
    padding,
    flexDirection: "column",
    justifyContent: "space-between",
  };
}

export default function OgImage(props: OgImageProps) {
  if (props.kind === "home" || props.kind === "page") return <HomeImage {...props} />;

  if (props.kind === "catalog") return <CatalogImage {...props} />;

  return <GuidelineImage {...props} />;
}
