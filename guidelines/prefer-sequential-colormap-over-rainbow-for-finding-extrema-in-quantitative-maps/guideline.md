---
id: prefer-sequential-colormap-over-rainbow-for-finding-extrema-in-quantitative-maps
title: Prefer a sequential colormap over a rainbow scheme for finding extrema in quantitative
  maps
bibliography: references.bib
description: For finding minimum/maximum values on quantitative maps, sequential color
  saturation encodings outperform rainbow hue encodings in accuracy and speed.
labels:
- chart:map
- task:find-extremum
- visual:color
- impact:accuracy
- data:quantitative
- audience:novice
- domain:cartography
---

## Use sequential color saturation for extrema-finding on maps <!-- role: advice -->

Use a sequential color saturation scheme instead of a rainbow hue scheme when users must identify minimum or maximum values in quantitative map-like visuals.

## Why sequential saturation helps extrema-finding <!-- role: reason -->

Sequential saturation provides a clearer ordered cue for magnitude judgments, which supports reliably detecting extremes.

**Mechanism:** A consistent dark-to-light progression supports ordinal interpretation, making it easier to spot the highest/lowest regions without mentally re-ordering hues.

**Evidence:** In extrema-finding tasks, sequential schemes (both choropleth and isarithmic conditions) ranked above rainbow schemes in both accuracy and time, with significant differences reported between sequential and rainbow conditions [@golbiowskaRainbowDashIntuitiveness2022]. This evidence is collated as a perception-driven guideline for recommendation contexts [@zengReviewCollationGraphical2023].

**Notes:** This guideline concerns task performance for extrema-finding, not aesthetics or preference.

## When extrema-finding with color applies <!-- role: context -->

- **User Goal:** Quickly and correctly identify where the minimum or maximum values occur.
- **Task:** Find extremum.
- **Data:** Quantitative values encoded as ordered color classes.
- **Chart Setting:** Static map-like display (e.g., choropleth or isarithmic/continuous field view).
- **Audience:** General audiences or learners performing map-reading tasks.
- **Success Criterion:** Higher accuracy and faster completion.

## When not to follow this extrema rule <!-- role: exceptions -->

**Break it when:** The task is not about identifying extremes but about recalling specific hues later. **Why:** The rainbow scheme can support hue recall better than a sequential scheme in recall-oriented tasks.

## Tradeoffs of sequential over rainbow <!-- role: costs -->

**Sacrifice:** You may lose distinct named hues that can be easy to verbally reference.\
**Risk:** Users may still struggle if adjacent classes are too similar in lightness.\
**Mitigation:** Ensure adjacent classes are perceptually distinct enough for the display context.

## Common mistakes in extrema-finding palettes <!-- role: mistakes -->

**Mistake:** Using a rainbow palette and assuming users will interpret it as an ordered scale. **Why it fails:** Users can have low agreement on hue order, harming ordered judgments like extrema-finding.

## Quick tests for extrema-finding readiness <!-- role: check -->

**Failure Sign:** Users hesitate or disagree on which region is the “highest” or “lowest” when using the color encoding.\
**Quick Check:** Ask a few readers to point to the maximum and minimum regions; watch for inconsistent choices.\
**Stronger Test:** Run a small timed task (find min/max) comparing candidate palettes and keep the one with higher accuracy.

## What to do instead of rainbow for extrema-finding <!-- role: fix -->

- Switch the quantitative color encoding from rainbow hue to a sequential saturation scheme.
- Reduce the cognitive load by adding clear legend ticks and labeling the min and max endpoints.
- If extremes are critical, add an additional cue (e.g., outline or annotation) on the extreme regions.
- If color ordering remains ambiguous, use a position-based summary view alongside the map to show ranked extremes.
