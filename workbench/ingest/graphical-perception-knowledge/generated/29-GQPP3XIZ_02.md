---
id: prefer-position-length-over-slope
title: "Use position or length over slope for comparing relational data"

tags:
  - impact:perceptual
  - impact:performance
  - chart:bar
  - chart:dot-plot
  - chart:line
  - task:compare
  - task:filter
  - task:aggregate
  - data:quantitative
  - visual:position
  - visual:length
  - visual:angle
  - visual:shape

evidence:
  strength: high
  summary: "Nothelfer & Franconeri (2020, n=26) found that encodings using position (dot plots) and length (bar charts) were significantly faster and more accurate than those using slope. This result strongly reinforces the foundational perceptual rankings established by Cleveland & McGill (1984) and replicated since."

sources:
  - type: research
    ref: Nothelfer & Franconeri, 2020
    url: https://doi.org/10.1109/TVCG.2019.2934801
    note: "Experiments 1 & 2 (n=26 total) showed that slope encodings led to significantly slower search rates and lower accuracy (p<0.001) than position or length encodings for relational tasks."
    role: primary
  - type: research
    ref: Cleveland & McGill, 1984
    url: https://doi.org/10.2307/2288400
    note: "Foundational work establishing the perceptual hierarchy where position and length are judged more accurately than angle/slope."
    role: supporting

---
## Guidance

When creating charts for comparing pairs of values, prefer to use position (as in a dot plot) or length (as in a bar chart) over slope or angle (as in a slope graph).

## Why

Humans are perceptually more accurate and efficient at judging differences in position along a common scale and differences in length than they are at judging differences in angle or orientation. Choosing an encoding that aligns with this perceptual hierarchy reduces cognitive load and leads to faster, more accurate interpretation.

### Core Principle

Align your choice of visual encoding with the known hierarchy of human perceptual accuracy.

## When it applies

- When choosing a chart type to show comparisons between pairs of quantitative values.
- When the primary task is to judge the magnitude or direction of change.
- This applies to both standard charts (e.g., grouped bar charts) and delta charts (e.g., bar chart of differences).

## Exceptions

- Slope graphs can be very effective for the specific task of showing **rank change** over two points in time. Their primary value in that context comes from showing the crossings and re-ordering of lines, a task for which bar charts or dot plots are less suited.

## Trade-offs

- Bar charts and dot plots may take up more horizontal space than a compact slope graph.
- A slope graph can sometimes feel more connected and fluid for showing change between two states.

## Signs of Trouble

- **Inaccurate Judgments:** Users struggle to accurately perceive the size of the change in a slope graph, often misjudging which changes are larger or smaller.
- **Slow Comparisons:** It takes users longer to compare changes when they are encoded as slopes versus when they are encoded as lengths on a common baseline.
- **Inconsistent Interpretation:** Different users arrive at different conclusions about the relative size of changes.

## How to Improve

- **Comprehensive Approach: Change the Chart Type.** If you are using a slope graph primarily to show the magnitude of change, consider switching to a chart that uses a more accurate encoding:
  - A **bar chart** plotting the deltas.
  - A **dumbbell plot** (or connected dot plot), which uses position on a common scale.
