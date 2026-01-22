---
id: use-stacked-graphs-only-when-series-are-additive-and-nonnegative
title: Use stacked graphs only when series are additive and nonnegative
bibliography: references.bib
description: Stack area charts to show totals and composition over time only when
  summation is meaningful and values are not negative.
labels:
- chart:stacked-area
- task:part-to-whole
- visual:position
- impact:interpretability
- data:temporal
- audience:general
- complexity:intermediate
---

## Stack time series only for meaningful, nonnegative totals <!-- role: advice -->

Use a stacked graph to show aggregate time-series patterns only when the component series should be summed and the data are nonnegative.

## Stacking encodes totals but distorts individual trend reading <!-- role: reason -->

Stacking communicates how components contribute to a total, but components above the baseline lose a stable reference line, making their trends harder to judge.

**Mechanism:** A shared baseline supports accurate trend perception; stacking shifts baselines for most layers, complicating comparisons across time for individual series.

**Evidence:** Stacked graphs depict aggregate patterns by stacking area charts, but they do not support negative numbers and are meaningless when values should not be summed (for example, temperatures), and stacking can make trends atop other curves difficult to interpret [@heerTourVisualizationZoo2010].

**Notes:** Interactive search and filtering are often used to compensate for interpretation difficulties.

## Context: Additive composition over time <!-- role: context -->

- **User Goal:** Understand total magnitude over time and how categories contribute to it.
- **Task:** Assess composition changes and overall aggregate pattern.
- **Data:** Multiple nonnegative time series where summation is meaningful.
- **Chart Setting:** Often interactive, with filtering/search to isolate layers.
- **Audience:** General audiences; interpretability depends on legibility and layer count.
- **Success Criterion:** Viewers can read the total and identify major contributors without misreading layer trends.

## Exceptions: When stacking breaks semantics or readability <!-- role: exceptions -->

- **Break it when:** The series can be negative. **Why:** The stacked form does not support negative numbers [@heerTourVisualizationZoo2010].
- **Break it when:** The values should not be summed. **Why:** The resulting total is not meaningful (for example, temperatures) [@heerTourVisualizationZoo2010].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Individual-series comparability is reduced for layers away from the baseline. **Risk:** Viewers may misjudge slopes or attribute changes to the wrong component due to shifting baselines. **Mitigation:** Reduce the number of layers shown at once through filtering or grouping.

## Mistakes: Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a stacked graph to compare precise trends of individual categories. **Why it fails:** Most layers lack a consistent baseline, making trend decoding harder [@heerTourVisualizationZoo2010].
- **Mistake:** Stacking measurements that should not be aggregated. **Why it fails:** The visualization implies a meaningful total where none exists [@heerTourVisualizationZoo2010].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Viewers disagree on whether a non-baseline layer increased or decreased between two times. **Quick Check:** Hide all but one layer and see if the perceived trend changes; if so, stacking is distorting interpretation. **Stronger Test:** Ask viewers to estimate changes for a mid-stack category; high error suggests switching designs.

## Fix: What to do instead <!-- role: fix -->

- Use small multiples so each series has its own baseline.
- Use an index chart if relative change comparisons are the goal.
- Add interactive filtering/search to isolate subsets of layers.
- Use a different aggregation view (for example, show only the total and provide drill-down).
