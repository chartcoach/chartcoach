---
id: reduce-marks-if-ungrouped
title: "Reduce mark quantity if data cannot be spatially grouped"

tags:
  - impact:perceptual
  - impact:performance
  - chart:scatter
  - chart:all
  - task:lookup
  - task:find-anomalies
  - data:cardinality.high
  - visual:position
  - medium:screen
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Gramazio, Schloss, & Laidlaw, 2014
    url: https://doi.org/10.1109/TVCG.2014.2346983
    note: "Experiments showed that for random (ungrouped) layouts, search time increased linearly with the number of marks. For grouped layouts, the number of marks had little to no effect on search time."

examples:
  - type: bad
    description: A scatterplot showing 5,000 individual, randomly-colored data points. Finding a specific point requires scanning through all 5,000, which is extremely slow and inefficient.
  - type: good
    description: Instead of plotting all 5,000 points, the data is summarized. The chart shows the top 100 most significant points and a note explains that 4,900 other points are not shown. This allows the user to quickly find key items.
---

## Guidance

If marks in a visualization cannot be spatially grouped by a distinguishing feature (like color), consider reducing the number of marks shown to improve visual search performance. The time it takes to find a target in an ungrouped layout is directly proportional to the total number of marks.

## Why

When marks are not grouped, the visual system has no preattentive cues to guide it. It must resort to a serial search, inspecting each item one by one until the target is found. This is a slow, linear process; doubling the number of items roughly doubles the search time. In contrast, when marks are grouped, the system can quickly dismiss entire groups, making the search much more efficient. If grouping is not an option, the only way to shorten a serial search is to reduce the number of items to search through.

## When it applies

- **Ungrouped Layouts:** This is critical for visualizations with a random or meaningful-but-ungrouped spatial layout, such as standard scatterplots where position is determined by data, or "confetti"-style categorical plots.
- **Search or Lookup Tasks:** The guideline is most relevant when the primary task is to find a known item or identify specific anomalies.
- **High Cardinality / High Density:** The problem is most acute in visualizations with hundreds or thousands of data points.

## Exceptions

- **Showing Every Point is Essential:** In some contexts (e.g., fraud detection, data validation), it may be critical to see every single data point to ensure nothing is missed. In these cases, performance may be a secondary concern to completeness.
- **Global Trend Analysis:** If the task is to understand the overall distribution, density, or shape of the data, then showing all points (often with transparency or as smaller marks) is necessary. Summarization would remove the very information the user needs.

## Trade-offs

- **Completeness vs. Performance:** Reducing the number of marks improves search speed but means you are not showing the complete dataset. This could cause users to miss important context or outliers that were filtered out.
- **Information Loss:** Summarization and aggregation are inherently lossy. The designer must make an informed decision about *what* to filter out, which may introduce bias.

## Signs of Trouble

- **Linear Slowdown:** As you add more data, the visualization becomes proportionally slower to use for finding things.
- **"Needle in a Haystack":** Users describe the task of finding a point as looking for a "needle in a haystack."
- **Overplotting:** The marks are so dense that they form an illegible mass, making a point-by-point search impossible anyway.
- **User Abandonment:** Users give up on finding a specific item because it takes too long.

## How to Improve

- **Quick Fix: Highlighting and Filtering.** Provide interactive controls that allow users to filter the data dynamically. This empowers the user to reduce the number of marks on-demand based on their current query, without the designer having to make a fixed choice.

- **Moderate Redesign: Data Summarization.** Instead of plotting all data, apply a rule to show only the most important points (e.g., top 100 by value, most recent items, or statistical outliers). Always include a clear note explaining that the data is summarized (e.g., "Showing 100 of 5,000 total items").

- **Comprehensive Redesign: Aggregation.** Change the visualization type to one that uses aggregation. For example, convert a dense scatterplot into a 2D histogram or a hexbin map. This groups points into bins, and color can then be used to show the density within each bin. This maintains the sense of distribution while dramatically reducing the number of rendered objects.
