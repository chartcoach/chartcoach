---
id: use-small-multiples-to-avoid-spaghetti-line-charts
title: Split overlapping multi-category line charts into small multiples
bibliography: references.bib
description: When many lines overlap, give each series its own panel to keep trends
  traceable.
labels:
- chart:small-multiples
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:mainstream
- complexity:intermediate
---

## Use small multiples for many overlapping time series <!-- role: advice -->

When many categories produce an overlapping “spaghetti” of lines, split the chart into small multiples so each line gets its own panel. Keep the chart type consistent across panels so comparisons remain possible.

## Why small multiples restore traceability <!-- role: reason -->

Separating series into repeated, aligned panels removes occlusion and reduces the tracking burden, while preserving a comparable structure.

**Mechanism:** Viewers can follow one trajectory at a time without line crossings, then compare patterns across panels through consistent axes and repeated form.

**Evidence:** Small-multiple layouts are recommended to handle lots of categories in time series when multiple lines overlap heavily, by giving each line its own panel [@muth_chart_types_guide_2025].

**Notes:** “Small multiples” refers to splitting one chart type into a grid of similar panels.

## Situations where small multiples apply <!-- role: context -->

- **User Goal:** Compare many categories’ trends without losing individual trajectories.
- **Task:** Identify which categories rise/fall similarly; spot outliers.
- **Data:** Temporal series with many categories and frequent overlaps.
- **Chart Setting:** Limited attention contexts where legibility matters more than compactness.
- **Audience:** Mainstream readers who struggle with dense line crossings.
- **Success Criterion:** A reader can trace any category from start to end quickly.

## When not to use small multiples <!-- role: exceptions -->

**Break it when:** You do not have enough space to allocate readable panels for each category. **Why:** The panels become too small to interpret reliably, pushing you toward more compact summaries like slope charts or arrow plots [@muth_chart_types_guide_2025].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** More space and potentially more scrolling. **Risk:** Readers may compare panels less precisely if axes or scales are inconsistent. **Mitigation:** Keep scales consistent across panels where comparison is intended.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Using small multiples but changing scales across panels without signaling it. **Why it fails:** The visual comparison between panels becomes misleading even if each panel is readable.

## Quick tests <!-- role: check -->

**Failure Sign:** Panels require zooming or labels collide. **Quick Check:** Ensure each panel can show labels and the full line without overlap. **Stronger Test:** Ask a reader to find the fastest-growing category; if they can’t scan panels quickly, the layout is too dense.

## What to do instead <!-- role: fix -->

- Use a slope chart if intermediate time points are not important.
- Use an arrow plot to summarize many categories compactly.
- Reduce the number of categories shown (e.g., highlight a subset) and keep the rest out of the primary view.
- Switch to a different goal-focused chart if the real message is ranking at one time point, not full trajectories.
