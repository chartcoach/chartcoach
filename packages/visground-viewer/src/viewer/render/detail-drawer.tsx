import clsx from "clsx";
import { Badge } from "@chartcoach/ui/components/badge";
import { Button } from "@chartcoach/ui/components/button";
import { Separator } from "@chartcoach/ui/components/separator";
import { MessageSquareText } from "lucide-react";
import type { CandidateGuidelineDetail, ViewerActions, ViewerState } from "../contract/types";
import { getCellByKey, getVariantByIndex, orientationLabel, renderImage } from "./utils";
import { ScoreBreakdownList } from "./score-ledger";

export function DetailDrawer({ state, actions }: { state: ViewerState; actions: ViewerActions }) {
  const cell = getCellByKey(state.overview, state.inspectCellKey);
  const variant = getVariantByIndex(cell, state.inspectVariantIndex);
  const candidate = variant?.candidate ?? null;
  if (!cell || !candidate || !variant) {
    return <section hidden />;
  }

  const labelParts = [cell.group_label, cell.row_label, cell.column_label].filter(
    (part): part is string => Boolean(part),
  );
  const label = orientationLabel(labelParts);

  return (
    <section className="pointer-events-auto fixed inset-0 z-[70]">
      <button
        className="absolute inset-0 border-0 bg-[var(--ccui-overlay)] p-0"
        onClick={() => actions.closeInspect()}
        type="button"
      />
      <aside className="absolute left-1/2 top-1/2 grid max-h-[min(98vh,72rem)] w-[min(96vw,96rem)] -translate-x-1/2 -translate-y-1/2 grid-rows-[auto_1fr] overflow-hidden border border-border bg-background shadow-[0_10px_26px_rgba(43,36,31,0.08)] max-[1180px]:fixed max-[1180px]:inset-0 max-[1180px]:h-auto max-[1180px]:max-h-none max-[1180px]:w-auto max-[1180px]:translate-x-0 max-[1180px]:translate-y-0 max-[1180px]:border-0 max-[1180px]:shadow-none">
        <div className="flex items-start justify-between gap-4 border-b border-border px-4 py-3 max-[1180px]:gap-3 max-[1180px]:px-4 max-[1180px]:py-3 max-[860px]:gap-2.5 max-[860px]:px-3.5 max-[860px]:py-3">
          <div className="grid min-w-0 flex-1 gap-2">
            <div className="flex flex-wrap items-center gap-x-2 gap-y-1 text-foreground max-[860px]:gap-x-1.5">
              {labelParts.map((part) => (
                <span
                  className="relative whitespace-nowrap font-mono text-[0.78rem] font-medium leading-[1.35] text-muted-foreground max-[860px]:text-[0.72rem] max-[860px]:leading-[1.3] [&:not(:first-child)]:ml-px [&:not(:first-child)]:pl-3 before:[&:not(:first-child)]:absolute before:[&:not(:first-child)]:left-0 before:[&:not(:first-child)]:top-1/2 before:[&:not(:first-child)]:h-[0.92rem] before:[&:not(:first-child)]:w-px before:[&:not(:first-child)]:-translate-y-1/2 before:[&:not(:first-child)]:bg-border max-[860px]:[&:not(:first-child)]:pl-[0.68rem] max-[860px]:before:[&:not(:first-child)]:h-[0.84rem]"
                  key={part}
                >
                  {part}
                </span>
              ))}
            </div>
            {state.overview ? (
              <div className="mt-px grid max-w-[min(54rem,100%)] grid-cols-[1.5rem_minmax(0,1fr)] items-start gap-2 max-[860px]:grid-cols-[1.36rem_minmax(0,1fr)] max-[860px]:gap-2">
                <span
                  aria-label="Query"
                  className="inline-flex w-6 justify-center pt-px text-muted-foreground max-[860px]:w-[1.36rem]"
                  title="Query"
                >
                  <MessageSquareText aria-hidden className="size-[1.12rem]" strokeWidth={1.8} />
                </span>
                <p
                  className="m-0 text-[0.84rem] font-semibold leading-[1.38] text-foreground [text-wrap:pretty] max-[860px]:text-[0.76rem]"
                  title={state.overview.label}
                >
                  {state.overview.label}
                </p>
              </div>
            ) : null}
          </div>
          <Button
            aria-label="Close"
            className="mt-px min-h-[1.55rem] min-w-[1.55rem] border-border bg-transparent p-0 text-[0.92rem] leading-none text-muted-foreground shadow-none hover:border-foreground hover:bg-muted hover:text-foreground"
            onClick={() => actions.closeInspect()}
            size="icon-xs"
            title="Close"
            type="button"
            variant="ghost"
          >
            ×
          </Button>
        </div>
        <div className="grid gap-2 overflow-auto px-[1.18rem] py-[1.08rem] max-[1180px]:px-4 max-[1180px]:py-4 max-[860px]:px-3.5 max-[860px]:py-3.5">
          <section className="grid content-start gap-3 bg-transparent">
            {cell.variants.length > 1 ? (
              <div className="mb-px flex flex-wrap items-center gap-1">
                {cell.variants.map((entry, index) => (
                  <button
                    className={clsx(
                      "vg-variant-chip",
                      index === state.inspectVariantIndex && "is-active",
                    )}
                    key={entry.variant_key}
                    onClick={() => actions.openInspect(cell.cell_key, index)}
                    type="button"
                  >
                    <span className="vg-variant-chip-label">
                      {entry.variant_label ?? entry.candidate.visgen_id}
                    </span>
                    <span className="vg-variant-chip-score">
                      {entry.candidate.overall_score?.toFixed(2) ?? "—"}
                    </span>
                  </button>
                ))}
              </div>
            ) : null}
            <div className="grid items-start gap-x-5 gap-y-4 [grid-template-columns:minmax(0,1.28fr)_minmax(22rem,0.92fr)] max-[1180px]:grid-cols-1 max-[860px]:gap-3">
              <div className="vg-detail-image-frame min-h-[clamp(14rem,46vh,28rem)] overflow-hidden">
                <div className="vg-chart-canvas is-detail grid min-h-[clamp(14rem,46vh,28rem)] h-full w-full place-items-start overflow-hidden px-[0.28rem] pb-[0.14rem] pt-[0.44rem]">
                  {candidate.error ? (
                    <p className="m-0 text-destructive">{candidate.error}</p>
                  ) : (
                    renderImage(
                      candidate.image_url || null,
                      label,
                      candidate.image_meta || null,
                      "detail",
                    )
                  )}
                </div>
              </div>
              <div className="grid content-start gap-3">
                <div className="font-mono text-[0.68rem] font-semibold uppercase tracking-[0.05em] text-muted-foreground">
                  Scores
                </div>
                <ScoreBreakdownList candidate={candidate} mode="detail" />
                <div className="flex flex-wrap gap-1.5">
                  {variant.variant_label ? (
                    <Badge
                      className="rounded-[3px] border-border bg-muted font-mono text-[0.62rem] leading-[1.1] text-muted-foreground"
                      variant="outline"
                    >
                      {variant.variant_label}
                    </Badge>
                  ) : null}
                </div>
              </div>
            </div>
            {candidate.guideline_details.length > 0 ? (
              <section className="grid gap-2 pt-px">
                <Separator className="mb-px" />
                <div className="font-mono text-[0.68rem] font-semibold uppercase tracking-[0.05em] text-muted-foreground">
                  {`Guidelines used (${candidate.guideline_details.length})`}
                </div>
                <div className="grid items-stretch gap-x-2 gap-y-2 [grid-template-columns:repeat(3,minmax(0,1fr))] max-[1120px]:[grid-template-columns:repeat(2,minmax(0,1fr))] max-[980px]:grid-cols-1">
                  {candidate.guideline_details.map((guideline) => (
                    <GuidelineCard guideline={guideline} key={guideline.id} />
                  ))}
                </div>
              </section>
            ) : null}
          </section>
        </div>
      </aside>
    </section>
  );
}

