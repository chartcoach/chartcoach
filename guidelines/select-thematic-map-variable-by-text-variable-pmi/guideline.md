---
id: select-thematic-map-variable-by-text-variable-pmi
title: Select the Map Variable Using Text-to-Variable PMI
bibliography: references.bib
description: Rank candidate geospatial variables by pointwise mutual information between
  article topic phrases and variable label phrases.
labels:
- chart:map
- task:match
- visual:color
- impact:relevance
- data:text
- audience:general
- domain:news
---

## The Rule <!-- role: advice -->

Rank candidate thematic-map variables by pointwise mutual information (PMI) between article noun-phrase terms and variable-label phrases, and only consider the top set above a threshold for mapping.

## The Logic <!-- role: reason -->

PMI operationalizes topical association by comparing co-occurrence versus independent occurrence in a news corpus, helping choose variables that the corpus shows are semantically tied to the article’s topic.

- **The Principle:** Corpus-based association for variable relevance
- **The Evidence:** [@gaoNewsViewsAutomatedPipeline2014]

## Where to Apply <!-- role: context -->

- **User Goal:** See a thematic map whose encoded quantity actually matches the story’s subject
- **Data Type:** Many candidate variables across topics (e.g., education, unemployment, health)
- **Audience:** General news readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** New or rare topics where the corpus lacks enough co-occurrence history
- **Reason:** PMI may be unreliable with sparse counts, pushing the system toward irrelevant or overly generic variables [@gaoNewsViewsAutomatedPipeline2014]

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires a large indexed corpus and preprocessing of variable phrases
- **The Risk:** Overfits to corpus phrasing; may miss correct variables described with novel wording [@gaoNewsViewsAutomatedPipeline2014]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Matching variables by direct string overlap with the article
- **Why it fails:** Article noun phrases often don’t match variable names directly (e.g., “job hunters” vs. “unemployment rate”) [@gaoNewsViewsAutomatedPipeline2014]

## How to Check <!-- role: check -->

- **Visual Sign:** The chosen variable reads like a different topic than the article (even if map looks plausible)
- **The Test:** Inspect top-ranked variables; if relevance drops sharply after a rank cutoff, threshold there rather than using a fixed top-K blindly [@gaoNewsViewsAutomatedPipeline2014]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Threshold the PMI-ranked list at the sharp drop-off (instead of always using top-K)
- **Best Fix:** Improve variable phrase extraction by keeping moderately frequent noun phrases and removing overly common/overly rare terms from variable labels [@gaoNewsViewsAutomatedPipeline2014]
