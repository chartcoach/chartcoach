import { GuidelineCard as GuidelineCardShell, type GuidelineCardLabel } from '@chartcoach/ui'

import type { EvalGuidelineResult } from '@chartcoach/eval-ui/eval/types'

import { LikertScale } from './likert-scale'

type GuidelineCardProps = {
  scenarioId: string
  result: EvalGuidelineResult
  rating: number | undefined
  onRate: (guidelineId: string, next: number) => void
  onClear: (guidelineId: string) => void
}

export function GuidelineCard({
  scenarioId,
  result,
  rating,
  onRate,
  onClear,
}: GuidelineCardProps) {
  const g = result.entry.guideline
  const guidelineId = g.id

  function handleRate(next: number) {
    onRate(guidelineId, next)
  }

  function handleClear() {
    onClear(guidelineId)
  }

  const labelsShown = g.labels.slice(0, 8)
  const labelsRemaining = Math.max(0, g.labels.length - labelsShown.length)
  const labels: GuidelineCardLabel[] = labelsShown.map((label) => ({
    value: { text: label },
  }))

  return (
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
          <span>·</span>
          <span className="tabular-nums">score {result.score.toFixed(2)}</span>
          <span>·</span>
          <span className="min-w-0 truncate">{g.id}</span>
        </>
      }
      actions={
        <div className="flex flex-col items-end gap-2">
          <LikertScale
            name={`relevance:${scenarioId}:${guidelineId}`}
            value={rating}
            onChange={handleRate}
          />
          <button
            type="button"
            onClick={handleClear}
            className="inline-flex rounded-md px-2 py-1 text-xs text-muted-foreground hover:bg-muted hover:text-foreground"
          >
            Clear
          </button>
        </div>
      }
    >
      <details>
        <summary className="cursor-pointer select-none text-xs font-medium text-muted-foreground hover:text-foreground focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60">
          Show full guideline
        </summary>
        <div className="mt-3 space-y-3">
          {g.sections?.length ? (
            <div className="space-y-2">
              {g.sections.slice(0, 6).map((s, idx) => (
                <div key={`${s.role}:${idx}`} className="rounded-lg bg-muted/40 p-3">
                  <div className="flex flex-wrap items-baseline gap-2 text-xs text-muted-foreground">
                    <span className="rounded bg-background/70 px-2 py-0.5 font-medium text-foreground">
                      {s.role}
                    </span>
                    <span className="font-medium text-foreground">{s.title}</span>
                  </div>
                  <div className="mt-2 whitespace-pre-wrap text-sm leading-relaxed">
                    {s.content}
                  </div>
                </div>
              ))}
            </div>
          ) : null}

          {result.entry.references?.length ? (
            <div className="rounded-lg bg-muted/40 p-3">
              <div className="text-xs font-medium text-muted-foreground">
                References ({result.entry.references.length})
              </div>
              <div className="mt-2 whitespace-pre-wrap text-xs leading-relaxed text-muted-foreground">
                {result.entry.references.slice(0, 2).join('\n\n')}
                {result.entry.references.length > 2 ? '\n\n…' : ''}
              </div>
            </div>
          ) : null}
        </div>
      </details>
    </GuidelineCardShell>
  )
}
