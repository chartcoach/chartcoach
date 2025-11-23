---
id: highlight-only-key-categories
title: Emphasize Key Categories and Gray Out the Rest
bibliography: references.bib
description: Reduce color usage by highlighting only the most relevant data points
  and letting others recede.
labels:
- chart:line
- chart:bar
- task:storytelling
- visual:color
- visual:contrast
---

## The Rule <!-- role: advice -->
Do not attempt to give every category equal visual weight. Identify the most important data points—the evidence for your statement—and color them boldly. Color all remaining categories in neutral greys or reduce their opacity.

## The Logic <!-- role: reason -->
Data visualization is often about communicating specific insights rather than just displaying raw data. By visually emphasizing only the categories relevant to the story (e.g., "Where is the evidence for the statement I want to make?"), you guide the reader's eye effectively. This reduces the cognitive load required to process a legend with many colors [@muth_fewer_colors_2022].

## Where to Apply <!-- role: context -->
*   **User Goal:** Communicating a specific insight, report, or narrative (e.g., "Our sales dropped, while competitors rose").
*   **Data Type:** Charts with many categories (lines or bars) where coloring all of them creates a "spaghetti" or "confetti" effect.
*   **Audience:** Readers looking for a takeaway message rather than an exploratory tool.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Exploratory dashboards.
*   **Reason:** If the user needs to look up any random category on equal footing, emphasizing one biases the tool and hides the others.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Contextual categories become harder to identify individually (often just becoming "the background noise").
*   **The Risk:** You might hide a relevant outlier by grouping it into the gray background mass.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Highlighting too many categories (e.g., highlighting 5 out of 7 lines).
*   **Why it fails:** If everything is emphasized, nothing is emphasized. You return to the problem of too many colors.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there more colorful elements than gray elements?
*   **The Test:** Ask: "If I had to remove categories one by one, which would be the one(s) I remove last?" Color only those [@muth_fewer_colors_2022].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Turn the saturation down to 0 for all categories except your primary subject.
*   **Best Fix:** Use a bold color for the main subject, a darker gray for meaningful context/comparison, and a light gray/low opacity for the rest.
