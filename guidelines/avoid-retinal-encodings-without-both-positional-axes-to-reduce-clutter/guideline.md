---
id: avoid-retinal-encodings-without-both-positional-axes-to-reduce-clutter
title: Use Retinal Encodings Only When Both Axes Are Present
bibliography: references.bib
description: Skip recommendations that add color/size/shape to dot plots lacking both
  x and y to prevent occlusion and clutter.
labels:
- chart:dot-plot
- task:explore
- visual:color
- impact:clarity
- data:categorical
- audience:analyst
- system:recommendation
---

## The Rule <!-- role: advice -->

Only recommend color/size/shape encodings when the chart uses both x and y; avoid retinal-encoded dot plots that have just one positional axis.

## The Logic <!-- role: reason -->

Compass avoids creating ineffective charts by omitting mappings that encode color, size, or shape unless both x and y are present, because single-axis dot plots with these encodings are likely to suffer from occlusion and visual clutter [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Prevent clutter and occlusion in constrained layouts
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly interpret recommended plots in a gallery
- **Data Type:** Mappings that would otherwise create one-dimensional dot plots
- **Audience:** Analysts browsing many small charts

## When to Break It <!-- role: exceptions -->

- **Scenario:** The system supports an alternative non-occluding 1D design for multi-category encodings (not described in Voyager/Compass).
- **Reason:** The stated guidance is tied to Compass’s chart forms and occlusion concerns.

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer 1D chart variants that attempt to show multiple dimensions.
- **The Risk:** Users may need to use aggregation/faceting instead to see subgroup structure.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding color to a 1D strip plot to “show categories.”
- **Why it fails:** Marks overlap and become hard to parse, especially at thumbnail sizes [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Many points overlap into indistinguishable blobs in single-axis plots.
- **The Test:** If category differences can’t be reliably discriminated without interaction, the encoding is too cluttered for a gallery.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Require both x and y before allowing retinal encodings in generated candidates.
- **Best Fix:** Use faceting (row/column) or aggregation/binning to produce clearer subgroup summaries instead of cluttered 1D plots [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
