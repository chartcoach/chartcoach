---
id: account-for-mark-shape-in-color-choice
title: "Account for Mark Shape When Choosing Colors"
tags:
  - impact:perceptual
  - chart:bar
  - chart:line
  - chart:scatter
  - task:compare
  - task:cluster
  - visual:color
  - visual:shape
evidence:
  strength: medium
  summary: "Szafir (2018, n=288 for bar experiment) found that elongated marks like bars and lines significantly increase color discriminability compared to equally thick compact marks like points. The effect is asymptotic, with most of the benefit gained by a length-to-thickness ratio of 2:1, providing an additional 5-10 ΔE of perceptual 'headroom'."
sources:
  - type: research
    ref: "Szafir, 2018"
    url: "https://doi.org/10.1109/TVCG.2017.2744359"
    note: "Experiment 2 (bar charts, n=288) and Experiment 3 (line charts, n=72) showed that elongation significantly reduces the Just Noticeable Difference (JND) for color compared to the point marks in Experiment 1 (n=72)."
    role: primary
---

## Guidance

Recognize that color differences are easier to perceive on elongated marks (like bars and lines) than on compact, symmetric marks (like points). You can use slightly more subtle color palettes on bar and line charts than on scatterplots with equally-thick marks.

## Why

The shape of a visual mark influences color perception. Elongated shapes provide more "edge" information for the visual system to process, which enhances its ability to discriminate between colors.

### Core Principle

The geometry of a mark, not just its size or color value, affects its perceptual properties. An encoding's effectiveness is a function of all its visual channels combined.

## When it applies

-   When choosing or designing color palettes for different chart types, such as bar charts, line charts, and scatterplots.
-   When trying to maximize the number of discernible steps in a color ramp for a bar or line chart.

## Exceptions

For very short bars where the length is similar to the width (aspect ratio near 1:1), they behave more like compact points, and the perceptual benefit of elongation is minimal.

## Trade-offs

Relying on this effect to use a highly subtle color palette can be risky if the bar or line lengths are not guaranteed to be sufficiently elongated. What works for long bars may fail for short ones.

## Signs of Trouble

-   **Misapplied Palettes:** A color palette designed specifically for a bar chart is reused on a scatterplot, resulting in points that are hard to distinguish.
-   **Overly Conservative Bars:** Using an extremely conservative color palette (very large perceptual steps) on a bar chart, which works but unnecessarily limits the number of colors you could have used.

## How to Improve

-   **Quick Fix: Prioritize the Weakest Link.** If you must use the same palette for multiple chart types (e.g., in a dashboard), design it to be robust for the chart with the least discriminable marks (usually the scatterplot). The palette will then be more than sufficient for the bars and lines.

-   **Moderate Approach: Use Chart-Specific Palettes.** If your tool allows, use a slightly more nuanced (more steps) color palette for bar and line charts than for associated scatterplots.

-   **Comprehensive Approach: Model the Elongation Effect.** Use the models provided by Szafir (2018) to calculate the required perceptual distance (ΔEp,s) for your specific mark type (point, bar, or line), thickness, and desired discriminability, then generate a palette that meets those specifications.
