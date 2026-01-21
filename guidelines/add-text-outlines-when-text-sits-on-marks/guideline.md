---
id: add-text-outlines-when-text-sits-on-marks
title: Outline Text Placed on Top of Chart Elements
bibliography: references.bib
description: Use a stroke (outline) around text to keep labels readable against gridlines,
  shapes, or other marks.
labels:
- chart:general
- task:label
- visual:text
- impact:accessibility
- data:general
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

When text sits on top of chart elements (including subtle gridlines), add a text outline (stroke), usually in the background color.

## The Logic <!-- role: reason -->

An outline separates letterforms from the underlying marks, improving contrast and preventing gridlines/shapes from visually cutting through text. This increases legibility without needing large opaque label boxes.

- **The Principle:** Increase local contrast at letter edges
- **The Evidence:** [@muth_text_in_data_visualizations_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Read labels/annotations placed directly on the data region
- **Data Type:** Dense charts/maps where labels overlay lines, bars, fills, or grids
- **Audience:** All; especially helpful when readers scan quickly and can’t pause to decipher text [@muth_text_in_data_visualizations_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The outline becomes visually dominant or makes thin type look fuzzy at small sizes.
  - **Reason:** The cure can become noise; you may need a different placement or less overlap instead [@muth_text_in_data_visualizations_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Slightly heavier text rendering; may change the visual style.
- **The Risk:** Over-thick outlines can reduce typographic elegance or interfere with small text [@muth_text_in_data_visualizations_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Leaving text directly on top of gridlines/marks with no separation.
  - **Why it fails:** Underlying lines visually slice the letters, reducing readability [@muth_text_in_data_visualizations_2022].
- **The Wrong Fix:** Using low-contrast text color to “blend” with the background.
  - **Why it fails:** Makes text harder to read; blending is the opposite of what overlay text needs [@muth_text_in_data_visualizations_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Letters intersect with gridlines/marks; parts of words disappear when you glance quickly.
- **The Test:** Toggle gridlines on/off mentally: if gridlines (or marks) would interfere with reading, add an outline or move the text [@muth_text_in_data_visualizations_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a thin outline in the chart background color around the text.
- **Best Fix:** Combine outlining with improved placement (avoid busiest regions) so the text needs only a subtle outline, not a thick halo [@muth_text_in_data_visualizations_2022].
