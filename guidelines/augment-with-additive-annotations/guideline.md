---
id: augment-with-additive-annotations
title: Augment maps with additive annotations
bibliography: references.bib
description: Use text annotations to add external context rather than just labeling
  visible data extremes.
labels:
- chart:map
- visual:text
- task:annotate
- impact:context
- data:textual
---

## The Rule <!-- role: advice -->
Supplement visualizations with "additive" annotations—information drawn from related sources that provides context not present in the chart data itself—rather than relying solely on "observational" annotations (like min/max labels).

## The Logic <!-- role: reason -->
While observational annotations (pointing out the highest value) are common, they often only state the obvious. Additive annotations deepen the narrative by explaining *why* a region might have a certain value or connecting it to broader trends. NewsViews retrieves headlines from *other* articles related to the map's locations and places them on the map to provide a "more tangible depiction of trends" [@gao_newsviews_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Gaining deeper insight or explanation for the patterns seen on a map.
*   **Data Type:** Thematic maps accompanying news articles or reports.
*   **Audience:** Readers looking for the "why" behind the data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The visualization is meant for rapid, at-a-glance reading of values only.
*   **Reason:** External text adds cognitive load and clutter that may distract from a pure data retrieval task.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate and visual simplicity.
*   **The Risk:** If the additive context is poorly selected (low relevance), it distracts from the main story.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Only labeling the "outliers" (highest and lowest values) with their numerical values.
*   **Why it fails:** This is "observational" use; it highlights data points but fails to add the narrative context that helps explain the data [@gao_newsviews_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** All text labels on the chart simply repeat the numbers already encoded by the visual variables (e.g., "15%").
*   **The Test:** Remove the annotations. Does the user lose any *contextual* knowledge, or just specific precision? If they only lose precision, the annotations are observational, not additive.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually write one annotation explaining a trend found in the map.
*   **Best Fix:** query a document corpus for related events or news items concerning the locations shown and place those headlines/summaries as annotations on the map.
