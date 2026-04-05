import type {
  CandidateImageMeta,
  CellVariant,
  MatrixCell,
  OverviewPayload,
} from "../contract/types";
export declare function toOptionValue(value: unknown): string;
export declare function fromOptionValue(value: string): string | null;
export declare function formatScore(value: unknown): string | null;
export declare function formatMetricScore(value: unknown): string | null;
export declare function renderImage(
  imageUrl: string | null,
  alt: string,
  imageMeta?: CandidateImageMeta | null,
  surface?: string,
): import("react/jsx-runtime").JSX.Element;
export declare function getCellByKey(
  overview: OverviewPayload | null,
  cellKey: string | null,
): MatrixCell | null;
export declare function clampVariantIndex(cell: MatrixCell, index: number): number;
export declare function getVariantByIndex(
  cell: MatrixCell | null | undefined,
  index: number,
): CellVariant | null;
export declare function orientationLabel(parts: Array<string | null | undefined>): string;
export declare function spotlightClass(hasHover: boolean, isActive: boolean): string;
//# sourceMappingURL=utils.d.ts.map
