---
id: increase-spacing-for-long-text-labels
title: Standardize Spacing in Tag Clouds
bibliography: references.bib
description: Longer words bias users toward perceiving higher quantities; increased
  spacing reduces this error.
labels:
- chart:text
- chart:tag-cloud
- visual:layout
- task:estimate
- impact:bias
- data:text
---

## The Rule <!-- role: advice -->
When visualizing text data where quantity is encoded (e.g., colored words), increase the spacing between letters in short words or spacing between words to normalize overall length.

## The Logic <!-- role: reason -->
Users estimating the numerosity of text elements are biased by the total area or length of the words. Longer words bias viewers toward perceiving a higher quantity of items. Adjusting spacing helps separate the visual signal of "length" from "count" [@szafir_four_2016].
*   **The Principle:** Area/Size Bias in Numerosity
*   **The Evidence:** Correll, Alexander, and Gleicher (2013) found that longer words biased viewers, and increasing spacing in short words improved estimation accuracy [@szafir_four_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating how frequently a category of words appears (e.g., "Are there more red words or blue words?").
*   **Data Type:** Tagged text, word clouds, or text corpora visualizations.
*   **Audience:** Analysts performing content analysis or "gist" extraction from text.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Standard reading is the primary goal.
*   **Reason:** Artificial spacing (kerning) reduces readability and reading speed.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Layout compactness and natural readability.
*   **The Risk:** The text becomes harder to read as a sentence or paragraph.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Simply coloring words in a standard paragraph block without adjusting layout.
*   **Why it fails:** Users will perceive the category with longer words (e.g., "philosophical") as more frequent than short words (e.g., "is", "at"), even if counts are identical.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do short words look much denser than long words?
*   **The Test:** Check if the visual "mass" of a category correlates with word length rather than word count.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use a monospaced font.
*   **Best Fix:** Algorithmically increase letter spacing for shorter words or padding around them to equalize the visual footprint of items.
