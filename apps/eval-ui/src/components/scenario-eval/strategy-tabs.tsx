import { Tabs, TabsList, TabsTrigger } from '@chartcoach/eval-ui/components/ui/tabs'
import type { EvalStrategyResult } from '@chartcoach/eval-ui/eval/types'

export function StrategyTabs({
  strategies,
  selectedStrategyId,
  onSelectStrategy,
}: {
  strategies: EvalStrategyResult[]
  selectedStrategyId: string | undefined
  onSelectStrategy: (strategyId: string) => void
}) {
  if (!strategies.length) return null

  return (
    <div className="space-y-2">
      <div className="text-xs font-semibold text-muted-foreground">Retrieval strategy</div>
      <Tabs value={selectedStrategyId ?? strategies[0]!.strategyId} onValueChange={onSelectStrategy}>
        <TabsList
          variant="line"
          className="h-auto w-full max-w-full justify-start overflow-x-auto rounded-none bg-transparent px-0 py-1 whitespace-nowrap"
        >
          {strategies.map((s) => (
            <TabsTrigger
              key={s.strategyId}
              value={s.strategyId}
              className="flex-none rounded-none px-2 py-1 text-xs text-foreground/80"
            >
              {s.strategyName}
            </TabsTrigger>
          ))}
        </TabsList>
      </Tabs>
    </div>
  )
}
