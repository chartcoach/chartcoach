---
id: use-sufficiently-large-marks-for-search
title: "Use sufficiently large marks for visual search tasks"
tags:
  - impact:perceptual
  - impact:performance
  - chart:scatter
  - chart:heatmap
  - chart:line
  - task:lookup
  - task:find-anomalies
  - visual:size
  - audience:general
  - medium:static
  - medium:interactive
evidence:
  strength: medium
  summary: "In two experiments, Gramazio et al. (2014) found that visual search was slowest for the smallest marks. Performance improved as mark size increased up to a point (around 0.76° visual angle), after which the benefits plateaued. The study recommends avoiding marks smaller than ~0.5° visual angle."
sources:
  - type: research
    ref: Gramazio et al., 2014
    url: https://doi.org/10.1109/TVCG.2014.2346983
    note: "Found that response times were greatest for the smallest marks and plateaued as mark size increased."
    role: primary
---

## Guidance

For tasks that require finding a specific target, ensure that visual marks are large enough to be easily and quickly identified. Avoid using very small marks (e.g., smaller than ~0.5° of visual angle).

## Why

Very small marks are difficult for the visual system to process, requiring more effort to differentiate and parse. This slows down performance regardless of whether the marks are grouped or not. As mark size increases, they become more legible, and performance improves. However, this benefit has diminishing returns; beyond a certain point (the study found a plateau around 0.76° to 1.27° of visual angle), making marks even larger does not further speed up search time and may begin to cause overplotting.

### Core Principle

Legibility precedes all other perceptual tasks. If a mark cannot be easily seen, it cannot be effectively interpreted.

## When it applies

- In any visualization where users need to identify individual marks, especially in dense displays like scatterplots, line charts with points, or heatmaps.
- When designing for a variety of screen sizes and resolutions, where the physical size of marks may change.
- When target detection speed is a critical performance metric.

## Exceptions

- When the primary goal is to show overall density or large-scale patterns, and individual mark identity is unimportant. In these cases, very small (even sub-pixel) marks can be effective for revealing density structures.
- In cases of extreme overplotting, using smaller, semi-transparent marks may be preferable to large, opaque marks that would occlude each other completely.

## Trade-offs

- Larger marks consume more screen space, which can lead to more overplotting and limit the total amount of data that can be displayed without occlusion.
- The optimal mark size depends on display density; what is appropriately large in a sparse plot may be too large in a dense one.

## Signs of Trouble

- **Squinting required:** Users have to lean in or squint to distinguish individual marks.
- **Slow performance on sparse charts:** Even with few data points, users take a long time to find targets.
- **"Pixel-hunting":** Marks are so small that they are difficult to see or to click on in an interactive visualization.

## How to Improve

- **Quick Fix: Increase Mark Size.** Simply increase the size (radius, area) of all marks until they are clearly legible. Based on the study, aim for a size between 0.5° and 1.0° of visual angle.
- **Moderate Approach: Add Outlines.** Add a contrasting outline (stroke) to marks. This can improve their discriminability from the background and each other without significantly increasing their footprint.
- **Comprehensive Approach: Make Mark Size Dynamic.** In an interactive system, allow mark size to be adjusted by the user or dynamically linked to the zoom level, ensuring marks remain legible as the user navigates through the data.
