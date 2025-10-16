---
id: choose-mark-size-by-task
title: "Choose mark size based on the primary analysis task"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:scatter
  - chart:heatmap
  - task:lookup
  - task:trend
  - task:distribution
  - visual:size
  - medium:screen
  - audience:expert

sources:
  - type: research
    ref: Gramazio, Schloss, & Laidlaw, 2014
    url: https://doi.org/10.1109/TVCG.2014.2346983
    note: "A case study with genomics researchers (Section 5) revealed an association between mark size and task type: larger marks were preferred for finding a single target, while smaller marks were preferred for discerning global patterns."

examples:
  - type: bad
    description: A single visualization with medium-sized marks is provided to an analyst who needs to both find specific outliers and assess the overall data distribution. The mark size is a poor compromise, being too small for easy lookup and too large to prevent overplotting that obscures the global trend.
  - type: good
    description: An interactive visualization tool offers a "view mode" toggle. One mode, "Find Outliers," uses large, opaque marks. The other mode, "See Trends," uses small, semi-transparent marks. This allows the user to optimize the view for their current task.
---

## Guidance

Select the size of visual marks based on the user's primary task. Use larger marks for local tasks like finding a specific target, and smaller marks for global tasks like identifying trends or overall patterns.

## Why

The optimal mark size is a trade-off between local detail and a global overview.
- **Larger marks** are easier to see, select, and distinguish individually, which facilitates *local* tasks like looking up a specific point.
- **Smaller marks** reduce overplotting and clutter, allowing the eye to integrate information across a wide area to perceive *global* patterns, such as the shape of a distribution, the density of clusters, or the direction of a trend.
A single, fixed size is often a poor compromise for both tasks.

## When it applies

- **Multi-purpose Visualizations:** This is especially relevant for expert tools and analytical dashboards where users perform a variety of tasks on the same visualization.
- **Dense Data:** The conflict between local and global views is most pronounced in visualizations with high data density, where larger marks would lead to significant overplotting.
- **Expert Audiences:** Expert users (like the genomics researchers in the source paper's case study) are often aware of their shifting analytical needs and can leverage task-specific views effectively.

## Exceptions

- **Single-Purpose Displays:** If a visualization is designed for one specific task (e.g., a chart in a news article that only exists to highlight one specific outlier), then only one mark size is needed.
- **Sparse Data:** When there are very few data points, you can often use marks that are large enough for easy lookup without causing any overplotting, making the trade-off irrelevant.

## Trade-offs

- **Prioritizing One Task Over Another:** Choosing a fixed mark size inherently optimizes for one type of task at the expense of the other.
- **Increased Complexity:** Providing multiple views or interactive controls for mark size adds complexity to the user interface.

## Signs of Trouble

- **Task Switching Complaints:** Users report that the chart is "great for seeing the big picture, but I can't find anything specific," or conversely, "I can see the individual points, but I have no idea what the overall trend is."
- **Inefficient Workflows:** Users are observed manually filtering data or zooming excessively to try and switch between global and local views, indicating the static view is insufficient.
- **User Frustration:** The visualization feels like it's fighting the user's analytical goal.

## How to Improve

- **Quick Fix: Create Two Static Versions.** If the medium is static (e.g., a report), create two versions of the chart: one with large marks, captioned "Highlighting Key Outliers," and another with small, transparent marks, captioned "Overall Data Distribution."

- **Moderate Redesign: Add a View Toggle.** In an interactive tool, add a simple control (e.g., a dropdown or button set) that allows the user to switch between a "Global" view (small marks) and a "Local" view (large marks).

- **Comprehensive Redesign: Zoom-Dependent Mark Sizing.** Implement a semantic zoom feature. When the user is zoomed out, display the data with small marks, transparency, or as an aggregated heatmap to show global patterns. As the user zooms in on a region of interest, automatically increase the mark size (or de-aggregate the data) to reveal individual data points and their local details. This fluidly adapts the view to the user's context without requiring explicit mode switches.
