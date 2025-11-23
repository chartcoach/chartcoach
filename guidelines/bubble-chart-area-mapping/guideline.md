---
id: bubble-chart-area-mapping
title: Map Quantitative Values to Area, Not Radius
bibliography: references.bib
description: Ensures proportional shape comparisons by avoiding exponential visual
  exaggeration.
labels:
- chart:bubble
- visual:area
- visual:size
- task:compare
- impact:integrity
---

## The Rule <!-- role: advice -->
When using circles (or other shapes) to represent quantity, map the data value to the **area** of the shape, never the radius or diameter.

## The Logic <!-- role: reason -->
Mapping a linear data value to a linear visual attribute (radius) results in a quadratic increase in the visual mass (area). This creates **Message Exaggeration**, where users perceive differences as much larger than they truly are.
*   **The Principle:** Area Perception vs. Linear Scaling
*   **The Evidence:** @pandey_how_2015 demonstrated that "Area as Quantity" distortion (mapping to radius) caused participants to significantly overestimate the difference between two values compared to correct area mapping.

## Where to Apply <!-- role: context -->
*   **User Goal:** Assessing the relative size or magnitude of different entities.
*   **Data Type:** Quantitative values represented by 2D shapes.
*   **Audience:** Any audience interpreting bubble charts or map markers.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** None based on this study.
*   **Reason:** The distortion is mathematical and perceptual; creating a deceptive visualization leads to demonstrable misinterpretation of the data.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Large values grow more slowly visually. An area-mapped bubble needs 4x the data value to look 2x as wide.
*   **The Risk:** Extreme outliers might not look as "dramatic" as a designer might want them to appear.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using 2D icons (like houses or dollar signs) and scaling them by height.
*   **Why it fails:** This introduces the same error as radius scaling—the area increases exponentially relative to the height, exaggerating the difference.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does a bubble representing "20" look four times as big as a bubble representing "10"? (It should only look twice as big).
*   **The Test:** Check the software settings or code. Ensure the scaling function targets `area` (or square root of data for radius calculation).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the encoding setting in your visualization tool from "Radius/Diameter" to "Area."
*   **Best Fix:** If precision is required, use a bar chart instead of a bubble chart, as length is judged more accurately than area.
