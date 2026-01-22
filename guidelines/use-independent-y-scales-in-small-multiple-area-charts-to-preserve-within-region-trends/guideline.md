---
id: use-independent-y-scales-in-small-multiple-area-charts-to-preserve-within-region-trends
title: Use independent y-scales in small-multiple area charts when the task is within-region
  trend detection
bibliography: references.bib
description: Use per-panel scaling to preserve visibility of temporal trends within
  each region when magnitudes differ greatly across regions.
labels:
- chart:area
- task:trend
- visual:scale
- impact:trend-detection
- data:temporal
- audience:expert
- complexity:advanced
- domain:health
---

## Scale each small multiple independently to reveal local temporal change <!-- role: advice -->

When comparing temporal trends across multiple regions with widely different magnitudes, give each region’s area chart its own y-axis scale if the user’s primary task is to detect within-region change.

## Why independent scales keep small changes visible <!-- role: reason -->

A shared global scale can flatten smaller-range series, making meaningful local variation hard to perceive; independent scales preserve the shape and variability needed for within-unit trend detection.

**Mechanism:** Per-panel scaling increases perceptual resolution for each series, improving detectability of changes that would be visually compressed under a global maximum.

**Evidence:** For region-level mortality rate area charts, separate y-axes were used so users could identify trends for specific regions; a shared scale would make lower-magnitude regions appear constant due to compression against a much larger maximum [@olaSimpleChartsDesign2016].

**Notes:** This supports within-region trend tasks; it is not ideal for direct cross-region magnitude comparison.

## When this applies in health data visualization <!-- role: context -->

- **User Goal:** See whether mortality is rising/falling within each region over time.
- **Task:** Within-series trend detection across multiple small multiples.
- **Data:** Time series for many regions with large differences in absolute magnitude.
- **Chart Setting:** Small-multiple area charts or similar continuous temporal views.
- **Audience:** Analysts examining regional trajectories.
- **Success Criterion:** Users can correctly identify direction and rough magnitude of change within each region.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary task is direct comparison of absolute levels between regions. **Why:** Independent scales can mislead magnitude comparisons across panels [@olaSimpleChartsDesign2016].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Cross-panel comparability of absolute values. **Risk:** Users may incorrectly infer that similarly shaped areas represent similar magnitudes. **Mitigation:** Provide clear labeling of per-panel scales and offer an alternative view for level comparison.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Forcing a shared y-scale across regions with extreme range differences. **Why it fails:** Smaller-range regions lose visible variation, undermining the trend task [@olaSimpleChartsDesign2016].

## Quick tests <!-- role: check -->

**Failure Sign:** Several panels look flat despite known changes in the data. **Quick Check:** Compute each region’s range; if max/min ratios differ greatly, a single scale will compress some series. **Stronger Test:** Ask users to identify the steepest increase within a low-magnitude region and verify they can do so without zooming.

## What to do instead <!-- role: fix -->

- Use per-panel y-axis scaling when the intended judgment is within-region change.
- Add explicit per-panel axis labels so users understand each scale.
- Provide a companion ranked list or aligned comparison view for absolute levels at a selected year.
- Allow interaction to toggle between independent and shared scaling depending on task focus.
