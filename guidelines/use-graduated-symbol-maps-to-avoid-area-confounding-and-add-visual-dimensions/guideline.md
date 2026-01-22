---
id: use-graduated-symbol-maps-to-avoid-area-confounding-and-add-visual-dimensions
title: Use graduated symbol maps to avoid area confounding and add visual dimensions
bibliography: references.bib
description: Place sized and colored symbols on a map to show quantities without conflating
  values with region area.
labels:
- chart:graduated-symbol-map
- task:compare
- visual:size
- impact:interpretability
- data:geospatial
- audience:general
- complexity:intermediate
---

## Overlay symbols when region shading would confound comparisons <!-- role: advice -->

Use a graduated symbol map by placing symbols over a geographic base map to encode values with symbol size, shape, and color instead of filling regions.

## Symbols decouple value from geographic region size <!-- role: reason -->

By using overlays, the viewer’s judgment is less influenced by the land area of a region, and additional variables can be encoded with symbol properties.

**Mechanism:** A symbol layer creates a separate mark whose visual properties carry the data, reducing reliance on irregular region boundaries as the primary carrier.

**Evidence:** Graduated symbol maps avoid confounding geographic area with data values and allow more dimensions to be visualized using symbol size, shape, and color, including more complex glyphs such as pie charts [@heerTourVisualizationZoo2010].

**Notes:** Complex glyphs increase information but also decoding effort.

## Context: Multivariate region summaries <!-- role: context -->

- **User Goal:** Compare magnitudes across regions while optionally seeing composition.
- **Task:** Identify large values and differences between regions.
- **Data:** Region-based aggregates, possibly with multiple subcomponents per region.
- **Chart Setting:** Map view where overlay clutter can be managed (zoom, filtering, or sparse symbols).
- **Audience:** General audiences if symbols are simple; expert audiences for complex glyphs.
- **Success Criterion:** Viewers can compare regions without being biased by region land area.

## Exceptions: When overlays would be illegible <!-- role: exceptions -->

**Break it when:** The map is too dense for symbols to be distinguishable without heavy overlap. **Why:** Symbol occlusion can prevent reliable comparison even if area confounding is reduced [@heerTourVisualizationZoo2010].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Symbol overlays can clutter the map, especially for small regions or dense geographies. **Risk:** Overplotting and occlusion can hide small values. **Mitigation:** Use interaction to filter, zoom, or simplify glyphs.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Using complex glyphs (such as pies) at sizes too small to read. **Why it fails:** Additional dimensions become visually noisy and stop supporting comparison [@heerTourVisualizationZoo2010].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Many symbols overlap or cannot be individually selected/read. **Quick Check:** If multiple neighboring regions’ symbols touch at the default view, the design is likely too dense. **Stronger Test:** Ask viewers to compare two adjacent regions’ values; frequent “can’t tell” responses indicate clutter.

## Fix: What to do instead <!-- role: fix -->

- Reduce symbol complexity to a single sized mark when the map is dense.
- Add interaction to filter categories or show details on demand.
- Switch to a choropleth using normalized values when overlays are too cluttered.
- Use a cartogram when the key message depends on totals and space-filling emphasis.
