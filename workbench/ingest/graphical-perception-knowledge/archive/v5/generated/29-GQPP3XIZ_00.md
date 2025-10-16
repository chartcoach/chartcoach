---
id: visualize-deltas-directly
title: "To compare changes between data pairs, visualize the difference directly"

tags:
  - impact:perceptual
  - impact:performance
  - impact:cognitive
  - task:compare
  - task:direction
  - task:filter
  - task:summary-mean
  - chart:bar
  - chart:scatter
  - chart:line
  - data:quantitative

evidence:
  strength: high
  summary: "A 2020 study found directly encoding differences (deltas) improved visual processing efficiency by 25-95% across tasks like searching, judging proportions, and estimating averages, compared to showing individual values side-by-side."

sources:
  - type: research
    ref: Nothelfer & Franconeri, 2020
    url: https://doi.org/10.1109/TVCG.2019.2934801
    note: "Primary experimental study measuring the performance benefit of encoding deltas for data pair relation perception across three distinct tasks (visual search, proportion judgment, average estimation)."
    role: primary
  - type: research
    ref: Srinivasan et al., 2018
    url: https://doi.org/10.1145/3173574.3174158
    note: "A related study that tested variations of multi-series bar charts, including a delta overlay, finding it offered performance benefits."
    role: related

tools:
  - type: learn
    name: "What's the difference?"
    url: https://dl.acm.org/doi/10.1145/3173574.3174158
    description: Research paper evaluating variations of multi-series bar charts for visual comparison tasks.

examples:
  - type: good
    description: "This chart explicitly plots the 'net change' as a separate delta chart. This allows for direct, efficient perception of the differences, rather than requiring mental calculation between 'before' and 'after' bars."
    url: https://i.imgur.com/kP02s1V.png
    caption: A separate chart visualizing the 'Net Change' (delta).
  - type: bad
    description: "This chart shows 'before' and 'after' values as grouped bars. To understand the change, the viewer must mentally calculate the difference for each pair, a slow and error-prone process."
    url: https://i.imgur.com/Vn5v33N.png
    caption: A grouped bar chart showing individual 'before' and 'after' values.
---

## Guidance

When the primary goal is to analyze the relationship between pairs of values (e.g., before/after, treatment/control), create a visualization that explicitly encodes the numerical difference (the "delta") rather than only showing the two original values.

## Why

Displaying deltas offloads the cognitive work of mental subtraction from the viewer to the chart itself. This dramatically speeds up perception and improves accuracy because the brain can directly process a single value (the delta) instead of performing a two-step operation: perceive value A, perceive value B, then calculate their difference.

### Core Principle

Make the most important comparisons the easiest to see. If the difference is the story, show the difference.

## When it applies

- When comparing pairs of quantitative values, such as "before" and "after" measurements, or "treatment" vs. "control".
- When the primary task is to find specific relationships (e.g., "Find all categories that decreased").
- When judging proportions of relationships (e.g., "Are there more increases than decreases?").
- When estimating the average change across all pairs.

## Exceptions

When the absolute magnitude of the original values is critical for context and cannot be lost. For example, a change of +10 is very different when the starting value is 20 versus when it is 2,000. In such cases, showing only the delta removes essential context.

## Trade-offs

- **Loss of Context:** Visualizing only the deltas removes the context of the original values. A large delta might be less significant if the base values are very large.
- **Space:** Creating a separate delta chart requires more screen or page real estate.

## Signs of Trouble

- **Slow Search:** It takes viewers a long time to find a specific relationship (e.g., "find the one item that went down").
- **Back-and-Forth Scans:** Viewers' eyes dart back and forth between paired bars or points to judge the difference for each category.
- **Inaccurate Judgments:** Viewers make mistakes when asked to identify the largest change or count the number of increases vs. decreases.

## How to Improve

- **Quick Fix: Group the Pairs.** In a bar chart, place the "before" and "after" bars next to each other for each category. This is the conventional approach but still relies on inefficient mental calculation. It's a starting point, not a solution.

- **Moderate Approach: Add a Delta Overlay.** On top of a grouped bar or dot plot, superimpose a marker (like a connecting line, dash, or arrow) that explicitly shows the delta. This retains the original values while adding the more efficient relational encoding.

- **Comprehensive Approach: Create a Delta Chart.** Create a separate chart that plots only the delta values for each category. This is the most perceptually efficient method for tasks focused purely on the change, but it sacrifices the context of the original values.