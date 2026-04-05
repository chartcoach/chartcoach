import clsx from "clsx";
import { BookOpen } from "lucide-react";

const EMPTY_PROPS: Record<string, string> = {};

export function AxisHeader({
  dimensionLabel,
  valueLabel,
  metaLabel = null,
  metaKind = null,
  kind,
  className,
  showDimension = true,
  extraProps = EMPTY_PROPS,
}: {
  dimensionLabel: string;
  valueLabel: string;
  metaLabel?: string | null;
  metaKind?: "guidelines" | null;
  kind: "group" | "column" | "row";
  className: string;
  showDimension?: boolean;
  extraProps?: Record<string, string>;
}) {
  const normalizedDimensionLabel = dimensionLabel.toLowerCase();
  const wrapperClass = clsx(
    kind === "group" &&
      "border border-border bg-muted px-[0.56rem] pb-[0.24rem] pt-[0.22rem] [border-left-width:4px] border-l-foreground",
  );
  const classes = clsx(className, !showDimension && "is-dimension-hidden", wrapperClass);
  const stackClass = clsx(
    "grid content-start",
    kind === "group" && "justify-items-start gap-[0.08rem]",
    kind === "column" &&
      "min-h-full w-full grid-rows-[0.62rem_auto] justify-items-start gap-[0.06rem]",
    kind === "row" &&
      "absolute bottom-0 left-0 w-max origin-bottom-left translate-y-full rotate-[-90deg] gap-[0.08rem]",
  );
  const dimensionClass = clsx(
    "font-mono font-semibold lowercase text-muted-foreground",
    kind === "group" && "text-[0.6rem] tracking-[0.09em]",
    kind === "column" && "text-[0.62rem] tracking-[0.07em]",
    kind === "row" && "text-[0.56rem] tracking-[0.08em]",
    !showDimension && "invisible",
  );
  const valueLineClass = clsx(
    "flex min-w-0 items-baseline gap-[0.3rem]",
    kind === "column" && "w-full justify-self-stretch",
    metaLabel && kind === "column" && "has-meta",
  );
  const valueLabelClass = clsx(
    "min-w-0 font-mono text-foreground",
    kind === "group" && "text-[0.86rem] font-bold leading-[1.18]",
    kind === "column" && "text-[0.8rem] font-bold leading-[1.14]",
    kind === "row" && "text-[0.74rem] font-semibold leading-[1.14] text-muted-foreground",
  );
  const valueMetaClass = clsx(
    "inline-flex min-w-0 flex-none items-center gap-[0.2rem] whitespace-nowrap font-mono leading-[1.1] text-muted-foreground",
    kind === "group" ? "text-[0.56rem]" : "text-[0.58rem]",
    kind === "column" && metaLabel && "ml-auto justify-end text-right",
  );

  return (
    <div className={classes} {...extraProps}>
      <div className={stackClass}>
        <div aria-hidden={showDimension ? undefined : true} className={dimensionClass}>
          {normalizedDimensionLabel}
        </div>
        <div className={valueLineClass}>
          <div className={valueLabelClass}>{valueLabel}</div>
          {metaLabel ? (
            <div className={valueMetaClass}>
              {metaKind === "guidelines" ? (
                <BookOpen aria-hidden className="size-[0.66rem] shrink-0" strokeWidth={1.85} />
              ) : null}
              <span>{metaLabel}</span>
            </div>
          ) : null}
        </div>
      </div>
    </div>
  );
}
