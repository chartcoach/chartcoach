---
id: use-flow-maps-to-encode-movement-with-multivariate-strokes
title: Use Flow Maps to Show Movement with Lines over Geography
bibliography: references.bib
description: Use flow maps to depict movement through space using line direction,
  thickness, and color.
labels:
- chart:map
- task:trace-flow
- visual:position
- impact:insight
- data:geospatial
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When visualizing movement through geography, draw flow lines on a map and encode attributes with direction, thickness, and color.

## The Logic <!-- role: reason -->

Flow lines can encode multiple dimensions at once (path, direction, magnitude, category), supporting interpretation of movement in space and implicitly in time; subtle geographic distortion may be used to accommodate or emphasize flows.

- **The Principle:** Layer multivariate movement encodings atop geographic reference
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand routes, directionality, and relative magnitude of movement
- **Data Type:** Origin-to-destination or path data tied to geography
- **Audience:** Broad audiences when well-labeled; analysts exploring routes

## When to Break It <!-- role: exceptions -->

- **Scenario:** The story is not about movement but about regional totals
- **Reason:** Flow encodings add unnecessary complexity compared to region-based mapping [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Visual simplicity; flows can clutter dense regions
- **The Risk:** Overlapping lines can obscure paths without careful design

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding movement only as points at origins/destinations
- **Why it fails:** You lose the path and directional cues central to flow interpretation [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can’t tell where movement goes or which routes dominate
- **The Test:** Ask “Can I trace the primary path and its direction at a glance?” If not, the flow encoding isn’t working [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase separation/clarity by adjusting stroke width and color encoding for key flows
- **Best Fix:** Redesign flows (including possible distortion/abstraction) to better accommodate and highlight movement patterns [@heerTourVisualizationZoo2010]
