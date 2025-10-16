---
id: faceted-charts-increase-time
title: "Use faceted charts cautiously as they can increase completion time"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:small-multiples
  - task:compare
  - task:rank
  - data:cardinality.high
  - medium:interactive
  - medium:screen
  - access:cognitive-load-risk
sources:
  - type: research
    ref: Kim & Heer, 2018
    url: https://doi.org/10.1111/cgf.13409
    note: "Section 4.1.1, 'Faceted charts (row) require more time,' is the direct source. The study found that while faceted charts had reasonable accuracy, they resulted in 'notably lower ranking' due to 'significantly longer completion times' (Figure 6)."
---

## Guidance

Be aware that using faceted charts (small multiples) can significantly increase the time it takes for a user to complete comparison tasks, even though they can be highly accurate.

## Why

Faceted charts break a complex visualization into a series of smaller, simpler charts. While this is excellent for avoiding overplotting and showing the distribution of individual categories, it forces the user to perform a more complex visual scanning task. To compare values, the user must find the relevant points in different plots, hold them in working memory, and mentally compare them. This process is more time-consuming and cognitively demanding than comparing points within a single, unified plot, especially if the facets require scrolling to view.

## When it applies

- The primary task involves **comparing** or **ranking** values across different categories.
- You are using **small multiples (faceted charts)**, where data is split into a grid of plots.
- The visualization is presented on a screen, where the full grid of charts may not be visible at once, requiring **scrolling**.
- The number of categories (facets) is large (e.g., more than 10).

## Exceptions

- **Avoiding Overplotting is Paramount:** When a single plot would be an unreadable, overplotted mess (e.g., a spaghetti plot of 20 time series), the clarity gained by faceting is worth the trade-off in comparison speed. The alternative is worse.
- **Task is "Within-Category" Analysis:** If the primary goal is for the user to understand the pattern *within* each category感染 (e.g., the trend of a single time series, the shape of a single group's distribution), faceting is an excellent choice. The slower cross-category comparison is a secondary concern.
- **All Facets are Visible:** If the number of facets is small enough that they can all be displayed on a single, non-scrolling screen, the time penalty is reduced.

## Trade-offs

- **Speed vs. Clarity:** You trade faster task completion time for a less cluttered, more readable view of each individual category. Faceting prioritizes clarity over speed of comparison.
- **Space vs. Simplicity:** Small multiples require much more screen real estate than a single, combined plot.

## Signs of Trouble

- **Excessive Scrolling:** Users have to scroll extensively, both horizontally and vertically, to find and compare the charts they need.
- **Losing Context:** Users report "getting lost" in the grid of charts and forgetting what they were comparing.
>"Back-and-Forth" Eye Movements: You observe users repeatedly scanning back and forth between two distant charts in the grid, a sign of high cognitive load.
- **Slow Performance:** Tasks that should be quick take users a surprisingly long time to complete.

## How to Improve

- **Quick Fix: Optimize the Sort Order.** Thoughtfully arrange the facets in the grid. Sorting them by a key metric (e.g., a-z by name, or descending by average value) can help users locate relevant charts faster and make comparisons between adjacent plots easier.

- **Moderate Redesign: Provide Interactive Highlighting.** Implement hover or click interactions that highlight a point or series in one facet and also highlight the corresponding points in all other facets. This helps the user track a specific entity across the small multiples. You could also provide interactive filters to reduce the number of visible facets.

- **Comprehensive Approach: Reconsider the Task and Chart.** If rapid cross-category comparison is the *most* important task, faceting may not be the right approach.
  - For comparing a single value across many categories, a **bar chart or dot plot** is much faster.
  - For comparing trends of multiple time series, a **single line chart with highlighting** or a "braided graph" might be better than a full grid of spaghetti plots. Choose the chart that directly supports the primary task.