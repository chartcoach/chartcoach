---
id: use-graduated-symbol-maps-to-avoid-area-confounds
title: Use Graduated Symbols When Geographic Area Would Mislead
bibliography: references.bib
description: Use symbol overlays (size/shape/color) to encode regional data without
  confounding it with region area.
labels:
- chart:map
- task:compare
- visual:size
- impact:clarity
- data:geospatial
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When comparing regions and you don’t want region area to bias perception, use a graduated symbol map instead of a choropleth.

## The Logic <!-- role: reason -->

Graduated symbols avoid confounding geographic area with data values and can encode more dimensions simultaneously using symbol size, shape, and color (including glyphs like pie charts).

- **The Principle:** Decouple regional measurement from region area by using overlay marks
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare magnitudes and composition across regions without area bias
- **Data Type:** Region-associated values, possibly multivariate (e.g., population + category proportions)
- **Audience:** General audiences if the glyph is simple and labeled

## When to Break It <!-- role: exceptions -->

- **Scenario:** The value is inherently a rate tied to region (prevalence) and area-based shading is appropriate
- **Reason:** A choropleth can communicate rates effectively when normalized properly [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Potential overlap/clutter of symbols in dense geographies
- **The Risk:** Complex glyphs (like pies) may be hard to read at small sizes

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a choropleth for totals and assuming viewers won’t notice area effects
- **Why it fails:** Perception of shading can be affected by the underlying region area [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers’ attention is drawn mostly to large geographic regions regardless of the legend value
- **The Test:** Ask whether two regions with equal value but different geographic size feel equal; if not, area is biasing perception [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace region shading with proportional circles
- **Best Fix:** Use symbols with size for magnitude and color/segments for additional dimensions, as appropriate [@heerTourVisualizationZoo2010]
