---
id: group-words-spatially-by-topic
title: Group Words Spatially by Topic
bibliography: references.bib
description: Arrange word clouds into spatially distinct zones based on semantic meaning
  rather than packing them tightly.
labels:
- chart:word-cloud
- task:summarize
- visual:position
- impact:comprehension
- data:text
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->
Organize words into spatially distinct zones (such as columns or clusters) based on their semantic category. Do not intermix words from different topics solely to achieve a compact or "playful" layout.

## The Logic <!-- role: reason -->
Standard word cloud algorithms (like Wordle) prioritize compactness, which forces the viewer to engage in "haphazard inspection" to find related concepts. Spatially grouping words allows the user to process information one category at a time, leveraging the eye's tendency to scan sequentially.
*   **The Principle:** Semantic Zoning
*   **The Evidence:** Controlled experiments showed that column-based layouts (where topics were spatially separated) significantly outperformed standard mixed layouts in topic identification tasks [@hearst_evaluation_2020]. Eye-tracking data confirmed that grouped layouts allow viewers to fixate within a single category before moving to the next, whereas mixed layouts cause erratic scanning [@hearst_evaluation_2020].

## Where to Apply <!-- role: context -->
*   **User Goal:** Analyzing text to understand underlying topics, gist, or summaries (e.g., analyzing survey feedback or document themes).
*   **Data Type:** Categorical text data where words belong to distinct semantic groups.
*   **Audience:** Users who need to extract information quickly rather than solve a visual puzzle.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Artistic Expression or Puzzles.
*   **Reason:** If the goal is to create a visual puzzle, enforce slow reading, or maximize "typographical liveliness" at the expense of data readability, a standard mixed layout may be appropriate [@hearst_evaluation_2020].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Compactness. Spatially grouped layouts often require more white space or specific aspect ratios compared to the tightly packed rectangles of standard word clouds.
*   **The Risk:** The resulting shape may look more like a list or a chart than a traditional "cloud," potentially reducing its novelty factor for some audiences.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Keeping a chaotic layout but using font size to emphasize topics.
*   **Why it fails:** Font size is typically interpreted as frequency or importance, not categorical relatedness. It does not help the user scan for semantic themes [@hearst_evaluation_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you draw a circle around a specific topic without catching words from other topics?
*   **The Test:** Ask a viewer to name the top 3 themes. If they have to scan the entire image multiple times to find related words, the spatial grouping is insufficient.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use a "Bubble Set" or "Seam Carving" layout algorithm that keeps related words adjacent, even if the overall shape is organic.
*   **Best Fix:** Use a columnar or radial layout where each topic has a dedicated, clearly defined region.
