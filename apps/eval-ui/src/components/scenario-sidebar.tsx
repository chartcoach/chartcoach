import type { MouseEvent } from 'react'

import { cn } from '@chartcoach/eval-ui/lib/utils'

import type { ScenarioSpec } from '@chartcoach/eval-ui/eval/schemas'

type ScenarioSidebarProps = {
  scenarios: ScenarioSpec[]
  selectedScenarioId: string
  onSelect: (scenarioId: string) => void
  className?: string
}

export function ScenarioSidebar({
  scenarios,
  selectedScenarioId,
  onSelect,
  className,
}: ScenarioSidebarProps) {
  function handleScenarioClick(event: MouseEvent<HTMLButtonElement>) {
    const nextScenarioId = event.currentTarget.dataset.scenarioId
    if (!nextScenarioId) return
    onSelect(nextScenarioId)
  }

  return (
    <aside className={cn('rounded-xl border bg-card', className)}>
      <div className="border-b px-4 py-3">
        <div className="text-xs font-semibold text-muted-foreground">
          Scenarios <span className="tabular-nums">({scenarios.length})</span>
        </div>
      </div>

      <nav className="p-2">
        <ul className="space-y-1.5">
          {scenarios.map((s) => {
            const active = s.id === selectedScenarioId
            return (
              <li key={s.id}>
                <button
                  type="button"
                  data-scenario-id={s.id}
                  onClick={handleScenarioClick}
                  aria-pressed={active}
                  className={cn(
                    'w-full rounded-lg px-3 py-2 text-left transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60',
                    active ? 'bg-muted' : 'hover:bg-muted',
                  )}
                >
                  <div className="line-clamp-2 text-sm font-medium leading-snug">
                    {s.title}
                  </div>
                </button>
              </li>
            )
          })}
        </ul>
      </nav>
    </aside>
  )
}
