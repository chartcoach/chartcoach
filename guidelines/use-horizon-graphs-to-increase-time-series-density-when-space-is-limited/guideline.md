---
id: use-horizon-graphs-to-increase-time-series-density-when-space-is-limited
title: Use horizon graphs to increase time-series density when space is limited
bibliography: references.bib
description: Compress area charts into layered bands to compare many time series in
  less vertical space while preserving resolution.
labels:
- chart:horizon
- task:compare
- visual:color
- impact:space-efficiency
- data:temporal
- audience:expert
- complexity:advanced
---

## Compress small time-series displays with horizon graph banding <!-- role: advice -->

Use a horizon graph to compare many time series in a small vertical space by splitting values into bands and layering them.

## Band layering increases density while preserving resolution <!-- role: reason -->

Horizon graphs fold and layer an area chart so that the same value resolution fits into less screen space, improving comparability when charts must be small.

**Mechanism:** Mirroring and banding reduce required vertical range while preserving encoded magnitude through color bands and overlap.

**Evidence:** Horizon graphs increase the data density of a time-series view while preserving resolution by dividing the graph into bands and layering them; they have been found more effective than standard plots when chart sizes get quite small [@heerTourVisualizationZoo2010].

**Notes:** The encoding requires learning and may need legends or onboarding cues.

## Context: Many time series, small display regions <!-- role: context -->

- **User Goal:** Compare many time series at once without losing overall patterns.
- **Task:** Detect deviations, spikes, and relative levels across many small charts.
- **Data:** Quantitative time-series values suitable for banding into ranges.
- **Chart Setting:** Dashboards, dense lists, or any setting with tight vertical constraints.
- **Audience:** Viewers willing to learn a compact encoding; often analyst audiences.
- **Success Criterion:** More series fit on screen while patterns remain distinguishable.

## Exceptions: When learnability dominates <!-- role: exceptions -->

**Break it when:** The audience cannot invest time to learn an unfamiliar encoding. **Why:** Horizon graphs “take some time to learn,” so initial comprehension may suffer [@heerTourVisualizationZoo2010].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Immediate readability compared to standard line/area charts. **Risk:** Without clear band/legend cues, viewers misread layered bands. **Mitigation:** Provide clear legends and allow interaction to reveal exact values when needed.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Deploying horizon graphs as a default time-series chart for broad audiences. **Why it fails:** The encoding has a learning curve that can impede comprehension [@heerTourVisualizationZoo2010].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Viewers cannot explain what the color bands represent. **Quick Check:** Ask a viewer to identify whether a value is in the top band or bottom band at a time point; confusion suggests inadequate scaffolding. **Stronger Test:** Compare task accuracy on small-multiple mini-charts versus horizon graphs at the target size.

## Fix: What to do instead <!-- role: fix -->

- Use small multiples with standard line or area charts if space permits.
- Add interaction to zoom or expand a selected series on demand.
- Reduce the number of series shown simultaneously via filtering/search.
- Use an index chart when the primary goal is relative change rather than dense per-series detail.
