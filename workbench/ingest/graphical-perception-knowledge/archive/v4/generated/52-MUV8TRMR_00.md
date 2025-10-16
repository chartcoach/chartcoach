---
id: group-similar-marks
title: "Group similar marks to speed up visual search"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:scatter
  - chart:heatmap
  - chart:all
  - task:lookup
  - task:find-anomalies
  - data:categorical
  - data:cardinality.high
  - visual:color
  - visual:position
  - medium:screen
  - medium:static
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Gramazio, Schloss, & Laidlaw, 2014
    url: https://doi.org/10.1109/TVCG.2014.2346983
    note: "Experiments 1 and 2 found that spatially grouping marks by color made visual search significantly faster and less affected by the number of marks, compared to random layouts."

examples:
  - type: bad
    description: "In a scatterplot with randomly distributed colors, finding a specific target (e.g., a single purple square) requires a slow, serial search through all points. The marks look like 'confetti'."
  - type: good
    description: "In a scatterplot where colors are spatially clustered, the target 'pops out' from its local group, allowing for rapid, preattentive identification. The human visual system can process each color group as a single object."
---

## Guidance

When the spatial position of marks is not itself encoding a primary variable (e.g., in categorical heatmaps or when reordering is acceptable), group marks with similar properties (like color) together.

## Why

Spatially grouping similar items allows the human visual system to perceive them as a single textured object or "chunk." This enables preattentive processing, where a target with a unique feature (the "pop-out" effect) can be identified almost instantly, regardless of the number of other items. In contrast, a random layout forces a slow, cognitively demanding serial search where each item is inspected one by one.

## When it applies

- **Primary Task is Search:** This is most critical when the user's main goal is to find or locate specific, known targets within a visualization.
- **High Data Density:** The benefits of grouping become exponentially larger as the number of data points (set size) increases. For a small number of points, the difference is negligible; for hundreds or thousands, it's dramatic.
- **Order is Flexible:** Applies to visualizations where the ordering of marks can be changed without losing meaning, such as treemaps, categorical heatmaps (mutation matrices), or bar charts sorted by value.

## Exceptions

- **Position Encodes Meaning:** Do not reorder marks if their position is determined by quantitative data, as in a standard scatterplot where X and Y axes represent continuous variables. In these cases, the spatial structure is the primary insight and should not be altered for grouping.
- **Task is Global Pattern Recognition:** If the goal is to see the overall distribution or correlation, enforcing an artificial grouping might create misleading patterns or obscure the natural structure of the data.

## Trade-offs

- **Ordering by a single property:** Grouping marks by one categorical variable (e.g., color representing region) may prevent you from ordering them by another important variable (e.g., value). You sacrifice one organizational principle for another.
- **Illusory Patterns:** Artificial grouping could inadvertently create visual clusters that imply a relationship between items that doesn't exist in the data.

## Signs of Trouble

- **The "Confetti" Test:** The visualization looks like a random spray of colored dots with no discernible structure, making it hard to focus.
- **Long Search Times:** It takes users a noticeably long time to find a specific item they are looking for. They may scan back and forth across the entire chart.
- **High Cognitive Load:** Viewers report that the chart is "busy," "cluttered," or "hard to read." They have to actively hunt for information rather than seeing it emerge.

## How to Improve

- **Quick Fix: Highlighting.** If you cannot reorder the data, use an interactive feature like a legend filter or search box to highlight all marks belonging to a specific category. This creates a temporary "group" for the user to focus on.

- **Moderate Redesign: Sort by Group.** In charts like bar charts or lists, apply a secondary sort by the categorical variable (e.g., sort first by value, then by region). This will bring similar items closer together.

- **Comprehensive Redesign: Use Small Multiples or Faceting.** Instead of plotting all categories on one chart, break the visualization into a grid of smaller charts (facets), one for each category. This creates the strongest possible grouping and allows for easy comparison across groups.
