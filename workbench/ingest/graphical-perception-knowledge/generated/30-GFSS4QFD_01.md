---
id: account-for-shape-size-bias
title: "Recognize that mark shape biases size perception in scatterplots"

tags:
  - impact:perceptual
  - impact:ethical
  - chart:scatter
  - task:compare
  - task:rank
  - data:quantitative
  - visual:size
  - visual:shape
  - medium:screen

evidence:
  strength: medium
  summary: "In a study with 489 participants, Smart & Szafir (2019) found that mark shape significantly biases perceived size. Shapes with more visual mass at the top or bottom (e.g., 'T', '■') were consistently perceived as larger than centrally-weighted shapes (e.g., '+') of the same pixel dimensions (p < .001). The bias was substantial, with 'T' shapes perceived as larger than other shapes in 82% of trials."

sources:
  - type: research
    ref: Smart & Szafir, 2019
    url: https://doi.org/10.1145/3290605.3300899
    note: "Experiment 3 (n=489) demonstrated a strong, asymmetric interference of shape on size perception. Filled shapes were also generally perceived as larger than unfilled counterparts. The effect was asymmetrical; size had a much smaller effect on shape perception."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.48550/arXiv.2109.01271
    note: "This meta-analysis highlights the work of Smart & Szafir as an example of interference effects between visual channels that challenge traditional assumptions of separability (Section 5.1.2)."
    role: related

tools:
  - type: implement
    name: "D3 Extension for Perceptual Correction"
    url: https://bit.ly/2prjuRu
    description: "The authors of the primary study implemented a D3.js extension to computationally model and correct for the perceptual biases between shape, size, and color. (Note: Link from original paper)."

examples:
  - type: bad
    description: "This chart uses different shapes (e.g., circles for 'Group A', triangles for 'Group B') and also uses size to encode a quantitative variable (e.g., revenue). A triangle and a circle of the same pixel diameter will be perceived as different sizes, leading to inaccurate comparisons of revenue between the groups."
  - type: good
    description: "This chart encodes a quantitative variable with size, but uses the same shape (circles) for all data points. This ensures that any perceived difference in size is due to the data, not an artifact of shape bias."
---

## Guidance

Avoid using both different shapes and size to encode distinct data variables in the same scatterplot. The choice of shape systematically alters the perceived size of a mark.

## Why

The human visual system does not judge the "size" of different geometric shapes uniformly. Shapes with more visual mass concentrated at their top or bottom edges (like triangles ▲ or capital 'T's) are consistently perceived as larger than shapes with mass at their center (like '+' or 'X's), even when they have the exact same bounding box height and width. This means viewers will make inaccurate comparisons of the size-encoded variable between different shape categories.

### Core Principle

Visual channels are not always separable. Shape and size are integral dimensions, meaning the perception of one is biased by the value of the other. The interference is also asymmetric: shape has a large effect on perceived size, while size has a very small effect on perceived shape.

## When it applies

- When creating a scatterplot that uses `size` to encode a continuous quantitative variable (e.g., market cap, population).
- When also using `shape` to encode a categorical variable in the same plot (e.g., continent, industry type).

## Exceptions

- **When size is purely decorative or uniform.** If all marks are the same size, or if size is not encoding data, using different shapes for categories is perfectly fine.
- **When only a single shape is used.** If all marks have the same shape, using size to encode data is effective because there is no shape-induced bias to account for.

## Trade-offs

- **Fewer Encoding Channels:** Adhering to this guideline means you cannot use both shape and size to encode data simultaneously, reducing the number of variables you can display in a single static plot. You may need to use faceting (small multiples) or a different chart type instead.

## Signs of Trouble

- **Mixed Encodings:** The chart legend shows that `size` represents one variable (e.g., "Revenue") and `shape` represents another (e.g., "Region").
- **Apples-to-Oranges Comparison:** The chart invites the viewer to compare the size of a ▲ to the size of a ● to draw a conclusion about the data.
- **Inconsistent Visual Weight:** Looking at two marks of supposedly the same "size" value, one appears noticeably larger or heavier than the other simply because it's a square and the other is a star.

## How to Improve

- **Quick Fix: Add Redundant Labels.** If you must keep the mixed encodings, add direct text labels for the size-encoded value to the marks. This provides a "cognitive escape hatch," allowing determined users to read the true values instead of relying on flawed perceptual judgments.

- **Moderate Approach: Use a Single Shape.** The most effective solution is to choose one channel to prioritize. If comparing the size-encoded variable is important, use a single, consistent shape for all data points and use only color to distinguish categories.

- **Comprehensive Approach: Facet the Chart.** Instead of encoding category by `shape` in one chart, create a series of small multiple scatterplots, one for each category. Within each plot, use a consistent shape and encode the quantitative value using `size`. This allows for accurate size comparisons within each category and high-level comparisons across charts, without perceptual interference.
