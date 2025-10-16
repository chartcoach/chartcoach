---
id: prefer-position-for-quantitative-data
title: "Use position on a common scale to encode quantitative data"

tags:
  - impact:perceptual
  - impact:logos
  - task:compare
  - task:rank
  - task:lookup
  - data:quantitative
  - visual:position
  - visual:length
  - visual:angle
  - visual:area
  - visual:color
  - audience:general
  - medium:static

evidence:
  strength: high
  summary: "Cleveland & McGill's foundational 1984 study (n=55), replicated and confirmed by numerous studies since (e.g., Heer & Bostock, 2010), established a perceptual hierarchy of visual encodings. Their experiments demonstrated that judgments of position along a common, aligned scale are significantly more accurate than judgments of length, angle, or area for quantitative comparisons (p<0.001)."

sources:
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: https://doi.org/10.1080/01621459.1984.10478080
    note: "Foundational study establishing the perceptual ranking of elementary graphical tasks. Showed position along a common scale is the most accurate encoding for quantitative comparison."
    role: primary
  - type: research
    ref: Heer & Bostock, 2010
    url: https://doi.org/10.1145/1753326.1753357
    note: "Large-scale crowdsourced replication (n~50 per experiment) that confirmed the relative rankings of position, length, and angle from Cleveland & McGill's original findings."
    role: supporting
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This review paper synthesizes and summarizes the continued relevance of this principle, listing it as a core effectiveness guideline (Table 3)."
    role: related

examples:
  - type: good
    description: "A bar chart encodes quantitative values using the position of the bars' endpoints along a common y-axis starting at zero. This allows for highly accurate comparisons."
  - type: bad
    description: "A pie chart encodes quantitative values using angles (and area). It is notoriously difficult for humans to accurately compare the sizes of different slices, especially when they are not adjacent or are of similar size."
---

## Guidance

For tasks requiring precise comparison or ranking of quantitative data, encode the data using position along a common, aligned scale. Prefer this over other visual channels like length (unaligned), angle, area, or color saturation.

## Why

Humans are significantly better at accurately perceiving and comparing differences in position along a common scale than they are at judging other visual variables. This perceptual advantage makes charts that use this encoding (like bar charts and dot plots) superior for tasks that require judging relative magnitudes. Using less accurate channels like angle (in pie charts) or area (in bubble charts) leads to higher error rates and makes it difficult for viewers to draw precise conclusions from the data.

### Core Principle

Match visual encodings to the perceptual capabilities of the human brain. The most effective visualizations leverage visual channels that our brains can decode quickly and accurately for the task at hand.

## When it applies

- When the primary goal is for the audience to accurately compare, rank, or look up quantitative values.
- When designing core chart types like bar charts, dot plots, line charts, or scatter plots.
- When choosing how to represent a quantitative variable in any chart.

## Exceptions

- **Showing Part-to-Whole:** When the primary goal is to show a part-to-whole relationship and precise comparison is secondary, an area-based chart like a treemap or even a simple pie chart (with few slices) can be acceptable, though a bar chart is often still clearer.
- **Geographic Data:** On a map, position is already used to encode geographic location. In this case, other channels like color (for choropleths) or area (for bubble maps) must be used to encode quantitative values, even though they are less perceptually accurate.
- **Limited Space:** When space is extremely constrained, area-based charts like treemaps can be more space-efficient than bar charts for displaying hierarchical data.

## Trade-offs

- **Space:** Charts that rely on position (like bar charts) can take up more space than area-based charts (like treemaps) for the same amount of data, especially with many categories.
- **Aesthetics vs. Clarity:** Sometimes, less perceptually accurate charts (like bubble charts) are chosen for their aesthetic appeal. This is a trade-off against the clarity and accuracy that a bar or dot plot would provide.

## Signs of Trouble

- **Pie Chart Overload:** A pie chart has more than 3-5 slices, making comparisons nearly impossible.
- **Bubble Trouble:** A bubble chart is used for a task that requires precise comparisons, forcing viewers to inaccurately judge differences in circle areas.
- **3D Effects:** Gratuitous 3D effects are applied to charts (e.g., 3D pie charts, 3D bars), which distorts perspective and makes judging position, length, or angle even more difficult.

## How to Improve

- **Quick Fix: Add Direct Labels.** If you must use a less accurate chart like a pie or bubble chart, add direct data labels (e.g., "42%") to each element. This provides an "escape hatch" for the user, allowing them to read the value directly instead of relying on flawed perceptual judgment.
- **Moderate Approach: Switch to a Better Chart.** If you are using a pie chart for comparison, switch to a bar chart. If you are using a bubble chart for ranking, switch to a dot plot or bar chart. This directly replaces the less effective encoding with a more effective one.
- **Comprehensive Approach: Re-evaluate the Task.** Consider if a different representation of the data would better serve the user's task. For example, instead of a single complex chart, a series of small, simple bar charts (small multiples) might provide clearer comparisons across different contexts.
