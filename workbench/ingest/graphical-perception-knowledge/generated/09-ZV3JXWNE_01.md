---
id: prefer-high-precision-charts-for-correlation
title: "For correlation tasks, prefer charts from high-precision groups over those from low-precision or chance-level groups"
tags:
  - impact:perceptual
  - task:correlation
  - data:quantitative
  - chart:scatter
  - chart:parallel-coordinates
  - chart:bar
  - chart:line
  - chart:pie
  - chart:area
evidence:
  strength: high
  summary: "Kay & Heer (2016) established a partial ranking of visualizations for correlation tasks. Their Bayesian analysis showed clear performance tiers, with the 'high precision' group being 1.5-2x more precise than the 'medium' group, and the 'low precision' group being 1.5-3x more precise than the 'chance-level' group."
sources:
  - type: research
    ref: Kay & Heer, 2016
    url: https://doi.org/10.1109/TVCG.2015.2467671
    note: "Established four distinct performance groups for correlation visualizations: 'high precision', 'medium precision', 'low precision', and 'indistinguishable from chance'. Quantified the performance gap between groups (Figure 8)."
    role: primary
  - type: research
    ref: Harrison et al., 2014
    url: https://doi.org/10.1109/TVCG.2014.2346979
    note: "The original study providing the data for the performance groups identified by Kay & Heer."
    role: supporting
---

## Guidance

When visualizing correlation, select a chart type from a group empirically shown to have higher perceptual precision. Avoid chart types that perform no better than random chance for this task.

## Why

Not all visualizations are equally effective for perceiving correlation. Using a chart from a low-performing group (e.g., radar chart, stacked area chart) can lead viewers to misjudge or completely miss correlations that would be apparent in a high-performing chart (e.g., scatterplot). The performance difference between groups is significant.

The empirically-derived performance groups are, from best to worst:
1.  **High Precision:** Scatterplot (positive/negative), Parallel Coordinates (negative).
2.  **Medium Precision:** Ordered Line (positive), Stacked Bar (negative), Donut Chart (negative), Parallel Coordinates (positive).
3.  **Low Precision:** Stacked Line (positive/negative), Stacked Area (negative), Ordered Line (negative).
4.  **Indistinguishable from Chance:** Radar Chart (positive/negative), Donut Chart (positive), Line Chart (negative), Stacked Bar (positive), Stacked Area (positive).

## When it applies

- When choosing a chart type to represent the correlation between two or more variables.
- When evaluating an existing visualization to see if a more effective alternative exists for its primary task.

## Exceptions

- A chart from a lower-performing group may be acceptable if the primary task is not correlation (e.g., a line chart's primary purpose is showing a trend over time, not just correlation).
- Strong domain conventions may favor a specific chart type, but be aware of the perceptual trade-offs.

## Trade-offs

- Choosing a higher-precision chart may require a less familiar format for your audience (e.g., moving from a conventional but poor-performing stacked bar chart to a more effective scatterplot).
- Higher-precision charts may have other limitations (e.g., scatterplots can have overplotting issues).

## Signs of Trouble

- **Chance-Level Performance:** The chosen visualization (e.g., a radar chart used to show correlation) is known to perform at or near chance level for this specific task.
- **Obscured Relationships:** A known strong correlation in the data is not visible to viewers in the chosen chart.
- **Poor Alternative:** The chart uses an encoding like angle or unaligned length to represent correlation, which are known to be perceptually weak.

## How to Improve

- **Upgrade to a High-Precision Chart:** If possible, switch to a scatterplot. For judging negative correlation specifically, a parallel coordinates plot is also a high-precision option. This provides the most significant performance gain.

- **Move Up One Tier:** If a full redesign is not possible, try to move from a "chance-level" or "low precision" chart to a "medium precision" one. For example, to show positive correlation, replacing a stacked bar chart (chance-level) with an ordered line chart (medium precision) is a measurable improvement.
