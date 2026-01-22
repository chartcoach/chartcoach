---
id: support-zoom-and-reflow-without-losing-chart-information
title: Support zoom and single-direction reflow without loss of chart information
  or functionality
bibliography: references.bib
description: Ensure the chart can be zoomed and reflowed without clipping, two-direction
  scrolling, or losing any meaningful content or interactions.
labels:
- chart:any
- task:any
- visual:any
- impact:accessibility
- data:any
- audience:all
- principle:flexible
- domain:datavis
---

## Support zoom and single-direction reflow for charts <!-- role: advice -->

Ensure the chart can be zoomed and that all text, geometries, and interactive elements scale appropriately. When zoomed or narrowed, reflow the chart so no meaningful information or functionality is clipped and users do not need to scroll in two directions.

## Why zoom + reflow must preserve meaning and operation <!-- role: reason -->

When users zoom or increase text size through user agents (browsers, operating systems, applications), the visualization must remain perceivable and operable in the new layout; otherwise, information becomes unreachable (clipped) or interactions become impractical (two-direction scrolling). Supporting reflow maintains access by adapting layout while preserving the same informational content and available controls across zoomed states.

**Mechanism:** Reflow keeps all chart content and controls within the viewport in a single reading direction so users can still perceive labels/values and operate interactions after scaling changes.

**Evidence:** Content must be presentable without loss of information or functionality when zoomed or viewed at narrow widths, and designs should avoid requiring horizontal scrolling by using responsive reflow behavior [@w3c_understanding_reflow]. This requirement is included as a Flexible accessibility heuristic for data visualizations to ensure user agent settings are respected across perceivability and operability needs [@elavskyHowAccessibleMy2022].

**Notes:** This guideline covers zoom behaviors that change text size and layout, not only full-page scaling, and it applies to both static and interactive visualization interfaces.

## Where zoom and reflow support is required <!-- role: context -->

- **User Goal:** Read chart labels/values and understand the visualization at increased magnification or larger text settings.
- **Task:** Access the same information and interactive functionality after zooming or narrowing the viewport.
- **Data:** Any dataset where labels, legends, annotations, axes, or controls are necessary to interpret or operate the visualization.
- **Chart Setting:** Web or app-based charts where users may zoom, change text size, or view on small/narrow screens and where responsive layout is possible.
- **Audience:** Users who rely on browser/OS/app zoom and text sizing, including people with low vision and users needing enlarged targets.
- **Success Criterion:** No meaningful chart content or control becomes hidden, clipped, or unreachable, and navigation does not require scrolling in two directions.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization is delivered in a fixed-layout medium where zoom and responsive reflow cannot be supported. **Why:** The required user-agent-driven resizing and reflow behavior cannot be implemented in that delivery format [@w3c_understanding_reflow; @elavskyHowAccessibleMy2022].

## Tradeoffs of supporting zoom + reflow <!-- role: costs -->

**Sacrifice:** Maintaining reflow can require additional responsive layout work and more design/testing time across viewport sizes and zoom states. **Risk:** Reflow may change spatial relationships and require redesigning legends, axes, or control placement to preserve meaning. **Mitigation:** Treat reflow states as first-class layouts and verify that the same information and operations remain available after rearrangement.

## Common ways teams fail zoom and reflow <!-- role: mistakes -->

- **Mistake:** Letting the chart container crop axes, legends, tooltips, or controls when zoomed. **Why it fails:** Meaningful information or functionality is lost, violating the requirement to preserve access under zoom/reflow [@w3c_understanding_reflow; @elavskyHowAccessibleMy2022].
- **Mistake:** Requiring both horizontal and vertical scrolling to read the chart after zooming. **Why it fails:** Two-direction navigation makes content effectively inaccessible and indicates reflow is not properly supported [@w3c_understanding_reflow; @elavskyHowAccessibleMy2022].
- **Mistake:** Scaling only some elements (for example, text) while marks/targets or interaction affordances do not scale appropriately. **Why it fails:** Users cannot reliably perceive labels or operate controls at the chosen zoom level, so functionality is not preserved [@elavskyHowAccessibleMy2022].

## Quick tests for zoom + reflow failures <!-- role: check -->

**Failure Sign:** After zooming or narrowing the viewport, parts of the chart (labels, legend, annotations, controls) are cut off or require both horizontal and vertical scrolling to access. **Quick Check:** Zoom the page and/or increase text size and confirm the chart still shows all meaningful content and controls without clipping. **Stronger Test:** Verify the visualization can be presented without loss of information or functionality at narrow widths and under zoom, and confirm users do not need two-direction scrolling to access content [@w3c_understanding_reflow; @elavskyHowAccessibleMy2022].

## Remediation actions for missing zoom + reflow support <!-- role: fix -->

- Make the chart layout responsive so legends, controls, and annotations reflow (wrap, stack, or move) instead of being clipped.
- Ensure text, marks, and interactive targets scale appropriately under user-agent zoom and text sizing so the same content remains perceivable and operable.
- Prevent two-direction scrolling by redesigning the chart container and internal layout so content fits in one scrolling direction after reflow.
- If the visualization cannot preserve meaning under reflow, provide an alternative presentation that retains the same information and functionality in the zoomed context.
