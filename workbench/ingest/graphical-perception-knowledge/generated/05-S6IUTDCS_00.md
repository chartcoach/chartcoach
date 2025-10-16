---
id: prefer-color-for-secondary-quantitative
title: "Prefer color over size for secondary quantitative variables in scatterplots"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:scatter
  - task:compare
  - task:lookup
  - data:quantitative
  - data:categorical
  - visual:color
  - visual:size
  - visual:position
  - audience:general
  - medium:static
  - medium:interactive
  - access:cognitive-load-risk

evidence:
  strength: medium
  summary: "A large-scale experiment (Kim & Heer, 2018, n=1,920) found that using size to encode a secondary quantitative variable interfered with position judgments, resulting in tasks taking at least 1.13 times longer compared to using color (p < 0.01)."

sources:
  - type: research
    ref: Kim & Heer, 2018
    url: https://doi.org/10.1111/cgf.13409
    note: "Primary experiment on trivariate data (2Q, 1N) showing that a size-encoded secondary variable (Q2) significantly slowed down value tasks (p < 0.01) on a position-encoded primary variable (Q1) compared to a color-encoded Q2."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This review highlights the need to translate such specific experimental findings into actionable rules for visualization recommendation systems."
    role: related
---

## Guidance

When creating a scatterplot that encodes a primary quantitative variable with position (x/y-axis) and a secondary quantitative variable, use a color ramp (e.g., color saturation or lightness) for the secondary variable instead of size.

## Why

Using size to encode a secondary variable introduces visual interference that complicates the primary task of judging the position of the marks. The human brain has to process the varying sizes, which slows down the ability to accurately and quickly perceive the x and y coordinates of each point. Color is a "separable" channel from position and creates less cognitive interference.

### Core Principle

Minimize cognitive load by avoiding interfering visual channels. When one visual channel (size) distracts from the main task of interpreting another (position), the visualization becomes less effective.

## When it applies

- When creating scatterplots or bubble charts with two or more quantitative variables.
- The primary analytical task is to read, look up, or compare the values encoded by position (the x and y axes).
- The variable encoded by size is of secondary importance to the immediate task.

## Exceptions

- When the primary task is to judge the secondary variable itself (the one encoded by size).
- When the visualization is intended for summary tasks (e.g., judging average size) rather than individual value lookups. Kim & Heer (2018) found that size can be very effective for "ensemble coding" or judging aggregate properties.
- If the secondary variable has a very small, discrete range of values where size differences are minimal and less likely to cause interference.

## Trade-offs

- **Aesthetics vs. Performance:** A bubble chart (using size) can sometimes be more visually engaging than a colored scatterplot, but this guidance prioritizes perceptual performance (speed and accuracy) over aesthetics.
- **Grayscale/Print Compatibility:** A size-encoded chart is inherently grayscale-friendly. Using color requires careful palette selection to ensure it works in print or for users with color vision deficiencies.

## Signs of Trouble

- **Slow Decoding:** Do users take a long time to answer specific questions about the position of points (e.g., "What is the X/Y value for point A?")?
- **User Complaints:** Viewers mention that the different sizes of the dots make it "distracting" or "hard to focus" on their location.
- **Inaccurate Judgments:** When asked to compare the positions of two points, users make more errors in a bubble chart than in a simple scatterplot.

## How to Improve

- **Quick Fix: Reduce Size Range.** If you must use size, reduce the range of the size encoding. Make the difference between the smallest and largest mark less extreme to minimize interference.
- **Moderate Redesign: Switch to Color.** Change the visual encoding for the secondary quantitative variable from `size` to `color`. Use a sequential color palette (e.g., from light blue to dark blue) to represent the ordered values.
- **Comprehensive Redesign: Use Small Multiples.** If both quantitative variables are of high importance, consider splitting the chart. For example, create small multiple scatterplots, faceted by binned values of the secondary variable. This gives each variable a clear positional encoding, eliminating interference.
