---
id: use-spatial-autocorrelation-morans-i-to-estimate-map-interestingness
title: "Estimate Map Interestingness with Moran\u2019s I"
bibliography: references.bib
description: "Use Moran\u2019s I as a proxy for how visually interesting a choropleth\u2019\
  s spatial pattern will be to viewers."
labels:
- chart:choropleth
- task:rank
- visual:pattern
- impact:engagement
- data:geospatial
- audience:general
- domain:news
---

## The Rule <!-- role: advice -->

Use Moran’s I (spatial autocorrelation) to score candidate thematic maps for visual “interestingness,” and prefer higher-scoring maps among similarly relevant candidates.

## The Logic <!-- role: reason -->

Spatial autocorrelation captures regionalization—whether nearby areas have similar values—which the system hypothesizes contributes to perceived interestingness; user ratings in the evaluation aligned with this measure enough to support its use in ranking.

- **The Principle:** Regionalization as a perceptual driver of map salience
- **The Evidence:** [@gaoNewsViewsAutomatedPipeline2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Notice meaningful spatial structure rather than noise
- **Data Type:** Choropleth maps over adjacent regions (e.g., counties)
- **Audience:** General news readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** When the important story signal is dispersion or isolated hotspots rather than clustering
- **Reason:** Moran’s I emphasizes clustering/neighbor similarity and may undervalue other meaningful patterns [@gaoNewsViewsAutomatedPipeline2014]

## The Price <!-- role: costs -->

- **The Sacrifice:** Diversity of pattern types shown
- **The Risk:** Over-prioritizing clustered patterns may bias which topics/variables get visualized [@gaoNewsViewsAutomatedPipeline2014]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Maximizing Moran’s I without ensuring variable relevance to the article
- **Why it fails:** It can select an “interesting” but irrelevant map, reducing explanatory value [@gaoNewsViewsAutomatedPipeline2014]

## How to Check <!-- role: check -->

- **Visual Sign:** Selected maps consistently show big clusters even when the story implies a different kind of spatial structure
- **The Test:** Compare a high-Moran’s-I candidate and a lower one for the same article-relevant variable; if both are relevant, prefer the higher-I, otherwise keep relevance first [@gaoNewsViewsAutomatedPipeline2014]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use Moran’s I only as a tie-breaker among high-relevance candidates
- **Best Fix:** Integrate Moran’s I into a multi-criterion ranker that preserves a relevance threshold and annotation relevance constraints [@gaoNewsViewsAutomatedPipeline2014]
