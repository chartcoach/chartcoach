---
id: define-metrics-and-variables
title: Define Metrics and Variables Clearly
bibliography: references.bib
description: Ensure all data sources, metrics, and calculations are explicitly defined
  near the visualization to prevent ambiguity.
labels:
- impact:clarity
- impact:accessibility
- visual:text
- task:interpret
- audience:general
---

## The Rule <!-- role: advice -->
Explicitly define all metadata, metrics, calculations, and variables used in the visualization. Place this information immediately adjacent to the chart—such as in the title, subtitle, or caption—rather than burying it in the surrounding body text.

## The Logic <!-- role: reason -->
Information presented without definition creates ambiguity and increases cognitive load. To minimize this load and ensure the chart does not mislead, the data and its source must be clearly identified. For users of assistive technologies, such as blind readers, defining variables and units is a critical component of making complex science content and diagrams understandable [@wgbh_effective_practices]. Explicit definitions ensure that the visualization supports the functional accessibility principle of being "Understandable" [@elavsky_how_2022].

## Where to Apply <!-- role: context -->
This advice applies to all data-driven interfaces, specifically:
*   **User Goal:** When the user needs to understand the specific nature, unit, or derivation of the data being presented.
*   **Data Type:** Any chart using calculated metrics, specific units of measurement, or scientific content [@wgbh_effective_practices].
*   **Audience:** All users, with specific importance for those using screen readers or audio descriptions to interpret the data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** There are no specific exceptions provided in the source material for data visualization contexts.
*   **Reason:** The guideline emphasizes that metrics must not be misleading or undefined to avoid "lying" to the user [@elavsky_how_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Dedicating space immediately surrounding the chart for textual explanations and definitions reduces the visual real estate available for the graphic itself.
*   **The Risk:** If not managed well, adding detailed definitions can increase visual clutter around the interface.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Explaining variables or metrics only in the body text of nearby paragraphs.
*   **Why it fails:** Users often scan visualizations independently of the text. If the definition is not convenient and close to the data interface, the user may miss it or struggle to retain the information while viewing the chart [@elavsky_how_2022].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for ambiguous axis labels (e.g., "Score," "Value") or data points without clear units.
*   **The Test:** Review the visualization in isolation from the article text. Can you identify exactly what the data represents, how it was calculated, and where it came from based *only* on the information provided in or immediately next to the graphic?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a clear subtitle or caption that defines the units and data sources.
*   **Best Fix:** In addition to visual labels, ensure the semantic description of the chart (for screen readers) includes definitions of variables, units, and metrics, and provide a summary of key trends [@wgbh_effective_practices].
