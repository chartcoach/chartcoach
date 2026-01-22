---
id: use-morans-i-to-approximate-perceived-choropleth-interestingness-when-selecting-among-relevant-maps
title: "Use Moran\u2019s I to approximate perceived choropleth interestingness when\
  \ selecting among relevant maps"
bibliography: references.bib
description: Prefer maps with stronger spatial autocorrelation as a proxy for visually
  interesting regional patterns.
labels:
- chart:choropleth
- task:prioritize
- visual:pattern
- impact:engagement
- data:geospatial
- audience:novice
- pipeline:saliency
---

## Prefer higher Moran’s I among topic-relevant candidate maps <!-- role: advice -->

When choosing among multiple topic-relevant choropleth candidates, prefer the map with higher Moran’s I (spatial autocorrelation) to increase the chance the displayed pattern is perceived as visually interesting.

## Why spatial autocorrelation can signal salient regionalization <!-- role: reason -->

Thematic maps are often valued for revealing coherent regional structure rather than noisy, unpatterned variation. Moran’s I quantifies spatial autocorrelation, which aligns with the presence of clustered regions that can be easier to notice and interpret as “patterns.”

**Mechanism:** Higher spatial autocorrelation increases the likelihood of contiguous areas sharing similar values, producing visually coherent regions that draw attention.

**Evidence:** The pipeline computes Moran’s I for each candidate map as a measure of visual interestingness and uses it in ranking; in user ratings, maps chosen with Moran’s-I-based saliency scored higher on perceived visual saliency and overall ratings than versions that did not prioritize saliency [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** The evaluation used randomized artificial data labeling to vary Moran’s I while keeping other factors constant.

## When Moran’s I prioritization applies <!-- role: context -->

- **User Goal:** Notice and interpret geographic patterns quickly.
- **Task:** Choose among multiple candidate thematic maps of different variables or renderings.
- **Data:** Choropleth-ready values over adjacent regions where neighborhood relations are defined.
- **Chart Setting:** Automated map selection; limited space to show only one map.
- **Audience:** General readers; benefits from clear regional patterns.
- **Success Criterion:** Higher perceived map interestingness without sacrificing topical relevance.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary objective is to highlight outliers rather than regional clustering. **Why:** High Moran’s I favors clustering and may down-rank maps where isolated extremes are the main story.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some relevant variables may be deprioritized if they have low spatial autocorrelation. **Risk:** Over-optimizing for clustering can encourage maps that look “patterned” but are not the best match to the story. **Mitigation:** Apply Moran’s I only after filtering to high-relevance variables.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using Moran’s I as the primary selector before ensuring topic relevance. **Why it fails:** The most clustered map can be off-topic and reduce explanatory value.

## Quick tests <!-- role: check -->

**Failure Sign:** The selected map looks patterned but readers do not feel it helps explain the article. **Quick Check:** Confirm the chosen variable is in the top relevance set before comparing Moran’s I. **Stronger Test:** Collect reader ratings for saliency and usefulness across candidates with different Moran’s I values.

## What to do instead <!-- role: fix -->

- Gate Moran’s I ranking behind a relevance filter (e.g., top PMI variables only).
- Use observational annotations (extreme values) when the selected map has low clustering but meaningful outliers.
- Switch to a reference map when neither relevance nor saliency can be achieved reliably.
