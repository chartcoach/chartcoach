import type {
  AssetPayload,
  CandidateImageMeta,
  MatrixCell,
  OverviewPayload,
} from "@/viewer/contract/types";

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
  if (!imageUrl) {
    return null;
  }
  const classes = ["vg-image", `surface-${surface}`];
  if (imageMeta?.is_extreme_aspect) {
    classes.push("is-extreme-aspect", `is-${imageMeta.aspect_kind}`);
  }
  return <img alt={alt} className={classes.join(" ")} loading="lazy" src={imageUrl} />;
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

export function resolveAsset(
  fallbackUrl: string | null | undefined,
  fallbackMeta: CandidateImageMeta | null | undefined,
  asset: AssetPayload | null | undefined,
) {
  return {
    imageUrl: asset?.image_url ?? fallbackUrl ?? null,
    imageMeta: asset?.image_meta ?? fallbackMeta ?? null,
    error: asset?.error ?? null,
  };
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
