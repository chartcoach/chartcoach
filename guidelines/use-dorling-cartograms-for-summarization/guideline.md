---
id: use-dorling-cartograms-for-summarization
title: Use Dorling Cartograms for Summarizing Data Trends
bibliography: references.bib
description: Dorling cartograms outperform other types for aggregate tasks and summarizing
  overall data patterns.
labels:
- chart:cartogram
- chart:dorling
- task:aggregate
- task:summarize
- impact:clarity
- data:geospatial
---

## The Rule <!-- role: advice -->
Use Dorling (circular) cartograms when the user needs to summarize overall data trends or aggregate values across a map.

## The Logic <!-- role: reason -->
Dorling cartograms represent regions as circles. The simple circular shapes convey data patterns more easily than complex polygons, allowing viewers to process the "big picture" more effectively.
*   **The Principle:** Shape Simplicity and Pattern Recognition.
*   **The Evidence:** In the review by [@zeng_review_2023], which collates data from [@nusrat_evaluating_2018], Dorling cartograms (E-4) ranked highest in accuracy for "aggregate" tasks, significantly outperforming rectangular cartograms.

## Where to Apply <!-- role: context -->
*   **User Goal:** Analyzing broad distributions, identifying outliers, or summarizing regional data.
*   **Data Type:** Geospatial data where exact geographic boundaries are secondary to the statistical value.
*   **Audience:** Users looking for high-level insights rather than precise local navigation.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to identify specific neighbors or adjacency relationships.
*   **Reason:** Dorling cartograms break topology; circles typically do not touch in the same way actual borders do, making adjacency tasks difficult [@nusrat_evaluating_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Geographic familiarity and topology. Shapes are reduced to circles, and borders are lost.
*   **The Risk:** Users may struggle to identify specific regions (filtering/locating) compared to contiguous cartograms.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using Rectangular cartograms for summaries.
*   **Why it fails:** Rectangular cartograms were ranked lowest for aggregation tasks in the study [@nusrat_evaluating_2018], likely due to the cognitive load of processing varying aspect ratios.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are regions represented by circles?
*   **The Test:** Ask a user to describe the general trend (e.g., "Which area has the highest concentration?"). If they struggle, the layout may be too cluttered.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Convert the mark type from polygon/rect to circle.
*   **Best Fix:** Implement a Dorling layout algorithm that minimizes overlap while maintaining relative spatial positions.
