---
id: avoid-rectangular-cartograms-for-summaries
title: "For summarizing broad patterns, avoid rectangular cartograms"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:map
  - chart:map.cartogram
  - task:summary-mean
  - task:trend
  - data:spatial
  - data:quantitative

evidence:
  strength: medium
  summary: "In a 2018 study (n=33) on summarizing trends, rectangular cartograms had the highest error rate, which was nearly double that of contiguous cartograms and significantly higher than non-contiguous and Dorling cartograms (p<0.005). Viewers also took over 100 seconds on average for these tasks with rectangular cartograms."

sources:
  - type: research
    ref: "Nusrat, Alam, & Kobourov, 2018"
    url: https://doi.org/10.1109/TVCG.2016.2642109
    note: "Experiment H5 tested a 'summarize' task. Rectangular cartograms performed worst in accuracy, with significantly higher error rates than Dorling and non-contiguous types. Completion time was also long."
    role: primary

---

## Guidance

When the goal is for viewers to understand a "big picture" trend or pattern across a map, avoid using **rectangular cartograms**. Prefer Dorling (circle), non-contiguous, or contiguous cartograms for this task.

## Why

The severe shape distortion and rigid, grid-like structure of rectangular cartograms make it difficult for viewers to perceive high-level geographic patterns. The abstract nature of the rectangles appears to obscure, rather than reveal, the overall data story. In experiments, they led to the highest error rates for summary tasks. In contrast, the simple and distinct shapes of Dorling cartograms or the more organic forms of contiguous cartograms were more effective for seeing broad trends.

## When it applies

- When the primary goal is for the audience to grasp a high-level summary, such as "Which part of the country contributes most to GDP?" or "What is the overall trend in this election map?"

## Exceptions

- When the goal is not to show a broad pattern but to provide a schematic of adjacencies. In such a case, the topological clarity of a rectangular cartogram might be its main purpose, overriding the need for pattern detection.

## Trade-offs

- Dorling and non-contiguous cartograms, which perform well for summaries, do not preserve topology, making them unsuitable for adjacency tasks. Contiguous cartograms offer a good balance but distort shapes.

## Signs of Trouble

- **Pattern Blindness:** Viewers are unable to describe the main trend or pattern shown in the map.
- **High Cognitive Load:** The chart is described as "confusing," "a mess," or "hard to read." Viewers take an excessively long time to answer summary-level questions.

## How to Improve

- **Quick Fix: Add an Explanatory Title or Annotation.** Use text to explicitly state the main takeaway or pattern that the rectangular cartogram is intended to show.

- **Moderate Redesign: Switch to a Dorling Cartogram.** For summary tasks, Dorling (circle) cartograms performed well and were also subjectively preferred by users. This is an effective alternative for highlighting broad patterns.

- **Comprehensive Redesign: Use a Simpler Map Type.** If the pattern is strong, a standard choropleth map might communicate it effectively without the perceptual complexity of a cartogram.
