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
  accent: "#E0364B",
  coral: "#F25A6D",
  dark: "#0A0A0A",
  darkBorder: "#2A2A2A",
  darkDivider: "#1F1F1F",
  darkMuted: "#7C7A76",
  darkText: "#B4B2AE",
  darkTextStrong: "#F2F0EC",
  ink: "#111111",
  labelBorder: "#E4E4E4",
  labelMuted: "#8A8884",
  labelSeparator: "#C0BEB8",
  labelSurface: "#F5F5F5",
  white: "#FFFFFF",
};

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
        border: `1px solid ${tone === "dark" ? theme.darkBorder : "rgba(224,54,75,0.4)"}`,
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
                  color: "#C9C7C3",
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
                    backgroundColor: index === 0 ? theme.accent : "#3A3A3A",
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
                  <span style={{ color: "#3A3A3A", fontSize: 15, marginLeft: 11 }}>/</span>
                )}
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

function labelParts(label: string): { namespace?: string; value: string } {
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
        fontSize: 13,
        fontWeight: 500,
        lineHeight: 1,
        padding: "6px 10px",
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
    const estimatedWidth = 24 + label.length * 7.4;
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
          fontSize: 16,
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
            color: "#1A1A1A",
            fontSize: 18,
            fontWeight: 500,
            lineHeight: 1.3,
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
              fontSize: 13.5,
              fontWeight: 400,
              lineHeight: 1.25,
              marginTop: 4,
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
  const titleSize = props.title.length > 128 ? 31 : props.title.length > 96 ? 34 : 38;
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
      <div style={contentStyle("64px 72px")}>
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
              letterSpacing: "-0.02em",
              lineHeight: 1.12,
              maxWidth: 1040,
            }}
          >
            {props.title}
          </div>
          <div style={{ display: "flex", flexDirection: "column", gap: 8, marginTop: 22 }}>
            {rows.map((row, rowIndex) => (
              <div key={`label-row-${rowIndex}`} style={{ display: "flex", gap: 8 }}>
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
              color: "#9A9893",
              fontFamily: "JetBrains Mono",
              fontSize: 12,
              fontWeight: 500,
              letterSpacing: "0.14em",
              lineHeight: 1,
              marginBottom: 18,
              paddingTop: 18,
            }}
          >
            SOURCES
          </div>
          <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
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
