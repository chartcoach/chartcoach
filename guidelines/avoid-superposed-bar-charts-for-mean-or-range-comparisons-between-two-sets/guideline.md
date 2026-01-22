---
id: avoid-superposed-bar-charts-for-mean-or-range-comparisons-between-two-sets
title: Avoid superposed bar charts when the task is comparing mean or range between
  two sets
bibliography: references.bib
description: Overlapping two bar-chart datasets reduces precision for mean and range
  comparisons relative to separated layouts.
labels:
- chart:bar
- task:compare
- visual:color
- visual:position
- impact:accuracy
- data:categorical
- audience:novice
- comparison:set-to-set
---

## Avoid overlap for mean/range set comparisons <!-- role: advice -->

Avoid overlapping (superposing) two bar-chart datasets in the same plotting space when users must compare which set has the larger mean or the larger range. Prefer layouts that keep the two sets separated into distinct chart areas.

## Why superposition hurts mean and range comparisons <!-- role: reason -->

When two sets are superposed, the viewer must separate them primarily by color rather than spatial separation, which can make set-level proxies (for mean) and within-set structure proxies (for range) harder to apply cleanly. This interference increases the signal difference required in the data for viewers to perform reliably.

**Mechanism:** Overlap increases perceptual competition between marks, reducing the reliability of the perceptual features that stand in for mean and range judgments.

**Evidence:** In both “biggest mean” and “biggest range” tasks using horizontal bar charts, superposed arrangements produced the lowest precision among tested arrangements [@jardinePerceptualProxiesVisual2020a].

**Notes:** The paper positions this as task-dependent: overlap can be beneficial for other comparison tasks (e.g., item-to-item delta), so the harm is not universal.

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Choose which of two sets is higher on average or more spread out.
- **Task:** Biggest mean or biggest range between two sets.
- **Data:** Two series with multiple items each.
- **Chart Setting:** Static or short animated viewing; separation by color is the main way to distinguish sets in an overlapped design.
- **Audience:** General audiences and non-experts.
- **Success Criterion:** Reliable decisions with small differences between sets.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The comparison is explicitly item-to-item between the two sets (e.g., detecting the largest change for a specific item across two states). **Why:** The same paper summarizes prior evidence that superposition/animation can improve precision for item-focused delta comparisons [@jardinePerceptualProxiesVisual2020a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You lose the compactness of overlay and may need more space for small multiples. **Risk:** Users may need to scan between panels, which can be slower for some tasks. **Mitigation:** Only pay this cost when the task is a set-level judgment of mean or range.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Choosing superposition because it feels like it “minimizes eye movement” without checking task type. **Why it fails:** Mean and range comparisons required larger differences to be judged accurately in superposed designs [@jardinePerceptualProxiesVisual2020a].

## Quick tests <!-- role: check -->

**Failure Sign:** Users focus on individual standout bars or get confused by overlapping marks instead of making a set-level judgment. **Quick Check:** Ask a user to pick the higher-mean or wider-range set in under two seconds; frequent hesitation indicates overlap is interfering. **Stronger Test:** A/B test superposed versus stacked at multiple signal levels (mean/range differences) and compare thresholds.

## What to do instead if you need compactness <!-- role: fix -->

- Use vertically stacked small multiples instead of overlap.
- Use horizontal adjacency as a space-saving alternative to stacking.
- Restrict each panel to the information needed for the judgment (e.g., reduce clutter within each set).
- Re-encode the comparison target directly so the decision does not depend on disentangling overlapped bars.
