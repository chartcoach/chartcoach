---
id: provide-underlying-data-table
title: Provide a Human-Readable Data Table
bibliography: references.bib
description: Ensure accessibility by providing a text-based table of the data underlying
  the visualization.
labels:
- impact:accessibility
- visual:text
- task:read
- audience:screen-reader-users
- data:tabular
---

## The Rule <!-- role: advice -->
Always provide a table containing the human-readable version of the data upon which the chart is based.

## The Logic <!-- role: reason -->
This requirement is based on the "Compromising" principle of accessibility, which focuses on understandable yet robust designs. It ensures transparency and tolerance by providing alternative information flows for users with disabilities and those using assistive technologies [@elavsky_how_2022].

*   **The Principle:** Transparency and Redundancy. Providing a table ensures that if the visual interface fails or is inaccessible to a specific user, the core information remains available.
*   **The Evidence:** Guidelines from the National Center for Accessible Media emphasize including data tables to make complex visuals understandable to blind readers [@wgbh_effective_practices_2].

## Where to Apply <!-- role: context -->
This heuristic applies to data-driven visualizations and interfaces audited for accessibility.

*   **User Goal:** To consume information through assistive technologies or to verify precise values not easily read from a visual graphic.
*   **Data Type:** Quantitative or categorical data represented visually.
*   **Audience:** Users with visual impairments, cognitive disabilities, or anyone needing raw data access.

## When to Break It <!-- role: exceptions -->
While this is a critical heuristic, there is a specific condition where a full table may be omitted.

*   **Scenario:** Simple or Text-Heavy Visuals.
*   **Reason:** A table may be excluded *only* if the chart title, summary, context, or annotations are sufficient at conveying *all* relevant information contained in the chart [@elavsky_how_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate. Tables can be space-consuming compared to the visualizations they support.
*   **The Risk:** Narrative Loss. A data table provides equivalent access to the *data*, but it does not provide an equivalent *narrative* or structural understanding to a visualization. It cannot represent relationships (like non-tabular structures) as effectively as the graphic [@elavsky_how_2022].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Replacing the chart entirely with a table to bypass accessibility difficulties (often to satisfy Section 508 compliance).
*   **Why it fails:** Chartability posits that a table is not an equivalent experience to a visualization. Having a table does not mean the chart itself can be left inaccessible; the chart provides structural relationships that the table does not [@elavsky_how_2022].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for a visible table adjacent to the chart or a clear UI element (like a button or link) that reveals the data.
*   **The Test:** Review the interface to ensure the raw data values are available in a structured, readable text format. If the table is missing, verify if the text summary fully explains every data point (which is rarely the case for complex data).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Append a standard HTML table below the visualization containing the dataset used to render the chart.
*   **Best Fix:** Integrate a toggle or view-switch that allows the user to swap between the visual representation and the tabular representation, ensuring the table is properly marked up for screen readers [@wgbh_effective_practices_3].
