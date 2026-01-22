---
id: support-hover-or-click-to-retrieve-item-details-in-treemaps
title: Provide hover or click lookup to retrieve item metadata from a treemap rectangle
bibliography: references.bib
description: Enable users to point at a treemap region and retrieve details such as
  name, type, date, or size without relying on labels inside rectangles.
labels:
- chart:treemap
- task:lookup
- visual:interaction
- impact:usability
- data:hierarchical
- audience:expert
- interaction:details-on-demand
---

## Add pointing-based detail lookup for treemap regions <!-- role: advice -->

Let users move a cursor to a treemap rectangle and click to reveal its filename or other metadata in a separate readout area (such as a status line or a pop-up near the cursor). Use this lookup as the primary way to access names when rectangles are too small for labels.

## Why details-on-demand complements dense space-filling layouts <!-- role: reason -->

Space-filling displays trade label space for global coverage, so item identification must be handled through interaction rather than embedded text. Point-and-reveal supports inspection and subsequent actions while preserving the overview.

**Mechanism:** Separating overview (area and color) from details (on demand) prevents clutter while still allowing precise identification of any selectable region.

**Evidence:** Retrieving filename, extension, date, and other details is supported by moving a cursor onto a region and clicking to show relevant information in a bottom line or near the cursor; follow-on operations like deletion or copying via pop-up menus are a natural extension [@shneidermanTreeVisualizationTreemaps1992].

**Notes:** This approach avoids requiring directory-style navigation that shows only one node at a time.

## When pointing-based lookup applies <!-- role: context -->

- **User Goal:** Identify a specific item after spotting it by size/color.
- **Task:** Inspect metadata, then act (delete, copy, mark).
- **Data:** Many leaves with names too long to fit in their rectangles.
- **Chart Setting:** Interactive screen-based treemap with mouse or pointer input.
- **Audience:** Users performing management tasks on hierarchical collections.
- **Success Criterion:** Any rectangle can be identified reliably without visual label clutter.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The output is static (print or screenshot) and cannot support interaction. **Why:** Users cannot access the required metadata without embedded labels or external tables.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Requires interaction support and event handling rather than pure rendering. **Risk:** Very small rectangles may be difficult to target, making lookup unreliable. **Mitigation:** Provide zooming or subtree selection so small targets become accessible.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Relying on text labels inside rectangles for identification at all scales. **Why it fails:** Labels become illegible or overlap as rectangles shrink.
- **Mistake:** Providing lookup but not indicating which rectangle is currently targeted. **Why it fails:** Users cannot confirm selection, especially in dense regions.

## Quick tests <!-- role: check -->

**Failure Sign:** Users repeatedly retrieve details for the wrong item or cannot select tiny items. **Quick Check:** Attempt to identify several small rectangles using the pointer; note mis-selections and time to success. **Stronger Test:** Run a short task where users must locate a specified file by attribute and confirm its metadata via lookup.

## What to do instead <!-- role: fix -->

- Add zooming to enlarge regions for accurate targeting and repeated inspection.
- Allow users to filter or select subdirectories to reduce density and improve hit targets.
- Provide a secondary list view synchronized with the treemap selection for exact item identification.
- Add a highlight outline on hover to confirm the rectangle being queried.
