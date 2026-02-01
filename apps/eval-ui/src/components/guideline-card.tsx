import { GuidelineCard as GuidelineCardShell, type GuidelineCardLabel } from "@chartcoach/ui";

import type { GuidelineRating } from "@chartcoach/eval-ui/db-collections";
import type { EvalGuidelineResult } from "@chartcoach/eval-ui/eval/schemas";
import { getGuidelineDetailHref } from "@chartcoach/eval-ui/lib/eval-utils";
import { cn } from "@chartcoach/eval-ui/lib/utils";

import { BucketScale } from "./bucket-scale";
import { LikertScale } from "./likert-scale";

type GuidelineRatingPatch = Partial<
  Omit<GuidelineRating, "id" | "scenarioId" | "guidelineId" | "createdAt" | "updatedAt">
>;

type GuidelineCardProps = {
  scenarioId: string;
  result: EvalGuidelineResult;
  rating: GuidelineRating | undefined;
  isActive?: boolean;
  onRate: (guidelineId: string, patch: GuidelineRatingPatch) => void;
  onClear: (guidelineId: string) => void;
};

const actionabilityOptions = [
  { value: 1, label: "Not actionable" },
  { value: 2, label: "Hard to apply" },
  { value: 3, label: "Somewhat actionable" },
  { value: 4, label: "Actionable" },
  { value: 5, label: "Immediately actionable" },
];

const impactOptions = [
  { value: 1, label: "No impact" },
  { value: 2, label: "Low impact" },
  { value: 3, label: "Moderate impact" },
  { value: 4, label: "High impact" },
  { value: 5, label: "Very high impact" },
];

const riskOptions = [
  { value: 1, label: "No risk" },
  { value: 2, label: "Low risk" },
  { value: 3, label: "Moderate risk" },
  { value: 4, label: "High risk" },
  { value: 5, label: "Very high risk" },
];

const credibilityOptions = [
  { value: 1, label: "Low credibility" },
  { value: 2, label: "Some credibility" },
  { value: 3, label: "Moderate credibility" },
  { value: 4, label: "High credibility" },
  { value: 5, label: "Very high credibility" },
];

