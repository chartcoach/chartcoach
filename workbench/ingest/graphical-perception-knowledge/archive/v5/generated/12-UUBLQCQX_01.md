---
id: limit-categorical-colors
title: "Use fewer than 8 categorical colors for better discrimination"
tags:
  - impact:perceptual
  - impact:cognitive
  - access:cognitive-load-risk
  - visual:color
  - data:categorical
  - data:cardinality.high

evidence:
  strength: high
  summary: "Gramazio et al. (2016) found that as palette size increased from 3 to 8 colors, user error rates in discrimination tasks rose significantly. This confirms a well-established principle in visualization that human capacity for distinguishing and remembering categorical colors is limited, typically to about 4-5 items."
sources:
  - type: research
    ref: Gramazio et al., 2016
    url: https://doi.org/10.1109/TVCG.2016.2598918
    note: "Experiment 1 showed that participant accuracy decreased and discard rates (due to high errors) increased as palette size grew from 3 to 5 to 8 colors."
    role: primary
  - type: research
    ref: Haroz & Whitney, 2012
    url: https://doi.org/10.1109/TVCG.2012.182
    note: "Found that viewers can track about 3-4 colored items at a time, demonstrating the low capacity of attention for colored objects."
    role: supporting

examples:
  - type: good
    description: A line chart showing trends for 4-5 key competitors, each with a distinct color.
  - type: bad
    description: A stacked bar chart or a map with 15 different categories, each assigned a unique color, forcing the user to constantly refer to the legend and still struggle to differentiate them.
---
## Guidance

Limit the number of distinct colors used to represent categories in a single view. Aim for 8 or fewer, and ideally 5 or fewer.

## Why

Humans have a limited capacity to reliably and quickly distinguish between many different colors. As you add more colors to a palette, the perceptual difference between them necessarily decreases, making them harder to tell apart. This leads to higher error rates, slower interpretation, and increased cognitive load for the viewer.

### Core Principle

Respect the limitations of human working memory and visual perception. An effective visualization does not overload the viewer's capacity to process information.

## When it applies

- When assigning colors to represent distinct, non-ordered categories (nominal data).
- When creating legends for charts like line charts, scatter plots, or multi-category bar charts.
- Any time the viewer must associate a color with a specific meaning.

## Exceptions

- In some visualization types like treemaps, color can be used to reinforce a grouping structure even with many items, as long as position and size are the primary encodings.
- If colors are not meant to be individually identified but are used to show a general pattern or texture, more colors may be acceptable.

## Trade-offs

- Limiting categories may require you to group some data into a less-specific "Other" category, which means a loss of detail.
- Choosing an alternative chart type (like small multiples) may take up more space.

## Signs of Trouble

- **The Rainbow Effect:** Your chart uses so many colors it looks like a bag of candy, with no clear visual hierarchy.
- **Constant Legend Look-ups:** You or your viewers have to repeatedly look back and forth between the legend and the chart to understand what's being shown.
- **Ambiguous Neighbors:** The palette contains very similar colors (e.g., teal and light green, or pink and light purple) that are hard to tell apart, especially as small marks.

## How to Improve

- **Quick approach:** If you have more than 8 categories, group the smallest or least important ones into a single "Other" category and color it with a neutral gray.
- **Moderate approach:** Highlight the 1-3 most important categories with distinct, saturated colors and de-emphasize all other categories by coloring them with shades of a single, muted hue (e.g., different shades of gray or blue).
- **Comprehensive approach:** Redesign the visualization to not rely on color for identification. Switch to a chart type that uses position, such as a bar chart, a dot plot, or a series of small multiples. This allows you to label categories directly.