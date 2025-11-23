---
id: levy-1996-3d-rendering-style
title: Render 3D Elements as Solid Volumes
bibliography: references.bib
description: When using 3D, users strongly prefer solid volume renderings over floating
  surfaces.
labels:
- visual:3d
- visual:volume
- visual:surface
- chart:bar
- chart:line
- impact:aesthetics
---

## The Rule <!-- role: advice -->
If you must use a 3-dimensional graph, render the data as solid objects with volume (filling the area to the axis) rather than as floating surfaces or ribbons.

## The Logic <!-- role: reason -->
Not all 3D effects are viewed equally. Users show a strong preference for "volume" graphs (which look like solid objects) over "surface" graphs (which look like ribbons floating in space).
*   **The Principle:** Ecological Validity.
*   **The Evidence:** @levy_gratuitous_1996 reports that subjects chose 3-D volume graphs significantly more often than 3-D surface graphs (90 to 41 in Experiment 1). The authors hypothesize that volume graphs more closely resemble real-world solid objects, making them easier to code in terms of visual schemas.

## Where to Apply <!-- role: context -->
This applies specifically when a designer has already decided to use a 3D perspective for line or bar charts.
*   **User Goal:** Creating a 3D chart that is aesthetically preferred and potentially more recognizable.
*   **Data Type:** 2D data rendered in 3D perspective.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Multiple data series need to be overlaid.
*   **Reason:** Solid volumes might occlude data behind them more severely than thin floating surfaces (though occlusion is a general risk of 3D).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Volume graphs use more "ink" or pixels than surface graphs.
*   **The Risk:** The added visual weight of the volume might distract from subtle changes in the data slope.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "ribbon" chart to show a line in 3D.
*   **Why it fails:** This creates a "surface" effect which was less preferred by subjects than the solid "volume" effect @levy_gratuitous_1996.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the data look like a piece of paper floating in the air (Surface) or a solid block sitting on the ground (Volume)?
*   **The Test:** Check if the area under the line or bar is filled in to create a solid block appearance.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the chart settings to "Area" or "Volume" mode rather than just "3D Line."
*   **Best Fix:** Ensure the 3D object looks like a physical structure with a base, as this aligns with the "volume" preference found in the study.
