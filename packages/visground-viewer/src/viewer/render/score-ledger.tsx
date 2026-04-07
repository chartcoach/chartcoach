import {
  FloatingFocusManager,
  autoUpdate,
  flip,
  offset,
  shift,
  useDismiss,
  useFloating,
  useInteractions,
} from "@floating-ui/react";
import clsx from "clsx";
import {
  BookOpenCheck,
  ChevronDown,
  ChevronLeft,
  ChevronRight,
  LayoutGrid,
  Lightbulb,
  Palette,
  PenTool,
  Scale,
  Sigma,
  type LucideIcon,
} from "lucide-react";
import { useRef, useState, type KeyboardEvent as ReactKeyboardEvent } from "react";
import type { CandidateRecord, CandidateScore } from "../contract/types";
import { formatMetricScore, formatScore } from "./utils";

const SCORE_ORDER = [
  "overall",
  "data_fidelity",
  "semantic_readability",
  "insight_discovery",
  "design_style",
  "visual_composition",
  "color_harmony",
] as const;

const ICONS_BY_SCORE_ID: Record<string, LucideIcon> = {
  overall: Sigma,
  data_fidelity: Scale,
  semantic_readability: BookOpenCheck,
  insight_discovery: Lightbulb,
  design_style: PenTool,
  visual_composition: LayoutGrid,
  color_harmony: Palette,
};

function getScoreById(candidate: CandidateRecord, scoreId: string): CandidateScore | null {
  return candidate.score_breakdown.find((item) => item.id === scoreId) ?? null;
}

function formatScoreValue(score: CandidateScore) {
  return score.id === "overall" ? formatScore(score.score) : formatMetricScore(score.score);
}

function buildScoreTooltip(scores: CandidateScore[]) {
  return scores.map((score) => `${score.label}: ${formatScoreValue(score) ?? "—"}`).join("\n");
}

function orderedScores(candidate: CandidateRecord) {
  return SCORE_ORDER.map((scoreId) => getScoreById(candidate, scoreId)).filter(
    (score): score is CandidateScore => Boolean(score),
  );
}

function sharedReasoning(scores: CandidateScore[]) {
  const runCounts = scores
    .filter((score) => score.id !== "overall")
    .map((score) => score.runs.filter((run) => run.reasoning).length)
    .filter((count) => count > 0);
  if (!runCounts.length) {
    return null;
  }
  const unique = Array.from(new Set(runCounts));
  return unique.length === 1 ? unique[0] : null;
}

function summarizeSharedReasoning(runCount: number | null) {
  if (!runCount) {
    return null;
  }
  return `Average of ${runCount} runs.`;
}

type ReasoningEntry = {
  entry_id: string;
  label: string;
  score: number | null;
  reasoning: string;
};

function collectReasoningEntries(score: CandidateScore): ReasoningEntry[] {
  const runEntries = score.runs
    .filter((run) => Boolean(run.reasoning))
    .map((run) => ({
      entry_id: run.run_id,
      label: run.label,
      score: run.score,
      reasoning: run.reasoning ?? "",
    }));

  if (runEntries.length > 0) {
    return runEntries;
  }

  if (!score.reasoning) {
    return [];
  }

  return [
    {
      entry_id: `${score.id}-summary`,
      label: "Summary",
      score: score.score,
      reasoning: score.reasoning,
    },
  ];
}

