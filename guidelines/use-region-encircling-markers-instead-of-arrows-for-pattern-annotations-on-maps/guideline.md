---
id: use-region-encircling-markers-instead-of-arrows-for-pattern-annotations-on-maps
title: Encircle Regions Instead of Pointing with Arrows
bibliography: references.bib
description: When annotations describe regional patterns, connect them with circles
  rather than arrows to reduce clutter and overemphasis.
labels:
- chart:map
- task:annotate
- visual:shape
- impact:clarity
- data:geospatial
- audience:general
- complexity:intermediate
- source:datawrapper-fix-my-chart
---

## The Rule <!-- role: advice -->

If your annotation describes a regional pattern (not a single point), connect it to the map with a circle/encircling marker rather than an arrow.

## The Logic <!-- role: reason -->

Arrows imply a precise target and add directional visual weight; encircling marks better match “area/pattern” claims and reduce the sense that text is shouting over the map—an explicit change recommended in [@mintzer_map_annotations_2024].

- **The Principle:** Match annotation connectors to what you’re referencing (point vs. region)
- **The Evidence:** [@mintzer_map_annotations_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand broad geographic patterns (clusters, sparse regions, regional contrasts)
- **Data Type:** Point/dot distribution map with many marks where exact individual points aren’t the story
- **Audience:** General readers scanning for takeaways

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must identify a specific facility/location or a single standout point
- **Reason:** A circle can be ambiguous about which exact mark is being referenced; a precise pointer may be necessary.

## The Price <!-- role: costs -->

- **The Sacrifice:** Less precision about the exact point being referenced.
- **The Risk:** Overly large circles can cover data marks and create new clutter if not sized carefully.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using arrows for everything (including area-level statements like “the plains get the most wind”).
- **Why it fails:** The connector style conflicts with the message (pattern vs. point) and adds unnecessary visual emphasis, the kind of clutter problem addressed in [@mintzer_map_annotations_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Your annotation feels like it’s “accusing” a single spot even though the text is about a region.
- **The Test:** Replace an arrow with a circle; if the statement suddenly reads more honestly and the map feels calmer, the arrow was the wrong connector.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert arrows to circles for any annotation that references an area, band, corridor, or cluster.
- **Best Fix:** Audit each annotation: use circles for regional patterns and reserve precise pointers only for truly point-specific claims, as in [@mintzer_map_annotations_2024].
