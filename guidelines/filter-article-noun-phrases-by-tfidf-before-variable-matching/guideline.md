---
id: filter-article-noun-phrases-by-tfidf-before-variable-matching
title: "Filter article noun phrases by tf\u2013idf before matching to variables"
bibliography: references.bib
description: "Use tf\u2013idf to keep topic-bearing noun phrases from the lede for\
  \ variable selection."
labels:
- chart:map
- task:extract
- visual:none
- impact:relevance
- data:text
- audience:expert
- pipeline:query-extraction
---

## Use tf–idf to keep only informative noun phrases <!-- role: advice -->

Extract noun phrases from the first three sentences and remove noun phrases with low tf–idf so only topic-bearing terms feed variable selection.

## Why tf–idf filtering preserves the article’s topical signal <!-- role: reason -->

Early news text contains both topical and boilerplate language; low tf–idf phrases are more likely to be generic and unhelpful for matching. Keeping higher tf–idf noun phrases increases the quality of the text signal used for selecting a relevant data variable.

**Mechanism:** tf–idf downweights globally frequent phrases, reducing noise in downstream similarity measures like PMI.

**Evidence:** The pipeline extracts noun phrases from the first three sentences and removes phrases with tf–idf below a threshold (\<0.001) before computing PMI against variable phrases [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** This step improves topic extraction rather than location extraction.

## When tf–idf filtering applies <!-- role: context -->

- **User Goal:** Ensure the chosen mapped variable reflects the story’s topic.
- **Task:** Extract topic terms for variable matching.
- **Data:** News text with mixed topical and generic phrasing.
- **Chart Setting:** Automated thematic map generation driven by text mining.
- **Audience:** Pipeline designers; end users indirectly benefit through better relevance.
- **Success Criterion:** Cleaner topic-term set leading to better-ranked variables.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The article’s key topic is expressed using very common phrasing in the corpus. **Why:** tf–idf filtering can remove genuinely important terms if they are globally frequent.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Potential loss of some legitimate topic indicators. **Risk:** Over-filtering can leave too few terms, weakening variable matching. **Mitigation:** Use multiple noun phrases and keep a minimum count before filtering becomes strict.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Feeding all extracted noun phrases directly into variable matching. **Why it fails:** Generic phrases dilute PMI signals and can elevate irrelevant variables.

## Quick tests <!-- role: check -->

**Failure Sign:** Selected variables match generic themes rather than the article’s specific topic. **Quick Check:** Review retained noun phrases and confirm they would help a human summarize the article topic. **Stronger Test:** Compare variable relevance ratings with and without tf–idf filtering.

## What to do instead <!-- role: fix -->

- Lower the tf–idf threshold if too few noun phrases remain for scoring.
- Add alternative topic seeds (e.g., additional lede sentences) when noun-phrase yield is low.
- Fall back to reference maps when topic-term extraction is too weak to select a thematic variable confidently.
