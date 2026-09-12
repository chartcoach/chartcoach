import { useEffect, useRef, useState } from "react";
import { guidelineRoleSections, guidelineRoles, type GuidelineRole } from "./role-sections";

type Point2D = {
  x: number;
  y: number;
};

type SectionPoint = Point2D & {
  role: GuidelineRole;
  text: string;
  color: string;
};

type CatalogPoint = Point2D & {
  role: GuidelineRole;
  color: string;
  opacity: number;
  radius: number;
};

type HoverState = {
  point: SectionPoint;
  left: number;
  top: number;
  placement: "above" | "below";
};

type CanvasColors = {
  bg: string;
  fg: string;
  muted: string;
  border: string;
};

type DrawTextOptions = {
  align?: CanvasTextAlign;
  maxWidth?: number;
  mono?: boolean;
  size?: number;
  weight?: number;
};

type PlotBounds = {
  left: number;
  top: number;
  width: number;
  height: number;
};

const roleColors = {
  advice: "#2563eb",
  reason: "#d97706",
  context: "#0891b2",
  exceptions: "#dc2626",
  costs: "#a16207",
  mistakes: "#db2777",
  check: "#059669",
  fix: "#7c3aed",
} satisfies Record<GuidelineRole, string>;

const sectionPointLayout = {
  advice: { x: 0.28, y: 0.48 },
  reason: { x: 0.55, y: 0.43 },
  context: { x: 0.35, y: 0.69 },
  exceptions: { x: 0.64, y: 0.29 },
  costs: { x: 0.73, y: 0.56 },
  mistakes: { x: 0.51, y: 0.78 },
  check: { x: 0.39, y: 0.25 },
  fix: { x: 0.78, y: 0.76 },
} satisfies Record<GuidelineRole, Point2D>;

const compactLabelOffsets = {
  advice: { x: -30, y: 19 },
  reason: { x: 11, y: -24 },
  context: { x: -39, y: 25 },
  exceptions: { x: -31, y: -28 },
  costs: { x: 10, y: 21 },
  mistakes: { x: -55, y: 25 },
  check: { x: -22, y: -28 },
  fix: { x: 11, y: 23 },
} satisfies Record<GuidelineRole, Point2D>;

const sectionPoints: readonly SectionPoint[] = guidelineRoleSections.map((section) => ({
  role: section.role,
  text: section.text,
  color: roleColors[section.role],
  ...sectionPointLayout[section.role],
}));

const catalogPoints = makeCatalogPoints();

export function EmbeddingCanvas() {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const [hover, setHover] = useState<HoverState | null>(null);
  const hoveredRole = hover?.point.role ?? null;

  useEffect(() => {
    const canvas = canvasRef.current;

    if (!canvas) return;

    const context = canvas.getContext("2d");

    if (!context) return;

    const draw = () => {
      resizeCanvas(canvas, context);
      drawEmbedding(context, canvas, hoveredRole);
    };

    const observer = new ResizeObserver(draw);
    const themeObserver = new MutationObserver(draw);
    observer.observe(canvas);
    themeObserver.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["class", "style"],
    });
    draw();

    return () => {
      observer.disconnect();
      themeObserver.disconnect();
    };
  }, [hoveredRole]);

  function handlePointerMove(event: React.PointerEvent<HTMLCanvasElement>) {
    const canvas = canvasRef.current;

    if (!canvas) return;

    const hit = findHoveredSection(canvas, event);
    canvas.style.cursor = hit ? "pointer" : "default";
    setHover((current) => {
      if (!hit) return current ? null : current;

      if (
        current?.point.role === hit.point.role &&
        current.left === hit.left &&
        current.top === hit.top
      ) {
        return current;
      }

      return hit;
    });
  }

  function handlePointerLeave() {
    const canvas = canvasRef.current;

    if (canvas) canvas.style.cursor = "default";
    setHover(null);
  }

  return (
    <div className="relative h-[24rem] w-full bg-bg lg:h-[27rem]">
      <canvas
        ref={canvasRef}
        className="block h-full w-full"
        aria-label="Two dimensional section embedding view with highlighted guideline section points."
        onPointerMove={handlePointerMove}
        onPointerLeave={handlePointerLeave}
      />
      {hover ? <EmbeddingPopover hover={hover} /> : null}
    </div>
  );
}

