---
id: prefer-color-over-size-for-secondary-q-variable
title: "Prefer color over size for a secondary quantitative variable in a scatterplot"
tags:
  - impact:perceptual
  - chart:scatter
  - chart:bubble
  - task:lookup
  - task:compare
  - data:quantitative
  - visual:position
  - visual:color
  - visual:size
sources:
  - type: research
    ref: Kim & Heer, 2018
    url: https://doi.org/10.1111/cgf.13409
    note: "Section 4.2.4, 'Size & color exhibit asymmetric effects for Q1 vs. Q2,' is the direct source. It finds that using size for a secondary variable (Q2) interferes with decoding the primary positional variables (Q1), while using color does not."
---

## Guidance

When creating a scatterplot (or bubble chart) with two primary quantitative variables on the X/Y axes and a third, secondary quantitative variable, prefer encoding the secondary variable with **color saturation** rather than **size** if the main tasks involve the X/Y positions.

## Why

There is an asymmetric interference effect between visual channels. While `size` is generally a more effective channel for quantity than `color`, using it for a secondary variable can interfere with and slow down the viewer's ability to decode the primary `x` and `y` position values. In contrast, encoding the secondary variable with `color` (specifically, color saturation/lightness) causes less interference with the primary positional decoding task.

In short: you are optimizing for the performance of the most important task. If judging position is primary, don't let a secondary encoding of size get in the way.

## When it applies

- You are visualizing **three quantitative variables**.
- Two "primary" variables are encoded using **X and Y position** in a scatterplot.
- A third "secondary" variable must be encoded using another channel, like **size (a bubble chart)** or **color saturation (a colored scatterplot)**.
- The most frequent or important user tasks involve judging the **X/Y positions** (e.g., "What is the Y-value of this point?", "Is this point further to the right than that one?", "What is the trend?").

## Exceptions

- **Primary Task is on the Secondary Variable:** If the most important task for the user is to judge the value of the secondary variable (e.g., "Which point has the largest [secondary value]?"), then using `size` is more effective. Size is a better channel for quantitative comparison than color, and in this case, you are willing to accept the slight interference with positional tasks.
- **Categorical Data:** This guideline applies to a secondary *quantitative* variable. For a secondary *categorical* variable, `color hue` is a standard and effective choice.

## Trade-offs

- **Perceptual Effectiveness of the Secondary Channel:** You are knowingly choosing a less effective quantitative channel (`color`) for the secondary variable to preserve the perceptual integrity of the primary channels (`position`). This is a deliberate trade-off that prioritizes the primary task. Viewers will be less accurate at judging the secondary variable's value from color than they would be from size.

## Signs of Trouble

- **Slowed Performance:** Users take longer to complete tasks related to the X/Y position on a bubble chart compared to a simple scatterplot.
- **Cluttered Appearance:** Large marks (bubbles) in a bubble chart can occlude one another, making it difficult to judge their exact X/Y position, especially in dense areas.
- **Task Mismatch:** The chart uses `size` to encode a secondary variable, but all the user's questions are about the relationship between the X and Y variables. The chosen encoding is hindering, not helping, the primary task.

## How to Improve

- **Quick Fix: Reduce Mark Size or Opacity.** In a bubble chart, reducing the overall size of the bubbles or making them semi-transparent can reduce occlusion and make it easier to see their central position. However, this can weaken the perception of the size encoding itself.

- **Moderate Redesign: Switch Channels.** Change the encoding for the secondary quantitative variable from `size` to `color saturation`. This turns the chart from a bubble chart into a colored scatterplot. Use a sequential color scheme (e.g., light blue to dark blue) to represent the quantitative values.

- **Comprehensive Approach: Use Faceting or Paired Plots.** If all three variables are equally important, a single 3-variable chart might be the wrong approach. Consider showing a "scatterplot matrix" (SPLOM), which is a grid of scatterplots showing the relationship between each pair of variables (`X vs Y`, `X vs Z`, `Y vs Z`) in separate, clear 2D plots. This removes all channel interference at the cost of increased space.