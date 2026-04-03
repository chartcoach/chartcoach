import clsx from "clsx";
import { BookOpen } from "lucide-react";

const EMPTY_PROPS: Record<string, string> = {};

export function AxisHeader({
  dimensionLabel,
  valueLabel,
  metaLabel = null,
  metaKind = null,
  className,
  showDimension = true,
  extraProps = EMPTY_PROPS,
}: {
  dimensionLabel: string;
  valueLabel: string;
  metaLabel?: string | null;
  metaKind?: "guidelines" | null;
  className: string;
  showDimension?: boolean;
  extraProps?: Record<string, string>;
}) {
  const normalizedDimensionLabel = dimensionLabel.toLowerCase();
  const classes = clsx(className, !showDimension && "is-dimension-hidden");

  return (
    <div className={classes} {...extraProps}>
      <div className="vg-axis-stack">
        <div
          aria-hidden={showDimension ? undefined : true}
          className={clsx("vg-axis-dimension-label", !showDimension && "is-placeholder")}
        >
          {normalizedDimensionLabel}
        </div>
        <div className={clsx("vg-axis-value-line", metaLabel && "has-meta")}>
          <div className="vg-axis-value-label">{valueLabel}</div>
          {metaLabel ? (
            <div className="vg-axis-value-meta">
              {metaKind === "guidelines" ? (
                <BookOpen aria-hidden className="vg-axis-value-meta-icon" strokeWidth={1.85} />
              ) : null}
              <span>{metaLabel}</span>
            </div>
          ) : null}
        </div>
      </div>
    </div>
  );
}
