---
id: prefer-square-bar-aspect-ratio
title: "Prefer square-like aspect ratios for bar marks to improve recall accuracy"
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
  summary: "Ceja et al. (2021) found in 3 experiments that bars with a square aspect ratio (1:1) showed no systematic bias when recalled from memory (mean bias of +0.11 pixels, not statistically significant). This suggests square-like marks are perceptually stable and recalled more accurately."

sources:
  - type: research
    ref: Ceja et al., 2021
    url: https://doi.org/10.1109/TVCG.2020.3030422
    note: "Primary study (n=25, n=15, n=21) showing that 1:1 aspect ratio bars did not produce a statistically significant memory bias, unlike wide or tall bars."
    role: primary

examples:
  - type: good
    description: "The paper shows that bars with a square-like aspect ratio (center) are recalled accurately, without the systematic over- or under-estimation bias that affects wide or tall bars."
---

## Guidance

When designing bar charts, Mekko charts, or treemaps, aim for marks with an aspect ratio that is close to 1:1 (square-like) to minimize memory bias.

## Why

Bar marks with a roughly square aspect ratio do not suffer from the systematic memory biases that affect very wide or very tall bars. Viewers can recall their height more accurately because the shape is perceptually stable. There is no "prototypical square" for the memory to be biased towards, as the shape is already regular.

### Core Principle

Perceptually stable shapes, like squares, are less prone to memory distortion than shapes with extreme aspect ratios. Using them for data marks can lead to more accurate recall.

## When it applies

-   This is a good default practice for any bar chart design where viewers might need to remember or compare values.
-   It is especially important in dashboards, small multiples, or animated sequences where values are compared across different views or time points.

## Exceptions

-   It is often impossible to make *all* bars in a single chart square-like, as their height is determined by the data. The goal is to adjust the overall chart proportions (e.g., bar width, spacing) so that the *average* or most typical bar in your dataset has a balanced, square-like aspect ratio.

## Trade-offs

-   Strictly enforcing a square aspect ratio can dictate the overall dimensions of your chart in a way that might not fit your layout constraints. For example, a chart with many bars would need to be very wide to maintain square-like marks.

## Signs of Trouble

-   **Extreme Shapes:** Most or all of the bars in your chart are either very wide "pancakes" or very tall "skyscrapers". This is a sign that the aspect ratios are not balanced, and memory biases are likely.

## How to Improve

-   **Quick Fix: Adjust Chart Proportions.** While keeping the number of bars fixed, adjust the overall width of the chart's plot area until the bars look more balanced and less extreme in their shape.

-   **Moderate Redesign: Optimize Bar Width and Spacing.** Re-evaluate the bar width and the spacing between bars. Sometimes reducing the gap between bars allows them to be wider and thus more square-like, without making the entire chart excessively wide.

-   **Comprehensive Redesign: Use Aspect Ratio as a Design Constraint.** When building responsive or automated visualization systems, use this principle as a design constraint. An algorithm can attempt to maintain a perceptually optimal aspect ratio for marks as the chart's viewport size changes.
