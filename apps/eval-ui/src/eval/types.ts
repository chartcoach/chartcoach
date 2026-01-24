import type { CatalogEntry } from '@chartcoach/catalog'
import type { ScenarioSpec } from './schemas'

export type EvalGuidelineResult = {
  rank: number
  score: number
  entry: CatalogEntry
}

export type EvalStrategyResult = {
  strategyId: string
  strategyName: string
  guidelines: EvalGuidelineResult[]
}

export type EvalScenarioBundle = {
  scenario: ScenarioSpec
  strategies: EvalStrategyResult[]
}

