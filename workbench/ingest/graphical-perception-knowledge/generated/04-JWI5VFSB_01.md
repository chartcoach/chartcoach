---
id: prioritize-area-arc-over-angle
title: "Rely on arc length and area over angle for encoding proportions"
tags:
  - impact:perceptual
  - chart:pie
  - chart:donut
  - chart:radial
  - task:composition
  - task:lookup
  - task:compare
  - data:quantitative
  - visual:angle
  - visual:size
  - visual:length
evidence:
  strength: medium
  summary: "Skau & Kosara (2016, n=92) tested isolated visual cues for proportion estimation. Charts relying only on angle produced significantly higher log absolute error (1.9-2.3) compared to those using arc length (1.29) or area (1.31), demonstrating that angle is the weakest of the three cues."
sources:
  - type: research
    ref: Skau & Kosara, 2016
    url: https://doi.org/10.1111/cgf.12888
    note: "In an experiment isolating visual cues, angle-only charts were the least accurate. The ranking of chart types by accuracy was: [Donut ≈ Pie] > [Arc ≈ Area] > Angle Pie > Angle Donut. This suggests angle is a much weaker perceptual cue than arc length or area."
    role: primary
examples:
  - type: bad
    description: A stylized pie chart where segments are distorted into shapes that preserve angle but not area or arc length. This design is difficult to read accurately.
  - type: good
    description: A standard pie or donut chart, which correctly preserves all three cues (angle, area, and arc length), allowing viewers to use the most effective channels for perception.
---

## Guidance

When designing radial charts (like pie or donut charts), ensure that the arc length and area of the segments accurately represent the data. Do not create chart variations that distort these cues under the assumption that viewers are only reading the angles.

## Why

Experiments that isolate the different visual cues in a pie chart show that viewers are least accurate when they can only judge the angle. They are significantly more accurate when judging arc length or area. Therefore, chart variations that distort arc length or area will likely harm perceptual accuracy, even if they preserve the angles of the segments.

### Core Principle

Visualizations should leverage the most effective perceptual channels for the given task. For proportion judgments in radial charts, arc length and area are more effective channels than angle.

## When it applies

- When designing any chart type that uses wedge-like shapes to show part-to-whole relationships.
- When evaluating the effectiveness of non-standard or stylized pie and donut chart variations.

## Exceptions

None known. Even for people who self-report using angle as their primary method, their performance is just as good (or better) when arc length and area are available and undistorted.

## Trade-offs

Sticking to standard pie and donut forms that preserve all three cues is the safest approach, but this might limit aesthetic creativity. This guideline suggests that creative forms are only acceptable as long as they preserve the integrity of the more effective cues: arc length and area.

## Signs of Trouble

- **Distorted Shapes:** The chart uses non-standard slice shapes (e.g., an oval pie chart, or a pie chart made of icons) that distort the area or arc length of the slices relative to their value.
- **Varying Radii:** The segments of the pie chart have different radii, breaking the consistency of the arc length and area encodings.

## How to Improve

- **Quick Fix:** If using a chart with distorted area or arc length (like an isometric pie chart), add direct data labels to each slice so viewers can read the values directly, bypassing the flawed visual encoding.
- **Moderate Redesign:** Re-draw the chart as a standard pie or donut chart to ensure arc length and area are correctly encoded and not distorted.
- **Comprehensive Redesign:** Switch from a radial chart to a linear one, like a bar chart or 100% stacked bar chart. These use position along a common scale, which is a more accurate perceptual channel for comparison than angle, area, or arc length.