function EmbeddingPopover({ hover }: { hover: HoverState }) {
  const transform =
    hover.placement === "above" ? "translate(-50%, calc(-100% - 14px))" : "translate(-50%, 14px)";

  return (
    <div
      className="pointer-events-none absolute z-20 w-[15.5rem] max-w-[calc(100%-2rem)] rounded-lg border border-border bg-bg px-3.5 py-3 text-left shadow-[0_18px_44px_color-mix(in_srgb,var(--color-fg)_14%,transparent)]"
      style={{ left: hover.left, top: hover.top, transform }}
    >
      <div className="flex items-center gap-2">
        <span
          className="h-2.5 w-2.5 shrink-0 rounded-full"
          style={{ backgroundColor: hover.point.color }}
          aria-hidden="true"
        />
        <p className="m-0 font-mono text-[0.6875rem] font-semibold uppercase tracking-[0.14em] text-muted">
          {hover.point.role}
        </p>
      </div>
      <p className="m-0 mt-2 text-[0.8125rem] font-medium leading-[1.45] text-fg">
        {hover.point.text}
      </p>
      <p className="m-0 mt-2 font-mono text-[0.6875rem] uppercase tracking-[0.12em] text-muted">
        embedded section text
      </p>
    </div>
  );
}

function makeCatalogPoints(): CatalogPoint[] {
  const clusters: readonly Point2D[] = [
    { x: 0.22, y: 0.43 },
    { x: 0.36, y: 0.68 },
    { x: 0.47, y: 0.38 },
    { x: 0.66, y: 0.48 },
    { x: 0.76, y: 0.58 },
  ];

  return Array.from({ length: 138 }, (_, index) => {
    const cluster = clusters[index % clusters.length];
    const role = guidelineRoles[index % guidelineRoles.length];
    const angle = index * 2.399963229728653;
    const radius = 0.025 + (((index * 23) % 100) / 100) * 0.18;

    return {
      role,
      x: clamp(cluster.x + Math.cos(angle) * radius, 0.07, 0.93),
      y: clamp(cluster.y + Math.sin(angle) * radius * 0.82, 0.14, 0.88),
      color: roleColors[role],
      opacity: 0.18 + ((index * 13) % 8) / 100,
      radius: 1.8 + ((index * 11) % 5) * 0.2,
    };
  });
}

function resizeCanvas(canvas: HTMLCanvasElement, context: CanvasRenderingContext2D) {
  const rect = canvas.getBoundingClientRect();
  const dpr = window.devicePixelRatio || 1;
  const width = Math.max(1, rect.width);
  const height = Math.max(1, rect.height);
  canvas.width = Math.round(width * dpr);
  canvas.height = Math.round(height * dpr);
  context.setTransform(dpr, 0, 0, dpr, 0, 0);
}

function readCanvasColors(canvas: HTMLCanvasElement): CanvasColors {
  const styles = getComputedStyle(canvas);

  return {
    bg: styles.getPropertyValue("--color-bg").trim() || "#ffffff",
    fg: styles.getPropertyValue("--color-fg").trim() || "#171717",
    muted: styles.getPropertyValue("--color-muted").trim() || "#666666",
    border: styles.getPropertyValue("--color-border").trim() || "#eaeaea",
  };
}

function drawEmbedding(
  context: CanvasRenderingContext2D,
  canvas: HTMLCanvasElement,
  hoveredRole: GuidelineRole | null,
) {
  const width = canvas.clientWidth || 1;
  const height = canvas.clientHeight || 1;
  const colors = readCanvasColors(canvas);
  const compact = width < 460;
  const bounds = getPlotBounds(width, height);

  context.clearRect(0, 0, width, height);
  context.fillStyle = colors.bg;
  context.fillRect(0, 0, width, height);

  drawGrid(context, bounds, colors);
  drawCatalogPoints(context, catalogPoints, bounds);
  drawSectionPoints(context, sectionPoints, bounds, colors, hoveredRole, compact);
}

