---
id: shuffle-pixels-for-average-judgment
title: "Randomly permute data points within a region to improve perceptual averaging"

tags:
  - impact:perceptual
  - impact:performance
  - chart:heatmap
  - task:summary-mean
  - data:temporal
  - data:quantitative
  - visual:color
  - access:cognitive-load-risk

evidence:
  strength: medium
  summary: "Correll et al. (2012, n=66) found that permuting (shuffling) the data points within each monthly region of a colorfield chart led to significantly higher accuracy for average-judgment tasks compared to an ordered colorfield (mean accuracy 91.4% vs 81.5%). The interaction between display type and permutation was significant (p < 0.0001)."

sources:
  - type: research
    ref: Correll et al., 2012
    url: https://doi.org/10.1145/2207676.2208556
    note: "Study found that a 2D permutation of data points in the colorfield condition significantly improved performance, supporting a perceptual averaging theory. This effect was not present for line charts."
    role: primary

examples:
  - type: good
    description: "The data points within each month are randomly permuted (shuffled). This mixes the colors, making the local average more representative of the global average for the region and making the perceptual averaging task easier and more accurate."
    url: https://i.imgur.com/kP4U1vX.png # Screenshot of Figure 3(d) from the paper
  - type: bad
    description: "The data points are ordered by time. Strong trends or patterns within a month can create large patches of uniform color, potentially biasing the user's perception of the average."
    url: https://i.imgur.com/K3Z4a2a.png # Screenshot of Figure 3(c) from the paper
---

## Guidance

When using a colorfield (1D heatmap) for judging average values of discrete regions, randomly permuting the data points within each region can improve user accuracy.

## Why

Perceptual averaging is most effective when the colors to be averaged are spatially close. In an ordered time-series colorfield, trends can create large, uniform color patches, forcing the visual system to average over a wider, more challenging area. Permuting the data points (shuffling the pixels) breaks up these patterns, mixing the colors within each region. This makes the local average more representative of the region's global average, making the perceptual task easier and more accurate.

### Core Principle

Facilitate pre-attentive processing by optimizing the spatial layout of visual information for the specific perceptual mechanism being leveraged.

## When it applies

- When using a colorfield or heatmap to help users judge the average value of discrete, bounded regions.
- When the underlying data within regions may have strong trends or patterns that could bias the perception of the overall average color.

## Exceptions

- If preserving the internal pattern or trend within each region is also important to the user's task. Permutation intentionally destroys this information.
- If the regions are very small (containing only a few data points), the effect of permutation will be negligible.

## Trade-offs

- **Loss of Detail:** This technique intentionally destroys the low-level temporal pattern (the "shape" of the data) within each region to improve perception of the summary statistic (the average). It is only suitable when the summary is the primary goal.
- **Unfamiliarity:** A permuted or "noisy" looking chart is highly unconventional and may be perceived as an error or a "broken" visualization if not explained.

## Signs of Trouble

- **"Trend" Bias:** When using an ordered colorfield, users' judgments of the average seem to be biased by strong trends within a region (e.g., they might overestimate the average of a region that ends on a high note, even if the overall average is lower).

## How to Improve

- **Quick Approach: Add an Average Indicator.** If you cannot permute the data, add a separate, explicit visual indicator of the average for each region, such as a colored border or an overlaid glyph whose color represents the average.

- **Comprehensive Approach: Implement Permutation.** For each defined region (e.g., a month), take all the data points belonging to it and randomly reorder them before rendering them as colored blocks. This directly optimizes the chart for perceptual averaging, but be sure to include a note for users explaining that the noisy appearance is intentional for improved summary perception.