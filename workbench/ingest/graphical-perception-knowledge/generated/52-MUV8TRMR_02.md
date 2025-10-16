---
id: use-large-enough-marks
title: "Use sufficiently large marks for target-finding tasks"
tags:
  - impact:perceptual
  - impact:accessibility
  - impact:performance
  - visual:size
  - task:lookup
  - task:filter
  - chart:scatter
  - chart:heatmap
  - chart:map.glyphs
  - chart:line
  - access:cognitive-load-risk
evidence:
  strength: high
  summary: "Gramazio et al. (2014, n=31) found that search performance was significantly slower for the smallest mark sizes (e.g., ≤ .508° visual angle) across both grid and scatterplot layouts (p<0.001). Performance improved as mark size increased, eventually plateauing at larger sizes."
sources:
  - type: research
    ref: Gramazio, Schloss, & Laidlaw, 2014
    url: https://doi.org/10.1109/TVCG.2014.2346983
    note: "Primary study (n=15 in Exp. 1, n=16 in Exp. 2) showing a robust effect of mark size on reaction time. Smallest marks were consistently the slowest, and performance plateaued for marks between .762° and 1.271° visual angle."
    role: primary
---
## Guidance

For visual search tasks, ensure marks are large enough to be easily seen and discriminated. Avoid using very small marks.

## Why

Extremely small marks are difficult for the visual system to parse and identify, increasing the time and cognitive effort required to find a target. Increasing the mark size up to a certain point improves performance by making them more discriminable. Beyond that point, further increases yield diminishing returns as the core task is no longer limited by legibility.

## When it applies

- In any visualization where a primary task is to locate an individual mark, such as finding a point in a scatterplot, a cell in a heatmap, or a glyph on a map.
- The effect holds true for various layouts, including single-color, grouped, and randomly arranged marks.

## Exceptions

- When the primary task is to assess global patterns, trends, or data density. The paper's case study suggests that smaller marks can be more effective for this, as larger marks can obscure these patterns through overplotting.

## Trade-offs

- Larger marks occupy more screen real estate, which can lead to overplotting and obscure underlying data points or patterns.
- Using larger marks may limit the total number of items that can be displayed without significant overlap.

## Signs of Trouble

- **The Squint Test:** You or your users have to squint or lean closer to the screen to distinguish individual marks.
- **Overplotting:** Marks are so large they overlap excessively, creating a solid mass that hides individual points and density variations.
- **User Complaints:** Users report that marks are "too tiny," "hard to see," or "all blend together."

## How to Improve

- **Quick Fix: Increase Mark Size.** Systematically increase the size (e.g., radius of points, width of squares) of all marks until they are clearly distinguishable. The study suggests performance improves up to ~0.75° of visual angle.
- **Moderate Approach: Interactive Sizing.** In an interactive tool, allow users to control mark size with a slider. This empowers them to adjust the view for either target-finding (larger marks) or pattern-spotting (smaller marks).
- **Comprehensive Approach: Implement Zooming.** For dense, interactive plots, implement a zooming function that automatically increases mark size as the user zooms in on a region. This maintains legibility at all levels of detail without causing overplotting in the overview.