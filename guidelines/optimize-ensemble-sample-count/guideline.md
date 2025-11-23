---
id: optimize-ensemble-sample-count
title: Display Sufficient Sample Density for Implicit Uncertainty
bibliography: references.bib
description: Ensure enough tracks are shown to convey spatial spread without relying
  on annotations.
labels:
- chart:ensemble
- task:estimate
- visual:density
- impact:accuracy
- data:simulation
- audience:general-public
---

## The Rule <!-- role: advice -->
When visualizing unannotated ensemble tracks, display a sufficiently high number of paths (more than 15) to ensure users perceive the correct spatial spread of uncertainty.

## The Logic <!-- role: reason -->
The number of tracks displayed directly influences the user's perception of risk and damage potential. Cognitive studies show that when looking at unannotated lines, viewers require a higher density to recognize the increased spatial uncertainty over time. In experiments, displaying 63 tracks successfully conveyed the flattening relationship between damage and distance over time (indicating spread), whereas displays with only 7 or 15 unannotated tracks failed to show this effect significantly [@liu_visualizing_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating risk or coverage area based solely on trajectory lines.
*   **Data Type:** Ensemble forecasts where the spread of lines indicates probability.
*   **Audience:** Users viewing static or non-interactive displays where clutter is less of a concern than accuracy.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** You are able to add rich annotations (size/intensity glyphs) to the tracks.
*   **Reason:** Annotations help users calibrate their judgments, allowing for fewer tracks (~15) to be used effectively without the loss of risk perception associated with sparse unannotated charts [@liu_visualizing_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual minimalism.
*   **The Risk:** Higher track counts (e.g., 63) increase visual clutter, making it difficult to trace individual paths or layer additional information like wind speed colors or size circles.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing only the mean track or a very small sample (e.g., 5-7 lines) to "clean up" the view.
*   **Why it fails:** Users underestimate the spatial spread of the potential outcomes, leading to overconfidence in areas just outside the sparse lines [@liu_visualizing_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there large gaps between the outermost tracks and the center tracks at the end of the forecast period?
*   **The Test:** Compare the "fan" of your subset to the full ensemble. If the subset looks significantly narrower or "gappier," you likely have too few lines.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the number of randomly selected tracks.
*   **Best Fix:** Use a recursive median clustering algorithm to select a specific number of tracks (e.g., 63) that mathematically maximize the coverage of the original distribution [@liu_visualizing_2019].
