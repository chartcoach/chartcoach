---
id: avoid-tall-bar-aspect-ratio
title: "Avoid tall, thin aspect ratios for bars to prevent underestimation"
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
  summary: "Ceja et al. (2021) found in 3 experiments that viewers systematically underestimate the height of bars with tall, thin aspect ratios (e.g., 1:11.5) when recalling them from memory (mean underestimation of -13.86 pixels, p<0.001). This bias is attributed to a memory effect pulling the shape towards a prototypical square."

sources:
  - type: research
    ref: Ceja et al., 2021
    url: https://doi.org/10.1109/TVCG.2020.3030422
    note: "Primary study with 3 experiments (n=25, n=15, n=21) demonstrating underestimation bias for tall bar marks recalled from memory."
    role: primary

examples:
  - type: bad
    description: "The paper shows that bars with a tall aspect ratio (right) are systematically recalled from memory as being shorter than they actually are (underestimation)."
---

## Guidance

Avoid using marks with very tall, thin aspect ratios in bar charts, Mekko charts, or treemaps.

## Why

Viewers systematically remember tall, thin bars as being shorter than they actually are. This memory bias occurs because our minds tend to "correct" the shape towards a more prototypical, regular shape (a square), leading to an underestimation of the taller dimension (height). This can cause viewers to downplay the significance of high values.

### Core Principle

Incidental visual properties, like aspect ratio, can create systematic biases in how we recall explicitly encoded data values, like position.

## When it applies

-   When viewers need to recall or compare values from memory, such as comparing a bar to one seen previously or to a bar in another chart.
-   When visualizing data with a large range, where some bars may become very tall relative to their width.

## Exceptions

-   In charts with data following a power-law distribution, some bars will inevitably be very tall. In these cases, the bias is difficult to avoid entirely through aspect ratio adjustment alone. Other solutions like adding annotations, using a log scale, or breaking the axis may be necessary.

## Trade-offs

-   To make tall bars more square-like, you would need to make the chart extremely wide, which is often impractical and can make it difficult to see all the data at once.

## Signs of Trouble

-   **Skyscraper Bars:** The bars in the chart are extremely tall and thin, resembling skyscrapers.
-   **Value Discrepancy:** When a viewer looks up the exact value of a tall bar, they are surprised by how high it actually is, because their perception was that it was shorter.

## How to Improve

-   **Quick Fix: Add Data Labels.** Add direct data labels, especially to the tallest bars. This provides a precise value that bypasses the viewer's biased perceptual memory.

-   **Moderate Redesign: Adjust Chart Width.** Make the overall chart wider or increase the width of the bars. This gives the bars a more balanced aspect ratio and mitigates the underestimation bias.

-   **Comprehensive Redesign: Use a Log Scale or Dot Plot.** If the data has a very large dynamic range, consider using a logarithmic scale to compress the tall bars and reduce the extremity of their aspect ratios. Alternatively, switch to a dot plot, which is not susceptible to this bias.
