---
id: group-categories-by-shared-color-and-separate-with-strokes
title: Group Categories with Shared Color and Separate Them with Strokes
bibliography: references.bib
description: Reduce the palette by giving related categories the same color while
  keeping individual segments visible via strokes.
labels:
- chart:treemap
- task:group
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Assign the same color to categories that belong to the same group, and use strokes (borders) to keep the individual categories visible and distinguishable.

## The Logic <!-- role: reason -->

This approach reduces the number of colors while still communicating how group totals are composed. Muth describes using strokes to separate same-colored parts so readers can see both grouping and individual pieces ([@muth_fewer_colors_2022]).

- **The Principle:** Encode grouping with color; encode individuation with separation.
- **The Evidence:** [@muth_fewer_colors_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Seeing grouped totals while still perceiving the constituent items.
- **Data Type:** Part-to-whole or packed layouts where many pieces must remain visible (e.g., treemaps, stacked segments).
- **Audience:** General audiences who need both group structure and composition.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The individual categories must be easily tracked/compared as separate entities.
- **Reason:** Same-colored categories are inherently harder to tell apart; strokes help but don’t fully replace distinct hues ([@muth_fewer_colors_2022]).

## The Price <!-- role: costs -->

- **The Sacrifice:** Immediate distinctness of each individual category.
- **The Risk:** If strokes are too subtle (or there are too many tiny pieces), categories can still visually merge ([@muth_fewer_colors_2022]).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using the same color for multiple categories without adding clear separation.
- **Why it fails:** Readers can’t see boundaries, so the chart becomes a solid block rather than many parts ([@muth_fewer_colors_2022]).

## How to Check <!-- role: check -->

- **Visual Sign:** Same-colored adjacent pieces visually fuse; boundaries are unclear.
- **The Test:** Zoom out or squint: if pieces of the same group become indistinguishable blobs, your separation cue is too weak ([@muth_fewer_colors_2022]).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a thin contrasting stroke around each piece.
- **Best Fix:** Use varying stroke strength (or spacing) to reinforce higher-level groups while still separating individual pieces, as in Muth’s examples ([@muth_fewer_colors_2022]).
