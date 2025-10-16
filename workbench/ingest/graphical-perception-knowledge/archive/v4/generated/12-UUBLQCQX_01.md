---
id: limit-categorical-colors
title: "Limit the number of colors in a categorical palette"

tags:
  - impact:perceptual
  - impact:cognitive
  - visual:color
  - data:categorical
  - data:cardinality.high
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Gramazio, Laidlaw, & Schloss, 2017
    url: https://doi.org/10.1109/TVCG.2016.2598918
    note: "Experiment 1 found that participant error rates in a discrimination task increased significantly as palette size grew from 3 to 5 to 8 colors (P1 in the paper)."

tools:
  - type: implement
    name: Colorgorical
    url: http://vrl.cs.brown.edu/color
    description: A tool whose performance degrades as the number of requested colors increases, illustrating the difficulty of the problem.

examples:
  - type: good
    description: A bar chart with 4-5 distinct categories, each with a clearly different color. Viewers can easily match the bars to the legend.
  - type: bad
    description: A line chart with 10 different colored lines. The legend becomes a "wall of colors" that is cognitively overwhelming to match to the tangled lines in the chart.
---

## Guidance

Use as few colors as possible when encoding categorical data, ideally no more than 5-7. As the number of colors in a palette increases, a viewer's ability to quickly and accurately distinguish between them decreases.

## Why

Research demonstrates a direct link between the number of colors and task performance. The study behind Colorgorical found that participants' error rates increased significantly as palette size grew from 3 to 8 colors. It becomes perceptually and cognitively more difficult to distinguish between and remember a larger set of colors, no matter how well-chosen the palette is. Each additional color makes the task of finding a sufficiently distinct new color harder, leading to "muddy" palettes with ambiguous colors.

## When it applies

- Any time you are using color to distinguish between discrete categories.
- This is especially critical for charts with many small marks (e.g., scatterplots) or overlapping elements (e.g., line charts), where colors can be even harder to tell apart.

## Exceptions

- There are no known exceptions where using many (10+) colors for categorical data is effective. If you have many categories, color is the wrong visual encoding to distinguish them all. The solution is to change the data grouping or the chart type, not to find a "better" 12-color palette.

## Trade-offs

- To adhere to this guideline, you may need to group or filter your data, for example by combining less important categories into an "Other" group. This means losing some granularity in the visualization in service of clarity.

## Signs of Trouble

- **Color Overload:** The chart legend has more than 7-8 distinct colors.
- **Lookalike Colors:** The palette is forced to include colors that are very similar to each other (e.g., teal and light green) because the perceptually "easy" colors are already used up.
- **The "Back-and-Forth" Dance:** You observe viewers repeatedly looking between the legend and the chart because they cannot hold all the color-category mappings in their working memory.
- **The Squint Test:** If you squint at the chart, multiple categories blur into the same color.

## How to Improve

- **Quick Fix: Group Categories.** Combine the least important or smallest categories into a single "Other" group. Use a neutral color, like gray, for this group to make it recede visually.

- **Moderate Redesign: Highlight Key Categories.** If your narrative focuses on only a few of the many categories, assign distinct colors to those key categories and color all other categories gray. This creates a clear visual hierarchy.

- **Comprehensive Redesign: Change the Chart Type.** If all categories are equally important, color is not the right tool for the job. Switch to a chart that uses position, which is more effective for distinguishing many categories. Good alternatives include a bar chart, a dot plot, or faceting (small multiples), where each category gets its own small chart.