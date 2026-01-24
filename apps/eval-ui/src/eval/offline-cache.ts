import { z } from 'zod'

import { ScenarioSpecSchema, type ScenarioSpec } from './schemas'
import type { EvalScenarioBundle } from './types'

const CacheEnvelopeSchema = z.object({
  version: z.literal(1),
  cachedAt: z.string(),
  data: z.unknown(),
})

type CacheEnvelope = z.infer<typeof CacheEnvelopeSchema>

const CachedScenariosSchema = z.array(ScenarioSpecSchema)

const GuidelineSectionSchema = z
  .object({
    role: z.string().min(1),
    title: z.string().optional(),
    content: z.string().min(1),
  })
  .passthrough()

const GuidelineSchema = z
  .object({
    id: z.string().min(1),
    title: z.string().min(1),
    description: z.string().optional(),
    labels: z.array(z.string()).default([]),
    sections: z.array(GuidelineSectionSchema).optional(),
  })
  .passthrough()

const CatalogEntrySchema = z
  .object({
    guideline: GuidelineSchema,
    references: z.array(z.string()).optional(),
  })
  .passthrough()

const EvalGuidelineResultSchema = z
  .object({
    rank: z.number(),
    score: z.number(),
    entry: CatalogEntrySchema,
  })
  .passthrough()

const EvalStrategyResultSchema = z.object({
  strategyId: z.string().min(1),
  strategyName: z.string().min(1),
  guidelines: z.array(EvalGuidelineResultSchema),
})

const EvalScenarioBundleSchema = z.object({
  scenario: ScenarioSpecSchema,
  strategies: z.array(EvalStrategyResultSchema),
})

const SCENARIOS_CACHE_KEY = 'chartcoach/eval-ui/cache/scenarios/v1'
const SCENARIO_BUNDLE_CACHE_PREFIX = 'chartcoach/eval-ui/cache/scenario-bundle/v1:'

function canUseLocalStorage() {
  try {
    return typeof window !== 'undefined' && typeof window.localStorage !== 'undefined'
  } catch {
    return false
  }
}

function readEnvelope(key: string): CacheEnvelope | undefined {
  if (!canUseLocalStorage()) return

  try {
    const raw = window.localStorage.getItem(key)
    if (!raw) return

    const parsed = CacheEnvelopeSchema.safeParse(JSON.parse(raw))
    if (!parsed.success) return
    return parsed.data
  } catch {
    return
  }
}

function writeEnvelope(key: string, data: unknown, cachedAt: Date = new Date()) {
  if (!canUseLocalStorage()) return

  const payload: CacheEnvelope = {
    version: 1,
    cachedAt: cachedAt.toISOString(),
    data,
  }

  try {
    window.localStorage.setItem(key, JSON.stringify(payload))
  } catch {
    // ignore quota / privacy errors
  }
}

function scenarioBundleKey(scenarioId: string) {
  return `${SCENARIO_BUNDLE_CACHE_PREFIX}${encodeURIComponent(scenarioId)}`
}

export function readCachedScenarios() {
  const envelope = readEnvelope(SCENARIOS_CACHE_KEY)
  if (!envelope) return

  const parsed = CachedScenariosSchema.safeParse(envelope.data)
  return parsed.success ? parsed.data : undefined
}

export function writeCachedScenarios(scenarios: ScenarioSpec[]) {
  writeEnvelope(SCENARIOS_CACHE_KEY, scenarios)
}

export function readCachedScenarioBundle(scenarioId: string) {
  const envelope = readEnvelope(scenarioBundleKey(scenarioId))
  if (!envelope) return

  const parsed = EvalScenarioBundleSchema.safeParse(envelope.data)
  return parsed.success ? (parsed.data as EvalScenarioBundle) : undefined
}

export function writeCachedScenarioBundle(bundle: EvalScenarioBundle) {
  writeEnvelope(scenarioBundleKey(bundle.scenario.id), bundle)
}
