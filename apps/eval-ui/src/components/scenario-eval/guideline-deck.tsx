import type { RelevanceRating } from "@chartcoach/eval-ui/db-collections";
import type { EvalGuidelineResult } from "@chartcoach/eval-ui/eval/schemas";
import { cn } from "@chartcoach/eval-ui/lib/utils";

import { GuidelineCard } from "../guideline-card";

type GuidelineDeckProps = {
  scenarioId: string;
  guidelines: EvalGuidelineResult[];
  activeGuidelineId: string | undefined;
  getRating: (guidelineId: string) => RelevanceRating | undefined;
  onRate: (guidelineId: string, relevance: number) => void;
  onClear: (guidelineId: string) => void;
  className?: string;
};

export function GuidelineDeck({
  scenarioId,
  guidelines,
  activeGuidelineId,
  getRating,
  onRate,
  onClear,
  className,
}: GuidelineDeckProps) {
  return (
    <ul
      aria-label="Guidelines"
      className={cn(
        "mt-4 -mx-4 flex touch-pan-x snap-x snap-mandatory gap-4 overflow-x-auto px-4 pb-4 scroll-px-4 [scrollbar-gutter:stable]",
        "lg:mx-0 lg:grid lg:grid-cols-1 lg:gap-4 lg:overflow-visible lg:px-0 lg:pb-0 lg:snap-none lg:scroll-px-0",
        "[@media(min-width:2400px)]:grid-cols-2",
        className,
      )}
    >
      {guidelines.map((g) => (
        <li
          key={g.entry.guideline.id}
          className="min-w-0 shrink-0 snap-start snap-always w-[min(560px,calc(100%-2rem))] lg:w-auto lg:shrink lg:snap-none"
        >
          <GuidelineCard
            scenarioId={scenarioId}
            result={g}
            rating={getRating(g.entry.guideline.id)?.relevance}
            isActive={g.entry.guideline.id === activeGuidelineId}
            onRate={onRate}
            onClear={onClear}
          />
        </li>
      ))}
    </ul>
  );
}
