const EMPTY_PROPS: Record<string, string> = {};

export function AxisHeader({
  dimensionLabel,
  valueLabel,
  className,
  showDimension = true,
  extraProps = EMPTY_PROPS,
}: {
  dimensionLabel: string;
  valueLabel: string;
  className: string;
  showDimension?: boolean;
  extraProps?: Record<string, string>;
}) {
  const normalizedDimensionLabel = dimensionLabel.toLowerCase();
  const classes = [className, showDimension ? "" : "is-dimension-hidden"].filter(Boolean).join(" ");

  return (
    <div className={classes} {...extraProps}>
      <div className="vg-axis-stack">
        <div
          aria-hidden={showDimension ? undefined : true}
          className={`vg-axis-dimension-label ${showDimension ? "" : "is-placeholder"}`.trim()}
        >
          {normalizedDimensionLabel}
        </div>
        <div className="vg-axis-value-label">{valueLabel}</div>
      </div>
    </div>
  );
}
