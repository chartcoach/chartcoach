import clsx from "clsx";
import { useEffect, useState } from "react";
import type {
  CandidateImageMeta,
  CellVariant,
  MatrixCell,
  OverviewPayload,
} from "../contract/types";

const loadedImageUrls = new Set<string>();

function cachedImageStatus(imageUrl: string | null): "loading" | "loaded" | "missing" {
  if (!imageUrl) {
    return "missing";
  }
  return loadedImageUrls.has(imageUrl) ? "loaded" : "loading";
}

export function toOptionValue(value: unknown): string {
  return value === null ? "__none__" : String(value);
}

export function fromOptionValue(value: string): string | null {
  return value === "__none__" ? null : value;
}

export function formatScore(value: unknown): string | null {
  if (value === null || value === undefined || Number.isNaN(value)) {
    return null;
  }
  return Number(value).toFixed(2);
}

export function formatMetricScore(value: unknown): string | null {
  if (value === null || value === undefined || Number.isNaN(value)) {
    return null;
  }
  const numeric = Number(value);
  if (Number.isInteger(numeric)) {
    return String(numeric);
  }
  return numeric.toFixed(1);
}

export function renderImage(
  imageUrl: string | null,
  alt: string,
  imageMeta: CandidateImageMeta | null = null,
  surface = "panel",
) {
  return <ImageSurface alt={alt} imageMeta={imageMeta} imageUrl={imageUrl} surface={surface} />;
}

function ImageSurface({
  imageUrl,
  alt,
  imageMeta,
  surface,
}: {
  imageUrl: string | null;
  alt: string;
  imageMeta: CandidateImageMeta | null;
  surface: string;
}) {
  const [status, setStatus] = useState<"loading" | "loaded" | "missing">(() =>
    cachedImageStatus(imageUrl),
  );

  useEffect(() => {
    setStatus(cachedImageStatus(imageUrl));
  }, [imageUrl]);

  if (!imageUrl || status === "missing") {
    return <ImagePlaceholder surface={surface} variant="missing" />;
  }

  const classes = ["vg-image", `surface-${surface}`];
  if (imageMeta?.is_extreme_aspect) {
    classes.push("is-extreme-aspect", `is-${imageMeta.aspect_kind}`);
  }
  return (
    <div className={clsx("vg-image-stage", `surface-${surface}`)}>
      {status === "loading" ? <ImagePlaceholder surface={surface} variant="loading" /> : null}
      <img
        alt={alt}
        className={clsx(classes)}
        loading="lazy"
        onError={() => setStatus("missing")}
        onLoad={() => {
          if (imageUrl) {
            loadedImageUrls.add(imageUrl);
          }
          setStatus("loaded");
        }}
        src={imageUrl}
        style={{ opacity: status === "loaded" ? 1 : 0 }}
      />
    </div>
  );
}

function ImagePlaceholder({
  surface,
  variant,
}: {
  surface: string;
  variant: "loading" | "missing";
}) {
  const isLoading = variant === "loading";
  return (
    <div
      className={clsx(
        "grid h-full min-h-full w-full place-items-center bg-[color:color-mix(in_srgb,var(--ccui-panel)_88%,var(--ccui-paper))] p-3 text-center text-muted-foreground",
        `surface-${surface}`,
      )}
      data-image-kind="placeholder"
    >
      <div className="grid w-[min(86%,12.8rem)] justify-items-center gap-2">
        <div className="grid aspect-[1.26/0.84] w-full place-items-center border border-border bg-[color:color-mix(in_srgb,var(--ccui-paper)_84%,var(--ccui-panel))] px-3 py-3 shadow-[inset_0_0_0_1px_color-mix(in_srgb,var(--ccui-border-strong)_8%,transparent)]">
          <svg
            aria-hidden
            className={clsx(
              "block aspect-[1.18/0.74] w-[min(66%,7rem)]",
              isLoading && "animate-pulse",
            )}
            viewBox="0 0 120 80"
          >
            <path
              fill="none"
              d="M16 12v52 M16 64h90"
              pathLength="1"
              stroke="color-mix(in srgb, var(--ccui-text) 26%, transparent)"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="1.6"
            />
            <path
              fill="none"
              d="M16 26h90 M16 40h90 M16 54h90"
              pathLength="1"
              stroke="color-mix(in srgb, var(--ccui-text) 10%, transparent)"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="1"
            />
            <path
              fill="none"
              d="M20 52 L36 48 L52 50 L70 42 L90 46 L104 38"
              pathLength="1"
              stroke="color-mix(in srgb, var(--ccui-text) 18%, transparent)"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="3"
            />
            <path
              fill="none"
              d="M20 58 L36 54 L52 42 L70 47 L90 28 L104 20"
              pathLength="1"
              stroke="color-mix(in srgb, var(--ccui-text) 36%, transparent)"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="3"
            />
          </svg>
        </div>
        <span className="font-mono text-[0.64rem] lowercase leading-[1.18] text-muted-foreground">
          {variant === "loading" ? "loading chart" : "image unavailable"}
        </span>
      </div>
    </div>
  );
}

export function getCellByKey(
  overview: OverviewPayload | null,
  cellKey: string | null,
): MatrixCell | null {
  if (!overview || !cellKey) {
    return null;
  }

  const matrix = overview.matrix;
  if (matrix.kind === "grouped") {
    for (const group of matrix.groups) {
      for (const row of group.rows) {
        for (const cell of row.cells) {
          if (cell.cell_key === cellKey) {
            return cell;
          }
        }
      }
    }
    return null;
  }

  for (const row of matrix.rows) {
    for (const cell of row.cells) {
      if (cell.cell_key === cellKey) {
        return cell;
      }
    }
  }
  return null;
}

export function clampVariantIndex(cell: MatrixCell, index: number): number {
  if (cell.variants.length === 0) {
    return 0;
  }
  return Math.min(Math.max(index, 0), cell.variants.length - 1);
}

export function getVariantByIndex(
  cell: MatrixCell | null | undefined,
  index: number,
): CellVariant | null {
  if (!cell || cell.variants.length === 0) {
    return null;
  }
  return cell.variants[clampVariantIndex(cell, index)] ?? null;
}

export function orientationLabel(parts: Array<string | null | undefined>): string {
  return parts.filter(Boolean).join(" · ");
}

export function spotlightClass(hasHover: boolean, isActive: boolean): string {
  if (!hasHover) {
    return "";
  }
  return isActive ? "is-hover-axis" : "is-recessed";
}
