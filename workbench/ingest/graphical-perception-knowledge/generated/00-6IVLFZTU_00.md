---
id: use-position-for-quantity
title: "Use position on a common scale to encode quantitative data"
tags:
  - impact:perceptual
  - impact:performance
  - task:compare
  - task:rank
  - data:quantitative
  - visual:position
  - visual:length
  - chart:bar
  - chart:scatter
  - chart:dot-plot
audience:
  - audience:general
medium:
  - medium:static
  - medium:interactive
evidence:
  strength: high
  summary: "Foundational research by Cleveland & McGill (1984) established a perceptual hierarchy of visual encodings, ranking position along a common scale as the most accurate for quantitative judgments. This has been replicated in numerous studies, including large-scale crowdsourced experiments by Heer & Bostock (2010), consistently showing position is significantly more accurate than angle, area, or color saturation for comparison tasks (p<0.001)."
sources:
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: https://doi.org/10.2307/2288400
    note: "The foundational experiment (n=55) that established the perceptual ranking of visual encodings, showing position on a common scale is most accurate for quantitative comparisons."
    role: primary
  - type: research
    ref: Mackinlay, 1986
    url: https://doi.org/10.1145/22949.22950
    note: "Formalized the perceptual rankings into an automated system (APT), extending them to include ordinal and nominal data types and codifying expressiveness and effectiveness criteria. This is cited extensively in the review by Zeng & Battle (2023)."
    role: supporting
  - type: research
    ref: Heer & Bostock, 2010
    url: https://doi.org/10.1145/1753326.1753357
    note: "A large-scale (n=1,935) crowdsourced replication that validated Cleveland & McGill's original findings, confirming the superior accuracy of position and length over angle and area."
    role: supporting
---
## Guidance
When encoding quantitative data for comparison or ranking tasks, use visual channels that rely on position along a common, aligned scale. Bar charts, dot plots, and scatter plots are effective examples.

## Why
Humans are exceptionally good at perceiving small differences in position along a straight line. This makes it the most accurate and efficient visual encoding for judging relative magnitudes. Other channels like angle (used in pie charts), area (used in bubble charts), or color saturation are perceived less precisely, leading to higher error rates and slower task completion.

### Core Principle
Make the most important comparisons the easiest to perform. For quantitative data, this means leveraging the visual channel that offers the highest perceptual accuracy: position.

## When it applies
- When the primary task is to compare, rank, or look up quantitative values.
- When creating bar charts, line charts, scatter plots, or dot plots.
- When data integrity and accuracy are critical.

## Exceptions
- When the primary task is not precise comparison but rather seeing part-to-whole relationships with very few categories (e.g., a pie chart with 2-3 slices).
- For geographic data where position is already used to encode location, other channels like color or size must be used for quantitative values.

## Trade-offs
- **Aesthetics vs. Accuracy:** Channels like area (bubble charts) or angle (pie charts) can sometimes be more engaging or compact, but this often comes at the expense of perceptual accuracy.
- **Information Density:** Using position for one variable can limit how other variables are encoded, especially in a small space.

## Signs of Trouble
- **Area/Angle Comparisons:** The chart requires users to compare the sizes of 2D areas (circles, irregular shapes) or the angles of pie slices to judge magnitude.
- **Misleading Rankings:** When sorted by value, the visual order of the elements does not clearly match the data order.
- **User Uncertainty:** Viewers express difficulty in determining which value is larger or by how much.

## How to Improve
- **Quick Fix: Add Direct Labels.** If you must use a pie or bubble chart, add direct data labels (e.g., "42%") to each element. This provides an escape hatch, allowing users to read the exact values instead of relying on less accurate perceptual judgments.
- **Moderate Redesign: Switch to a Better Chart Type.** Replace the pie chart, donut chart, or bubble chart with a bar chart or dot plot. This aligns all values to a common positional scale, making comparisons dramatically easier and more accurate.
- **Comprehensive Redesign: Re-evaluate Encodings.** Review all data-to-visual-channel mappings in the visualization. Ensure that the most important quantitative variable is mapped to the most effective channel (position), and less critical variables are mapped to other channels (e.g., color, shape).