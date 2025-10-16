---
id: prioritize-position-encoding
title: "Prioritize position encodings over other visual channels"

tags:
  - impact:perceptual
  - impact:performance
  - visual:position
  - visual:length
  - visual:angle
  - visual:area
  - visual:color
  - data:quantitative
  - data:ordinal
  - data:categorical
  - audience:general

sources:
  - type: research
    ref: Zeng & Battle, 2023
    note: "This review paper synthesizes foundational research, stating 'In general, position encodings (PX, PY) are the top choices for representing all data types (quantitative, nominal, ordinal)' (p. 8)."
  - type: research
    ref: Cleveland & McGill, 1984
    url: https://doi.org/10.2307/2288400
    note: "Original foundational research establishing the hierarchy of perceptual accuracy for visual encodings, with position on a common scale ranked highest."
  - type: research
    ref: Mackinlay, 1986
    url: https://doi.org/10.1145/22949.22950
    note: "Extended Cleveland & McGill's work, formalizing the expressiveness and effectiveness principles for automated visualization design."

---

## Guidance

When designing a visualization, use position along a common scale (as in bar charts and scatter plots) as the primary visual variable to encode your most important data.

## Why

Human visual perception is most accurate, efficient, and consistent at decoding information encoded by position. We can judge differences in position and length far more accurately than we can judge differences in angle, area, or color saturation. This hierarchy of perceptual tasks, established by foundational research, is a cornerstone of effective visualization design. Using a less effective encoding (like area in a bubble chart) for your primary data will lead to less accurate interpretation by your audience.

## When it applies

- You are encoding quantitative data for comparison (e.g., sales figures, measurements).
- You need to show the rank or order of categorical data.
- You are plotting data on a 2D plane (e.g., any chart with an X and Y axis).

## Exceptions

- **When position is already used:** In some charts, like maps (geographical position) or treemaps (hierarchical position), the `position` channel is already taken. In these cases, other channels like `color` or `size` must be used to encode quantitative values.
- **For aesthetic or conceptual reasons:** A designer might intentionally choose a less perceptually accurate encoding (like area) to create a certain aesthetic or to better match a metaphor (e.g., using circles to represent 'bubbles'). This is a deliberate trade-off of accuracy for other communicative goals.

## Trade-offs

- **Space:** Charts that rely on position, like bar charts, can take up more space than more compact forms like treemaps or packed bubble charts.
- **Familiarity:** In some contexts, audiences may be more familiar with a less effective chart type (like a pie chart) than a more effective one (like a bar chart), creating a potential learning curve.

## Signs of Trouble

- **Inaccurate comparisons:** Users have difficulty accurately judging which value is larger when comparing angles in a pie chart or areas in a bubble chart.
- **Misleading charts:** The most important data in your visualization is encoded with a secondary channel like color hue or shape, while position is used for less important data.
- **The "Which is bigger?" problem:** It is difficult to answer "How much bigger is A than B?" with any precision.

## How to Improve

- **Quick approach:** If using a chart with a less effective primary encoding (e.g., bubble chart), add direct text labels with the exact values. This provides a "perceptual escape hatch" by allowing users to read the numbers directly.
- **Comprehensive approach:** Re-design the visualization to use a more effective encoding for the most important data.
  - Instead of a **pie chart** (angle), use a **bar chart** (length/position).
  - Instead of a **bubble chart** (area), use a **bar chart** or **dot plot** (position).
  - Instead of encoding a quantitative value with only **color**, use **position** on an axis.
