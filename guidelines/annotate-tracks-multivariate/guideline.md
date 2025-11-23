---
id: annotate-tracks-multivariate
title: Annotate Ensemble Tracks with Multivariate Attributes
bibliography: references.bib
description: Directly encoding size and intensity on trajectory lines improves risk
  calibration.
labels:
- chart:map
- visual:color
- visual:size
- task:assess-risk
- impact:utility
- data:multivariate
---

## The Rule <!-- role: advice -->
Encode secondary attributes (such as intensity and size) directly onto the ensemble tracks using color segments and periodic glyphs, rather than relying on separate charts or text.

## The Logic <!-- role: reason -->
Users' damage estimates are heavily influenced by information about size and intensity. When these attributes are integrated directly into the spatial visualization (e.g., coloring the line for wind speed and placing circles for storm size), users can accurately calibrate risk assessments even with fewer tracks. Experimental results showed that a 15-track display *with* annotations performed comparably to a 63-track display *without* annotations in conveying spatial uncertainty, while maintaining a cleaner layout [@liu_visualizing_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Making complex decisions that require knowing "where," "when," and "how strong" simultaneously.
*   **Data Type:** Trajectory data with changing attributes along the path (e.g., hurricane wind speed and radius).
*   **Audience:** Emergency managers or the public needing actionable risk information.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-density displays (e.g., >50 tracks).
*   **Reason:** Annotations (especially size circles) will overlap significantly, creating an illegible blob of color and shapes. Annotations work best on a carefully selected, smaller subset of tracks (e.g., ~15) [@liu_visualizing_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You must severely reduce the number of tracks displayed to make room for the annotations.
*   **The Risk:** If the subset of tracks is not mathematically representative, the annotations may give a false sense of precision about specific locations.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a separate legend or text description for intensity while leaving the map lines uniform.
*   **Why it fails:** It forces the user to split attention and mentally integrate separate data sources, which is cognitively demanding and prone to error [@liu_visualizing_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the lines just simple distinct colors (e.g., to show different models) rather than encoding data values?
*   **The Test:** Can you determine the storm's intensity at "landfall" just by looking at the map location, or do you have to look up a time/table?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Color-code the track segments based on intensity thresholds.
*   **Best Fix:** Sample the ensemble to a clean subset (e.g., 15 tracks), color-code segments using discriminable categories (not continuous ramps), and place size-indicating glyphs at regular time intervals (e.g., every 12 hours) to avoid overlap [@liu_visualizing_2019].
