---
id: ensure-minimum-text-size
title: Set Minimum Text Size to 9 Points
bibliography: references.bib
description: Ensure all textual content in visualizations is at least 9pt (12px) to
  maintain legibility for users with low vision.
labels:
- impact:accessibility
- impact:legibility
- visual:text
- visual:size
- audience:low-vision
- chart:any
---

## The Rule <!-- role: advice -->
Render all text within the visualization at a minimum size of 9pt (approximately 12px). Reserve this minimum size only for minor elements, such as axis labels, ensuring that primary content is rendered larger.

## The Logic <!-- role: reason -->
Text size is a fundamental component of the "Perceivable" accessibility principle. While current standards like WCAG 2.1 do not have an absolute size requirement, research supports specific thresholds for legibility.

*   **The Principle:** Visual Acuity and Discriminability.
*   **The Evidence:** Text smaller than approximately 9pt (12px) significantly reduces readability and reading speed [@arditi_rethinking_ada_2017]. Consequently, the Chartability framework identifies violations of this size threshold as a critical failure in the heuristic evaluation of data interfaces [@elavsky_how_2022]. Furthermore, emerging work for future standards (WCAG 3.0) aims to integrate contrast evaluation with size, recognizing that size directly affects color discriminability [@elavsky_how_2022].

## Where to Apply <!-- role: context -->
This guideline applies to all information-rich systems where text is used to convey meaning.

*   **User Goal:** Reading data values, understanding axis scales, and interpreting annotations.
*   **Data Type:** Any visualization containing text (e.g., titles, labels, legends, tooltips).
*   **Audience:** All users, particularly those with low vision or visual impairments.

## When to Break It <!-- role: exceptions -->
As this is classified as a "Critical" heuristic within the Chartability framework, exceptions are rare for informational text.

*   **Scenario:** Non-informational textures or purely decorative patterns.
*   **Reason:** If the visual element does not convey data or semantic meaning required for understanding the chart, the strict legibility requirements for text may not apply.

## The Price <!-- role: costs -->
Increasing text size impacts the spatial layout of the visualization.

*   **The Sacrifice:** Screen real estate. Larger text requires more space, which may reduce the area available for the graphical representation of data.
*   **The Risk:** Overcrowding or occlusion. On high-density charts, larger labels may overlap or require aggressive occlusion culling (hiding labels), potentially obscuring data points.

## Common Mistakes <!-- role: mistakes -->
Practitioners often treat the minimum as the target rather than the floor.

*   **The Wrong Fix:** Setting *all* text to 9pt/12px.
*   **Why it fails:** The guideline suggests that the minimum size be used *only* for minor text. Using the minimum size for everything destroys visual hierarchy and makes the chart difficult to scan [@elavsky_how_2022].

## How to Check <!-- role: check -->
Testing for font size is complex because it is difficult to measure visually if the values are not explicitly known.

*   **Visual Sign:** Text appears difficult to read without squinting or zooming.
*   **The Test:** Inspect the code or design file directly. Verify that the CSS `font-size` or SVG text attributes are not set below 12px (or 9pt). Do not rely solely on visual estimation [@elavsky_how_2022].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Update the global style settings to ensure the base font size is at least 12px.
*   **Best Fix:** Implement a typographic scale where axis labels sit at the 12px minimum, while titles, annotations, and data labels use progressively larger sizes to ensure both accessibility and clear information hierarchy [@elavsky_how_2022].
