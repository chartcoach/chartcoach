---
id: preserve-consistent-encodings-and-ordering-across-related-charts-to-support-scanning
title: Preserve consistent encodings and ordering across related charts to support
  scanning
bibliography: references.bib
description: Keep axes, colors, and ordering consistent for the same variables across
  a gallery to make multi-chart reading easier.
labels:
- chart:gallery
- task:compare
- visual:color
- visual:position
- impact:scannability
- data:multivariate
- audience:novice
- system:recommendation
---

## Keep axis placement and variable-to-color mappings consistent across the gallery <!-- role: advice -->

When multiple charts include the same variables, use consistent axis assignments and consistent color mappings for those variables, and order related charts predictably to support rapid scanning.

## Consistency reduces re-learning costs across many small charts <!-- role: reason -->

In a gallery, users repeatedly parse axes, legends, and labels. Consistent encoding choices let users transfer understanding from one chart to the next, reducing cognitive overhead and improving comparative reading across multiple views.

**Mechanism:** Stable mappings reduce the need to re-interpret legends and axes, enabling faster pattern detection across charts.

**Evidence:** The gallery design aligns axes, uses consistent colors for variables, and orders related charts so effort spent interpreting one chart supports interpreting subsequent charts in context [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

**Notes:** This is about cross-chart consistency, not the optimal encoding for any single chart in isolation.

## When users must read many charts in a single session <!-- role: context -->

- **User Goal:** Scan and compare many related charts quickly.
- **Task:** Browsing and pattern recognition across multiple recommendations.
- **Data:** Repeated variables appearing across recommended views.
- **Chart Setting:** A scrolling gallery of small charts.
- **Audience:** Users who benefit from reduced cognitive load during scanning.
- **Success Criterion:** Users can interpret successive charts without repeatedly re-reading legends and axes.

## When strict consistency may be counterproductive <!-- role: exceptions -->

**Break it when:** A different encoding is required to satisfy expressiveness or to produce a valid chart for a particular transformation. **Why:** Consistency should not force an inappropriate mapping that makes a view misleading or invalid [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Tradeoffs of enforcing consistency <!-- role: costs -->

**Sacrifice:** Some charts may not use the locally optimal encoding if global consistency is prioritized. **Risk:** Over-standardization can reduce the perceived diversity of views. **Mitigation:** Keep consistency for shared variables while still allowing meaningful data variation across charts [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Common mistakes that hinder gallery scanning <!-- role: mistakes -->

**Mistake:** Remapping the same variable to different channels (or different colors) across adjacent charts. **Why it fails:** Users must re-parse the chart grammar each time, slowing comparison [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Quick checks for cross-chart consistency <!-- role: check -->

**Failure Sign:** Users repeatedly look for legends or misread which variable is on which axis. **Quick Check:** For a given variable, verify its assigned color (or axis role) is the same wherever it appears in the gallery. **Stronger Test:** Observe whether users can describe differences between two adjacent charts without referencing the legend each time [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## What to do if consistency conflicts with chart validity <!-- role: fix -->

- Prioritize expressiveness constraints first, then apply consistency within the remaining valid choices.
- Cluster and group charts so those with shared encodings appear near each other.
- Provide expanded mode for users to intentionally explore alternative encodings when needed [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
