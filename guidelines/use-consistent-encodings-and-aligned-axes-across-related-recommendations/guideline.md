---
id: use-consistent-encodings-and-aligned-axes-across-related-recommendations
title: Keep Encodings Consistent Across Related Recommended Charts
bibliography: references.bib
description: Align axes and reuse visual mappings so effort interpreting one chart
  transfers to the next.
labels:
- chart:gallery
- task:compare
- visual:color
- impact:scannability
- data:multivariate
- audience:analyst
- system:layout
---

## The Rule <!-- role: advice -->

Across a recommendation gallery, keep axis positions aligned and reuse consistent visual encodings (e.g., the same color mapping for the same field) for related charts.

## The Logic <!-- role: reason -->

Voyager aims to promote reading multiple charts “in context” by aligning axes, using consistent colors for variables, and ordering related charts so interpretation transfers from one view to the next [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Reduce re-learning cost across small multiples
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare many recommended charts quickly
- **Data Type:** Repeated fields across multiple views (e.g., a selected variable appears in many suggestions)
- **Audience:** Analysts scanning galleries

## When to Break It <!-- role: exceptions -->

- **Scenario:** A different encoding is required to satisfy expressiveness constraints for a particular view.
- **Reason:** Validity may require changing the mapping or mark type.

## The Price <!-- role: costs -->

- **The Sacrifice:** Less flexibility to optimize each chart independently.
- **The Risk:** A globally consistent choice (e.g., a specific color palette) may be suboptimal for a specific chart’s structure.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reassigning colors or swapping axes unpredictably between adjacent recommendations.
- **Why it fails:** Users must repeatedly re-parse legends and axes, increasing cognitive load [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** The same variable appears with different colors or different axis placements across neighboring views.
- **The Test:** Hover/highlight a variable token and verify that all occurrences map consistently across the gallery.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Establish stable default mappings for each variable (position, color palette) and reuse them.
- **Best Fix:** Order and group charts with shared axes near each other and maintain consistent encodings within those groups [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
