import { GuidelineCard as GuidelineCardShell, type GuidelineCardLabel } from '@chartcoach/ui'

import type { EvalGuidelineResult } from '@chartcoach/eval-ui/eval/types'
import { getGuidelineDetailHref } from '@chartcoach/eval-ui/eval/guideline-detail-url'
import { cn } from '@chartcoach/eval-ui/lib/utils'

import { LikertScale } from './likert-scale'

type GuidelineCardProps = {
  scenarioId: string
  result: EvalGuidelineResult
  rating: number | undefined
  isActive?: boolean
  onRate: (guidelineId: string, next: number) => void
  onClear: (guidelineId: string) => void
}

export function GuidelineCard({
  scenarioId,
  result,
  rating,
  isActive,
  onRate,
  onClear,
}: GuidelineCardProps) {
  const g = result.entry.guideline
  const guidelineId = g.id
  const detailHref = getGuidelineDetailHref(guidelineId)
  const domId = `guideline-${encodeURIComponent(guidelineId)}`

  function handleChange(next: number | undefined) {
    if (next === undefined) {
      onClear(guidelineId)
      return
    }
    onRate(guidelineId, next)
  }

  const labelsShown = g.labels.slice(0, 4)
  const labelsRemaining = Math.max(0, g.labels.length - labelsShown.length)
  const labels: GuidelineCardLabel[] = labelsShown.map((label) => ({
    value: { text: label },
  }))

  return (
    <div
      id={domId}
      className={cn(
        'eval-guideline-card',
        'relative',
        'rounded-[calc(var(--radius)+2px)]',
        'scroll-mt-6',
        detailHref ? 'cursor-pointer' : null,
        isActive ? 'bg-muted/30' : 'bg-transparent',
      )}
    >
      {detailHref ? (
        <a
          href={detailHref}
          target="_blank"
          rel="noopener noreferrer"
          aria-label={`Open guideline: ${g.title}`}
          className="absolute inset-0 z-10 rounded-[calc(var(--radius)+2px)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
        />
      ) : null}

      <GuidelineCardShell
        as="article"
        title={
          <span className="whitespace-normal">{g.title}</span>
        }
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
        <div className="relative z-20 mt-3 flex w-full justify-center lg:justify-start">
          <LikertScale
            name={`relevance:${scenarioId}:${guidelineId}`}
            value={rating}
            onChange={handleChange}
          />
        </div>
      </GuidelineCardShell>
    </div>
  )
}
