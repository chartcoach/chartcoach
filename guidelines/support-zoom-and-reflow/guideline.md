---
id: support-zoom-and-reflow
title: Support Zoom and Reflow for Visualization Layouts
bibliography: references.bib
description: Ensure chart text and geometries resize and rearrange appropriately when
  users zoom in or change viewport sizes, avoiding data loss or two-dimensional scrolling.
labels:
- impact:accessibility
- impact:compliance
- visual:layout
- visual:geometry
- task:read
- audience:low-vision
---

## The Rule <!-- role: advice -->
Design data visualizations to support zooming and reflow capabilities provided by the user agent (browser) or assistive technology. Ensure that text, geometries, and interface elements change size appropriate to the zoom level, and that content reflows to fit the view without being cut off or requiring scrolling in two directions.

## The Logic <!-- role: reason -->
This guideline is rooted in the **Flexible** principle of the Chartability framework, which asserts that designs must respect user settings in lower-level systems (like browsers) and allow for robust user agency [@elavsky_how_2022].

*   **The Principle:** Flexibility and Robustness. Flexible heuristics demand a tight coupling between the data experience and the technological context, ensuring that preferences set by the user (such as zoom levels) are respected [@elavsky_how_2022].
*   **The Evidence:** WCAG criteria (1.4.4, 1.4.10, 1.4.12) require that content can be presented without loss of information or functionality when zoomed or viewed at a width of 320 CSS pixels [@w3c_understanding_reflow].

## Where to Apply <!-- role: context -->
This rule applies to all data-driven interfaces and visualizations, particularly in web environments.

*   **User Goal:** Reading text or perceiving small geometries when living with low vision, or when using mobile devices.
*   **Data Type:** All visual data representations, especially those with high information density requiring distinct labels and axes.
*   **Audience:** Users employing screen magnifiers, users with visual impairments, or users on small screens.

## When to Break It <!-- role: exceptions -->
While the source text emphasizes that designs must not be rigid, strict adherence to reflow might be challenged in specific technical constraints:

*   **Scenario:** When the loss of spatial relationship destroys the data's meaning.
*   **Reason:** The guideline notes that responsive design may need to *re-arrange* the display to ensure no meaningful information is lost [@elavsky_how_2022]. If re-arranging destroys the data integrity (e.g., a complex map where relative position is the only data encoding), 2D scrolling may be the only option, though this is suboptimal.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Implementing robust reflow often requires significant engineering effort to make SVG or Canvas elements responsive (e.g., dynamically reducing axis ticks or moving legends).
*   **The Risk:** If not implemented carefully, reflowing content can clutter the screen or disrupt the visual hierarchy intended by the designer.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Allowing the chart container to shrink while the internal SVG content remains static.
*   **Why it fails:** This results in content being "cut off from view in two directions" or clipped entirely, making the data inaccessible [@elavsky_how_2022].
*   **The Lazy Fix:** Relying solely on browser zoom without checking layout breaks.
*   **Why it fails:** Elements may overlap or obscure each other when text size increases but container size does not.

## How to Check <!-- role: check -->
*   **The Test:** Zoom the browser to 200% or 400%, or resize the window width to 320 CSS pixels.
*   **Visual Sign:** Check if any text or data points are clipped (cut off), or if you are forced to scroll both horizontally and vertically to read a single sentence or view a single data group [@elavsky_how_2022].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Ensure all containers use relative units (percentages, ems) rather than fixed pixels, allowing them to wrap naturally.
*   **Best Fix:** Implement responsive design logic that re-arranges the display (e.g., moving a legend from the side to the bottom, stacking side-by-side charts vertically) to ensure no meaningful information or functionality is lost during reflow [@elavsky_how_2022].
