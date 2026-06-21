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

type PlotBounds = {
  left: number;
  top: number;
  width: number;
  height: number;
};

const roleColors: Record<GuidelineRole, string> = {
  advice: "#2563eb",
  reason: "#d97706",
  context: "#0891b2",
  exceptions: "#dc2626",
  costs: "#a16207",
  mistakes: "#db2777",
  check: "#059669",
  fix: "#7c3aed",
};

const sectionPointLayout: Record<GuidelineRole, Point2D> = {
  advice: { x: 0.28, y: 0.48 },
  reason: { x: 0.55, y: 0.43 },
  context: { x: 0.35, y: 0.69 },
  exceptions: { x: 0.64, y: 0.29 },
  costs: { x: 0.73, y: 0.56 },
  mistakes: { x: 0.51, y: 0.78 },
  check: { x: 0.39, y: 0.25 },
  fix: { x: 0.78, y: 0.76 },
};

const sectionPoints: readonly SectionPoint[] = guidelineRoleSections.map((section) => ({
  role: section.role,
  text: section.text,
  color: roleColors[section.role],
  ...sectionPointLayout[section.role],
}));

const catalogPoints = makeCatalogPoints();

type EmbeddingCanvasProps = {
  active: boolean;
};

export function EmbeddingCanvas({ active }: EmbeddingCanvasProps) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const startedAt = useRef<number | null>(null);
  const [hover, setHover] = useState<HoverState | null>(null);
  const hoveredRole = hover?.point.role ?? null;

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const context = canvas.getContext("2d");
    if (!context) return;

    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    let animationFrame = 0;

    const resize = () => resizeCanvas(canvas, context);

    const observer = new ResizeObserver(() => {
      resize();
      drawEmbedding(context, canvas, 1, 0, hoveredRole);
    });

    resize();
    observer.observe(canvas);

    const render = (now: number) => {
      if (!startedAt.current || !active) startedAt.current = now;
      const elapsed = now - startedAt.current;
      const progress = reduceMotion ? 1 : easeOutCubic(Math.min(elapsed / 900, 1));
      drawEmbedding(context, canvas, active ? progress : 1, reduceMotion ? 0 : elapsed, hoveredRole);

      if (active || progress < 1) {
        animationFrame = window.requestAnimationFrame(render);
      }
    };

    animationFrame = window.requestAnimationFrame(render);

    return () => {
      observer.disconnect();
      if (animationFrame) window.cancelAnimationFrame(animationFrame);
    };
  }, [active, hoveredRole]);

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
    hover.placement === "above"
      ? "translate(-50%, calc(-100% - 14px))"
      : "translate(-50%, 14px)";

  return (
    <div
      className="pointer-events-none absolute z-20 max-w-[15.5rem] rounded-lg border border-border bg-bg px-3.5 py-3 text-left shadow-[0_18px_44px_color-mix(in_srgb,var(--color-fg)_14%,transparent)]"
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
      opacity: 0.18 + (((index * 13) % 8) / 100),
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
  progress: number,
  pulse: number,
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
  drawCatalogPoints(context, catalogPoints, bounds, progress);
  drawSectionPoints(context, sectionPoints, bounds, colors, progress, pulse, hoveredRole, compact);
}

function drawGrid(
  context: CanvasRenderingContext2D,
  bounds: PlotBounds,
  colors: CanvasColors,
) {
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
  progress: number,
) {
  const fade = 0.3 + progress * 0.7;

  for (const point of points) {
    const projected = projectPoint(point, bounds);
    context.beginPath();
    context.arc(projected.x, projected.y, point.radius, 0, Math.PI * 2);
    context.fillStyle = withAlpha(point.color, point.opacity * fade);
    context.fill();
  }
}

function drawSectionPoints(
  context: CanvasRenderingContext2D,
  points: readonly SectionPoint[],
  bounds: PlotBounds,
  colors: CanvasColors,
  progress: number,
  pulse: number,
  hoveredRole: GuidelineRole | null,
  compact: boolean,
) {
  for (const [index, point] of points.entries()) {
    const projected = projectPoint(point, bounds);
    const reveal = clamp((progress - index * 0.08) / 0.72, 0, 1);
    const hovered = point.role === hoveredRole;
    const radius = (hovered ? 8.2 : 6.5) * reveal;
    const halo = (hovered ? 20 : 15) + Math.sin(pulse / 520 + index) * 1.2;

    context.beginPath();
    context.arc(projected.x, projected.y, halo, 0, Math.PI * 2);
    context.fillStyle = withAlpha(point.color, (hovered ? 0.16 : 0.08) * reveal);
    context.fill();

    context.beginPath();
    context.arc(projected.x, projected.y, radius + 3, 0, Math.PI * 2);
    context.fillStyle = colors.bg;
    context.fill();

    context.beginPath();
    context.arc(projected.x, projected.y, radius, 0, Math.PI * 2);
    context.fillStyle = withAlpha(point.color, reveal);
    context.fill();

    context.beginPath();
    context.arc(projected.x, projected.y, radius + 3, 0, Math.PI * 2);
    context.strokeStyle = withAlpha(point.color, hovered ? 0.52 : 0.3);
    context.lineWidth = hovered ? 1.5 : 1;
    context.stroke();

    if (!compact) {
      drawText(context, point.role, projected.x + 14, projected.y + 5, colors.fg, {
        mono: true,
        size: 11,
        weight: 650,
      });
    }
  }
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
  options: {
    align?: CanvasTextAlign;
    maxWidth?: number;
    mono?: boolean;
    size?: number;
    weight?: number;
  } = {},
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

function easeOutCubic(value: number) {
  return 1 - (1 - value) ** 3;
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
