---
id: use-enclosure-circles-instead-of-arrows-for-regional-map-annotations
title: Use enclosure circles instead of arrows when annotations describe regional
  patterns
bibliography: references.bib
description: "Connect notes to geographic regions with circles when you\u2019re describing\
  \ patterns rather than pointing to single locations."
labels:
- chart:map
- task:explain
- visual:annotation
- impact:clarity
- data:geospatial
- audience:general
- annotation:enclosure
---

## Enclose regions with circles when the annotation is about an area, not a point <!-- role: advice -->

Use circles to connect annotations to the map when you are describing regional patterns rather than labeling a specific data point.

## Why enclosure matches “regional pattern” meaning <!-- role: reason -->

Arrows imply a precise target, which can feel mismatched when the message is “this area tends to have more of X” or “this region differs from another.” Enclosing an area with a circle communicates that the note applies broadly within a region and avoids the visual insistence of a pointer that suggests one exact location.

**Mechanism:** Enclosure signals grouping and scope, so readers interpret the annotation as describing an area-level pattern instead of searching for a single referenced mark.

**Evidence:** Circles were recommended over arrows specifically because the annotations were describing regional patterns instead of labeling specific points, improving the fit between annotation style and message [@mintzer_map_annotations_2024].

**Notes:** The circle is a visual “scope marker,” not a requirement to outline exact boundaries.

## When this applies to annotated maps <!-- role: context -->

- **User Goal:** Learn how the distribution differs across broad regions.
- **Task:** Link a note to a cluster, corridor, or region-wide pattern.
- **Data:** Many points/marks where no single mark is the focus.
- **Chart Setting:** Static or lightly interactive maps where annotation marks must stay legible.
- **Audience:** Readers scanning for patterns rather than looking up exact facilities/addresses.
- **Success Criterion:** Readers understand the geographic scope of each note without hunting for a single “target” point.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The annotation truly refers to a specific location, facility, or single standout mark. **Why:** A circle suggests an area-level claim and can mislead about the intended precision.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Exactness about which mark is being referenced. **Risk:** Circles can cover dense data and add visual weight if too large or too many are used. **Mitigation:** Keep enclosure marks light and limited so they indicate scope without obscuring the data.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using arrows to point into a dense cluster when the text describes a broad regional trend. **Why it fails:** The arrow suggests a single intended target, creating ambiguity and making the reader search for “the” point being indicated [@mintzer_map_annotations_2024].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers can’t tell what the arrow is pointing at, or they disagree about which mark is referenced. **Quick Check:** Remove the arrowhead; if the annotation still makes sense as an area claim, it should likely be an enclosure. **Stronger Test:** Ask a colleague what the note refers to; if they name a single point but you intended a region, switch to circles.

## What to do instead <!-- role: fix -->

- Replace arrows with simple enclosure circles around the region being described.
- Adjust circle size so it communicates scope without covering key clusters.
- Move the annotation text so it sits near, but not on top of, the densest data marks.
- If you must reference both a region and a specific outlier, split the message into two annotations with distinct connectors.
