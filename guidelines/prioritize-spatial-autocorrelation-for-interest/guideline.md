---
id: prioritize-spatial-autocorrelation-for-interest
title: Prioritize maps showing spatial clustering
bibliography: references.bib
description: When selecting among multiple possible thematic maps, prefer those with
  high spatial autocorrelation to increase user perceived interestingness.
labels:
- chart:map
- chart:choropleth
- task:rank
- impact:engagement
- data:geospatial
- visual:pattern
---

## The Rule <!-- role: advice -->
When generating or selecting thematic maps to accompany a narrative, prioritize datasets that exhibit high spatial autocorrelation (clustering of similar values) over those with random distributions.

## The Logic <!-- role: reason -->
Users perceive maps with distinct regional patterns as more visually interesting and salient than maps with scattered or noisy data. The NewsViews pipeline utilizes Moran’s I, a measure of spatial autocorrelation, as a proxy for "interestingness." Evaluation showed a correlation between this metric and users' ratings of how visually interesting a map appeared [@gao_newsviews_2014].
*   **The Principle:** Spatial Autocorrelation (Moran's I)
*   **The Evidence:** User studies in [@gao_newsviews_2014] confirmed that maps with higher Moran's I were rated as more visually interesting.

## Where to Apply <!-- role: context -->
*   **User Goal:** Engaging a casual news reader or increasing the "saliency" of a visualization.
*   **Data Type:** Geospatial data (specifically choropleth maps) where multiple variables could potentially be visualized.
*   **Audience:** General news consumers who may be drawn in by clear visual patterns.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data variable is strictly required by the narrative regardless of its distribution.
*   **Reason:** Relevance (semantic match to the text) is more critical than interestingness. The authors note that while interestingness is important, it is secondary to the variable actually matching the article's topic [@gao_newsviews_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may exclude variables that are highly relevant but geographically uniform or random.
*   **The Risk:** You might favor a "pretty" map over a more informative but "noisy" one, potentially distorting the story if the lack of pattern is the actual insight.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Visualizing data with very low spatial autocorrelation (random noise).
*   **Why it fails:** Users find these maps visually uninteresting and difficult to interpret as they lack discernible regional trends [@gao_newsviews_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the map look like "TV static" or a checkerboard?
*   **The Test:** Calculate Moran's I for the variable. If the value is near 0 (indicating randomness), the map is likely to be perceived as uninteresting.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If multiple relevant variables are available, choose the one with the most distinct regional grouping.
*   **Best Fix:** Filter candidate visualizations using a Moran's I threshold to ensure only spatially structured data is presented to the user.
