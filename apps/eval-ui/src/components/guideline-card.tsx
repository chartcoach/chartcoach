import { GuidelineCard as GuidelineCardShell, type GuidelineCardLabel } from '@chartcoach/ui'
import { Eraser, ExternalLink } from 'lucide-react'

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

  function handleRate(next: number) {
    onRate(guidelineId, next)
  }

  function handleClear() {
    onClear(guidelineId)
  }

  const labelsShown = g.labels.slice(0, 4)
  const labelsRemaining = Math.max(0, g.labels.length - labelsShown.length)
  const labels: GuidelineCardLabel[] = labelsShown.map((label) => ({
    value: { text: label },
  }))

  return (
    <div
      id={domId}
      tabIndex={-1}
      className={cn(
        'rounded-[calc(var(--radius)+2px)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60',
        'scroll-mt-[calc(var(--app-header-height)+8rem)]',
        isActive ? 'ring-2 ring-ring/50' : 'ring-0',
      )}
    >
      <GuidelineCardShell
        as="article"
        title={<span className="line-clamp-2">{g.title}</span>}
        description={
          g.description ? <span className="line-clamp-2">{g.description}</span> : undefined
        }
        labels={labels}
        labelsRemaining={labelsRemaining || undefined}
        meta={
          <>
            <span className="tabular-nums">#{result.rank}</span>
          </>
        }
        actions={
          <div className="flex flex-col items-end gap-2">
            <LikertScale
              name={`relevance:${scenarioId}:${guidelineId}`}
              value={rating}
              onChange={handleRate}
            />
            <div className="flex items-center gap-1">
              {detailHref ? (
                <a
                  href={detailHref}
                  target="_blank"
                  rel="noreferrer"
                  className="inline-flex size-11 items-center justify-center rounded-md text-muted-foreground hover:bg-muted hover:text-foreground focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
                  aria-label="Open guideline in browser"
                  title="Open guideline in browser"
                >
                  <ExternalLink className="size-4" aria-hidden="true" />
                  <span className="sr-only">Open</span>
                </a>
              ) : null}
              <button
                type="button"
                onClick={handleClear}
                className="inline-flex size-11 items-center justify-center rounded-md text-muted-foreground hover:bg-muted hover:text-foreground focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60"
                aria-label="Clear rating"
                title="Clear rating"
              >
                <Eraser className="size-4" aria-hidden="true" />
                <span className="sr-only">Clear</span>
              </button>
            </div>
          </div>
        }
      />
    </div>
  )
}
