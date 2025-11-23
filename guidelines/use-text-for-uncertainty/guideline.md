---
id: use-text-for-uncertainty
title: Use Text to Explain Uncertainty for Lay Audiences
bibliography: references.bib
description: For general audiences, textual annotations describing uncertainty can
  be more effective than complex visual error bars.
labels:
- visual:annotation
- data:uncertainty
- audience:novice
- impact:clarity
---

## The Rule <!-- role: advice -->
Use explicit textual annotations (e.g., "forecast," "leap-of-faith," "margin of error") to communicate uncertainty, rather than relying solely on visual encodings like error bars or confidence envelopes.

## The Logic <!-- role: reason -->
The analysis of narrative visualizations suggests a "dominance of textual uncertainty representations" over visual ones. This reliance on text indicates that standard visual codes for uncertainty (like error bars) are often not understood by non-experts. Textual rhetoric effectively signals the "inferential limits" of the data without requiring the user to decode complex statistical graphics [@hullman_visualization_2011].

## Where to Apply <!-- role: context -->
*   **User Goal:** conveying that data is an estimate or prediction.
*   **Data Type:** Forecasts, extrapolations, or survey data with margins of error.
*   **Audience:** Mass media consumers or non-statisticians.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Scientific publications or expert dashboards.
*   **Reason:** Experts prefer and expect precise visual quantification of uncertainty (error bars, box plots).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision.
*   **The Risk:** Text is qualitative; it may not convey the *magnitude* of the uncertainty as roughly as a visual range would.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding complex "fuzzy" borders or gradient shading to bars.
*   **Why it fails:** These "obscuring" techniques can violate discriminability limits and may simply look like bad design to a lay user [@hullman_visualization_2011].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there error bars?
*   **The Test:** If you remove the error bars, does the title or subtitle still warn the user that the data is an estimate?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a subtitle: "Data is estimated."
*   **Best Fix:** Annotate the specific part of the line graph where data turns into prediction with a label like "Forecast" or "Projected."
