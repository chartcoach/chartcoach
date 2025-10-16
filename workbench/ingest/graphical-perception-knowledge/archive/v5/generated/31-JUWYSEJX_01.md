---
id: use-elongated-marks-for-color
title: "Use Elongated Marks (Bars, Lines) for Better Color Discriminability"

tags:
  - impact:perceptual
  - chart:bar
  - chart:line
  - chart:scatter
  - task:compare
  - task:distribution
  - visual:color
  - visual:shape
  - medium:screen

evidence:
  strength: medium
  summary: "A 2018 study directly compared color perception on points, bars, and lines. It found that elongated marks (bars and lines) significantly increase color discriminability compared to symmetric marks (points) of the same thickness."

sources:
  - type: research
    ref: "Szafir, 2018. Modeling Color Difference for Visualization Design"
    url: "https://doi.org/10.1109/TVCG.2017.2744359"
    note: "Primary study demonstrating that colors are more discriminable on bars and lines than on scatterplot points of equal thickness. Figures 4 and 5 show that the Just-Noticeable Difference (JND) thresholds are significantly lower for bars and lines."
    role: primary

tools:
  - type: learn
    name: "VisColors Repository"
    url: "http://cmci.colorado.edu/visualab/VisColors/"
    description: "The data and infrastructure from the source paper, which can be used to model the 'elongation effect'."

examples:
  - type: bad
    description: "A scatterplot with many (>10) categorical colors. Viewers may struggle to differentiate between similar colors (e.g., multiple shades of blue) because the small, symmetric point marks offer poor color discriminability."
  - type: good
    description: "A bar chart representing the same data. The elongated shape of the bars makes the same set of categorical colors significantly easier to tell apart, even if the bars are thin."
---

## Guidance

When color discriminability is critical, prefer using elongated marks (like bars or lines) over symmetric marks (like points or squares) of the same thickness.

## Why

The human visual system can distinguish color differences more easily on elongated shapes. The study refers to this as the "elongation effect," where the increased length of a mark enhances color perception. This means you can use more subtle color variations on a bar chart or line chart than on a scatterplot and still have them be perceptually distinct. This effect effectively gives you a wider, more nuanced "encoding space" for color.

### Core Principle

Mark geometry directly influences the perception of other visual channels. The shape of a mark is not just decorative; it can enhance or inhibit the effectiveness of its color encoding.

## When it applies

- When choosing between different chart types (e.g., bar chart vs. scatterplot) and color is a primary channel for encoding important information.
- When you need to encode a categorical variable with high cardinality (many unique values) and need to maximize the number of distinguishable colors.
- When designing with a color palette that contains subtle, adjacent color steps.

## Exceptions

- When the primary analytical task is best served by a specific chart type that uses symmetric marks. For example, if the goal is to show the correlation between two continuous variables, a scatterplot (which uses points) is the correct choice, even if its color discriminability is lower than a bar chart's.
- The benefit of elongation is asymptotic, leveling off when a mark's length is roughly twice its thickness. For very short and wide bars, this guidance may not apply as strongly.

## Trade-offs

- **Chart Functionality:** Choosing a chart type for better color perception may mean sacrificing the optimal chart type for the primary analytical task. For example, changing a scatterplot to a bar chart to improve color clarity means you can no longer encode two continuous variables on the X and Y axes.
- **Layout and Space:** Elongated marks like bars often require more space and a more rigid layout (e.g., aligned to a common baseline) than a more flexible scatterplot layout.

## Signs of Trouble

- **Color Mismatch:** You have a categorical variable that is easy to distinguish in a bar chart but becomes difficult to tell apart when you represent the same data in a scatterplot using the same colors.
- **Over-Reliance on a Legend:** In a scatterplot, viewers have to constantly refer back to the legend to identify which color corresponds to which category because the points on the chart are not easily distinguishable by their color alone.

## How to Improve

- **Quick Fix: Change Mark Shape.** If using a scatterplot, consider changing the point mark to a thin, vertically or horizontally oriented line or plus sign. This introduces some elongation and may slightly improve color perception without changing the chart type.

- **Moderate Approach: Switch Chart Type.** If one of your variables is categorical or can be binned, consider switching from a scatterplot to a bar chart or dot plot. This allows you to leverage the elongation of bars (or the clear position of dots) while making the color encoding more effective.

- **Comprehensive Approach: Model the Elongation Effect.** When designing a color palette, use a perceptual model that accounts for mark shape. Use a smaller CIELAB ΔE requirement for elongated marks than for point marks to reflect their increased discriminability, allowing for more steps in your palette.