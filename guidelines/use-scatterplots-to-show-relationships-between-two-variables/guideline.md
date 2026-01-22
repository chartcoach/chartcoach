---
id: use-scatterplots-to-show-relationships-between-two-variables
title: Use a scatter plot to show correlations between two variables
bibliography: references.bib
description: Scatter plots are the go-to chart type for exploring and communicating
  how two variables relate.
labels:
- chart:scatter
- task:correlate
- visual:position
- impact:clarity
- data:multivariate
- audience:mainstream
- complexity:intermediate
---

## Use scatter plots for relationship questions <!-- role: advice -->

Use a scatter plot when your core question is whether two variables move together across cases (countries, districts, people, items). If point size encodes a third variable, treat it as a bubble chart.

## Why scatter plots fit correlation tasks <!-- role: reason -->

Scatter plots map two variables to two axes, making association patterns visible through clustering, slopes, and outliers.

**Mechanism:** Position on two perpendicular scales supports judging co-variation and spotting exceptions, which is difficult in one-dimensional charts.

**Evidence:** Scatter plots are recommended for exploring and showing how categories relate to each other, with “bubble chart” used when symbols vary in size [@muth_chart_types_guide_2025].

**Notes:** Relationship visibility can degrade when points overlap heavily.

## Context <!-- role: context -->

- **User Goal:** Understand whether higher X tends to correspond to higher (or lower) Y.
- **Task:** Detect correlation, clusters, and outliers.
- **Data:** Two quantitative variables across many cases; optional third variable for size.
- **Chart Setting:** Analysis and explanatory communication.
- **Audience:** Mixed audiences, potentially less familiar with multivariate charts.
- **Success Criterion:** Readers can describe the direction/shape of association and identify notable outliers.

## Exceptions <!-- role: exceptions -->

**Break it when:** Overplotting makes the point cloud unreadable and hides density patterns. **Why:** Individual dots no longer convey where most cases lie [@muth_chart_types_guide_2025].

## Costs <!-- role: costs -->

**Sacrifice:** Scatter plots can feel complex for mainstream audiences. **Risk:** Overlap and visual noise can obscure the message. **Mitigation:** Treat readability as a prerequisite and consider density-based alternatives when overlap is high.

## Mistakes <!-- role: mistakes -->

**Mistake:** Using a scatter plot for a mainstream audience without checking whether the key pattern is visible amid overlapping points. **Why it fails:** The intended relationship can disappear in a “sea of dots” [@muth_chart_types_guide_2025].

## Check <!-- role: check -->

**Failure Sign:** Most points overlap, creating a dark blob with no discernible structure. **Quick Check:** Reduce opacity mentally; if you still can’t see density differences, the scatter is too crowded. **Stronger Test:** Ask a reader to describe where most points are; if they can’t, use a density alternative.

## Fix <!-- role: fix -->

- Switch to a two-dimensional histogram (2D histogram) to show density when points overlap.
- Reduce the number of plotted cases if the message can be supported with a subset.
- Use annotation to highlight the key pattern and important outliers when the overall cloud is still readable.
- Consider introducing the topic with simpler charts before showing the scatter plot if audience complexity tolerance is low [@muth_chart_types_guide_2025].
