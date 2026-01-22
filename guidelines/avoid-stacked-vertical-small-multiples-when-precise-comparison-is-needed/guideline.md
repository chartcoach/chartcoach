---
id: avoid-stacked-vertical-small-multiples-when-precise-comparison-is-needed
title: Avoid stacked (vertical) small multiples for precise two-series bar-chart comparisons
bibliography: references.bib
description: Stacked vertical small multiples led to poorer comparison performance
  than adjacent or mirrored layouts in bar-chart correlation judgments, and performed
  very poorly in a bar-chart biggest-mover task.
labels:
- chart:bar
- task:compare
- visual:position
- impact:accuracy
- data:categorical
- audience:novice
- layout:small-multiples
---

## Stacked small multiples as a low-performing comparison layout <!-- role: advice -->

Avoid stacking two bar charts vertically when users must make precise comparisons between corresponding values across the two series. Prefer a layout that aligns corresponding items with minimal search for correspondence.

## Vertical separation increases matching and memory demands <!-- role: reason -->

When the compared elements are separated into distinct regions, the viewer must repeatedly map each item in one chart to its counterpart in the other, increasing correspondence effort and reliance on visual working memory. This can reduce discrimination performance for comparison tasks.

**Mechanism:** Vertical separation increases cross-view matching work, making fine-grained discrimination harder under brief viewing.

**Evidence:** In the bar-chart correlation task, stacked small multiples required a higher signal (higher titers) than adjacent small multiples [@ondovFaceFaceEvaluating2019a]. In the bar-chart maximum-delta task, stacked and adjacent layouts exhibited strong floor effects and low accuracy near the maximum allowed difficulty scaling, indicating the task was highly difficult in stacked bar charts under the tested conditions [@ondovFaceFaceEvaluating2019a].

**Notes:** The bar-chart max-delta result for stacked layouts is limited by a titer cap and floor effects, but it still indicates severe difficulty under that study setup.

## Context where stacked layouts are risky <!-- role: context -->

- **User Goal:** Make accurate comparisons between two series across shared categories.
- **Task:** Correlation-as-similarity judgments, or identifying the largest change between series.
- **Data:** Two snapshots/conditions with aligned categories.
- **Chart Setting:** Brief viewing time, or situations where users cannot carefully scan back and forth.
- **Audience:** General audiences or non-expert users doing quick judgments.
- **Success Criterion:** Lower error rate and ability to discriminate smaller differences.

## Exceptions for stacked small multiples <!-- role: exceptions -->

- **Break it when:** Vertical stacking is required by narrow screen constraints and the task tolerates slower, more deliberate reading. **Why:** The layout may be acceptable when speed/threshold precision is not the primary success criterion.

## Costs of avoiding stacked layouts <!-- role: costs -->

**Sacrifice:** Alternative layouts may require more horizontal space or introduce unfamiliar conventions (e.g., mirroring). **Risk:** Forcing a non-stacked layout into a constrained space can shrink charts and reduce legibility. **Mitigation:** Use responsive design to switch layouts based on available width.

## Mistakes with stacked small multiples <!-- role: mistakes -->

**Mistake:** Assuming aligned baselines in a vertical stack automatically make comparisons easy. **Why it fails:** The main burden can be matching corresponding items across separated views, not judging each chart independently [@ondovFaceFaceEvaluating2019a].

## Check for stacked-layout failure <!-- role: check -->

**Failure Sign:** Users frequently lose track of which bar in the top chart corresponds to which bar in the bottom chart. **Quick Check:** Time how long it takes a few users to compare one named category across the two charts; long search indicates correspondence trouble. **Stronger Test:** Run a small accuracy test on your key comparison task and compare stacked versus adjacent or mirrored.

## Fixes if you must keep a stacked layout <!-- role: fix -->

- Add strong alignment aids that help users trace correspondence between charts (e.g., consistent ordering and clear category labels).
- Switch to adjacent small multiples when width allows to align items along a shared positional axis.
- Use a mirrored layout for exactly two series to reduce the correspondence distance.
- Replace the two-view comparison with a single-view encoding that directly represents change.
