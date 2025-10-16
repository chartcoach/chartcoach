---
id: choose-cartogram-by-task
title: "Choose a cartogram type based on the analytical task"

impact:
  - perceptual
  - cognitive
  - performance
  - logos
tags:
  - cartogram
  - map
  - spatial-data
  - task-based-design
  - comparison
  - adjacency
  - summarize

sources:
  - type: research
    ref: Nusrat, Alam, & Kobourov, 2018
    url: https://doi.org/10.1109/TVCG.2016.2642109
    note: "Evaluated four major cartogram types (contiguous, non-contiguous, rectangular, Dorling) and found that performance varies significantly by task, with no single 'best' type for all scenarios."

examples:
  - type: good
    description: "For finding neighbors (an 'adjacency' task), a contiguous cartogram is effective because it preserves the topological relationships between regions, leading to low error rates."
  - type: good
    description: "For recognizing the original shape of regions, a non-contiguous cartogram is the best choice because it scales each area independently without distortion."
  - type: bad
    description: "Using a rectangular cartogram to show a 'big picture' trend. Research shows this type performs poorly for summary tasks, with high error rates and long interpretation times, as the severe shape distortion makes it hard to see patterns."
  - type: bad
    description: "Using a Dorling (circle) or non-contiguous cartogram when the main goal is to identify which regions touch each other. These types break adjacency, making the task nearly impossible without interaction."
---

## Guidance

Select the cartogram type that best supports the primary analytical task your audience needs to perform. There is no single "best" type of cartogram; the most effective choice depends on the specific question you want to answer.

## Why

Cartograms work by distorting geographic features (like shape, area, and location) to represent a data variable. Different cartogram algorithms make different trade-offs:

*   **Contiguous** cartograms preserve neighbor relationships (topology) while trying to maintain shape.
*   **Non-contiguous** cartograms preserve shape perfectly but break topology.
*   **Dorling** cartograms use circles, abandoning both original shape and topology to show value.
*   **Rectangular** cartograms preserve topology with rectangles but completely sacrifice original shapes.

Research shows that choosing a cartogram mismatched to the task leads to higher error rates, longer interpretation times, and user frustration. Aligning the chart type with the task makes the visualization more accurate and efficient.

## When it applies

- When creating a cartogram, where the area of geographic regions (like countries or states) is scaled to a data variable (like population or GDP).

## Exceptions

- If the primary goal is purely aesthetic, artistic, or to create an abstract "map-like" graphic without a specific analytical purpose, you might prioritize visual style over functional performance.

## Trade-offs

- Optimizing for one task comes at a cost. A non-contiguous cartogram perfectly preserves familiar shapes, but makes it impossible to see which regions are neighbors. A rectangular cartogram is great for seeing neighbors but makes regions unrecognizable.
- Using a general-purpose option like a **contiguous cartogram** is a safe, balanced choice but may not be the absolute top performer for any single, specialized task.

## Evaluate

- [ ] The primary task is to identify neighbors, but a non-contiguous or Dorling (circle) cartogram is used.
- [ ] The primary task requires recognizing familiar geographic shapes, but a rectangular or Dorling cartogram is used.
- [ ] The primary task is to summarize a broad pattern, but a rectangular cartogram is used.

## Repair

1.  First, clearly define the single most important question you want your audience to answer. Then, choose the cartogram type that aligns with that task.
2.  For **general-purpose analysis**, **locating regions**, or **comparing values**, use a **contiguous cartogram**. It's a strong, well-understood default.
3.  If **identifying neighbors** (adjacency) is the most critical task, use a **contiguous** or **rectangular** cartogram.
4.  If **recognizing original shapes** is the most important task, use a **non-contiguous** cartogram.
5.  To show **broad patterns and "big picture" trends**, a **Dorling** (circle-based) or **contiguous** cartogram is effective and engaging. Avoid rectangular cartograms for this purpose.