function ScoreReasoningPopover({
  score,
  entries,
}: {
  score: CandidateScore;
  entries: ReasoningEntry[];
}) {
  const [open, setOpen] = useState(false);
  const [pageIndex, setPageIndex] = useState(0);
  const popoverRef = useRef<HTMLDivElement | null>(null);
  const entry = entries[pageIndex] ?? entries[0] ?? null;
  const { refs, floatingStyles, context } = useFloating({
    open,
    onOpenChange: setOpen,
    placement: "bottom-start",
    strategy: "fixed",
    whileElementsMounted: autoUpdate,
    middleware: [offset(8), flip({ padding: 12 }), shift({ padding: 12 })],
  });
  const dismiss = useDismiss(context);
  const { getReferenceProps, getFloatingProps } = useInteractions([dismiss]);

  if (!entry) {
    return null;
  }

  const entryValue =
    entry.score === null ? "—" : formatScoreValue({ ...score, score: entry.score });
  const hasMultipleEntries = entries.length > 1;

  function openPopover() {
    setPageIndex(0);
    setOpen(true);
  }

  function closePopover() {
    setOpen(false);
  }

  function togglePopover() {
    if (open) {
      closePopover();
      return;
    }
    openPopover();
  }

  function showPreviousEntry() {
    setPageIndex((current) => (current - 1 + entries.length) % entries.length);
  }

  function showNextEntry() {
    setPageIndex((current) => (current + 1) % entries.length);
  }

  function handlePopoverKeyDown(event: ReactKeyboardEvent<HTMLDivElement>) {
    if (event.key === "Escape") {
      event.preventDefault();
      event.stopPropagation();
      closePopover();
      return;
    }
    if (!entries.length) {
      return;
    }
    if (event.key === "ArrowLeft") {
      event.preventDefault();
      event.stopPropagation();
      showPreviousEntry();
    }
    if (event.key === "ArrowRight") {
      event.preventDefault();
      event.stopPropagation();
      showNextEntry();
    }
  }

  return (
    <div className={clsx("relative grid w-full justify-items-start", open && "is-open")}>
      <button
        aria-expanded={open}
        aria-haspopup="dialog"
        className={clsx(
          "inline-flex min-h-0 items-center gap-1 border-0 bg-transparent p-0 font-mono text-[0.62rem] leading-[1.25] tracking-[0.02em] text-muted-foreground opacity-90 transition-colors hover:text-foreground",
          open && "text-foreground/80",
        )}
        ref={refs.setReference}
        type="button"
        {...getReferenceProps({
          onClick: togglePopover,
        })}
      >
        <span>{entries.length === 1 ? "1 reason" : `${entries.length} reasons`}</span>
        <ChevronDown
          aria-hidden
          className={clsx("size-[0.82rem] transition-transform duration-150", open && "rotate-180")}
          strokeWidth={1.8}
        />
      </button>
      {open ? (
        <FloatingFocusManager context={context} initialFocus={popoverRef} modal={false} returnFocus>
          <div
            aria-label={`${score.label} judge reasoning`}
            className="z-10 grid w-[min(100%,23rem)] max-w-[calc(100vw-8rem)] gap-2 border border-border bg-background px-3 py-3 shadow-[var(--ccui-shadow)] max-[980px]:max-w-[calc(100vw-3rem)]"
            role="dialog"
            style={floatingStyles}
            tabIndex={-1}
            {...getFloatingProps({
              onKeyDown: handlePopoverKeyDown,
              onPointerDown(event) {
                event.stopPropagation();
              },
            })}
            ref={(node) => {
              popoverRef.current = node;
              refs.setFloating(node);
            }}
          >
            <div className="grid grid-cols-[minmax(0,1fr)_auto] items-center gap-2">
              <span className="font-mono text-[0.62rem] font-bold uppercase tracking-[0.08em] text-muted-foreground">
                Judge reasoning
              </span>
              <div className="inline-flex items-center gap-1">
                {hasMultipleEntries ? (
                  <>
                    <button
                      aria-label="Previous trace"
                      className="inline-flex size-[1.4rem] items-center justify-center border border-border/60 bg-muted text-muted-foreground transition-colors hover:text-foreground"
                      onClick={showPreviousEntry}
                      type="button"
                    >
                      <ChevronLeft aria-hidden strokeWidth={1.8} />
                    </button>
                    <span className="font-mono text-[0.62rem] text-muted-foreground">
                      {`${pageIndex + 1} / ${entries.length}`}
                    </span>
                    <button
                      aria-label="Next trace"
                      className="inline-flex size-[1.4rem] items-center justify-center border border-border/60 bg-muted text-muted-foreground transition-colors hover:text-foreground"
                      onClick={showNextEntry}
                      type="button"
                    >
                      <ChevronRight aria-hidden strokeWidth={1.8} />
                    </button>
                  </>
                ) : (
                  <span className="font-mono text-[0.62rem] text-muted-foreground">1 / 1</span>
                )}
              </div>
            </div>
            <div className="grid gap-1 border-t border-border/60 pt-1">
              <div className="flex justify-end">
                <span className="font-mono text-[0.64rem] text-foreground">{`Rating: ${entryValue}`}</span>
              </div>
              <p className="m-0 text-[0.72rem] leading-[1.52] text-muted-foreground">
                {entry.reasoning}
              </p>
            </div>
          </div>
        </FloatingFocusManager>
      ) : null}
    </div>
  );
}

function ScoreItem({
  score,
  mode,
  variant,
}: {
  score: CandidateScore;
  mode: "matrix" | "floating";
  variant: "overall" | "subscore";
}) {
  const Icon = ICONS_BY_SCORE_ID[score.id] ?? Sigma;
  const value = formatScoreValue(score);
  const showLabel = mode === "floating";
  const wrapperClass =
    mode === "matrix"
      ? variant === "overall"
        ? "inline-grid grid-cols-[auto_minmax(3.2ch,auto)] items-center gap-[0.16rem] font-mono text-[calc(var(--vg-score-font-size,0.56rem)+0.1rem)] font-extrabold leading-none text-foreground"
        : "inline-grid grid-cols-[var(--vg-score-icon-size,0.72rem)_minmax(2.1ch,auto)] items-center gap-[0.16rem] font-mono text-[calc(var(--vg-score-font-size,0.56rem)+0.02rem)] leading-none text-muted-foreground"
      : clsx(
          "grid w-full min-w-0 items-center gap-x-1.5 leading-[1.15]",
          variant === "overall"
            ? "grid-cols-[auto_auto] text-[0.8rem] font-extrabold text-foreground"
            : "grid-cols-[auto_minmax(0,1fr)_auto] text-[0.64rem] text-muted-foreground",
        );
  const iconClass = clsx(
    "shrink-0",
    mode === "matrix" ? "size-[var(--vg-score-icon-size,0.72rem)]" : "size-[0.92rem]",
    variant === "subscore" && "opacity-75",
  );
  const valueClass =
    mode === "matrix"
      ? variant === "overall"
        ? "inline-flex min-w-[3.2ch] items-center justify-end text-right"
        : "inline-flex min-w-[2.1ch] items-center justify-end text-right"
      : "justify-self-end text-right";

  return (
    <span aria-label={`${score.label}: ${value ?? "—"}`} className={wrapperClass}>
      <Icon aria-hidden className={iconClass} strokeWidth={1.75} />
      {showLabel ? <span className="min-w-0">{score.label}</span> : null}
      <span className={valueClass}>{value ?? "—"}</span>
    </span>
  );
}

