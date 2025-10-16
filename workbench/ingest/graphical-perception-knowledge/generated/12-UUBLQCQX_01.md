---
id: limit-categorical-colors
title: "Limit categorical palettes to 8 colors or fewer"

tags:
  - impact:perceptual
  - impact:cognitive
  - access:cognitive-load-risk
  - visual:color
  - data:categorical
  - data:cardinality.high
  - chart:bar
  - chart:line
  - chart:scatter
  - chart:pie

evidence:
  strength: high
  summary: "Multiple studies confirm that discrimination accuracy decreases as the number of colors increases. Gramazio et al. (2017, n=77) found error rates in a visual discrimination task more than doubled from 3-color palettes (12% error) to 8-color palettes (29% error), F(2,57)=30.8, p<0.001. This aligns with foundational work on attentional capacity limits, which suggests humans can only track about 4-5 items at a time (Haroz & Whitney, 2012)."

sources:
  - type: research
    ref: Gramazio, Laidlaw, & Schloss, 2017
    url: https://doi.org/10.1109/TVCG.2016.2598918
    note: "Experiment 1 (n=77) showed that as palette size increased from 3 to 5 to 8 colors, mean error rates rose from 79/660 to 119/660 to 190/660, a statistically significant increase (p < .001). The authors also noted that models of color perception became less predictable for 8-color palettes."
    role: primary
  - type: research
    ref: Haroz & Whitney, 2012
    url: https://doi.org/10.1109/TVCG.2012.180
    note: "Found that attentional capacity limits make visualizations with more than 5 distinct colors harder to process, supporting the need to limit color cardinality."
    role: supporting
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "The survey notes that most graphical perception studies focus on a limited set of chart types and encodings, but the principle of limited cardinality is a consistent theme."
    role: related

tools:
  - type: learn
    name: "Datawrapper: Which color scale to use"
    url: https://www.datawrapper.de/v/which-color-scale-to-use-for-my-data-vis/
    description: "Provides practical advice on when to use categorical scales and why they should be limited in size."
  - type: implement
    name: Colorgorical
    url: http://vrl.cs.brown.edu/color
    description: "Can generate palettes up to 22 colors but the authors note 'it is inadvisable to use that many colors due to perceptual limitations'."

examples:
  - type: bad
    description: "A pie chart or bar chart with 12 or more slices/bars, each with a unique color. It becomes a 'chartjunk' rainbow, and the viewer cannot reliably match the colors in the chart to the legend."
  - type: good
    description: "A chart with 10 categories where the top 5 are assigned distinct colors and the remaining 5 'long-tail' categories are grouped into a single 'Other' category, colored in a neutral gray."
---

## Guidance

For categorical data, limit the number of distinct colors in a single view to a maximum of eight, and ideally aim for five or fewer.

## Why

The human brain has a limited capacity for processing and remembering distinct visual information. As you add more colors, it becomes exponentially harder for a viewer to quickly and accurately distinguish between them. This increases cognitive load, slows down interpretation, and leads to more errors. Forcing a user to constantly refer back to a legend to decode a dozen colors makes a chart ineffective.

### Core Principle

Respect the cognitive limits of your audience. The goal of visualization is to reduce cognitive load, not increase it. Overloading a chart with too many distinct colors defeats this purpose.

## When it applies

- When using color to represent distinct, non-ordered categories.
- In any chart type where colors are mapped to a legend, including bar charts, line charts, scatter plots, and pie charts.
- Particularly important when the viewer needs to make quick comparisons between categories.

## Exceptions

- **Direct Labeling:** If every colored item is directly labeled with its category name, the cognitive burden of remembering the color-legend mapping is removed. While still visually complex, using more than 8 colors can be acceptable in this case.
- **Exploratory Analysis by Experts:** For an expert user performing interactive, exploratory data analysis, a larger color palette may be a necessary tool for discovery, as they can filter, zoom, and hover to disambiguate colors. This does not apply to static, explanatory visualizations for a general audience.
- **Spatial Contiguity:** In maps or other visualizations where same-colored regions are spatially clustered (e.g., a choropleth map of US regions), the brain can group them more easily. However, the limit still largely applies.

## Trade-offs

- **Loss of Granularity:** By limiting colors, you may need to group some categories into an "Other" bucket. This means you sacrifice the ability to see detail in the less-prominent categories.
- **Design Complexity:** It requires more thought to decide which categories to show and which to group, rather than simply assigning a color to every unique value in a data column.

## Signs of Trouble

- **The Rainbow Effect:** The chart uses a wide spectrum of colors that looks like a rainbow, making it visually noisy and hard to interpret.
- **Legend-Gazing:** You observe users repeatedly moving their eyes (or mouse) back and forth between the chart and the legend.
- **Subtle Neighbors:** The palette contains multiple colors that are very similar (e.g., three different shades of blue, or a teal next to a green). This is a common symptom when trying to create a 10+ color palette.
- **"What color is this?"** Users ask questions not about the data, but about which category a particular color represents.

## How to Improve

- **Quick Fix: Grouping.** Identify the most important categories you want to highlight. Assign distinct, highly discriminable colors to them. Group the remaining "long-tail" categories into a single "Other" or "Miscellaneous" category and color it with a neutral gray.

- **Moderate Redesign: Faceting (Small Multiples).** Instead of putting all categories in one large, color-coded chart, break it into a series of smaller, simpler charts (a "small multiple" or "facet" grid). Each small chart can show one or a few categories, drastically reducing the number of colors needed in any single view.

- **Comprehensive Redesign: Re-evaluate the Goal.** If you feel you absolutely need to show 20 different categories, ask if a single chart is the right approach. Perhaps a searchable, sortable table is more appropriate. Or, maybe the core message of the visualization can be reframed to focus on a more limited, important subset of the data.