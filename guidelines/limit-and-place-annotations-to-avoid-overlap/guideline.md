---
id: limit-and-place-annotations-to-avoid-overlap
title: Place Annotations to Avoid Overlap and Crowding
bibliography: references.bib
description: Use a placement strategy that fits annotations into available space without
  overlapping each other.
labels:
- chart:map
- task:annotate
- visual:layout
- impact:readability
- data:text
- audience:general
- domain:news
---

## The Rule <!-- role: advice -->

Constrain the number of annotations and place them using a layout/placement algorithm that prevents overlap and respects available screen space.

## The Logic <!-- role: reason -->

Overlapping callouts reduce legibility and can hide the underlying map, undermining the map’s role in communicating geographic patterns and context.

- **The Principle:** Spatial layout constraints for annotation readability
- **The Evidence:** [@gaoNewsViewsAutomatedPipeline2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Read annotations without losing the map pattern
- **Data Type:** Maps with multiple candidate annotated locations
- **Audience:** General news readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** Extremely sparse maps with one clear focal location
- **Reason:** Overlap is unlikely; heavy placement logic may be unnecessary [@gaoNewsViewsAutomatedPipeline2014]

## The Price <!-- role: costs -->

- **The Sacrifice:** Some relevant annotations will be omitted
- **The Risk:** Placement rules may prioritize layout over showing the most important locations [@gaoNewsViewsAutomatedPipeline2014]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing every retrieved annotation
- **Why it fails:** It creates clutter and makes both the map and annotations harder to read [@gaoNewsViewsAutomatedPipeline2014]

## How to Check <!-- role: check -->

- **Visual Sign:** Annotation boxes collide, cover each other, or occlude key regions of the map
- **The Test:** Scan for any overlaps at the default zoom; if overlaps exist, the placement rule has failed [@gaoNewsViewsAutomatedPipeline2014]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce annotation count (e.g., cap to a small number)
- **Best Fix:** Apply an overlap-avoiding placement algorithm that selects and positions annotations jointly under screen-space constraints [@gaoNewsViewsAutomatedPipeline2014]
