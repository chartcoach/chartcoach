---
id: encode-storm-intensity-as-seven-discrete-categories-with-distinct-colors-on-track-segments
title: Encode storm intensity as seven discrete categories with distinct colors on
  track segments
bibliography: references.bib
description: Map wind-speed predictions to standard storm categories and color each
  track segment by category to make intensity changes readable.
labels:
- chart:trajectory
- task:identify-change
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- domain:tropical-cyclone
---

## Color track segments by discrete intensity categories, not by a continuous gradient of wind speed <!-- role: advice -->

Convert predicted wind speeds into the seven storm intensity categories used in tropical cyclone communication, and color each track segment by the category at that segment’s start time. Use seven clearly distinguishable colors so adjacent categories are visually separable.

## Discrete categories match the decision framing and reduce ambiguous color interpretation <!-- role: reason -->

Storm advisories are often understood via categorical scales; encoding intensity as categories aligns with that mental model and avoids requiring viewers to interpret fine-grained continuous color differences. Using distinct labeling colors increases discriminability across the seven categories, making intensity transitions along tracks easier to see.

**Mechanism:** Category colors support fast classification and comparison across times/paths, while continuous gradients can hide boundaries or imply precision that the forecast does not support.

**Evidence:** The visualization design maps wind speeds to the Saffir–Simpson categories plus tropical depression and tropical storm (seven total), and uses a set of seven distinct colors applied per track segment to make categories highly distinguishable in the forecast display [@liuVisualizingUncertainTropical2019].

**Notes:** The paper also applies a small deadband around category boundaries to reduce rapid color flipping when values hover near thresholds.

## When this applies: forecasts where intensity categories are salient to users <!-- role: context -->

- **User Goal:** Understand how storm intensity may evolve along possible paths.
- **Task:** Identify intensity category at times/locations and compare across tracks.
- **Data:** Wind speed predictions convertible to standard categories.
- **Chart Setting:** Track map where segments can be colored.
- **Audience:** General public or operational stakeholders using category language.
- **Success Criterion:** Viewers can reliably identify category changes along the forecast.

## When not to follow it: when users need exact wind-speed values rather than categories <!-- role: exceptions -->

**Break it when:** The decision requires reading precise wind speed (not category membership). **Why:** Category encoding hides within-category variability.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You lose continuous resolution of wind speed. **Risk:** Too-similar colors or large luminance differences can overemphasize some categories. **Mitigation:** Keep colors discriminable while avoiding extreme value contrast that makes one category dominate.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a smooth rainbow gradient for wind speed and expecting viewers to map it to categories. **Why it fails:** Category boundaries become unclear and interpretation becomes inconsistent.

## Quick tests <!-- role: check -->

**Failure Sign:** Users cannot correctly name the category at a point on the track using the legend. **Quick Check:** Print or screenshot the display and verify each category color is distinguishable from the others and from the map background. **Stronger Test:** Ask users to identify category changes along a path and measure accuracy.

## What to do instead <!-- role: fix -->

- Bin wind speeds into the seven communication categories and assign one color per category.
- Apply the category color to each track segment based on the segment’s starting time point.
- Add a small deadband around category thresholds to reduce jittery back-and-forth color changes.
- Provide a legend that lists categories in order with their corresponding colors.