export function ScoreLedger({
  candidate,
  mode,
}: {
  candidate: CandidateRecord;
  mode: "matrix" | "floating";
}) {
  const scores = orderedScores(candidate);
  if (scores.length === 0) {
    return null;
  }

  const overall = scores.find((score) => score.id === "overall") ?? null;
  const subscores = scores.filter((score) => score.id !== "overall");
  const showSubscores = subscores.length > 0;
  const showDivider = mode === "matrix" && overall && showSubscores;
  const tooltip = buildScoreTooltip(scores);

  return (
    <div
      aria-label={tooltip}
      className={clsx(
        "min-w-0",
        mode === "matrix"
          ? "flex w-full items-center gap-[0.42rem] whitespace-nowrap pt-[0.22rem]"
          : "grid w-full items-start gap-[0.42rem] whitespace-normal",
      )}
      title={tooltip}
    >
      {overall ? (
        <div className={clsx(mode === "floating" && "w-full")}>
          <ScoreItem mode={mode} score={overall} variant="overall" />
        </div>
      ) : null}
      {showDivider ? (
        <span
          aria-hidden
          className="mx-[0.04rem] my-0 h-[0.92rem] w-px shrink-0 bg-[var(--vg-divider)] opacity-60"
        />
      ) : null}
      {showSubscores ? (
        <div
          className={clsx(
            mode === "matrix"
              ? "grid min-w-0 auto-cols-max grid-flow-col items-center gap-[0.34rem]"
              : "grid items-start gap-x-3 gap-y-2 whitespace-normal [grid-template-columns:repeat(2,minmax(0,1fr))]",
          )}
        >
          {subscores.map((score) => (
            <ScoreItem key={score.id} mode={mode} score={score} variant="subscore" />
          ))}
        </div>
      ) : null}
    </div>
  );
}

export function ScoreBreakdownList({
  candidate,
  mode,
}: {
  candidate: CandidateRecord;
  mode: "compact" | "detail";
}) {
  const scores = orderedScores(candidate);
  if (scores.length === 0) {
    return null;
  }
  const sharedReasoningNote = mode === "detail" ? sharedReasoning(scores) : null;

  return (
    <div
      className={clsx(
        "grid w-full gap-2",
        mode === "detail" &&
          "[grid-template-columns:repeat(2,minmax(0,1fr))] items-start gap-x-3 gap-y-2.5",
      )}
    >
      {mode === "detail" && sharedReasoningNote ? (
        <div className="col-span-full px-0.5 pt-px font-mono text-[0.72rem] leading-[1.4] text-muted-foreground">
          {summarizeSharedReasoning(sharedReasoningNote)}
        </div>
      ) : null}
      {scores.map((score) => {
        const Icon = ICONS_BY_SCORE_ID[score.id] ?? Sigma;
        const value = formatScoreValue(score);
        const reasoningEntries = mode === "detail" ? collectReasoningEntries(score) : [];
        return (
          <div
            className={clsx(
              "relative grid gap-1.5 overflow-visible border border-border bg-[color:color-mix(in_srgb,var(--ccui-paper)_92%,var(--ccui-panel))] px-3 py-2.5",
              score.id === "overall" &&
                "col-span-full border-l-[3px] border-l-foreground/70 bg-muted [border-color:color-mix(in_srgb,var(--ccui-border-strong)_18%,var(--ccui-border))]",
            )}
            key={`${candidate.visgen_id}:${score.id}`}
          >
            <div className="grid grid-cols-[minmax(0,1fr)_auto] items-baseline gap-3">
              <span className="inline-grid min-w-0 grid-cols-[auto_minmax(0,1fr)] items-baseline gap-2">
                <Icon
                  aria-hidden
                  className="size-[0.84rem] self-center text-muted-foreground"
                  strokeWidth={1.75}
                />
                <span
                  className={clsx(
                    "min-w-0 font-mono text-[0.74rem] leading-[1.3] text-foreground",
                    score.id === "overall" && "text-[0.94rem] font-semibold",
                  )}
                >
                  {score.label}
                </span>
              </span>
              <span
                className={clsx(
                  "text-right font-mono text-[0.82rem] font-bold text-foreground",
                  score.id === "overall" && "text-[0.94rem]",
                )}
              >
                {value ?? "—"}
              </span>
            </div>
            {mode === "detail" && reasoningEntries.length > 0 ? (
              <ScoreReasoningPopover entries={reasoningEntries} score={score} />
            ) : null}
          </div>
        );
      })}
    </div>
  );
}
