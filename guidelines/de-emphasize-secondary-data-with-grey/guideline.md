---
id: de-emphasize-secondary-data-with-grey
title: De-emphasize Secondary Data with Grey
bibliography: references.bib
description: Use grey to de-emphasize 'no data', 'misc', or context categories.
labels:
- visual:color
- impact:focus
- task:highlight
- visual:contrast
---

## The Rule <!-- role: advice -->
Use grey to color categories representing "no data," "miscellaneous," "others," or context data that is not the focus of the story.

## The Logic <!-- role: reason -->
In any color scale (categorical, sequential, or diverging), the goal is to direct attention. @muth_which_color_scale_2021 advises that grey effectively pushes elements to the background, ensuring they do not compete with the highlighted categories or value ranges that convey the main insight.

## Where to Apply <!-- role: context -->
*   **User Goal:** Telling a specific story or highlighting a specific data subset.
*   **Data Type:** Incomplete datasets ("no data") or high-cardinality categories where only a few matter.
*   **Audience:** Readers who need to focus on the signal, not the noise.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** "Others" is a dominant category.
*   **Reason:** If the "Miscellaneous" category is the largest or most significant part of the data, greying it out may hide the most important finding.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose detailed information about the specific makeup of the "greyed out" data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a low-saturation version of a main hue (e.g., pale blue) for "no data."
*   **Why it fails:** Readers may interpret this as a low value on the scale rather than an absence of data.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the "no data" region look like part of the sequential scale (e.g., very light blue)?
*   **The Test:** Ask a user what the grey area represents. If they say "zero," the design needs adjustment.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Use a neutral grey that is distinct from the color hues used in the main scale.
