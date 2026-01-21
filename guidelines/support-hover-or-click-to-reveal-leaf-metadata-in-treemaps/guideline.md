---
id: support-hover-or-click-to-reveal-leaf-metadata-in-treemaps
title: Reveal Item Details on Interaction Instead of Pre-Labeling
bibliography: references.bib
description: Use cursor-based interaction (e.g., click) to show filenames and metadata
  for treemap rectangles.
labels:
- chart:treemap
- task:inspect
- visual:interaction
- impact:usability
- data:hierarchical
- audience:novice
- source:shneiderman-1992
---

## The Rule <!-- role: advice -->

Let users point to a treemap rectangle and click (or otherwise interact) to display the item’s name and metadata (e.g., filename, extension, date) outside the rectangle.

## The Logic <!-- role: reason -->

Treemaps often contain many small regions that cannot be labeled without clutter; interaction provides on-demand details while preserving a clean overview.

- **The Principle:** Overview first, details on demand (via interaction)
- **The Evidence:** Shneiderman proposes moving a cursor onto a region and clicking to obtain filename and related information in a status line or near the cursor [@shneidermanTreeVisualizationTreemaps1992].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify what a particular rectangle represents after noticing its size/color.
- **Data Type:** Large sets of leaves (e.g., thousands of files) where labels won’t fit.
- **Audience:** Interactive system users exploring directories or other hierarchies.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The display is static (print) and interaction is impossible.
- **Reason:** The technique depends on cursor interaction to reveal names [@shneidermanTreeVisualizationTreemaps1992].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires interaction support and a dedicated place to show details.
- **The Risk:** Users may not discover the interaction without cues/instructions [@shneidermanTreeVisualizationTreemaps1992].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Trying to label every rectangle directly in the treemap.
- **Why it fails:** Small regions make text unreadable and add clutter, undermining the overview goal implied by Shneiderman’s approach [@shneidermanTreeVisualizationTreemaps1992].

## How to Check <!-- role: check -->

- **Visual Sign:** Labels overlap, are illegible, or dominate the visualization.
- **The Test:** Attempt to read names for small rectangles; if it’s not feasible, use on-demand detail instead.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a status line that updates with the rectangle’s metadata on click.
- **Best Fix:** Provide interactive operations (e.g., deletion/copying/marking) via pop-up menus tied to selected rectangles, as suggested [@shneidermanTreeVisualizationTreemaps1992].
