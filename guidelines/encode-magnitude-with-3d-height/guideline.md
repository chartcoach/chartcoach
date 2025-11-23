---
id: encode-magnitude-with-3d-height
title: Encode Magnitude with 3D Height Instead of 2D Area
bibliography: references.bib
description: Use 3D vertical extrusion (pins/bars) to represent quantities on maps
  or grids to improve discrimination and anchor points.
labels:
- chart:map
- chart:bar
- visual:length
- visual:position
- task:compare
- data:geospatial
- impact:clarity
---

## The Rule <!-- role: advice -->
When plotting quantities on a dense map or grid, extrude data points into vertical 3D pins or bars rather than using 2D circles (area) or color (hue/brightness).

## The Logic <!-- role: reason -->
3D extrusion utilizes **position and length** on a unified scale, which are perceptually more accurate than area or color.
*   **The Principle:** Length estimation has a lower error rate than area or hue estimation. 3D height offers a greater dynamic range than 2D brightness (which may only have 2-5 discriminable levels) or area.
*   **The Evidence:** According to [@brath_3d_2014], users can accurately estimate and compare the heights of 3D columns (e.g., Boston vs. New York), whereas 2D circles suffer from higher error rates in size estimation. Additionally, 3D pins provide an unambiguous anchor point on the map, whereas the center of a large 2D bubble can be hard to locate in dense regions.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing values with wide variations (large vs. small) while maintaining precise location.
*   **Data Type:** Geospatial data or dense grids with quantitative counts.
*   **Audience:** Users needing to identify outliers and precise locations simultaneously.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset is dense and uniform (low variance) without "long-tail" characteristics.
*   **Reason:** If all bars are of similar medium height, occlusion prevents reading the data behind them. 3D works best when the data has a "long tail" (few tall outliers, many small items) [@brath_3d_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You introduce occlusion (objects blocking each other).
*   **The Risk:** Users may struggle to see smaller data points located immediately behind larger ones if the view angle is not adjustable.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using 2D bubbles with transparency to handle overlap.
*   **Why it fails:** It muddies the visual signal and makes the "anchor point" (the specific location of the data) ambiguous for large bubbles [@brath_3d_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using circles that overlap so much the map underneath is invisible?
*   **The Test:** Check if you can pinpoint the exact geographic center of your largest data point. If not, consider a 3D pin.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch circle size encoding to vertical line height.
*   **Best Fix:** Implement a "pin map" where height encodes value, ensuring the base of the pin touches the exact data location.
