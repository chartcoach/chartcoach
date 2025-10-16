---
id: use-woven-colorfields-for-summarization
title: "Use woven colorfields to improve visual summarization"
tags:
  - impact:perceptual
  - impact:performance
  - chart:heatmap
  - chart:custom
  - task:summary-mean
  - task:distribution
  - data:quantitative
  - data:temporal
  - visual:color
  - visual:texture
  - medium:static
  - medium:screen
evidence:
  strength: low
  summary: "An experiment found that 'woven' colorfields (where pixels are shuffled within discrete time blocks) improved accuracy for judging average values (from 61% to 78%) and spread (from 58% to 71%) compared to standard, sequential colorfields. This is a novel technique with promising initial results."
sources:
  - type: research
    ref: Albers, Correll, & Gleicher, 2014
    url: https://doi.org/10.1145/2556288.2557200
    note: "Primary experiment introducing and testing the 'woven colorfield' concept."
    role: primary
---

## Guidance

To help viewers visually estimate summary statistics like the average or spread from a time series heatmap (colorfield), consider transforming it into a "woven colorfield" by randomly shuffling the data points within each discrete time period.

## Why

A standard colorfield of a time series contains local structures and trends (e.g., a gradient of color from light to dark). These patterns can interfere with the human visual system's ability to form an accurate summary of the whole. By breaking these local structures through random permutation, the "woven" display creates a texture-like block whose overall color and variation are easier for the brain to summarize pre-attentively.

### Core Principle

Visual aggregation of a region can be improved by removing local spatial correlations that are irrelevant to the summary task, allowing the visual system to perceive the region's overall statistical properties more effectively.

## When it applies

- When using a color-based encoding (heatmap/colorfield) for time series data.
- When the primary tasks are to compare the average value or the variance of different time blocks, and not to see the trend within those blocks.

## Exceptions

- This technique intentionally destroys all sequential information within each time block. If the order of events or trends within a block are important, this method should not be used.
- It is significantly less effective for point-based tasks like finding the maximum or minimum value.

## Trade-offs

- **Total Loss of Trend Information:** Woven colorfields make it impossible to see the temporal order of events within each aggregated block. They are a pure summarization tool and sacrifice all detail about intra-period trends.
- **Novelty:** This is an unconventional chart type that may require explanation for the audience to understand what they are seeing (and what they are not seeing).

## Signs of Trouble

- **Gradient Bias:** Viewers looking at a standard time series heatmap have difficulty judging the average color of a block because of strong internal gradients or patterns.
- **Inaccurate Summaries:** Viewers' estimates of the average or variance of a time period are biased by salient but unrepresentative features within that period (e.g., a single very dark point).

## How to Improve

- **Moderate Approach:** If using a colorfield for time series analysis and summarization is the goal, transform it into a woven colorfield. For each time block (e.g., each month), collect all the pixel color values and randomly re-assign them to the pixel positions within that same block. This creates the texture-like effect that aids summarization.
