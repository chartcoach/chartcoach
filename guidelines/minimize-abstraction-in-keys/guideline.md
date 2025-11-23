---
id: minimize-abstraction-in-keys
title: Label Keys with Direct Measures
bibliography: references.bib
description: Avoid abstract rating systems in legends; label colors with the direct
  underlying data values.
labels:
- visual:color
- visual:legend
- impact:readability
- data:quantitative
---

## The Rule <!-- role: advice -->
Cut out abstract rating systems (like star ratings) in your color key and explain the measure directly.

## The Logic <!-- role: reason -->
Using abstract categories (e.g., "5 Star" vs "1 Star") forces the reader to mentally translate the category back into the actual data (e.g., number of hot days). By labeling the color key with the direct measure (e.g., "Blue < 30 Summer Days"), you remove "one less layer of abstraction for readers to deal with" [@mintzer_fix_my_chart_text_elements_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** When the audience needs to understand the magnitude of the data, not just a ranking.
*   **Data Type:** Continuous or binned quantitative data (e.g., temperature days, dollar amounts).
*   **Audience:** Readers who need to verify the criteria behind a ranking.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the underlying metric is a complex composite index that is meaningless on its own.
*   **Reason:** If the metric is "arbitrary points calculated by an algorithm," a simplified Tier/Star rating might be the only understandable metric.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "shorthand" of a simple "Best to Worst" ranking.
*   **The Risk:** The legend may require more horizontal space to explain the bins (e.g., "Under 30 days of extreme heat").

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Creating a "Star System" based on data thresholds, then explaining the thresholds in a footnote.
*   **Why it fails:** It splits the information location. The reader looks at the map, sees a star, looks at the legend, then has to hunt in the footer to see what a star actually means.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does your legend use symbols or numbers (1-5) that do not appear in the raw data?
*   **The Test:** Ask "What does blue mean?" If the answer is "5 stars," you have an abstraction layer. If the answer is "Less than 30 hot days," you are direct.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Rename the legend labels from categories (Stars) to value ranges (30-40 days).
*   **Best Fix:** Define the bins in the legend clearly (e.g., "Blue <30 Summer Days. Red > 60 Summer Days") as seen in the source example [@mintzer_fix_my_chart_text_elements_2024].
