---
id: small-multiples-accuracy-speed-tradeoff
title: "Recognize the accuracy-for-speed trade-off in small multiples"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:small-multiples
  - task:compare
  - data:cardinality.high
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "Kim & Heer (2018) found that while small multiples (faceted charts) are highly accurate for comparison tasks, they result in significantly longer completion times compared to other chart types, especially as the number of categories increases."
sources:
  - type: research
    ref: Kim & Heer, 2018
    url: https://doi.org/10.1111/cgf.13409
    note: "Experiment showing that faceted charts (N:row) had low error rates but significantly longer completion times (see Figure 6 and Section 4.1.1)."
    role: primary
tools: []
examples: []
---

## Guidance

Use small multiples (also known as faceted or trellis charts) when comparison accuracy is more important than speed. Be aware that this approach can significantly increase task completion time, especially with a high number of categories.

## Why

By giving each category its own dedicated chart, small multiples prevent the occlusion and clutter that can occur in overlaid charts (like a single scatterplot with many colored categories). This separation leads to more accurate perception. However, it requires the viewer to visually scan across multiple charts, often involving scrolling, which increases cognitive load and takes more time.

### Core Principle

Reducing visual interference (by separating data into different charts) often comes at the cost of increased cognitive effort (scanning, memory) and interaction cost (scrolling).

## When it applies

- When comparing distributions or patterns across multiple categories.
- When data for different categories would heavily overlap and occlude each other if plotted on a single chart.
- When the number of categories is high (e.g., >10), often requiring scrolling to see all plots.

## Exceptions

- When task completion speed is the highest priority.
- For low-cardinality data where all small plots can be viewed simultaneously on a single screen without scrolling. The time penalty is less severe in this case.
- When the task is to compare a category only to the overall average, not to every other category.

## Trade-offs

- **You gain:** High perceptual accuracy and a clear, uncluttered view of each category.
- **You sacrifice:** Speed of analysis and screen real estate. You also potentially increase cognitive load from scanning and remembering information across different charts.

## Signs of Trouble

- **User Complaints:** Viewers find the task of comparing across the multiples to be slow, tedious, or overwhelming.
- **Scrolling Fatigue:** Users have to scroll extensively to make comparisons, and may miss or forget about plots that are off-screen.
- **Analysis Paralysis:** The sheer number of plots makes it difficult for the viewer to synthesize the information and draw a conclusion.

## How to Improve

- **Quick Fix: Prioritize and Filter.** Order the small multiples by a key metric (e.g., average value) and show only the top N most relevant ones by default. Provide controls (e.g., a "Show More" button) to let users view the rest if needed.

- **Moderate Approach: Overlay a Summary.** On each individual plot, superimpose a faint visual summary of all other categories (e.g., an average line or a 95% confidence band for the overall data). This provides a common baseline for comparison and reduces the need for wide scanning.

- **Comprehensive Redesign: Use an Interactive Drill-Down.** Start with an aggregated view (e.g., a bar chart of averages for all categories). Allow the user to click a category to "drill down" into its detailed small multiple view, or to select multiple categories to compare them side-by-side.
