---
id: filter-variable-label-phrases-by-corpus-frequency-to-improve-pmi-matching
title: Filter variable-label phrases by corpus frequency before PMI matching
bibliography: references.bib
description: Drop overly common and extremely rare label phrases so PMI uses informative
  variable descriptors.
labels:
- chart:map
- task:match
- visual:none
- impact:robustness
- data:text
- audience:expert
- pipeline:variable-selection
---

## Keep only moderately frequent variable phrases for PMI <!-- role: advice -->

When generating noun-phrase candidates from variable labels, discard phrases that are too frequent in the corpus and phrases that are too rare, and compute PMI only on the remaining phrases.

## Why frequency filtering makes PMI more discriminative <!-- role: reason -->

Very common terms contribute little topical information and inflate matches across unrelated articles, while extremely rare phrases may never appear and provide no usable co-occurrence signal. Restricting to moderately frequent phrases improves the chance that PMI reflects meaningful topic-variable relationships.

**Mechanism:** Removing stop-like tokens and near-absent tokens increases signal-to-noise in co-occurrence statistics used for relevance ranking.

**Evidence:** Variable labels are decomposed into phrase sets and filtered by corpus frequency, discarding terms with frequency above 0.05 and below 0.0001 before computing mean PMI for variable ranking [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** The specific thresholds are an operational choice; the underlying principle is to avoid uninformative and unusable terms.

## When frequency filtering applies <!-- role: context -->

- **User Goal:** Get a thematic variable that matches the article topic.
- **Task:** Improve variable-to-text matching quality.
- **Data:** Variable labels that include generic tokens (e.g., “county”) and rare formal phrases.
- **Chart Setting:** Automated variable selection using corpus indexing.
- **Audience:** System builders and data journalists creating automated pipelines.
- **Success Criterion:** Higher-quality candidate variable rankings for map generation.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The corpus is small or highly specialized and rare phrases are still reliable signals. **Why:** Aggressive filtering can remove legitimately informative descriptors needed for matching.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional preprocessing and corpus statistics collection. **Risk:** Filtering may drop the best descriptor for some variables, hurting recall. **Mitigation:** Keep multiple alternative phrases per variable so at least one survives filtering.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Leaving generic geography-level terms (e.g., “county”) in the variable phrase set. **Why it fails:** Such terms appear across many topics and can dominate PMI-based relevance.

## Quick tests <!-- role: check -->

**Failure Sign:** Many unrelated variables receive similar relevance scores. **Quick Check:** Inspect retained variable phrases and verify they are topic-bearing rather than structural (unit/geography) tokens. **Stronger Test:** Compare relevance rankings with and without frequency filtering on held-out articles.

## What to do instead <!-- role: fix -->

- Expand each variable label into multiple candidate noun phrases and compute corpus frequencies for each.
- Remove high-frequency and ultra-low-frequency phrases before PMI computation.
- Store the retained phrase set per variable so scoring is consistent across runs.
