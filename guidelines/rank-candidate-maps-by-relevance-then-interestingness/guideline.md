---
id: rank-candidate-maps-by-relevance-then-interestingness
title: Rank Candidate Maps by Relevance Before Interestingness
bibliography: references.bib
description: Select the final map by prioritizing topic-variable relevance, then use
  spatial pattern measures and annotation relevance as secondary ranking criteria.
labels:
- chart:map
- task:rank
- visual:color
- impact:relevance
- data:geospatial
- audience:general
- domain:news
---

## The Rule <!-- role: advice -->

When choosing among candidate maps, prioritize variable-to-article relevance first, then prioritize visually interesting spatial patterns, while also considering annotation relevance.

## The Logic <!-- role: reason -->

A visually compelling map that depicts the wrong variable harms comprehension; NewsViews’ ranking emphasizes topical match (PMI) and then uses pattern “interestingness” (Moran’s I) to choose among relevant candidates.

- **The Principle:** Relevance-first selection to maintain narrative integrity
- **The Evidence:** [@gaoNewsViewsAutomatedPipeline2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Trust that the map supports the story and also notice meaningful geographic patterns
- **Data Type:** Multiple plausible variable/time slices and multiple candidate annotated views
- **Audience:** General news readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** When the editorial goal is explicitly exploratory or “serendipity-first” rather than story-explanatory
- **Reason:** In exploration contexts, prioritizing “interestingness” can be acceptable even with weaker topical grounding [@gaoNewsViewsAutomatedPipeline2014]

## The Price <!-- role: costs -->

- **The Sacrifice:** Some highly “interesting” patterns might be excluded if relevance is lower
- **The Risk:** Over-thresholding relevance can result in fewer thematic maps and more reference maps [@gaoNewsViewsAutomatedPipeline2014]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking the most visually striking map regardless of topical fit
- **Why it fails:** It can maximize perceived pattern while minimizing explanatory value for the article [@gaoNewsViewsAutomatedPipeline2014]

## How to Check <!-- role: check -->

- **Visual Sign:** Readers react to the pattern, but the variable title doesn’t align with article topic terms
- **The Test:** Validate that the chosen variable is among the top relevance-ranked set before applying the interestingness ranking [@gaoNewsViewsAutomatedPipeline2014]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Enforce a relevance threshold (e.g., retain only high-PMI candidates) before ranking by Moran’s I
- **Best Fix:** Use a multi-criterion ranking that orders candidates primarily by PMI relevance and secondarily by Moran’s I while filtering by annotation relevance [@gaoNewsViewsAutomatedPipeline2014]