export function GuidelineCard({
  scenarioId,
  result,
  rating,
  isActive,
  onRate,
  onClear,
}: GuidelineCardProps) {
  const g = result.entry.guideline;
  const guidelineId = g.id;
  const detailHref = getGuidelineDetailHref(guidelineId);
  const domId = `guideline-${encodeURIComponent(guidelineId)}`;

  const bucket = rating?.bucket;
  const dimensionsDisabled = !bucket || bucket === "not_applicable";
  const notesDisabled = !bucket;

  function handleBucketChange(next: GuidelineRating["bucket"] | undefined) {
    if (next === undefined) {
      onClear(guidelineId);
      return;
    }

    const patch: GuidelineRatingPatch = { bucket: next };
    if (next === "not_applicable") {
      patch.actionability = undefined;
      patch.impact = undefined;
      patch.risk = undefined;
      patch.credibility = undefined;
    }
    onRate(guidelineId, patch);
  }

  const labelsShown = g.labels.slice(0, 4);
  const labelsRemaining = Math.max(0, g.labels.length - labelsShown.length);
  const labels: GuidelineCardLabel[] = labelsShown.map((label) => ({
    value: { text: label },
  }));

  return (
    <div
      id={domId}
      className={cn(
        "eval-guideline-card",
        "relative",
        "rounded-[calc(var(--radius)+2px)]",
        "scroll-mt-6",
        detailHref ? "cursor-pointer" : null,
        isActive ? "bg-muted/30" : "bg-transparent",
      )}
    >
      {detailHref ? (
        <a
          href={detailHref}
          target="_blank"
          rel="noopener noreferrer"
          aria-label={`Open guideline: ${g.title}`}
          className="absolute inset-0 z-10 rounded-[calc(var(--radius)+2px)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
        />
      ) : null}

      <GuidelineCardShell
        as="article"
        title={<span className="whitespace-normal">{g.title}</span>}
        description={
          g.description ? <span className="whitespace-normal">{g.description}</span> : undefined
        }
        labels={labels}
        labelsRemaining={labelsRemaining || undefined}
        meta={
          <>
            <span className="tabular-nums">#{result.rank}</span>
          </>
        }
      >
        <div className="relative z-20 mt-3 w-full space-y-4">
          <div className="flex items-start justify-between gap-3">
            <div className="min-w-0">
              <div className="text-xs font-semibold">Bucket</div>
              <div className="text-[11px] text-muted-foreground">
                Pick the primary label. Optional dimensions come next.
              </div>
            </div>
            {bucket ? (
              <button
                type="button"
                onClick={() => onClear(guidelineId)}
                className="shrink-0 rounded-md border px-2 py-1 text-xs text-muted-foreground hover:bg-muted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
              >
                Clear
              </button>
            ) : null}
          </div>

          <BucketScale
            name={`bucket:${scenarioId}:${guidelineId}`}
            value={bucket}
            onChange={handleBucketChange}
          />

          <div className="grid gap-4 sm:grid-cols-2">
            <div className="space-y-1">
              <div className="text-xs font-semibold">Actionability</div>
              <LikertScale
                name={`actionability:${scenarioId}:${guidelineId}`}
                value={rating?.actionability}
                options={actionabilityOptions}
                ariaLabel="Actionability (1-5)"
                disabled={dimensionsDisabled}
                onChange={(next) => {
                  if (!bucket) return;
                  onRate(guidelineId, { actionability: next });
                }}
              />
            </div>

            <div className="space-y-1">
              <div className="text-xs font-semibold">Impact</div>
              <LikertScale
                name={`impact:${scenarioId}:${guidelineId}`}
                value={rating?.impact}
                options={impactOptions}
                ariaLabel="Impact (1-5)"
                disabled={dimensionsDisabled}
                onChange={(next) => {
                  if (!bucket) return;
                  onRate(guidelineId, { impact: next });
                }}
              />
            </div>

            <div className="space-y-1">
              <div className="text-xs font-semibold">Risk / harm</div>
              <LikertScale
                name={`risk:${scenarioId}:${guidelineId}`}
                value={rating?.risk}
                options={riskOptions}
                ariaLabel="Risk (1-5)"
                disabled={dimensionsDisabled}
                onChange={(next) => {
                  if (!bucket) return;
                  onRate(guidelineId, { risk: next });
                }}
              />
            </div>

            <div className="space-y-1">
              <div className="text-xs font-semibold">Credibility</div>
              <LikertScale
                name={`credibility:${scenarioId}:${guidelineId}`}
                value={rating?.credibility}
                options={credibilityOptions}
                ariaLabel="Credibility (1-5)"
                disabled={dimensionsDisabled}
                onChange={(next) => {
                  if (!bucket) return;
                  onRate(guidelineId, { credibility: next });
                }}
              />
            </div>
          </div>

          <div className="space-y-1">
            <label
              htmlFor={`notes:${scenarioId}:${guidelineId}`}
              className="text-xs font-semibold"
            >
              Notes (optional)
            </label>
            <textarea
              id={`notes:${scenarioId}:${guidelineId}`}
              value={rating?.notes ?? ""}
              disabled={notesDisabled}
              placeholder={notesDisabled ? "Set a bucket first." : "Any nuance to remember?"}
              rows={3}
              onChange={(event) => {
                if (!bucket) return;
                const next = event.currentTarget.value;
                onRate(guidelineId, { notes: next.trim() ? next : undefined });
              }}
              className={cn(
                "w-full rounded-md border bg-background px-3 py-2 text-sm leading-relaxed shadow-sm",
                "placeholder:text-muted-foreground/70",
                "focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60",
                notesDisabled ? "cursor-not-allowed opacity-60" : null,
              )}
            />
          </div>
        </div>
      </GuidelineCardShell>
    </div>
  );
}
