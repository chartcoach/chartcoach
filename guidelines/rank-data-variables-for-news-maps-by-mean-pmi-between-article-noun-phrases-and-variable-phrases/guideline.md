---
id: rank-data-variables-for-news-maps-by-mean-pmi-between-article-noun-phrases-and-variable-phrases
title: Rank candidate map variables by mean PMI between article noun phrases and variable
  phrases
bibliography: references.bib
description: Use co-occurrence statistics from a news corpus to match article topics
  to dataset variable labels.
labels:
- chart:map
- task:select
- visual:none
- impact:relevance
- data:text
- audience:novice
- pipeline:variable-selection
---

## Score variable-to-article relevance using mean PMI <!-- role: advice -->

Compute the mean Pointwise Mutual Information (PMI) between noun phrases extracted from the article’s first three sentences and noun phrases derived from each candidate variable name, and rank variables by this score.

## Why PMI aligns article topics with dataset variables <!-- role: reason -->

Article wording rarely matches dataset column labels exactly, so direct string matching fails. PMI captures how strongly terms co-occur in a large corpus, letting the system infer that different phrasings refer to the same underlying concept.

**Mechanism:** Co-occurrence-based association functions as a proxy for semantic relatedness between article topic terms and variable descriptors, improving variable selection for thematic mapping.

**Evidence:** Variables are represented by extracted “variable phrases,” articles contribute filtered noun phrases, and mean PMI over all pairings is used to rank 155 candidate variables; perceived relevance decreases as PMI rank decreases, with relevance dropping off around rank ~30 in user ratings [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** PMI is used to prioritize variable relevance ahead of other ranking features in the final map selection.

## When PMI-based variable ranking applies <!-- role: context -->

- **User Goal:** See data that matches what the article is about.
- **Task:** Select the most relevant quantitative variable to map.
- **Data:** News article text plus a table database of georeferenced variables with textual labels.
- **Chart Setting:** Automated generation of thematic choropleth maps.
- **Audience:** General news readers; low tolerance for off-topic visuals.
- **Success Criterion:** Chosen variable is rated as relevant to the article topic.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The article contains explicit statistics that directly name the variable and geography level. **Why:** Corpus co-occurrence may be unnecessary and can be less direct than matching the explicitly stated measure.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Requires a large, indexed corpus for co-occurrence queries. **Risk:** PMI can overvalue spurious correlations in the corpus or underperform for rare/new topics. **Mitigation:** Apply thresholds and fallbacks when PMI evidence is weak.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using the raw variable string (including overly specific tokens) as the matching target. **Why it fails:** Over-specific labels reduce recall and lower measured association with article language.

## Quick tests <!-- role: check -->

**Failure Sign:** The map’s variable feels unrelated to the story’s main topic. **Quick Check:** Inspect top-ranked variables and confirm they share recognizable topical terms with the article’s lede. **Stronger Test:** Have raters judge relevance for a sample and verify ratings degrade as PMI rank decreases.

## What to do instead <!-- role: fix -->

- Generate multiple noun-phrase variants from each variable label and score against article noun phrases.
- Filter article noun phrases using a tf–idf threshold before computing PMI.
- If no variable passes a relevance threshold, generate a reference (locator) map instead of a thematic map.
