---
id: label-every-data-encoding-with-a-legend-or-direct-keys
title: Label Every Data Encoding Close to the Marks
bibliography: references.bib
description: Ensure every visual element representing data is labeled clearly, and
  place labels as close to the data as possible.
labels:
- chart:general
- task:identify
- visual:label
- impact:clarity
- data:general
- audience:general
- process:workflow
- source:datawrapper
---

## The Rule <!-- role: advice -->

Label every visual element that encodes data, and place the label as close to the element as possible.

## The Logic <!-- role: reason -->

Keys/legends prevent ambiguity about what marks mean, and proximity reduces the effort of matching labels to data, saving readers time and energy—an explicit recommendation in the “Add legends/keys” section of [@muth_better_charts_2017].

- **The Principle:** Reduce lookup cost through proximity labeling
- **The Evidence:** [@muth_better_charts_2017]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which line/bar/area corresponds to which category without confusion.
- **Data Type:** Multi-category charts or any chart using color/shape/line style to distinguish series.
- **Audience:** Readers scanning quickly who may abandon the chart if decoding takes effort.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart has only one encoded series and its identity is unambiguous from nearby text/description.
- **Reason:** A legend would be redundant; Muth’s rule is about ensuring every encoding is labeled “somehow” when needed [@muth_better_charts_2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Space and potential visual clutter, especially with many categories.
- **The Risk:** Labels can overlap marks if not placed carefully [@muth_better_charts_2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a legend that is far from the plotted data while also using similar colors.
- **Why it fails:** Readers must “travel far distances with the eye,” increasing errors and friction [@muth_better_charts_2017].

## How to Check <!-- role: check -->

- **Visual Sign:** You find yourself tracing back and forth between marks and a distant legend to decode categories.
- **The Test:** Time yourself: can you correctly name a series in under 2 seconds? If not, labels are too far/unclear [@muth_better_charts_2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move the key/legend closer to the data region.
- **Best Fix:** Replace or supplement the legend with labels placed next to the relevant marks (where feasible) so decoding is immediate [@muth_better_charts_2017].