function drawGrid(context: CanvasRenderingContext2D, bounds: PlotBounds, colors: CanvasColors) {
  context.save();
  context.strokeStyle = withAlpha(colors.border, 0.42);
  context.lineWidth = 1;

  for (let index = 0; index <= 6; index += 1) {
    const x = bounds.left + (bounds.width * index) / 6;
    context.beginPath();
    context.moveTo(x, bounds.top);
    context.lineTo(x, bounds.top + bounds.height);
    context.stroke();
  }

  for (let index = 0; index <= 5; index += 1) {
    const y = bounds.top + (bounds.height * index) / 5;
    context.beginPath();
    context.moveTo(bounds.left, y);
    context.lineTo(bounds.left + bounds.width, y);
    context.stroke();
  }

  context.restore();
}

function drawCatalogPoints(
  context: CanvasRenderingContext2D,
  points: readonly CatalogPoint[],
  bounds: PlotBounds,
) {
  for (const point of points) {
    const projected = projectPoint(point, bounds);
    context.beginPath();
    context.arc(projected.x, projected.y, point.radius, 0, Math.PI * 2);
    context.fillStyle = withAlpha(point.color, point.opacity);
    context.fill();
  }
}

function drawSectionPoints(
  context: CanvasRenderingContext2D,
  points: readonly SectionPoint[],
  bounds: PlotBounds,
  colors: CanvasColors,
  hoveredRole: GuidelineRole | null,
  compact: boolean,
) {
  for (const point of points) {
    const projected = projectPoint(point, bounds);
    const hovered = point.role === hoveredRole;
    const radius = hovered ? 8.2 : 6.5;
    const halo = hovered ? 20 : 15;

    context.beginPath();
    context.arc(projected.x, projected.y, halo, 0, Math.PI * 2);
    context.fillStyle = withAlpha(point.color, hovered ? 0.16 : 0.08);
    context.fill();

    context.beginPath();
    context.arc(projected.x, projected.y, radius + 3, 0, Math.PI * 2);
    context.fillStyle = colors.bg;
    context.fill();

    context.beginPath();
    context.arc(projected.x, projected.y, radius, 0, Math.PI * 2);
    context.fillStyle = point.color;
    context.fill();

    context.beginPath();
    context.arc(projected.x, projected.y, radius + 3, 0, Math.PI * 2);
    context.strokeStyle = withAlpha(point.color, hovered ? 0.52 : 0.3);
    context.lineWidth = hovered ? 1.5 : 1;
    context.stroke();

    if (compact) {
      const offset = compactLabelOffsets[point.role];
      drawRoleLabelPill(
        context,
        point.role,
        projected.x + offset.x,
        projected.y + offset.y,
        bounds,
        colors,
        point.color,
        1,
      );
    } else {
      drawText(context, point.role, projected.x + 14, projected.y + 5, colors.fg, {
        mono: true,
        size: 11,
        weight: 650,
      });
    }
  }
}

function drawRoleLabelPill(
  context: CanvasRenderingContext2D,
  text: string,
  x: number,
  y: number,
  bounds: PlotBounds,
  colors: CanvasColors,
  color: string,
  opacity: number,
) {
  const font = '650 9px SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace';
  const paddingX = 5;
  const height = 17;

  context.save();
  context.font = font;
  const width = Math.ceil(context.measureText(text).width + paddingX * 2);
  const left = clamp(x, bounds.left - 22, bounds.left + bounds.width + 22 - width);
  const top = clamp(y, bounds.top - 28, bounds.top + bounds.height + 18 - height);

  drawRoundedRect(context, left, top, width, height, 8);
  context.fillStyle = withAlpha(colors.bg, 0.94 * opacity);
  context.fill();
  context.strokeStyle = withAlpha(color, 0.28 * opacity);
  context.lineWidth = 1;
  context.stroke();

  context.font = font;
  context.fillStyle = withAlpha(colors.fg, 0.82 * opacity);
  context.textAlign = "left";
  context.textBaseline = "middle";
  context.fillText(text, left + paddingX, top + height / 2);
  context.restore();
}

