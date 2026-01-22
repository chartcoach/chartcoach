---
id: place-map-annotations-using-a-non-overlapping-layout-constrained-by-available-screen-space
title: Place map annotations using a non-overlapping layout constrained by available
  screen space
bibliography: references.bib
description: "Arrange annotation boxes so they do not overlap and fit within the map\u2019\
  s available space."
labels:
- chart:map
- task:annotate
- visual:layout
- impact:readability
- data:geospatial
- audience:novice
- pipeline:annotation-placement
---

## Prevent annotation overlap with a placement algorithm <!-- role: advice -->

Place annotation text boxes using a layout algorithm that avoids overlap and respects the map’s available screen space constraints.

## Why non-overlapping annotations preserve readability <!-- role: reason -->

Overlapping callouts obscure both the map and the text, degrading comprehension and interaction. An explicit placement step makes annotations legible while keeping the map visible enough to interpret patterns.

**Mechanism:** Constraint-based layout reduces occlusion, allowing readers to associate each annotation with its geographic target without visual interference.

**Evidence:** The pipeline uses a custom placement algorithm to match annotation realizations (including text box parameters) to available screen space so annotations can be placed without overlap [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** This is orthogonal to choosing which annotations to include.

## When non-overlapping placement applies <!-- role: context -->

- **User Goal:** Read map callouts while still seeing the underlying geography/data.
- **Task:** Associate each callout with a location and keep the map legible.
- **Data:** A small set of annotation candidates tied to locations.
- **Chart Setting:** Limited screen space; annotations rendered as text boxes on/near the map.
- **Audience:** General readers; low patience for cluttered visuals.
- **Success Criterion:** Callouts are readable and do not hide key regions.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization is purely a reference map with simple place markers and no text boxes. **Why:** Overlap-avoiding text-box layout is unnecessary without boxed annotations.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** May limit the number of annotations that can be shown at once. **Risk:** Aggressive collision avoidance can push annotations far from their targets, weakening association. **Mitigation:** Keep the annotation count small and prefer the most relevant ones.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding multiple callouts without accounting for collisions. **Why it fails:** Occlusion increases and the visualization becomes unreadable.

## Quick tests <!-- role: check -->

**Failure Sign:** Any annotation box covers another annotation or hides a large portion of the map. **Quick Check:** Run an overlap detection check on rendered bounding boxes. **Stronger Test:** Ask users to match callouts to locations and measure errors/time.

## What to do instead <!-- role: fix -->

- Reduce the number of simultaneous annotations to fit the available area.
- Use shorter extracted sentences so boxes occupy less space.
- Provide interaction to reveal additional annotations on demand rather than showing all at once.
