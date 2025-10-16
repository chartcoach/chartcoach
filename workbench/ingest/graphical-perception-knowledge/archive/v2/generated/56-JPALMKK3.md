---
id: consider-pie-charts-for-composition
title: "Consider pie charts for simple part-to-whole comparisons"
impact:
  - perceptual
  - cognitive
  - logos
  - ethos
tags:
  - pie-chart
  - bar-chart
  - stacked-bar-chart
  - composition
  - part-to-whole
  - comparison
  - accuracy
  - angle
  - length
sources:
  - type: research
    ref: Redmond, 2019
    url: https://doi.org/10.1109/VISUAL.2019.8933718
    note: "Found that pie charts were more accurate than baseline stacked bar charts for a simple part-to-whole estimation task."
  - type: research
    ref: Eells, 1926
    url: https://doi.org/10.2307/2276953
    note: "Early empirical work suggesting pie charts can be read as quickly and accurately as bar charts for component parts."
  - type: research
    ref: Kosara, 2019
    url: https://doi.org/10.1109/VISUAL.2019.8933547
    note: "Suggests that area, not angle, is the primary visual cue in pie charts, and they perform well for part-to-whole tasks."
examples:
  - type: good
    description: "A pie chart with only two or three slices clearly shows the proportion of each part to the whole, making it easy to see if a component is more or less than half, a quarter, etc."
  - type: bad
    description: "A pie chart with ten slices, some of which are very small. It becomes impossible to accurately compare the parts to each other or estimate their value relative to the whole."

---

## Guidance

For showing a simple part-to-whole relationship (i.e., composition), a pie chart can be as effective, or even more accurate, than a basic stacked bar chart. Don't automatically dismiss it based on conventional wisdom alone.

## Why

Despite their controversial reputation, pie charts are well-suited for the specific task of part-to-whole comparison. People can judge proportions in a pie chart with surprising accuracy, likely by using the circle's shape to provide natural "anchors" at 0%, 25%, 50%, and 75%.

In direct experimental comparisons for estimating the size of a segment, pie charts have been shown to produce smaller errors than simple stacked bar charts that lack a quantitative scale.

## When it applies

- When your primary goal is to show the composition of a single whole.
- When you have a small number of categories (ideally 2-4).
- When the audience needs to quickly judge if a part is a minority, a majority, or a quarter of the whole.

## Exceptions

- **Too many slices:** Avoid using a pie chart with more than 4 or 5 slices. It becomes cluttered and perceptually difficult to distinguish or compare the smaller segments.
- **Comparing parts to parts:** If the main task is to precisely compare the individual parts against *each other* (not against the whole), a standard bar chart is more effective because viewers only need to compare lengths along a common baseline.
- **Comparing across groups:** To compare the composition of multiple different groups, a series of pie charts is very difficult to read. A stacked bar chart or a grouped bar chart is a much better choice.

## Trade-offs

- A pie chart is specialized for a single part-to-whole judgment. A stacked bar chart is more versatile and can be more easily extended to compare compositions across multiple groups.
- While a baseline pie chart may outperform a baseline stacked bar, a stacked bar chart with a clear quantitative scale (e.g., 0% to 100%) will almost always be more accurate than either.

## Evaluate

- [ ] The chart has more than 5 slices.
- [ ] Multiple pie charts are used side-by-side to compare categories.
- [ ] The slices are not ordered in a logical way (e.g., largest to smallest, clockwise).
- [ ] The task is to compare parts to each other, not to the whole.

## Repair

1.  **Too many slices?** Group the smallest, least important slices into a single "Other" category.
2.  **Need to compare parts?** Switch to a simple bar chart, which makes direct length comparisons easy.
3.  **Need to compare compositions?** Use a 100% stacked bar chart, which aligns multiple compositions along a common scale for easier comparison.