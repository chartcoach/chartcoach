---
id: use-3d-when-height-avoids-2d-overplotting
title: Use 3D Height to Encode Counts When 2D Overplots
bibliography: references.bib
description: Encode counts as vertical height in 3D when a 2D map would suffer from
  overplotting or weak color/area discrimination.
labels:
- chart:map
- chart:bar
- task:compare
- task:rank
- visual:position
- visual:length
- impact:clarity
- data:geospatial
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Encode counts on a map as 3D vertical height (e.g., pins/bars) when 2D encodings would overplot or force you into hue/area encodings.

## The Logic <!-- role: reason -->

3D adds an extra positional dimension so you can use **length/height**, which supports more accurate relative estimation than hue/brightness or area, and it can reduce ambiguity in dense map regions by keeping an unambiguous anchor point at each location [@brath3DInfoVisHere2014].

- **The Principle:** Prefer position/length encodings; use the third dimension to avoid 2D overlap.
- **The Evidence:** [@brath3DInfoVisHere2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare magnitudes at many geographic locations, including small differences among smaller values.
- **Data Type:** Point-based geospatial counts, often long-tailed (a few tall stacks, many small ones).
- **Audience:** Analysts or viewers who need quick relative comparisons without heavy decoding.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your dataset produces heavy occlusion (many similarly tall bars close together).
- **Reason:** Occlusion can erode the benefit of 3D height and make comparisons unreliable [@brath3DInfoVisHere2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Increased perspective error vs a flat 2D baseline.
- **The Risk:** Tall marks can hide smaller marks behind them, especially without a favorable distribution [@brath3DInfoVisHere2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to 2D bubbles sized by area in dense regions.
- **Why it fails:** Area judgments are harder and overlapping circles can still occlude; center/anchor can be harder to infer in dense areas [@brath3DInfoVisHere2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Many locations disappear behind a few tall marks, or you can’t reliably compare smaller columns.
- **The Test:** Rotate slightly—if rankings among small values change dramatically with viewpoint, occlusion/perspective is dominating [@brath3DInfoVisHere2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Choose a viewpoint that minimizes self-occlusion for the region of interest.
- **Best Fix:** Restrict to datasets/views where occlusion remains low (e.g., long-tail patterns) or redesign the layout to reduce overlap [@brath3DInfoVisHere2014].
