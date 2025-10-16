---
id: use-faceted-charts-for-accuracy-not-speed
title: "Use faceted charts for accuracy, but be wary of increased completion time"

tags S
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:small-multiples
  - chart:scatter
  - task:compare
  - task:lookup
  - data:categorical
  - data:cardinality.high
  - data:cardinality.medium
  - visual:position
  - medium:interactive
  - medium:screen
  - access:cognitive-load-risk

evidence:
  strength: medium
  summary: "A large-scale experiment (Kim & Heer, 2018, n=1,920) found that while faceted charts (small multiples) maintain high accuracy, they result in significantly longer task completion times, especially as the number of facets increases (e.g., for cardinalities of 10 or 20)."

sources:
  - type: research
    ref: Kim & Heer, 2018
    url: https://doi.org/10.1111/cgf.13409
    note: "Primary experiment showing that faceted charts (encoding a nominal variable with the 'row' channel) had reasonable accuracy but were ranked significantly lower overall due to longer completion times, likely due to the need to scan and scroll across multiple plots."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This review synthesizes findings on graphical perception to create guidelines for automated systems, confirming the trade-offs between different chart designs like faceting."
    role: related
---

## Guidance

Use faceted charts (small multiples) when accuracy is paramount and viewers have adequate time for analysis. Avoid them when quick, at-a-glance comparisons are the priority, as they tend to increase task completion time.

## Why

Faceted charts are powerful because they use the highly effective channel of position for all variables, dedicating a separate chart to each category. This prevents the clutter and overplotting that can occur when encoding categories with color or shape in a single chart. However, this clarity comes at a cost: viewers must shift their attention between different charts, hold information in working memory to make comparisons, and potentially scroll to see all the facets. This increases cognitive load and total time required for the task.

### Core Principle

There is often a direct trade-off between visual clarity and cognitive/temporal efficiency. Spreading information out (faceting) reduces clutter in any single view but increases the effort required to synthesize information across views.

## When it applies

- When visualizing data with a categorical variable that has a medium-to-high number of unique values (e.g., 5 to 30 categories).
- When the task requires accurate comparisons of patterns (e.g., correlation, distribution) within each category.
- When the viewing medium is a screen, especially an interactive one where scrolling may be necessary.
- In analytical or exploratory settings where thoroughness is more important than speed.

## Exceptions

- When the number of categories (facets) is very small (e.g., 2-4) and all facets can be displayed on a single, non-scrollable screen. The time penalty is significantly reduced in this case.
- For tasks that do not require comparison *between* facets, but only analysis *within* each facet.
- In static print formats where the layout is fixed and optimized for easy scanning.

## Trade-offs

- **Accuracy vs. Speed:** You gain perceptual accuracy and reduce overplotting, but you sacrifice the speed of at-a-glance takeaways.
- **Clarity vs. Density:** Faceting provides a clear view for each category but requires much more screen real estate than a single, more dense chart.

## Signs of Trouble

- **Excessive Scrolling:** Users have to scroll extensively up-and-down or left-and-right to compare different categories.
- **User Frustration:** Viewers complain that it takes too long to find what they're looking for or that they "lose their place" when comparing charts.
- **High "Time to Insight":** In usability testing, it takes users significantly longer to answer questions using the faceted display compared to an alternative, integrated view.
- **Abandonment:** Users in an exploratory setting give up on a task because the cognitive effort of comparing across many facets is too high.

## How to Improve

- **Quick Fix: Optimize Sort Order.** Intelligently sort the facets based on a key metric (e.g., average value, variance). This helps users quickly locate the most important charts and can guide their comparisons.
- **Moderate Redesign: Provide an Overview Chart.** Accompany the faceted view with a single overview chart (e.g., a colored scatterplot) that summarizes the entire dataset. This gives a "big picture" view, and users can then drill down into the facets for detailed, accurate comparisons.
- **Comprehensive Redesign: Implement Interactive Highlighting.** In an interactive setting, allow users to select or hover over a point or region in one facet to highlight corresponding data in all other facets (cross-filtering or brushing). This dramatically reduces the memory load required for comparisons.
