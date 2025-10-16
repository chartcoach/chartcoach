---
id: avoid-wide-bar-aspect-ratio
title: "Avoid wide, short aspect ratios for bars to prevent overestimation"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:ethical
  - chart:bar
  - chart:treemap
  - chart:bar.mekko
  - task:lookup
  - task:compare
  - data:quantitative
  - visual:position
  - visual:size
  - audience:general
  - medium:static
  - medium:interactive
  - access:cognitive-load-risk

evidence:
  strength: medium
  summary: "Ceja et al. (2021) found in 3 experiments that viewers systematically overestimate the height of bars with wide aspect ratios (e.g., 11.5:1) when recalling them from memory (mean overestimation of +4.75 pixels, p<0.001). This bias is attributed to a memory effect pulling the shape towards a prototypical square."

sources:
  - type: research
    ref: Ceja et al., 2021
    url: https://doi.org/10.1109/TVCG.2020.3030422
    note: "Primary study with 3 experiments (n=25, n=15, n=21) demonstrating overestimation bias for wide bar marks recalled from memory."
    role: primary

examples:
  - type: bad
    description: "The paper shows that bars with a wide aspect ratio (left) are systematically recalled from memory as being taller than they actually are (overestimation)."
---

## Guidance

Avoid using marks with very wide, short aspect ratios in bar charts, Mekko charts, or treemaps.

## Why

Viewers systematically remember wide bars as being taller than they actually are. This memory bias occurs because our minds tend to "correct" the shape towards a more prototypical, regular shape (a square), leading to an overestimation of the shorter dimension (height). This can cause viewers to misinterpret or misremember the magnitude of the data.

### Core Principle

Incidental visual properties, like aspect ratio, can create systematic biases in how we recall explicitly encoded data values, like position.

## When it applies

-   When viewers need to recall or compare values from memory. This is common when comparing a bar to one seen previously, in another chart (like in a dashboard or small multiples), or on a different screen.
-   This is particularly relevant for bar charts, Mekko charts, and treemaps where mark aspect ratios can become extreme.

## Exceptions

-   If the primary goal is not precise value recall but simply showing the presence/absence of a value or a very rough sense of magnitude, this bias may be less critical.

## Trade-offs

-   To avoid wide bars, you may need to make the chart taller or narrower than your layout allows. This can be a challenge when visualizing many categories in a limited space.

## Signs of Trouble

-   **Pancake Bars:** The bars in the chart are extremely wide and short, resembling pancakes.
-   **Misleading Comparisons:** Comparisons made between charts or over time may be skewed, as the recalled values of wide bars are inflated.

## How to Improve

-   **Quick Fix: Add Data Labels.** If you must use wide bars, add direct data labels (e.g., the exact number) to each bar. This provides an "escape hatch" for viewers, allowing them to read the precise value instead of relying on biased perceptual judgment.

-   **Moderate Redesign: Adjust Chart Dimensions.** Modify the overall chart dimensions (e.g., make it taller or reduce the width allocated to each bar) to make the bars less wide and closer to a square-like shape.

-   **Comprehensive Redesign: Use a Dot Plot.** Consider switching to a chart type where aspect ratio is not an issue, such as a dot plot. Since dots have a fixed aspect ratio, they are not susceptible to this type of memory bias.
