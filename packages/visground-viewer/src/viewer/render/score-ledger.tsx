import {
  BookOpenCheck,
  LayoutGrid,
  Lightbulb,
  Palette,
  PenTool,
  Scale,
  Sigma,
  type LucideIcon,
} from "lucide-react";
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
  const classes = ["vg-score-item", `is-${mode}`, `is-${variant}`].filter(Boolean).join(" ");
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
  const scores = SCORE_ORDER.map((scoreId) => getScoreById(candidate, scoreId)).filter(
    (score): score is CandidateScore => Boolean(score),
  );
  if (scores.length === 0) {
    return null;
  }

  const overall = scores.find((score) => score.id === "overall") ?? null;
  const subscores = scores.filter((score) => score.id !== "overall");
  const showSubscores = subscores.length > 0;
  const showDivider = mode === "matrix" && overall && showSubscores;
  const tooltip = buildScoreTooltip(scores);

  return (
    <div aria-label={tooltip} className={`vg-score-ledger is-${mode}`.trim()} title={tooltip}>
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
