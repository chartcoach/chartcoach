---
id: round-natural-breaks-with-custom-steps-to-improve-legend-readability
title: Round Breakpoints with Custom Steps
bibliography: references.bib
description: Use custom class breaks to turn hard-to-read (but useful) data-driven
  cut points into readable legend values with minimal change to the map.
labels:
- chart:choropleth
- task:label
- visual:color
- impact:readability
- data:quantitative
- audience:general
- complexity:advanced
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

When data-driven breaks (like Natural/Jenks) yield awkward numbers, use a custom interpolation to round breakpoints to readable values while keeping the map’s overall pattern nearly unchanged. [@muth_interpolation_2022]

## The Logic <!-- role: reason -->

Readers interpret legends faster when thresholds are simple; rounding preserves most classification intent while reducing cognitive friction from non-round numbers (e.g., 4.1 → 4, 5.7 → 6). [@muth_interpolation_2022]

- **The Principle:** Legend digestibility via readable thresholds
- **The Evidence:** [@muth_interpolation_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly understanding class boundaries from the legend
- **Data Type:** Classed color scales where computed breaks are non-round (often with skewed distributions)
- **Audience:** General audiences who rely on the legend for interpretation [@muth_interpolation_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** High-stakes contexts where even small threshold shifts are unacceptable.
- **Reason:** Rounding changes which regions fall into which bins (even if only slightly). [@muth_interpolation_2022]

## The Price <!-- role: costs -->

- **The Sacrifice:** Mathematical precision in class boundaries.
- **The Risk:** Slight reclassification can affect a few regions and potentially alter edge-case interpretations. [@muth_interpolation_2022]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Arbitrarily choosing custom breaks without anchoring them to the data distribution.
- **Why it fails:** Custom steps can easily misrepresent the distribution and narrative if not derived from a defensible basis. [@muth_interpolation_2022]
- **The Wrong Fix:** Over-rounding into overly coarse bins.
- **Why it fails:** You may lose the improved pattern visibility that motivated Natural breaks in the first place. [@muth_interpolation_2022]

## How to Check <!-- role: check -->

- **Visual Sign:** Legend breakpoints are hard to read or explain (many decimals), even though the map looks good.
- **The Test:** Compare the map before/after rounding and look for noticeable pattern shifts; if differences are barely visible, rounding succeeded. [@muth_interpolation_2022]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Round each Natural breakpoint to the nearest clean number and re-check which regions change class. [@muth_interpolation_2022]
- **Best Fix:** Start from Natural breaks, then iteratively adjust custom thresholds to maximize legend readability while minimizing changes in the spatial pattern and story. [@muth_interpolation_2022]
