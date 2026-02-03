import { LikertScale } from "@chartcoach/eval-ui/components/likert-scale";
import { upsertSetRating, type ScenarioSetRating } from "@chartcoach/eval-ui/db-collections";

const SUFFICIENCY = [
  { value: 1, label: "Insufficient" },
  { value: 2, label: "Weak" },
  { value: 3, label: "Okay" },
  { value: 4, label: "Strong" },
  { value: 5, label: "Sufficient" },
];

const REDUNDANCY = [
  { value: 1, label: "Very redundant" },
  { value: 2, label: "Redundant" },
  { value: 3, label: "Mixed" },
  { value: 4, label: "Mostly non-redundant" },
  { value: 5, label: "Non-redundant" },
];

const COHERENCE = [
  { value: 1, label: "Incoherent" },
  { value: 2, label: "Somewhat incoherent" },
  { value: 3, label: "Mixed" },
  { value: 4, label: "Coherent" },
  { value: 5, label: "Very coherent" },
];

const HARM = [
  { value: 1, label: "Risky/harmful" },
  { value: 2, label: "Some risk" },
  { value: 3, label: "Unclear" },
  { value: 4, label: "Mostly safe" },
  { value: 5, label: "Safe" },
];

export function SetRatingPanel({
  scenarioId,
  strategyId,
  rating,
}: {
  scenarioId: string;
  strategyId: string;
  rating: ScenarioSetRating | undefined;
}) {
  function patch(p: Partial<Omit<ScenarioSetRating, "id" | "scenarioId" | "strategyId" | "createdAt" | "updatedAt">>) {
    upsertSetRating({
      scenarioId,
      strategyId,
      patch: p,
    });
  }

  return (
    <section className="mt-6 rounded-xl border bg-card p-4">
      <div className="flex flex-wrap items-baseline justify-between gap-2">
        <h2 className="text-sm font-semibold">Set-level rating</h2>
        <div className="text-xs text-muted-foreground">
          Strategy: <span className="font-mono">{strategyId}</span>
        </div>
      </div>

      <div className="mt-4 grid gap-4 md:grid-cols-2">
        <div className="space-y-1">
          <div className="text-xs font-medium text-muted-foreground">Sufficiency</div>
          <LikertScale
            name={`set-sufficiency:${scenarioId}:${strategyId}`}
            value={rating?.sufficiency}
            onChange={(next) => patch({ sufficiency: next })}
            options={SUFFICIENCY}
            ariaLabel="Set sufficiency rating"
          />
        </div>

        <div className="space-y-1">
          <div className="text-xs font-medium text-muted-foreground">Harm / risk</div>
          <LikertScale
            name={`set-harm:${scenarioId}:${strategyId}`}
            value={rating?.harm}
            onChange={(next) => patch({ harm: next })}
            options={HARM}
            ariaLabel="Set harm rating"
          />
        </div>

        <div className="space-y-1">
          <div className="text-xs font-medium text-muted-foreground">Redundancy</div>
          <LikertScale
            name={`set-redundancy:${scenarioId}:${strategyId}`}
            value={rating?.redundancy}
            onChange={(next) => patch({ redundancy: next })}
            options={REDUNDANCY}
            ariaLabel="Set redundancy rating"
          />
        </div>

        <div className="space-y-1">
          <div className="text-xs font-medium text-muted-foreground">Coherence</div>
          <LikertScale
            name={`set-coherence:${scenarioId}:${strategyId}`}
            value={rating?.coherence}
            onChange={(next) => patch({ coherence: next })}
            options={COHERENCE}
            ariaLabel="Set coherence rating"
          />
        </div>
      </div>

      <div className="mt-4 space-y-2">
        <div className="flex items-center justify-between gap-2">
          <div className="text-xs font-medium text-muted-foreground">Notes</div>
          <div className="text-[11px] text-muted-foreground">
            Optional; short, set-level impressions.
          </div>
        </div>
        <textarea
          className="min-h-24 w-full resize-y rounded-md border bg-background p-2 text-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
          value={rating?.notes ?? ""}
          placeholder="e.g., strong coverage of accessibility + labeling, but misses chart-type specific advice…"
          onChange={(event) => {
            const text = event.currentTarget.value;
            patch({ notes: text.trim() ? text : undefined });
          }}
        />
      </div>
    </section>
  );
}