function drawRoundedRect(
  context: CanvasRenderingContext2D,
  x: number,
  y: number,
  width: number,
  height: number,
  radius: number,
) {
  const corner = Math.min(radius, width / 2, height / 2);
  context.beginPath();
  context.moveTo(x + corner, y);
  context.lineTo(x + width - corner, y);
  context.quadraticCurveTo(x + width, y, x + width, y + corner);
  context.lineTo(x + width, y + height - corner);
  context.quadraticCurveTo(x + width, y + height, x + width - corner, y + height);
  context.lineTo(x + corner, y + height);
  context.quadraticCurveTo(x, y + height, x, y + height - corner);
  context.lineTo(x, y + corner);
  context.quadraticCurveTo(x, y, x + corner, y);
  context.closePath();
}

function findHoveredSection(
  canvas: HTMLCanvasElement,
  event: React.PointerEvent<HTMLCanvasElement>,
): HoverState | null {
  const rect = canvas.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;
  const bounds = getPlotBounds(rect.width, rect.height);

  let best: { point: SectionPoint; distance: number; projected: Point2D } | null = null;

  for (const point of sectionPoints) {
    const projected = projectPoint(point, bounds);
    const distance = Math.hypot(projected.x - x, projected.y - y);

    if (distance <= 17 && (!best || distance < best.distance)) {
      best = { point, distance, projected };
    }
  }

  if (!best) return null;

  const popoverWidth = Math.min(248, rect.width - 32);
  const left = clamp(best.projected.x, popoverWidth / 2 + 12, rect.width - popoverWidth / 2 - 12);
  const placement = best.projected.y > 118 ? "above" : "below";

  return {
    point: best.point,
    left,
    top: best.projected.y,
    placement,
  };
}

function getPlotBounds(width: number, height: number): PlotBounds {
  const compact = width < 460;
  const insetX = compact ? 32 : 44;
  const insetTop = compact ? 44 : 42;
  const insetBottom = compact ? 44 : 46;

  return {
    left: insetX,
    top: insetTop,
    width: Math.max(1, width - insetX * 2),
    height: Math.max(1, height - insetTop - insetBottom),
  };
}

function projectPoint(point: Point2D, bounds: PlotBounds) {
  return {
    x: bounds.left + point.x * bounds.width,
    y: bounds.top + point.y * bounds.height,
  };
}

function drawText(
  context: CanvasRenderingContext2D,
  text: string,
  x: number,
  y: number,
  color: string,
  options: DrawTextOptions = {},
) {
  const font = options.mono
    ? 'SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace'
    : '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif';

  context.save();
  context.font = `${options.weight ?? 600} ${options.size ?? 11}px ${font}`;
  context.fillStyle = color;
  context.textAlign = options.align ?? "left";
  context.textBaseline = "alphabetic";
  context.fillText(text, x, y, options.maxWidth);
  context.restore();
}

function clamp(value: number, min: number, max: number) {
  return Math.min(Math.max(value, min), max);
}

function withAlpha(color: string, alpha: number) {
  if (color.startsWith("#")) {
    const hex =
      color.length === 4
        ? color
            .slice(1)
            .split("")
            .map((value) => value + value)
            .join("")
        : color.slice(1);

    const value = Number.parseInt(hex, 16);
    const red = (value >> 16) & 255;
    const green = (value >> 8) & 255;
    const blue = value & 255;

    return `rgba(${red}, ${green}, ${blue}, ${alpha})`;
  }

  if (color.startsWith("rgb(")) {
    return color.replace("rgb(", "rgba(").replace(")", `, ${alpha})`);
  }

  return color;
}
