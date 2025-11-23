---
id: ensure-minimum-target-size
title: Ensure Minimum Size for Interactive Targets
bibliography: references.bib
description: Interactive elements must be large enough to select easily, requiring
  a minimum target size of 24px x 24px or alternative selection methods.
labels:
- impact:accessibility
- impact:operability
- visual:geometry
- visual:size
- task:interaction
- task:selection
- audience:motor-impairment
---

## The Rule <!-- role: advice -->
Ensure that all interactive elements targeted by a mouse or touch pointer have a minimum size of at least 24px by 24px. If visual marks must be smaller due to data encoding, provide alternative mechanisms to select or activate the information.

## The Logic <!-- role: reason -->
This guideline ensures that users with limited dexterity, motor impairments, or imprecise input methods (like touch screens) can successfully activate controls without error.
*   **The Principle:** Operability and Error Tolerance.
*   **The Evidence:** This requirement is derived from the "Operable" category of the Chartability framework [@elavsky_how_2022] and aligns with W3C standards which state that controls must be large enough for users with limited dexterity [@w3c_understanding_target].

## Where to Apply <!-- role: context -->
This applies to any data-driven interface involving pointer interaction.
*   **User Goal:** Selecting, hovering, filtering, or activating specific data points.
*   **Data Type:** Visualizations using size or density to encode variables (e.g., scatterplots, maps, dot plots).
*   **Audience:** Users with motor, vestibular, and neurological disabilities, as well as users on mobile devices.

## When to Break It <!-- role: exceptions -->
While the interaction target size is a hard requirement for accessibility, the *visual* representation may need to be smaller.
*   **Scenario:** High-density visualizations where data points physically cannot be 24px wide without overlapping (e.g., a dense scatterplot).
*   **Reason:** While the *visual* mark must remain small to represent the data accurately, the *interaction* requirement must still be met through other means (see "How to Fix").

## The Price <!-- role: costs -->
*   **The Sacrifice:** Implementation complexity. Simply attaching an event listener to a small SVG circle is insufficient; developers must decouple the visual layer from the interaction layer or build auxiliary UI structures.
*   **The Risk:** A cluttered interface if designers attempt to force every visual mark to meet the 24px threshold rather than using invisible hit areas or alternative controls.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on Voronoi diagrams (tessellation) to expand hit areas.
*   **Why it fails:** While often cited as a solution, Voronoi diagrams "still pose significant operability barriers for people with motor impairments" regarding precision and predictability [@elavsky_how_2022].
*   **The Lazy Fix:** Scaling interaction zones directly to data values.
*   **Why it fails:** This results in targets that are physically too small to select when the data value is low [@elavsky_how_2022].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there tiny data points that require pixel-perfect precision to hover over or click?
*   **The Test:** Verify if the clickable area measures at least 24 CSS pixels on each side [@w3c_understanding_target].

## How to Fix <!-- role: fix -->
If the data visualization requires small marks, you must provide alternatives.
*   **Quick Fix:** Add invisible padding to the element to increase its hit area to 24px x 24px without changing its visual appearance.
*   **Best Fix:** Provide alternative interfaces for selection, such as text labels that meet minimum size, accompanying data tables, search functions, or features like zooming and filtering [@elavsky_how_2022].
*   **Robust Fix:** Ensure the element can be navigated and selected via keyboard or alternative inputs, bypassing the pointer requirement entirely [@elavsky_how_2022].
