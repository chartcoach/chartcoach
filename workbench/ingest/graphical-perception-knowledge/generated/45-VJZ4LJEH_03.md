---
id: prioritize-position-for-quantity
title: "Use position along a common scale to represent quantitative data"

tags:
  - impact:perceptual
  - impact:logos
  - data:quantitative
  - task:compare
  - task:rank
  - task:lookup
  - visual:position
  - visual:length
  - visual:angle
  - visual:area
  - visual:color
  - chart:bar
  - chart:scatter
  - chart:pie

evidence:
  strength: high
  summary: "A foundational principle established by Cleveland & McGill (1984) and extended by Mackinlay (1986). Numerous replications confirm that humans judge quantities more accurately and efficiently by comparing position along a common scale than by comparing length, angle, area, or color."

sources:
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: https://doi.org/10.2307/2288400
    note: "Foundational study (n=55) that experimentally established a hierarchy of perceptual tasks, with position on a common scale being most accurate for quantitative comparisons (p<0.001)."
    role: primary
  - type: research
    ref: Heer & Bostock, 2010
    url: https://doi.org/10.1145/1753326.1753357
    note: "Large-scale crowdsourced replication (n≈2000) that confirmed the original Cleveland & McGill rankings, demonstrating the robustness of the principle."
    role: supporting
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "Review paper synthesizing the literature, reaffirming the hierarchy 'PX=PY > L=An=O > Ar > CS > CH' for quantitative data, where PX/PY is position."
    role: related
---

## Guidance

When designing a visualization for comparing quantitative values, prioritize using position along a common, aligned scale as the primary visual encoding.

## Why

The human visual system is exceptionally good at accurately judging distances and comparing positions when the objects are aligned to a common baseline (like in a bar chart). This perceptual task is faster, more accurate, and less prone to bias than judging other visual channels like length (for unaligned bars), angle (in a pie chart), area (in a treemap), or color saturation.

### Core Principle

Make the most important comparisons the easiest and most accurate to perform. For quantitative comparisons, this means leveraging the most effective perceptual channel: position on a common scale.

## When it applies

- The primary task for the viewer is to compare magnitudes, rank values, or look up specific quantities.
- Accuracy is a key requirement for the visualization.
- You need to choose between different chart types for representing quantitative data (e.g., bar chart vs. pie chart vs. treemap).

## Exceptions

- **Showing part-to-whole relationships:** While less accurate for comparison, a pie chart or treemap can be more effective at emphasizing that values are components of a whole. However, even here, a stacked bar chart often performs better.
- **Showing correlation:** A scatterplot, which uses position on two *unaligned* scales, is the standard for showing the relationship between two variables.
- **Severe space constraints:** An area-based chart like a treemap can display hierarchical data in a more compact space than a bar chart, at the cost of comparison accuracy.

## Trade-offs

- **Space Efficiency:** Bar charts and dot plots can take up more space (especially vertical space for many categories) than more compact, area-based representations.
- **Familiarity/Aesthetics:** In some contexts, audiences may expect or prefer a pie chart, even though a bar chart would be more perceptually effective.

## Signs of Trouble

- **The "Pie Chart Problem":** Viewers cannot reliably tell which slice of a pie chart is larger when the values are close.
- **Area Ambiguity:** In a bubble chart or treemap, it's difficult to judge if one shape is 1.5x or 2x the area of another.
- **Constant Legend-Checking:** Viewers have to repeatedly look at a color legend to decode quantitative values, because the color channel is not precise enough for direct comparison.

## How to Improve

- **Quick Fix: Add Direct Labels.** If you must use a less accurate chart type (like a pie chart), add direct data labels (e.g., "42%"). This provides a textual "escape hatch" for viewers, allowing them to compare numbers directly instead of relying on flawed perceptual judgments of angle or area.

- **Moderate Redesign: Switch to a Bar or Dot Plot.** When the goal is comparison, convert the visualization to a bar chart or dot plot. This aligns all values to a common baseline (the x-axis), allowing for highly accurate comparisons using position.

- **Comprehensive Approach: Educate Your Audience.** If you are replacing a familiar but ineffective chart type (like a pie chart), briefly explain the rationale. A small note like "Bar charts are used to make comparisons easier" can help manage audience expectations and highlight the benefit of the more effective design.