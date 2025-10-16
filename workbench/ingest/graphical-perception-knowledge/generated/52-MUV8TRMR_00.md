---
id: group-similar-marks
title: "Group similar items to speed up visual search"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:heatmap
  - chart:treemap
  - chart:bar
  - chart:small-multiples
  - task:lookup
  - task:filter
  - data:categorical
  - visual:color
  - visual:position
  - medium:screen
  - medium:static
  - access:cognitive-load-risk
evidence:
  strength: high
  summary: "Gramazio et al. (2014, n=31) found that spatially grouping marks by color dramatically reduced search time compared to random layouts (p<0.001). In grid-based layouts, search time in grouped displays was almost unaffected by the number of items, demonstrating a strong 'pop-out' effect."
sources:
  - type: research
    ref: Gramazio, Schloss, & Laidlaw, 2014
    url: https://doi.org/10.1109/TVCG.2014.2346983
    note: "Primary study (n=15 in Exp. 1, n=16 in Exp. 2) showing that search performance was significantly faster (p<0.001) and less affected by set size in grouped layouts compared to random layouts."
    role: primary
---
## Guidance

When the user's task is to find a specific item, group similar marks together spatially (e.g., by color).

## Why

Spatial grouping allows the human visual system to use pre-attentive processing. Instead of scanning every individual item (serial search), the viewer perceives distinct groups as single 'objects'. This allows a known target to 'pop out' from its surroundings, significantly reducing cognitive load and the time required to find it.

### Core Principle

Make the most important comparisons and searches the easiest to perform by leveraging pre-attentive attributes like spatial proximity.

## When it applies

- When the primary user task is to locate a known target (`lookup`) or find all items of a certain type (`filter`).
- In visualizations where the position of marks is not strictly determined by data values, such as heatmaps, treemaps, or non-value-sorted bar charts.

## Exceptions

- When the position of each mark is defined by its quantitative data values, such as in a scatterplot or a map. In these cases, the data's structure dictates the position.
- When the grouping might create a misleading secondary pattern, such as implying a continuous gradient or order where none exists (e.g., ordering categorical colors in a way that resembles a rainbow).

## Trade-offs

- Grouping by one characteristic (e.g., color) may conflict with another desired ordering principle (e.g., sorting alphabetically or by a quantitative value).
- It may require additional design effort to determine the optimal clustering or arrangement of groups.

## Signs of Trouble

- **The "Where's Waldo" effect:** Users have to scan the entire visualization item by item to find what they're looking for, even when the target's color is known.
- **Color Chaos:** Marks of the same category are scattered randomly throughout the display, forcing the user's eye to jump around.

## How to Improve

- **Quick Fix: Sort by Category.** In a list, table, or bar chart, apply a secondary sort on the categorical variable to bring similar items into adjacent rows.
- **Moderate Approach: Reorder the Layout.** In a heatmap or small multiples grid, reorder the rows and columns using a clustering algorithm to create contiguous, monochromatic blocks.
- **Comprehensive Approach: Redesign for Grouping.** If possible, choose a chart type that inherently supports grouping, like a treemap, where sub-categories are nested within larger ones.