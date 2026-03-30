import { useEffect, useState } from "react";
import type {
  CandidateImageMeta,
  CellVariant,
  MatrixCell,
  OverviewPayload,
} from "@/viewer/contract/types";

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
    <div className={`vg-image-stage surface-${surface}`.trim()}>
      {status === "loading" ? <ImagePlaceholder surface={surface} variant="loading" /> : null}
      <img
        alt={alt}
        className={classes.join(" ")}
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
  return (
    <div className={`vg-image-placeholder surface-${surface} is-${variant}`.trim()}>
      <div className="vg-image-placeholder-card">
        <div className="vg-image-placeholder-frame">
          <svg aria-hidden className="vg-image-placeholder-glyph" viewBox="0 0 120 80">
            <path
              className="vg-image-placeholder-axis"
              d="M16 12v52 M16 64h90"
              fill="none"
              pathLength="1"
            />
            <path
              className="vg-image-placeholder-grid"
              d="M16 26h90 M16 40h90 M16 54h90"
              fill="none"
              pathLength="1"
            />
            <path
              className="vg-image-placeholder-series is-secondary"
              d="M20 52 L36 48 L52 50 L70 42 L90 46 L104 38"
              fill="none"
              pathLength="1"
            />
            <path
              className="vg-image-placeholder-series is-primary"
              d="M20 58 L36 54 L52 42 L70 47 L90 28 L104 20"
              fill="none"
              pathLength="1"
            />
          </svg>
        </div>
        <span className="vg-image-placeholder-copy">
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
