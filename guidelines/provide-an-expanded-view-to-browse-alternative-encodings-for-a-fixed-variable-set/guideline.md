---
id: provide-an-expanded-view-to-browse-alternative-encodings-for-a-fixed-variable-set
title: Provide an expanded view to browse alternative encodings for a fixed variable
  set
bibliography: references.bib
description: Let users drill down from a recommended chart to compare encoding variants
  for the same underlying data.
labels:
- chart:gallery
- task:refine
- visual:encoding
- impact:control
- data:tabular
- audience:expert
- system:mixed-initiative
---

## Let users expand a chart to explore multiple encodings of the same data <!-- role: advice -->

Provide an “expand” interaction that enlarges the selected chart and surfaces alternative encodings of the same variable set in a dedicated view.

## Drill-down supports depth without cluttering breadth-first browsing <!-- role: reason -->

A single default encoding is useful for scanning, but users often need to evaluate other encodings once they find a promising relationship. Separating “browse many data slices” from “compare encodings for one slice” supports both breadth and depth while keeping the main gallery scannable.

**Mechanism:** Two-level navigation (overview gallery → expanded encoding browser) matches shifting user goals from discovery to refinement.

**Evidence:** The interface design includes an expanded gallery that presents the selected chart at larger size and shows alternative encodings in a sidebar, enabling users to inspect different visual encodings for the same data [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

**Notes:** Expanded mode also creates room for interaction controls that are impractical in thumbnails.

## When users find a promising view and want to refine or compare it <!-- role: context -->

- **User Goal:** Explore different ways to visualize the same variables to better see structure or outliers.
- **Task:** Encoding comparison and view refinement after initial discovery.
- **Data:** A fixed set of variables and transformations.
- **Chart Setting:** A gallery-based recommender with small default thumbnails.
- **Audience:** Users transitioning from exploratory browsing to targeted inspection.
- **Success Criterion:** Users can quickly switch among encoding alternatives without rebuilding the chart manually.

## When an expanded encoding browser is less valuable <!-- role: exceptions -->

**Break it when:** The recommendation space for the selected data slice is already very small (for example, only one sensible encoding exists). **Why:** The expanded mode adds a step without providing meaningful alternatives [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Tradeoffs of adding an expanded mode <!-- role: costs -->

**Sacrifice:** Additional UI complexity and navigation state. **Risk:** Users may lose context of where the chart came from in the broader gallery. **Mitigation:** Keep a clear link back to the main gallery and maintain consistent variable labeling across views [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Common mistakes when adding drill-down <!-- role: mistakes -->

**Mistake:** Showing encoding alternatives directly in the main gallery instead of behind an expand action. **Why it fails:** It undermines breadth-first exploration by consuming gallery space with near-duplicates [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Quick checks for a useful expanded mode <!-- role: check -->

**Failure Sign:** Users repeatedly rebuild similar charts in a manual tool to try different encodings. **Quick Check:** From a chart in the main gallery, verify that expanded mode can show multiple distinct encodings for the same data. **Stronger Test:** Observe whether users use expanded mode to answer follow-up questions after discovering a pattern [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## What to do if expanded mode still feels limiting <!-- role: fix -->

- Add a thumbnail strip or sidebar that lists alternative encodings and allows one-click switching.
- Include lightweight refinement controls (for example, transpose, sort, scale toggle) in expanded mode.
- Preserve the selected view’s variable capsules and styling so users can compare alternatives without re-parsing labels [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
