import type { MouseEvent } from 'react'

import { cn } from '@chartcoach/eval-ui/lib/utils'

type StrategyPickerStrategy = {
  strategyId: string
  strategyName: string
}

type StrategyPickerProps = {
  strategies: readonly StrategyPickerStrategy[]
  selectedStrategyId: string | undefined
  onSelect: (strategyId: string) => void
}

export function StrategyPicker({
  strategies,
  selectedStrategyId,
  onSelect,
}: StrategyPickerProps) {
  function handleClick(event: MouseEvent<HTMLButtonElement>) {
    const nextStrategyId = event.currentTarget.dataset.strategyId
    if (!nextStrategyId) return
    onSelect(nextStrategyId)
  }

  return (
    <div className="flex gap-2 overflow-x-auto pb-1 sm:flex-wrap sm:overflow-visible sm:pb-0">
      {strategies.map((strategy) => {
        const active = strategy.strategyId === selectedStrategyId
        return (
          <button
            key={strategy.strategyId}
            type="button"
            data-strategy-id={strategy.strategyId}
            onClick={handleClick}
            aria-pressed={active}
            className={cn(
              'shrink-0 rounded-full border px-3 py-1.5 text-xs font-medium transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring/60',
              active
                ? 'border-foreground/20 bg-muted'
                : 'border-transparent text-muted-foreground hover:bg-muted hover:text-foreground',
            )}
          >
            {strategy.strategyName}
          </button>
        )
      })}
    </div>
  )
}
