---
id: avoid-perfect-squares-in-area-comparisons
title: Allow Non-Square Aspect Ratios in Area Judgments
bibliography: references.bib
description: When designing treemaps or cartograms, avoiding perfect 1:1 aspect ratios
  can actually improve area estimation accuracy.
labels:
- chart:treemap
- chart:cartogram
- visual:area
- task:compare
- impact:accuracy
---

## The Rule <!-- role: advice -->
Do not force rectangles in area-based visualizations (like treemaps) to have a perfect 1:1 aspect ratio. Allow for some variation in aspect ratio rather than strictly optimizing for squares.

## The Logic <!-- role: reason -->
Counter-intuitively, users perform worse when comparing rectangles that are perfect squares (aspect ratio 1:1). Research suggests that viewers may substitute 1D length comparisons (side length) as a proxy for area. When shapes are perfectly square, this heuristic leads to maximal error in estimation. A lack of perfect optimization helps viewers avoid this perceptual trap [@heer_crowdsourcing_2010].
*   **The Principle:** Heuristic Estimation Bias
*   **The Evidence:** Experiment 1B in [@heer_crowdsourcing_2010] showed that comparisons of rectangles with aspect ratio 1 exhibited the worst performance compared to mixed aspect ratios.

## Where to Apply <!-- role: context -->
*   **User Goal:** Visually estimating and comparing the magnitude of values encoded by area.
*   **Data Type:** Quantitative data mapped to rectangular areas.
*   **Audience:** General users viewing static or interactive area-based charts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Extreme Aspect Ratios.
*   **Reason:** While perfect squares are not optimal, extreme variations (very thin, long rectangles) are known to hamper judgment significantly based on prior literature cited in the study [@heer_crowdsourcing_2010].

## The Price <!-- role: costs -->
*   **The Sacrifice:** The visualization may look slightly less uniform or "clean" geometrically.
*   **The Risk:** If aspect ratios become too extreme (very narrow strips), legibility and label placement become difficult.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Aggressively optimizing layout algorithms to produce only perfect squares.
*   **Why it fails:** It inadvertently triggers 1D length comparison heuristics that decrease area judgment accuracy [@heer_crowdsourcing_2010].

## How to Check <!-- role: check -->
*   **Visual Sign:** A treemap where every cell looks like a perfect square.
*   **The Test:** Review the aspect ratios of the generated rectangles; slight deviation from 1:1 is desirable.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Relax the constraints of the "squarified" layout algorithm.
*   **Best Fix:** Use a layout algorithm that balances aspect ratio quality with topology, accepting ratios slightly off 1:1.