function GuidelineCard({ guideline }: { guideline: CandidateGuidelineDetail }) {
  const href = safeGuidelineHref(guideline.url);

  return (
    <article className="grid h-full grid-rows-[auto_auto_1fr_auto] gap-px border border-border border-l-[3px] border-l-foreground/70 bg-muted px-2.5 py-2.5">
      {href ? (
        <a
          className="text-[0.78rem] font-bold leading-[1.35] text-foreground underline-offset-2 hover:underline focus-visible:underline"
          href={href}
          rel="noopener noreferrer"
          target="_blank"
        >
          {guideline.title}
        </a>
      ) : (
        <div className="text-[0.78rem] font-bold leading-[1.35] text-foreground">
          {guideline.title}
        </div>
      )}
      {guideline.description ? (
        <p className="m-0 overflow-hidden text-[0.7rem] leading-[1.42] text-muted-foreground [display:-webkit-box] [-webkit-box-orient:vertical] [-webkit-line-clamp:3]">
          {guideline.description}
        </p>
      ) : null}
      {guideline.sources.length > 0 ? (
        <div className="grid gap-px border-t border-border pt-1">
          <div className="font-mono text-[0.58rem] font-bold uppercase tracking-[0.08em] text-muted-foreground">
            Sources
          </div>
          <p className="m-0 overflow-wrap-anywhere font-mono text-[0.62rem] leading-[1.42] text-muted-foreground [overflow-wrap:anywhere]">
            {guideline.sources.join("; ")}
          </p>
        </div>
      ) : null}
    </article>
  );
}

export function safeGuidelineHref(url: string | null | undefined): string | null {
  const raw = url?.trim();
  if (!raw) {
    return null;
  }

  try {
    const base = typeof window === "undefined" ? "http://localhost" : window.location.origin;
    const parsed = new URL(raw, base);
    if (parsed.protocol !== "http:" && parsed.protocol !== "https:") {
      return null;
    }
    return raw;
  } catch {
    return null;
  }
}
