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
import type { CandidateRecord, CandidateScore } from "@/viewer/contract/types";
import { formatMetricScore, formatScore } from "@/viewer/render/utils";

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
    <div className={clsx("vg-score-breakdown-reasoning", open && "is-open")}>
      <button
        aria-expanded={open}
        aria-haspopup="dialog"
        className="vg-score-breakdown-reasoning-button"
        ref={refs.setReference}
        type="button"
        {...getReferenceProps({
          onClick: togglePopover,
        })}
      >
        <span>{entries.length === 1 ? "1 reason" : `${entries.length} reasons`}</span>
        <ChevronDown
          aria-hidden
          className="vg-score-breakdown-reasoning-button-icon"
          strokeWidth={1.8}
        />
      </button>
      {open ? (
        <FloatingFocusManager context={context} initialFocus={popoverRef} modal={false} returnFocus>
          <div
            aria-label={`${score.label} judge reasoning`}
            className="vg-score-breakdown-reasoning-popover"
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
            <div className="vg-score-breakdown-reasoning-popover-head">
              <span className="vg-score-breakdown-reasoning-popover-kicker">Judge reasoning</span>
              <div className="vg-score-breakdown-reasoning-popover-nav">
                {hasMultipleEntries ? (
                  <>
                    <button
                      aria-label="Previous trace"
                      className="vg-score-breakdown-reasoning-nav-button"
                      onClick={showPreviousEntry}
                      type="button"
                    >
                      <ChevronLeft aria-hidden strokeWidth={1.8} />
                    </button>
                    <span className="vg-score-breakdown-reasoning-popover-count">
                      {`${pageIndex + 1} / ${entries.length}`}
                    </span>
                    <button
                      aria-label="Next trace"
                      className="vg-score-breakdown-reasoning-nav-button"
                      onClick={showNextEntry}
                      type="button"
                    >
                      <ChevronRight aria-hidden strokeWidth={1.8} />
                    </button>
                  </>
                ) : (
                  <span className="vg-score-breakdown-reasoning-popover-count">1 / 1</span>
                )}
              </div>
            </div>
            <div className="vg-score-breakdown-reasoning-popover-body">
              <div className="vg-score-breakdown-reasoning-run-meta">
                <span className="vg-score-breakdown-reasoning-run-value">{`Rating: ${entryValue}`}</span>
              </div>
              <p className="vg-score-breakdown-reasoning-run-copy">{entry.reasoning}</p>
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
  const classes = clsx("vg-score-item", `is-${mode}`, `is-${variant}`);
  const showLabel = mode === "floating";

  return (
    <span aria-label={`${score.label}: ${value ?? "—"}`} className={classes}>
      <Icon aria-hidden className="vg-score-item-icon" strokeWidth={1.75} />
      {showLabel ? <span className="vg-score-item-label">{score.label}</span> : null}
      <span className="vg-score-item-value">{value ?? "—"}</span>
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
    <div aria-label={tooltip} className={clsx("vg-score-ledger", `is-${mode}`)} title={tooltip}>
      {overall ? (
        <div className="vg-score-ledger-overall">
          <ScoreItem mode={mode} score={overall} variant="overall" />
        </div>
      ) : null}
      {showDivider ? <span aria-hidden className="vg-score-ledger-divider" /> : null}
      {showSubscores ? (
        <div className="vg-score-ledger-subscores">
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
    <div className={clsx("vg-score-breakdown-list", `is-${mode}`)}>
      {mode === "detail" && sharedReasoningNote ? (
        <div className="vg-score-breakdown-note">
          {summarizeSharedReasoning(sharedReasoningNote)}
        </div>
      ) : null}
      {scores.map((score) => {
        const Icon = ICONS_BY_SCORE_ID[score.id] ?? Sigma;
        const value = formatScoreValue(score);
        const reasoningEntries = mode === "detail" ? collectReasoningEntries(score) : [];
        return (
          <div
            className={clsx("vg-score-breakdown-item", score.id === "overall" && "is-overall")}
            key={`${candidate.visgen_id}:${score.id}`}
          >
            <div className="vg-score-breakdown-item-head">
              <span className="vg-score-breakdown-item-heading">
                <Icon aria-hidden className="vg-score-breakdown-item-icon" strokeWidth={1.75} />
                <span className="vg-score-breakdown-item-label">{score.label}</span>
              </span>
              <span className="vg-score-breakdown-item-value">{value ?? "—"}</span>
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
