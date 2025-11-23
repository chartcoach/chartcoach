---
id: use-whitespace-to-separate-topics
title: Separate Topics with White Space
bibliography: references.bib
description: Use clear whitespace gaps to define topic zones in text visualizations.
labels:
- chart:word-cloud
- task:segment
- visual:position
- impact:readability
- data:text
- audience:novice
---

## The Rule <!-- role: advice -->
Introduce white space gaps between groups of related words. Avoid "tight packing" algorithms that eliminate negative space between distinct semantic clusters.

## The Logic <!-- role: reason -->
White space provides a clear visual boundary that reduces the cognitive load required to segment groups. While spatial proximity (clustering) helps, explicit white space separation performs best for analytic tasks.
*   **The Principle:** Proximity and Region (Gestalt)
*   **The Evidence:** Layouts with whitespace separators (Column layouts) led to significantly stronger understanding of underlying topics compared to tightly packed layouts (like Seam Carving or Wordle), even when the tightly packed layouts were semantically sorted [@hearst_evaluation_2020].

## Where to Apply <!-- role: context -->
*   **User Goal:** Analytic tasks such as summarizing or gisting documents.
*   **Data Type:** Text data grouped into specific categories.
*   **Audience:** Users evaluating content for information (e.g., deciding whether to take a course based on a syllabus word cloud).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Limited Screen Real Estate.
*   **Reason:** If space is extremely constrained (e.g., a small mobile thumbnail), the white space required for column/separated layouts might force font sizes to become unreadably small.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Density. You fit fewer words per square inch compared to standard word cloud algorithms.
*   **The Risk:** The design looks less "organic" and more structured, which some designers fear looks "boring" (though evidence suggests users prefer the structured look for analysis).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using lines or borders to separate tightly packed words without adding padding.
*   **Why it fails:** Visual clutter increases. White space is a more effective and cleaner separator than ink-based boundaries [@hearst_evaluation_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the visualization look like a single solid block of text?
*   **The Test:** Squint at the image. Can you still see distinct "blobs" or columns, or does it merge into one shape?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the padding parameters in your force-directed layout or word placement algorithm.
*   **Best Fix:** Switch to a layout that explicitly designates regions (columns, radial segments) and reserves space between them.
