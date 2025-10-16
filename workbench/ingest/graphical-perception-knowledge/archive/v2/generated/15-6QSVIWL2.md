---
id: prioritize-position-for-quantitative-data
title: "Prioritize position for encoding quantitative data"

impact:
  - perceptual
  - logos
  - ethical
  - cognitive

tags:
  - position
  - length
  - angle
  - area
  - quantitative
  - comparison
  - ranking
  - scatterplot
  - bar-chart
  - pie-chart
  - bubble-chart
  - treemap

sources:
  - type: research
    ref: Heer & Bostock, 2010
    url: https://doi.org/10.1145/1753326.1753357
    note: "This paper replicated and confirmed the classic perceptual hierarchy for quantitative data using crowdsourced experiments. It found that position on a common scale is judged most accurately, followed by length, then angle, and finally area."
  - type: research
    ref: Cleveland & McGill, 1984
    url: https://doi.org/10.1080/01621459.1984.10478080
    note: "The original seminal research establishing the hierarchy of graphical perception tasks."

examples:
  - type: good
    description: A dot plot or scatter plot, where each data point is placed according to its value along one or two axes. This allows for highly accurate comparisons.
  - type: good
    description: A bar chart, where the endpoint of each bar is positioned along a common scale, making it easy to compare values.
  - type: bad
    description: A bubble chart that uses the area of circles to represent quantities. It is difficult for viewers to accurately judge the precise difference between two bubble sizes.
  - type: bad
    description: A pie chart used for comparing categories that are not adjacent or have similar values. Estimating the difference between angles is much harder than comparing bar lengths.
---

## Guidance

When your audience needs to make precise comparisons between quantitative values, encode those values using position along a common, aligned scale.

## Why

Humans are best at judging differences in position along a single, shared axis. We are less accurate when judging other visual variables like length, angle, or area. This hierarchy of "graphical perception" means that using position leads to more accurate and faster data interpretation, reducing the risk of misjudgment.

The general order of effectiveness for quantitative comparison is:
1.  **Position** (most accurate)
2.  **Length**
3.  **Angle**
4.  **Area** (least accurate)

## When it applies

- This is crucial when the primary task is to **compare**, **rank**, or **look up** specific quantitative values.
- Charts that use position effectively include **scatter plots**, **dot plots**, and **bar charts** (which use both position of the endpoint and length).
- Charts that rely on less accurate encodings for comparison include **pie charts** (angle), **bubble charts** (area), and **treemaps** (area).

## Exceptions

- **Showing part-to-whole relationships:** If the main goal is to show how a few parts make up a whole (e.g., "Category A is about 25% of the total"), a pie chart can be acceptable, though a bar chart is often still clearer.
- **Showing hierarchical structure:** If the goal is to give a general sense of magnitude within a hierarchy, a treemap is appropriate, even though it's poor for precise comparisons between non-adjacent rectangles.
- **Limited space:** Sometimes, area-based charts like treemaps are used because they are more space-efficient for displaying a large number of categories.

## Trade-offs

- Using position can sometimes take up more space than using area. A bar chart with 100 bars will be much longer than a treemap showing the same 100 values. In these cases, you might trade some perceptual accuracy for a more compact layout.

## Evaluate

- [ ] A key quantitative variable intended for precise comparison is encoded by area (e.g., bubble size, treemap rectangle size).
- [ ] A key quantitative variable intended for precise comparison is encoded by angle (e.g., a pie chart slice).
- [ ] The chart requires the user to compare the lengths of non-aligned bars (e.g., comparing the top segments in a stacked bar chart).

## Repair

1.  **If using a pie, donut, or bubble chart for comparisons:** Change it to a simple bar chart. Sort the bars by value to make comparison even easier.
2.  **If you need to show two quantitative variables:** Use a scatter plot, which leverages position on both the X and Y axes.
3.  **If using a stacked bar chart for comparing individual segments:** Change it to a grouped bar chart or a dot plot. This will place all values on a common, aligned baseline, making them easy to compare.